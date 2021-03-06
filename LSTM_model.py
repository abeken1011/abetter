import re
import pickle
import torch
import torch.nn as nn
import MeCab

class SequenceGenerationNet(nn.Module):
  def __init__(self, num_embeddings, embedding_dim=50, hidden_size=50, num_layers=1, dropout=0.2):
    super().__init__()
    self.emb=nn.Embedding(num_embeddings, embedding_dim)
    self.lstm=nn.LSTM(embedding_dim, hidden_size, num_layers, batch_first=True, dropout=dropout)

    self.linear=nn.Linear(hidden_size, num_embeddings)

  def forward(self, x, h0=None):
    x=self.emb(x)
    x, h =self.lstm(x, h0)
    x=self.linear(x)
    return x, h

def make_wakati(sentence):
  tagger = MeCab.Tagger("-Owakati -d /usr/lib/mecab/dic/mecab-ipadic-neologd")
  sentence = sentence.replace(",\n", " ")
  # MeCabで分かち書き
  sentence = tagger.parse(sentence)
  # 半角全角英数字除去
  sentence = re.sub(r'[0-9０-９]+', "0", sentence)
  sentence.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
  # 記号もろもろ除去
  sentence = re.sub(r'[\．_－―─！＠＃＄％＾＆\-‐|\\＊\“（）＿■×+α※÷⇒—●★☆〇◎◆▼◇△□(：〜～＋=)／*&^%$#@!~`){}［］…\[\]\"\'\”\’:;<>?＜＞〔〕〈〉？、。・,\./『』【】「」→←○《》≪≫\n\u3000]+', "", sentence)
  # スペースで区切って形態素の配列へ
  wakati = sentence.split(" ")
  # 空の要素は削除
  wakati = list(filter(("").__ne__, wakati))
  return wakati

def sentence2index(sentences):
  wakati = make_wakati(sentences)
  with open("data/w2i.pkl", "rb")as data:
    word2index = pickle.load(data)
  id_stc = [word2index[i] for i in make_wakati(sentences)]
  return id_stc

def generate_seq(net, start_phase="eスポーツを盛り上げる", length=200, temperature=0.8, device="cpu"):
  net.eval()
  result=[]

  start_tensor=torch.tensor(
      sentence2index(start_phase), dtype=torch.int64
  ).to(device)

  x0=start_tensor.unsqueeze(0)
  o, h=net(x0)
  out_dist=o[:, -1].view(-1).exp()
  top_i=torch.multinomial(out_dist, 1)[0]
  result.append(top_i)

  for i in range(length):
    inp=torch.tensor([[top_i]], dtype=torch.int64)
    inp=inp.to(device)
    o, h=net(inp, h)
    out_dist=o.view(-1).exp()
    top_i=torch.multinomial(out_dist, 1)[0]
    result.append(top_i)
  with open("data/i2w.pkl", "rb")as data:
    index2word = pickle.load(data)
  res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
  return start_phase+ res