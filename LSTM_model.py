Last login: Mon Oct  7 21:39:23 on ttys000
-bash: export　PATH=/Users/anbujianjie/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin: No such file or directory
(base) abekensukenoMacBook-Pro:~ anbujianjie$ cd Desktop/abetter/
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ pwd
/Users/anbujianjie/Desktop/abetter
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ ls
LSTM_model.py	app.py		model.pkl	tweet.js
__pycache__	i2w.pkl		templates	w2i.pkl
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS               NAMES
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   24 minutes ago      Up 23 minutes                           suspicious_swanson
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker images
REPOSITORY                                   TAG                 IMAGE ID            CREATED             SIZE
container                                    1.0                 5613848570b6        42 minutes ago      4.06GB
vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   latest              5613848570b6        42 minutes ago      4.06GB
ubuntu                                       16.04               657d80a6401d        2 weeks ago         121MB
lucidfrontier45/pytorch                      latest              d8bc3d6b7ec5        7 weeks ago         2.96GB
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docek exec -it container bash
-bash: docek: command not found
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -it -p 8888:8888 -v ~/Desktop/abetter/:/abetter container:1.0
root@d74199e159c4:/# pwd
/
root@d74199e159c4:/# cd abetter/
root@d74199e159c4:/abetter# pwd
/abetter
root@d74199e159c4:/abetter# ls
LSTM_model.py  __pycache__  app.py  i2w.pkl  model.pkl  templates  tweet.js  w2i.pkl
root@d74199e159c4:/abetter# pip install torch
Collecting torch
  Downloading https://files.pythonhosted.org/packages/30/57/d5cceb0799c06733eefce80c395459f28970ebb9e896846ce96ab579a3f1/torch-1.2.0-cp36-cp36m-manylinux1_x86_64.whl (748.8MB)
     |################################| 748.9MB 5.2kB/s 
Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from torch) (1.17.2)
Installing collected packages: torch
Successfully installed torch-1.2.0
root@d74199e159c4:/abetter# set SLASK_APP = app.py
root@d74199e159c4:/abetter# flask run
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 966, in main
    cli.main(prog_name="python -m flask" if as_module else None)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 696, in main
    _verify_python3_env()
  File "/usr/local/lib/python3.6/dist-packages/click/_unicodefun.py", line 124, in _verify_python3_env
    ' mitigation steps.' + extra
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment. Consult https://click.palletsprojects.com/en/7.x/python3/ for mitigation steps.

This system supports the C.UTF-8 locale which is recommended.
You might be able to resolve your issue by exporting the
following environment variables:

    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
root@d74199e159c4:/abetter# set FLASK_APP = app.py
root@d74199e159c4:/abetter# flask run
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 966, in main
    cli.main(prog_name="python -m flask" if as_module else None)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 696, in main
    _verify_python3_env()
  File "/usr/local/lib/python3.6/dist-packages/click/_unicodefun.py", line 124, in _verify_python3_env
    ' mitigation steps.' + extra
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment. Consult https://click.palletsprojects.com/en/7.x/python3/ for mitigation steps.

This system supports the C.UTF-8 locale which is recommended.
You might be able to resolve your issue by exporting the
following environment variables:

    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
root@d74199e159c4:/abetter# export LC_ALL=C.UTF-8
root@d74199e159c4:/abetter# export LANG=C.UTF-8
root@d74199e159c4:/abetter# flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: While importing "app", an ImportError was raised:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 240, in locate_app
    __import__(module_name)
  File "/abetter/app.py", line 1, in <module>
    import cloudpickle
ModuleNotFoundError: No module named 'cloudpickle'

root@d74199e159c4:/abetter# pip install cloudpickle
Collecting cloudpickle
  Downloading https://files.pythonhosted.org/packages/c1/49/334e279caa3231255725c8e860fa93e72083567625573421db8875846c14/cloudpickle-1.2.2-py2.py3-none-any.whl
Installing collected packages: cloudpickle
Successfully installed cloudpickle-1.2.2
root@d74199e159c4:/abetter# flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
^Croot@d74199e159c4:/abetter# exit
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -it -p 5000:5000 -v ~/Desktop/abetter/:/abetter container:1.0
root@900c3d70bddf:/# pwd
/
root@900c3d70bddf:/# ls
abetter  bin  boot  dev  etc  home  lib  lib64  mecab-ipadic-neologd  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@900c3d70bddf:/# cd abetter/
root@900c3d70bddf:/abetter# set FLASK_APP = app.py
root@900c3d70bddf:/abetter# flaskr un
bash: flaskr: command not found
root@900c3d70bddf:/abetter# flask run
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 966, in main
    cli.main(prog_name="python -m flask" if as_module else None)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 696, in main
    _verify_python3_env()
  File "/usr/local/lib/python3.6/dist-packages/click/_unicodefun.py", line 124, in _verify_python3_env
    ' mitigation steps.' + extra
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment. Consult https://click.palletsprojects.com/en/7.x/python3/ for mitigation steps.

This system supports the C.UTF-8 locale which is recommended.
You might be able to resolve your issue by exporting the
following environment variables:

    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
root@900c3d70bddf:/abetter# export LC_ALL=C.UTF-8
root@900c3d70bddf:/abetter#     export LANG=C.UTF-8
root@900c3d70bddf:/abetter# flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: While importing "app", an ImportError was raised:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 240, in locate_app
    __import__(module_name)
  File "/abetter/app.py", line 1, in <module>
    import cloudpickle
ModuleNotFoundError: No module named 'cloudpickle'

root@900c3d70bddf:/abetter# pip install cloudpickle torch
Collecting cloudpickle
  Downloading https://files.pythonhosted.org/packages/c1/49/334e279caa3231255725c8e860fa93e72083567625573421db8875846c14/cloudpickle-1.2.2-py2.py3-none-any.whl
Collecting torch
  Downloading https://files.pythonhosted.org/packages/30/57/d5cceb0799c06733eefce80c395459f28970ebb9e896846ce96ab579a3f1/torch-1.2.0-cp36-cp36m-manylinux1_x86_64.whl (748.8MB)
     |████████████████████████████████| 748.9MB 7.5kB/s 
Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from torch) (1.17.2)
Installing collected packages: cloudpickle, torch
Successfully installed cloudpickle-1.2.2 torch-1.2.0
root@900c3d70bddf:/abetter# flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
^Croot@900c3d70bddf:/abetterflask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
^Croot@900c3d70bddf:/abetter# (base) abekensukenoMacBook-Pro:abetter anbujianjie$ pwd
/Users/anbujianjie/Desktop/abetter
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ ls
LSTM_model.py	__pycache__	app.py		i2w.pkl		model.pkl	templates	tweet.js	w2i.pkl
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS                      PORTS                    NAMES
900c3d70bddf        container:1.0                                "/bin/bash"              7 minutes ago       Up 7 minutes                0.0.0.0:5000->5000/tcp   zen_meninsky
d74199e159c4        container:1.0                                "/bin/bash"              14 minutes ago      Exited (0) 7 minutes ago                             focused_ptolemy
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   39 minutes ago      Up 39 minutes                                        suspicious_swanson
3ab271d6462c        container:1.0                                "/bin/bash"              49 minutes ago      Exited (0) 41 minutes ago                            nifty_pike
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm d74199e159c4
d74199e159c4
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS                      PORTS                    NAMES
900c3d70bddf        container:1.0                                "/bin/bash"              7 minutes ago       Up 7 minutes                0.0.0.0:5000->5000/tcp   zen_meninsky
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   40 minutes ago      Up 40 minutes                                        suspicious_swanson
3ab271d6462c        container:1.0                                "/bin/bash"              49 minutes ago      Exited (0) 41 minutes ago                            nifty_pike
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm 3ab271d6462c
3ab271d6462c
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
900c3d70bddf        container:1.0                                "/bin/bash"              7 minutes ago       Up 7 minutes        0.0.0.0:5000->5000/tcp   zen_meninsky
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   40 minutes ago      Up 40 minutes                                suspicious_swanson
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:8000
curl: (7) Failed to connect to localhost port 8000: Connection refused
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:8090
curl: (7) Failed to connect to localhost port 8090: Connection refused
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ pwd
/Users/anbujianjie/Desktop/abetter
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ set FLASK_APP=app.py
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
^C(base) abekensukenoMacBook-Pro:abetter anbujianjie$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [08/Oct/2019 11:35:04] "GET / HTTP/1.1" 200 -
^C(base) abekensukenoMacBook-Pro:abetter anbujianjie$ pwd
/Users/anbujianjie/Desktop/abetter
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ ls
LSTM_model.py	app.py		model.pkl	tweet.js
__pycache__	i2w.pkl		templates	w2i.pkl
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [08/Oct/2019 11:36:08] "GET / HTTP/1.1" 200 -
[2019-10-08 11:36:11,937] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/Users/anbujianjie/anaconda3/lib/python3.7/site-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/Users/anbujianjie/anaconda3/lib/python3.7/site-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/Users/anbujianjie/anaconda3/lib/python3.7/site-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/Users/anbujianjie/anaconda3/lib/python3.7/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/Users/anbujianjie/anaconda3/lib/python3.7/site-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/Users/anbujianjie/anaconda3/lib/python3.7/site-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/Users/anbujianjie/Desktop/abetter/app.py", line 19, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/Users/anbujianjie/Desktop/abetter/LSTM_model.py", line 72, in generate_seq
    sentence2index(start_phase), dtype=torch.int64
  File "/Users/anbujianjie/Desktop/abetter/LSTM_model.py", line 45, in sentence2index
    wakati = make_wakati(sentences)
  File "/Users/anbujianjie/Desktop/abetter/LSTM_model.py", line 19, in make_wakati
    tagger = MeCab.Tagger("-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
NameError: name 'MeCab' is not defined
127.0.0.1 - - [08/Oct/2019 11:36:11] "POST / HTTP/1.1" 500 -
^C(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docekr ps
-bash: docekr: command not found
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
900c3d70bddf        container:1.0                                "/bin/bash"              34 minutes ago      Up 33 minutes       0.0.0.0:5000->5000/tcp   zen_meninsky
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   About an hour ago   Up About an hour                             suspicious_swanson
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker logs vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7
Error: No such container: vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker logs fb5884f77bdd
Container started
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
900c3d70bddf        container:1.0                                "/bin/bash"              40 minutes ago      Up 40 minutes       0.0.0.0:5000->5000/tcp   zen_meninsky
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   About an hour ago   Up About an hour                             suspicious_swanson
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker exec -it fb5884f77bdd -p 5000:5080 bash
OCI runtime exec failed: exec failed: container_linux.go:345: starting container process caused "exec: \"-p\": executable file not found in $PATH": unknown
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker exec -it 900c3d70bddf -p 5000:5080 bash
OCI runtime exec failed: exec failed: container_linux.go:345: starting container process caused "exec: \"-p\": executable file not found in $PATH": unknown
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -it 900c3d70bddf -p 5000:5080 bash
Unable to find image '900c3d70bddf:latest' locally
docker: Error response from daemon: pull access denied for 900c3d70bddf, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -d -p 9000:8080 900c3d70bddf
Unable to find image '900c3d70bddf:latest' locally
docker: Error response from daemon: pull access denied for 900c3d70bddf, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
900c3d70bddf        container:1.0                                "/bin/bash"              44 minutes ago      Up 44 minutes       0.0.0.0:5000->5000/tcp   zen_meninsky
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   About an hour ago   Up About an hour                             suspicious_swanson
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
900c3d70bddf        container:1.0                                "/bin/bash"              45 minutes ago      Up 45 minutes       0.0.0.0:5000->5000/tcp   zen_meninsky
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   About an hour ago   Up About an hour                             suspicious_swanson
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm fb5884f77bdd
Error response from daemon: You cannot remove a running container fb5884f77bdde1000e98b30de4241305a5aea14bd7dd3827bb1dcf99199596e9. Stop the container before attempting removal or force remove
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker stop fb5884f77bdd
^C
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
900c3d70bddf        container:1.0                                "/bin/bash"              46 minutes ago      Up 45 minutes       0.0.0.0:5000->5000/tcp   zen_meninsky
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   About an hour ago   Up About an hour                             suspicious_swanson
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
900c3d70bddf        container:1.0                                "/bin/bash"              46 minutes ago      Up 46 minutes       0.0.0.0:5000->5000/tcp   zen_meninsky
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   About an hour ago   Up 8 seconds                                 suspicious_swanson
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
900c3d70bddf        container:1.0                                "/bin/bash"              48 minutes ago      Up 48 minutes       0.0.0.0:5000->5000/tcp   zen_meninsky
fb5884f77bdd        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   About an hour ago   Up 2 minutes                                 suspicious_swanson
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker stop fb5884f77bdd
fb5884f77bdd
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm fb5884f77bdd
fb5884f77bdd
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
900c3d70bddf        container:1.0       "/bin/bash"         49 minutes ago      Up 49 minutes       0.0.0.0:5000->5000/tcp   zen_meninsky
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl http://localhost:5000
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ curl 127.0.0.1:5000 -v
*   Trying 127.0.0.1:5000...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.65.2
> Accept: */*
> 
* Empty reply from server
* Connection #0 to host 127.0.0.1 left intact
curl: (52) Empty reply from server
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
d01cb42db15a        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   8 minutes ago       Up 8 minutes        5000/tcp                 stupefied_greider
900c3d70bddf        container:1.0                                "/bin/bash"              About an hour ago   Up About an hour    0.0.0.0:5000->5000/tcp   zen_meninsky
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker top d01cb42db15a
PID                 USER                TIME                COMMAND
20590               root                0:00                /bin/sh -c echo Container started ; while sleep 1; do :; done
22106               root                0:00                sh /root/.vscode-server/bin/b37e54c98e1a74ba89e03073e5a3761284e3ffb0/server.sh --disable-user-env-probe --port 0
22119               root                0:02                /root/.vscode-server/bin/b37e54c98e1a74ba89e03073e5a3761284e3ffb0/node /root/.vscode-server/bin/b37e54c98e1a74ba89e03073e5a3761284e3ffb0/out/vs/server/main.js --disable-user-env-probe --port 0
22237               root                0:00                /root/.vscode-server/bin/b37e54c98e1a74ba89e03073e5a3761284e3ffb0/node -e const net = require('net'); process.stdin.pause(); const client = net.createConnection({ port: 39535 }, () => { client.pipe(process.stdout); process.stdin.pipe(client); }); client.on('close', function (hadError) { process.exit(hadError ? 1 : 0); }); client.on('error', function (err) { process.stderr.write(err && (err.stack || err.message) || String(err)); });
22274               root                0:00                /root/.vscode-server/bin/b37e54c98e1a74ba89e03073e5a3761284e3ffb0/node -e const net = require('net'); process.stdin.pause(); const client = net.createConnection({ port: 39535 }, () => { client.pipe(process.stdout); process.stdin.pipe(client); }); client.on('close', function (hadError) { process.exit(hadError ? 1 : 0); }); client.on('error', function (err) { process.stderr.write(err && (err.stack || err.message) || String(err)); });
22297               root                0:04                /root/.vscode-server/bin/b37e54c98e1a74ba89e03073e5a3761284e3ffb0/node /root/.vscode-server/bin/b37e54c98e1a74ba89e03073e5a3761284e3ffb0/out/bootstrap-fork --type=extensionHost --uriTransformerPath=/root/.vscode-server/bin/b37e54c98e1a74ba89e03073e5a3761284e3ffb0/out/vs/server/uriTransformer.js
22312               root                0:01                /root/.vscode-server/bin/b37e54c98e1a74ba89e03073e5a3761284e3ffb0/node /root/.vscode-server/bin/b37e54c98e1a74ba89e03073e5a3761284e3ffb0/out/bootstrap-fork --type=watcherService
22364               root                0:00                /bin/bash
22681               root                0:00                {flask} /usr/bin/python3.6 /usr/local/bin/flask run
22937               root                0:00                sleep 1
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
d01cb42db15a        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   12 minutes ago      Up 12 minutes       5000/tcp                 stupefied_greider
900c3d70bddf        container:1.0                                "/bin/bash"              About an hour ago   Up About an hour    0.0.0.0:5000->5000/tcp   zen_meninsky
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker images
REPOSITORY                                   TAG                 IMAGE ID            CREATED             SIZE
vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   latest              eef71bb91514        14 minutes ago      6.18GB
container                                    1.0                 5613848570b6        2 hours ago         4.06GB
ubuntu                                       16.04               657d80a6401d        2 weeks ago         121MB
lucidfrontier45/pytorch                      latest              d8bc3d6b7ec5        7 weeks ago         2.96GB
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -it container -p 5000:5000 /bin/bash
Unable to find image 'container:latest' locally
docker: Error response from daemon: pull access denied for container, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -it -p 5000:5000 -v ~/Desktop/abetter/:/abetter container:1.0
docker: Error response from daemon: driver failed programming external connectivity on endpoint blissful_dirac (954cdc702603b26c677c51ccd852e48a42aac81f60f690f0088e5998e7008235): Bind for 0.0.0.0:5000 failed: port is already allocated.
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
005ac9fb9928        container:1.0                                "/bin/bash"              11 seconds ago      Created                                      blissful_dirac
d01cb42db15a        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   16 minutes ago      Up 16 minutes       5000/tcp                 stupefied_greider
900c3d70bddf        container:1.0                                "/bin/bash"              About an hour ago   Up About an hour    0.0.0.0:5000->5000/tcp   zen_meninsky
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm 900c3d70bddf
Error response from daemon: You cannot remove a running container 900c3d70bddfe1fc378d865478a2fd9a8c6cc24d3d7057711f80ad8b6cf4056b. Stop the container before attempting removal or force remove
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker stop 900c3d70bddf
900c3d70bddf
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm 900c3d70bddf
900c3d70bddf
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker stop 005ac9fb9928
005ac9fb9928
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm 005ac9fb9928
005ac9fb9928
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS               NAMES
d01cb42db15a        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   16 minutes ago      Up 16 minutes       5000/tcp            stupefied_greider
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -it -p 5000:5000 -v ~/Desktop/abetter/:/abetter container:1.0
root@7c35a59b3c3d:/# pwd
/
root@7c35a59b3c3d:/# ls
abetter  bin  boot  dev  etc  home  lib  lib64  mecab-ipadic-neologd  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@7c35a59b3c3d:/# cd abetter/
root@7c35a59b3c3d:/abetter# pwd
/abetter
root@7c35a59b3c3d:/abetter# ls
LSTM_model.py  __pycache__  app.py  i2w.pkl  model.pkl  templates  tweet.js  w2i.pkl
root@7c35a59b3c3d:/abetter# exit
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS                     PORTS               NAMES
7c35a59b3c3d        container:1.0                                "/bin/bash"              24 seconds ago      Exited (0) 5 seconds ago                       vigilant_beaver
d01cb42db15a        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   17 minutes ago      Up 17 minutes              5000/tcp            stupefied_greider
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm 7c35a59b3c3d
7c35a59b3c3d
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ pwd
/Users/anbujianjie/Desktop/abetter
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker build -t container:1.0 .
unable to prepare context: unable to evaluate symlinks in Dockerfile path: lstat /Users/anbujianjie/Desktop/abetter/Dockerfile: no such file or directory
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker images
REPOSITORY                                   TAG                 IMAGE ID            CREATED             SIZE
vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   latest              eef71bb91514        17 minutes ago      6.18GB
container                                    1.0                 5613848570b6        2 hours ago         4.06GB
ubuntu                                       16.04               657d80a6401d        2 weeks ago         121MB
lucidfrontier45/pytorch                      latest              d8bc3d6b7ec5        7 weeks ago         2.96GB
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rmi container
Error: No such image: container
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rmi 5613848570b6
Error response from daemon: conflict: unable to delete 5613848570b6 (cannot be forced) - image has dependent child images
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rmi vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7
Error response from daemon: conflict: unable to remove repository reference "vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7" (must force) - container d01cb42db15a is using its referenced image eef71bb91514
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS               NAMES
d01cb42db15a        vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7   "/bin/sh -c 'echo Co…"   18 minutes ago      Up 18 minutes       5000/tcp            stupefied_greider
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker stop d01cb42db15a
d01cb42db15a
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm d01cb42db15a
d01cb42db15a
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rmi vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7
Untagged: vsc-flask-2c32c1fc261342d2b33ffb7ad66dfbf7:latest
Deleted: sha256:eef71bb91514b4d9c74757d495db95f1f818bbdc956b969f16864bf2ac43c731
Deleted: sha256:3ff0ff560e68cdbe24d03ba33b4674492682d56a5c5a5ea4cf342b186cf838fc
Deleted: sha256:305118fbe60412f326a7a3be15836d92cf58d4d8dd6c0407ce9ae6da00aa1207
Deleted: sha256:3d94f6ed35bd31cd4e25d8c2572e2b3ad218ecf1b24a4f54718208ab89872ddf
Deleted: sha256:7989e391ad57ebcaa524f6056792fe9d682b0a88ad45d0cb327a653cfdf80981
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rmi 5613848570b6
Untagged: container:1.0
Deleted: sha256:5613848570b64366d4fcd011b13118493910632437072c35c385c33f62ad4146
Deleted: sha256:66386eb1c226514753f8a9052260fe339f886da4e73c93ce305fc1bd3dc3f584
Deleted: sha256:14eff63f38634eeb5466b1cde99ae9d0ffa4a0ae2eedd19cffa9a81b816eb530
Deleted: sha256:696bdbf0ef431198ac9bb2ba0d6d6e903fde6d5cba60bfb24a4a81ccda5d9f9f
Deleted: sha256:98076514c2b8b7c1d89c8a88c712b551b2593be3d4b2ffd60d93783c787a9d9c
Deleted: sha256:fc181cbc8da1eac0ce049fff9fe70b91af83dfb9030a1f9d53dda9875b2e9cbb
Deleted: sha256:ba3f03e1263e23192f7059b69b6e1ffb251a4c5f89a2a1e25c2d6a77563e96be
Deleted: sha256:4d0e3a4f9ffbcd84729d0995f193cc06ec360ede334b98897ee0717cd439851c
Deleted: sha256:0959f22c0040391384f535636acf5d4e2291ee776e53678638e29514cc5cbb39
Deleted: sha256:577dde9396230b034697cb4db13e78f3edf47926a547325b1883bb13b2b5a002
Deleted: sha256:37e1654d3385de4bb0a6291bb2314412e976c2a3e6f822059e5d8a245ad49ccc
Deleted: sha256:d99af1da899b1c6fab43e23d733b7594161a243c2d64e1ac4ab4fafb06558106
Deleted: sha256:4bbc005ddca3bd3708469c71e9e9a2e66399986ea1ccda08be7f6bfb071a1663
Deleted: sha256:047b659d96d79676ed1a89350434ec347ada4c7e2be6daf898919cde111963db
Deleted: sha256:c9d9ecbf6254e66ea8c81ed9233c966c4a5f0e98c8aebff2cf471b5ac5c575fc
Deleted: sha256:8062d9188638706b2e476b1f8f5037f6a4591df9754837037b81f21f5e3418bb
Deleted: sha256:f7a9e1e0722263cb08d40451fd9d5db4ed9c1b40b1b2b082c30795a6554998dc
Deleted: sha256:8ded3e13576b0a2ba76ec9177e33af293bdb15a1450330c604f0ef9adb555df7
Deleted: sha256:bbd5a7e5a65051c57f1d0a17d6b4637dd0c0e252f88c17225556355d90059932
Deleted: sha256:47c5343ccd7cc708485cdb5ba741e5ced2dfd15dc37acad739803d9e41ead318
Deleted: sha256:de298d7d3781ee8982946fe96d6327c34a2f0a4b179ab8525b21a2ec8c546eb5
Deleted: sha256:beb67d9b379489683389267a8292dd619ec4c306e033c08799d2ff9f77232b87
Deleted: sha256:f7ff1c22a89f4b8903bbb36cc5543ad04435422e0877e08f3dcfe241ef4e9c74
Deleted: sha256:3eab479efa42d5fca09d1d68a7e1775a8c7fab70c879292797ca1071e4bcb72e
Deleted: sha256:1089db7f18d147e647577cd679f2dad2ca0c2b6f3ab9d9d2a4f59b9d8eb58981
Deleted: sha256:170b2efe2d6b92bf49d52cf79388c4f511c9d1d1077ab99b9701ba35ba3862d4
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker images
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
ubuntu                    16.04               657d80a6401d        2 weeks ago         121MB
lucidfrontier45/pytorch   latest              d8bc3d6b7ec5        7 weeks ago         2.96GB
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ dokcer ps -a
-bash: dokcer: command not found
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ pwd
/Users/anbujianjie/Desktop/abetter
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ ls
LSTM_model.py	__pycache__	app.py		i2w.pkl		model.pkl	templates	tweet.js	w2i.pkl
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker build -t container:1.0 .
unable to prepare context: unable to evaluate symlinks in Dockerfile path: lstat /Users/anbujianjie/Desktop/abetter/Dockerfile: no such file or directory
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ ls
LSTM_model.py	__pycache__	app.py		i2w.pkl		model.pkl	templates	tweet.js	w2i.pkl
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ cd ../Flask/
(base) abekensukenoMacBook-Pro:Flask anbujianjie$ ls
Dockerfile	LSTM_model.py	Untitled.ipynb	__pycache__	app.py		model.pkl	modeling.py	templates	tweet.js
(base) abekensukenoMacBook-Pro:Flask anbujianjie$ docker build -t container:1.0 .
Sending build context to Docker daemon  15.22MB
Step 1/19 : FROM ubuntu:16.04
 ---> 657d80a6401d
Step 2/19 : RUN apt-get update     && apt-get install -y mecab     && apt-get install -y libmecab-dev     && apt-get install -y mecab-ipadic-utf8    && apt-get install -y git    && apt-get install -y make    && apt-get install -y curl    && apt-get install -y xz-utils    && apt-get install -y file    && apt-get install -y sudo    && apt-get install -y wget
 ---> Running in 4d5726d908af
Get:1 http://security.ubuntu.com/ubuntu xenial-security InRelease [109 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial InRelease [247 kB]
Get:3 http://security.ubuntu.com/ubuntu xenial-security/main amd64 Packages [971 kB]
Get:4 http://archive.ubuntu.com/ubuntu xenial-updates InRelease [109 kB]
Get:5 http://archive.ubuntu.com/ubuntu xenial-backports InRelease [107 kB]
Get:6 http://security.ubuntu.com/ubuntu xenial-security/restricted amd64 Packages [12.7 kB]
Get:7 http://security.ubuntu.com/ubuntu xenial-security/universe amd64 Packages [587 kB]
Get:8 http://archive.ubuntu.com/ubuntu xenial/main amd64 Packages [1558 kB]
Get:9 http://security.ubuntu.com/ubuntu xenial-security/multiverse amd64 Packages [6276 B]
Get:10 http://archive.ubuntu.com/ubuntu xenial/restricted amd64 Packages [14.1 kB]
Get:11 http://archive.ubuntu.com/ubuntu xenial/universe amd64 Packages [9827 kB]
Get:12 http://archive.ubuntu.com/ubuntu xenial/multiverse amd64 Packages [176 kB]
Get:13 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 Packages [1348 kB]
Get:14 http://archive.ubuntu.com/ubuntu xenial-updates/restricted amd64 Packages [13.1 kB]
Get:15 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 Packages [991 kB]
Get:16 http://archive.ubuntu.com/ubuntu xenial-updates/multiverse amd64 Packages [19.2 kB]
Get:17 http://archive.ubuntu.com/ubuntu xenial-backports/main amd64 Packages [7942 B]
Get:18 http://archive.ubuntu.com/ubuntu xenial-backports/universe amd64 Packages [8807 B]
Fetched 16.1 MB in 20s (781 kB/s)
Reading package lists...
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  libmecab2 mecab-jumandic mecab-utils
The following NEW packages will be installed:
  libmecab2 mecab mecab-jumandic mecab-utils
0 upgraded, 4 newly installed, 0 to remove and 4 not upgraded.
Need to get 13.3 MB of archives.
After this operation, 81.4 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial/universe amd64 libmecab2 amd64 0.996-1.2ubuntu1 [264 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial/universe amd64 mecab-utils amd64 0.996-1.2ubuntu1 [4566 B]
Get:3 http://archive.ubuntu.com/ubuntu xenial/universe amd64 mecab-jumandic all 5.1+20070304-3 [13.0 MB]
Get:4 http://archive.ubuntu.com/ubuntu xenial/universe amd64 mecab amd64 0.996-1.2ubuntu1 [83.2 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 13.3 MB in 8s (1506 kB/s)
Selecting previously unselected package libmecab2.
(Reading database ... 4777 files and directories currently installed.)
Preparing to unpack .../libmecab2_0.996-1.2ubuntu1_amd64.deb ...
Unpacking libmecab2 (0.996-1.2ubuntu1) ...
Selecting previously unselected package mecab-utils.
Preparing to unpack .../mecab-utils_0.996-1.2ubuntu1_amd64.deb ...
Unpacking mecab-utils (0.996-1.2ubuntu1) ...
Selecting previously unselected package mecab-jumandic.
Preparing to unpack .../mecab-jumandic_5.1+20070304-3_all.deb ...
Unpacking mecab-jumandic (5.1+20070304-3) ...
Selecting previously unselected package mecab.
Preparing to unpack .../mecab_0.996-1.2ubuntu1_amd64.deb ...
Unpacking mecab (0.996-1.2ubuntu1) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Setting up libmecab2 (0.996-1.2ubuntu1) ...
Setting up mecab-utils (0.996-1.2ubuntu1) ...
Setting up mecab-jumandic (5.1+20070304-3) ...
Compiling Juman dictionary for Mecab.  This takes long time...
reading /usr/share/mecab/dic/juman/unk.def ... 37
emitting double-array: 100% |###########################################| 
/usr/share/mecab/dic/juman/model.def is not found. skipped.
reading /usr/share/mecab/dic/juman/Noun.hukusi.csv ... 74
reading /usr/share/mecab/dic/juman/ContentW.csv ... 483161
reading /usr/share/mecab/dic/juman/Noun.suusi.csv ... 46
reading /usr/share/mecab/dic/juman/Demonstrative.csv ... 76
reading /usr/share/mecab/dic/juman/Prefix.csv ... 75
reading /usr/share/mecab/dic/juman/Postp.csv ... 104
reading /usr/share/mecab/dic/juman/Noun.keishiki.csv ... 10
reading /usr/share/mecab/dic/juman/AuxV.csv ... 421
reading /usr/share/mecab/dic/juman/Rengo.csv ... 913
reading /usr/share/mecab/dic/juman/Suffix.csv ... 1163
reading /usr/share/mecab/dic/juman/Assert.csv ... 30
reading /usr/share/mecab/dic/juman/Noun.koyuu.csv ... 29805
reading /usr/share/mecab/dic/juman/Special.csv ... 124
emitting double-array: 100% |###########################################| 
reading /usr/share/mecab/dic/juman/matrix.def ... 1509x1509
emitting matrix      : 100% |###########################################| 

done!
update-alternatives: using /var/lib/mecab/dic/juman to provide /var/lib/mecab/dic/debian (mecab-dictionary) in auto mode
Setting up mecab (0.996-1.2ubuntu1) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.22.1 /usr/local/share/perl/5.22.1 /usr/lib/x86_64-linux-gnu/perl5/5.22 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.22 /usr/share/perl/5.22 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base .) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
Compiling Juman dictionary for Mecab.  This takes long time...
reading /usr/share/mecab/dic/juman/unk.def ... 37
emitting double-array: 100% |###########################################| 
/usr/share/mecab/dic/juman/model.def is not found. skipped.
reading /usr/share/mecab/dic/juman/Noun.hukusi.csv ... 74
reading /usr/share/mecab/dic/juman/ContentW.csv ... 483161
reading /usr/share/mecab/dic/juman/Noun.suusi.csv ... 46
reading /usr/share/mecab/dic/juman/Demonstrative.csv ... 76
reading /usr/share/mecab/dic/juman/Prefix.csv ... 75
reading /usr/share/mecab/dic/juman/Postp.csv ... 104
reading /usr/share/mecab/dic/juman/Noun.keishiki.csv ... 10
reading /usr/share/mecab/dic/juman/AuxV.csv ... 421
reading /usr/share/mecab/dic/juman/Rengo.csv ... 913
reading /usr/share/mecab/dic/juman/Suffix.csv ... 1163
reading /usr/share/mecab/dic/juman/Assert.csv ... 30
reading /usr/share/mecab/dic/juman/Noun.koyuu.csv ... 29805
reading /usr/share/mecab/dic/juman/Special.csv ... 124
emitting double-array: 100% |###########################################| 
reading /usr/share/mecab/dic/juman/matrix.def ... 1509x1509
emitting matrix      : 100% |###########################################| 

done!
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Reading package lists...
Building dependency tree...
Reading state information...
The following NEW packages will be installed:
  libmecab-dev
0 upgraded, 1 newly installed, 0 to remove and 4 not upgraded.
Need to get 313 kB of archives.
After this operation, 3261 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial/universe amd64 libmecab-dev amd64 0.996-1.2ubuntu1 [313 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 313 kB in 1s (171 kB/s)
Selecting previously unselected package libmecab-dev.
(Reading database ... 4854 files and directories currently installed.)
Preparing to unpack .../libmecab-dev_0.996-1.2ubuntu1_amd64.deb ...
Unpacking libmecab-dev (0.996-1.2ubuntu1) ...
Setting up libmecab-dev (0.996-1.2ubuntu1) ...
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  mecab-ipadic
The following NEW packages will be installed:
  mecab-ipadic mecab-ipadic-utf8
0 upgraded, 2 newly installed, 0 to remove and 4 not upgraded.
Need to get 12.1 MB of archives.
After this operation, 54.4 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial/universe amd64 mecab-ipadic all 2.7.0-20070801+main-1 [12.1 MB]
Get:2 http://archive.ubuntu.com/ubuntu xenial/universe amd64 mecab-ipadic-utf8 all 2.7.0-20070801+main-1 [3522 B]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 12.1 MB in 5s (2125 kB/s)
Selecting previously unselected package mecab-ipadic.
(Reading database ... 4864 files and directories currently installed.)
Preparing to unpack .../mecab-ipadic_2.7.0-20070801+main-1_all.deb ...
Unpacking mecab-ipadic (2.7.0-20070801+main-1) ...
Selecting previously unselected package mecab-ipadic-utf8.
Preparing to unpack .../mecab-ipadic-utf8_2.7.0-20070801+main-1_all.deb ...
Unpacking mecab-ipadic-utf8 (2.7.0-20070801+main-1) ...
Setting up mecab-ipadic (2.7.0-20070801+main-1) ...
Compiling IPA dictionary for Mecab.  This takes long time...
reading /usr/share/mecab/dic/ipadic/unk.def ... 40
emitting double-array: 100% |###########################################| 
/usr/share/mecab/dic/ipadic/model.def is not found. skipped.
reading /usr/share/mecab/dic/ipadic/Adnominal.csv ... 135
reading /usr/share/mecab/dic/ipadic/Adj.csv ... 27210
reading /usr/share/mecab/dic/ipadic/Prefix.csv ... 221
reading /usr/share/mecab/dic/ipadic/Noun.demonst.csv ... 120
reading /usr/share/mecab/dic/ipadic/Postp.csv ... 146
reading /usr/share/mecab/dic/ipadic/Auxil.csv ... 199
reading /usr/share/mecab/dic/ipadic/Symbol.csv ... 208
reading /usr/share/mecab/dic/ipadic/Noun.csv ... 60477
reading /usr/share/mecab/dic/ipadic/Noun.others.csv ... 151
reading /usr/share/mecab/dic/ipadic/Noun.adjv.csv ... 3328
reading /usr/share/mecab/dic/ipadic/Noun.number.csv ... 42
reading /usr/share/mecab/dic/ipadic/Noun.place.csv ... 72999
reading /usr/share/mecab/dic/ipadic/Conjunction.csv ... 171
reading /usr/share/mecab/dic/ipadic/Postp-col.csv ... 91
reading /usr/share/mecab/dic/ipadic/Noun.name.csv ... 34202
reading /usr/share/mecab/dic/ipadic/Noun.org.csv ... 16668
reading /usr/share/mecab/dic/ipadic/Adverb.csv ... 3032
reading /usr/share/mecab/dic/ipadic/Verb.csv ... 130750
reading /usr/share/mecab/dic/ipadic/Noun.adverbal.csv ... 795
reading /usr/share/mecab/dic/ipadic/Others.csv ... 2
reading /usr/share/mecab/dic/ipadic/Interjection.csv ... 252
reading /usr/share/mecab/dic/ipadic/Suffix.csv ... 1393
reading /usr/share/mecab/dic/ipadic/Noun.nai.csv ... 42
reading /usr/share/mecab/dic/ipadic/Noun.verbal.csv ... 12146
reading /usr/share/mecab/dic/ipadic/Noun.proper.csv ... 27327
reading /usr/share/mecab/dic/ipadic/Filler.csv ... 19
emitting double-array: 100% |###########################################| 
reading /usr/share/mecab/dic/ipadic/matrix.def ... 1316x1316
emitting matrix      : 100% |###########################################| 

done!
update-alternatives: using /var/lib/mecab/dic/ipadic to provide /var/lib/mecab/dic/debian (mecab-dictionary) in auto mode
Setting up mecab-ipadic-utf8 (2.7.0-20070801+main-1) ...
Compiling IPA dictionary for Mecab.  This takes long time...
reading /usr/share/mecab/dic/ipadic/unk.def ... 40
emitting double-array: 100% |###########################################| 
/usr/share/mecab/dic/ipadic/model.def is not found. skipped.
reading /usr/share/mecab/dic/ipadic/Adnominal.csv ... 135
reading /usr/share/mecab/dic/ipadic/Adj.csv ... 27210
reading /usr/share/mecab/dic/ipadic/Prefix.csv ... 221
reading /usr/share/mecab/dic/ipadic/Noun.demonst.csv ... 120
reading /usr/share/mecab/dic/ipadic/Postp.csv ... 146
reading /usr/share/mecab/dic/ipadic/Auxil.csv ... 199
reading /usr/share/mecab/dic/ipadic/Symbol.csv ... 208
reading /usr/share/mecab/dic/ipadic/Noun.csv ... 60477
reading /usr/share/mecab/dic/ipadic/Noun.others.csv ... 151
reading /usr/share/mecab/dic/ipadic/Noun.adjv.csv ... 3328
reading /usr/share/mecab/dic/ipadic/Noun.number.csv ... 42
reading /usr/share/mecab/dic/ipadic/Noun.place.csv ... 72999
reading /usr/share/mecab/dic/ipadic/Conjunction.csv ... 171
reading /usr/share/mecab/dic/ipadic/Postp-col.csv ... 91
reading /usr/share/mecab/dic/ipadic/Noun.name.csv ... 34202
reading /usr/share/mecab/dic/ipadic/Noun.org.csv ... 16668
reading /usr/share/mecab/dic/ipadic/Adverb.csv ... 3032
reading /usr/share/mecab/dic/ipadic/Verb.csv ... 130750
reading /usr/share/mecab/dic/ipadic/Noun.adverbal.csv ... 795
reading /usr/share/mecab/dic/ipadic/Others.csv ... 2
reading /usr/share/mecab/dic/ipadic/Interjection.csv ... 252
reading /usr/share/mecab/dic/ipadic/Suffix.csv ... 1393
reading /usr/share/mecab/dic/ipadic/Noun.nai.csv ... 42
reading /usr/share/mecab/dic/ipadic/Noun.verbal.csv ... 12146
reading /usr/share/mecab/dic/ipadic/Noun.proper.csv ... 27327
reading /usr/share/mecab/dic/ipadic/Filler.csv ... 19
emitting double-array: 100% |###########################################| 
reading /usr/share/mecab/dic/ipadic/matrix.def ... 1316x1316
emitting matrix      : 100% |###########################################| 

done!
update-alternatives: using /var/lib/mecab/dic/ipadic-utf8 to provide /var/lib/mecab/dic/debian (mecab-dictionary) in auto mode
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  ca-certificates git-man ifupdown iproute2 isc-dhcp-client isc-dhcp-common
  krb5-locales less libasn1-8-heimdal libatm1 libbsd0 libcurl3-gnutls
  libdns-export162 libedit2 liberror-perl libexpat1 libffi6 libgdbm3 libgmp10
  libgnutls30 libgssapi-krb5-2 libgssapi3-heimdal libhcrypto4-heimdal
  libheimbase1-heimdal libheimntlm0-heimdal libhogweed4 libhx509-5-heimdal
  libidn11 libisc-export160 libk5crypto3 libkeyutils1 libkrb5-26-heimdal
  libkrb5-3 libkrb5support0 libldap-2.4-2 libmnl0 libnettle6 libp11-kit0
  libperl5.22 libpopt0 libroken18-heimdal librtmp1 libsasl2-2 libsasl2-modules
  libsasl2-modules-db libsqlite3-0 libssl1.0.0 libtasn1-6 libwind0-heimdal
  libx11-6 libx11-data libxau6 libxcb1 libxdmcp6 libxext6 libxmuu1
  libxtables11 netbase openssh-client openssl patch perl perl-modules-5.22
  rename rsync xauth
Suggested packages:
  gettext-base git-daemon-run | git-daemon-sysvinit git-doc git-el git-email
  git-gui gitk gitweb git-arch git-cvs git-mediawiki git-svn ppp rdnssd
  iproute2-doc resolvconf avahi-autoipd isc-dhcp-client-ddns apparmor
  gnutls-bin krb5-doc krb5-user libsasl2-modules-otp libsasl2-modules-ldap
  libsasl2-modules-sql libsasl2-modules-gssapi-mit
  | libsasl2-modules-gssapi-heimdal ssh-askpass libpam-ssh keychain
  monkeysphere ed diffutils-doc perl-doc libterm-readline-gnu-perl
  | libterm-readline-perl-perl make openssh-server
The following NEW packages will be installed:
  ca-certificates git git-man ifupdown iproute2 isc-dhcp-client
  isc-dhcp-common krb5-locales less libasn1-8-heimdal libatm1 libbsd0
  libcurl3-gnutls libdns-export162 libedit2 liberror-perl libexpat1 libffi6
  libgdbm3 libgmp10 libgnutls30 libgssapi-krb5-2 libgssapi3-heimdal
  libhcrypto4-heimdal libheimbase1-heimdal libheimntlm0-heimdal libhogweed4
  libhx509-5-heimdal libidn11 libisc-export160 libk5crypto3 libkeyutils1
  libkrb5-26-heimdal libkrb5-3 libkrb5support0 libldap-2.4-2 libmnl0
  libnettle6 libp11-kit0 libperl5.22 libpopt0 libroken18-heimdal librtmp1
  libsasl2-2 libsasl2-modules libsasl2-modules-db libsqlite3-0 libssl1.0.0
  libtasn1-6 libwind0-heimdal libx11-6 libx11-data libxau6 libxcb1 libxdmcp6
  libxext6 libxmuu1 libxtables11 netbase openssh-client openssl patch perl
  perl-modules-5.22 rename rsync xauth
0 upgraded, 67 newly installed, 0 to remove and 4 not upgraded.
Need to get 19.4 MB of archives.
After this operation, 98.4 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial/main amd64 libatm1 amd64 1:2.5.1-1.5 [24.2 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial/main amd64 libmnl0 amd64 1.0.3-5 [12.0 kB]
Get:3 http://archive.ubuntu.com/ubuntu xenial/main amd64 libpopt0 amd64 1.16-10 [26.0 kB]
Get:4 http://archive.ubuntu.com/ubuntu xenial/main amd64 libgdbm3 amd64 1.8.3-13.1 [16.9 kB]
Get:5 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxau6 amd64 1:1.0.8-1 [8376 B]
Get:6 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxdmcp6 amd64 1:1.1.2-1.1 [11.0 kB]
Get:7 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxcb1 amd64 1.11.1-1ubuntu1 [40.0 kB]
Get:8 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx11-data all 2:1.6.3-1ubuntu2.1 [113 kB]
Get:9 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libx11-6 amd64 2:1.6.3-1ubuntu2.1 [570 kB]
Get:10 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxext6 amd64 2:1.3.3-1 [29.4 kB]
Get:11 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 perl-modules-5.22 all 5.22.1-9ubuntu0.6 [2629 kB]
Get:12 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libperl5.22 amd64 5.22.1-9ubuntu0.6 [3405 kB]
Get:13 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 perl amd64 5.22.1-9ubuntu0.6 [237 kB]
Get:14 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 iproute2 amd64 4.3.0-1ubuntu3.16.04.5 [523 kB]
Get:15 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 ifupdown amd64 0.8.10ubuntu1.4 [54.9 kB]
Get:16 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libisc-export160 amd64 1:9.10.3.dfsg.P4-8ubuntu1.15 [153 kB]
Get:17 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdns-export162 amd64 1:9.10.3.dfsg.P4-8ubuntu1.15 [665 kB]
Get:18 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 isc-dhcp-client amd64 4.3.3-5ubuntu12.10 [224 kB]
Get:19 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 isc-dhcp-common amd64 4.3.3-5ubuntu12.10 [105 kB]
Get:20 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 less amd64 481-2.1ubuntu0.2 [110 kB]
Get:21 http://archive.ubuntu.com/ubuntu xenial/main amd64 libbsd0 amd64 0.8.2-1 [41.7 kB]
Get:22 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libexpat1 amd64 2.1.0-7ubuntu0.16.04.5 [71.5 kB]
Get:23 http://archive.ubuntu.com/ubuntu xenial/main amd64 libffi6 amd64 3.2.1-4 [17.8 kB]
Get:24 http://archive.ubuntu.com/ubuntu xenial/main amd64 libgmp10 amd64 2:6.1.0+dfsg-2 [240 kB]
Get:25 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libnettle6 amd64 3.2-1ubuntu0.16.04.1 [93.5 kB]
Get:26 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libhogweed4 amd64 3.2-1ubuntu0.16.04.1 [136 kB]
Get:27 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libidn11 amd64 1.32-3ubuntu1.2 [46.5 kB]
Get:28 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libp11-kit0 amd64 0.23.2-5~ubuntu16.04.1 [105 kB]
Get:29 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libtasn1-6 amd64 4.7-3ubuntu0.16.04.3 [43.5 kB]
Get:30 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgnutls30 amd64 3.4.10-4ubuntu1.5 [548 kB]
Get:31 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libsqlite3-0 amd64 3.11.0-1ubuntu1.2 [397 kB]
Get:32 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libssl1.0.0 amd64 1.0.2g-1ubuntu4.15 [1084 kB]
Get:33 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxtables11 amd64 1.6.0-2ubuntu3 [27.2 kB]
Get:34 http://archive.ubuntu.com/ubuntu xenial/main amd64 netbase all 5.3 [12.9 kB]
Get:35 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 openssl amd64 1.0.2g-1ubuntu4.15 [492 kB]
Get:36 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 ca-certificates all 20170717~16.04.2 [167 kB]
Get:37 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 krb5-locales all 1.13.2+dfsg-5ubuntu2.1 [13.6 kB]
Get:38 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libroken18-heimdal amd64 1.7~git20150920+dfsg-4ubuntu1.16.04.1 [41.4 kB]
Get:39 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libasn1-8-heimdal amd64 1.7~git20150920+dfsg-4ubuntu1.16.04.1 [174 kB]
Get:40 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libkrb5support0 amd64 1.13.2+dfsg-5ubuntu2.1 [31.2 kB]
Get:41 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libk5crypto3 amd64 1.13.2+dfsg-5ubuntu2.1 [81.3 kB]
Get:42 http://archive.ubuntu.com/ubuntu xenial/main amd64 libkeyutils1 amd64 1.5.9-8ubuntu1 [9904 B]
Get:43 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libkrb5-3 amd64 1.13.2+dfsg-5ubuntu2.1 [273 kB]
Get:44 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgssapi-krb5-2 amd64 1.13.2+dfsg-5ubuntu2.1 [120 kB]
Get:45 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libhcrypto4-heimdal amd64 1.7~git20150920+dfsg-4ubuntu1.16.04.1 [85.0 kB]
Get:46 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libheimbase1-heimdal amd64 1.7~git20150920+dfsg-4ubuntu1.16.04.1 [29.3 kB]
Get:47 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libwind0-heimdal amd64 1.7~git20150920+dfsg-4ubuntu1.16.04.1 [47.8 kB]
Get:48 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libhx509-5-heimdal amd64 1.7~git20150920+dfsg-4ubuntu1.16.04.1 [107 kB]
Get:49 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libkrb5-26-heimdal amd64 1.7~git20150920+dfsg-4ubuntu1.16.04.1 [202 kB]
Get:50 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libheimntlm0-heimdal amd64 1.7~git20150920+dfsg-4ubuntu1.16.04.1 [15.1 kB]
Get:51 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgssapi3-heimdal amd64 1.7~git20150920+dfsg-4ubuntu1.16.04.1 [96.1 kB]
Get:52 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libsasl2-modules-db amd64 2.1.26.dfsg1-14ubuntu0.1 [14.5 kB]
Get:53 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libsasl2-2 amd64 2.1.26.dfsg1-14ubuntu0.1 [48.6 kB]
Get:54 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libldap-2.4-2 amd64 2.4.42+dfsg-2ubuntu3.7 [160 kB]
Get:55 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 librtmp1 amd64 2.4+20151223.gitfa8646d-1ubuntu0.1 [54.4 kB]
Get:56 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libcurl3-gnutls amd64 7.47.0-1ubuntu2.14 [184 kB]
Get:57 http://archive.ubuntu.com/ubuntu xenial/main amd64 libedit2 amd64 3.1-20150325-1ubuntu2 [76.5 kB]
Get:58 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libsasl2-modules amd64 2.1.26.dfsg1-14ubuntu0.1 [47.5 kB]
Get:59 http://archive.ubuntu.com/ubuntu xenial/main amd64 libxmuu1 amd64 2:1.1.2-2 [9674 B]
Get:60 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 openssh-client amd64 1:7.2p2-4ubuntu2.8 [590 kB]
Get:61 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 rsync amd64 3.1.1-3ubuntu1.2 [329 kB]
Get:62 http://archive.ubuntu.com/ubuntu xenial/main amd64 xauth amd64 1:1.0.9-1ubuntu2 [22.7 kB]
Get:63 http://archive.ubuntu.com/ubuntu xenial/main amd64 liberror-perl all 0.17-1.2 [19.6 kB]
Get:64 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 git-man all 1:2.7.4-0ubuntu1.6 [736 kB]
Get:65 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 git amd64 1:2.7.4-0ubuntu1.6 [3176 kB]
Get:66 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 patch amd64 2.7.5-1ubuntu0.16.04.2 [90.8 kB]
Get:67 http://archive.ubuntu.com/ubuntu xenial/main amd64 rename all 0.20-4 [12.0 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 19.4 MB in 1min 31s (212 kB/s)
Selecting previously unselected package libatm1:amd64.
(Reading database ... 4909 files and directories currently installed.)
Preparing to unpack .../libatm1_1%3a2.5.1-1.5_amd64.deb ...
Unpacking libatm1:amd64 (1:2.5.1-1.5) ...
Selecting previously unselected package libmnl0:amd64.
Preparing to unpack .../libmnl0_1.0.3-5_amd64.deb ...
Unpacking libmnl0:amd64 (1.0.3-5) ...
Selecting previously unselected package libpopt0:amd64.
Preparing to unpack .../libpopt0_1.16-10_amd64.deb ...
Unpacking libpopt0:amd64 (1.16-10) ...
Selecting previously unselected package libgdbm3:amd64.
Preparing to unpack .../libgdbm3_1.8.3-13.1_amd64.deb ...
Unpacking libgdbm3:amd64 (1.8.3-13.1) ...
Selecting previously unselected package libxau6:amd64.
Preparing to unpack .../libxau6_1%3a1.0.8-1_amd64.deb ...
Unpacking libxau6:amd64 (1:1.0.8-1) ...
Selecting previously unselected package libxdmcp6:amd64.
Preparing to unpack .../libxdmcp6_1%3a1.1.2-1.1_amd64.deb ...
Unpacking libxdmcp6:amd64 (1:1.1.2-1.1) ...
Selecting previously unselected package libxcb1:amd64.
Preparing to unpack .../libxcb1_1.11.1-1ubuntu1_amd64.deb ...
Unpacking libxcb1:amd64 (1.11.1-1ubuntu1) ...
Selecting previously unselected package libx11-data.
Preparing to unpack .../libx11-data_2%3a1.6.3-1ubuntu2.1_all.deb ...
Unpacking libx11-data (2:1.6.3-1ubuntu2.1) ...
Selecting previously unselected package libx11-6:amd64.
Preparing to unpack .../libx11-6_2%3a1.6.3-1ubuntu2.1_amd64.deb ...
Unpacking libx11-6:amd64 (2:1.6.3-1ubuntu2.1) ...
Selecting previously unselected package libxext6:amd64.
Preparing to unpack .../libxext6_2%3a1.3.3-1_amd64.deb ...
Unpacking libxext6:amd64 (2:1.3.3-1) ...
Selecting previously unselected package perl-modules-5.22.
Preparing to unpack .../perl-modules-5.22_5.22.1-9ubuntu0.6_all.deb ...
Unpacking perl-modules-5.22 (5.22.1-9ubuntu0.6) ...
Selecting previously unselected package libperl5.22:amd64.
Preparing to unpack .../libperl5.22_5.22.1-9ubuntu0.6_amd64.deb ...
Unpacking libperl5.22:amd64 (5.22.1-9ubuntu0.6) ...
Selecting previously unselected package perl.
Preparing to unpack .../perl_5.22.1-9ubuntu0.6_amd64.deb ...
Unpacking perl (5.22.1-9ubuntu0.6) ...
Selecting previously unselected package iproute2.
Preparing to unpack .../iproute2_4.3.0-1ubuntu3.16.04.5_amd64.deb ...
Unpacking iproute2 (4.3.0-1ubuntu3.16.04.5) ...
Selecting previously unselected package ifupdown.
Preparing to unpack .../ifupdown_0.8.10ubuntu1.4_amd64.deb ...
Unpacking ifupdown (0.8.10ubuntu1.4) ...
Selecting previously unselected package libisc-export160.
Preparing to unpack .../libisc-export160_1%3a9.10.3.dfsg.P4-8ubuntu1.15_amd64.deb ...
Unpacking libisc-export160 (1:9.10.3.dfsg.P4-8ubuntu1.15) ...
Selecting previously unselected package libdns-export162.
Preparing to unpack .../libdns-export162_1%3a9.10.3.dfsg.P4-8ubuntu1.15_amd64.deb ...
Unpacking libdns-export162 (1:9.10.3.dfsg.P4-8ubuntu1.15) ...
Selecting previously unselected package isc-dhcp-client.
Preparing to unpack .../isc-dhcp-client_4.3.3-5ubuntu12.10_amd64.deb ...
Unpacking isc-dhcp-client (4.3.3-5ubuntu12.10) ...
Selecting previously unselected package isc-dhcp-common.
Preparing to unpack .../isc-dhcp-common_4.3.3-5ubuntu12.10_amd64.deb ...
Unpacking isc-dhcp-common (4.3.3-5ubuntu12.10) ...
Selecting previously unselected package less.
Preparing to unpack .../less_481-2.1ubuntu0.2_amd64.deb ...
Unpacking less (481-2.1ubuntu0.2) ...
Selecting previously unselected package libbsd0:amd64.
Preparing to unpack .../libbsd0_0.8.2-1_amd64.deb ...
Unpacking libbsd0:amd64 (0.8.2-1) ...
Selecting previously unselected package libexpat1:amd64.
Preparing to unpack .../libexpat1_2.1.0-7ubuntu0.16.04.5_amd64.deb ...
Unpacking libexpat1:amd64 (2.1.0-7ubuntu0.16.04.5) ...
Selecting previously unselected package libffi6:amd64.
Preparing to unpack .../libffi6_3.2.1-4_amd64.deb ...
Unpacking libffi6:amd64 (3.2.1-4) ...
Selecting previously unselected package libgmp10:amd64.
Preparing to unpack .../libgmp10_2%3a6.1.0+dfsg-2_amd64.deb ...
Unpacking libgmp10:amd64 (2:6.1.0+dfsg-2) ...
Selecting previously unselected package libnettle6:amd64.
Preparing to unpack .../libnettle6_3.2-1ubuntu0.16.04.1_amd64.deb ...
Unpacking libnettle6:amd64 (3.2-1ubuntu0.16.04.1) ...
Selecting previously unselected package libhogweed4:amd64.
Preparing to unpack .../libhogweed4_3.2-1ubuntu0.16.04.1_amd64.deb ...
Unpacking libhogweed4:amd64 (3.2-1ubuntu0.16.04.1) ...
Selecting previously unselected package libidn11:amd64.
Preparing to unpack .../libidn11_1.32-3ubuntu1.2_amd64.deb ...
Unpacking libidn11:amd64 (1.32-3ubuntu1.2) ...
Selecting previously unselected package libp11-kit0:amd64.
Preparing to unpack .../libp11-kit0_0.23.2-5~ubuntu16.04.1_amd64.deb ...
Unpacking libp11-kit0:amd64 (0.23.2-5~ubuntu16.04.1) ...
Selecting previously unselected package libtasn1-6:amd64.
Preparing to unpack .../libtasn1-6_4.7-3ubuntu0.16.04.3_amd64.deb ...
Unpacking libtasn1-6:amd64 (4.7-3ubuntu0.16.04.3) ...
Selecting previously unselected package libgnutls30:amd64.
Preparing to unpack .../libgnutls30_3.4.10-4ubuntu1.5_amd64.deb ...
Unpacking libgnutls30:amd64 (3.4.10-4ubuntu1.5) ...
Selecting previously unselected package libsqlite3-0:amd64.
Preparing to unpack .../libsqlite3-0_3.11.0-1ubuntu1.2_amd64.deb ...
Unpacking libsqlite3-0:amd64 (3.11.0-1ubuntu1.2) ...
Selecting previously unselected package libssl1.0.0:amd64.
Preparing to unpack .../libssl1.0.0_1.0.2g-1ubuntu4.15_amd64.deb ...
Unpacking libssl1.0.0:amd64 (1.0.2g-1ubuntu4.15) ...
Selecting previously unselected package libxtables11:amd64.
Preparing to unpack .../libxtables11_1.6.0-2ubuntu3_amd64.deb ...
Unpacking libxtables11:amd64 (1.6.0-2ubuntu3) ...
Selecting previously unselected package netbase.
Preparing to unpack .../archives/netbase_5.3_all.deb ...
Unpacking netbase (5.3) ...
Selecting previously unselected package openssl.
Preparing to unpack .../openssl_1.0.2g-1ubuntu4.15_amd64.deb ...
Unpacking openssl (1.0.2g-1ubuntu4.15) ...
Selecting previously unselected package ca-certificates.
Preparing to unpack .../ca-certificates_20170717~16.04.2_all.deb ...
Unpacking ca-certificates (20170717~16.04.2) ...
Selecting previously unselected package krb5-locales.
Preparing to unpack .../krb5-locales_1.13.2+dfsg-5ubuntu2.1_all.deb ...
Unpacking krb5-locales (1.13.2+dfsg-5ubuntu2.1) ...
Selecting previously unselected package libroken18-heimdal:amd64.
Preparing to unpack .../libroken18-heimdal_1.7~git20150920+dfsg-4ubuntu1.16.04.1_amd64.deb ...
Unpacking libroken18-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Selecting previously unselected package libasn1-8-heimdal:amd64.
Preparing to unpack .../libasn1-8-heimdal_1.7~git20150920+dfsg-4ubuntu1.16.04.1_amd64.deb ...
Unpacking libasn1-8-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Selecting previously unselected package libkrb5support0:amd64.
Preparing to unpack .../libkrb5support0_1.13.2+dfsg-5ubuntu2.1_amd64.deb ...
Unpacking libkrb5support0:amd64 (1.13.2+dfsg-5ubuntu2.1) ...
Selecting previously unselected package libk5crypto3:amd64.
Preparing to unpack .../libk5crypto3_1.13.2+dfsg-5ubuntu2.1_amd64.deb ...
Unpacking libk5crypto3:amd64 (1.13.2+dfsg-5ubuntu2.1) ...
Selecting previously unselected package libkeyutils1:amd64.
Preparing to unpack .../libkeyutils1_1.5.9-8ubuntu1_amd64.deb ...
Unpacking libkeyutils1:amd64 (1.5.9-8ubuntu1) ...
Selecting previously unselected package libkrb5-3:amd64.
Preparing to unpack .../libkrb5-3_1.13.2+dfsg-5ubuntu2.1_amd64.deb ...
Unpacking libkrb5-3:amd64 (1.13.2+dfsg-5ubuntu2.1) ...
Selecting previously unselected package libgssapi-krb5-2:amd64.
Preparing to unpack .../libgssapi-krb5-2_1.13.2+dfsg-5ubuntu2.1_amd64.deb ...
Unpacking libgssapi-krb5-2:amd64 (1.13.2+dfsg-5ubuntu2.1) ...
Selecting previously unselected package libhcrypto4-heimdal:amd64.
Preparing to unpack .../libhcrypto4-heimdal_1.7~git20150920+dfsg-4ubuntu1.16.04.1_amd64.deb ...
Unpacking libhcrypto4-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Selecting previously unselected package libheimbase1-heimdal:amd64.
Preparing to unpack .../libheimbase1-heimdal_1.7~git20150920+dfsg-4ubuntu1.16.04.1_amd64.deb ...
Unpacking libheimbase1-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Selecting previously unselected package libwind0-heimdal:amd64.
Preparing to unpack .../libwind0-heimdal_1.7~git20150920+dfsg-4ubuntu1.16.04.1_amd64.deb ...
Unpacking libwind0-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Selecting previously unselected package libhx509-5-heimdal:amd64.
Preparing to unpack .../libhx509-5-heimdal_1.7~git20150920+dfsg-4ubuntu1.16.04.1_amd64.deb ...
Unpacking libhx509-5-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Selecting previously unselected package libkrb5-26-heimdal:amd64.
Preparing to unpack .../libkrb5-26-heimdal_1.7~git20150920+dfsg-4ubuntu1.16.04.1_amd64.deb ...
Unpacking libkrb5-26-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Selecting previously unselected package libheimntlm0-heimdal:amd64.
Preparing to unpack .../libheimntlm0-heimdal_1.7~git20150920+dfsg-4ubuntu1.16.04.1_amd64.deb ...
Unpacking libheimntlm0-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Selecting previously unselected package libgssapi3-heimdal:amd64.
Preparing to unpack .../libgssapi3-heimdal_1.7~git20150920+dfsg-4ubuntu1.16.04.1_amd64.deb ...
Unpacking libgssapi3-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Selecting previously unselected package libsasl2-modules-db:amd64.
Preparing to unpack .../libsasl2-modules-db_2.1.26.dfsg1-14ubuntu0.1_amd64.deb ...
Unpacking libsasl2-modules-db:amd64 (2.1.26.dfsg1-14ubuntu0.1) ...
Selecting previously unselected package libsasl2-2:amd64.
Preparing to unpack .../libsasl2-2_2.1.26.dfsg1-14ubuntu0.1_amd64.deb ...
Unpacking libsasl2-2:amd64 (2.1.26.dfsg1-14ubuntu0.1) ...
Selecting previously unselected package libldap-2.4-2:amd64.
Preparing to unpack .../libldap-2.4-2_2.4.42+dfsg-2ubuntu3.7_amd64.deb ...
Unpacking libldap-2.4-2:amd64 (2.4.42+dfsg-2ubuntu3.7) ...
Selecting previously unselected package librtmp1:amd64.
Preparing to unpack .../librtmp1_2.4+20151223.gitfa8646d-1ubuntu0.1_amd64.deb ...
Unpacking librtmp1:amd64 (2.4+20151223.gitfa8646d-1ubuntu0.1) ...
Selecting previously unselected package libcurl3-gnutls:amd64.
Preparing to unpack .../libcurl3-gnutls_7.47.0-1ubuntu2.14_amd64.deb ...
Unpacking libcurl3-gnutls:amd64 (7.47.0-1ubuntu2.14) ...
Selecting previously unselected package libedit2:amd64.
Preparing to unpack .../libedit2_3.1-20150325-1ubuntu2_amd64.deb ...
Unpacking libedit2:amd64 (3.1-20150325-1ubuntu2) ...
Selecting previously unselected package libsasl2-modules:amd64.
Preparing to unpack .../libsasl2-modules_2.1.26.dfsg1-14ubuntu0.1_amd64.deb ...
Unpacking libsasl2-modules:amd64 (2.1.26.dfsg1-14ubuntu0.1) ...
Selecting previously unselected package libxmuu1:amd64.
Preparing to unpack .../libxmuu1_2%3a1.1.2-2_amd64.deb ...
Unpacking libxmuu1:amd64 (2:1.1.2-2) ...
Selecting previously unselected package openssh-client.
Preparing to unpack .../openssh-client_1%3a7.2p2-4ubuntu2.8_amd64.deb ...
Unpacking openssh-client (1:7.2p2-4ubuntu2.8) ...
Selecting previously unselected package rsync.
Preparing to unpack .../rsync_3.1.1-3ubuntu1.2_amd64.deb ...
Unpacking rsync (3.1.1-3ubuntu1.2) ...
Selecting previously unselected package xauth.
Preparing to unpack .../xauth_1%3a1.0.9-1ubuntu2_amd64.deb ...
Unpacking xauth (1:1.0.9-1ubuntu2) ...
Selecting previously unselected package liberror-perl.
Preparing to unpack .../liberror-perl_0.17-1.2_all.deb ...
Unpacking liberror-perl (0.17-1.2) ...
Selecting previously unselected package git-man.
Preparing to unpack .../git-man_1%3a2.7.4-0ubuntu1.6_all.deb ...
Unpacking git-man (1:2.7.4-0ubuntu1.6) ...
Selecting previously unselected package git.
Preparing to unpack .../git_1%3a2.7.4-0ubuntu1.6_amd64.deb ...
Unpacking git (1:2.7.4-0ubuntu1.6) ...
Selecting previously unselected package patch.
Preparing to unpack .../patch_2.7.5-1ubuntu0.16.04.2_amd64.deb ...
Unpacking patch (2.7.5-1ubuntu0.16.04.2) ...
Selecting previously unselected package rename.
Preparing to unpack .../archives/rename_0.20-4_all.deb ...
Unpacking rename (0.20-4) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Processing triggers for systemd (229-4ubuntu21.22) ...
Setting up libatm1:amd64 (1:2.5.1-1.5) ...
Setting up libmnl0:amd64 (1.0.3-5) ...
Setting up libpopt0:amd64 (1.16-10) ...
Setting up libgdbm3:amd64 (1.8.3-13.1) ...
Setting up libxau6:amd64 (1:1.0.8-1) ...
Setting up libxdmcp6:amd64 (1:1.1.2-1.1) ...
Setting up libxcb1:amd64 (1.11.1-1ubuntu1) ...
Setting up libx11-data (2:1.6.3-1ubuntu2.1) ...
Setting up libx11-6:amd64 (2:1.6.3-1ubuntu2.1) ...
Setting up libxext6:amd64 (2:1.3.3-1) ...
Setting up perl-modules-5.22 (5.22.1-9ubuntu0.6) ...
Setting up libperl5.22:amd64 (5.22.1-9ubuntu0.6) ...
Setting up perl (5.22.1-9ubuntu0.6) ...
update-alternatives: using /usr/bin/prename to provide /usr/bin/rename (rename) in auto mode
Setting up iproute2 (4.3.0-1ubuntu3.16.04.5) ...
Setting up ifupdown (0.8.10ubuntu1.4) ...
Creating /etc/network/interfaces.
Setting up libisc-export160 (1:9.10.3.dfsg.P4-8ubuntu1.15) ...
Setting up libdns-export162 (1:9.10.3.dfsg.P4-8ubuntu1.15) ...
Setting up isc-dhcp-client (4.3.3-5ubuntu12.10) ...
Setting up isc-dhcp-common (4.3.3-5ubuntu12.10) ...
Setting up less (481-2.1ubuntu0.2) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
Setting up libbsd0:amd64 (0.8.2-1) ...
Setting up libexpat1:amd64 (2.1.0-7ubuntu0.16.04.5) ...
Setting up libffi6:amd64 (3.2.1-4) ...
Setting up libgmp10:amd64 (2:6.1.0+dfsg-2) ...
Setting up libnettle6:amd64 (3.2-1ubuntu0.16.04.1) ...
Setting up libhogweed4:amd64 (3.2-1ubuntu0.16.04.1) ...
Setting up libidn11:amd64 (1.32-3ubuntu1.2) ...
Setting up libp11-kit0:amd64 (0.23.2-5~ubuntu16.04.1) ...
Setting up libtasn1-6:amd64 (4.7-3ubuntu0.16.04.3) ...
Setting up libgnutls30:amd64 (3.4.10-4ubuntu1.5) ...
Setting up libsqlite3-0:amd64 (3.11.0-1ubuntu1.2) ...
Setting up libssl1.0.0:amd64 (1.0.2g-1ubuntu4.15) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
Setting up libxtables11:amd64 (1.6.0-2ubuntu3) ...
Setting up netbase (5.3) ...
Setting up openssl (1.0.2g-1ubuntu4.15) ...
Setting up ca-certificates (20170717~16.04.2) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
Setting up krb5-locales (1.13.2+dfsg-5ubuntu2.1) ...
Setting up libroken18-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Setting up libasn1-8-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Setting up libkrb5support0:amd64 (1.13.2+dfsg-5ubuntu2.1) ...
Setting up libk5crypto3:amd64 (1.13.2+dfsg-5ubuntu2.1) ...
Setting up libkeyutils1:amd64 (1.5.9-8ubuntu1) ...
Setting up libkrb5-3:amd64 (1.13.2+dfsg-5ubuntu2.1) ...
Setting up libgssapi-krb5-2:amd64 (1.13.2+dfsg-5ubuntu2.1) ...
Setting up libhcrypto4-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Setting up libheimbase1-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Setting up libwind0-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Setting up libhx509-5-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Setting up libkrb5-26-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Setting up libheimntlm0-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Setting up libgssapi3-heimdal:amd64 (1.7~git20150920+dfsg-4ubuntu1.16.04.1) ...
Setting up libsasl2-modules-db:amd64 (2.1.26.dfsg1-14ubuntu0.1) ...
Setting up libsasl2-2:amd64 (2.1.26.dfsg1-14ubuntu0.1) ...
Setting up libldap-2.4-2:amd64 (2.4.42+dfsg-2ubuntu3.7) ...
Setting up librtmp1:amd64 (2.4+20151223.gitfa8646d-1ubuntu0.1) ...
Setting up libcurl3-gnutls:amd64 (7.47.0-1ubuntu2.14) ...
Setting up libedit2:amd64 (3.1-20150325-1ubuntu2) ...
Setting up libsasl2-modules:amd64 (2.1.26.dfsg1-14ubuntu0.1) ...
Setting up libxmuu1:amd64 (2:1.1.2-2) ...
Setting up openssh-client (1:7.2p2-4ubuntu2.8) ...
Setting up rsync (3.1.1-3ubuntu1.2) ...
invoke-rc.d: could not determine current runlevel
invoke-rc.d: policy-rc.d denied execution of restart.
Setting up xauth (1:1.0.9-1ubuntu2) ...
Setting up liberror-perl (0.17-1.2) ...
Setting up git-man (1:2.7.4-0ubuntu1.6) ...
Setting up git (1:2.7.4-0ubuntu1.6) ...
Setting up patch (2.7.5-1ubuntu0.16.04.2) ...
Setting up rename (0.20-4) ...
update-alternatives: using /usr/bin/file-rename to provide /usr/bin/rename (rename) in auto mode
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Processing triggers for systemd (229-4ubuntu21.22) ...
Processing triggers for ca-certificates (20170717~16.04.2) ...
Updating certificates in /etc/ssl/certs...
148 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
Reading package lists...
Building dependency tree...
Reading state information...
Suggested packages:
  make-doc
The following NEW packages will be installed:
  make
0 upgraded, 1 newly installed, 0 to remove and 4 not upgraded.
Need to get 151 kB of archives.
After this operation, 365 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial/main amd64 make amd64 4.1-6 [151 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 151 kB in 2s (70.0 kB/s)
Selecting previously unselected package make.
(Reading database ... 8668 files and directories currently installed.)
Preparing to unpack .../archives/make_4.1-6_amd64.deb ...
Unpacking make (4.1-6) ...
Setting up make (4.1-6) ...
Reading package lists...
Building dependency tree...
Reading state information...
The following NEW packages will be installed:
  curl
0 upgraded, 1 newly installed, 0 to remove and 4 not upgraded.
Need to get 139 kB of archives.
After this operation, 340 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 curl amd64 7.47.0-1ubuntu2.14 [139 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 139 kB in 1s (89.0 kB/s)
Selecting previously unselected package curl.
(Reading database ... 8684 files and directories currently installed.)
Preparing to unpack .../curl_7.47.0-1ubuntu2.14_amd64.deb ...
Unpacking curl (7.47.0-1ubuntu2.14) ...
Setting up curl (7.47.0-1ubuntu2.14) ...
Reading package lists...
Building dependency tree...
Reading state information...
The following NEW packages will be installed:
  xz-utils
0 upgraded, 1 newly installed, 0 to remove and 4 not upgraded.
Need to get 78.8 kB of archives.
After this operation, 393 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial/main amd64 xz-utils amd64 5.1.1alpha+20120614-2ubuntu2 [78.8 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 78.8 kB in 1s (59.2 kB/s)
Selecting previously unselected package xz-utils.
(Reading database ... 8691 files and directories currently installed.)
Preparing to unpack .../xz-utils_5.1.1alpha+20120614-2ubuntu2_amd64.deb ...
Unpacking xz-utils (5.1.1alpha+20120614-2ubuntu2) ...
Setting up xz-utils (5.1.1alpha+20120614-2ubuntu2) ...
update-alternatives: using /usr/bin/xz to provide /usr/bin/lzma (lzma) in auto mode
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  libmagic1
The following NEW packages will be installed:
  file libmagic1
0 upgraded, 2 newly installed, 0 to remove and 4 not upgraded.
Need to get 237 kB of archives.
After this operation, 4156 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libmagic1 amd64 1:5.25-2ubuntu1.2 [216 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 file amd64 1:5.25-2ubuntu1.2 [21.2 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 237 kB in 2s (99.7 kB/s)
Selecting previously unselected package libmagic1:amd64.
(Reading database ... 8729 files and directories currently installed.)
Preparing to unpack .../libmagic1_1%3a5.25-2ubuntu1.2_amd64.deb ...
Unpacking libmagic1:amd64 (1:5.25-2ubuntu1.2) ...
Selecting previously unselected package file.
Preparing to unpack .../file_1%3a5.25-2ubuntu1.2_amd64.deb ...
Unpacking file (1:5.25-2ubuntu1.2) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Setting up libmagic1:amd64 (1:5.25-2ubuntu1.2) ...
Setting up file (1:5.25-2ubuntu1.2) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Reading package lists...
Building dependency tree...
Reading state information...
The following NEW packages will be installed:
  sudo
0 upgraded, 1 newly installed, 0 to remove and 4 not upgraded.
Need to get 390 kB of archives.
After this operation, 1622 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 sudo amd64 1.8.16-0ubuntu1.7 [390 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 390 kB in 1s (202 kB/s)
Selecting previously unselected package sudo.
(Reading database ... 8755 files and directories currently installed.)
Preparing to unpack .../sudo_1.8.16-0ubuntu1.7_amd64.deb ...
Unpacking sudo (1.8.16-0ubuntu1.7) ...
Setting up sudo (1.8.16-0ubuntu1.7) ...
Reading package lists...
Building dependency tree...
Reading state information...
The following NEW packages will be installed:
  wget
0 upgraded, 1 newly installed, 0 to remove and 4 not upgraded.
Need to get 299 kB of archives.
After this operation, 905 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 wget amd64 1.17.1-1ubuntu1.5 [299 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 299 kB in 1s (158 kB/s)
Selecting previously unselected package wget.
(Reading database ... 8808 files and directories currently installed.)
Preparing to unpack .../wget_1.17.1-1ubuntu1.5_amd64.deb ...
Unpacking wget (1.17.1-1ubuntu1.5) ...
Setting up wget (1.17.1-1ubuntu1.5) ...
Removing intermediate container 4d5726d908af
 ---> 34d7a447e204
Step 3/19 : RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git    && cd mecab-ipadic-neologd    && bin/install-mecab-ipadic-neologd -n -y
 ---> Running in 979fd9db514e
Cloning into 'mecab-ipadic-neologd'...
[install-mecab-ipadic-NEologd] : Start..
[install-mecab-ipadic-NEologd] : Check the existance of libraries
[install-mecab-ipadic-NEologd] :     find => ok
[install-mecab-ipadic-NEologd] :     sort => ok
[install-mecab-ipadic-NEologd] :     head => ok
[install-mecab-ipadic-NEologd] :     cut => ok
[install-mecab-ipadic-NEologd] :     egrep => ok
[install-mecab-ipadic-NEologd] :     mecab => ok
[install-mecab-ipadic-NEologd] :     mecab-config => ok
[install-mecab-ipadic-NEologd] :     make => ok
[install-mecab-ipadic-NEologd] :     curl => ok
[install-mecab-ipadic-NEologd] :     sed => ok
[install-mecab-ipadic-NEologd] :     cat => ok
[install-mecab-ipadic-NEologd] :     diff => ok
[install-mecab-ipadic-NEologd] :     tar => ok
[install-mecab-ipadic-NEologd] :     unxz => ok
[install-mecab-ipadic-NEologd] :     xargs => ok
[install-mecab-ipadic-NEologd] :     grep => ok
[install-mecab-ipadic-NEologd] :     iconv => ok
[install-mecab-ipadic-NEologd] :     patch => ok
[install-mecab-ipadic-NEologd] :     which => ok
[install-mecab-ipadic-NEologd] :     file => ok
[install-mecab-ipadic-NEologd] :     openssl => ok
[install-mecab-ipadic-NEologd] :     awk => ok

[install-mecab-ipadic-NEologd] : mecab-ipadic-NEologd is already up-to-date

[install-mecab-ipadic-NEologd] : mecab-ipadic-NEologd will be install to /usr/lib/mecab/dic/mecab-ipadic-neologd

[install-mecab-ipadic-NEologd] : Make mecab-ipadic-NEologd
[make-mecab-ipadic-NEologd] : Start..
[make-mecab-ipadic-NEologd] : Check local seed directory
[make-mecab-ipadic-NEologd] : Check local seed file
[make-mecab-ipadic-NEologd] : Check local build directory
[make-mecab-ipadic-NEologd] : create /mecab-ipadic-neologd/libexec/../build
[make-mecab-ipadic-NEologd] : Download original mecab-ipadic file
[make-mecab-ipadic-NEologd] : Try to access to https://ja.osdn.net
[make-mecab-ipadic-NEologd] : Try to download from https://ja.osdn.net/frs/g_redir.php?m=kent&f=mecab%2Fmecab-ipadic%2F2.7.0-20070801%2Fmecab-ipadic-2.7.0-20070801.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 11.6M  100 11.6M    0     0  16.4M      0 --:--:-- --:--:-- --:--:-- 16.4M
Hash value of /mecab-ipadic-neologd/libexec/../build/mecab-ipadic-2.7.0-20070801.tar.gz matched
[make-mecab-ipadic-NEologd] : Decompress original mecab-ipadic file
mecab-ipadic-2.7.0-20070801/
mecab-ipadic-2.7.0-20070801/README
mecab-ipadic-2.7.0-20070801/AUTHORS
mecab-ipadic-2.7.0-20070801/COPYING
mecab-ipadic-2.7.0-20070801/ChangeLog
mecab-ipadic-2.7.0-20070801/INSTALL
mecab-ipadic-2.7.0-20070801/Makefile.am
mecab-ipadic-2.7.0-20070801/Makefile.in
mecab-ipadic-2.7.0-20070801/NEWS
mecab-ipadic-2.7.0-20070801/aclocal.m4
mecab-ipadic-2.7.0-20070801/config.guess
mecab-ipadic-2.7.0-20070801/config.sub
mecab-ipadic-2.7.0-20070801/configure
mecab-ipadic-2.7.0-20070801/configure.in
mecab-ipadic-2.7.0-20070801/install-sh
mecab-ipadic-2.7.0-20070801/missing
mecab-ipadic-2.7.0-20070801/mkinstalldirs
mecab-ipadic-2.7.0-20070801/Adj.csv
mecab-ipadic-2.7.0-20070801/Adnominal.csv
mecab-ipadic-2.7.0-20070801/Adverb.csv
mecab-ipadic-2.7.0-20070801/Auxil.csv
mecab-ipadic-2.7.0-20070801/Conjunction.csv
mecab-ipadic-2.7.0-20070801/Filler.csv
mecab-ipadic-2.7.0-20070801/Interjection.csv
mecab-ipadic-2.7.0-20070801/Noun.adjv.csv
mecab-ipadic-2.7.0-20070801/Noun.adverbal.csv
mecab-ipadic-2.7.0-20070801/Noun.csv
mecab-ipadic-2.7.0-20070801/Noun.demonst.csv
mecab-ipadic-2.7.0-20070801/Noun.nai.csv
mecab-ipadic-2.7.0-20070801/Noun.name.csv
mecab-ipadic-2.7.0-20070801/Noun.number.csv
mecab-ipadic-2.7.0-20070801/Noun.org.csv
mecab-ipadic-2.7.0-20070801/Noun.others.csv
mecab-ipadic-2.7.0-20070801/Noun.place.csv
mecab-ipadic-2.7.0-20070801/Noun.proper.csv
mecab-ipadic-2.7.0-20070801/Noun.verbal.csv
mecab-ipadic-2.7.0-20070801/Others.csv
mecab-ipadic-2.7.0-20070801/Postp-col.csv
mecab-ipadic-2.7.0-20070801/Postp.csv
mecab-ipadic-2.7.0-20070801/Prefix.csv
mecab-ipadic-2.7.0-20070801/Suffix.csv
mecab-ipadic-2.7.0-20070801/Symbol.csv
mecab-ipadic-2.7.0-20070801/Verb.csv
mecab-ipadic-2.7.0-20070801/char.def
mecab-ipadic-2.7.0-20070801/feature.def
mecab-ipadic-2.7.0-20070801/left-id.def
mecab-ipadic-2.7.0-20070801/matrix.def
mecab-ipadic-2.7.0-20070801/pos-id.def
mecab-ipadic-2.7.0-20070801/rewrite.def
mecab-ipadic-2.7.0-20070801/right-id.def
mecab-ipadic-2.7.0-20070801/unk.def
mecab-ipadic-2.7.0-20070801/dicrc
mecab-ipadic-2.7.0-20070801/RESULT
[make-mecab-ipadic-NEologd] : Configure custom system dictionary on /mecab-ipadic-neologd/libexec/../build/mecab-ipadic-2.7.0-20070801-neologd-20190930
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking whether make sets $(MAKE)... yes
checking for working aclocal-1.4... missing
checking for working autoconf... missing
checking for working automake-1.4... missing
checking for working autoheader... missing
checking for working makeinfo... missing
checking for a BSD-compatible install... /usr/bin/install -c
checking for mecab-config... /usr/bin/mecab-config
configure: creating ./config.status
config.status: creating Makefile
[make-mecab-ipadic-NEologd] : Encode the character encoding of system dictionary resources from EUC_JP to UTF-8
./../../libexec/iconv_euc_to_utf8.sh ./Adnominal.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Adj.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Prefix.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.demonst.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Postp.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Auxil.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Symbol.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.others.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.adjv.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.number.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.place.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Conjunction.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Postp-col.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.name.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.org.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Adverb.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Verb.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.adverbal.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Others.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Interjection.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Suffix.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.nai.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.verbal.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Noun.proper.csv 
./../../libexec/iconv_euc_to_utf8.sh ./Filler.csv 
rm ./Adnominal.csv 
rm ./Adj.csv 
rm ./Prefix.csv 
rm ./Noun.demonst.csv 
rm ./Postp.csv 
rm ./Auxil.csv 
rm ./Symbol.csv 
rm ./Noun.csv 
rm ./Noun.others.csv 
rm ./Noun.adjv.csv 
rm ./Noun.number.csv 
rm ./Noun.place.csv 
rm ./Conjunction.csv 
rm ./Postp-col.csv 
rm ./Noun.name.csv 
rm ./Noun.org.csv 
rm ./Adverb.csv 
rm ./Verb.csv 
rm ./Noun.adverbal.csv 
rm ./Others.csv 
rm ./Interjection.csv 
rm ./Suffix.csv 
rm ./Noun.nai.csv 
rm ./Noun.verbal.csv 
rm ./Noun.proper.csv 
rm ./Filler.csv 
./../../libexec/iconv_euc_to_utf8.sh ./char.def 
./../../libexec/iconv_euc_to_utf8.sh ./feature.def 
./../../libexec/iconv_euc_to_utf8.sh ./right-id.def 
./../../libexec/iconv_euc_to_utf8.sh ./rewrite.def 
./../../libexec/iconv_euc_to_utf8.sh ./matrix.def 
./../../libexec/iconv_euc_to_utf8.sh ./pos-id.def 
./../../libexec/iconv_euc_to_utf8.sh ./unk.def 
./../../libexec/iconv_euc_to_utf8.sh ./left-id.def 
rm ./char.def 
rm ./feature.def 
rm ./right-id.def 
rm ./rewrite.def 
rm ./matrix.def 
rm ./pos-id.def 
rm ./unk.def 
rm ./left-id.def 
mv ./Others.csv.utf8 ./Others.csv 
mv ./char.def.utf8 ./char.def 
mv ./feature.def.utf8 ./feature.def 
mv ./Noun.verbal.csv.utf8 ./Noun.verbal.csv 
mv ./Suffix.csv.utf8 ./Suffix.csv 
mv ./Noun.adverbal.csv.utf8 ./Noun.adverbal.csv 
mv ./Noun.nai.csv.utf8 ./Noun.nai.csv 
mv ./Adverb.csv.utf8 ./Adverb.csv 
mv ./Noun.proper.csv.utf8 ./Noun.proper.csv 
mv ./rewrite.def.utf8 ./rewrite.def 
mv ./Prefix.csv.utf8 ./Prefix.csv 
mv ./Noun.number.csv.utf8 ./Noun.number.csv 
mv ./Auxil.csv.utf8 ./Auxil.csv 
mv ./unk.def.utf8 ./unk.def 
mv ./left-id.def.utf8 ./left-id.def 
mv ./Filler.csv.utf8 ./Filler.csv 
mv ./Interjection.csv.utf8 ./Interjection.csv 
mv ./Adj.csv.utf8 ./Adj.csv 
mv ./Postp.csv.utf8 ./Postp.csv 
mv ./Noun.place.csv.utf8 ./Noun.place.csv 
mv ./right-id.def.utf8 ./right-id.def 
mv ./pos-id.def.utf8 ./pos-id.def 
mv ./Noun.demonst.csv.utf8 ./Noun.demonst.csv 
mv ./Symbol.csv.utf8 ./Symbol.csv 
mv ./Noun.csv.utf8 ./Noun.csv 
mv ./matrix.def.utf8 ./matrix.def 
mv ./Noun.others.csv.utf8 ./Noun.others.csv 
mv ./Postp-col.csv.utf8 ./Postp-col.csv 
mv ./Noun.name.csv.utf8 ./Noun.name.csv 
mv ./Adnominal.csv.utf8 ./Adnominal.csv 
mv ./Noun.adjv.csv.utf8 ./Noun.adjv.csv 
mv ./Conjunction.csv.utf8 ./Conjunction.csv 
mv ./Noun.org.csv.utf8 ./Noun.org.csv 
mv ./Verb.csv.utf8 ./Verb.csv 
[make-mecab-ipadic-NEologd] : Fix yomigana field of IPA dictionary
patching file Noun.csv
patching file Noun.place.csv
patching file Verb.csv
patching file Noun.verbal.csv
patching file Noun.name.csv
patching file Noun.adverbal.csv
patching file Noun.csv
patching file Noun.name.csv
patching file Noun.org.csv
patching file Noun.others.csv
patching file Noun.place.csv
patching file Noun.proper.csv
patching file Noun.verbal.csv
patching file Prefix.csv
patching file Suffix.csv
patching file Noun.proper.csv
patching file Noun.csv
patching file Noun.name.csv
patching file Noun.org.csv
patching file Noun.place.csv
patching file Noun.proper.csv
patching file Noun.verbal.csv
patching file Noun.name.csv
patching file Noun.org.csv
patching file Noun.place.csv
patching file Noun.proper.csv
patching file Suffix.csv
patching file Noun.demonst.csv
patching file Noun.csv
patching file Noun.name.csv
[make-mecab-ipadic-NEologd] : Copy user dictionary resource
[make-mecab-ipadic-NEologd] : Install adverb entries using /mecab-ipadic-neologd/libexec/../seed/neologd-adverb-dict-seed.20150623.csv.xz
[make-mecab-ipadic-NEologd] : Install interjection entries using /mecab-ipadic-neologd/libexec/../seed/neologd-interjection-dict-seed.20170216.csv.xz
[make-mecab-ipadic-NEologd] : Install noun orthographic variant entries using /mecab-ipadic-neologd/libexec/../seed/neologd-common-noun-ortho-variant-dict-seed.20170228.csv.xz
[make-mecab-ipadic-NEologd] : Install noun orthographic variant entries using /mecab-ipadic-neologd/libexec/../seed/neologd-proper-noun-ortho-variant-dict-seed.20161110.csv.xz
[make-mecab-ipadic-NEologd] : Install entries of orthographic variant of a noun used as verb form using /mecab-ipadic-neologd/libexec/../seed/neologd-noun-sahen-conn-ortho-variant-dict-seed.20160323.csv.xz
[make-mecab-ipadic-NEologd] : Install frequent adjective orthographic variant entries using /mecab-ipadic-neologd/libexec/../seed/neologd-adjective-std-dict-seed.20151126.csv.xz
[make-mecab-ipadic-NEologd] : Not install /mecab-ipadic-neologd/libexec/../seed/neologd-adjective-exp-dict-seed.20151126.csv.xz
[make-mecab-ipadic-NEologd] :     When you install neologd-adjective-exp-dict-seed.20151126.csv.xz, please set --install_adjective_exp option

[make-mecab-ipadic-NEologd] : Install adjective verb orthographic variant entries using /mecab-ipadic-neologd/libexec/../seed/neologd-adjective-verb-dict-seed.20160324.csv.xz
[make-mecab-ipadic-NEologd] : Not install /mecab-ipadic-neologd/libexec/../seed/neologd-date-time-infreq-dict-seed.20190415.csv.xz
[make-mecab-ipadic-NEologd] :     When you install neologd-date-time-infreq-dict-seed.20190415.csv.xz, please set --install_infreq_datetime option

[make-mecab-ipadic-NEologd] : Not install /mecab-ipadic-neologd/libexec/../seed/neologd-quantity-infreq-dict-seed.20190415.csv.xz
[make-mecab-ipadic-NEologd] :     When you install neologd-quantity-infreq-dict-seed.20190415.csv.xz, please set --install_infreq_quantity option

[make-mecab-ipadic-NEologd] : Install entries of ill formed words using /mecab-ipadic-neologd/libexec/../seed/neologd-ill-formed-words-dict-seed.20170127.csv.xz
[make-mecab-ipadic-NEologd] : Re-Index system dictionary
reading ./unk.def ... 40
emitting double-array: 100% |###########################################| 
./model.def is not found. skipped.
reading ./Adnominal.csv ... 135
reading ./mecab-user-dict-seed.20190930.csv ... 3160313
reading ./Adj.csv ... 27210
reading ./Prefix.csv ... 224
reading ./Noun.demonst.csv ... 120
reading ./neologd-adjective-std-dict-seed.20151126.csv ... 507812
reading ./Postp.csv ... 146
reading ./Auxil.csv ... 199
reading ./Symbol.csv ... 208
reading ./neologd-proper-noun-ortho-variant-dict-seed.20161110.csv ... 138379
reading ./Noun.csv ... 60734
reading ./Noun.others.csv ... 153
reading ./neologd-adjective-verb-dict-seed.20160324.csv ... 20268
reading ./neologd-common-noun-ortho-variant-dict-seed.20170228.csv ... 152869
reading ./Noun.adjv.csv ... 3328
reading ./Noun.number.csv ... 42
reading ./Noun.place.csv ... 73194
reading ./neologd-adverb-dict-seed.20150623.csv ... 139792
reading ./Conjunction.csv ... 171
reading ./Postp-col.csv ... 91
reading ./Noun.name.csv ... 34215
reading ./Noun.org.csv ... 17149
reading ./Adverb.csv ... 3032
reading ./Verb.csv ... 130750
reading ./Noun.adverbal.csv ... 808
reading ./Others.csv ... 2
reading ./Interjection.csv ... 252
reading ./Suffix.csv ... 1448
reading ./Noun.nai.csv ... 42
reading ./Noun.verbal.csv ... 12150
reading ./neologd-ill-formed-words-dict-seed.20170127.csv ... 60616
reading ./neologd-interjection-dict-seed.20170216.csv ... 4701
reading ./Noun.proper.csv ... 27493
reading ./Filler.csv ... 19
reading ./neologd-noun-sahen-conn-ortho-variant-dict-seed.20160323.csv ... 26058
emitting double-array: 100% |###########################################| 
reading ./matrix.def ... 1316x1316
emitting matrix      : 100% |###########################################| 

done!
[make-mecab-ipadic-NEologd] : Make custom system dictionary on /mecab-ipadic-neologd/libexec/../build/mecab-ipadic-2.7.0-20070801-neologd-20190930
make: Nothing to be done for 'all'.
[make-mecab-ipadic-NEologd] : Finish..
[install-mecab-ipadic-NEologd] : OK. Let's install mecab-ipadic-NEologd.
[install-mecab-ipadic-NEologd] : Start..
[install-mecab-ipadic-NEologd] : /usr/lib/mecab/dic isn't current user's directory
[install-mecab-ipadic-NEologd] : Sudo make install to /usr/lib/mecab/dic/mecab-ipadic-neologd
make[1]: Entering directory '/mecab-ipadic-neologd/build/mecab-ipadic-2.7.0-20070801-neologd-20190930'
make[1]: Nothing to be done for 'install-exec-am'.
/bin/bash ./mkinstalldirs /usr/lib/mecab/dic/mecab-ipadic-neologd
mkdir /usr/lib/mecab/dic
mkdir /usr/lib/mecab/dic/mecab-ipadic-neologd
 /usr/bin/install -c -m 644 ./matrix.bin /usr/lib/mecab/dic/mecab-ipadic-neologd/matrix.bin
 /usr/bin/install -c -m 644 ./char.bin /usr/lib/mecab/dic/mecab-ipadic-neologd/char.bin
 /usr/bin/install -c -m 644 ./sys.dic /usr/lib/mecab/dic/mecab-ipadic-neologd/sys.dic
 /usr/bin/install -c -m 644 ./unk.dic /usr/lib/mecab/dic/mecab-ipadic-neologd/unk.dic
 /usr/bin/install -c -m 644 ./left-id.def /usr/lib/mecab/dic/mecab-ipadic-neologd/left-id.def
 /usr/bin/install -c -m 644 ./right-id.def /usr/lib/mecab/dic/mecab-ipadic-neologd/right-id.def
 /usr/bin/install -c -m 644 ./rewrite.def /usr/lib/mecab/dic/mecab-ipadic-neologd/rewrite.def
 /usr/bin/install -c -m 644 ./pos-id.def /usr/lib/mecab/dic/mecab-ipadic-neologd/pos-id.def
 /usr/bin/install -c -m 644 ./dicrc /usr/lib/mecab/dic/mecab-ipadic-neologd/dicrc
make[1]: Leaving directory '/mecab-ipadic-neologd/build/mecab-ipadic-2.7.0-20070801-neologd-20190930'

[install-mecab-ipadic-NEologd] : Install completed.
[install-mecab-ipadic-NEologd] : When you use MeCab, you can set '/usr/lib/mecab/dic/mecab-ipadic-neologd' as a value of '-d' option of MeCab.
[install-mecab-ipadic-NEologd] : Usage of mecab-ipadic-NEologd is here.
Usage:
    $ mecab -d /usr/lib/mecab/dic/mecab-ipadic-neologd ...

[install-mecab-ipadic-NEologd] : Finish..
[install-mecab-ipadic-NEologd] : Finish..
Removing intermediate container 979fd9db514e
 ---> d0fe7420cee4
Step 4/19 : RUN apt-get install -y software-properties-common vim
 ---> Running in 1c8d8c345aa0
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  cron dbus dh-python distro-info-data gir1.2-glib-2.0 iso-codes
  libapt-inst2.0 libcap-ng0 libdbus-1-3 libdbus-glib-1-2 libgirepository-1.0-1
  libglib2.0-0 libglib2.0-data libgpm2 libicu55 libmpdec2 libpython3-stdlib
  libpython3.5 libpython3.5-minimal libpython3.5-stdlib libxml2 lsb-release
  mime-support powermgmt-base python-apt-common python3 python3-apt
  python3-dbus python3-gi python3-minimal python3-pycurl
  python3-software-properties python3.5 python3.5-minimal sgml-base
  shared-mime-info ucf unattended-upgrades vim-common vim-runtime
  xdg-user-dirs xml-core
Suggested packages:
  anacron logrotate checksecurity exim4 | postfix | mail-transport-agent
  dbus-user-session | dbus-x11 libdpkg-perl isoquery gpm lsb python3-doc
  python3-tk python3-venv python3-apt-dbg python-apt-doc python-dbus-doc
  python3-dbus-dbg libcurl4-gnutls-dev python-pycurl-doc python3-pycurl-dbg
  python3.5-venv python3.5-doc binutils binfmt-support sgml-base-doc bsd-mailx
  default-mta | mail-transport-agent needrestart ctags vim-doc vim-scripts
  vim-gnome-py2 | vim-gtk-py2 | vim-gtk3-py2 | vim-athena-py2 | vim-nox-py2
  debhelper
The following NEW packages will be installed:
  cron dbus dh-python distro-info-data gir1.2-glib-2.0 iso-codes
  libapt-inst2.0 libcap-ng0 libdbus-1-3 libdbus-glib-1-2 libgirepository-1.0-1
  libglib2.0-0 libglib2.0-data libgpm2 libicu55 libmpdec2 libpython3-stdlib
  libpython3.5 libpython3.5-minimal libpython3.5-stdlib libxml2 lsb-release
  mime-support powermgmt-base python-apt-common python3 python3-apt
  python3-dbus python3-gi python3-minimal python3-pycurl
  python3-software-properties python3.5 python3.5-minimal sgml-base
  shared-mime-info software-properties-common ucf unattended-upgrades vim
  vim-common vim-runtime xdg-user-dirs xml-core
0 upgraded, 44 newly installed, 0 to remove and 4 not upgraded.
Need to get 26.0 MB of archives.
After this operation, 122 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial/main amd64 cron amd64 3.0pl1-128ubuntu2 [68.4 kB]
Get:2 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython3.5-minimal amd64 3.5.2-2ubuntu0~16.04.8 [525 kB]
Get:3 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3.5-minimal amd64 3.5.2-2ubuntu0~16.04.8 [1598 kB]
Get:4 http://archive.ubuntu.com/ubuntu xenial/main amd64 python3-minimal amd64 3.5.1-3 [23.3 kB]
Get:5 http://archive.ubuntu.com/ubuntu xenial/main amd64 mime-support all 3.59ubuntu1 [31.0 kB]
Get:6 http://archive.ubuntu.com/ubuntu xenial/main amd64 libmpdec2 amd64 2.4.2-1 [82.6 kB]
Get:7 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython3.5-stdlib amd64 3.5.2-2ubuntu0~16.04.8 [2137 kB]
Get:8 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3.5 amd64 3.5.2-2ubuntu0~16.04.8 [165 kB]
Get:9 http://archive.ubuntu.com/ubuntu xenial/main amd64 libpython3-stdlib amd64 3.5.1-3 [6818 B]
Get:10 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 dh-python all 2.20151103ubuntu1.2 [73.9 kB]
Get:11 http://archive.ubuntu.com/ubuntu xenial/main amd64 python3 amd64 3.5.1-3 [8710 B]
Get:12 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libglib2.0-0 amd64 2.48.2-0ubuntu4.4 [1120 kB]
Get:13 http://archive.ubuntu.com/ubuntu xenial/main amd64 sgml-base all 1.26+nmu4ubuntu1 [12.5 kB]
Get:14 http://archive.ubuntu.com/ubuntu xenial/main amd64 libgpm2 amd64 1.20.4-6.1 [16.5 kB]
Get:15 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 distro-info-data all 0.28ubuntu0.12 [4638 B]
Get:16 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libapt-inst2.0 amd64 1.2.32 [55.8 kB]
Get:17 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 lsb-release all 9.20160110ubuntu0.2 [11.8 kB]
Get:18 http://archive.ubuntu.com/ubuntu xenial/main amd64 ucf all 3.0036 [52.9 kB]
Get:19 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 vim-common amd64 2:7.4.1689-3ubuntu1.3 [103 kB]
Get:20 http://archive.ubuntu.com/ubuntu xenial/main amd64 libcap-ng0 amd64 0.7.7-1 [10.9 kB]
Get:21 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdbus-1-3 amd64 1.10.6-1ubuntu3.4 [161 kB]
Get:22 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 dbus amd64 1.10.6-1ubuntu3.4 [142 kB]
Get:23 http://archive.ubuntu.com/ubuntu xenial/main amd64 libgirepository-1.0-1 amd64 1.46.0-3ubuntu1 [88.3 kB]
Get:24 http://archive.ubuntu.com/ubuntu xenial/main amd64 gir1.2-glib-2.0 amd64 1.46.0-3ubuntu1 [127 kB]
Get:25 http://archive.ubuntu.com/ubuntu xenial/main amd64 iso-codes all 3.65-1 [2268 kB]
Get:26 http://archive.ubuntu.com/ubuntu xenial/main amd64 libdbus-glib-1-2 amd64 0.106-1 [67.1 kB]
Get:27 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libglib2.0-data all 2.48.2-0ubuntu4.4 [131 kB]
Get:28 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libicu55 amd64 55.1-7ubuntu0.4 [7646 kB]
Get:29 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libxml2 amd64 2.9.3+dfsg1-1ubuntu0.6 [697 kB]
Get:30 http://archive.ubuntu.com/ubuntu xenial/main amd64 powermgmt-base all 1.31+nmu1 [7178 B]
Get:31 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 python-apt-common all 1.1.0~beta1ubuntu0.16.04.5 [16.2 kB]
Get:32 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3-apt amd64 1.1.0~beta1ubuntu0.16.04.5 [138 kB]
Get:33 http://archive.ubuntu.com/ubuntu xenial/main amd64 python3-dbus amd64 1.2.0-3 [83.1 kB]
Get:34 http://archive.ubuntu.com/ubuntu xenial/main amd64 python3-gi amd64 3.20.0-0ubuntu1 [153 kB]
Get:35 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 shared-mime-info amd64 1.5-2ubuntu0.2 [405 kB]
Get:36 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 xdg-user-dirs amd64 0.15-2ubuntu6.16.04.1 [61.8 kB]
Get:37 http://archive.ubuntu.com/ubuntu xenial/main amd64 xml-core all 0.13+nmu2 [23.3 kB]
Get:38 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libpython3.5 amd64 3.5.2-2ubuntu0~16.04.8 [1360 kB]
Get:39 http://archive.ubuntu.com/ubuntu xenial/main amd64 python3-pycurl amd64 7.43.0-1ubuntu1 [42.3 kB]
Get:40 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3-software-properties all 0.96.20.9 [20.1 kB]
Get:41 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 software-properties-common all 0.96.20.9 [9452 B]
Get:42 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 unattended-upgrades all 1.1ubuntu1.18.04.7~16.04.3 [41.4 kB]
Get:43 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 vim-runtime all 2:7.4.1689-3ubuntu1.3 [5179 kB]
Get:44 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 vim amd64 2:7.4.1689-3ubuntu1.3 [1036 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 26.0 MB in 1min 4s (402 kB/s)
Selecting previously unselected package cron.
(Reading database ... 8819 files and directories currently installed.)
Preparing to unpack .../cron_3.0pl1-128ubuntu2_amd64.deb ...
Unpacking cron (3.0pl1-128ubuntu2) ...
Selecting previously unselected package libpython3.5-minimal:amd64.
Preparing to unpack .../libpython3.5-minimal_3.5.2-2ubuntu0~16.04.8_amd64.deb ...
Unpacking libpython3.5-minimal:amd64 (3.5.2-2ubuntu0~16.04.8) ...
Selecting previously unselected package python3.5-minimal.
Preparing to unpack .../python3.5-minimal_3.5.2-2ubuntu0~16.04.8_amd64.deb ...
Unpacking python3.5-minimal (3.5.2-2ubuntu0~16.04.8) ...
Selecting previously unselected package python3-minimal.
Preparing to unpack .../python3-minimal_3.5.1-3_amd64.deb ...
Unpacking python3-minimal (3.5.1-3) ...
Selecting previously unselected package mime-support.
Preparing to unpack .../mime-support_3.59ubuntu1_all.deb ...
Unpacking mime-support (3.59ubuntu1) ...
Selecting previously unselected package libmpdec2:amd64.
Preparing to unpack .../libmpdec2_2.4.2-1_amd64.deb ...
Unpacking libmpdec2:amd64 (2.4.2-1) ...
Selecting previously unselected package libpython3.5-stdlib:amd64.
Preparing to unpack .../libpython3.5-stdlib_3.5.2-2ubuntu0~16.04.8_amd64.deb ...
Unpacking libpython3.5-stdlib:amd64 (3.5.2-2ubuntu0~16.04.8) ...
Selecting previously unselected package python3.5.
Preparing to unpack .../python3.5_3.5.2-2ubuntu0~16.04.8_amd64.deb ...
Unpacking python3.5 (3.5.2-2ubuntu0~16.04.8) ...
Selecting previously unselected package libpython3-stdlib:amd64.
Preparing to unpack .../libpython3-stdlib_3.5.1-3_amd64.deb ...
Unpacking libpython3-stdlib:amd64 (3.5.1-3) ...
Selecting previously unselected package dh-python.
Preparing to unpack .../dh-python_2.20151103ubuntu1.2_all.deb ...
Unpacking dh-python (2.20151103ubuntu1.2) ...
Processing triggers for systemd (229-4ubuntu21.22) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Setting up libpython3.5-minimal:amd64 (3.5.2-2ubuntu0~16.04.8) ...
Setting up python3.5-minimal (3.5.2-2ubuntu0~16.04.8) ...
Setting up python3-minimal (3.5.1-3) ...
Selecting previously unselected package python3.
(Reading database ... 9801 files and directories currently installed.)
Preparing to unpack .../python3_3.5.1-3_amd64.deb ...
Unpacking python3 (3.5.1-3) ...
Selecting previously unselected package libglib2.0-0:amd64.
Preparing to unpack .../libglib2.0-0_2.48.2-0ubuntu4.4_amd64.deb ...
Unpacking libglib2.0-0:amd64 (2.48.2-0ubuntu4.4) ...
Selecting previously unselected package sgml-base.
Preparing to unpack .../sgml-base_1.26+nmu4ubuntu1_all.deb ...
Unpacking sgml-base (1.26+nmu4ubuntu1) ...
Selecting previously unselected package libgpm2:amd64.
Preparing to unpack .../libgpm2_1.20.4-6.1_amd64.deb ...
Unpacking libgpm2:amd64 (1.20.4-6.1) ...
Selecting previously unselected package distro-info-data.
Preparing to unpack .../distro-info-data_0.28ubuntu0.12_all.deb ...
Unpacking distro-info-data (0.28ubuntu0.12) ...
Selecting previously unselected package libapt-inst2.0:amd64.
Preparing to unpack .../libapt-inst2.0_1.2.32_amd64.deb ...
Unpacking libapt-inst2.0:amd64 (1.2.32) ...
Selecting previously unselected package lsb-release.
Preparing to unpack .../lsb-release_9.20160110ubuntu0.2_all.deb ...
Unpacking lsb-release (9.20160110ubuntu0.2) ...
Selecting previously unselected package ucf.
Preparing to unpack .../archives/ucf_3.0036_all.deb ...
Moving old data out of the way
Unpacking ucf (3.0036) ...
Selecting previously unselected package vim-common.
Preparing to unpack .../vim-common_2%3a7.4.1689-3ubuntu1.3_amd64.deb ...
Unpacking vim-common (2:7.4.1689-3ubuntu1.3) ...
Selecting previously unselected package libcap-ng0:amd64.
Preparing to unpack .../libcap-ng0_0.7.7-1_amd64.deb ...
Unpacking libcap-ng0:amd64 (0.7.7-1) ...
Selecting previously unselected package libdbus-1-3:amd64.
Preparing to unpack .../libdbus-1-3_1.10.6-1ubuntu3.4_amd64.deb ...
Unpacking libdbus-1-3:amd64 (1.10.6-1ubuntu3.4) ...
Selecting previously unselected package dbus.
Preparing to unpack .../dbus_1.10.6-1ubuntu3.4_amd64.deb ...
Unpacking dbus (1.10.6-1ubuntu3.4) ...
Selecting previously unselected package libgirepository-1.0-1:amd64.
Preparing to unpack .../libgirepository-1.0-1_1.46.0-3ubuntu1_amd64.deb ...
Unpacking libgirepository-1.0-1:amd64 (1.46.0-3ubuntu1) ...
Selecting previously unselected package gir1.2-glib-2.0:amd64.
Preparing to unpack .../gir1.2-glib-2.0_1.46.0-3ubuntu1_amd64.deb ...
Unpacking gir1.2-glib-2.0:amd64 (1.46.0-3ubuntu1) ...
Selecting previously unselected package iso-codes.
Preparing to unpack .../iso-codes_3.65-1_all.deb ...
Unpacking iso-codes (3.65-1) ...
Selecting previously unselected package libdbus-glib-1-2:amd64.
Preparing to unpack .../libdbus-glib-1-2_0.106-1_amd64.deb ...
Unpacking libdbus-glib-1-2:amd64 (0.106-1) ...
Selecting previously unselected package libglib2.0-data.
Preparing to unpack .../libglib2.0-data_2.48.2-0ubuntu4.4_all.deb ...
Unpacking libglib2.0-data (2.48.2-0ubuntu4.4) ...
Selecting previously unselected package libicu55:amd64.
Preparing to unpack .../libicu55_55.1-7ubuntu0.4_amd64.deb ...
Unpacking libicu55:amd64 (55.1-7ubuntu0.4) ...
Selecting previously unselected package libxml2:amd64.
Preparing to unpack .../libxml2_2.9.3+dfsg1-1ubuntu0.6_amd64.deb ...
Unpacking libxml2:amd64 (2.9.3+dfsg1-1ubuntu0.6) ...
Selecting previously unselected package powermgmt-base.
Preparing to unpack .../powermgmt-base_1.31+nmu1_all.deb ...
Unpacking powermgmt-base (1.31+nmu1) ...
Selecting previously unselected package python-apt-common.
Preparing to unpack .../python-apt-common_1.1.0~beta1ubuntu0.16.04.5_all.deb ...
Unpacking python-apt-common (1.1.0~beta1ubuntu0.16.04.5) ...
Selecting previously unselected package python3-apt.
Preparing to unpack .../python3-apt_1.1.0~beta1ubuntu0.16.04.5_amd64.deb ...
Unpacking python3-apt (1.1.0~beta1ubuntu0.16.04.5) ...
Selecting previously unselected package python3-dbus.
Preparing to unpack .../python3-dbus_1.2.0-3_amd64.deb ...
Unpacking python3-dbus (1.2.0-3) ...
Selecting previously unselected package python3-gi.
Preparing to unpack .../python3-gi_3.20.0-0ubuntu1_amd64.deb ...
Unpacking python3-gi (3.20.0-0ubuntu1) ...
Selecting previously unselected package shared-mime-info.
Preparing to unpack .../shared-mime-info_1.5-2ubuntu0.2_amd64.deb ...
Unpacking shared-mime-info (1.5-2ubuntu0.2) ...
Selecting previously unselected package xdg-user-dirs.
Preparing to unpack .../xdg-user-dirs_0.15-2ubuntu6.16.04.1_amd64.deb ...
Unpacking xdg-user-dirs (0.15-2ubuntu6.16.04.1) ...
Selecting previously unselected package xml-core.
Preparing to unpack .../xml-core_0.13+nmu2_all.deb ...
Unpacking xml-core (0.13+nmu2) ...
Selecting previously unselected package libpython3.5:amd64.
Preparing to unpack .../libpython3.5_3.5.2-2ubuntu0~16.04.8_amd64.deb ...
Unpacking libpython3.5:amd64 (3.5.2-2ubuntu0~16.04.8) ...
Selecting previously unselected package python3-pycurl.
Preparing to unpack .../python3-pycurl_7.43.0-1ubuntu1_amd64.deb ...
Unpacking python3-pycurl (7.43.0-1ubuntu1) ...
Selecting previously unselected package python3-software-properties.
Preparing to unpack .../python3-software-properties_0.96.20.9_all.deb ...
Unpacking python3-software-properties (0.96.20.9) ...
Selecting previously unselected package software-properties-common.
Preparing to unpack .../software-properties-common_0.96.20.9_all.deb ...
Unpacking software-properties-common (0.96.20.9) ...
Selecting previously unselected package unattended-upgrades.
Preparing to unpack .../unattended-upgrades_1.1ubuntu1.18.04.7~16.04.3_all.deb ...
Unpacking unattended-upgrades (1.1ubuntu1.18.04.7~16.04.3) ...
Selecting previously unselected package vim-runtime.
Preparing to unpack .../vim-runtime_2%3a7.4.1689-3ubuntu1.3_all.deb ...
Adding 'diversion of /usr/share/vim/vim74/doc/help.txt to /usr/share/vim/vim74/doc/help.txt.vim-tiny by vim-runtime'
Adding 'diversion of /usr/share/vim/vim74/doc/tags to /usr/share/vim/vim74/doc/tags.vim-tiny by vim-runtime'
Unpacking vim-runtime (2:7.4.1689-3ubuntu1.3) ...
Selecting previously unselected package vim.
Preparing to unpack .../vim_2%3a7.4.1689-3ubuntu1.3_amd64.deb ...
Unpacking vim (2:7.4.1689-3ubuntu1.3) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Processing triggers for systemd (229-4ubuntu21.22) ...
Setting up cron (3.0pl1-128ubuntu2) ...
Adding group `crontab' (GID 108) ...
Done.
update-rc.d: warning: start and stop actions are no longer supported; falling back to defaults
update-rc.d: warning: stop runlevel arguments (1) do not match cron Default-Stop values (none)
invoke-rc.d: could not determine current runlevel
invoke-rc.d: policy-rc.d denied execution of start.
Setting up mime-support (3.59ubuntu1) ...
Setting up libmpdec2:amd64 (2.4.2-1) ...
Setting up libpython3.5-stdlib:amd64 (3.5.2-2ubuntu0~16.04.8) ...
Setting up python3.5 (3.5.2-2ubuntu0~16.04.8) ...
Setting up libpython3-stdlib:amd64 (3.5.1-3) ...
Setting up libglib2.0-0:amd64 (2.48.2-0ubuntu4.4) ...
No schema files found: doing nothing.
Setting up sgml-base (1.26+nmu4ubuntu1) ...
Setting up libgpm2:amd64 (1.20.4-6.1) ...
Setting up distro-info-data (0.28ubuntu0.12) ...
Setting up libapt-inst2.0:amd64 (1.2.32) ...
Setting up ucf (3.0036) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
Setting up vim-common (2:7.4.1689-3ubuntu1.3) ...
Setting up libcap-ng0:amd64 (0.7.7-1) ...
Setting up libdbus-1-3:amd64 (1.10.6-1ubuntu3.4) ...
Setting up dbus (1.10.6-1ubuntu3.4) ...
Setting up libgirepository-1.0-1:amd64 (1.46.0-3ubuntu1) ...
Setting up gir1.2-glib-2.0:amd64 (1.46.0-3ubuntu1) ...
Setting up iso-codes (3.65-1) ...
Setting up libdbus-glib-1-2:amd64 (0.106-1) ...
Setting up libglib2.0-data (2.48.2-0ubuntu4.4) ...
Setting up libicu55:amd64 (55.1-7ubuntu0.4) ...
Setting up libxml2:amd64 (2.9.3+dfsg1-1ubuntu0.6) ...
Setting up powermgmt-base (1.31+nmu1) ...
Setting up shared-mime-info (1.5-2ubuntu0.2) ...
Setting up xdg-user-dirs (0.15-2ubuntu6.16.04.1) ...
Setting up xml-core (0.13+nmu2) ...
Setting up libpython3.5:amd64 (3.5.2-2ubuntu0~16.04.8) ...
Setting up vim-runtime (2:7.4.1689-3ubuntu1.3) ...
Setting up vim (2:7.4.1689-3ubuntu1.3) ...
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vim (vim) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vimdiff (vimdiff) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/rvim (rvim) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/rview (rview) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vi (vi) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/view (view) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/ex (ex) in auto mode
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/editor (editor) in auto mode
Setting up python3 (3.5.1-3) ...
running python rtupdate hooks for python3.5...
running python post-rtupdate hooks for python3.5...
Setting up lsb-release (9.20160110ubuntu0.2) ...
Setting up python-apt-common (1.1.0~beta1ubuntu0.16.04.5) ...
Setting up python3-apt (1.1.0~beta1ubuntu0.16.04.5) ...
Setting up python3-dbus (1.2.0-3) ...
Setting up python3-gi (3.20.0-0ubuntu1) ...
Setting up python3-pycurl (7.43.0-1ubuntu1) ...
Setting up python3-software-properties (0.96.20.9) ...
Setting up software-properties-common (0.96.20.9) ...
Setting up unattended-upgrades (1.1ubuntu1.18.04.7~16.04.3) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline

Creating config file /etc/apt/apt.conf.d/20auto-upgrades with new version

Creating config file /etc/apt/apt.conf.d/50unattended-upgrades with new version
Setting up dh-python (2.20151103ubuntu1.2) ...
Processing triggers for systemd (229-4ubuntu21.22) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Processing triggers for sgml-base (1.26+nmu4ubuntu1) ...
Processing triggers for dbus (1.10.6-1ubuntu3.4) ...
Removing intermediate container 1c8d8c345aa0
 ---> c0197d69f564
Step 5/19 : RUN add-apt-repository ppa:jonathonf/python-3.6
 ---> Running in 6317cd875e76
 A plain backport of *just* Python 3.6. System extensions/Python libraries may or may not work.

Don't remove Python 3.5 from your system - it will break.
 More info: https://launchpad.net/~jonathonf/+archive/ubuntu/python-3.6
gpg: keyring `/tmp/tmp5uiblcje/secring.gpg' created
gpg: keyring `/tmp/tmp5uiblcje/pubring.gpg' created
gpg: requesting key F06FC659 from hkp server keyserver.ubuntu.com
gpg: /tmp/tmp5uiblcje/trustdb.gpg: trustdb created
gpg: key F06FC659: public key "Launchpad PPA for J Fernyhough" imported
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)
OK
Removing intermediate container 6317cd875e76
 ---> a0caac62b44c
Step 6/19 : RUN apt-get update
 ---> Running in d1b0c0628617
Get:1 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial InRelease [18.0 kB]
Hit:2 http://archive.ubuntu.com/ubuntu xenial InRelease
Hit:3 http://security.ubuntu.com/ubuntu xenial-security InRelease
Hit:4 http://archive.ubuntu.com/ubuntu xenial-updates InRelease
Get:5 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 Packages [5200 B]
Hit:6 http://archive.ubuntu.com/ubuntu xenial-backports InRelease
Fetched 23.2 kB in 1s (12.1 kB/s)
Reading package lists...
Removing intermediate container d1b0c0628617
 ---> b2d07f9d360c
Step 7/19 : RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
 ---> Running in 07457b3f0bae
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  binutils bzip2 cpp cpp-5 dpkg-dev fakeroot g++ g++-5 gcc gcc-5
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan2 libatomic1 libc-dev-bin libc6-dev libcc1-0 libcilkrts5 libdpkg-perl
  libexpat1-dev libfakeroot libfile-fcntllock-perl libgcc-5-dev libgomp1
  libisl15 libitm1 liblsan0 libmpc3 libmpfr4 libmpx0 libpython3.6
  libpython3.6-dev libpython3.6-minimal libpython3.6-stdlib libquadmath0
  libstdc++-5-dev libtsan0 libubsan0 linux-libc-dev manpages manpages-dev
  python-pip-whl python3-pkg-resources python3-setuptools python3-wheel
  python3.6-minimal
Suggested packages:
  binutils-doc bzip2-doc cpp-doc gcc-5-locales debian-keyring g++-multilib
  g++-5-multilib gcc-5-doc libstdc++6-5-dbg gcc-multilib autoconf automake
  libtool flex bison gdb gcc-doc gcc-5-multilib libgcc1-dbg libgomp1-dbg
  libitm1-dbg libatomic1-dbg libasan2-dbg liblsan0-dbg libtsan0-dbg
  libubsan0-dbg libcilkrts5-dbg libmpx0-dbg libquadmath0-dbg glibc-doc
  libstdc++-5-doc man-browser python-setuptools-doc python3.6-doc
  binfmt-support
Recommended packages:
  python3-dev
The following NEW packages will be installed:
  binutils build-essential bzip2 cpp cpp-5 dpkg-dev fakeroot g++ g++-5 gcc
  gcc-5 libalgorithm-diff-perl libalgorithm-diff-xs-perl
  libalgorithm-merge-perl libasan2 libatomic1 libc-dev-bin libc6-dev libcc1-0
  libcilkrts5 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-5-dev libgomp1 libisl15 libitm1 liblsan0 libmpc3 libmpfr4 libmpx0
  libpython3.6 libpython3.6-dev libpython3.6-minimal libpython3.6-stdlib
  libquadmath0 libstdc++-5-dev libtsan0 libubsan0 linux-libc-dev manpages
  manpages-dev python-pip-whl python3-pip python3-pkg-resources
  python3-setuptools python3-wheel python3.6 python3.6-dev python3.6-minimal
  python3.6-venv
0 upgraded, 52 newly installed, 0 to remove and 4 not upgraded.
Need to get 86.8 MB of archives.
After this operation, 235 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu xenial/main amd64 libmpfr4 amd64 3.1.4-1 [191 kB]
Get:2 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 libpython3.6-minimal amd64 3.6.8-1~16.04.york1 [578 kB]
Get:3 http://archive.ubuntu.com/ubuntu xenial/main amd64 libmpc3 amd64 1.0.3-1 [39.7 kB]
Get:4 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 python3.6-minimal amd64 3.6.8-1~16.04.york1 [1689 kB]
Get:5 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 bzip2 amd64 1.0.6-8ubuntu0.2 [32.5 kB]
Get:6 http://archive.ubuntu.com/ubuntu xenial/main amd64 manpages all 4.04-2 [1087 kB]
Get:7 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 libpython3.6-stdlib amd64 3.6.8-1~16.04.york1 [1968 kB]
Get:8 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 binutils amd64 2.26.1-1ubuntu1~16.04.8 [2312 kB]
Get:9 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 libpython3.6 amd64 3.6.8-1~16.04.york1 [1457 kB]
Get:10 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libc-dev-bin amd64 2.23-0ubuntu11 [68.5 kB]
Get:11 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 linux-libc-dev amd64 4.4.0-165.193 [838 kB]
Get:12 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 libpython3.6-dev amd64 3.6.8-1~16.04.york1 [39.5 MB]
Get:13 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libc6-dev amd64 2.23-0ubuntu11 [2086 kB]
Get:14 http://archive.ubuntu.com/ubuntu xenial/main amd64 libisl15 amd64 0.16.1-1 [524 kB]
Get:15 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 cpp-5 amd64 5.4.0-6ubuntu1~16.04.11 [7660 kB]
Get:16 http://archive.ubuntu.com/ubuntu xenial/main amd64 cpp amd64 4:5.3.1-1ubuntu1 [27.7 kB]
Get:17 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libcc1-0 amd64 5.4.0-6ubuntu1~16.04.11 [38.8 kB]
Get:18 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgomp1 amd64 5.4.0-6ubuntu1~16.04.11 [55.0 kB]
Get:19 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libitm1 amd64 5.4.0-6ubuntu1~16.04.11 [27.4 kB]
Get:20 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 python3.6 amd64 3.6.8-1~16.04.york1 [246 kB]
Get:21 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libatomic1 amd64 5.4.0-6ubuntu1~16.04.11 [8896 B]
Get:22 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libasan2 amd64 5.4.0-6ubuntu1~16.04.11 [264 kB]
Get:23 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 python3.6-dev amd64 3.6.8-1~16.04.york1 [508 kB]
Get:24 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 liblsan0 amd64 5.4.0-6ubuntu1~16.04.11 [105 kB]
Get:25 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial/main amd64 python3.6-venv amd64 3.6.8-1~16.04.york1 [6114 B]
Get:26 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libtsan0 amd64 5.4.0-6ubuntu1~16.04.11 [244 kB]
Get:27 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libubsan0 amd64 5.4.0-6ubuntu1~16.04.11 [95.4 kB]
Get:28 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libcilkrts5 amd64 5.4.0-6ubuntu1~16.04.11 [40.1 kB]
Get:29 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libmpx0 amd64 5.4.0-6ubuntu1~16.04.11 [9748 B]
Get:30 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libquadmath0 amd64 5.4.0-6ubuntu1~16.04.11 [131 kB]
Get:31 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libgcc-5-dev amd64 5.4.0-6ubuntu1~16.04.11 [2229 kB]
Get:32 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 gcc-5 amd64 5.4.0-6ubuntu1~16.04.11 [8417 kB]
Get:33 http://archive.ubuntu.com/ubuntu xenial/main amd64 gcc amd64 4:5.3.1-1ubuntu1 [5244 B]
Get:34 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libstdc++-5-dev amd64 5.4.0-6ubuntu1~16.04.11 [1426 kB]
Get:35 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 g++-5 amd64 5.4.0-6ubuntu1~16.04.11 [8310 kB]
Get:36 http://archive.ubuntu.com/ubuntu xenial/main amd64 g++ amd64 4:5.3.1-1ubuntu1 [1504 B]
Get:37 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libdpkg-perl all 1.18.4ubuntu1.6 [195 kB]
Get:38 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 dpkg-dev all 1.18.4ubuntu1.6 [584 kB]
Get:39 http://archive.ubuntu.com/ubuntu xenial/main amd64 build-essential amd64 12.1ubuntu2 [4758 B]
Get:40 http://archive.ubuntu.com/ubuntu xenial/main amd64 libfakeroot amd64 1.20.2-1ubuntu1 [25.5 kB]
Get:41 http://archive.ubuntu.com/ubuntu xenial/main amd64 fakeroot amd64 1.20.2-1ubuntu1 [61.8 kB]
Get:42 http://archive.ubuntu.com/ubuntu xenial/main amd64 libalgorithm-diff-perl all 1.19.03-1 [47.6 kB]
Get:43 http://archive.ubuntu.com/ubuntu xenial/main amd64 libalgorithm-diff-xs-perl amd64 0.04-4build1 [11.0 kB]
Get:44 http://archive.ubuntu.com/ubuntu xenial/main amd64 libalgorithm-merge-perl all 0.08-3 [12.0 kB]
Get:45 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libexpat1-dev amd64 2.1.0-7ubuntu0.16.04.5 [115 kB]
Get:46 http://archive.ubuntu.com/ubuntu xenial/main amd64 libfile-fcntllock-perl amd64 0.22-3 [32.0 kB]
Get:47 http://archive.ubuntu.com/ubuntu xenial/main amd64 manpages-dev all 4.04-2 [2048 kB]
Get:48 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 python-pip-whl all 8.1.1-2ubuntu0.4 [1110 kB]
Get:49 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 python3-pip all 8.1.1-2ubuntu0.4 [109 kB]
Get:50 http://archive.ubuntu.com/ubuntu xenial/main amd64 python3-pkg-resources all 20.7.0-1 [79.0 kB]
Get:51 http://archive.ubuntu.com/ubuntu xenial/main amd64 python3-setuptools all 20.7.0-1 [88.0 kB]
Get:52 http://archive.ubuntu.com/ubuntu xenial/universe amd64 python3-wheel all 0.29.0-1 [48.1 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 86.8 MB in 1min 10s (1236 kB/s)
Selecting previously unselected package libpython3.6-minimal:amd64.
(Reading database ... 12854 files and directories currently installed.)
Preparing to unpack .../libpython3.6-minimal_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking libpython3.6-minimal:amd64 (3.6.8-1~16.04.york1) ...
Selecting previously unselected package python3.6-minimal.
Preparing to unpack .../python3.6-minimal_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking python3.6-minimal (3.6.8-1~16.04.york1) ...
Selecting previously unselected package libmpfr4:amd64.
Preparing to unpack .../libmpfr4_3.1.4-1_amd64.deb ...
Unpacking libmpfr4:amd64 (3.1.4-1) ...
Selecting previously unselected package libmpc3:amd64.
Preparing to unpack .../libmpc3_1.0.3-1_amd64.deb ...
Unpacking libmpc3:amd64 (1.0.3-1) ...
Selecting previously unselected package bzip2.
Preparing to unpack .../bzip2_1.0.6-8ubuntu0.2_amd64.deb ...
Unpacking bzip2 (1.0.6-8ubuntu0.2) ...
Selecting previously unselected package manpages.
Preparing to unpack .../manpages_4.04-2_all.deb ...
Unpacking manpages (4.04-2) ...
Selecting previously unselected package binutils.
Preparing to unpack .../binutils_2.26.1-1ubuntu1~16.04.8_amd64.deb ...
Unpacking binutils (2.26.1-1ubuntu1~16.04.8) ...
Selecting previously unselected package libc-dev-bin.
Preparing to unpack .../libc-dev-bin_2.23-0ubuntu11_amd64.deb ...
Unpacking libc-dev-bin (2.23-0ubuntu11) ...
Selecting previously unselected package linux-libc-dev:amd64.
Preparing to unpack .../linux-libc-dev_4.4.0-165.193_amd64.deb ...
Unpacking linux-libc-dev:amd64 (4.4.0-165.193) ...
Selecting previously unselected package libc6-dev:amd64.
Preparing to unpack .../libc6-dev_2.23-0ubuntu11_amd64.deb ...
Unpacking libc6-dev:amd64 (2.23-0ubuntu11) ...
Selecting previously unselected package libisl15:amd64.
Preparing to unpack .../libisl15_0.16.1-1_amd64.deb ...
Unpacking libisl15:amd64 (0.16.1-1) ...
Selecting previously unselected package cpp-5.
Preparing to unpack .../cpp-5_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking cpp-5 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package cpp.
Preparing to unpack .../cpp_4%3a5.3.1-1ubuntu1_amd64.deb ...
Unpacking cpp (4:5.3.1-1ubuntu1) ...
Selecting previously unselected package libcc1-0:amd64.
Preparing to unpack .../libcc1-0_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libcc1-0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package libgomp1:amd64.
Preparing to unpack .../libgomp1_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libgomp1:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package libitm1:amd64.
Preparing to unpack .../libitm1_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libitm1:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package libatomic1:amd64.
Preparing to unpack .../libatomic1_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libatomic1:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package libasan2:amd64.
Preparing to unpack .../libasan2_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libasan2:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package liblsan0:amd64.
Preparing to unpack .../liblsan0_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking liblsan0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package libtsan0:amd64.
Preparing to unpack .../libtsan0_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libtsan0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package libubsan0:amd64.
Preparing to unpack .../libubsan0_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libubsan0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package libcilkrts5:amd64.
Preparing to unpack .../libcilkrts5_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libcilkrts5:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package libmpx0:amd64.
Preparing to unpack .../libmpx0_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libmpx0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package libquadmath0:amd64.
Preparing to unpack .../libquadmath0_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libquadmath0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package libgcc-5-dev:amd64.
Preparing to unpack .../libgcc-5-dev_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libgcc-5-dev:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package gcc-5.
Preparing to unpack .../gcc-5_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking gcc-5 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package gcc.
Preparing to unpack .../gcc_4%3a5.3.1-1ubuntu1_amd64.deb ...
Unpacking gcc (4:5.3.1-1ubuntu1) ...
Selecting previously unselected package libstdc++-5-dev:amd64.
Preparing to unpack .../libstdc++-5-dev_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking libstdc++-5-dev:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package g++-5.
Preparing to unpack .../g++-5_5.4.0-6ubuntu1~16.04.11_amd64.deb ...
Unpacking g++-5 (5.4.0-6ubuntu1~16.04.11) ...
Selecting previously unselected package g++.
Preparing to unpack .../g++_4%3a5.3.1-1ubuntu1_amd64.deb ...
Unpacking g++ (4:5.3.1-1ubuntu1) ...
Selecting previously unselected package libdpkg-perl.
Preparing to unpack .../libdpkg-perl_1.18.4ubuntu1.6_all.deb ...
Unpacking libdpkg-perl (1.18.4ubuntu1.6) ...
Selecting previously unselected package dpkg-dev.
Preparing to unpack .../dpkg-dev_1.18.4ubuntu1.6_all.deb ...
Unpacking dpkg-dev (1.18.4ubuntu1.6) ...
Selecting previously unselected package build-essential.
Preparing to unpack .../build-essential_12.1ubuntu2_amd64.deb ...
Unpacking build-essential (12.1ubuntu2) ...
Selecting previously unselected package libfakeroot:amd64.
Preparing to unpack .../libfakeroot_1.20.2-1ubuntu1_amd64.deb ...
Unpacking libfakeroot:amd64 (1.20.2-1ubuntu1) ...
Selecting previously unselected package fakeroot.
Preparing to unpack .../fakeroot_1.20.2-1ubuntu1_amd64.deb ...
Unpacking fakeroot (1.20.2-1ubuntu1) ...
Selecting previously unselected package libalgorithm-diff-perl.
Preparing to unpack .../libalgorithm-diff-perl_1.19.03-1_all.deb ...
Unpacking libalgorithm-diff-perl (1.19.03-1) ...
Selecting previously unselected package libalgorithm-diff-xs-perl.
Preparing to unpack .../libalgorithm-diff-xs-perl_0.04-4build1_amd64.deb ...
Unpacking libalgorithm-diff-xs-perl (0.04-4build1) ...
Selecting previously unselected package libalgorithm-merge-perl.
Preparing to unpack .../libalgorithm-merge-perl_0.08-3_all.deb ...
Unpacking libalgorithm-merge-perl (0.08-3) ...
Selecting previously unselected package libexpat1-dev:amd64.
Preparing to unpack .../libexpat1-dev_2.1.0-7ubuntu0.16.04.5_amd64.deb ...
Unpacking libexpat1-dev:amd64 (2.1.0-7ubuntu0.16.04.5) ...
Selecting previously unselected package libfile-fcntllock-perl.
Preparing to unpack .../libfile-fcntllock-perl_0.22-3_amd64.deb ...
Unpacking libfile-fcntllock-perl (0.22-3) ...
Selecting previously unselected package libpython3.6-stdlib:amd64.
Preparing to unpack .../libpython3.6-stdlib_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking libpython3.6-stdlib:amd64 (3.6.8-1~16.04.york1) ...
Selecting previously unselected package libpython3.6:amd64.
Preparing to unpack .../libpython3.6_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking libpython3.6:amd64 (3.6.8-1~16.04.york1) ...
Selecting previously unselected package libpython3.6-dev:amd64.
Preparing to unpack .../libpython3.6-dev_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking libpython3.6-dev:amd64 (3.6.8-1~16.04.york1) ...
Selecting previously unselected package manpages-dev.
Preparing to unpack .../manpages-dev_4.04-2_all.deb ...
Unpacking manpages-dev (4.04-2) ...
Selecting previously unselected package python-pip-whl.
Preparing to unpack .../python-pip-whl_8.1.1-2ubuntu0.4_all.deb ...
Unpacking python-pip-whl (8.1.1-2ubuntu0.4) ...
Selecting previously unselected package python3-pip.
Preparing to unpack .../python3-pip_8.1.1-2ubuntu0.4_all.deb ...
Unpacking python3-pip (8.1.1-2ubuntu0.4) ...
Selecting previously unselected package python3-pkg-resources.
Preparing to unpack .../python3-pkg-resources_20.7.0-1_all.deb ...
Unpacking python3-pkg-resources (20.7.0-1) ...
Selecting previously unselected package python3-setuptools.
Preparing to unpack .../python3-setuptools_20.7.0-1_all.deb ...
Unpacking python3-setuptools (20.7.0-1) ...
Selecting previously unselected package python3-wheel.
Preparing to unpack .../python3-wheel_0.29.0-1_all.deb ...
Unpacking python3-wheel (0.29.0-1) ...
Selecting previously unselected package python3.6.
Preparing to unpack .../python3.6_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking python3.6 (3.6.8-1~16.04.york1) ...
Selecting previously unselected package python3.6-dev.
Preparing to unpack .../python3.6-dev_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking python3.6-dev (3.6.8-1~16.04.york1) ...
Selecting previously unselected package python3.6-venv.
Preparing to unpack .../python3.6-venv_3.6.8-1~16.04.york1_amd64.deb ...
Unpacking python3.6-venv (3.6.8-1~16.04.york1) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Processing triggers for mime-support (3.59ubuntu1) ...
Setting up libpython3.6-minimal:amd64 (3.6.8-1~16.04.york1) ...
Setting up python3.6-minimal (3.6.8-1~16.04.york1) ...
Setting up libmpfr4:amd64 (3.1.4-1) ...
Setting up libmpc3:amd64 (1.0.3-1) ...
Setting up bzip2 (1.0.6-8ubuntu0.2) ...
Setting up manpages (4.04-2) ...
Setting up binutils (2.26.1-1ubuntu1~16.04.8) ...
Setting up libc-dev-bin (2.23-0ubuntu11) ...
Setting up linux-libc-dev:amd64 (4.4.0-165.193) ...
Setting up libc6-dev:amd64 (2.23-0ubuntu11) ...
Setting up libisl15:amd64 (0.16.1-1) ...
Setting up cpp-5 (5.4.0-6ubuntu1~16.04.11) ...
Setting up cpp (4:5.3.1-1ubuntu1) ...
Setting up libcc1-0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up libgomp1:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up libitm1:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up libatomic1:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up libasan2:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up liblsan0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up libtsan0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up libubsan0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up libcilkrts5:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up libmpx0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up libquadmath0:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up libgcc-5-dev:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up gcc-5 (5.4.0-6ubuntu1~16.04.11) ...
Setting up gcc (4:5.3.1-1ubuntu1) ...
Setting up libstdc++-5-dev:amd64 (5.4.0-6ubuntu1~16.04.11) ...
Setting up g++-5 (5.4.0-6ubuntu1~16.04.11) ...
Setting up g++ (4:5.3.1-1ubuntu1) ...
update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
Setting up libdpkg-perl (1.18.4ubuntu1.6) ...
Setting up dpkg-dev (1.18.4ubuntu1.6) ...
Setting up build-essential (12.1ubuntu2) ...
Setting up libfakeroot:amd64 (1.20.2-1ubuntu1) ...
Setting up fakeroot (1.20.2-1ubuntu1) ...
update-alternatives: using /usr/bin/fakeroot-sysv to provide /usr/bin/fakeroot (fakeroot) in auto mode
Setting up libalgorithm-diff-perl (1.19.03-1) ...
Setting up libalgorithm-diff-xs-perl (0.04-4build1) ...
Setting up libalgorithm-merge-perl (0.08-3) ...
Setting up libexpat1-dev:amd64 (2.1.0-7ubuntu0.16.04.5) ...
Setting up libfile-fcntllock-perl (0.22-3) ...
Setting up libpython3.6-stdlib:amd64 (3.6.8-1~16.04.york1) ...
Setting up libpython3.6:amd64 (3.6.8-1~16.04.york1) ...
Setting up libpython3.6-dev:amd64 (3.6.8-1~16.04.york1) ...
Setting up manpages-dev (4.04-2) ...
Setting up python-pip-whl (8.1.1-2ubuntu0.4) ...
Setting up python3-pip (8.1.1-2ubuntu0.4) ...
Setting up python3-pkg-resources (20.7.0-1) ...
Setting up python3-setuptools (20.7.0-1) ...
Setting up python3-wheel (0.29.0-1) ...
Setting up python3.6 (3.6.8-1~16.04.york1) ...
Setting up python3.6-dev (3.6.8-1~16.04.york1) ...
Setting up python3.6-venv (3.6.8-1~16.04.york1) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Removing intermediate container 07457b3f0bae
 ---> 7ae82dfc5ecc
Step 8/19 : RUN python3.6 -m pip install pip --upgrade
 ---> Running in a1bcba4317d2
Collecting pip
  Downloading https://files.pythonhosted.org/packages/30/db/9e38760b32e3e7f40cce46dd5fb107b8c73840df38f0046d8e6514e675a1/pip-19.2.3-py2.py3-none-any.whl (1.4MB)
Installing collected packages: pip
  Found existing installation: pip 8.1.1
    Not uninstalling pip at /usr/lib/python3/dist-packages, outside environment /usr
Successfully installed pip-19.2.3
Removing intermediate container a1bcba4317d2
 ---> d4335b1c01d8
Step 9/19 : RUN pip install flask
 ---> Running in 4c93be6575a4
Collecting flask
  Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
Collecting Werkzeug>=0.15 (from flask)
  Downloading https://files.pythonhosted.org/packages/ce/42/3aeda98f96e85fd26180534d36570e4d18108d62ae36f87694b476b83d6f/Werkzeug-0.16.0-py2.py3-none-any.whl (327kB)
Collecting itsdangerous>=0.24 (from flask)
  Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting click>=5.1 (from flask)
  Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
Collecting Jinja2>=2.10.1 (from flask)
  Downloading https://files.pythonhosted.org/packages/65/e0/eb35e762802015cab1ccee04e8a277b03f1d8e53da3ec3106882ec42558b/Jinja2-2.10.3-py2.py3-none-any.whl (125kB)
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10.1->flask)
  Downloading https://files.pythonhosted.org/packages/b2/5f/23e0023be6bb885d00ffbefad2942bc51a620328ee910f64abe5a8d18dd1/MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl
Installing collected packages: Werkzeug, itsdangerous, click, MarkupSafe, Jinja2, flask
Successfully installed Jinja2-2.10.3 MarkupSafe-1.1.1 Werkzeug-0.16.0 click-7.0 flask-1.1.1 itsdangerous-1.1.0
Removing intermediate container 4c93be6575a4
 ---> 68e4207ce9fa
Step 10/19 : RUN pip install numpy
 ---> Running in 0cda6eb4f84a
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/e5/e6/c3fdc53aed9fa19d6ff3abf97dfad768ae3afce1b7431f7500000816bda5/numpy-1.17.2-cp36-cp36m-manylinux1_x86_64.whl (20.4MB)
Installing collected packages: numpy
Successfully installed numpy-1.17.2
Removing intermediate container 0cda6eb4f84a
 ---> 6d28e1da96f2
Step 11/19 : RUN pip install pandas
 ---> Running in 8648baa1ce4d
Collecting pandas
  Downloading https://files.pythonhosted.org/packages/73/9b/52e228545d14f14bb2a1622e225f38463c8726645165e1cb7dde95bfe6d4/pandas-0.25.1-cp36-cp36m-manylinux1_x86_64.whl (10.5MB)
Requirement already satisfied: numpy>=1.13.3 in /usr/local/lib/python3.6/dist-packages (from pandas) (1.17.2)
Collecting pytz>=2017.2 (from pandas)
  Downloading https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl (509kB)
Collecting python-dateutil>=2.6.1 (from pandas)
  Downloading https://files.pythonhosted.org/packages/41/17/c62faccbfbd163c7f57f3844689e3a78bae1f403648a6afb1d0866d87fbb/python_dateutil-2.8.0-py2.py3-none-any.whl (226kB)
Collecting six>=1.5 (from python-dateutil>=2.6.1->pandas)
  Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Installing collected packages: pytz, six, python-dateutil, pandas
Successfully installed pandas-0.25.1 python-dateutil-2.8.0 pytz-2019.3 six-1.12.0
Removing intermediate container 8648baa1ce4d
 ---> 238fdf852177
Step 12/19 : RUN pip install sklearn
 ---> Running in 979706c4a7c7
Collecting sklearn
  Downloading https://files.pythonhosted.org/packages/1e/7a/dbb3be0ce9bd5c8b7e3d87328e79063f8b263b2b1bfa4774cb1147bfcd3f/sklearn-0.0.tar.gz
Collecting scikit-learn (from sklearn)
  Downloading https://files.pythonhosted.org/packages/a0/c5/d2238762d780dde84a20b8c761f563fe882b88c5a5fb03c056547c442a19/scikit_learn-0.21.3-cp36-cp36m-manylinux1_x86_64.whl (6.7MB)
Collecting joblib>=0.11 (from scikit-learn->sklearn)
  Downloading https://files.pythonhosted.org/packages/8f/42/155696f85f344c066e17af287359c9786b436b1bf86029bb3411283274f3/joblib-0.14.0-py2.py3-none-any.whl (294kB)
Requirement already satisfied: numpy>=1.11.0 in /usr/local/lib/python3.6/dist-packages (from scikit-learn->sklearn) (1.17.2)
Collecting scipy>=0.17.0 (from scikit-learn->sklearn)
  Downloading https://files.pythonhosted.org/packages/29/50/a552a5aff252ae915f522e44642bb49a7b7b31677f9580cfd11bcc869976/scipy-1.3.1-cp36-cp36m-manylinux1_x86_64.whl (25.2MB)
Building wheels for collected packages: sklearn
  Building wheel for sklearn (setup.py): started
  Building wheel for sklearn (setup.py): finished with status 'done'
  Created wheel for sklearn: filename=sklearn-0.0-py2.py3-none-any.whl size=2323 sha256=a7eb50f934c2a58eaab42fd992d22aeb3683433ec03040bf49a51146c72a11e3
  Stored in directory: /root/.cache/pip/wheels/76/03/bb/589d421d27431bcd2c6da284d5f2286c8e3b2ea3cf1594c074
Successfully built sklearn
Installing collected packages: joblib, scipy, scikit-learn, sklearn
Successfully installed joblib-0.14.0 scikit-learn-0.21.3 scipy-1.3.1 sklearn-0.0
Removing intermediate container 979706c4a7c7
 ---> b0de4e649124
Step 13/19 : RUN pip install gensim
 ---> Running in 1a680616b337
Collecting gensim
  Downloading https://files.pythonhosted.org/packages/d1/dd/112bd4258cee11e0baaaba064060eb156475a42362e59e3ff28e7ca2d29d/gensim-3.8.1-cp36-cp36m-manylinux1_x86_64.whl (24.2MB)
Collecting smart-open>=1.8.1 (from gensim)
  Downloading https://files.pythonhosted.org/packages/37/c0/25d19badc495428dec6a4bf7782de617ee0246a9211af75b302a2681dea7/smart_open-1.8.4.tar.gz (63kB)
Requirement already satisfied: numpy>=1.11.3 in /usr/local/lib/python3.6/dist-packages (from gensim) (1.17.2)
Requirement already satisfied: scipy>=0.18.1 in /usr/local/lib/python3.6/dist-packages (from gensim) (1.3.1)
Requirement already satisfied: six>=1.5.0 in /usr/local/lib/python3.6/dist-packages (from gensim) (1.12.0)
Collecting boto>=2.32 (from smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/23/10/c0b78c27298029e4454a472a1919bde20cb182dab1662cec7f2ca1dcc523/boto-2.49.0-py2.py3-none-any.whl (1.4MB)
Collecting requests (from smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl (57kB)
Collecting boto3 (from smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/8f/8f/a40b9d2e1b479bda3d60badaa88626636d608db0723ac3ba0614fe57a4d4/boto3-1.9.244-py2.py3-none-any.whl (128kB)
Collecting chardet<3.1.0,>=3.0.2 (from requests->smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests->smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/e0/da/55f51ea951e1b7c63a579c09dd7db825bb730ec1fe9c0180fc77bfb31448/urllib3-1.25.6-py2.py3-none-any.whl (125kB)
Collecting idna<2.9,>=2.5 (from requests->smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl (58kB)
Collecting certifi>=2017.4.17 (from requests->smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/18/b0/8146a4f8dd402f60744fa380bc73ca47303cccf8b9190fd16a827281eac2/certifi-2019.9.11-py2.py3-none-any.whl (154kB)
Collecting botocore<1.13.0,>=1.12.244 (from boto3->smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/28/cc/985436be0da63e4d7d41e476596ef853b35a1629cf26afe0a1d7b1a988e2/botocore-1.12.244-py2.py3-none-any.whl (5.7MB)
Collecting s3transfer<0.3.0,>=0.2.0 (from boto3->smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/16/8a/1fc3dba0c4923c2a76e1ff0d52b305c44606da63f718d14d3231e21c51b0/s3transfer-0.2.1-py2.py3-none-any.whl (70kB)
Collecting jmespath<1.0.0,>=0.7.1 (from boto3->smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/83/94/7179c3832a6d45b266ddb2aac329e101367fbdb11f425f13771d27f225bb/jmespath-0.9.4-py2.py3-none-any.whl
Collecting docutils<0.16,>=0.10 (from botocore<1.13.0,>=1.12.244->boto3->smart-open>=1.8.1->gensim)
  Downloading https://files.pythonhosted.org/packages/22/cd/a6aa959dca619918ccb55023b4cb151949c64d4d5d55b3f4ffd7eee0c6e8/docutils-0.15.2-py3-none-any.whl (547kB)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1; python_version >= "2.7" in /usr/local/lib/python3.6/dist-packages (from botocore<1.13.0,>=1.12.244->boto3->smart-open>=1.8.1->gensim) (2.8.0)
Building wheels for collected packages: smart-open
  Building wheel for smart-open (setup.py): started
  Building wheel for smart-open (setup.py): finished with status 'done'
  Created wheel for smart-open: filename=smart_open-1.8.4-cp36-none-any.whl size=73402 sha256=ed2992ef0225974f8323f1b483a3126074cf24f168d1f761336a800e168c2984
  Stored in directory: /root/.cache/pip/wheels/5f/ea/fb/5b1a947b369724063b2617011f1540c44eb00e28c3d2ca8692
Successfully built smart-open
Installing collected packages: boto, chardet, urllib3, idna, certifi, requests, docutils, jmespath, botocore, s3transfer, boto3, smart-open, gensim
Successfully installed boto-2.49.0 boto3-1.9.244 botocore-1.12.244 certifi-2019.9.11 chardet-3.0.4 docutils-0.15.2 gensim-3.8.1 idna-2.8 jmespath-0.9.4 requests-2.22.0 s3transfer-0.2.1 smart-open-1.8.4 urllib3-1.25.6
Removing intermediate container 1a680616b337
 ---> 5023c498c201
Step 14/19 : RUN pip install mecab-python3
 ---> Running in 3ea1a7951bea
Collecting mecab-python3
  Downloading https://files.pythonhosted.org/packages/b3/92/e7e7f38df8457fa40c1ca86928be5ddbe2bf341e90a35e6ada30d03ef16d/mecab_python3-0.996.2-cp36-cp36m-manylinux1_x86_64.whl (15.9MB)
Installing collected packages: mecab-python3
Successfully installed mecab-python3-0.996.2
Removing intermediate container 3ea1a7951bea
 ---> 7893b056ea6b
Step 15/19 : RUN pip install cloudpickle
 ---> Running in c97eaeb46d2e
Collecting cloudpickle
  Downloading https://files.pythonhosted.org/packages/c1/49/334e279caa3231255725c8e860fa93e72083567625573421db8875846c14/cloudpickle-1.2.2-py2.py3-none-any.whl
Installing collected packages: cloudpickle
Successfully installed cloudpickle-1.2.2
Removing intermediate container c97eaeb46d2e
 ---> 43b64fb2a558
Step 16/19 : RUN pip install torch
 ---> Running in b23e77f7f4cb
Collecting torch
  Downloading https://files.pythonhosted.org/packages/30/57/d5cceb0799c06733eefce80c395459f28970ebb9e896846ce96ab579a3f1/torch-1.2.0-cp36-cp36m-manylinux1_x86_64.whl (748.8MB)
Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from torch) (1.17.2)
Installing collected packages: torch
Successfully installed torch-1.2.0
Removing intermediate container b23e77f7f4cb
 ---> 75901f7945bd
Step 17/19 : RUN export LC_ALL=C.UTF-8
 ---> Running in 7b70015ee63f
Removing intermediate container 7b70015ee63f
 ---> 2debe72c622d
Step 18/19 : RUN export LANG=C.UTF-8
 ---> Running in 43192e14c168
Removing intermediate container 43192e14c168
 ---> ea663f3ceb33
Step 19/19 : EXPOSE 5000
 ---> Running in 4d1dc4c1e8d2
Removing intermediate container 4d1dc4c1e8d2
 ---> 939e163d8581
Successfully built 939e163d8581
Successfully tagged container:1.0
(base) abekensukenoMacBook-Pro:Flask anbujianjie$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
(base) abekensukenoMacBook-Pro:Flask anbujianjie$ docker images
REPOSITORY                TAG                 IMAGE ID            CREATED              SIZE
container                 1.0                 939e163d8581        About a minute ago   6.18GB
ubuntu                    16.04               657d80a6401d        2 weeks ago          121MB
lucidfrontier45/pytorch   latest              d8bc3d6b7ec5        7 weeks ago          2.96GB
(base) abekensukenoMacBook-Pro:Flask anbujianjie$ docker run  -it -p 5000:5000 -v ~/Desktop/abetter/:/abetter container:1.0
root@3e2045edcd9f:/# cd abetter/
root@3e2045edcd9f:/abetter# ls
LSTM_model.py  __pycache__  app.py  i2w.pkl  model.pkl  modeling.py  templates  tweet.js  w2i.pkl
root@3e2045edcd9f:/abetter# set FLASK_APP=app.py
root@3e2045edcd9f:/abetter# flask run
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 966, in main
    cli.main(prog_name="python -m flask" if as_module else None)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 696, in main
    _verify_python3_env()
  File "/usr/local/lib/python3.6/dist-packages/click/_unicodefun.py", line 124, in _verify_python3_env
    ' mitigation steps.' + extra
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment. Consult https://click.palletsprojects.com/en/7.x/python3/ for mitigation steps.

This system supports the C.UTF-8 locale which is recommended.
You might be able to resolve your issue by exporting the
following environment variables:

    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
root@3e2045edcd9f:/abetter# export LC_ALL=C.UTF-8
root@3e2045edcd9f:/abetter#     export LANG=C.UTF-8
root@3e2045edcd9f:/abetter# flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
^Croot@3e2045edcd9f:/abetter# vi app.py
root@3e2045edcd9f:/abetter# (base) abekensukenoMacBook-Pro:Flask anbujianjie$ pwd
/Users/anbujianjie/Desktop/Flask
(base) abekensukenoMacBook-Pro:Flask anbujianjie$ cd ../abetter/
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ pdw
-bash: pdw: command not found
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ set FLASK_APP=app.py
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [08/Oct/2019 12:37:40] "GET / HTTP/1.1" 200 -
^C(base) abekensukenoMacBook-Pro:abetter anbujianjie$ 
  [復元日時2019/10/08 12:38:49]
Last login: Tue Oct  8 12:38:44 on console
Restored session: 2019年 10月 8日 火曜日 12時37分55秒 JST
-bash: export　PATH=/Users/anbujianjie/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin: No such file or directory
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps 
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                        PORTS                    NAMES
3e2045edcd9f        container:1.0       "/bin/bash"         5 minutes ago       Exited (255) 18 seconds ago   0.0.0.0:5000->5000/tcp   upbeat_spence
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker start 3e2045edcd9f
3e2045edcd9f
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker exec 3e2045edcd9f -it bash
OCI runtime exec failed: exec failed: container_linux.go:345: starting container process caused "exec: \"-it\": executable file not found in $PATH": unknown
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker exec -it 3e2045edcd9f bash
root@3e2045edcd9f:/# pwd
/
root@3e2045edcd9f:/# cd abetter/
root@3e2045edcd9f:/abetter# ls
LSTM_model.py  __pycache__  app.py  i2w.pkl  model.pkl  modeling.py  templates  tweet.js  w2i.pkl
root@3e2045edcd9f:/abetter# set FLASK_APP=app.py
root@3e2045edcd9f:/abetter# flask run
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 966, in main
    cli.main(prog_name="python -m flask" if as_module else None)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 696, in main
    _verify_python3_env()
  File "/usr/local/lib/python3.6/dist-packages/click/_unicodefun.py", line 124, in _verify_python3_env
    ' mitigation steps.' + extra
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment. Consult https://click.palletsprojects.com/en/7.x/python3/ for mitigation steps.

This system supports the C.UTF-8 locale which is recommended.
You might be able to resolve your issue by exporting the
following environment variables:

    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
root@3e2045edcd9f:/abetter# export LC_ALL=C.UTF-8
root@3e2045edcd9f:/abetter#     export LANG=C.UTF-8
root@3e2045edcd9f:/abetter# flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
pwd
^Croot@3e2045edcd9f:/abetter# pwd
/abetter
root@3e2045edcd9f:/abetter# ls
LSTM_model.py  __pycache__  app.py  i2w.pkl  model.pkl  modeling.py  templates  tweet.js  w2i.pkl
root@3e2045edcd9f:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 03:45:49] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [08/Oct/2019 03:45:49] "GET /favicon.ico HTTP/1.1" 404 -
^Croot@3e2045edcd9f:/abetter# set FLASK_APP=modeling.py
root@3e2045edcd9f:/abetter# flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
^Croot@3e2045edcd9f:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 03:51:03] "GET / HTTP/1.1" 200 -
^Croot@3e2045edcd9f:/abetter# set FLASK_APP=modeling.py
root@3e2045edcd9f:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 03:51:25] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [08/Oct/2019 03:51:25] "GET / HTTP/1.1" 200 -
read escape sequence
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ pwd
/Users/anbujianjie/Desktop/abetter
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ ls
LSTM_model.py	__pycache__	app.py		i2w.pkl		model.pkl	modeling.py	templates	tweet.js	w2i.pkl
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ ?!doc
?docker exec -it 3e2045edcd9f bash
-bash: ?docker: command not found
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ !?doc
?docker exec -it 3e2045edcd9f bash
-bash: ?docker: command not found
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -it -p 5000:5000 -v ~/Desktop/abetter/:/abetter container:1.0
docker: Error response from daemon: driver failed programming external connectivity on endpoint naughty_feistel (c42b2e22ccc762b55795ff481ca0ab86ddea463ca2dce29c559d089a6ad84983): Bind for 0.0.0.0:5000 failed: port is already allocated.
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ pwd
/Users/anbujianjie/Desktop/abetter
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
6161e6ca3c78        container:1.0       "/bin/bash"         10 seconds ago      Created                                      naughty_feistel
3e2045edcd9f        container:1.0       "/bin/bash"         18 minutes ago      Up 12 minutes       0.0.0.0:5000->5000/tcp   upbeat_spence
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker stop 3e2045edcd9f 
3e2045edcd9f
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker stop 6161e6ca3c78
6161e6ca3c78
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm 6161e6ca3c78
6161e6ca3c78
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm 3e2045edcd9f 
3e2045edcd9f
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -it -p 5000:5000 -v ~/Desktop/abetter/:/abetter container:1.0
root@42f2975ee38b:/# pwd
/
root@42f2975ee38b:/# cd abetter/
root@42f2975ee38b:/abetter# ls
LSTM_model.py  __pycache__  app.py  i2w.pkl  model.pkl  modeling.py  templates  tweet.js  w2i.pkl
root@42f2975ee38b:/abetter# set FLASK_APP=modeling.py
root@42f2975ee38b:/abetter# flask run --host 0.0.0.0
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 966, in main
    cli.main(prog_name="python -m flask" if as_module else None)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 696, in main
    _verify_python3_env()
  File "/usr/local/lib/python3.6/dist-packages/click/_unicodefun.py", line 124, in _verify_python3_env
    ' mitigation steps.' + extra
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment. Consult https://click.palletsprojects.com/en/7.x/python3/ for mitigation steps.

This system supports the C.UTF-8 locale which is recommended.
You might be able to resolve your issue by exporting the
following environment variables:

    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
root@42f2975ee38b:/abetter# export LC_ALL=C.UTF-8
root@42f2975ee38b:/abetter#     export LANG=C.UTF-8
root@42f2975ee38b:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 03:54:27] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [08/Oct/2019 03:54:30] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [08/Oct/2019 03:54:30] "GET / HTTP/1.1" 200 -
^Croot@42f2975ee38b:/abetter# pwd
/abetter
root@42f2975ee38b:/abetter# rename app.py app2.py
Bareword "app" not allowed while "strict subs" in use at (user-supplied code).
Bareword "py" not allowed while "strict subs" in use at (user-supplied code).
root@42f2975ee38b:/abetter# mv app.py app2.py
root@42f2975ee38b:/abetter# mv modeling.py app.py
mv: cannot stat 'modeling.py': No such file or directory
root@42f2975ee38b:/abetter# ls
LSTM_model.py  __pycache__  app2.py  i2w.pkl  model.pkl  templates  tweet.js  w2i.pkl
root@42f2975ee38b:/abetter# mv app2.py app.py
root@42f2975ee38b:/abetter# flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
^Croot@42f2975ee38b:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 03:57:26] "GET / HTTP/1.1" 200 -
^Croot@42f2975ee38b:/abetter# vi app.py 
root@42f2975ee38b:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 03:58:48] "GET / HTTP/1.1" 200 -
[2019-10-08 03:58:49,987] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 72, in generate_seq
    sentence2index(start_phase), dtype=torch.int64
  File "/abetter/LSTM_model.py", line 45, in sentence2index
    wakati = make_wakati(sentences)
  File "/abetter/LSTM_model.py", line 19, in make_wakati
    tagger = MeCab.Tagger("-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
NameError: name 'MeCab' is not defined
172.17.0.1 - - [08/Oct/2019 03:58:50] "POST / HTTP/1.1" 500 -
^Croot@42f2975ee38b:/abetter# vi LSTM_model.py 
root@42f2975ee38b:/abetter# (base) abekensukenoMacBook-Pro:abetter anbujianjie$ pwd
/Users/anbujianjie/Desktop/abetter
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ ls
LSTM_model.py	__pycache__	app.py		i2w.pkl		model.pkl	templates	tweet.js	w2i.pkl
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
42f2975ee38b        container:1.0       "/bin/bash"         7 minutes ago       Up 7 minutes        0.0.0.0:5000->5000/tcp   pedantic_liskov
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
42f2975ee38b        container:1.0       "/bin/bash"         7 minutes ago       Up 7 minutes        0.0.0.0:5000->5000/tcp   pedantic_liskov
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm 42f2975ee38b
Error response from daemon: You cannot remove a running container 42f2975ee38bfb366d76f13092e9f4a23748b446a8385c6c5756836c44c66e98. Stop the container before attempting removal or force remove
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker stop 42f2975ee38b
42f2975ee38b
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm 42f2975ee38b
42f2975ee38b
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -it -p 5000:5000 -v ~/Desktop/abetter/:/abetter container:1.0
root@9760940920b7:/# set FLASK_APP=app.py
root@9760940920b7:/# flask run --host 0.0.0.0
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 966, in main
    cli.main(prog_name="python -m flask" if as_module else None)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 696, in main
    _verify_python3_env()
  File "/usr/local/lib/python3.6/dist-packages/click/_unicodefun.py", line 124, in _verify_python3_env
    ' mitigation steps.' + extra
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment. Consult https://click.palletsprojects.com/en/7.x/python3/ for mitigation steps.

This system supports the C.UTF-8 locale which is recommended.
You might be able to resolve your issue by exporting the
following environment variables:

    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
root@9760940920b7:/# export LC_ALL=C.UTF-8
root@9760940920b7:/#     export LANG=C.UTF-8
root@9760940920b7:/# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
root@9760940920b7:/# ls
abetter  bin  boot  dev  etc  home  lib  lib64  mecab-ipadic-neologd  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@9760940920b7:/# cd abetter/
root@9760940920b7:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 966, in main
    cli.main(prog_name="python -m flask" if as_module else None)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 717, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 1137, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 956, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/decorators.py", line 64, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 848, in run_command
    app = DispatchingApp(info.load_app, use_eager_loading=eager_loading)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 305, in __init__
    self._load_unlocked()
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 330, in _load_unlocked
    self._app = rv = self.loader()
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 392, in load_app
    app = locate_app(self, import_name, None, raise_if_not_found=False)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 240, in locate_app
    __import__(module_name)
  File "/abetter/app.py", line 3, in <module>
    import LSTM_model
  File "/abetter/LSTM_model.py", line 43
    net.eval()
      ^
IndentationError: expected an indented block
root@9760940920b7:/abetter# exit
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps 
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker ps  -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
9760940920b7        container:1.0       "/bin/bash"         4 minutes ago       Exited (1) 5 seconds ago                       affectionate_neumann
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker rm 9760940920b7
9760940920b7
(base) abekensukenoMacBook-Pro:abetter anbujianjie$ docker run -it -p 5000:5000 -v ~/Desktop/abetter/:/abetter container:1.0
root@0ca109d793fb:/# cd abetter/
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 966, in main
    cli.main(prog_name="python -m flask" if as_module else None)
  File "/usr/local/lib/python3.6/dist-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/click/core.py", line 696, in main
    _verify_python3_env()
  File "/usr/local/lib/python3.6/dist-packages/click/_unicodefun.py", line 124, in _verify_python3_env
    ' mitigation steps.' + extra
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment. Consult https://click.palletsprojects.com/en/7.x/python3/ for mitigation steps.

This system supports the C.UTF-8 locale which is recommended.
You might be able to resolve your issue by exporting the
following environment variables:

    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
root@0ca109d793fb:/abetter# export LC_ALL=C.UTF-8
root@0ca109d793fb:/abetter#     export LANG=C.UTF-8
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
[2019-10-08 04:07:56,640] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 47, in generate_seq
    sentence2index(start_phase), dtype=torch.int64
  File "/abetter/LSTM_model.py", line 36, in sentence2index
    wakati = make_wakati(sentences)
  File "/abetter/LSTM_model.py", line 20, in make_wakati
    tagger = MeCab.Tagger("-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
  File "/usr/local/lib/python3.6/dist-packages/MeCab/__init__.py", line 97, in __init__
    super(Tagger, self).__init__(*args)
RuntimeError
172.17.0.1 - - [08/Oct/2019 04:07:56] "POST / HTTP/1.1" 500 -
172.17.0.1 - - [08/Oct/2019 04:08:00] "GET / HTTP/1.1" 200 -
[2019-10-08 04:08:01,703] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 47, in generate_seq
    sentence2index(start_phase), dtype=torch.int64
  File "/abetter/LSTM_model.py", line 36, in sentence2index
    wakati = make_wakati(sentences)
  File "/abetter/LSTM_model.py", line 20, in make_wakati
    tagger = MeCab.Tagger("-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
  File "/usr/local/lib/python3.6/dist-packages/MeCab/__init__.py", line 97, in __init__
    super(Tagger, self).__init__(*args)
RuntimeError
172.17.0.1 - - [08/Oct/2019 04:08:01] "POST / HTTP/1.1" 500 -
^Croot@0ca109d793fb:/abetter# vi LSTM_model.py 
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
[2019-10-08 04:13:16,720] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 47, in generate_seq
    sentence2index(start_phase), dtype=torch.int64
  File "/abetter/LSTM_model.py", line 36, in sentence2index
    wakati = make_wakati(sentences)
  File "/abetter/LSTM_model.py", line 25, in make_wakati
    sentence = re.sub(r'[0-9０-９]+', "0", sentence)
NameError: name 're' is not defined
172.17.0.1 - - [08/Oct/2019 04:13:16] "POST / HTTP/1.1" 500 -
172.17.0.1 - - [08/Oct/2019 04:13:18] "GET / HTTP/1.1" 200 -
[2019-10-08 04:13:20,566] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 47, in generate_seq
    sentence2index(start_phase), dtype=torch.int64
  File "/abetter/LSTM_model.py", line 36, in sentence2index
    wakati = make_wakati(sentences)
  File "/abetter/LSTM_model.py", line 25, in make_wakati
    sentence = re.sub(r'[0-9０-９]+', "0", sentence)
NameError: name 're' is not defined
172.17.0.1 - - [08/Oct/2019 04:13:20] "POST / HTTP/1.1" 500 -
^Croot@0ca109d793fb:/abetter# vi LSTM_model.py 
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 04:13:48] "GET / HTTP/1.1" 200 -
[2019-10-08 04:13:50,759] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 48, in generate_seq
    sentence2index(start_phase), dtype=torch.int64
  File "/abetter/LSTM_model.py", line 38, in sentence2index
    with open("w2i", "rb")as data:
FileNotFoundError: [Errno 2] No such file or directory: 'w2i'
172.17.0.1 - - [08/Oct/2019 04:13:50] "POST / HTTP/1.1" 500 -
^Croot@0ca109d793fb:/abetter# ls
Dockerfile  LSTM_model.py  __pycache__  app.py  i2w.pkl  model.pkl  templates  tweet.js  w2i.pkl
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
^Croot@0ca109d793fb:/abetter# vi LSTM_model.py 
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 04:14:53] "GET / HTTP/1.1" 200 -
[2019-10-08 04:14:55,090] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 48, in generate_seq
    sentence2index(start_phase), dtype=torch.int64
  File "/abetter/LSTM_model.py", line 39, in sentence2index
    word2index = pickle.load(data)
NameError: name 'pickle' is not defined
172.17.0.1 - - [08/Oct/2019 04:14:55] "POST / HTTP/1.1" 500 -
	^Croot@0ca109d793fb:/abetter# vi LSTM_model.py 
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
[2019-10-08 04:15:28,323] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 68, in generate_seq
    res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
  File "/abetter/LSTM_model.py", line 68, in <listcomp>
    res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
KeyError: 10767
172.17.0.1 - - [08/Oct/2019 04:15:28] "POST / HTTP/1.1" 500 -
172.17.0.1 - - [08/Oct/2019 04:15:29] "GET / HTTP/1.1" 200 -
[2019-10-08 04:15:30,550] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 68, in generate_seq
    res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
  File "/abetter/LSTM_model.py", line 68, in <listcomp>
    res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
KeyError: 121
172.17.0.1 - - [08/Oct/2019 04:15:30] "POST / HTTP/1.1" 500 -
^[[A^[[B^Croot@0ca109d793fb:/abetter# vi LSTM_model.py 
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 04:25:57] "GET / HTTP/1.1" 200 -
[2019-10-08 04:26:03,462] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 68, in generate_seq
    res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
  File "/abetter/LSTM_model.py", line 68, in <listcomp>
    res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
KeyError: 6758
172.17.0.1 - - [08/Oct/2019 04:26:03] "POST / HTTP/1.1" 500 -
^Croot@0ca109d793fb:/abetter# vi LSTM_model.py 
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 04:30:32] "GET / HTTP/1.1" 200 -
{'海外': 0, 'は': 1, '許諾': 2, 'とっ': 3, 'て': 4, 'バリバリ': 5, '動画': 6, '販売': 7, 'し': 8, 'てる': 9, 'とこ': 10, 'ある': 11, 'よ': 12, 'ね': 13, '軽減税率': 14, 'って': 15, 'ギャグ': 16, 'か': 17, 'と': 18, '思っ': 19, 'たら': 20, 'マジで': 21, '実施': 22, 'さ': 23, 'れる': 24, '施策': 25, 'な': 26, 'の': 27, '0歳': 28, 'に': 29, 'なっ': 30, 'た': 31, 'けど': 32, '敬語': 33, '使い方': 34, '全く': 35, 'わから': 36, 'ない': 37, 'こう': 38, 'みる': 39, 'スポーツ': 40, '本当に': 41, '同じ': 42, 'や': 43, '日本代表': 44, '渡航': 45, '費': 46, 'クラァン': 47, '純粋': 48, '集まり': 49, '切っ': 50, 'が': 51, 'すごい': 52, 'クリエイティブ': 53, 'を': 54, '作成': 55, 'やる': 56, 'こと': 57, '意義': 58, '社会': 59, '訴え': 60, 'かけれ': 61, 'ば': 62, '集金': 63, '可能': 64, 'という': 65, '事例': 66, '作っ': 67, '意味': 68, 'で': 69, '二重': 70, 'dafran': 71, '待機時間': 72, 'せい': 73, 'タンク': 74, 'メイン': 75, '笑う': 76, 'n': 77, '一方': 78, 'Haksal': 79, '0時間': 80, 'かけて': 81, '新': 82, '垢': 83, 'DPS': 84, '認定': 85, '終わら': 86, 'せ': 87, 'nDPS': 88, 'プロ': 89, 'ランク': 90, '練習': 91, '時間': 92, '取れ': 93, 'なく': 94, '大変': 95, 'そう': 96, '明る': 97, '単': 98, '振動': 99, 'まじ': 100, 'やばい': 101, '目': 102, 'チカチカ': 103, 'する': 104, 'mac': 105, 'バチクソバグ': 106, '電源': 107, '入れ': 108, 'なおす': 109, 'たび': 110, '異なる': 111, 'キー': 112, '0回': 113, 'タイピング': 114, '押さ': 115, '挙動': 116, '作業': 117, '効率': 118, '下がる': 119, '次': 120, 'から': 121, 'ryzencpu': 122, '格安': 123, 'ノート': 124, '買う': 125, 'つくば': 126, 'ラーメン': 127, 'うまさ': 128, 'ガチ': 129, 'note': 130, '過去': 131, '記事': 132, '見返し': 133, '思う': 134, 'ゲーム': 135, '楽しさ': 136, '部活': 137, 'みたい': 138, '体験': 139, '家': 140, '帰っ': 141, 'パソコン': 142, '起動': 143, 'だけ': 144, 'でき': 145, '年齢': 146, '場所': 147, '問わ': 148, 'ず': 149, '真剣勝負': 150, '楽しめる': 151, 'ところ': 152, 'なあ': 153, 'nteppen': 154, 'カードゲーム': 155, 'も': 156, '楽しい': 157, '人': 158, '交流': 159, 'twitter': 160, '配信': 161, '上': 162, 'しか': 163, '無く': 164, '個人的': 165, '満足度': 166, 'チーム': 167, 'FPS': 168, '圧倒的': 169, 'teppen': 170, 'AI': 171, '作り': 172, 'たく': 173, '強化学習': 174, '調べ': 175, '行動': 176, '学習': 177, 'プラットフォーム': 178, '作る': 179, '一番': 180, '要は': 181, 'ため': 182, 'API': 183, '公開': 184, 'れ': 185, 'せる': 186, '0': 187, 'プログラム': 188, '落とし込ま': 189, 'いけ': 190, 'そこ': 191, '0週間': 192, 'くらい': 193, 'かかる': 194, 'Twitch': 195, 'より': 196, 'Youtube': 197, '方': 198, 'レコメンド': 199, 'システム': 200, 'とか': 201, '結果': 202, '表示': 203, '含め': 204, 'よっぽど': 205, '優れ': 206, '新規': 207, '投稿': 208, '上位表示': 209, '知っ': 210, 'あれ': 211, 'よく': 212, '考えれ': 213, '•': 214, '動画投稿者': 215, 'チャンス': 216, '与える': 217, 'エコシステム': 218, '全体': 219, '新陳代謝': 220, '早める': 221, '量産': 222, 'モチベーション': 223, '登録者': 224, '数': 225, '者': 226, '考える': 227, 'アルゴリズム': 228, '形成': 229, 'できる': 230, 'ん': 231, 'だ': 232, '気づい': 233, 'uD': 234, 'D': 235, 'uDC': 236, '科学': 237, 'へ': 238, '興味': 239, 'パラノイア': 240, '性': 241, '牧歌的': 242, '大事': 243, '気': 244, 'なる': 245, '後で': 246, '読む': 247, '来月': 248, '中国': 249, '行き': 250, 'たいん': 251, '中国語': 252, 'わからん': 253, 'eスポーツ': 254, '企業': 255, 'について': 256, 'たい': 257, '万': 258, 'こういう': 259, '調査': 260, 'レポート': 261, 'まとめ': 262, '送っ': 263, 'くれる': 264, 'サービス': 265, 'ないん': 266, 'イラレマジ': 267, '使い': 268, 'づれ': 269, 'nIT': 270, '土方': 271, 'み': 272, '飯': 273, '資金': 274, '調達': 275, '社長': 276, '0人': 277, '来る': 278, 'マジ': 279, '楽しみ': 280, 'ｗ': 281, '漫画村': 282, '運営': 283, '経歴': 284, 'ググっ': 285, '嘘': 286, '本当': 287, '情報': 288, '大量': 289, '出': 290, 'き': 291, '遵法': 292, '意識': 293, '低い': 294, 'ガッツ': 295, '印象': 296, '半端ない': 297, '本人': 298, '努力': 299, 'あっ': 300, 'こそ': 301, 'コーチング': 302, 'ブロンズ': 303, 'グラマス': 304, 'すご': 305, 'すぎる': 306, 'いい': 307, '感じ': 308, '人数': 309, 'んで': 310, '締め': 311, 'ます': 312, '二': 313, '回': 314, '開催': 315, 'それぞれ': 316, '会社': 317, 'やっ': 318, 'ゲスト': 319, '呼ぼ': 320, 'う': 321, 'C': 322, '向け': 323, '日本': 324, '上場': 325, 'くる': 326, 'やろ': 327, '人月': 328, '0万': 329, 'マザーズ': 330, '強': 331, '応募': 332, 'いただき': 333, 'まし': 334, 'ありがとう': 335, 'ござい': 336, 'いっぱい': 337, '集まっ': 338, '僕': 339, 'おごり': 340, '焼肉': 341, 'でも': 342, 'ましょ': 343, '最高': 344, '普段': 345, '新宿': 346, '本郷': 347, '渋谷': 348, 'い': 349, '最近': 350, '新しい': 351, '会っ': 352, '業界': 353, 'なんか': 354, 'めっちゃ': 355, 'エイム': 356, 'きれい': 357, '今日': 358, 'ロケ': 359, 'ラン': 360, 'ワンショット': 361, 'キル': 362, 'ハンゾーリワーク': 363, 'オバフ': 364, '成績': 365, 'めちゃくちゃ': 366, '草': 367, '後': 368, 'ブリ': 369, '勝率': 370, '0番': 371, 'とかいう': 372, '誰か': 373, '金': 374, '出す': 375, '0円': 376, 'フォトショ': 377, '教え': 378, 'ほしい': 379, '敷居が高い': 380, 'フォートナイト': 381, 'esports': 382, 'なのか': 383, 'デュオ': 384, 'スク': 385, 'シフティ': 386, 'グリーシー': 387, '向かう': 388, '強い': 389, 'その': 390, '理由': 391, 'ブログ': 392, '書い': 393, '一緒に': 394, 'miro': 395, 'どこ': 396, 'いっ': 397, 'かき': 398, 'しない': 399, '相手': 400, 'とら': 401, '初心者': 402, 'だっ': 403, '場合': 404, '有効': 405, '先': 406, '一人': 407, '顔出し': 408, 'フォーカス': 409, 'もらっ': 410, '耐え': 411, 'ながら': 412, 'ショットガン': 413, 'ヘッド': 414, 'ぶち込む': 415, '動き': 416, '結構': 417, '敵': 418, 'ただ': 419, '打た': 420, '油断': 421, 'そこそこ': 422, '決まる': 423, 'スクアッド': 424, 'うまく': 425, 'なれ': 426, '行ける': 427, 'よう': 428, 'なり': 429, 'いって': 430, '初めて': 431, '優勝': 432, 'うれしい': 433, 'リプレイ': 434, 'チーミング': 435, '氏': 436, '取る': 437, 'やつ': 438, '多い': 439, 'わ': 440, 'フォトナマジ': 441, 'OW': 442, '似': 443, '武器': 444, 'ピック': 445, 'ポジショニング': 446, '誰': 447, '集める': 448, 'どういう': 449, '順番': 450, '顔出': 451, 'すか': 452, '要素': 453, '寄り': 454, '負け': 455, '試合': 456, '確認': 457, '全部': 458, '裏': 459, '横': 460, '体力': 461, '差': 462, '作ら': 463, 'ほとんど': 464, 'なー': 465, 'デュオスク': 466, '複数人': 467, '来ら': 468, '位置': 469, '把握': 470, '間違え': 471, '死ぬ': 472, '難しい': 473, '最後': 474, 'なぜ': 475, '急': 476, '切り替わっ': 477, '来': 478, 'やら': 479, '批評家': 480, 'もの': 481, 'に対して': 482, '文句': 483, '失敗': 484, '俺': 485, '言っ': 486, 'とおり': 487, 'っていう': 488, '簡単': 489, '実際': 490, '事業': 491, '起こし': 492, '責任': 493, 'もっ': 494, 'ビジネス': 495, 'として': 496, '成り立つ': 497, '力': 498, '必要': 499, '協会': 500, '声': 501, '上げ': 502, 'なら': 503, '自分': 504, '作れ': 505, 'そういう': 506, '行動力': 507, 'いない': 508, '外部': 509, '団体': 510, 'ばっか': 511, 'jesu': 512, 'どっか': 513, 'レンタルオフィス': 514, '借りて': 515, 'たって': 516, '安い': 517, 'コスト': 518, '儲かる': 519, 'かなっ': 520, '多分': 521, 'たり': 522, '提携': 523, '法人': 524, '登記': 525, '借りる': 526, 'ので': 527, '持つ': 528, '別': 529, '側': 530, 'スキーム': 531, '提供': 532, 'ライセンス': 533, '発行': 534, '料': 535, '当たれ': 536, 'おいしい': 537, 'ダメ': 538, '大して': 539, 'ダメージ': 540, 'グレポン': 541, '必要性': 542, '装備': 543, 'アサルト': 544, 'スナ': 545, '爆発物': 546, '回復': 547, '0つ': 548, '安定': 549, 'スカーズ': 550, '人勝': 551, '率': 552, 'べ': 553, 'え': 554, 'バケモン': 555, 'PUBG': 556, '違っ': 557, '集めれ': 558, 'まぐれ': 559, 'アンチ': 560, '運': 561, '負ける': 562, 'ほぼ': 563, '常に': 564, '忙しく': 565, 'アグレッシブ': 566, '戦える': 567, 'リーダーボード': 568, '見': 569, '上位': 570, '層': 571, '名前': 572, '倒し': 573, 'ビクロイ': 574, '当たり': 575, 'あい': 576, '多く': 577, 'まあ': 578, 'それ': 579, '以外': 580, 'あんまり': 581, 'フォトナ': 582, 'おもし': 583, 'えな': 584, 'bot': 585, 'もれなく': 586, 'フォロー': 587, '今回': 588, 'フォトナブログ': 589, 'SEO': 590, '対策': 591, 'ちゃんと': 592, 'やり': 593, '検索': 594, '予測': 595, '候補': 596, 'ワード': 597, 'タイトル': 598, '名': 599, '攻略': 600, 'アクセス': 601, '0割': 602, 'グーグル': 603, 'はてブ': 604, 'バカ': 605, '重い': 606, 'この': 607, '勉強': 608, 'aktm': 609, '人気': 610, '日本人': 611, 'OPUTO': 612, 'AKTM': 613, 'もん': 614, 'きつく': 615, 'ダスティデポ': 616, '降り': 617, '建築': 618, '無視': 619, 'ジャンプ': 620, 'まくり': 621, '天下': 622, '一': 623, '舞踏': 624, '会す': 625, 'おもろ': 626, 'すぎ': 627, '一応': 628, 'sanma': 629, 'あの': 630, '宇宙人': 631, '魚': 632, 'スキン': 633, '買お': 634, '悩む': 635, 'ユーザー': 636, '聞い': 637, '早く': 638, '変え': 639, 'いいもの': 640, 'しよう': 641, '姿勢': 642, '伝わっ': 643, '0v': 644, 's': 645, 'どう': 646, 'かも': 647, 'ブロックバスター': 648, 'なん': 649, 'だろ': 650, '方向性': 651, '違い': 652, '完成度': 653, '深さ': 654, '勝っ': 655, '好き': 656, 'えー': 657, 'アバター': 658, '早い': 659, 'オメガ': 660, 'かっこいい': 661, 'カーバイド': 662, 'チャレンジ': 663, 'ワクワク': 664, 'アプデ': 665, '神': 666, '過ぎ': 667, 'フレンド': 668, 'いっつも': 669, 'フォトナフレンド': 670, '募集': 671, '画像': 672, '屋敷': 673, '物資': 674, '量': 675, 'やばかっ': 676, '前': 677, 'gorou': 678, 'さん': 679, 'ソロ': 680, 'ラスト': 681, 's0': 682, '当たっ': 683, 'うま': 684, 'チート': 685, '天使大学': 686, 'デジハリ': 687, '中': 688, '鉄板': 689, '毎回': 690, '七': 691, '位': 692, '猛者': 693, 'がふ': 694, 'ざけてかいとるんやろなあ': 695, 'Vermillion': 696, 'まだ': 697, '健在': 698, '今季': 699, '始め': 700, '数字': 701, '引っ張ら': 702, '来期': 703, 'トップ': 704, 'G': 705, 'SR': 706, '箱': 707, '出し': 708, '時点': 709, '丸まっ': 710, '端っこ': 711, '丸まり': 712, '治ら': 713, 'キレ': 714, '速攻': 715, 'メルカリ': 716, '記憶': 717, 'パッドサーフェス': 718, '良かっ': 719, '滑る': 720, '無理': 721, 'ハヤテ': 722, '甲': 723, 'かなり': 724, 'GS': 725, 'R': 726, '表面': 727, 'ぶっちゃけ': 728, 'どっち': 729, 'そんなに': 730, '変わら': 731, '下': 732, '滑り止め': 733, 'artisan': 734, 'あと': 735, '送料': 736, '高く': 737, '関係': 738, 'パッド': 739, '丸め': 740, 'られ': 741, '送ら': 742, '残念': 743, 'リアルタイム': 744, '機械学習': 745, '処理': 746, '女の子': 747, 'データ': 748, '集め': 749, 'すげ': 750, 'これ': 751, 'トール': 752, 'LAG': 753, '変更': 754, '早': 755, 'ウケる': 756, '案外': 757, '攻め': 758, 'ああ': 759, 'いう': 760, '状況': 761, 'あり': 762, 'トレゲン': 763, 'ぶっ': 764, '刺さる': 765, 'アンチダイブ': 766, '使っ': 767, 'ウィンストン': 768, 'ラインハルト': 769, 'ウィドウ': 770, 'ザリア': 771, '機能': 772, 'いる': 773, 'かな': 774, '法則': 775, 'モード': 776, '残り': 777, '分け合っ': 778, 'じゃ': 779, '狩り': 780, '気分': 781, 'ジャンパ': 782, '飛ん': 783, '歩いてる': 784, '殺し': 785, 'そいつ': 786, '回収': 787, 'っ': 788, '無限ループ': 789, 'お': 790, '治っ': 791, 'クラッシュ': 792, '腹立つ': 793, 'PC': 794, '初期': 795, '化': 796, '最初': 797, '画面': 798, '動か': 799, '逝っ': 800, 'くさい': 801, 'みなさん': 802, 'さようなら': 803, '熱': 804, 'クーラー': 805, '付け': 806, '暖房': 807, '気づく': 808, 'かかっ': 809, 'てか': 810, 'どの': 811, 'タイヤ': 812, '対処': 813, '一切': 814, '決まら': 815, 'void': 816, '入っ': 817, 'bischu': 818, 'nLAG': 819, 'もっと強く': 820, '仕事': 821, '事務': 822, '手続き': 823, '週間': 824, '取ら': 825, '郵送': 826, '書類': 827, '待つ': 828, '一週間': 829, 'まったり': 830, 'ずっと': 831, '滞っ': 832, '展開': 833, 'ぞ': 834, 'ウルト': 835, '怒っ': 836, '増え': 837, 'もらう': 838, '地味': 839, 'でしょ': 840, 'ヒーロー': 841, '伝わら': 842, 'ねえ': 843, 'アースシャター': 844, 'どかーんっ': 845, 'メタ': 846, 'カップ麺': 847, '食っ': 848, 'おっさん': 849, '確か': 850, '警察署前': 851, '暴走族': 852, '交差点': 853, '信号': 854, '警察': 855, '煽っ': 856, '地元': 857, '人間': 858, '愚か': 859, '象徴': 860, '支援物資': 861, '群がる': 862, '見る': 863, '牛丼': 864, '無料': 865, '十分': 866, '並ん': 867, 'でる': 868, '思い出す': 869, '何で': 870, '老人': 871, 'お金': 872, '貯め': 873, 'こむ': 874, 'まで': 875, '理解': 876, 'なかっ': 877, '若い人': 878, '投資': 879, '経済活性化': 880, 'す': 881, 'べき': 882, 'だって': 883, '信じ': 884, 'vs': 885, '本質': 886, '的': 887, '部分': 888, '見え': 889, 'いや': 890, 'コミュニケーション': 891, '味方': 892, '渡す': 893, '信じる': 894, '勝利': 895, '最適': 896, '解': 897, '関わら': 898, 'あまりに': 899, 'むかつく': 900, 'Reddit': 901, 'スレ': 902, '立てる': 903, '開発': 904, '奪わ': 905, 'イライラ': 906, '以下': 907, 'meko': 908, '自爆': 909, 'うめ': 910, 'OWL': 911, 'レベル': 912, '高さ': 913, '貢献': 914, 'いろいろ': 915, '感動': 916, '年収': 917, '高い': 918, '受け': 919, 'いく': 920, 'リクナビ': 921, '日程': 922, '適当': 923, '受けて': 924, '出る': 925, 'ことは': 926, '足り': 927, '離職率': 928, '人材': 929, '獲得': 930, '払わ': 931, 'ヤバイ': 932, '就活': 933, 'サイト': 934, 'あて': 935, '，': 936, '社': 937, '内定': 938, 'やめる': 939, 'やれ': 940, 'ほど': 941, '少し': 942, 'づつわかるしいろいろ': 943, 'まじめ': 944, 'やろう': 945, '彼': 946, '大企業': 947, '受けろ': 948, '大': 949, 'けれど': 950, '給料': 951, '福利厚生': 952, '身': 953, 'つく': 954, 'スキル': 955, '研修': 956, '質': 957, '説明会': 958, '昨日': 959, 'むちゃくちゃ': 960, '疲れ': 961, '行進': 962, 'むためどうすればいいかとか': 963, '何': 964, 'メモ': 965, 'ヤバい': 966, '茨城': 967, '東京': 968, '行く': 969, 'るす': 970, 'ぎて': 971, '詰め込ん': 972, 'どる': 973, 'しんどい': 974, '専': 975, '話': 976, 'メカニカル': 977, '以前': 978, '協調性': 979, 'なけれ': 980, 'レート': 981, '落ちる': 982, '当然': 983, '低': 984, '納得': 985, 'ロール': 986, '協調': 987, 'プレイヤー': 988, '多少': 989, '当たり前': 990, '面接': 991, 'サークル': 992, '研究': 993, 'つまら': 994, '話し': 995, 'クスタウキウキ': 996, 'LAV': 997, 'クスタ': 998, 'スペース': 999, 'バニー': 1000, 'イケイケ': 1001, '普通': 1002, '学生': 1003, '有利': 1004, 'つかつか': 1005, 'つかれ': 1006, 'がち': 1007, '疲れる': 1008, '青木': 1009, '就活グッズ': 1010, '買っ': 1011, '萎える': 1012, 'マナー': 1013, 'パワポ': 1014, '印刷': 1015, 'した': 1016, '紙': 1017, 'スタバ': 1018, 'ドトール': 1019, 'うるさ': 1020, '机': 1021, '狭い': 1022, 'カフェ': 1023, 'チェーン店': 1024, '静か': 1025, 'じれる': 1026, 'うるさく': 1027, 'ください': 1028, 'ルノアール': 1029, '知り': 1030, 'ませ': 1031, '久しぶり': 1032, '筋トレ': 1033, '気持ちいい': 1034, '上腕三頭筋': 1035, '燃える': 1036, 'パンプ': 1037, '同士': 1038, '対決': 1039, '使わ': 1040, '一方的': 1041, '倒せる': 1042, '誘導': 1043, 'ミサイル': 1044, '削除': 1045, '大きな': 1046, '有能': 1047, '全て': 1048, '細かい': 1049, 'やり取り': 1050, 'ライン': 1051, '行い': 1052, 'winz': 1053, 'akm': 1054, '兄弟': 1055, 'nwinz': 1056, '個': 1057, '世界チャンピオン': 1058, 'やっぱ': 1059, '才能': 1060, '世界': 1061, '知らんけど': 1062, 'なんで': 1063, '減っ': 1064, 'のに': 1065, 'レイジ': 1066, '使う': 1067, 'パック': 1068, 'クール': 1069, '生かし': 1070, '抑える': 1071, 'そもそも': 1072, '減る': 1073, '考え方': 1074, '攻撃': 1075, 'エフェクト': 1076, 'オゲ': 1077, '言葉': 1078, '壁': 1079, 'カバー': 1080, '今': 1081, 'ダラス': 1082, '続き': 1083, 'デカ': 1084, 'かっ': 1085, '戦力': 1086, '相当': 1087, '重要': 1088, '上回る': 1089, '放出': 1090, 'ツイッター': 1091, '感じる': 1092, 'SNS': 1093, '討論': 1094, '白黒': 1095, '善悪': 1096, '存在': 1097, '主観': 1098, '依存': 1099, '肯定': 1100, '意見': 1101, 'ひたすら': 1102, 'RT': 1103, 'つっ': 1104, 'ー': 1105, 'jjonak': 1106, '唯一': 1107, 'KD': 1108, '比': 1109, '超': 1110, 'えて': 1111, 'トレーサー': 1112, '殺さ': 1113, '殺す': 1114, 'SFSvsSHD': 1115, 'むっちゃ': 1116, 'いい試合': 1117, '上海': 1118, '初勝利': 1119, 'SHD': 1120, 'マーシー': 1121, 'アーキテクト': 1122, 'バルキリー': 1123, 'カウンター': 1124, 'シーン': 1125, '出して': 1126, '笑っ': 1127, 'イーブン': 1128, '状態': 1129, 'geguri': 1130, 'pogchamp': 1131, 'げ': 1132, 'うまい': 1133, 'AKM': 1134, 'ソンブラ': 1135, '悪い': 1136, 'やばく': 1137, '萎え': 1138, '命': 1139, '犠牲': 1140, '死体': 1141, '打っ': 1142, '道連れ': 1143, 'きつ': 1144, 'そん': 1145, '永久': 1146, 'BAN': 1147, 'トロール': 1148, '許容': 1149, 'Overwatch': 1150, 'LUL': 1151, 'HARAOK': 1152, '例': 1153, 'gt': 1154, 'すれ': 1155, '単純': 1156, '計算': 1157, 'ハンゾー': 1158, '明確': 1159, '毎': 1160, 'ずつ': 1161, '落とす': 1162, 'それで': 1163, '以上': 1164, '集まる': 1165, '証明写真': 1166, '顔': 1167, 'FIssure': 1168, '起き': 1169, 'フィッシャー': 1170, '言う': 1171, 'スポンサード': 1172, 'KarQ': 1173, 'まさしく': 1174, 'プロゲーマー': 1175, 'コミュニティ': 1176, 'スケール': 1177, 'によって': 1178, 'コンテンツ': 1179, '時': 1180, '収益': 1181, '否': 1182, '変わっ': 1183, 'つまり': 1184, '多': 1185, 'acer': 1186, 'るし': 1187, '週': 1188, 'バッセン': 1189, 'いか': 1190, 'すっきり': 1191, '超える': 1192, 'タバコ': 1193, '吸う': 1194, '吸っ': 1195, 'レッドブル': 1196, '飲ん': 1197, '脳みそ': 1198, 'ポワポワ': 1199, 'エンジン': 1200, 'やめ': 1201, 'エンジニア': 1202, 'コンサル': 1203, '初任給': 1204, '五': 1205, '百': 1206, '方法': 1207, '無限': 1208, 'リソース': 1209, '広告': 1210, '運用': 1211, '欲しい': 1212, 'シェア': 1213, '仲間': 1214, '共同開発': 1215, '楽し': 1216, 'うらやましい': 1217, '日': 1218, 'RATEL': 1219, 'UI': 1220, '見せ': 1221, 'よかっ': 1222, 'ne': 1223, '素晴らしい': 1224, 'プロダクト': 1225, 'こちら': 1226, 'Shin': 1227, 'XL': 1228, '選ば': 1229, 'ピーク': 1230, '0位': 1231, 'らしい': 1232, 'こんな': 1233, '日本語': 1234, 'うから': 1235, '英語': 1236, 'スケールする': 1237, 'たかっ': 1238, 'わかり': 1239, 'やすい': 1240, '解説': 1241, 'とともに': 1242, 'クオリティ': 1243, '実現': 1244, '投げ': 1245, 'ビビら': 1246, 'Yoshi': 1247, 'haru': 1248, '面白い': 1249, 'OWpedia': 1250, '後援': 1251, 'ここ': 1252, 'プロチーム': 1253, 'イベント': 1254, '参加': 1255, '企画': 1256, 'を通じて': 1257, '発展': 1258, '意味合い': 1259, '私設': 1260, '書誌': 1261, '住所': 1262, '本当は': 1263, '倍': 1264, 'プレー': 1265, '指摘': 1266, '覚え': 1267, 'ないし': 1268, 'とりあえず': 1269, '抜き出し': 1270, '後記': 1271, '事': 1272, '個人ブログ': 1273, '読ま': 1274, '残ら': 1275, 'インターネット': 1276, 'デ': 1277, 'クソ': 1278, 'しょうが': 1279, 'アーカイブ': 1280, '読める': 1281, '書か': 1282, '無駄': 1283, 'キャラ': 1284, '性能': 1285, '引き出す': 1286, 'みんな': 1287, 'がる': 1288, 'アナ': 1289, '死に': 1290, 'にくく': 1291, 'ほう': 1292, '0倍': 1293, '楽': 1294, '分断': 1295, 'ヒーラー': 1296, 'ひきつけ': 1297, 'ゼニヤッタ': 1298, '後ろ': 1299, '死な': 1300, '不和': 1301, 'つけ': 1302, 'てれ': 1303, 'どんな': 1304, '本能': 1305, '理解度': 1306, 'もろに': 1307, '影響': 1308, 'シルゴル': 1309, 'いいんじゃない': 1310, '思え': 1311, 'ごと': 1312, 'なんて': 1313, 'わけ': 1314, 'ランキング': 1315, '参考': 1316, '空間': 1317, '能力': 1318, '云々': 1319, '特に': 1320, 'まくっ': 1321, 'に関する': 1322, '書き': 1323, '正直': 1324, '日本軍': 1325, '片道': 1326, '分': 1327, '燃料': 1328, '特攻': 1329, 'シルバー': 1330, 'ゴールド': 1331, '最大限': 1332, 'ポジション': 1333, '取れる': 1334, '敵味方': 1335, '打つ': 1336, '殺せる': 1337, '指導': 1338, '0日': 1339, '上がっ': 1340, 'プラチナ': 1341, 'リンクサ': 1342, 'わかる': 1343, '働い': 1344, '全': 1345, 'ら': 1346, '見せしめ': 1347, 'バン': 1348, '初動': 1349, 'イカれた': 1350, '行為': 1351, 'はず': 1352, 'クマ': 1353, 'なのは': 1354, 'ブリザード': 1355, '最大': 1356, 'ベータテスト': 1357, 'tabete': 1358, 'ダウンロード': 1359, '市役所': 1360, '待たさ': 1361, 'サクッと': 1362, 'かける': 1363, '書く': 1364, 'ザリーパー': 1365, '怖い': 1366, '周り': 1367, 'ちやほや': 1368, '感情': 1369, '満たす': 1370, 'ポストトゥルース': 1371, '追い求め': 1372, '代行': 1373, 'ブースト': 1374, 'じゃなくて': 1375, '自己顕示欲': 1376, '自分自身': 1377, '変化': 1378, '数値': 1379, '上下': 1380, 'のみ': 1381, '欺く': 1382, '平気': 1383, '行う': 1384, '精神': 1385, '問題': 1386, 'custa': 1387, '勝てる': 1388, '確率': 1389, 'ダイナスティ': 1390, '移籍': 1391, 'ボコボコ': 1392, 'にっこり': 1393, '当たる': 1394, 'とき': 1395, '九': 1396, '割': 1397, 'ダイヤ': 1398, 'VC': 1399, '言わ': 1400, '都合': 1401, '切り取っ': 1402, '悪者': 1403, '晒し': 1404, 'マウント': 1405, 'メンタル': 1406, 'Artisan': 1407, 'マウスパッド': 1408, 'アキバ': 1409, '大会': 1410, '履歴書': 1411, '手書き': 1412, '受ける': 1413, 'やめよ': 1414, '特筆': 1415, '資格': 1416, '自動車免許': 1417, 'いえ': 1418, 'もう': 1419, 'ツイート': 1420, '一年生': 1421, 'センス': 1422, '方向': 1423, '行っ': 1424, 'ブルドーザー': 1425, 'ぶっ殺し': 1426, 'いける': 1427, 'しおりん': 1428, '完全': 1429, '趣味': 1430, '合う': 1431, '合わせ': 1432, 'マッチ': 1433, 'ドンカツツ': 1434, '出来': 1435, 'スクアッドメンバー': 1436, '得ん': 1437, '強かっ': 1438, 'デスク': 1439, 'セットアップ': 1440, '椅子': 1441, '届い': 1442, 'バケツ': 1443, '腰': 1444, 'au': 1445, '営業': 1446, '月': 1447, '回線': 1448, '使える': 1449, '契約': 1450, 'キャズム': 1451, '新しいことを始めよう': 1452, '怪し': 1453, 'マックス': 1454, '頭': 1455, 'おかしい': 1456, 'られる': 1457, 'なかなか': 1458, '住民': 1459, 'うる': 1460, '睡眠': 1461, '起きる': 1462, '寮': 1463, '引っ越し': 1464, 'アメニティ': 1465, '失っ': 1466, 'ダンボール': 1467, '寝': 1468, '置く': 1469, '奥の手': 1470, '球': 1471, '瞬間': 1472, '陰影': 1473, '表現': 1474, '変わる': 1475, '手前': 1476, '親指': 1477, 'ピクセル': 1478, 'ボケ': 1479, 'かた': 1480, '荒く': 1481, '編集': 1482, '機械': 1483, '奴隷': 1484, 'キリヒト': 1485, '毎日': 1486, 'コメント': 1487, 'もらえ': 1488, 'うれしかっ': 1489, '住民票': 1490, 'そのまま': 1491, '元': 1492, '住ん': 1493, '他県': 1494, '委': 1495, '移そ': 1496, '必須': 1497, 'ファイル': 1498, 'PDFファイル': 1499, 'なんや': 1500, '公的': 1501, '色々': 1502, '出さ': 1503, '直後': 1504, 'また': 1505, 'だるい': 1506, '限り': 1507, 'それとも': 1508, 'ロゴデザイン': 1509, 'さくっと': 1510, 'ランサーズ': 1511, '依頼': 1512, '0件': 1513, '期待値': 1514, '収入': 1515, 'デザイナー': 1516, '業': 1517, '過酷': 1518, '悪貨が良貨を駆逐する': 1519, '典型': 1520, '調べる': 1521, 'IR': 1522, 'PR': 1523, '美男': 1524, '美女': 1525, 'ばかり': 1526, '威圧': 1527, '自己分析': 1528, 'まとめる': 1529, 'つ': 1530, 'ジュ': 1531, '聞く': 1532, '失礼': 1533, '払っ': 1534, '聞き': 1535, '有料': 1536, '利益': 1537, '折半': 1538, 'ソリューション': 1539, 'サブスク': 1540, 'ライブ': 1541, 'ドネート': 1542, '感覚': 1543, 'いけや': 1544, '持続可能': 1545, '生み出す': 1546, '稼げ': 1547, 'なんらかの': 1548, 'インセンティブ': 1549, '有名': 1550, 'インタビュー': 1551, 'おる': 1552, 'nNote': 1553, '関連': 1554, '手法': 1555, 'とる': 1556, '高所': 1557, 'ひっくり返す': 1558, '最強': 1559, 'おかげ': 1560, 'ドン勝': 1561, '涙': 1562, 'あまり': 1563, 'いろんな': 1564, '福岡': 1565, '暮らそ': 1566, '些細なこと': 1567, '十': 1568, '株式会社': 1569, 'グラディエーター': 1570, '揃っ': 1571, 'やす': 1572, 'マノ': 1573, 'てん': 1574, 'すき': 1575, '蘇生': 1576, 'かー': 1577, 'ぺやばすぎ': 1578, 'プロ選手': 1579, 'J': 1580, 'AKE': 1581, 'フラストレーション': 1582, 'たまる': 1583, '発言': 1584, 'シーガルミッキーデュオ': 1585, '別に': 1586, '補欠': 1587, 'ディス': 1588, '気に入ら': 1589, 'ラスカル': 1590, 'あ': 1591, 'あら': 1592, '終わり': 1593, 'きびし': 1594, '利他': 1595, '長期的': 1596, '生存戦略': 1597, 'なんの': 1598, '関心': 1599, '引く': 1600, '結びつい': 1601, '発達': 1602, '広範囲': 1603, '届け': 1604, '性質': 1605, '晒す': 1606, 'ぱっと': 1607, '人類の進化': 1608, '過程': 1609, '合理的': 1610, 'メリット': 1611, '強者': 1612, '卍': 1613, '直接': 1614, '面白かっ': 1615, '嬉しい': 1616, '是非': 1617, '感想': 1618, '伝え': 1619, 'あげ': 1620, 'うれ': 1621, 'ぴ': 1622, '大体': 1623, 'ゲー': 1624, 'フォー': 1625, 'ナイト': 1626, 'なし': 1627, '読め': 1628, '頼ん': 1629, 'だら': 1630, '提案': 1631, '美術': 1632, '壊れ': 1633, 'Ninja': 1634, 'SOLO': 1635, 'DUO': 1636, 'ワロタ': 1637, 'nDUO': 1638, 'かわいい': 1639, '見た目': 1640, '反し': 1641, '実力': 1642, '反映': 1643, 'シビア': 1644, 'ゲーム性': 1645, 'ヤマトン': 1646, '0勝': 1647, 'wosp': 1648, '気軽': 1649, '質問': 1650, 'でし': 1651, 'アドバイス': 1652, '元にし': 1653, 'シーズン': 1654, '十日': 1655, 'マスター': 1656, '考え': 1657, 'BR': 1658, '二位': 1659, 'どん': 1660, 'かつ': 1661, 'やたら': 1662, '建造': 1663, 'モンスター': 1664, '四': 1665, '建': 1666, '鉄筋コンクリート': 1667, 'マンション': 1668, '打ち込ん': 1669, 'キツ': 1670, 'pon': 1671, 'overwatch': 1672, '答え': 1673, '図': 1674, 'ミ': 1675, 'スっ': 1676, '東': 1677, '群': 1678, '左上': 1679, '右下': 1680, '違う': 1681, '回答': 1682, '特定': 1683, '縛っ': 1684, '条件': 1685, '満たし': 1686, '数学': 1687, '証明': 1688, '西': 1689, '逆': 1690, 'もしくは': 1691, '読ん': 1692, 'ツリー': 1693, '状': 1694, 'パターン': 1695, '出せる': 1696, 'pubg': 1697, '真面目': 1698, 'エンジョイゲーマー': 1699, '差出る': 1700, 'スクアット': 1701, 'でかい': 1702, '建造物': 1703, '戦う': 1704, 'w': 1705, 'クソアフィブログ': 1706, 'こん': 1707, '攻略サイト': 1708, 'レジェンド': 1709, 'だまさ': 1710, 'ミニガン': 1711, '笑': 1712, '発射': 1713, '秒': 1714, 'ジョーク': 1715, 'ウェブサービス': 1716, 'いかに': 1717, '経済的': 1718, '合理性': 1719, '持た': 1720, '価値': 1721, '追求': 1722, '非常': 1723, 'これから': 1724, 'がんばる': 1725, '合計': 1726, '何となく': 1727, '勘所': 1728, 'わかっ': 1729, 'GamerCoach': 1730, '他': 1731, '0か月': 1732, '悪かっ': 1733, '閉鎖': 1734, '途中': 1735, '面白く': 1736, 'そ': 1737, 'ゲーマーコーチ': 1738, '一年': 1739, '今年': 1740, '頑張る': 1741, '諸々': 1742, 'しんど': 1743, '喫煙': 1744, '三': 1745, 'Zunba': 1746, '気持ち': 1747, '辛い': 1748, 'ペット': 1749, '死ん': 1750, 'ツイー': 1751, '流れ': 1752, 'nSNS': 1753, '不': 1754, '動かし': 1755, '本来': 1756, '触れる': 1757, '触れ': 1758, 'しまう': 1759, 'よろしく': 1760, 'AutoChess': 1761, 'リスナー': 1762, 'TFT': 1763, '0万人': 1764, 'わろ': 1765, 'パクっ': 1766, '勝ち': 1767, '無知': 1768, 'バグ': 1769, '消し飛ん': 1770, 'ぬ': 1771, 'ザイル': 1772, 'くくっ': 1773, '薄氷': 1774, '一緒': 1775, '飛び込む': 1776, '利害関係': 1777, '結べ': 1778, '株': 1779, '使え': 1780, '長時間労働': 1781, 'ガシガシ': 1782, '貴重': 1783, '一日': 1784, '観戦': 1785, 'そして': 1786, '若く': 1787, '好きな人': 1788, 'やってき': 1789, 'おじさん': 1790, '視点': 1791, '一点': 1792, '尽きる': 1793, '平たく': 1794, 'ドメイン知識': 1795, 'ニーズ': 1796, '読み取っ': 1797, 'だからこそ': 1798, '盛り上げ': 1799, 'い人': 1800, '独自': 1801, '基づい': 1802, '当たら': 1803, 'すでに': 1804, '効果': 1805, '実証': 1806, 'ローカライズ': 1807, '独自性': 1808, '求める': 1809, '活動': 1810, '専門': 1811, 'discord': 1812, '置き換わる': 1813, '未来': 1814, '像': 1815, 'パクリ': 1816, '半年': 1817, '絶対': 1818, 'リリース': 1819, '当初': 1820, '評価': 1821, '緊張感': 1822, '良': 1823, '正義': 1824, '言い': 1825, 'Time': 1826, 'to': 1827, 'retire': 1828, 'ff0': 1829, 'リュック': 1830, '声優': 1831, 'ツボ': 1832, 'おかしく': 1833, 'ケルニッヒ': 1834, 'フレ': 1835, '暴言': 1836, '飛ばさ': 1837, 'ハリウッド': 1838, '第': 1839, 'ブロンゴ': 1840, 'LP': 1841, 'LOL': 1842, '対人': 1843, '戦': 1844, 'わざと': 1845, '放置': 1846, 'くれ': 1847, '下げ': 1848, '初心者狩り': 1849, '怒ら': 1850, '抜け': 1851, '厳しい': 1852, '紫電改': 1853, 'か月': 1854, '湿気': 1855, '引っ掛かり': 1856, 'やっぱり': 1857, 'ヒエン': 1858, 'ハルト': 1859, 'マップ': 1860, '少な': 1861, 'Dva': 1862, '突っ込ん': 1863, 'コントロールライン': 1864, 'よわ': 1865, '落ち': 1866, 'マウンティング': 1867, '正しい': 1868, '某': 1869, 'EMP': 1870, 'キング': 1871, 'スロー': 1872, '格下': 1873, 'チャージ': 1874, '当て': 1875, '殴っ': 1876, 'シャター': 1877, '防い': 1878, '決め': 1879, 'ハルザリデュオ': 1880, '見せつけ': 1881, '気持ち良': 1882, 'モイラ': 1883, '悪玉': 1884, 'えらい': 1885, '眠かっ': 1886, '肩身': 1887, 'せめ': 1888, '類友': 1889, '極み': 1890, 'widow': 1891, '0k': 1892, 'd': 1893, 'ファラ': 1894, 'かられ': 1895, 'クリティカル': 1896, '屈伸': 1897, '小指': 1898, '折れ': 1899, 'FFA': 1900, '神ゲー': 1901, 'しゃがみ': 1902, 'シフト': 1903, 'マウス': 1904, 'サイド': 1905, 'ボタン': 1906, '具': 1907, 'ラップリングフック': 1908, 'スパム': 1909, 'いれ': 1910, 'Widow': 1911, 'sniper': 1912, 'ググ': 1913, '探し': 1914, 'わかん': 1915, '下さい': 1916, 'Google': 1917, 'is': 1918, 'GOD': 1919, 'nGoogle': 1920, 'dominates': 1921, 'the': 1922, 'world': 1923, 'Google翻訳': 1924, '韓国語': 1925, '翻訳': 1926, '精度': 1927, '普通に': 1928, '会話': 1929, 'ビビる': 1930, 'ついで': 1931, 'OWBlog': 1932, 'デザイン': 1933, '変えよ': 1934, 'nSEO': 1935, 'HTML': 1936, 'CSS': 1937, 'Bootstrap': 1938, 'ニッチ': 1939, '対応': 1940, 'づらく': 1941, '選択': 1942, '強いる': 1943, 'ウェーブ': 1944, '回っ': 1945, 'ルート': 1946, 'タレット': 1947, 'こさ': 1948, 'にくい': 1949, '中途半端': 1950, '貯まっ': 1951, '迷い': 1952, 'づらい': 1953, '間違える': 1954, '火力': 1955, 'ヒートー': 1956, 'トールビョーン': 1957, 'ティア': 1958, 'メトラ': 1959, '次いで': 1960, 'だし': 1961, 'フィリー': 1962, 'EQO': 1963, 'シャドウバー': 1964, 'ゼニヤッタウルト': 1965, '編成': 1966, 'さす': 1967, 'ナノゼニ': 1968, 'ありか': 1969, 'しれ': 1970, '中の人': 1971, 'です': 1972, 'ハブ': 1973, '知る': 1974, '知ら': 1975, 'ブースター': 1976, '半分': 1977, '上昇': 1978, '真上': 1979, '飛ぶ': 1980, '目的': 1981, '気持ちよ': 1982, 'ぱねえ': 1983, '俳優': 1984, '目力': 1985, 'おもろい': 1986, 'ケインコスギ': 1987, 'チャンネル': 1988, 'トップチア': 1989, '池谷直樹': 1990, '苦しみ': 1991, 'ルシモイラ': 1992, '悪玉コレステロール': 1993, '飛ばし': 1994, '自慢': 1995, 'しよ': 1996, 'なちゅ': 1997, '北': 1998, 'コーチ': 1999, 'しれっと': 2000, '加入': 2001, 'しとる': 2002, '脳死': 2003, '感': 2004, 'そっち': 2005, 'ホグ': 2006, '奴': 2007, '小学生': 2008, 'ころ': 2009, 'サンダーボルト': 2010, 'ハーピイ': 2011, '設定': 2012, 'ゼニ': 2013, 'TIPS': 2014, 'どうり': 2015, 'クラメン': 2016, 'らしく': 2017, '検証': 2018, 'もっと': 2019, '入る': 2020, '反省': 2021, 'ブロック': 2022, '申請': 2023, 'ッ': 2024, 'くるん': 2025, '許可': 2026, '鼻水': 2027, 'くしゃみ': 2028, '止まら': 2029, '苦しい': 2030, 'ロン': 2031, '鯖': 2032, 'リアル': 2033, 'N': 2034, '勢い': 2035, 'アメリカ': 2036, '勢': 2037, '韓国': 2038, 'ボコっ': 2039, '同期': 2040, '就職': 2041, '旅立っ': 2042, 'uDE': 2043, 'ボディビル': 2044, '好きだから': 2045, '足': 2046, '太': 2047, '大腿四頭筋': 2048, '見える': 2049, 'rt': 2050, 'fav': 2051, 'すぐ': 2052, 'pv': 2053, '草生える': 2054, '飛燕': 2055, 'VE': 2056, 'バージョン': 2057, 'させ': 2058, '意味不明': 2059, '始めて': 2060, 'メイヘム': 2061, '虹彩': 2062, '実家': 2063, 'OP': 2064, '感謝': 2065, '土地': 2066, '戻っ': 2067, 'QOL': 2068, '爆上': 2069, 'りし': 2070, '泣い': 2071, '基本': 2072, '増やし': 2073, 'いき': 2074, 'How': 2075, 'get': 2076, 'Dia': 2077, '花粉症': 2078, 'ひどい': 2079, '政治家': 2080, '杉': 2081, '絶滅': 2082, '思わ': 2083, '深': 2084, 'ヒール': 2085, '写し': 2086, 'カメラ': 2087, '微妙': 2088, '真': 2089, '隣': 2090, '瞬': 2091, '離脱': 2092, '流行り': 2093, 'ドラゴンズ': 2094, 'フラッシュウルブズ': 2095, 'Diya': 2096, 'リップタイヤ': 2097, '時間切れ': 2098, '爆発': 2099, 'made': 2100, 'in': 2101, 'china': 2102, '埋まっ': 2103, 'フロリダ': 2104, 'OPC': 2105, 'デトネーター': 2106, 'サンシス': 2107, 'シュアフォー': 2108, 'なんと': 2109, '言えん': 2110, 'FISSURE': 2111, '大当たり': 2112, '手': 2113, '楽しく': 2114, 'スタダ': 2115, 'GG': 2116, 'そこら': 2117, 'サポート': 2118, '熱く': 2119, '丸の内': 2120, 'イタリアン': 2121, '昼間': 2122, '食い': 2123, 'だべる': 2124, '主婦': 2125, '来世': 2126, '平日': 2127, 'ちょっと': 2128, '高め': 2129, 'だいたい': 2130, '悪口大会': 2131, '集団': 2132, 'AVA': 2133, 'FF': 2134, 'わざわざ': 2135, 'アンインストール': 2136, '二度と': 2137, '復帰': 2138, '宣言': 2139, 'ブリジットクソ': 2140, 'いら': 2141, '増える': 2142, 'ベイングローリー': 2143, 'にくかっ': 2144, 'とにかく': 2145, '良質': 2146, 'ロル': 2147, 'ローセンシ': 2148, 'マック': 2149, 'トラックパッド': 2150, '操作': 2151, 'チャンピオン': 2152, '正面': 2153, '戦っ': 2154, 'レーン': 2155, 'コア': 2156, '壊し': 2157, 'ロ': 2158, 'る': 2159, '目やに': 2160, 'ハルザリ': 2161, '不明': 2162, 'ファック': 2163, 'だの': 2164, 'オーマイガー': 2165, 'ダフラン': 2166, 'いつ': 2167, 'もお': 2168, 'おっ': 2169, '熱意': 2170, '裁判': 2171, '弁護士ドットコム': 2172, 'バクマン': 2173, '岩瀬': 2174, '人間味': 2175, 'S': 2176, 'サポ': 2177, '山崎': 2178, '代打': 2179, '演説': 2180, 'イチロー': 2181, 'ファン': 2182, '反論': 2183, '中間管理職': 2184, 'トネガワ': 2185, 'ギャグ漫画': 2186, '深い': 2187, 'コミュ力': 2188, '辛いっ': 2189, '大学': 2190, 'つら': 2191, 'Tips': 2192, '空港': 2193, '予定': 2194, '夜': 2195, '助かっ': 2196, '高松空港': 2197, '松山空港': 2198, '愛媛': 2199, '香川': 2200, 'しまっ': 2201, 'なう': 2202, 'エアギア': 2203, '登場': 2204, 'ジェイク': 2205, 'ジェーーーイク': 2206, '叫ん': 2207, 'メンヘラ': 2208, 'かまってちゃん': 2209, 'ゼロ': 2210, '今度': 2211, 'ザリアピック': 2212, '年': 2213, 'こ': 2214, 'スタンダード': 2215, '役に立っ': 2216, 'おｋ': 2217, 'やっと': 2218, 'みずほ': 2219, '口座': 2220, 'ネット': 2221, 'バンク': 2222, '使用': 2223, '手数料': 2224, '振込手数料': 2225, '0時': 2226, '鬼': 2227, '仕様': 2228, '困り': 2229, '文章': 2230, 'まさか': 2231, '行': 2232, '申し込む': 2233, '羽目': 2234, '住信SBIネット銀行': 2235, '良い': 2236, 'スタートアップ': 2237, '申し込ん': 2238, '難易度': 2239, '遅れ': 2240, 'ｔ': 2241, 'サービス開始': 2242, '全然': 2243, '潮流': 2244, 'っぽい': 2245, '銀行': 2246, '修正': 2247, '箇所': 2248, 'はん': 2249, '押し': 2250, 'てぃー': 2251, '令和': 2252, '人並': 2253, 'IT': 2254, 'ってな': 2255, 'っけ': 2256, '高齢化': 2257, '軍隊': 2258, '式': 2259, '教育': 2260, 'による': 2261, 'オープン': 2262, 'マインド': 2263, '欠如': 2264, 'どうにも': 2265, 'Discord': 2266, '鯖落ち': 2267, 'ビデオ': 2268, '通話': 2269, 'サーバー': 2270, '復活': 2271, '送信': 2272, '危ない': 2273, 'やすく': 2274, 'ATM': 2275, 'パスワード': 2276, '空い': 2277, '窓口': 2278, '行か': 2279, '行け': 2280, '規制': 2281, '守ら': 2282, '昭和': 2283, '苦しめ': 2284, '現金': 2285, '盗難': 2286, 'ミス': 2287, '手元': 2288, 'ひきおろす': 2289, '円': 2290, '害悪': 2291, 'ツール': 2292, '罰金': 2293, 'かけ': 2294, 'コワーキングスペース': 2295, '意識高い': 2296, '蕁麻疹': 2297, '言え': 2298, '最新': 2299, 'ある程度': 2300, 'つい': 2301, '適応': 2302, '拡散': 2303, '新参': 2304, '聞き取れ': 2305, '見れ': 2306, 'もったいない': 2307, 'せめて': 2308, '字幕': 2309, '実装': 2310, 'くん': 2311, 'ねー': 2312, 'Skype': 2313, '音声': 2314, '認識': 2315, 'あらゆる': 2316, 'ストリーミング': 2317, 'めちゃ': 2318, 'クチャ': 2319, '起用': 2320, 'ソルジャー': 2321, '得意': 2322, 'うける': 2323, 'ダイブ': 2324, 'バック': 2325, '生かせる': 2326, '判断': 2327, '悲しい': 2328, '平地': 2329, 'Owl': 2330, '公式': 2331, 'アプリ': 2332, 'タブレット端末': 2333, 'fissure': 2334, '帝国': 2335, '竜田揚げ': 2336, 'レパートリー': 2337, 'チーム名': 2338, 'カタカナ': 2339, '文字': 2340, '集中': 2341, 'まわし': 2342, '徹夜': 2343, 'ow': 2344, 'ティルト': 2345, '下げる': 2346, 'あげる': 2347, '不眠': 2348, '回し': 2349, '落とし': 2350, 'ウホウホ': 2351, '明日': 2352, '謎': 2353, '終わっ': 2354, '寝る': 2355, 'サブ': 2356, 'Bz': 2357, 'ORANGE': 2358, 'RANGE': 2359, '聞け': 2360, '体': 2361, '育っ': 2362, '役に立つ': 2363, '自動': 2364, '生成': 2365, 'もと': 2366, 'ネイティブ': 2367, '聞き取る': 2368, 'Soon': 2369, 'スー': 2370, '為': 2371, '手が込ん': 2372, 'Youtuber': 2373, '結局': 2374, '立ち回り': 2375, 'ダーツ': 2376, '残っ': 2377, '確定': 2378, 'モーション': 2379, '反応': 2380, 'マトリクス': 2381, '貼る': 2382, '余裕': 2383, 'メンバー': 2384, '招集': 2385, '触っ': 2386, 'クイック': 2387, 'ぱすわど': 2388, '印象深い': 2389, '夢見': 2390, '拠点': 2391, '踏ま': 2392, 'きん': 2393, 'Jesl': 2394, 'なれる': 2395, '開ける': 2396, '0秒': 2397, '二日': 2398, '冊': 2399, '本読': 2400, '家探': 2401, '仲介業者': 2402, 'ボリ': 2403, '0月': 2404, '引っ越す': 2405, 'プロパイダ': 2406, 'しのう': 2407, 'アホ': 2408, '主張': 2409, '根拠': 2410, 'ソース': 2411, '無し': 2412, '一部': 2413, '記述': 2414, 'ページ': 2415, '捨て': 2416, '変える': 2417, '男': 2418, 'イーロンマスク': 2419, 'つま': 2420, '著者': 2421, 'サーベイ': 2422, '不足': 2423, '参考文献': 2424, 'ないっ': 2425, 'ていう': 2426, '加え': 2427, '過度': 2428, '原発': 2429, '批判': 2430, 'rox': 2431, 'orcas': 2432, 'ロゴ': 2433, '変換': 2434, '背景': 2435, '抜い': 2436, 'パク': 2437, 'いくら': 2438, '見つかり': 2439, 'コンテンダーズ': 2440, '非公式': 2441, '消え': 2442, 'アカデミー': 2443, 'そういや': 2444, 'リザーブ': 2445, 'つもり': 2446, 'ナメクジ': 2447, '努める': 2448, 'ESC': 2449, '流行らす': 2450, 'OASIS': 2451, '二つ': 2452, 'SUP': 2453, '低かっ': 2454, '個人': 2455, '信用': 2456, 'ドタキャン': 2457, 'オーブ': 2458, '割合': 2459, 'ヌンバニ': 2460, 'ヒット': 2461, 'スキャン': 2462, 'アリ': 2463, 'キラー': 2464, 'メイ': 2465, '強く': 2466, 'やん': 2467, 'リミテッド': 2468, '楽しかっ': 2469, '右': 2470, '左': 2471, 'ダンテ': 2472, 'xqc': 2473, 'シナトラ': 2474, '全員': 2475, '協力': 2476, 'ついて': 2477, 'ふざけ': 2478, '0分': 2479, 'タイマー': 2480, '腹': 2481, '痛かっ': 2482, 'ひゅーーーーーーーーーー': 2483, 'ーー': 2484, 'じ': 2485, 'ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ': 2486, 'ウイイレ': 2487, 'メッシ': 2488, 'クリロナ': 2489, '入れる': 2490, 'アレ': 2491, 'シーガル': 2492, '出番': 2493, 'COC': 2494, 'よー': 2495, 'hz': 2496, 'しきら': 2497, 'ディスプレイ': 2498, 'おもっ': 2499, '裸の王様': 2500, '0年': 2501, 'たっ': 2502, 'ウィンドウズ': 2503, 'Nvidia': 2504, 'かん': 2505, 'lol': 2506, 'フェーカー': 2507, 'いかん': 2508, '真ん中': 2509, 'よる': 2510, 'ヘリックスジャンプ': 2511, '躱せ': 2512, '事故死': 2513, 'リスク': 2514, '背負っ': 2515, 'ぶっちぎり': 2516, 'うまかっ': 2517, 'nas': 2518, 'ty': 2519, 'RUMATA': 2520, 'OTP': 2521, '昔': 2522, '0kg': 2523, '0cm': 2524, '適正': 2525, '体重': 2526, '表': 2527, 'ガリガリ': 2528, 'ジャスト': 2529, 'モイラウルト': 2530, '思い': 2531, 'プレッシャー': 2532, 'CTF': 2533, 'ルシオ': 2534, 'デスマラソン': 2535, 'ソルマク': 2536, 'サウンドバリア': 2537, '完璧': 2538, 'ロンドン': 2539, 'nyxl': 2540, 'もっか': 2541, 'かい': 2542, 'つえ': 2543, 'バードリングキレキレ': 2544, 'Saebyelobe': 2545, 'NYXL': 2546, 'スピットファイア': 2547, 'アツ': 2548, 'バードリングクソイケメン': 2549, 'ルシオボール': 2550, 'ルール': 2551, '対面': 2552, '殴り合い': 2553, '勝負': 2554, '勝つ': 2555, '残酷': 2556, 'トールメトラ': 2557, 'サッカー': 2558, '上がれ': 2559, 'ディフェンス': 2560, '配置': 2561, 'もんじゃ': 2562, 'タン': 2563, 'フラッグ': 2564, 'スピブ': 2565, '運べ': 2566, 'カンカン': 2567, 'ダスト': 2568, 'もらえる': 2569, 'フルパ': 2570, '現在': 2571, 'アカウント': 2572, 'ctf': 2573, 'ガイジ': 2574, 'ドール': 2575, '待っ': 2576, 'ガン': 2577, 'タキ': 2578, 'メトラビョーン': 2579, '守り': 2580, '嫌がっ': 2581, '逃げ': 2582, 'トリプルキル': 2583, '取っ': 2584, '囚人のジレンマ': 2585, '一連': 2586, '高校時代': 2587, '教師': 2588, 'ども': 2589, '怒り': 2590, '蘇っ': 2591, 'おこ': 2592, 'じゃん': 2593, '帰り': 2594, 'てえ': 2595, '久々': 2596, '大阪': 2597, 'きた': 2598, 'まんがな': 2599, 'だらだら': 2600, '暮らし': 2601, '経済': 2602, '自立': 2603, '起業': 2604, 'スモールビジネス': 2605, '労働': 2606, 'めんどく': 2607, '親夜': 2608, 'ダラダラ': 2609, 'twitch': 2610, 'シコシコ': 2611, '便利': 2612, 'ゲグリシャター': 2613, 'かわし': 2614, 'igs': 2615, 'なっちゃった': 2616, '履い': 2617, '適性': 2618, 'モイラマジ': 2619, 'ビーム': 2620, '無理やり': 2621, 'バレッジ': 2622, '安心': 2623, '打てる': 2624, '罪悪感': 2625, '迷わ': 2626, 'ポンポン': 2627, '付': 2628, '老い': 2629, 'マーシーナーフ': 2630, '以降': 2631, 'キュートマーシーアイコン': 2632, '嫌': 2633, '予感': 2634, '友達': 2635, '呼ば': 2636, '退出': 2637, '持っ': 2638, 'かれ': 2639, '飛行機': 2640, 'バリアント': 2641, 'だいぶ': 2642, 'えっ': 2643, 'つよ': 2644, '中村': 2645, '藤田': 2646, '名誉回復': 2647, 'あたり': 2648, 'ヤバ': 2649, 'ルシゼニモイラ': 2650, '弱い': 2651, '花村': 2652, 'チョーク': 2653, 'きつい': 2654, 'マーシーピック': 2655, 'パラディンズ': 2656, '連合軍': 2657, 'こいつ': 2658, '逆ギレ': 2659, '未検証': 2660, '始まっ': 2661, 'ログアウト': 2662, '低下': 2663, 'グリッチ': 2664, '発見': 2665, 'かもしれん': 2666, 'ディバ': 2667, '悪く': 2668, 'どうにか': 2669, '厳しさ': 2670, '四月': 2671, 'まとも': 2672, 'に関して': 2673, '江尻': 2674, '勝': 2675, '0敗': 2676, '後半': 2677, 'だれ': 2678, '達': 2679, '台湾': 2680, 'アジア': 2681, 'プロリーグ': 2682, '参戦': 2683, '実感': 2684, 'そうだ': 2685, '日本チーム': 2686, '応援': 2687, '伴わ': 2688, '次第に': 2689, 'ワザップ': 2690, 'フォーカース': 2691, '中央集権': 2692, 'メディア': 2693, '熱量': 2694, '生かす': 2695, '難しく': 2696, '解決': 2697, '図書館': 2698, '仕組み': 2699, '作れる': 2700, 'エンパワーメント': 2701, '連鎖': 2702, '続い': 2703, 'オバフスクレイピング': 2704, '閾値': 2705, '超え': 2706, '更新': 2707, '続ける': 2708, '戦績': 2709, '面白': 2710, 'マクリー': 2711, '変遷': 2712, '今週': 2713, '今月': 2714, '比較': 2715, 'グラ': 2716, 'マス': 2717, '近く': 2718, 'スチーム': 2719, '管理': 2720, 'MOD': 2721, 'OK': 2722, 'オート': 2723, 'チェス': 2724, 'Steam': 2725, '商用': 2726, '利用': 2727, 'ゆるく': 2728, 'Mod': 2729, 'パクる': 2730, '流行っ': 2731, 'カオス': 2732, 'ゲーム版': 2733, 'Qiita': 2734, '天命': 2735, '授け': 2736, '以内': 2737, 'クラ': 2738, 'チーム作り': 2739, 'サムネ': 2740, '職人': 2741, '泥臭く': 2742, '自己': 2743, 'ブランディング': 2744, '対極': 2745, 'ぜひとも': 2746, '意思決定': 2747, '自腹': 2748, '我々': 2749, '血税': 2750, '介護': 2751, '環境保全': 2752, '回さ': 2753, '流行らし': 2754, 'いし': 2755, '暴力': 2756, 'ノリ': 2757, '開か': 2758, 'エモい': 2759, '在留カード': 2760, '取り上げ': 2761, '選手': 2762, '嫌がらせ': 2763, '管理者': 2764, '立場': 2765, '外国人実習生': 2766, '取り上げる': 2767, '弱み': 2768, 'うえ': 2769, '最悪': 2770, 'ナチュ': 2771, '被っ': 2772, '見学': 2773, 'KR': 2774, 'すら': 2775, '明らか': 2776, 'オリーサ': 2777, 'スパイス': 2778, 'オフ会': 2779, '一つ': 2780, '深層学習': 2781, '用い': 2782, '統計': 2783, '分析': 2784, '出力': 2785, '入力': 2786, '予想': 2787, 'ツッコミどころ': 2788, '高校': 2789, '出て': 2790, '公務員': 2791, '千': 2792, '保証': 2793, 'もはや': 2794, '高校テニス': 2795, '規模': 2796, '悲惨': 2797, '◦': 2798, '事故現場': 2799, 'ゲグリ': 2800, '頑張っ': 2801, 'Taimou': 2802, 'け': 2803, 'cocco': 2804, '嫌い': 2805, 'lt': 2806, '↑': 2807, 'ワン': 2808, '会場': 2809, '歓声': 2810, '上がる': 2811, 'ボストン': 2812, 'ニューヨーク': 2813, 'ニート': 2814, '二人': 2815, '内': 2816, '大学生': 2817, '高校生': 2818, 'たしなん': 2819, 'どうして': 2820, '時給': 2821, '桁': 2822, 'mbps': 2823, '流石': 2824, 'ggwp': 2825, '研究室': 2826, 'おしゃれ': 2827, 'owl': 2828, '始まる': 2829, 'ギリギリ': 2830, 'ゼニモイラ': 2831, 'ナーフ': 2832, '名称': 2833, '連携': 2834, '賞金': 2835, '合法': 2836, '支払う': 2837, '新た': 2838, '反発': 2839, 'パズドラプロフォロワー': 2840, 'LONDON': 2841, 'KDP': 2842, 'GCB': 2843, '構成': 2844, 'APEX': 2845, 'VOID': 2846, 'ましてや': 2847, 'あんなに': 2848, 'jasper': 2849, 'チャレ': 2850, '右クリック': 2851, '上げろ': 2852, 'ドヤ': 2853, '悔しさ': 2854, 'バネ': 2855, '成り立っ': 2856, '偉い': 2857, '歪め': 2858, 'どうこう': 2859, '論調': 2860, '現実': 2861, '取り合い': 2862, '強め': 2863, '権化': 2864, '知り合い': 2865, '顔写真': 2866, '枚': 2867, 'AV': 2868, '出演': 2869, '技術的': 2870, '確実': 2871, 'ゴミ': 2872, 'さっ': 2873, '引っ越そ': 2874, 'スクリム': 2875, '重': 2876, 'フック': 2877, 'つられ': 2878, '中身': 2879, '制限': 2880, '時代': 2881, 'ゲンジ': 2882, '属': 2883, '風切り': 2884, '突っ込め': 2885, 'さよなら': 2886, 'でれー': 2887, 'ぶ': 2888, '犯罪': 2889, '仮想通貨': 2890, '度合い': 2891, '応じ': 2892, 'カルマ': 2893, 'ポイント': 2894, '増加': 2895, 'ラウンド': 2896, '等間隔': 2897, 'TOP': 2898, '次元': 2899, '身の回り': 2900, 'すべて': 2901, 'ウェーブサージ': 2902, 'バリア': 2903, '張ら': 2904, 'csgo': 2905, '詳しく': 2906, 'スマーフ': 2907, 'パーティー': 2908, '勝て': 2909, '爽快感': 2910, 'デブ': 2911, 'XQ': 2912, 'お墨付き': 2913, 'さすが': 2914, 'むに': 2915, '伸び': 2916, 'あるとき': 2917, 'ガンガン': 2918, '詰め': 2919, '取って': 2920, '逃げ道': 2921, 'ボイチェン': 2922, '許さ': 2923, 'miku': 2924, '太い': 2925, '指示': 2926, 'スタンプ': 2927, 'ギザギザ': 2928, 'がき': 2929, '教授': 2930, '面談': 2931, '論文': 2932, '本': 2933, '夢み': 2934, 'おもれ': 2935, 'えぐ': 2936, '食らわ': 2937, 'タイミング': 2938, '徹底': 2939, 'ファ': 2940, 'ラマ': 2941, '攻防': 2942, 'ポジ': 2943, 'ふけ': 2944, 'おめでとう': 2945, '間違えれ': 2946, 'デッドアイ': 2947, '警戒': 2948, 'キャップ': 2949, '番頭': 2950, '援護': 2951, '視界': 2952, '広く': 2953, '決める': 2954, '繰り返し': 2955, '延々と': 2956, 'ランクイン': 2957, '集計': 2958, '対象': 2959, '万人': 2960, '難し': 2961, 'パ': 2962, '入ら': 2963, '拷問': 2964, '時間帯': 2965, '電波': 2966, '激': 2967, 'ジャンク': 2968, '一生': 2969, 'ドラド': 2970, '力不足': 2971, '刺さっ': 2972, '田舎': 2973, 'スーパーチャージャー': 2974, '盾突き': 2975, '置い': 2976, '倒す': 2977, 'パクツイ': 2978, 'くそ': 2979, 'ジャンクラ': 2980, '間違い': 2981, 'インキャ': 2982, '所属': 2983, 'よろしくお願いします': 2984, '集まん': 2985, 'メンバー募集': 2986, 'ちゃっかり': 2987, '載せる': 2988, 'マウントゴックス': 2989, '被害額': 2990, '草草': 2991, 'シャム': 2992, '大人': 2993, '金づる': 2994, 'かわいそう': 2995, '韓国人': 2996, '国内': 2997, '他国': 2998, 'リーグ': 2999, '完成': 3000, '優位': 3001, 'なくなっ': 3002, 'シャドウ': 3003, 'バーン': 3004, 'Carpe': 3005, 'ロマン': 3006, 'わあ': 3007, 'フュージョン': 3008, 'SBB': 3009, 'ネトゲ': 3010, 'レーティング': 3011, '決まっ': 3012, 'いいね': 3013, 'アニオタ': 3014, '界隈': 3015, '学歴': 3016, '職業': 3017, '地位': 3018, 'アニメ業界': 3019, 'どれ': 3020, 'アニメ': 3021, '表現技法': 3022, '行わ': 3023, 'ダル': 3024, 'コミケ': 3025, '批評': 3026, '文': 3027, '盛ん': 3028, '血で血を洗う': 3029, 'いわ': 3030, 'weeked': 3031, '裏取り': 3032, '積極的': 3033, '着': 3034, '逃げれ': 3035, 'Dafran': 3036, '今すぐ': 3037, '入り': 3038, 'くどい': 3039, '絵': 3040, '淡白': 3041, '投票': 3042, 'ぇむって': 3043, 'マンガ': 3044, 'サイコ': 3045, '可愛さ': 3046, '独特': 3047, '織田信長': 3048, '信長': 3049, 'キルログ': 3050, '維持': 3051, 'がん': 3052, 'ばろん': 3053, 'つり革': 3054, 'つかまら': 3055, '満員電車': 3056, '思い切り': 3057, 'もたれかかっ': 3058, 'iCloud': 3059, 'オフ': 3060, '不可能': 3061, 'オフタンク': 3062, '立つ': 3063, '鳥': 3064, '濁す': 3065, 'その後': 3066, '最も': 3067, 'ちなみ': 3068, '銀だこ': 3069, '塩': 3070, 'マヨネーズ': 3071, '離れ': 3072, '弱': 3073, '一個': 3074, '東大': 3075, '地方': 3076, '駅弁': 3077, '国立': 3078, '魅力': 3079, '殴り': 3080, '合い': 3081, '佐藤かよ': 3082, '可愛い': 3083, '覚える': 3084, '苦手': 3085, '長く': 3086, '生き延びる': 3087, 'サポタン': 3088, 'ファース': 3089, 'トピック': 3090, 'つか': 3091, '市役所職員': 3092, 'ガチガチ': 3093, '固め': 3094, '税金': 3095, 'nCERO': 3096, 'A': 3097, '認め': 3098, '強気': 3099, 'っぷり': 3100, '優勝賞金': 3101, '決して': 3102, 'ガラパゴス化': 3103, 'ちまっ': 3104, '専攻': 3105, '漏れ': 3106, 'ショート': 3107, '育成': 3108, 'インフルエンサー': 3109, '支援': 3110, 'その間': 3111, 'ティーチング': 3112, '投げ銭': 3113, '稼ぐ': 3114, '素晴らし': 3115, '文字通り': 3116, '桁違い': 3117, 'グルメアプリ': 3118, '困っ': 3119, 'データベース': 3120, '頼れる': 3121, '体感': 3122, 'こんなに': 3123, '流動性': 3124, '激しい': 3125, 'nリーグ': 3126, 'ソウル': 3127, 'ラーメン屋': 3128, '見つけ': 3129, '表せ': 3130, 'マーケティング': 3131, '店': 3132, '雰': 3133, '囲': 3134, '看板': 3135, 'っぽ': 3136, 'さは': 3137, '丁': 3138, '肝心': 3139, '味': 3140, 'おざなり': 3141, 'めまい': 3142, 'スマホチェス': 3143, '0g': 3144, 'ガチャ': 3145, '回す': 3146, '0連勝': 3147, '気持ちよく': 3148, 'タイマン': 3149, '打ち': 3150, '若干': 3151, 'うち': 3152, 'ベター': 3153, '隣人': 3154, 'うるさいっ': 3155, 'プライド': 3156, '匿名': 3157, '見せる': 3158, 'パルス': 3159, '突撃': 3160, 'ビビっ': 3161, 'たまに': 3162, '竜': 3163, '撃破': 3164, '食らっ': 3165, 'させる': 3166, 'たま': 3167, '議論': 3168, '反対': 3169, 'キャラコ': 3170, 'ン': 3171, '下手': 3172, 'ゲーム内': 3173, '煽り': 3174, '煽ら': 3175, 'ムカ': 3176, '辛く': 3177, '白': 3178, '弱く': 3179, 'JAKE': 3180, '定点': 3181, 'コンカッション': 3182, 'とい': 3183, '残し': 3184, '逃げる': 3185, 'リスポーンポコポコスパム': 3186, 'ジワジワ': 3187, '戦中': 3188, 'たまらない': 3189, '吸収': 3190, '不利': 3191, '延命': 3192, '貯める': 3193, 'ヒーローキャリー': 3194, '平均': 3195, '奪う': 3196, 'らす': 3197, 'ごく楽': 3198, '称号': 3199, 'ついてる': 3200, 'ww': 3201, 'グラマスウィドウ': 3202, 'おれ': 3203, 'ちなみに': 3204, 'PV': 3205, 'フォロワー': 3206, '広報': 3207, '発信': 3208, 'リーチ': 3209, 'だから': 3210, 'もらい': 3211, '聖典': 3212, '気合い': 3213, 'もう一度': 3214, 'PS0': 3215, 'まず': 3216, 'マウサー': 3217, 'なろ': 3218, '強調': 3219, '段差': 3220, '頭ぶ': 3221, 'フレタ': 3222, '高': 3223, 'メック': 3224, 'ぶつけれ': 3225, 'オアシス': 3226, 'ルシオモイラ': 3227, 'Tviq': 3228, '好きなんだけど': 3229, 'アザ': 3230, 'ラック': 3231, 'プール': 3232, '広い': 3233, '専門性': 3234, 'がっつり': 3235, '感銘': 3236, 'ディスコード': 3237, '釣る': 3238, '同時に': 3239, '書き込ん': 3240, 'すごく': 3241, '緊張': 3242, '走る': 3243, '担当': 3244, '正直しんどい': 3245, 'っと': 3246, '破壊力': 3247, 'のう': 3248, 'ざさ': 3249, 'おかしな': 3250, 'モルテンコア': 3251, '返り討ち': 3252, 'えぐい': 3253, 'torb': 3254, '注意': 3255, '引き続け': 3256, 'トールビョーンマジ': 3257, 'ライトユーザー': 3258, '脱オタク': 3259, 'ペディア': 3260, '我': 3261, '内容': 3262, '書け': 3263, '読み返し': 3264, 'にとって': 3265, '良く': 3266, '少ない': 3267, '少なく': 3268, '教科書': 3269, '得': 3270, 'Re': 3271, 'メンバー全員': 3272, 'マーシーウルト': 3273, 'うつ': 3274, 'ぶれる': 3275, '側面': 3276, '分岐': 3277, 'nRIP': 3278, 'バイザー': 3279, 'ささる': 3280, 'グラビトンサージ': 3281, '重要性': 3282, '自信': 3283, 'タイン': 3284, '即': 3285, 'ピ': 3286, '地獄': 3287, '帯': 3288, 'saebyeolbe': 3289, '間合い': 3290, '取り': 3291, '美しく': 3292, '芸術': 3293, 'スパイ': 3294, 'ギア': 3295, 'よん': 3296, 'オバペディア': 3297, 'データセット': 3298, 'なに': 3299, '読み込ん': 3300, 'プログラミング': 3301, '奨学金': 3302, '薄く': 3303, '配る': 3304, '狭く': 3305, '太く': 3306, '配っ': 3307, '優秀': 3308, '後輩': 3309, 'しょう': 3310, 'バイト': 3311, '勿体無く': 3312, 'しんどく': 3313, 'google翻訳': 3314, '過ぎる': 3315, 'Lasty': 3316, 'イリダータ': 3317, 'ほか': 3318, '悔しく': 3319, '奇声': 3320, '上げる': 3321, '数年': 3322, 'nOverwatch': 3323, '悪影響': 3324, 'ストレス': 3325, '与え': 3326, '重度': 3327, '入院': 3328, '至る': 3329, '悪質': 3330, 'ドラッグ': 3331, '驚い': 3332, 'ってか': 3333, '軸': 3334, '盛り上げる': 3335, '営利目的': 3336, '好ま': 3337, '求め': 3338, 'かって': 3339, 'ローグ': 3340, '母体': 3341, '支配': 3342, 'コピペ': 3343, 'スクショ': 3344, 'txt': 3345, '落とし込め': 3346, 'D0': 3347, 'watch': 3348, 'アップライジング': 3349, '戦い方': 3350, 'マクロ': 3351, '調べれ': 3352, '平等': 3353, '機会': 3354, '親': 3355, 'デジタルディバイド': 3356, 'たどり着け': 3357, '個々人': 3358, '国立大学': 3359, '持ちだし': 3360, 'センター': 3361, '鑑': 3362, 'センター試験': 3363, 'やな': 3364, '受験': 3365, '不祥事': 3366, '起きれ': 3367, '試験': 3368, 'やり直し': 3369, 'おお': 3370, '日本時間': 3371, 'からか': 3372, 'うてる': 3373, 'NY': 3374, '仕方': 3375, 'おやすみなさい': 3376, '違': 3377, 'く': 3378, '龍神': 3379, '剣': 3380, 'キャンセル': 3381, '環境': 3382, 'コントロール': 3383, '活躍': 3384, 'スーパーエイム': 3385, '期待': 3386, 'Apex': 3387, 'LH': 3388, '無線マウス': 3389, '無線': 3390, 'xQc': 3391, 'シャターサージ': 3392, '返さ': 3393, 'マジゴミ': 3394, 'らっと': 3395, '局所': 3396, '源': 3397, '自体': 3398, '消し': 3399, 'ちゃう': 3400, 'イメージ': 3401, '土管': 3402, 'fleta': 3403, 'TOBI': 3404, '焦り': 3405, 'だす': 3406, 'リーパー': 3407, 'Fleta': 3408, 'ちい': 3409, '高度': 3410, '個人技': 3411, '理不尽': 3412, '生まれ': 3413, 'チップスマジ': 3414, 'やわー': 3415, 'り': 3416, 'ゅ': 3417, 'トイレ': 3418, 'HS': 3419, 'ウイドウ': 3420, 'お互い': 3421, 'ぶち': 3422, '抜き': 3423, '下手くそ': 3424, '腐っ': 3425, '引き連れ': 3426, 'げんなり': 3427, 'スピード感': 3428, 'テンセント': 3429, '忙し': 3430, '楽しむ': 3431, '向上': 3432, '打ち勝ち': 3433, '味わう': 3434, 'パブ': 3435, 'リッシャ': 3436, 'アイデア': 3437, '覇権': 3438, '握っ': 3439, 'ちゃ': 3440, 'Auto': 3441, 'Chess': 3442, 'iOS': 3443, 'パクリゲー': 3444, '進化': 3445, '段階': 3446, '広告費': 3447, 'かかわら': 3448, '件': 3449, 'すで': 3450, '本家': 3451, '運命': 3452, '土日': 3453, '追加': 3454, '発表': 3455, '合宿': 3456, 'おやすみ': 3457, '系': 3458, '視聴': 3459, '置き換える': 3460, '撃ち殺し': 3461, '暴れる': 3462, 'ごり押し': 3463, 'アップデート': 3464, '本物': 3465, 'アイデンティティ': 3466, '概念': 3467, '埋もれ': 3468, 'ルナ': 3469, '頃': 3470, 'お題': 3471, 'グループ': 3472, 'アップ': 3473, 'エゴサ': 3474, 'オススメ': 3475, '何人': 3476, '惑わさ': 3477, '描い': 3478, 'かこ': 3479, 'LimitBreaks': 3480, '青年': 3481, '勇士': 3482, '喋り': 3483, '伝える': 3484, 'ほん': 3485, 'XQQ': 3486, '態度': 3487, '有意義': 3488, 'スナイプトロール': 3489, 'pichu': 3490, 'たん': 3491, '咎め': 3492, '怪しい': 3493, 'ウォッチ': 3494, '切り替え': 3495, '待機': 3496, 'カッコ': 3497, '一覧': 3498, '隠せる': 3499, 'ユーモア': 3500, '振り返る': 3501, '回数': 3502, 'ゼニャッタ': 3503, 'てこ': 3504, 'いつう': 3505, 'め': 3506, '限界': 3507, '撤廃': 3508, '遠慮なく': 3509, 'バスティオン': 3510, '浴び': 3511, '続け': 3512, 'アーマー': 3513, '受けれ': 3514, 'カット': 3515, '0発': 3516, 'スケ': 3517, 'べし': 3518, '選び': 3519, '反則': 3520, '級': 3521, '運転手': 3522, 'じゃない方': 3523, 'セーフ': 3524, '助っ人': 3525, 'nS': 3526, 'FUCK': 3527, 'くき': 3528, '前期': 3529, '泣き': 3530, '背筋': 3531, '立て': 3532, 'どんどん': 3533, 'キチガイ': 3534, '戻し': 3535, '善意': 3536, '悪意': 3537, '役に立た': 3538, '公平': 3539, '働く': 3540, '引っ張り': 3541, 'がり': 3542, 'ノイジーマイノリティ': 3543, '回転寿司': 3544, '生ん': 3545, '文化': 3546, 'この世': 3547, 'カルビン': 3548, 'デッドアイキャンセルリロード': 3549, '大好き': 3550, '寝起き': 3551, '地震速報': 3552, '走馬灯': 3553, '見かけ': 3554, 'otp': 3555, '隠し': 3556, '通常': 3557, 'ワンチャン': 3558, 'おわ': 3559, 'コンピョーターサイエンス': 3560, 'オタク': 3561, 'たち': 3562, '学問': 3563, 'パンチ': 3564, '挟む': 3565, '節約': 3566, '壊す': 3567, '増やす': 3568, '族': 3569, 'キルタイム': 3570, 'あきまん': 3571, 'ストファイ': 3572, '開示': 3573, '透明性': 3574, '健全': 3575, 'Legal': 3576, 'action': 3577, 'will': 3578, 'e': 3579, 'taken': 3580, 'ネタ': 3581, '玉': 3582, '半径': 3583, 'メートル': 3584, '何度': 3585, '角度': 3586, 'パーセント': 3587, '反射': 3588, 'まっすぐ': 3589, '向かっ': 3590, 'クネ': 3591, '貧者': 3592, 'VR': 3593, '自己愛': 3594, '宗教': 3595, 'マクリートレーサー': 3596, 'ざる': 3597, '解消': 3598, '限定': 3599, '思わず': 3600, '高校受験': 3601, '中学生': 3602, 'アラド戦記': 3603, 'SF': 3604, '懐かし': 3605, '問題発言': 3606, '自ら': 3607, '停滞': 3608, 'みなす': 3609, '設計': 3610, '工夫': 3611, '自己満足': 3612, 'ベクトル': 3613, '違和感': 3614, '現実的': 3615, '引き起こし': 3616, '生活': 3617, '苦労': 3618, 'アフェリエイト': 3619, '一円': 3620, '奴ら': 3621, 'オブラート': 3622, '動く': 3623, 'アマチュア': 3624, '作戦': 3625, '雑魚': 3626, 'ディ': 3627, 'おら': 3628, 'トップチーム': 3629, '公表': 3630, '今後': 3631, 'おそらく': 3632, '永遠に': 3633, '広告塔': 3634, '役割': 3635, '自己紹介': 3636, 'デバイス': 3637, '乗っかっ': 3638, 'サル': 3639, 'しろ': 3640, '名乗っ': 3641, '情報発信': 3642, 'アピール': 3643, '最低限': 3644, 'ツーイト': 3645, '当時': 3646, '増し': 3647, '手のひら': 3648, 'くるくる': 3649, '有象無象': 3650, 'カス': 3651, 'そんな': 3652, '月数': 3653, '後世': 3654, '自称': 3655, 'テンション': 3656, 'そーいや': 3657, 'スら': 3658, 'フィジカル': 3659, '面': 3660, 'おせ': 3661, 'エイムカス': 3662, '明け': 3663, '同調圧力': 3664, '銃社会': 3665, '銃': 3666, '売れる': 3667, 'なくなら': 3668, 'スワット': 3669, 'みれ': 3670, 'やってくる': 3671, '確かめる': 3672, '手順': 3673, 'おかしいっ': 3674, 'くない': 3675, '去年': 3676, '年越し': 3677, 'ぶっ続け': 3678, 'ライゼスト': 3679, '年越しイベント': 3680, 'NOT': 3681, '野良連合': 3682, 'CANON': 3683, '一眼': 3684, 'じっと': 3685, '日本製': 3686, '正月': 3687, '帰れ': 3688, '後人': 3689, '切れる': 3690, 'カ能': 3691, '学生時代': 3692, '受託': 3693, '稼い': 3694, '高専': 3695, '出身': 3696, '学部': 3697, '間に合わ': 3698, 'ナチュラル': 3699, 'ゴリゴリ': 3700, 'スマーフサブ': 3701, '様相': 3702, '抑え': 3703, 'チンパンジー': 3704, '0度': 3705, 'うーん': 3706, '様': 3707, '胃': 3708, 'キリ': 3709, '光彩': 3710, 'MOBA': 3711, '相関': 3712, 'va': 3713, 'きれ': 3714, 'おろそか': 3715, 'ウルトチャージ': 3716, '攻撃力': 3717, '00倍': 3718, '速度': 3719, '量的': 3720, 'パリピ': 3721, '流': 3722, '自殺': 3723, 'なそ': 3724, '引き合い': 3725, '敗因': 3726, 'スケープゴート': 3727, 'てなんと': 3728, 'タノチー': 3729, 'あまっ': 3730, '震え': 3731, 'taiyo': 3732, 'リスポーン': 3733, 'リロード': 3734, '振り向い': 3735, '影響力': 3736, 'skyfull': 3737, 'きって': 3738, '変態': 3739, 'DANTE': 3740, 'ROY': 3741, 'AL': 3742, '何者': 3743, 'ドラミング': 3744, 'たさ': 3745, 'ｗｗｗｗｗ': 3746, 'roy': 3747, 'al': 3748, '正しく': 3749, '社会保障': 3750, '弱者救済': 3751, '社会主義': 3752, '法人税': 3753, '国家': 3754, 'プロフ': 3755, '画': 3756, '度': 3757, '笑える': 3758, '一部の人': 3759, '需要': 3760, '丁寧': 3761, '雑記': 3762, 'アメリカ代表': 3763, 'ボム': 3764, 'ぶっ飛ばす': 3765, '組ま': 3766, 'せれ': 3767, '機動力': 3768, '三拍子': 3769, 'そろっ': 3770, 'ジャンクラット': 3771, 'ニッチピックメイン': 3772, 'クリスマス': 3773, 'ビッグデータ': 3774, '教える': 3775, '偏見': 3776, 'はらま': 3777, 'nAlphaGO': 3778, 'Alpha': 3779, 'とらわれ': 3780, '普遍': 3781, '真理': 3782, 'いえる': 3783, '曖昧': 3784, '出せ': 3785, 'を通して': 3786, '事実': 3787, 'らん': 3788, 'ずれ': 3789, '近い': 3790, 'ハック': 3791, '不当': 3792, '得る': 3793, '思想': 3794, '全体最適': 3795, '資本主義': 3796, '実務': 3797, '実行': 3798, '組織': 3799, '並列': 3800, 'まとま': 3801, '扱わ': 3802, 'により': 3803, '外貨': 3804, '良貨': 3805, '駆逐': 3806, '無い': 3807, 'ミクロ': 3808, 'コード': 3809, '総合格闘技': 3810, 'こなす': 3811, 'クラウドワークス': 3812, '対': 3813, 'マッチングサイト': 3814, 'クライアント': 3815, '手抜き': 3816, 'チャットボット': 3817, '組み': 3818, '営業力': 3819, '無': 3820, '頼む': 3821, '外注': 3822, 'ろくな': 3823, '終わる': 3824, '郵便局': 3825, '挙句': 3826, '代替': 3827, '学費': 3828, '安さ': 3829, '多様性': 3830, '留学': 3831, 'ありがたさ': 3832, '潰し': 3833, 'きき': 3834, '代え': 3835, '難い': 3836, '黎明期': 3837, '専門学校': 3838, '分野': 3839, '立てよ': 3840, '相応': 3841, '覚悟': 3842, '講師': 3843, '雇う': 3844, '学校': 3845, '経営': 3846, '成り立た': 3847, '実績': 3848, 'カリキュラム': 3849, '立ち': 3850, '授業': 3851, '生徒': 3852, '経験': 3853, '現状': 3854, '乖離': 3855, '発生': 3856, '避け': 3857, '多産': 3858, '死': 3859, '芽': 3860, '体育大学': 3861, 'スポーツ選手': 3862, '暮らせる': 3863, '暴論': 3864, '挑戦': 3865, '土壌': 3866, '用意': 3867, '旧来': 3868, '生産性': 3869, '普及': 3870, '雇用': 3871, '守る': 3872, '法律': 3873, 'ツケ': 3874, 'イキリ': 3875, 'お手本': 3876, '全力': 3877, '疎ま': 3878, 'とも': 3879, 'イキリパワー': 3880, '魂': 3881, '落とさ': 3882, '下がっ': 3883, 'リンク': 3884, '一本': 3885, '出かける': 3886, '引い': 3887, '絶望': 3888, '残す': 3889, '時事': 3890, '人見': 3891, '広': 3892, 'ちげ': 3893, '前見': 3894, '横見': 3895, '狙う': 3896, '的確': 3897, 'ワンマガ': 3898, 'saebyelobe': 3899, 'マジゲーム': 3900, 'Gesture': 3901, '表明': 3902, '示し': 3903, '反響': 3904, 'ウケ': 3905, 'リポート': 3906, 'jp': 3907, 'シリーズ化': 3908, '低く': 3909, '扱い': 3910, '認知': 3911, '自宅': 3912, 'エクセル': 3913, 'MS': 3914, 'Office': 3915, '製品': 3916, 'しゃー': 3917, 'イラレ': 3918, '妹': 3919, '美人': 3920, '不完全': 3921, '締切': 3922, '決めて': 3923, '昼': 3924, '締め切り': 3925, 'グラフ': 3926, 'Radeon': 3927, '素材': 3928, '動画編集': 3929, 'youtube': 3930, '過去最高': 3931, 'エネルギー': 3932, 'クリ': 3933, '近接': 3934, '立っ': 3935, '言い訳': 3936, '歩': 3937, '客観的': 3938, '空気': 3939, 'バランス': 3940, '人格': 3941, '認める': 3942, '択': 3943, 'スピーディー': 3944, '行える': 3945, '雰囲気': 3946, '物事': 3947, '固める': 3948, '擦り': 3949, 'はっきり': 3950, '勘違い': 3951, 'ごめんなさい': 3952, '突っ込み': 3953, 'どころ': 3954, 'KOYAMA': 3955, 'ジャン': 3956, 'ロケジャン': 3957, '障碍者': 3958, '呼ん': 3959, '試合中': 3960, 'かく乱': 3961, '勝手': 3962, '存続': 3963, '兼': 3964, 'ビデオ撮影': 3965, '係': 3966, '悔し': 3967, 'いかれ': 3968, 'まさかの': 3969, '上手い': 3970, 'ドゥーム': 3971, 'ぼこぼこ': 3972, '駅前': 3973, '在日特権': 3974, '軍団': 3975, '暴れ': 3976, 'ベンチプレス': 3977, 'クラン': 3978, '撮影': 3979, '元祖': 3980, 'pray': 3981, 'for': 3982, 'us': 3983, '集結': 3984, 'メンツ': 3985, '商品': 3986, '狙っ': 3987, '龍': 3988, 'ぼんやり': 3989, 'サイクロプス': 3990, 'そうとう': 3991, 'カート': 3992, '止め': 3993, 'おもしろかっ': 3994, '恒例': 3995, '変': 3996, '子供': 3997, '精神的負担': 3998, '大き': 3999, 'スナイプ': 4000, '粘着': 4001, '車': 4002, 'ひく': 4003, '筑': 4004, '豊': 4005, '考えよ': 4006, 'フィードバック': 4007, 'ドライバ': 4008, 'マイク': 4009, '音': 4010, '拾わ': 4011, '一通り': 4012, 'トラブルシューティング': 4013, '試し': 4014, '拾っ': 4015, 'nPC': 4016, '端子': 4017, 'ケース': 4018, 'マザボ': 4019, 'それでも': 4020, 'だめ': 4021, '敗退': 4022, 'お疲れ様': 4023, 'りさん': 4024, 'クリーンインストール': 4025, 'ナンパ': 4026, 'イスラム教': 4027, '禁止': 4028, 'Tier': 4029, 'シンメトラ': 4030, 'ナンバーワン': 4031, '暇': 4032, 'Ana': 4033, 'gold': 4034, 'Grandmaster': 4035, '通し': 4036, '仮説': 4037, '思いつい': 4038, 'webサービス': 4039, '進め': 4040, '来年': 4041, '短期': 4042, 'サンマ': 4043, '解散': 4044, 'ジャンクラマジ': 4045, '深夜': 4046, '叩け': 4047, '叩い': 4048, 'wwww': 4049, 'RON': 4050, '僕達': 4051, 'どうせ': 4052, 'うん': 4053, '千円': 4054, 'かうん': 4055, '連絡': 4056, '突き詰め': 4057, '精神的': 4058, '厳しく': 4059, 'いい加減': 4060, 'ズボラ': 4061, '例えば': 4062, '風向き': 4063, '偶然': 4064, 'しかし': 4065, '将棋': 4066, 'つながら': 4067, 'しまい': 4068, '学科': 4069, '思い出し': 4070, '無能': 4071, '共': 4072, 'ボイス': 4073, '耳元': 4074, '聞か': 4075, '連呼': 4076, '既に': 4077, '程度': 4078, '自然': 4079, '表情': 4080, '報酬': 4081, '脳': 4082, '刺激': 4083, 'さらに': 4084, '追い求める': 4085, '習性': 4086, 'もてあそば': 4087, '泥沼': 4088, 'はまっている': 4089, '長文': 4090, 'まとめれ': 4091, '格上': 4092, 'ベスト': 4093, 'ハンド': 4094, '覆せ': 4095, '試合結果': 4096, '良しあし': 4097, '見分ける': 4098, '人心': 4099, '掌握': 4100, '人として': 4101, 'パフォーマンス': 4102, '引き出し': 4103, '思いやっ': 4104, '発揮': 4105, '楽勝': 4106, 'ホワイト企業': 4107, '望ん': 4108, 'ブラック企業': 4109, 'まったく': 4110, '理論': 4111, '意図': 4112, 'くみ取っ': 4113, 'or': 4114, '同様': 4115, '向き': 4116, '不向き': 4117, '動い': 4118, 'コーパス': 4119, 'つかっ': 4120, '正規': 4121, 'ノンネイティブ': 4122, '戦略': 4123, 'ゴミ箱': 4124, 'ポエム': 4125, 'チラシの裏': 4126, '乗る': 4127, '積極的休養': 4128, 'サバゲー': 4129, 'エイ': 4130, 'ム力': 4131, 'マシン': 4132, '組み合わせ': 4133, '状況判断': 4134, 'クリア': 4135, '進める': 4136, '報告': 4137, '色': 4138, '幅': 4139, '情熱': 4140, '好奇心': 4141, '定位': 4142, '判別': 4143, 'ゼンハイザー': 4144, '追わ': 4145, 'ビットコイン': 4146, '技術': 4147, 'BTC': 4148, 'BCH': 4149, 'segwit': 4150, 'こっち': 4151, '0次': 4152, '追い': 4153, 'トレード': 4154, '引っかから': 4155, '0ch': 4156, 'アフィブログ': 4157, '外し': 4158, 'フルダイブ': 4159, 'スタン': 4160, 'みに': 4161, 'ムッチャ': 4162, 'ケバブ': 4163, '店舗': 4164, '毛色': 4165, 'トルコ料理': 4166, '高学歴': 4167, 'キラキラ': 4168, '終身雇用': 4169, '年功序列': 4170, '人生': 4171, '安泰': 4172, '♫': 4173, '価値観': 4174, 'むず痒く': 4175, 'サンクコスト': 4176, '手札': 4177, '観': 4178, '高田馬場': 4179, 'インターン': 4180, '卒論': 4181, 'メーカー': 4182, 'Amazon': 4183, '業者': 4184, 'レビュー': 4185, 'のっ': 4186, '一周': 4187, '担当者': 4188, '信頼': 4189, '思える': 4190, '酒飲み': 4191, '肉': 4192, '海鮮': 4193, '原価': 4194, '直撃': 4195, 'ワイン': 4196, '飲ま': 4197, 'まさに': 4198, 'PDCA': 4199, '風': 4200, '満足': 4201, '成長': 4202, '損切り': 4203, '痛む': 4204, '心': 4205, '堀川': 4206, '痛い': 4207, 'おもしろ': 4208, 'ちー': 4209, '質問箱': 4210, '心情': 4211, '泣け': 4212, '漫画': 4213, 'ヘルク': 4214, '最終話': 4215, '苦悩': 4216, 'アン': 4217, 'ストーリー': 4218, '希望の光': 4219, '綺麗': 4220, '全巻': 4221, 'ポチる': 4222, '安全': 4223, '帰る': 4224, '未来永劫': 4225, '残る': 4226, '思考': 4227, '寄稿': 4228, '初め': 4229, '説明': 4230, '出来上がっ': 4231, '充実': 4232, '高かっ': 4233, 'なんだか': 4234, '希望': 4235, 'F': 4236, 'K0': 4237, 'ラバー': 4238, 'ホイール': 4239, 'クリック': 4240, '良さ': 4241, '気に入っ': 4242, 'rival': 4243, '諦め': 4244, 'DPI': 4245, 'ingame': 4246, '手首': 4247, '支点': 4248, 'っぱなし': 4249, '着地': 4250, '効果的': 4251, '短期的': 4252, 'スシロー': 4253, '段ボール': 4254, '取引': 4255, '人神': 4256, '00': 4257, '儲け': 4258, 'UUUM': 4259, 'アイドル': 4260, '修羅': 4261, '道': 4262, '活用': 4263, 'など': 4264, '知名度': 4265, 'ミッキー': 4266, '絡み': 4267, 'ジェフカプラン': 4268, '甘': 4269, '嘘っぱち': 4270, '発': 4271, 'DF': 4272, '冷': 4273, 'ひえ': 4274, '課税': 4275, '競馬': 4276, 'FB': 4277, '形': 4278, 'いま': 4279, 'まい': 4280, '＝': 4281, 'プレイ': 4282, '裏返し': 4283, '運営側': 4284, '表面的': 4285, 'ランクマッチ': 4286, 'オフシーズン': 4287, '長い': 4288, 'やばいっ': 4289, '営利企業': 4290, 'のす': 4291, '原因': 4292, 'DQR': 4293, 'しば': 4294, '遊ぶ': 4295, 'slack': 4296, 'ショートカット': 4297, 'コマンド': 4298, 'ワンパンマン': 4299, 'ことば': 4300, 'グレイラース': 4301, 'top': 4302, '手段': 4303, 'いくらでも': 4304, '試せ': 4305, '仮説検証': 4306, 'さしづめ': 4307, '出世': 4308, '天井': 4309, 'アラフォー': 4310, 'スタミナ': 4311, '向き合っ': 4312, '意思': 4313, 'マンネリ': 4314, '失わ': 4315, 'げーじ': 4316, 'ゃないと': 4317, '真剣': 4318, 'ジレンマ': 4319, 'ドラゴンクエストライバルズ': 4320, 'nOW': 4321, '解除': 4322, '通知': 4323, 'ズゴゴゴゴ': 4324, 'ピルロ': 4325, 'すごそ': 4326, '俯瞰': 4327, '力強い': 4328, 'バスケ': 4329, 'だして': 4330, 'ジェットコースター': 4331, '蓄え': 4332, '位置エネルギー': 4333, '解放': 4334, 'れよ': 4335, '課金': 4336, 'taigahagorrila': 4337, '予想外': 4338, 'マッチョ': 4339, 'かかり': 4340, '小学校': 4341, 'クラス': 4342, '匿名性': 4343, '相まって': 4344, '定期的': 4345, '風斬り': 4346, 'スピード': 4347, 'CPU': 4348, 'スパコン': 4349, 'sinatraa': 4350, 'ブリンク': 4351, '距離': 4352, '適切': 4353, 'ス': 4354, 'みえる': 4355, '読み返す': 4356, '人間性': 4357, '0話': 4358, 'ハロー効果': 4359, '強烈': 4360, 'じわじわ': 4361, 'webサイト': 4362, 'やったー': 4363, '返せる': 4364, 'ワンウェーブ': 4365, 'バスティオリーサハルトザリア': 4366, 'フルメンバー': 4367, 'ゃないってよくわからんけどすごい': 4368, '起こっ': 4369, 'べつ': 4370, '指導者': 4371, '小遣い': 4372, '稼ぎ': 4373, '忙しい': 4374, '社会人': 4375, '満たせる': 4376, 'web': 4377, 'ウェブサイト': 4378, '足りる': 4379, '競技': 4380, '提出': 4381, 'ステ': 4382, '会見': 4383, 'めんどい': 4384, '多様': 4385, '特徴': 4386, 'パラメタライズ': 4387, '勝者': 4388, '振る舞う': 4389, '替玉': 4390, '名古屋': 4391, 'OJA': 4392, '勝ち星': 4393, '刻ま': 4394, 'oja': 4395, 'sns': 4396, 'スポンサー': 4397, '代表': 4398, '失言': 4399, 'しな': 4400, 'やし': 4401, '見習う': 4402, 'お前': 4403, 'アザラック': 4404, 'リフトオフ': 4405, 'ぼん': 4406, 'ブラウン': 4407, 'アルターエデン': 4408, 'た人': 4409, 'Rpg': 4410, 'まるで': 4411, '社会性': 4412, 'ヤベー': 4413, '平常心': 4414, '全身': 4415, '埋め': 4416, '尽くし': 4417, 'カフェイン': 4418, '半減期': 4419, '即席': 4420, 'エンジョイ': 4421, 'チェックイン': 4422, '間に合う': 4423, 'ルーキー': 4424, 'カップ': 4425, 'ディブロ': 4426, 'そりゃ': 4427, 'つよい': 4428, 'ONE': 4429, 'モブサイコ': 4430, '投球': 4431, '裏サンデー': 4432, 'HELCK': 4433, '完結': 4434, 'やば': 4435, '迷走': 4436, 'GCWiki': 4437, 'オーバーウォッチ': 4438, '移転': 4439, 'リダイレクト': 4440, '順位': 4441, '消え去っ': 4442, 'GamerCoachWiki': 4443, '本腰': 4444, '教材': 4445, '媒体': 4446, 'テキスト': 4447, '目指し': 4448, 'Twitter': 4449, '上手く': 4450, 'できれ': 4451, 'あんま': 4452, '卒業生': 4453, '受け入れる': 4454, '無自覚': 4455, '嫉妬心': 4456, '私': 4457, '勇気': 4458, 'あなた': 4459, '許し': 4460, 'クソリプ': 4461, '辟易': 4462, '斜': 4463, '構え': 4464, '嫌儲': 4465, 'マン': 4466, 'ダサ': 4467, '異常': 4468, '最たる': 4469, 'そういった': 4470, '生まれる': 4471, '喜び': 4472, '儲ける': 4473, 'よし': 4474, '近所': 4475, 'ゴールドジム': 4476, '屋': 4477, 'メン': 4478, 'これこれ': 4479, '振っ': 4480, '家で': 4481, 'ヶ月': 4482, 'はじめて': 4483, '売上': 4484, 'ゴーツ': 4485, 'そろそろ': 4486, '飽き': 4487, 'ハク': 4488, 'バチバチ': 4489, 'Rascal': 4490, 'Akm': 4491, '喧嘩': 4492, 'クビ': 4493, '成し遂げ': 4494, 'トキシック': 4495, '天才': 4496, 'タイプ': 4497, '低め': 4498, 'ワーク': 4499, 'nDF': 4500, '温厚': 4501, '多め': 4502, 'iPhone': 4503, 'Android': 4504, 'ゲームクラブ': 4505, 'コミュニティサイト': 4506, '文中': 4507, 'GamersClub': 4508, 'mode': 4509, 'ブラジル': 4510, '語': 4511, 'トップクラス': 4512, '精神衛生上': 4513, '理想': 4514, 'そこで': 4515, '局所化': 4516, 'ユートピア': 4517, '永遠': 4518, 'まよっ': 4519, '社員': 4520, '権限': 4521, 'にかけて': 4522, '寒い': 4523, 'スプレー': 4524, '盤面': 4525, '潰さ': 4526, 'ギルド': 4527, 'アグロチンパンズ': 4528, '伝わる': 4529, 'ゼシカアンチ': 4530, 'ひとだま': 4531, 'バイキング': 4532, 'ミラー': 4533, 'マリガン': 4534, '最優先': 4535, '行こ': 4536, 'ゼシカ': 4537, 'クソゲー': 4538, 'マナ': 4539, 'バラモス': 4540, 'みならいあくま': 4541, 'はまじ': 4542, 'テンポゼシカ': 4543, 'キーカード': 4544, 'NR': 4545, '北海道': 4546, '大概': 4547, 'ガバガバ': 4548, '自己弁護': 4549, '公式アカウント': 4550, 'リツイート': 4551, '人相': 4552, '当': 4553, '入れ替え': 4554, '毎度': 4555, 'ディスる': 4556, '恥ずかしい': 4557, 'セクシービーム': 4558, 'トラ': 4559, '特技': 4560, 'アグロ': 4561, 'アグロゼシカ': 4562, '人魂': 4563, 'ミネア': 4564, 'リーダー': 4565, 'アリーナ': 4566, '占い師': 4567, 'トルネコ': 4568, '闘技': 4569, '場': 4570, '三枚': 4571, '考慮': 4572, 'わた': 4573, 'ぼう': 4574, '中国人': 4575, '女性': 4576, 'ど': 4577, 'ゆこ': 4578, 'スライド': 4579, '同情': 4580, 'スタイル': 4581, '移行': 4582, '朝': 4583, 'プレゼン': 4584, '資料': 4585, '真っ赤': 4586, 'いつも': 4587, '切れ': 4588, '失神': 4589, 'エピソード': 4590, '縛り': 4591, 'デッキ': 4592, '錬': 4593, '足りん': 4594, 'dqr': 4595, '奥': 4596, '後々': 4597, 'サイレス': 4598, '封じ': 4599, 'ガチャコッコ': 4600, 'けやり': 4601, 'レジェ': 4602, '我が': 4603, 'アグロチンパンリア': 4604, '友': 4605, 'ターン': 4606, '除去': 4607, 'アンサー': 4608, '亡者': 4609, 'ござっ': 4610, '交換': 4611, 'バンバン': 4612, '打点': 4613, '減らさ': 4614, '場面': 4615, 'のっち': 4616, '色んな': 4617, 'はぐれメタル': 4618, '何故か': 4619, 'トラップ': 4620, '顔面': 4621, '殴れる': 4622, '倒さ': 4623, '揃え': 4624, 'カード': 4625, 'アグロデッキ': 4626, 'きが': 4627, 'カミュ': 4628, 'キャラガチ': 4629, 'テリー': 4630, '序盤': 4631, '縦': 4632, '並べる': 4633, '削り': 4634, '悔しい': 4635, '先程': 4636, '並べ': 4637, '斜め': 4638, '並ぶ': 4639, 'チンパン': 4640, '研究発表': 4641, '文系': 4642, '噛み砕い': 4643, '用語': 4644, '専門用語': 4645, 'だらけ': 4646, '冒頭': 4647, 'キチ': 4648, 'よろ': 4649, '次ぐ': 4650, 'なるほど': 4651, 'なぁ': 4652, 'ソシャゲ': 4653, '観点': 4654, 'とらえ': 4655, '論': 4656, '盛り上がり': 4657, '単に': 4658, 'すく': 4659, 'リム': 4660, '消滅': 4661, 'ドラクエライバルズ': 4662, '想像': 4663, 'ドラクエ': 4664, 'ククール': 4665, '無敗': 4666, 'こっ': 4667, '上がら': 4668, 'アグロアンチ': 4669, '後なん': 4670, 'ちょいちょい': 4671, 'ドルイド': 4672, 'DQ': 4673, 'ライバル': 4674, '有り': 4675, '丸パクリ': 4676, 'たし': 4677, '引ける': 4678, 'りゅうおう': 4679, 'アンルシア': 4680, '共通': 4681, 'ぜ': 4682, 'とく': 4683, 'ノアノア': 4684, 'モチベ': 4685, 'つまん': 4686, '喜んで': 4687, '横流し': 4688, '訳し': 4689, '断捨離': 4690, '秋': 4691, '秋葉原': 4692, 'おばさん': 4693, '眠く': 4694, '必ず': 4695, '生活習慣': 4696, '秋葉': 4697, '向かい': 4698, '射程': 4699, '追尾': 4700, '野球': 4701, 'セカンドキャリア': 4702, '込み': 4703, '買い': 4704, '売り出し': 4705, '売り': 4706, '売る': 4707, '売っ': 4708, '良心': 4709, '価格': 4710, 'チャット': 4711, 'おまけ': 4712, 'つき': 4713, 'チェーン': 4714, 'たこ焼き屋': 4715, 'たろ': 4716, '惰性': 4717, '消す': 4718, '梅原': 4719, '偏差値': 4720, '必死': 4721, 'かかわる': 4722, '塾': 4723, '余地': 4724, 'ブランド': 4725, 'のち': 4726, '些末な': 4727, 'ベース': 4728, 'おい': 4729, 'Top': 4730, 'マジバケモン': 4731, 'owpedia': 4732, 'Overpedia': 4733, 'ついてれ': 4734, '一瞬': 4735, '置け': 4736, 'からっ': 4737, '先考': 4738, 'いち': 4739, 'タックル': 4740, 'クリップ': 4741, '書ける': 4742, '調整': 4743, 'karq': 4744, '待ち': 4745, 'ツイッチプライム': 4746, '登録': 4747, 'Delave': 4748, '不安定': 4749, 'おすすめ': 4750, 'しません': 4751, '糞': 4752, '実況': 4753, '百害あって一利なし': 4754, '勘弁': 4755, 'ワールドカップ': 4756, '覚えりゃ': 4757, 'China': 4758, 'イギリス': 4759, 'スウェーデン': 4760, 'オープンマイク': 4761, '鼻歌': 4762, '歌っ': 4763, 'ソンブラシンメマジ': 4764, '欄': 4765, '承認': 4766, '持ち主': 4767, '素早く': 4768, '消える': 4769, 'あたっ': 4770, '築': 4771, 'めちゃめちゃ': 4772, '揺れ': 4773, '喜ぶ': 4774, '一定': 4775, '課題': 4776, '本気': 4777, '受け取る': 4778, '決済': 4779, 'ペース': 4780, '有志': 4781, 'Web': 4782, '安く': 4783, 'ボランティア': 4784, 'につき': 4785, '負担': 4786, 'フル': 4787, 'NDA': 4788, 'はじめ': 4789, 'フィルター': 4790, '激減': 4791, 'つぶやく': 4792, '海外展開': 4793, '富裕層': 4794, 'ぜひ': 4795, '売れ': 4796, 'とどく': 4797, '廉価版': 4798, 'マルチ': 4799, '勧誘': 4800, '視線': 4801, '疲労': 4802, '食生活': 4803, 'pandas': 4804, '芸当': 4805, '熟睡': 4806, 'トレ': 4807, 'ベンチ': 4808, 'ジム': 4809, 'びびっ': 4810, 'プッシュアップバー': 4811, 'ポチっ': 4812, 'スマート': 4813, '根性': 4814, '乗り切る': 4815, 'googleアラート': 4816, 'がめ': 4817, '一文字': 4818, 'ライター': 4819, 'あろう': 4820, 'オリジナリティ': 4821, 'かけら': 4822, '真似': 4823, '語尾': 4824, '虚無': 4825, 'LoL': 4826, 'スマホゲー': 4827, 'スマホ': 4828, '打ち合わせ': 4829, 'ありとあらゆる': 4830, 'ドメイン': 4831, '流通': 4832, '細分': 4833, 'OWWC': 4834, '接戦': 4835, 'オーストラリア代表': 4836, 'BLK': 4837, 'トリル': 4838, '大差': 4839, '英語圏': 4840, 'Baconjack': 4841, 'しかり': 4842, 'wiki': 4843, '回せ': 4844, 'サーバー管理者': 4845, 'よい': 4846, '出稿': 4847, '拡大': 4848, '回せる': 4849, '作りました': 4850, '食える': 4851, '博多ラーメン': 4852, '博多': 4853, '一双': 4854, '大砲ラーメン': 4855, '商売': 4856, '物寂しい': 4857, 'やはり': 4858, '定義': 4859, 'おはよう': 4860, 'ツイッチ': 4861, '滅多': 4862, 'ない層': 4863, '広め': 4864, 'LTV': 4865, 'タレント': 4866, 'マネジメント': 4867, 'なんとなく': 4868, 'トロールチート': 4869, '自由': 4870, 'chara': 4871, '生き': 4872, 'NRhokkaidou': 4873, 'nOrisa': 4874, 'change': 4875, 'キングスロウ': 4876, '部屋': 4877, '引き': 4878, 'こもっ': 4879, '説': 4880, '布教': 4881, '返事': 4882, 'メール': 4883, 'バフ': 4884, 'ぐらい': 4885, 'もんぱ': 4886, 'ぁ': 4887, '彼氏': 4888, 'やすかっ': 4889, '各': 4890, 'Dexo': 4891, 'ねる': 4892, '起床': 4893, '動画ネタ': 4894, 'フィンガー': 4895, 'チップ': 4896, '少数派': 4897, 'きち': 4898, '感度': 4899, '振り': 4900, '腕': 4901, '振り向き': 4902, '指先': 4903, '開始': 4904, 'ハッピー': 4905, '体毛': 4906, 'Fuel': 4907, 'かっこよ': 4908, 'RJM': 4909, 'Kirihito': 4910, 'シーズンプラチナフィニッシュ': 4911, 'まして': 4912, '射精': 4913, 'えーん': 4914, '注文': 4915, 'あん': 4916, '店員': 4917, 'ブチ': 4918, '合唱': 4919, 'ヴァーヴァー': 4920, 'カナダ': 4921, 'マズ': 4922, '情報ソース': 4923, '辿っ': 4924, '抵抗': 4925, 'すっと': 4926, '感性': 4927, '食お': 4928, 'フランス領': 4929, '歴史': 4930, '合間': 4931, '街並み': 4932, 'フランス人': 4933, 'フランス': 4934, 'ハーフ': 4935, 'アメリカ人': 4936, 'マレーシア': 4937, '英語力': 4938, 'DMM': 4939, '英会話': 4940, 'TOEIC': 4941, '上げよ': 4942, '話せ': 4943, '恥じ': 4944, '追い込ん': 4945, '全盛期': 4946, 'genji': 4947, 'FS': 4948, '跳ね返す': 4949, 'ぶつかっ': 4950, '代わり': 4951, 'なおかつ': 4952, '電撃': 4953, 'ぶつから': 4954, 'ビリビリ': 4955, '何とか': 4956, 'シーズン終了': 4957, 'たつ': 4958, 'gc': 4959, 'busan': 4960, 'カ国': 4961, '次に': 4962, 'ヨーロッパ': 4963, 'パスタ': 4964, '日本食': 4965, 'くい': 4966, 'テー': 4967, 'ズーーーーーット': 4968, 'DNN': 4969, '教師なし学習': 4970, 'CG': 4971, '知識': 4972, '人工知能': 4973, '取り組め': 4974, '塊': 4975, '野良': 4976, '恐ろしい': 4977, '統率力': 4978, 'ヒラタン': 4979, '始める': 4980, '芯': 4981, '点': 4982, '一貫': 4983, 'ネガティブ': 4984, 'なくなる': 4985, '実験': 4986, 'なんj': 4987, '迷言': 4988, 'ほんと': 4989, '版': 4990, 'すいません': 4991, '筋肉': 4992, '回り': 4993, '0秒間': 4994, '転': 4995, '回転': 4996, 'フレームレート': 4997, 'fps': 4998, '高速': 4999, '実質': 5000, '疑似': 5001, '前後': 5002, '張っ': 5003, 'プロジェクタイル': 5004, '方位': 5005, '防げる': 5006, 'トルネード': 5007, '判定': 5008, '間': 5009, '周囲': 5010, '遊び': 5011, 'gs': 5012, 'r': 5013, '募': 5014, 'n0': 5015, '心なし': 5016, '九州': 5017, '関東': 5018, '呼ぶ': 5019, '自己肯定感': 5020, 'ルックス': 5021, 'こだわら': 5022, 'トゥトゥトゥトゥウィッティ': 5023, 'ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ': 5024, '稼働': 5025, '働か': 5026, '規則': 5027, '羅列': 5028, '眠い': 5029, '集中力': 5030, 'をもって': 5031, 'こなせ': 5032, '直前': 5033, 'ストレス耐性': 5034, '人格的': 5035, '思いやり': 5036, '精神的支柱': 5037, 'ゲーミングデバイス': 5038, 'こだわる': 5039, '受験勉強': 5040, 'こだわっ': 5041, 'いただけ': 5042, 'そのため': 5043, 'つかめる': 5044, 'フェティシズム': 5045, '凍ら': 5046, '蝶': 5047, '標本': 5048, '係り': 5049, 'WhatEver': 5050, '出来る': 5051, '主': 5052, '練': 5053, '高める': 5054, '頻度': 5055, 'ご': 5056, 'nRT': 5057, 'いただける': 5058, '皇帝': 5059, 'マネージャー': 5060, '人出': 5061, 'すっ': 5062, '選択肢': 5063, 'ログイン': 5064, '待ち時間': 5065, 'どなた': 5066, '今シーズン': 5067, '行き来': 5068, '期': 5069, '評論家': 5070, '墓': 5071, 'AmazonPrime': 5072, '結びつけ': 5073, 'おま国': 5074, '指': 5075, 'チョチョっと': 5076, '動かせる': 5077, '接触': 5078, '複雑': 5079, '種類': 5080, '提示': 5081, '凄い': 5082, 'ドルクエ': 5083, 'かわいく': 5084, 'ファンタジー': 5085, '王道': 5086, '存在感': 5087, 'ゴールデンタイム': 5088, 'モバイルワイファイルーター': 5089, '格安sim': 5090, '刺し': 5091, '携帯': 5092, 'LTE': 5093, 'ping': 5094, '向い': 5095, '容量': 5096, 'テザリング': 5097, '他社': 5098, 'WiMAX': 5099, '宣伝': 5100, 'ステマ': 5101, '汚染': 5102, 'ポケットワイファイ': 5103, 'ひど': 5104, 'ポケットルーター': 5105, 'ワイファイ': 5106, '打ち合い': 5107, '打て': 5108, 'ラグ': 5109, '人柱': 5110, 'オワ': 5111, '指南': 5112, '講座': 5113, 'オワチッチ': 5114, '故': 5115, 'ゾエルニキ': 5116, 'エッチ': 5117, 'そりゃあ': 5118, '杉内': 5119, '年生': 5120, '修士': 5121, '補完': 5122, 'ガチサウナ': 5123, 'ザコ': 5124, 'よって': 5125, 'どうも': 5126, 'ワンヒーラー': 5127, 'あみ': 5128, 'だむ': 5129, '求む': 5130, '不動産': 5131, '自営': 5132, '雇わ': 5133, '限度': 5134, '雇っ': 5135, 'うなぎ': 5136, '寿司': 5137, '海外旅行': 5138, '遊ん': 5139, 'たな': 5140, 'もちろん': 5141, '要するに': 5142, '落とし込み': 5143, '思いつく': 5144, '手先': 5145, 'パイ': 5146, '狭まっ': 5147, '頼ら': 5148, '傘': 5149, 'やよい軒': 5150, '最速': 5151, '平成最後': 5152, '顔だし': 5153, 'オフイベ': 5154, 'オフライン': 5155, 'ダイレクトマーケティング': 5156, 'レア': 5157, 'あるかな': 5158, '飲み': 5159, '弊': 5160, 'びっくり': 5161, '未': 5162, '初見': 5163, '確かめ': 5164, '共有': 5165, 'テスト': 5166, '付き合っ': 5167, '方い': 5168, '接続': 5169, '丸々': 5170, '単位': 5171, '直近': 5172, 'google': 5173, 'analytics': 5174, 'Photoshop': 5175, '問題解決': 5176, 'ル': 5177, 'しながら': 5178, 'シームレス': 5179, 'ヌンバーニ': 5180, '階段': 5181, '登っ': 5182, '盾': 5183, '前提': 5184, 'トレソル': 5185, '押し切れ': 5186, 'Loccat': 5187, 'Kone': 5188, 'Pure': 5189, 'Logi': 5190, 'ヘッドセット': 5191, 'Zowie': 5192, 'マウスバンジーポチ': 5193, 'アバラ': 5194, '格好': 5195, 'トーク': 5196, 'ホスト': 5197, 'mori': 5198, '森さん': 5199, 'teen': 5200, 'GTX': 5201, 'Ti': 5202, 'SLM': 5203, 'つない': 5204, 'カスタム': 5205, '転売': 5206, 'ちゃっ': 5207, '新卒': 5208, '初任': 5209, '給': 5210, '越え': 5211, 'アメリカアマゾン': 5212, '個人輸入': 5213, '転送': 5214, '仕入れ': 5215, '稼げる': 5216, 'リア垢': 5217, 'に関し': 5218, '稼が': 5219, '勝ち負け': 5220, 'なるか': 5221, 'わか': 5222, 'みっき': 5223, 'Envy': 5224, '0D': 5225, 'PS': 5226, '世界中': 5227, '強いっ': 5228, '遊戯王': 5229, 'レアカード': 5230, 'エフェクトザリア': 5231, '人気者': 5232, '流石に': 5233, '飽きる': 5234, 'ボット': 5235, 'テレポート': 5236, 'プロパイダー': 5237, '選べ': 5238, 'おも': 5239, '解決策': 5240, '長かっ': 5241, 'うんこ製造機': 5242, '憑かれ': 5243, '模試': 5244, '熱中': 5245, '学業': 5246, '専念': 5247, '今頃': 5248, '再来年': 5249, '目指す': 5250, '浪人生': 5251, '多浪': 5252, 'オバッチ': 5253, 'めたん': 5254, '❔': 5255, '睡眠時間': 5256, '日本語版': 5257, '散在': 5258, 'アーカイブス': 5259, '照らし': 5260, '総合': 5261, 'ぼやっと': 5262, '関わっ': 5263, 'づついろんな': 5264, 'Mac': 5265, '相性': 5266, '悪': 5267, 'クレア': 5268, 'できん': 5269, 'まらん': 5270, '戦記': 5271, '読も': 5272, '何もかも': 5273, '実例': 5274, 'できないよ': 5275, 'ラグランジュ': 5276, '未定': 5277, '乗数': 5278, '習っ': 5279, '実用': 5280, '感慨深い': 5281, '常識': 5282, '既存': 5283, '真似れ': 5284, '削ら': 5285, 'ヤフオク': 5286, '出品': 5287, 'ユーロ': 5288, 'たかい': 5289, '絡ん': 5290, '評判': 5291, '支障': 5292, '切り替える': 5293, 'ファイブ': 5294, 'JCG': 5295, '決勝': 5296, '見ん': 5297, 'ゲーミングハウス': 5298, 'サラッと': 5299, 'いかつ': 5300, '震える': 5301, 'tweetdeck': 5302, '予約': 5303, 'pm': 5304, 'やる気': 5305, 'まち': 5306, 'パッチ': 5307, '改変': 5308, '見つから': 5309, '動かす': 5310, 'チンパンジーゲー': 5311, '幸せ': 5312, 'ウンタラカンタラ': 5313, '面倒': 5314, 'COD': 5315, '撃ち殺す': 5316, 'ツイッターアカウント': 5317, 'BO': 5318, '期間': 5319, 'お祭り': 5320, '穏やか': 5321, '幻想': 5322, '突き止め': 5323, '仕掛け': 5324, '雨': 5325, 'けん': 5326, 'サッサ': 5327, 'K': 5328, 'グループb': 5329, 'ホッグ': 5330, '0回戦': 5331, '一位': 5332, '絶望的': 5333, 'ミロポ': 5334, '乗れる': 5335, 'デマ': 5336, 'デマ情報': 5337, '指定': 5338, '乗れ': 5339, 'ミロポジ': 5340, '乗り': 5341, 'コツ': 5342, 'ベストアンサー': 5343, 'バカゲー': 5344, 'ゴミゲー': 5345, '乗っ': 5346, '撮り': 5347, '手伝っ': 5348, 'エリア': 5349, '気持': 5350, '分かっ': 5351, '雑': 5352, '短時間': 5353, '深く': 5354, 'nXQ': 5355, 'なげ': 5356, '学べる': 5357, 'コンセプト': 5358, '狙い': 5359, '読み取る': 5360, 'しも': 5361, '解説動画': 5362, '基礎': 5363, '平然と': 5364, '不快': 5365, '要項': 5366, '貸し': 5367, 'しらん': 5368, '持ち帰る': 5369, 'イマイチ': 5370, 'za': 5371, '性格': 5372, 'S0': 5373, '一筋': 5374, '銀': 5375, '枠': 5376, 'プレースタイル': 5377, 'ちょくちょく': 5378, '六': 5379, 'ログ': 5380, '炊い': 5381, 'クリティカルヒット': 5382, 'ちょい': 5383, 'あいつ': 5384, '一体': 5385, 'コリアン': 5386, '0p': 5387, 't': 5388, '捗る': 5389, '矢': 5390, 'チン': 5391, 'ブー': 5392, '組ん': 5393, 'FU': 5394, 'CCC': 5395, 'CCCCCCCCCCCCCCCCCCCCCCCCK': 5396, 'とうとう': 5397, 'サ': 5398, 'さっき': 5399, '自前': 5400, 'スピーカー': 5401, '音楽': 5402, '流し': 5403, 'ウェイ': 5404, '人組': 5405, '一気に': 5406, '見識': 5407, 'ディナー': 5408, '食う': 5409, '吉野家': 5410, '励まさ': 5411, '配達': 5412, '受け取れ': 5413, 'なんとか': 5414, '新宿駅': 5415, '徒歩': 5416, '分の': 5417, 'SF0': 5418, '電車': 5419, '0年前': 5420, 'お話': 5421, 'いただい': 5422, '含蓄': 5423, '協賛': 5424, '自社': 5425, 'GAFA': 5426, '追いつけ': 5427, '投入': 5428, '人口': 5429, '番手': 5430, 'アップサイド': 5431, '小さ': 5432, 'PFN': 5433, '特化': 5434, '朝定食': 5435, 'エニタイム': 5436, 'マイブーム': 5437, 'アパート': 5438, 'MB': 5439, 'Legends': 5440, '幸運': 5441, '惹か': 5442, '0m': 5443, 'bs': 5444, '再インストール': 5445, 'p0p': 5446, 'ぐ': 5447, 'fk': 5448, 'あき': 5449, '乗り越える': 5450, '拳': 5451, '心地よく': 5452, '周波数': 5453, '仕掛ける': 5454, '移動': 5455, 'スタッツ': 5456, 'ランクマクソコンテンツ': 5457, 'live': 5458, '見やすい': 5459, 'a': 5460, 'スタヌ': 5461, '辞め': 5462, 'DTN': 5463, 'ドイツ': 5464, '極めよ': 5465, '舞台': 5466, 'どころか': 5467, '皮肉': 5468, '律': 5469, '泣ける': 5470, '自陣': 5471, '押し出す': 5472, 'マーシーウル': 5473, '辛': 5474, '久': 5475, '々': 5476, '高橋': 5477, 'ゲーミングメンバー': 5478, 'キーボード': 5479, '小さい': 5480, '左側': 5481, '振り向く': 5482, 'ガ': 5483, 'ツン': 5484, 'ぶつかる': 5485, 'DM': 5486, 'たい動': 5487, '経営者': 5488, '仮想敵': 5489, '大好きだよ': 5490, 'さっさと': 5491, '永': 5492, '制裁': 5493, '下り': 5494, '手足': 5495, '口': 5496, '落下': 5497, 'ｿﾝﾌﾞﾗ': 5498, '即死': 5499, '病': 5500, 'つまらな': 5501, 'れす': 5502, 'たまっ': 5503, 'サブヒーラー': 5504, 'ホットスナック': 5505, '数量': 5506, '引き抜い': 5507, '界': 5508, '読売巨人軍': 5509, '金持ち': 5510, '引き抜き': 5511, '噂': 5512, 'リアルフォース': 5513, 'キートップ': 5514, '掃除': 5515, '壊れる': 5516, '短い': 5517, '訴訟': 5518, '運営方針': 5519, 'dis': 5520, '発言内容': 5521, '否定': 5522, '焦燥感': 5523, 'ドリブン': 5524, '日々': 5525, 'ぶり': 5526, 'ぼつ': 5527, 'プロスト': 5528, 'リーマー': 5529, '帰国': 5530, 'iphone': 5531, 'アニモジ': 5532, '劇': 5533, 'エモ': 5534, '上の': 5535, 'そっ': 5536, '頑張り': 5537, '所': 5538, '変動': 5539, '統計的': 5540, '収束': 5541, '被験者': 5542, 'さあ': 5543, 'jesl': 5544, 'ふふ': 5545, '全額': 5546, 'ありがたい': 5547, '陽気': 5548, 'バス': 5549, '逃し': 5550, 'ビール': 5551, 'ドイツ語': 5552, '話しかけ': 5553, 'ドイツ人': 5554, 'ベー': 5555, 'ピザ': 5556, 'ソーセージ': 5557, '肥満': 5558, '食文化': 5559, '食べ': 5560, 'フリックエイム': 5561, '使': 5562, 'かったん': 5563, '果たして': 5564, 'バレる': 5565, 'と腹': 5566, 'オーケー': 5567, 'ワキヤン': 5568, '風土': 5569, '物価': 5570, 'XP': 5571, '壁紙': 5572, '景色': 5573, '城': 5574, '誹謗中傷': 5575, '体制': 5576, 'コーラ': 5577, 'ストロー': 5578, 'ひっくり返し': 5579, '荷物': 5580, 'くれよ': 5581, '乗り越えよ': 5582, '学会': 5583, '進ま': 5584, '出張': 5585, 'オーストリア': 5586, '弱けれ': 5587, 'しそう': 5588, '落ち着い': 5589, '半端': 5590, '上下関係': 5591, '疑問': 5592, 'アナリスト': 5593, '不問': 5594, '思いつか': 5595, 'いてる': 5596, '連続': 5597, 'てきが': 5598, 'ーホッグ': 5599, 'ほっ': 5600, 'ウィンストンガイジ': 5601, 'える': 5602, '初': 5603, '効か': 5604, '徹底的': 5605, '払う': 5606, 'ジャンク品': 5607, '新しく': 5608, '直す': 5609, 'realforce': 5610, '故障': 5611, 'ぐぐっ': 5612, '修理': 5613, '東プレ': 5614, '直し': 5615, '段': 5616, '法っ': 5617, 'タイモウ': 5618, 'アンケート': 5619, 'シュール': 5620, '素直': 5621, '表し': 5622, '吐き': 5623, '好感': 5624, '持てる': 5625, 'どんだけ': 5626, 'ファイト': 5627, '厳禁': 5628, '世の中': 5629, '競争率': 5630, '参入障壁': 5631, 'たとえ': 5632, '席': 5633, '奪い合う': 5634, '到達': 5635, 'アジアン': 5636, 'だれか': 5637, '見やすく': 5638, 'くれー': 5639, '本質的': 5640, '成熟': 5641, '市場': 5642, '突っ込む': 5643, '厳し': 5644, 'POV': 5645, '移さ': 5646, '東北': 5647, '狙わ': 5648, 'benymd': 5649, 'ff': 5650, '星': 5651, '正': 5652, '少なくとも': 5653, '細かく': 5654, '大きく': 5655, '運動神経': 5656, '未だに': 5657, 'QCK': 5658, '滑り': 5659, '滑らか': 5660, '減点': 5661, '見習っ': 5662, 'FAZE': 5663, 'アイヘン': 5664, 'トータルメイヘム': 5665, 'プロゲンジ': 5666, 'University': 5667, '放題': 5668, 'ワンパン': 5669, '突っ込ま': 5670, '再来月': 5671, '来週': 5672, 'びみょ': 5673, 'うだっ': 5674, '趣旨': 5675, '載せ': 5676, '前もって': 5677, 'ハテブ': 5678, '番目': 5679, '有名人': 5680, 'アマチュア時代': 5681, 'お勧め': 5682, '引用': 5683, 'アビューズ': 5684, '上手': 5685, '落とし込める': 5686, '具体': 5687, '大河': 5688, 'お台場': 5689, '暮らす': 5690, '済む': 5691, '薬': 5692, '飲め': 5693, '成分': 5694, 'あー': 5695, 'ろ': 5696, 'みや': 5697, 'ガーディアンエンジェル': 5698, 'ターゲット': 5699, '加わっ': 5700, '近づい': 5701, 'キリングエンジェル': 5702, 'ほしかっ': 5703, 'Uber': 5704, '大学院': 5705, '最先端': 5706, '多かっ': 5707, '生む': 5708, '自動運転': 5709, '過渡期': 5710, '換算': 5711, '目と': 5712, '単純労働': 5713, '画像解析': 5714, '代わら': 5715, 'コモディティ': 5716, 'Airbnn': 5717, '常時': 5718, '繋がり': 5719, '非': 5720, 'タクシードライバー': 5721, '築く': 5722, 'ロサンゼルス': 5723, 'ゲームメーカー': 5724, '本社': 5725, '衝撃': 5726, 'ハーバード': 5727, '基本的': 5728, '返済': 5729, '不要': 5730, '初年度': 5731, '上手けれ': 5732, 'タダ': 5733, '夢': 5734, '施設見学': 5735, '博士': 5736, '持ち': 5737, '創業': 5738, 'ゴリ': 5739, 'テック': 5740, 'ネカフェ': 5741, 'コンシューマーゲー': 5742, 'オンラインゲーム': 5743, '産業振興': 5744, '開く': 5745, '国民': 5746, 'エンタメ': 5747, '福祉': 5748, '差し置い': 5749, '驚く': 5750, 'イベンター': 5751, '継続': 5752, '流出': 5753, 'どちら': 5754, '支社': 5755, '外資': 5756, 'がよく': 5757, 'やりがい': 5758, '輝く': 5759, 'ヤベートコ': 5760, '忘れ': 5761, 'リザレク': 5762, 'chinamin': 5763, '走り': 5764, 'お山の大将': 5765, '自信満々': 5766, '強み': 5767, '人権': 5768, '上場企業': 5769, 'パルスボム': 5770, '去': 5771, '釈迦': 5772, 'ホモ': 5773, 'イケボ': 5774, '兄さん': 5775, 'macbookpro': 5776, 'bp': 5777, '薄い': 5778, 'しっかり': 5779, 'ユーチューブ': 5780, '応用': 5781, 'ユーチューバー': 5782, 'ネットリテラシー': 5783, '学べ': 5784, '描き': 5785, 'たし前': 5786, 'wikipedia': 5787, '女声': 5788, 'ESL': 5789, '体型': 5790, '研究者': 5791, '理系': 5792, 'オタサーの姫': 5793, '嫌味': 5794, '演出': 5795, 'さとし': 5796, 'もち': 5797, 'ばけん': 5798, 'ま': 5799, '減少': 5800, 'きつかっ': 5801, '発狂': 5802, 'ポジショントーク': 5803, '理念': 5804, 'そうじゃない': 5805, 'U0': 5806, '余っ': 5807, 'おっさん化': 5808, 'bor': 5809, '気力': 5810, 'おき': 5811, 'oops': 5812, 'ミュートワード': 5813, 'rpg': 5814, 'プレゼント': 5815, '抽選': 5816, 'にやけ': 5817, 'aprx': 5818, '早期': 5819, 'ひっくり返る': 5820, 'もろ': 5821, 'MVPspace': 5822, '這う': 5823, 'スクリプト': 5824, '組': 5825, 'ホント': 5826, '話し合っ': 5827, '奨励': 5828, '重大': 5829, '欠陥': 5830, 'トリーサ': 5831, 'おり': 5832, '単体': 5833, 'ボックス': 5834, 'かいし': 5835, 'しほん': 5836, 'ゲーミング': 5837, '0年ぶり': 5838, '冷静': 5839, 'コメ': 5840, '現れ': 5841, '目立つ': 5842, '離れる': 5843, 'コメ欄': 5844, 'クソワロタ': 5845, 'MVP': 5846, 'SPACE': 5847, 'ルナハイ': 5848, '二次創作': 5849, '権利': 5850, '違反': 5851, 'リュジェホン': 5852, '指揮系統': 5853, 'つながっ': 5854, '連動': 5855, 'もうい': 5856, 'ろいろ': 5857, 'まんま': 5858, '数式': 5859, '論理': 5860, 'フーリエ変換': 5861, '光学': 5862, '工学': 5863, '幾何学': 5864, '電気': 5865, '欲しかっ': 5866, '劫火': 5867, '経典': 5868, 'ドウシテコウナッタ': 5869, '懲役0年': 5870, '返し': 5871, 'だけど': 5872, '自分のために': 5873, '言えないよ': 5874, '人材不足': 5875, '込ん': 5876, '言える': 5877, 'はたして': 5878, 'ジェットストリームアタック': 5879, '検索エンジン': 5880, '引っかかる': 5881, '伸びる': 5882, '旦那': 5883, 'HAHA': 5884, '変わん': 5885, '無表情': 5886, '吐き気': 5887, '位置づける': 5888, '結びつか': 5889, '将来': 5890, '捉える': 5891, '湧い': 5892, '結びつく': 5893, '番': 5894, 'wtf': 5895, '望遠鏡': 5896, 'ルナコロ': 5897, '休まら': 5898, '大きい': 5899, '清水': 5900, 'bacon': 5901, 'jack': 5902, 'owec': 5903, 'ここら': 5904, '辺': 5905, 'くらっ': 5906, 'ばいいん': 5907, 'バスティオンラインハルト': 5908, '対処法': 5909, 'セット': 5910, '作れれ': 5911, '的外れ': 5912, '捉え': 5913, '然': 5914, 'PT': 5915, 'なんとも': 5916, 'すごいっ': 5917, 'くるし': 5918, 'チーター': 5919, '囲い': 5920, '立てて': 5921, '不手際': 5922, 'コメントアレ': 5923, 'るん': 5924, 'birdring': 5925, '超イケメン': 5926, 'エアリアル': 5927, 'バルサ': 5928, 'スタメン': 5929, 'ベタ': 5930, 'ミン': 5931, '読み方': 5932, 'ドラクエ0': 5933, 'マルティナ': 5934, '可': 5935, '愛す': 5936, 'ぎんか': 5937, 'カーブ': 5938, 'ごろ': 5939, 'FIFA': 5940, '軌道': 5941, 'シュート': 5942, 'ぜみ': 5943, 'pc': 5944, '組み立': 5945, '初期不良': 5946, '組み上げ': 5947, 'モデル': 5948, '達人': 5949, 'エーリアンウェア': 5950, '見づらく': 5951, '差し替え': 5952, 'ブラスク': 5953, 'CS': 5954, 'O0': 5955, 'ブログネタ': 5956, 'スコア': 5957, 'ワンちゃん': 5958, 'キルアシスト': 5959, 'どい': 5960, 'かれる': 5961, 'フォーラム': 5962, '書き込む': 5963, '蹴ら': 5964, 'サレンダー': 5965, 'スナイパー': 5966, '片方': 5967, '用': 5968, '源氏': 5969, 'ズンバ': 5970, '両方': 5971, '成立': 5972, '塞い': 5973, '掴み': 5974, '安定性': 5975, '左右': 5976, 'おk': 5977, 'ミラティブ': 5978, '入室': 5979, 'nTwitch': 5980, '比べ': 5981, '加速': 5982, '重視': 5983, '文脈': 5984, 'たい人': 5985, '満足感': 5986, '含む': 5987, '形式': 5988, 'スムーズ': 5989, '利する': 5990, 'ズバッと': 5991, '言い切っ': 5992, '問題点': 5993, '洗い出し': 5994, '改善': 5995, '洗い出す': 5996, '語れる': 5997, '電子機器': 5998, '語ら': 5999, '長時間': 6000, '守れ': 6001, '損益分岐点': 6002, 'nYoutube': 6003, 'において': 6004, '可能性': 6005, 'マネタイズ': 6006, '明文化': 6007, '事務所': 6008, 'シンプル': 6009, '参入': 6010, '言語': 6011, '政府': 6012, '人件費': 6013, '削減': 6014, '障害': 6015, 'プロジェクト': 6016, '名付け': 6017, 'ざっと': 6018, 'た感': 6019, 'ハローワーク': 6020, 'デバッグ': 6021, 'おもえ': 6022, 'フラワー': 6023, 'ひねくれ': 6024, 'jcg': 6025, '人少': 6026, 'ハーモニクス': 6027, '何回': 6028, 'チームワーク': 6029, '荒れる': 6030, 'デュームフィスト': 6031, '崩壊': 6032, 'リス': 6033, 'ハメ': 6034, '攻メ': 6035, 'オーストラリア': 6036, 'ダブルスナイパー': 6037, '少なかっ': 6038, '虐殺': 6039, 'ショー': 6040, '韓国代表': 6041, 'オランダ': 6042, 'ポーランド': 6043, 'Twoeasy': 6044, 'オーバー': 6045, '振り向け': 6046, 'dhu': 6047, 'dolu': 6048, 'dwu': 6049, 'ndwu': 6050, 'ームフィスト': 6051, '小': 6052, 'ギリ': 6053, '届か': 6054, '丁度': 6055, '届く': 6056, 'かしいかえん': 6057, '目安': 6058, '−': 6059, '集まれ': 6060, '気楽': 6061, '揺れる': 6062, 'AIM': 6063, 'うっと': 6064, 'おしい': 6065, 'エンジョイスクリムゲーマーズクラン': 6066, 'g': 6067, 'ベンチマーク': 6068, '最適化': 6069, '大した': 6070, 'AMD': 6071, 'マザーボード': 6072, 'GPU': 6073, '買い換える': 6074, '決まり': 6075, 'Intell': 6076, 'ゆれ': 6077, 'すぎや': 6078, '非公開': 6079, 'リスト': 6080, 'おもんない': 6081, '連鎖的': 6082, '共著': 6083, '国際': 6084, '通っ': 6085, 'シックス': 6086, 'モノマネ': 6087, '浮かし': 6088, 'やり方': 6089, '肘': 6090, 'でかす': 6091, 'みよ': 6092, 'gg': 6093, '半減': 6094, 'タクティカルバイザー': 6095, 'アナルシオ': 6096, '打ち勝と': 6097, 'envy': 6098, 'AP': 6099, 'EX': 6100, 'ｗｗｗｗｗｗｗｗｗｗ': 6101, 'B': 6102, 'スプラ': 6103, 'ちょろっと': 6104, 'Splatoon': 6105, '塗っ': 6106, 'ディープラーニング': 6107, '回路': 6108, '事象': 6109, 'ラベリング': 6110, '全自動': 6111, 'イヤホン': 6112, 'なくす': 6113, 'い説': 6114, '部': 6115, 'イ': 6116, 'グラボ': 6117, '乗': 6118, 'エイムアシストマックス': 6119, '見渡せ': 6120, 'エイムアシストバリバリ': 6121, '遅': 6122, '反撃': 6123, 'フラバン': 6124, '溜まり': 6125, '好評': 6126, 'にて': 6127, 'wordpress': 6128, 'gif': 6129, '挿入': 6130, '貼り': 6131, '読み込み': 6132, '遅く': 6133, '原理': 6134, '読み込む': 6135, '情報量': 6136, 'うい': 6137, '堂': 6138, 'ハリー': 6139, 'まとめ記事': 6140, '凄いっ': 6141, 'すね': 6142, '駅': 6143, 'バナナ': 6144, 'ジュース': 6145, '一人暮らし': 6146, 'ふと': 6147, '食べる': 6148, 'ーエモーショナル': 6149, 'エブリデイ': 6150, 'ミーティング': 6151, '遅刻': 6152, '絵師': 6153, '描く': 6154, '乳首': 6155, 'uDDFE': 6156, 'こうっ': 6157, '人たち': 6158, '相手チーム': 6159, 'moba': 6160, 'やらし': 6161, '散々': 6162, '日本勢': 6163, 'プレーオフ': 6164, '食い下がっ': 6165, '嬉しかっ': 6166, '中洲': 6167, '日常': 6168, '光景': 6169, '取り返し': 6170, 'ウィンストントレゲンノ': 6171, 'god': 6172, 'claire': 6173, 'Aetar': 6174, '坂': 6175, 'ペイ': 6176, 'へん': 6177, '国': 6178, 'ぇべ': 6179, '再開': 6180, 'からかね': 6181, 'アツフォーカスヤバ': 6182, 'ジャスパー': 6183, 'trill': 6184, 'インタビュアー': 6185, 'マリクフォルテ': 6186, 'フラッシュウルブズメイン': 6187, '当てる': 6188, 'マクリーウルト': 6189, '溜まる': 6190, 'deadeye': 6191, 'Another': 6192, 'タイ': 6193, 'モウ': 6194, 'タイモウマクリー': 6195, '神龍': 6196, '撃剣': 6197, 'タイミングリーパー': 6198, 'レイス': 6199, 'ちょうど': 6200, 'スタンスミス': 6201, 'NiP': 6202, 'ペイロード': 6203, 'ミスターグッドエイム': 6204, '正味': 6205, '姿': 6206, 'パーツ': 6207, '検討': 6208, '美し': 6209, '問う': 6210, 'しん': 6211, 'ぺー': 6212, 'お話し': 6213, '哲学': 6214, '具現化': 6215, '著': 6216, '実に': 6217, '年代': 6218, '関わり': 6219, '中心': 6220, '同': 6221, '世代': 6222, 'グロース': 6223, 'ゆるふわ': 6224, '座談会': 6225, 'メガネ': 6226, 'タッチペン': 6227, '写す': 6228, 'ソフト': 6229, 'nDiscord': 6230, '筑波': 6231, '通過': 6232, 'good': 6233, 'きそう': 6234, 'altm': 6235, '帰ろ': 6236, '恋しい': 6237, '代表選': 6238, 'ほんとに': 6239, '正念場': 6240, 'フィンランド': 6241, '抜ける': 6242, 'とっても': 6243, '同率': 6244, '直接対決': 6245, 'ベトナム': 6246, 'スペイン': 6247, '中西': 6248, 'みき': 6249, 'ちゃん': 6250, 'いちいち': 6251, '値段': 6252, '問い合わせ': 6253, '二度手間': 6254, 'よず': 6255, '慣れ': 6256, '異国': 6257, '地': 6258, '疲弊': 6259, 'リフ': 6260, '潰す': 6261, 'ハリフ': 6262, 'スター': 6263, 'ベビーディーバ': 6264, 'ナノ': 6265, 'ぶつけ': 6266, '結果的': 6267, 'わー': 6268, 'いこ': 6269, 'ハリーフックソルジャー': 6270, 'あらら': 6271, 'Aktm': 6272, 'マクリーチート': 6273, 'チームメイト': 6274, '国なん': 6275, 'だい': 6276, 'りてん': 6277, 'JPWIN': 6278, 'うめー': 6279, 'ジャパン': 6280, 'ばれー': 6281, 'ぐながらぶりんくしてるけど': 6282, 'スイッチ': 6283, '希望小売価格': 6284, 'アマゾン': 6285, '汚': 6286, 'ハイセンシ': 6287, '繊細': 6288, 'いづ': 6289, 'ゾエル': 6290, '相変わらず': 6291, '早稲田': 6292, '卒': 6293, '基づく': 6294, '論理展開': 6295, '魔境': 6296, '語っ': 6297, 'らっしゃる': 6298, 'ペンギン': 6299, '率いる': 6300, '民': 6301, '額': 6302, 'チー': 6303, '入ろう': 6304, '月日': 6305, 'きり': 6306, 'ひと': 6307, '布団': 6308, 'カメムシ': 6309, '見かける': 6310, '負荷': 6311, '長期間': 6312, '持続': 6313, '至上主義': 6314, '削っ': 6315, 'いわゆる': 6316, 'IT系': 6317, '気合': 6318, '余計': 6319, 'こなせる': 6320, 'フルタイム': 6321, 'DTNG': 6322, '回戦': 6323, 'sf0': 6324, 'ステージ': 6325, '幼少期': 6326, 'ゲーム機': 6327, '娯楽': 6328, 'サムシング': 6329, 'あああああ': 6330, 'フルスクラッチ': 6331, '行列': 6332, 'おけ': 6333, '後悔': 6334, 'くぅー': 6335, '殆ど': 6336, '戦術': 6337, '求人': 6338, '任三郎': 6339, 'ういい': 6340, '無敵': 6341, '解け': 6342, '動け': 6343, '呼び方': 6344, '正し': 6345, '寝よ': 6346, '取り戻そ': 6347, 'リア友': 6348, 'ぅぅ': 6349, 'ぅ': 6350, '見よ': 6351, 'イヤホンジャック': 6352, 'ビジネス街': 6353, 'いつき': 6354, '混ん': 6355, '開き': 6356, '何故': 6357, '0d': 6358, 'ps': 6359, 'ハンドガン': 6360, 'W杯': 6361, '人外': 6362, '登り': 6363, 'デンマーク': 6364, '司会': 6365, '気まず': 6366, 'エイムアシスト': 6367, '不自然': 6368, '不公平': 6369, '産ん': 6370, '無くし': 6371, 'なんだろう': 6372, '嫌悪感': 6373, 'コントローラー': 6374, '自由度': 6375, '補う': 6376, 'まう': 6377, 'さー': 6378, '小さく': 6379, 'シバターバリ': 6380, 'エンターテイナー': 6381, '油': 6382, 'プロレス': 6383, '構造': 6384, 'ハード': 6385, '敷居': 6386, 'インターネット上': 6387, '切り取ら': 6388, '生み出さ': 6389, '抜き取ら': 6390, 'vc': 6391, '降りる': 6392, 'ナイス': 6393, 'オチ': 6394, '向井': 6395, 'すまん': 6396, 'cross': 6397, 'modal': 6398, 'haptics': 6399, 'ツエー': 6400, 'オキュラスリフト': 6401, '売ら': 6402, 'オキュラス': 6403, '悩み': 6404, '都市': 6405, '買わ': 6406, '0億円': 6407, 'レッツワイズ': 6408, '叩きつける': 6409, '死にかけ': 6410, 'h0z0': 6411, 'ゲーマー': 6412, '定数': 6413, '奪い合い': 6414, '大義名分': 6415, '掲げ': 6416, '目線': 6417, '盛り上げよ': 6418, '要因': 6419, '送る': 6420, '遠征': 6421, 'しんどかっ': 6422, 'モニター': 6423, 'アーム': 6424, '迷っ': 6425, 'サッチャー': 6426, '名言': 6427, 'お金持ち': 6428, '貧乏': 6429, '貧乏人': 6430, '通じる': 6431, 'エモーショナル': 6432, 'くせ': 6433, 'エントリ': 6434, '名文': 6435, '嫉妬': 6436, '悪口': 6437, '無意味': 6438, 'スッと': 6439, '痛く': 6440, '進捗': 6441, 'ハースストーン': 6442, 'corento': 6443, '脱退': 6444, 'デト': 6445, '愚痴る': 6446, '愚痴っ': 6447, '毀損': 6448, '賠償金': 6449, 'デトネ': 6450, 'ロス': 6451, 'キス': 6452, 'きたす': 6453, '構築': 6454, '聖人': 6455, 'ごとき': 6456, 'キレる': 6457, 'ロルト': 6458, 'jeff': 6459, 'ズレ': 6460, 'どうしても': 6461, 'バイアス': 6462, '多数': 6463, 'ジェフ': 6464, 'ツイッター民': 6465, '上級': 6466, 'さえ': 6467, 'デベロッパー': 6468, 'ブラウザ': 6469, '視聴者': 6470, 'クラウド': 6471, 'テレビ': 6472, 'つなが': 6473, '遅延': 6474, '0K': 6475, 'つながる': 6476, '世界観': 6477, 'Stadia': 6478, '歓迎': 6479, '寝れ': 6480, 'dexo': 6481, '唐突': 6482, '心臓': 6483, '中学時代': 6484, '積み': 6485, '台': 6486, '軽く': 6487, 'PTR': 6488, 'ptr': 6489, 'デュー': 6490, 'む': 6491, 'フィスト': 6492, '負けず嫌い': 6493, 'ドゥームフィスト': 6494, 'doomfist': 6495, '速報': 6496, '書こ': 6497, 'プラン': 6498, '聞き取り': 6499, 'NELFD': 6500, '焦点': 6501, '追い詰め': 6502, 'マイナー': 6503, '事務作業': 6504, 'ゲーミングマウス': 6505, 'うすい': 6506, 'スルメ': 6507, 'スプレンダー': 6508, '日本版': 6509, 'GOSU': 6510, 'フィーリング': 6511, '除い': 6512, 'ダイブメタ': 6513, 'Fuck': 6514, 'renderrrrrrrrrr': 6515, '文字数': 6516, '多けれ': 6517, '凶悪': 6518, '古': 6519, '最新版': 6520, '未満': 6521, 'メイト': 6522, '話題': 6523, 'めんどくさい': 6524, 'ファボ': 6525, 'undertale': 6526, '雪だるま': 6527, 'cs': 6528, 'イケメン': 6529, 'コネ': 6530, 'ヤフー': 6531, '週休': 6532, '月間': 6533, '整え': 6534, '対し': 6535, 'つける': 6536, '無償': 6537, '嫌わ': 6538, '矛盾': 6539, 'これだけ': 6540, 'ねっ': 6541, 'zoel': 6542, '容姿': 6543, '捏造': 6544, 'バレ': 6545, 'ツイートパフォーマンス': 6546, '新社会人': 6547, '停止': 6548, 'Diablo': 6549, 'まさお': 6550, 'ドルディン': 6551, 'まさ': 6552, 'おどる': 6553, 'ディン': 6554, 'マイノリティ': 6555, '耳': 6556, '傾ける': 6557, 'マジョリティ': 6558, 'キャッチアップ': 6559, 'かけよ': 6560, 'といった': 6561, '項目': 6562, 'なにか': 6563, 'レイコー': 6564, '橋': 6565, 'ポン': 6566, '定石': 6567, '擬似': 6568, 'やれる': 6569, 'がっぽ': 6570, 'そや': 6571, 'せん': 6572, 'ステルスコーチ': 6573, '手腕': 6574, '拝見': 6575, '可愛かっ': 6576, 'GL': 6577, '交互': 6578, 'ざとやってんのかな': 6579, 'eac': 6580, 'CGB': 6581, 'ミスティック': 6582, 'わき': 6583, 'ラスカルジェスターニ': 6584, 'セブンス': 6585, '左前': 6586, '座っ': 6587, 'コンプレックス': 6588, 'つたない': 6589, '馬鹿': 6590, 'AOC': 6591, 'にこ': 6592, 'でか': 6593, 'ps0': 6594, 'スタヌー': 6595, 'あらし': 6596, 'あらわれ': 6597, '微分積分': 6598, '線形代数': 6599, '物理': 6600, 'ハンドガンボウガン': 6601, '湧き': 6602, 'レッドオーシャン': 6603, 'ブルーオーシャン': 6604, '計画': 6605, '織り込む': 6606, '計測': 6607, '困る': 6608, '正論': 6609, '間違っ': 6610, 'するどい': 6611, 'いつか': 6612, '弱まっ': 6613, 'か決': 6614, 'た方': 6615, '伝承': 6616, '追う': 6617, '後ブ': 6618, '割と': 6619, '樹脂': 6620, 'トンチンカン': 6621, '美しい': 6622, '対価': 6623, '不健全': 6624, '小銭': 6625, '乗せ': 6626, 'アフィカスアフィカス': 6627, '日本語字幕': 6628, '某氏': 6629, '金曜': 6630, 'ポケモン': 6631, 'スッキリ': 6632, '猛烈': 6633, 'ぃすられててたのしかった': 6634, '目立ち': 6635, '自尊心': 6636, 'したがり': 6637, '抱え': 6638, '猿': 6639, '典型例': 6640, 'ブラック': 6641, '国交省': 6642, '部署': 6643, 'delave': 6644, '悲しく': 6645, '永田町': 6646, 'じゃぶじゃぶ': 6647, '紹介': 6648, '侵害': 6649, '有る': 6650, '終バス': 6651, '弱体化': 6652, 'その他': 6653, 'てつまん': 6654, '読者': 6655, 'お客様': 6656, '飲み会': 6657, 'ふん': 6658, 'ラインハルトナーフ': 6659, 'きっ': 6660, 'かっこよく': 6661, 'ツッコミ': 6662, '流れる': 6663, '注目': 6664, '根幹': 6665, '人いれ': 6666, '日本語翻訳': 6667, '日本語訳': 6668, '付ける': 6669, 'ろか': 6670, 'グレー': 6671, 'スカイフル': 6672, '揃えろ': 6673, 'プラチナーマスター': 6674, 'しろっ': 6675, '同意': 6676, 'スカイ': 6677, 'USAOVERWATCH': 6678, 'てりゃ': 6679, '寺田心': 6680, '感情論': 6681, '平行線': 6682, '辿る': 6683, '可視': 6684, '探す': 6685, 'バオドゥーエンジン': 6686, 'DreamTeam': 6687, 'ソーシャル': 6688, '特': 6689, '不幸': 6690, 'では': 6691, '物': 6692, '報': 6693, '割れる': 6694, '進ん': 6695, 'ゲームコーチングサイト': 6696, 'adobe': 6697, '軽い': 6698, '教わり': 6699, '売買': 6700, '次第': 6701, 'エディタ': 6702, '体系': 6703, 'nUI': 6704, '入り口': 6705, '後進国': 6706, '後進': 6707, '投資ファンド': 6708, '追いつける': 6709, '推測': 6710, 'サムネイル': 6711, '偏重': 6712, '広告収入': 6713, '起因': 6714, 'サブスクモデル': 6715, '時計': 6716, '針': 6717, '先進国': 6718, 'タッグ': 6719, 'ビジネスモデル': 6720, '白紙': 6721, '投資額': 6722, '極める': 6723, '無くなっ': 6724, '合戦': 6725, 'しっくり': 6726, '捕捉': 6727, '湧く': 6728, '叩く': 6729, '風潮': 6730, 'ファーストペンギン': 6731, '血': 6732, '海': 6733, '飛び込ん': 6734, 'お絵描き': 6735, 'Ipad': 6736, '労力': 6737, 'aster': 6738, '過剰': 6739, '書き方': 6740, '国語': 6741, '書き手': 6742, '至ら': 6743, 'あいまっ': 6744, '賛否両論': 6745, '大炎上': 6746, '巻き起こし': 6747, '偉': 6748, '飛ばす': 6749, 'バズ': 6750, 'り方': 6751, '詳しい': 6752, 'もし': 6753, '通り': 6754, '莫大': 6755, '❤': 6756, '️': 6757, 'ばか': 6758, '怖がっ': 6759, '代案': 6760, '気付い': 6761, '戦法': 6762, 'デメリット': 6763, '建設': 6764, 'エモエモ': 6765, '得たい': 6766, 'したこと': 6767, '断定': 6768, '反感': 6769, '秀逸': 6770, '広める': 6771, 'あえて': 6772, 'ワンパターン': 6773, '主流': 6774, '外れ': 6775, '大々的': 6776, 'あふれ': 6777, '成功': 6778, '現行': 6779, '誰も知らない': 6780, 'astar': 6781, 'つぶやい': 6782, 'zunba': 6783, 'ryu': 6784, '規約違反': 6785, 'タブー': 6786, 'TL': 6787, '訳す': 6788, '開い': 6789, '役': 6790, '立た': 6791, 'トップレベル': 6792, '素早い': 6793, 'OverwatchBlog': 6794, '0chまとめサイト': 6795, '訳する': 6796, '特有': 6797, '言い回し': 6798, '会': 6799, '新大久保': 6800, '秒間': 6801, '必読': 6802, '難': 6803, 'しみ': 6804, 'こかさ': 6805, 'ねんね': 6806, 'DVA': 6807, 'かわいいっ': 6808, '楽しん': 6809, '効率的': 6810, 'それでいて': 6811, 'エーリアンウェアゾーン': 6812, '供給': 6813, '思い出せ': 6814, '書き留め': 6815, '親切': 6816, 'pepper': 6817, '掴ん': 6818, '還元': 6819, 'くと': 6820, '寄付': 6821, 'キャスター': 6822, '明後日': 6823, '金曜日': 6824, 'このまま': 6825, '載っけ': 6826, '総': 6827, 'プレ': 6828, 'イ人': 6829, 'まとん': 6830, 'メモリ': 6831, '0gb': 6832, '上がり': 6833, '呟き': 6834, 'いくよ': 6835, '現実世界': 6836, '出し合っ': 6837, 'クラウドソーシング': 6838, '出来上がる': 6839, 'カッコヨク': 6840, '校正': 6841, '投げる': 6842, '載っ': 6843, '揃う': 6844, 'まずは': 6845, '日本一': 6846, 'ミロ': 6847, 'コンビ': 6848, '猛威': 6849, '振るっ': 6850, 'それと': 6851, 'Sさん': 6852, 'TS': 6853, 'スパイギアデュオ': 6854, '索敵': 6855, '軽量': 6856, '空中': 6857, '充電': 6858, '受け入れ': 6859, '溢れ': 6860, 'logicool': 6861, '独占': 6862, '相対': 6863, '振れ': 6864, '極めれ': 6865, 'メジャー': 6866, 'すくなくとも': 6867, '0本': 6868, '網羅': 6869, '目標': 6870, '文章力': 6871, 'だるいっ': 6872, 'シュプリーム': 6873, '吉本': 6874, '買収': 6875, '封鎖': 6876, '封じる': 6877, 'nDva': 6878, 'プラチナファラ': 6879, '訳': 6880, '兼ね': 6881, 'クリアリング': 6882, '空': 6883, 'とぼ': 6884, 'しっ': 6885, '割り': 6886, '単語': 6887, '近距離': 6888, '戦お': 6889, 'まずい': 6890, '踏める': 6891, 'どこか': 6892, 'まとまっ': 6893, '作り出す': 6894, 'ググる': 6895, '基準': 6896, '実践': 6897, '試行': 6898, '繰り返す': 6899, '存在価値': 6900, 'つりあげよ': 6901, '教員': 6902, '世界史': 6903, '地理': 6904, 'ムダ': 6905, '受けよ': 6906, 'ゲキヤバ': 6907, '合わ': 6908, 'どこら': 6909, '囲碁': 6910, '整備': 6911, '嫌悪': 6912, '示す': 6913, '民主主義': 6914, '若年層': 6915, '爆': 6916, 'アド': 6917, '損': 6918, 'n国': 6919, 'ポスター': 6920, 'あかるい': 6921, '標榜': 6922, '既得権益': 6923, '表れ': 6924, 'トップダウン': 6925, '人民': 6926, '採用': 6927, 'スイッチングコスト': 6928, 'nシステム': 6929, '諦観': 6930, 'ボトムアップ': 6931, 'AR': 6932, '先端': 6933, '領域': 6934, '模倣': 6935, '新時代': 6936, '見込める': 6937, 'Lobi': 6938, 'HANAMURA': 6939, '広義': 6940, '可読性': 6941, '広げ': 6942, '一般的': 6943, 'クローズド': 6944, '速': 6945, 'それなら': 6946, '考': 6947, '加わら': 6948, '指標': 6949, 'エモエモエモ': 6950, '社会的地位': 6951, '攻め立て': 6952, '見つける': 6953, 'フォーエバーチャットファイト': 6954, 'バトル': 6955, '正当': 6956, '打ち倒し': 6957, '醍醐味': 6958, '戦い': 6959, 'nTop': 6960, 'かみ': 6961, '山': 6962, 'なき': 6963, 'せめぎ': 6964, '儚': 6965, 'べる': 6966, 'ぃつよ': 6967, '高けれ': 6968, '対照実験': 6969, 'イチャイチャ': 6970, '黒い': 6971, '服': 6972, '子': 6973, '可愛く': 6974, '番組': 6975, '囲ま': 6976, '写真': 6977, '撮っ': 6978, 'ねぎっ': 6979, 'たんか': 6980, '役得': 6981, '例外': 6982, '選考': 6983, 'USG': 6984, '別格': 6985, 'ゲーミングキーボード': 6986, 'テンキー': 6987, 'ロジクール': 6988, 'センサー': 6989, 'ワイヤレス': 6990, '機器': 6991, 'ワイヤレスマウス': 6992, 'zowie': 6993, 'レーザー': 6994, 'デスアダー': 6995, 'クーガー': 6996, '劣化': 6997, '至っ': 6998, 'ロケット': 6999, 'ブランド名': 7000, '止まっ': 7001, 'まま': 7002, 'ゼミ': 7003, 'ねれ': 7004, '溶け': 7005, '録画': 7006, 'ガッツリ': 7007, '一息': 7008, 'シ': 7009, 'NA': 7010, 'ぼーっ': 7011, '振り返り': 7012, '逮捕': 7013, '荒らす': 7014, 'のん': 7015, 'けさ': 7016, 'リプライ': 7017, 'いきなり': 7018, 'フオロウワウー': 7019, 'ボコ': 7020, 'ヘイト': 7021, '不正': 7022, 'っす': 7023, 'テクノロジー': 7024, 'インパクト': 7025, '私大': 7026, '人文': 7027, '図書館科学': 7028, 'しょ': 7029, 'nemus': 7030, 'ipad': 7031, 'ゲーミングディスプレイ': 7032, '面白いっ': 7033, 'ばっち': 7034, '濃度': 7035, 'apex': 7036, 'ボルスカヤ': 7037, '瀕死': 7038, 'URL': 7039, '盛り上がろ': 7040, 'ゃないしどうでもいいから': 7041, '主催者': 7042, 'レートグラマス': 7043, '伝わり': 7044, 'やすけれ': 7045, '伝われ': 7046, 'ないか': 7047, '限ら': 7048, 'あり方': 7049, '話す': 7050, 'シバー': 7051, '眠': 7052, 'エグ': 7053, 'オートエイム': 7054, '比例': 7055, 'Misfits': 7056, '不調': 7057, '多種': 7058, '数多く': 7059, 'メタソンブラ': 7060, '不可欠': 7061, '踏む': 7062, 'マッサージ': 7063, '高周波': 7064, 'ゴロゴロ': 7065, '中学': 7066, '働きかける': 7067, 'もらえれ': 7068, '上位陣': 7069, '新規性': 7070, '順序': 7071, 'オリジナル': 7072, 'USGSP': 7073, '全体的': 7074, 'potm': 7075, '浅い': 7076, 'nggwp': 7077, 'すて': 7078, 'こーち': 7079, '殺人予告': 7080, '書き込み': 7081, '教室': 7082, '黒板': 7083, 'ノー': 7084, '恨み': 7085, 'お世話': 7086, '手出': 7087, '杭': 7088, '外': 7089, 'さらさ': 7090, 'ひん': 7091, 'せいな': 7092, '皆様': 7093, '好か': 7094, 'nonke': 7095, 'gif画像': 7096, '作り方': 7097, 'レイアウト': 7098, '学ん': 7099, '繋がっ': 7100, '追え': 7101, '殿': 7102, '無職': 7103, '呼ばわり': 7104, 'さんま': 7105, 'すりー': 7106, '生きる': 7107, 'ノア': 7108, 'あさん': 7109, 'ガレリア': 7110, 'たのしみ': 7111, 'ガール': 7112, 'open': 7113, 'ゾーイ': 7114, '反転': 7115, '色味': 7116, '間隔': 7117, 'マガジン': 7118, 'きついっ': 7119, '一斉': 7120, '有用': 7121, 'hanatyan': 7122, 'ツイートマン': 7123, 'ロドホ': 7124, 'くりー': 7125, '威力': 7126, 'ブログ記事': 7127, 'STORIA': 7128, '除名': 7129, 'バカバカしい': 7130, 'ナウ': 7131, '部外者': 7132, '並び': 7133, '犯罪者': 7134, '検挙': 7135, '列挙': 7136, '習う': 7137, '存在意義': 7138, '書けれ': 7139, 'uDCA': 7140, '非営利': 7141, '取り扱い': 7142, 'とどまら': 7143, 'べく': 7144, '門戸': 7145, 'アウトプット': 7146, 'アウトソーシング': 7147, 'プレゼンス': 7148, 'いただく': 7149, '五十人': 7150, 'だるく': 7151, 'バンクーバー': 7152, 'ステージ0': 7153, '最終': 7154, 'アトランタ': 7155, 'マッチング': 7156, '領収書': 7157, '忘れる': 7158, '最新情報': 7159, 'negitaku': 7160, '流す': 7161, 'るか': 7162, '一時': 7163, 'Stocklip': 7164, '銘柄': 7165, '赤字': 7166, 'スーパーリーグ': 7167, 'ギトギト': 7168, '黒字': 7169, 'ひどかっ': 7170, '薬局': 7171, '洗浄液': 7172, '効く': 7173, '我慢': 7174, 'Gizzard': 7175, '早漏': 7176, '下ネタ': 7177, 'チンコ': 7178, '論理回路': 7179, 'ツッコミ待ち': 7180, 'もしかして': 7181, 'Zoel': 7182, '妄想': 7183, '生み出し': 7184, '詳細': 7185, '襲わ': 7186, 'ぶん': 7187, 'bkstars': 7188, 'bunny': 7189, '長引い': 7190, '単騎': 7191, 'パネエ': 7192, 'ビジョン': 7193, '追い出さ': 7194, '垂れ流し': 7195, '無価値': 7196, '作ん': 7197, 'つくん': 7198, 'たれ': 7199, 'づけ': 7200, 'まとめサイト': 7201, 'バラバラ': 7202, 'ポータルサイト': 7203, 'USGI': 7204, '相対的': 7205, '誤認': 7206, '謝罪': 7207, '老害': 7208, 'プロゲーマーズ': 7209, '構図': 7210, '入団': 7211, 'storia': 7212, 'おもう': 7213, '求めて': 7214, '焦っ': 7215, 'コンプライアンス': 7216, 'プロ意識': 7217, '薄かっ': 7218, '炎上': 7219, '方面': 7220, '叩か': 7221, 'まくる': 7222, '直訴': 7223, '出場資格': 7224, '皆さん': 7225, '落ち着こ': 7226, 'ちな': 7227, '執筆': 7228, 'ブラックジョーク': 7229, '盛り込も': 7230, '邪魔': 7231, 'センシティブな問題': 7232, '荒れ': 7233, '迷惑': 7234, '社会的': 7235, '認めよ': 7236, '炎上マーケティング': 7237, '熱い': 7238, 'これぞ': 7239, 'エンターテイメント': 7240, 'どうと': 7241, 'せっかく': 7242, '0回目': 7243, '杯': 7244, '先週': 7245, '盛り上がっ': 7246, '打ち込め': 7247, '使お': 7248, 'コリアンプロ': 7249, '生': 7250, 'だったん': 7251, 'ヘッドライン': 7252, '張り付い': 7253, 'ばす': 7254, 'クラメンデュオ': 7255, '軍': 7256, '団ラン': 7257, 'ゾ': 7258, '終電': 7259, 'オナニーマスター黒沢': 7260, '洗わ': 7261, '取り組める': 7262, 'BI': 7263, '人間らしく': 7264, '目指そ': 7265, '生計': 7266, 'ベーシックインカム': 7267, '春休み': 7268, '曜日感覚': 7269, '引っ張る': 7270, '得する': 7271, '年下': 7272, '真価': 7273, '奮い立た': 7274, '引っ張っ': 7275, '誹謗': 7276, '中傷': 7277, 'パワーワード': 7278, 'Runaway': 7279, 'セミプロ': 7280, 'ダサい': 7281, '事情': 7282, 'ahq': 7283, '再生回数': 7284, '描こ': 7285, 'プロゲーミングチーム': 7286, '搾取': 7287, '午前': 7288, 'サボっ': 7289, 'さと': 7290, 'タメ口': 7291, 'ボカロ': 7292, '山手線': 7293, '無法地帯': 7294, '返す': 7295, '足手まとい': 7296, '見れる': 7297, '赤坂': 7298, '袋': 7299, 'メイク': 7300, '緑': 7301, 'スト': 7302, 'そっくり': 7303, '意識高い系': 7304, 'katoo': 7305, 'スーパー': 7306, '熱心': 7307, 'kino': 7308, 'ko': 7309, 'mendokusai': 7310, 'neru': 7311, '驚嘆': 7312, 'お釣り': 7313, 'キリキリ': 7314, '当事者意識': 7315, '自戒': 7316, '卒業': 7317, '買える': 7318, '私立大学': 7319, '長崎': 7320, 'ウエスレヤン': 7321, '肉薄': 7322, 'Winston': 7323, '休日': 7324, '蒸し': 7325, 'ポリゴン': 7326, '0D酔い': 7327, '映像': 7328, 'ぐるぐる': 7329, '酔わ': 7330, 'したい': 7331, '自作PC': 7332, '借り': 7333, '再': 7334, 'シバター': 7335, 'メインロスター': 7336, 'cm': 7337, '吸い': 7338, '付い': 7339, 'ワンマグ': 7340, 'Effect': 7341, 'ばり': 7342, 'トレーサーエイム': 7343, 'かんたん': 7344, 'E': 7345, 'かよ': 7346, 'ナンバー0': 7347, 'ライト': 7348, 'スルメゲー': 7349, '短く': 7350, '楽しめ': 7351, '三日': 7352, '五日': 7353, '泥棒': 7354, 'uDD': 7355, '被弾': 7356, 'wifi': 7357, 'ヘルプ': 7358, 'ヘルプページ': 7359, '方針': 7360, 'ベンチャー': 7361, '促進': 7362, '行政': 7363, '下らな': 7364, 'つぶれる': 7365, '中間': 7366, '税': 7367, '利益誘導': 7368, '喜ば': 7369, 'おもちゃ': 7370, 'hirou': 7371, 'sugoi': 7372, 'スケーラビリティ': 7373, 'n中': 7374, '同義': 7375, '交通': 7376, '便': 7377, 'キャッチ': 7378, '騒い': 7379, '煩悩': 7380, 'モロに': 7381, '充て': 7382, '背': 7383, 'づらかっ': 7384, '余り': 7385, 'デスクワーク': 7386, '働き': 7387, '卓球': 7388, 'アッパー': 7389, '0才': 7390, '日本の人': 7391, '各国': 7392, '進め方': 7393, 'ハングリー精神': 7394, 'フィルタリング': 7395, 'GameWith': 7396, 'コンソール': 7397, '取り組ん': 7398, '攻略wiki': 7399, 'Dizzy': 7400, '原則': 7401, '定量': 7402, '筋': 7403, 'い道': 7404, '勝と': 7405, '死屍累々': 7406, '前日': 7407, 'ninja': 7408, 'キャリー': 7409, '一躍': 7410, 'ドリーム': 7411, 'NRG': 7412, 'アメリカンドリーム': 7413, 'おく': 7414, 'スゲー': 7415, 'パブリックドメイン': 7416, 'メリットデメリット': 7417, '語り': 7418, 'つくせ': 7419, '求めよ': 7420, '漁っ': 7421, 'nesports': 7422, '視座': 7423, 'sports': 7424, '市場規模': 7425, '語る': 7426, 'HADO': 7427, '拡張': 7428, 'スマートホン': 7429, '浸透': 7430, 'PCゲーム': 7431, '同列': 7432, '産業': 7433, '枠組み': 7434, '伴っ': 7435, '掛け合わ': 7436, 'ホン': 7437, 'それら': 7438, '広がっ': 7439, 'ウォッチャー': 7440, 'ゲームセンター': 7441, '化し': 7442, '早朝': 7443, '校': 7444, 'はやっ': 7445, 'バレー': 7446, '体罰': 7447, 'パラシュート': 7448, '0キロ': 7449, 'マッハパンチ': 7450, '繰り出し': 7451, 'ロビー': 7452, 'ナンバーゼロ': 7453, 'スタヌスパイギア': 7454, 'コンドーム': 7455, 'arduino': 7456, 'java': 7457, '世界一': 7458, 'あつめ': 7459, 'スタ': 7460, '脳内': 7461, 'オンリー': 7462, '据え置き': 7463, 'コンシューマ': 7464, 'nVR': 7465, 'しきっ': 7466, '盛り上がる': 7467, 'アーハン': 7468, 'afb': 7469, 'mano': 7470, 'ウマ': 7471, 'ばい': 7472, '練ら': 7473, 'ワンヒーラートールビョーンオリーサ': 7474, '止める': 7475, '八': 7476, '捻出': 7477, 'ミリ': 7478, '土下座': 7479, '会わ': 7480, '会う': 7481, 'シグナリング': 7482, '虚しい': 7483, 'アルデュイ': 7484, 'ノノノノ': 7485, '小手先': 7486, '其の': 7487, '凌ぎ': 7488, 'みじんこ': 7489, '生物': 7490, 'ゴミダァ': 7491, '大物': 7492, 'TitanX': 7493, 'つなぐ': 7494, 'のようなもの': 7495, '濃ゆい': 7496, '遠く': 7497, 'ついでに': 7498, 'PCケース': 7499, '買い替え': 7500, '予想通り': 7501, 'カエル': 7502, '鳴き声': 7503, 'ノコギリ': 7504, '木': 7505, '切ろ': 7506, '池': 7507, 'べた': 7508, 'みんく': 7509, '何より': 7510, '集約': 7511, '検閲': 7512, 'ストレスブースト': 7513, 'ソフトウェア': 7514, 'えん': 7515, 'インテル': 7516, '引き抜か': 7517, 'あほ': 7518, 'デトネーション': 7519, '堂々': 7520, 'てかっ': 7521, 'こいい': 7522, '酒': 7523, 'おかず': 7524, '据え': 7525, 'たひ': 7526, 'ちゃんこ': 7527, '負けん気': 7528, '男前': 7529, '単調': 7530, '耐性': 7531, '体育': 7532, '東大生': 7533, 'っしょ': 7534, 'ホワイト': 7535, '難儀': 7536, '内部': 7537, 'ネット上': 7538, '怖かっ': 7539, '腐らす': 7540, '勿体無い': 7541, '配慮': 7542, '支え': 7543, 'リア': 7544, '冷たく': 7545, '刻': 7546, '駆ける': 7547, '少女': 7548, '数少ない': 7549, '叫': 7550, 'びまくっててすげ': 7551, 'ヌルヌル': 7552, '液晶': 7553, 'アルファド': 7554, '君': 7555, 'スペック': 7556, '組め': 7557, '出せん': 7558, 'もうちょい': 7559, 'gtx': 7560, '安物': 7561, '優先': 7562, '秋田': 7563, 'ウキウキ': 7564, 'ドライバインストール': 7565, 'トリプルエックス': 7566, '申し込ま': 7567, 'インターネット接続': 7568, '復旧': 7569, '対戦': 7570, '誘っ': 7571, '₍₍': 7572, '꒪່౪̮꒪່': 7573, '⁾⁾': 7574, '浮気': 7575, 'あるある': 7576, '関わる': 7577, '自己主張': 7578, 'オラオラ': 7579, '島田': 7580, 'ハストン': 7581, 'Beta': 7582, 'Test': 7583, 'Today': 7584, 'rate': 7585, 'Games': 7586, 'Used': 7587, 'time': 7588, 'heros': 7589, 'reinhardt': 7590, 'winston': 7591, 'lucio': 7592, 'todays': 7593, 'KH': 7594, '結ん': 7595, 'かから': 7596, 'スポンサー契約': 7597, '成城石井': 7598, 'ブルジョア': 7599, '設営': 7600, 'ボクシング': 7601, '背中': 7602, '合っ': 7603, '楽しも': 7604, '修復': 7605, 'つけれ': 7606, '燃え上がる': 7607, '徳': 7608, 'らっしゃい': 7609, 'コントロールシンメトラ': 7610, '申し訳ない': 7611, '挑戦者': 7612, '海賊': 7613, 'ウォリアー': 7614, 'アグロドルイド': 7615, 'メタル': 7616, '四つ': 7617, 'ガチマッチ': 7618, 'ニルグ': 7619, 'イロハ': 7620, '教わっ': 7621, 'ダコ': 7622, 'けしからん': 7623, '稼': 7624, 'ぐのはけしからんっておもって': 7625, 'ストリートファッション': 7626, 'ごつい': 7627, '開発チーム': 7628, '試行錯誤': 7629, 'デザイン案': 7630, 'キャラクター': 7631, '込め': 7632, 'にわたって': 7633, '審査': 7634, '決済手数料': 7635, '異質': 7636, 'サブスクリプション': 7637, 'フリーミアム': 7638, 'サブスクライブ': 7639, 'Udemy': 7640, 'ボーナス': 7641, 'クエスト': 7642, 'プリースト': 7643, '挑発': 7644, '連発': 7645, 'ミッドレンジパラディン': 7646, 'クエストローグ': 7647, '九時': 7648, 'C0': 7649, '大丈夫': 7650, 'ハースゲーマーズ': 7651, 'トレビア': 7652, '競争': 7653, '激し': 7654, '送り': 7655, '若い': 7656, '磨か': 7657, '思いっきり': 7658, '過ごす': 7659, '同時': 7660, '進行': 7661, '絶対無理': 7662, 'USB': 7663, 'SSD': 7664, '行こう': 7665, '詰まっ': 7666, '聞こ': 7667, 'デイリーミッションクリア': 7668, 'ウォーロック': 7669, 'ダイナミックディスク': 7670, 'パーティション': 7671, '区切っ': 7672, 'ハードウェア': 7673, 'フォーマット': 7674, 'まみれ': 7675, '圏': 7676, 'BTO': 7677, '買え': 7678, 'OS': 7679, 'インストール': 7680, 'インスコ': 7681, 'きんわ': 7682, 'ubi': 7683, 'ジャガイモ': 7684, '炊き': 7685, 'スクワット': 7686, '上流': 7687, '受け継い': 7688, '確信': 7689, 'ディスティニードロー': 7690, '一発逆転': 7691, '動き回る': 7692, '息切れ': 7693, 'きると': 7694, 'GeForceONAIR': 7695, 'Google検索': 7696, 'ぱくる': 7697, '確': 7698, 'エモート': 7699, 'アドバンテージ': 7700, 'BIOS': 7701, '日本初': 7702, '見応え': 7703, 'pung': 7704, 'ギリートサプ': 7705, 'サイハテ': 7706, '積極': 7707, '活性化': 7708, 'もっともっと': 7709, '豊か': 7710, 'なくなり': 7711, '消え去り': 7712, '尊い': 7713, 'ニートオンリー': 7714, 'バッチ': 7715, 'リテーナー': 7716, 'フルボッコ': 7717, '阻害': 7718, '左右対称': 7719, 'いらん': 7720, '濃かっ': 7721, '痛感': 7722, '高橋さん': 7723, 'ガー': 7724, 'しぃ': 7725, 'ゆたぽん': 7726, 'zonda': 7727, '順々': 7728, '近': 7729, 'ゲージ': 7730, '組織的': 7731, '想定': 7732, '統率': 7733, '兵役': 7734, '集団行動': 7735, '室': 7736, '開成高校': 7737, 'ヤンキー': 7738, 'につれ': 7739, '真っ当': 7740, '高杉': 7741, '利き': 7742, 'amazon': 7743, '詐欺': 7744, '値下げ': 7745, '先取り': 7746, 'ユニフォーム': 7747, 'おかし': 7748, 'イカ': 7749, 'セントス': 7750, 'セン': 7751, 'トス': 7752, '要件': 7753, '寝坊': 7754, 'たて': 7755, '選ん': 7756, 'ドリームチーム': 7757, 'ナゲッツ': 7758, '親子': 7759, '一般': 7760, 'ばら': 7761, '歴': 7762, '選出': 7763, 'パッと': 7764, '反省会': 7765, '発し': 7766, 'カジュアルゲーマー': 7767, '引退': 7768, 'ディスコ': 7769, '制約': 7770, '稼ご': 7771, '延長': 7772, '稼げれ': 7773, 'オッケー': 7774, 'ボヤー': 7775, 'FPSwatcher': 7776, '褒め': 7777, '0万円': 7778, 'せいぜい': 7779, 'nFPS': 7780, 'コピー': 7781, '知名': 7782, '杉草': 7783, 'ノンケ': 7784, 'パチ': 7785, 'マリ': 7786, 'たけ': 7787, '申し訳': 7788, 'tips': 7789, '十倍': 7790, 'にらめっこ': 7791, 'ブサイク': 7792, '優劣': 7793, '自爆テロ': 7794, 'エキサイティング': 7795, '秘め': 7796, '赴く': 7797, '自作': 7798, 'る説': 7799, '濃厚': 7800, '悟空': 7801, '思い浮かべ': 7802, 'ツクモ': 7803, '最': 7804, '安': 7805, '実店舗': 7806, '買い換え': 7807, '電気店': 7808, 'ミドルスペック': 7809, 'ハイスペック': 7810, '価格差': 7811, 'コスパ': 7812, 'ぽんぽこ': 7813, '六万': 7814, '済ん': 7815, 'ミロウィンストン': 7816, '飛び出す': 7817, 'ノック': 7818, '孤立': 7819, '等しく': 7820, '休学': 7821, '再生': 7822, '略称': 7823, '改名': 7824, '由来': 7825, '本名': 7826, 'ヘッドホン': 7827, '虫': 7828, '欠点': 7829, 'アペレジェマジ': 7830, 'バトロワ': 7831, 'アベマ': 7832, 'ウルトラゲームスチャンネル': 7833, '整理': 7834, '格ゲー': 7835, '多岐': 7836, 'わたっ': 7837, 'さっぱり': 7838, '嗜好': 7839, 'シャドバ': 7840, 'AbemaTV': 7841, '放映': 7842, 'スマホユーザー': 7843, 'オンライン': 7844, 'テレビ局': 7845, '縛ら': 7846, '放送': 7847, '形態': 7848, '再現': 7849, 'ウルトラゲームス': 7850, 'SE': 7851, '周期': 7852, '独裁主義': 7853, '偽っ': 7854, '本垢': 7855, 'テンプレ': 7856, '万か': 7857, 'b': 7858, 'amd': 7859, 'ryzen': 7860, 'i': 7861, 'k': 7862, 'R0': 7863, 'サムライ': 7864, 'しゃ': 7865, 'きめ': 7866, '挙げる': 7867, '悲劇のヒロイン': 7868, '所々': 7869, 'キモい': 7870, 'オーラ': 7871, '際': 7872, 'Numlocked': 7873, 'ポンコツ': 7874, 'あんな': 7875, 'ハルク': 7876, 'Lazer': 7877, 'kittenz': 7878, 'ヘッドコーチ': 7879, 'IDDQD': 7880, 'ありえん': 7881, '行方': 7882, '溶かさ': 7883, 'numlocked': 7884, 'ハルトランク': 7885, '四位': 7886, '化け物': 7887, 'sanctum': 7888, '縦長': 7889, 'ももたん': 7890, 'クソロングチャージ': 7891, 'スプレッドシート': 7892, '滝田': 7893, '木滝': 7894, '専属': 7895, 'グルーピングアップ': 7896, '健康': 7897, 'プリセット': 7898, '保存': 7899, '取り出す': 7900, '時間的': 7901, '委託': 7902, '発動': 7903, '逆転': 7904, '中部地方': 7905, '愛知県': 7906, '県': 7907, '柵': 7908, '通らん': 7909, 'すり抜ける': 7910, 'むく': 7911, '気絶': 7912, 'スカッド': 7913, 'あそこ': 7914, 'ぶち込ん': 7915, 'ガス': 7916, '運転': 7917, 'フリーズ': 7918, '全滅': 7919, 'マチェット': 7920, '爆笑': 7921, 'クレーム': 7922, 'ヒジ': 7923, 'まっ': 7924, 'ち': 7925, '文字化け': 7926, '文字列': 7927, 'inque': 7928, '過疎': 7929, 'オンゲ': 7930, 'カスタムメイド0D0': 7931, 'スクリーム': 7932, '高台': 7933, '飛び越え': 7934, 'クレストゲーミング': 7935, 'プルプル': 7936, '招待': 7937, 'エンビー': 7938, '半': 7939, '国主': 7940, '導': 7941, '制度': 7942, '取り入れ': 7943, 'ローン': 7944, '作り上げ': 7945, '減らす': 7946, '主導': 7947, '足並み': 7948, '電子マネー': 7949, '導入': 7950, 'ゴリラ': 7951, '溶ける': 7952, 'uru': 7953, 'ca': 7954, 'FW': 7955, '対野': 7956, 'stylus': 7957, 'スタイラス': 7958, 'フルパランクマ': 7959, 'コンビニ': 7960, 'ホテル': 7961, '無人': 7962, '比べる': 7963, '成果': 7964, '生み出せる': 7965, 'まだまだ': 7966, '過労': 7967, 'いざ': 7968, 'ブラジル人': 7969, 'uDDE': 7970, 'uDDF': 7971, '欲': 7972, '金髪': 7973, 'うっ': 7974, 'ウルカ': 7975, 'オリンピック': 7976, '物理的': 7977, '足音': 7978, '聞こえ': 7979, 'どり': 7980, 'にも': 7981, 'スコ': 7982, 'だぁ': 7983, '太刀打ち': 7984, 'チョッパリヌーブ': 7985, 'ネーム': 7986, 'ダッシュ': 7987, 'うさぎ': 7988, '跳び': 7989, 'つらい': 7990, 'ウィキ': 7991, 'すり減らし': 7992, 'するり': 7993, '後衛': 7994, 'ブツブツ': 7995, '精神状態': 7996, '自身': 7997, 'STEM': 7998, 'はっ': 7999, 'owW': 8000, '採択': 8001, '発売': 8002, '休ま': 8003, 'view': 8004, '0時間後': 8005, '直感的': 8006, 'つけよ': 8007, '玄関': 8008, 'ちの': 8009, 'はいれ': 8010, '断言': 8011, '法的': 8012, '円筒': 8013, '辞書': 8014, '穴埋め': 8015, 'すう': 8016, '現代人': 8017, 'toeic': 8018, 'すみ': 8019, '詰める': 8020, 'だるかっ': 8021, 'キーロック': 8022, '死ぬかと思った': 8023, 'サンシスター': 8024, 'しそ': 8025, 'M0': 8026, '下し': 8027, '争い': 8028, '恐れる': 8029, 'フリー': 8030, 'フラバンガ': 8031, '消せ': 8032, 'ナノブ': 8033, '殴る': 8034, 'ふり': 8035, '読み切っ': 8036, '殴れ': 8037, '末': 8038, 'しゃぶら': 8039, 'ペイパル': 8040, '個人間送金': 8041, '振り込み': 8042, '毎月': 8043, '支払っ': 8044, 'バカバカし': 8045, 'さま': 8046, '監督': 8047, '作品': 8048, 'legends': 8049, '年末調整': 8050, '確定申告': 8051, 'い場所': 8052, '絞る': 8053, 'グッズ': 8054, '運営会社': 8055, '売り上げ': 8056, '損失': 8057, 'に対する': 8058, '頻繁': 8059, '共闘': 8060, '高まっ': 8061, 'ゲームイベント': 8062, 'しゃぶり': 8063, 'シャカ': 8064, '曰く': 8065, 'ずらし': 8066, '戦え': 8067, 'ぽーん': 8068, '飛ば': 8069, 'トランポリン': 8070, '先輩': 8071, 'しっぷう': 8072, '乙': 8073, 'すかー': 8074, '騒音': 8075, '苦情': 8076, '全敗': 8077, 'ファイヤ': 8078, 'ボール': 8079, 'まとめよ': 8080, '逃げられない': 8081, '押す': 8082, '残党': 8083, 'ゆっくり': 8084, '起こさ': 8085, '白星': 8086, 'immortals': 8087, 'エイリアンウェアー': 8088, 'マンスリーメレー': 8089, 'beta': 8090, 'test': 8091, 'ダイブアンチ': 8092, '通い': 8093, '最低賃金': 8094, 'インフレ': 8095, '貨幣': 8096, 'さげれ': 8097, 'ジンバブエ': 8098, 'ジンバブエドル': 8099, 'それに': 8100, 'タグ': 8101, 'りの': 8102, '追っかけ': 8103, '芋': 8104, '壊さ': 8105, '置き': 8106, '疑う': 8107, '核爆弾': 8108, '降っ': 8109, '降る': 8110, 'ひきこもる': 8111, 'はそん': 8112, 'ロー': 8113, '人的': 8114, 'シャターガード': 8115, '深まっ': 8116, '深み': 8117, '隠れる': 8118, '飛べ': 8119, '浴びる': 8120, '隠れ': 8121, 'フォーカスルシオ': 8122, 'フライングルシオ': 8123, '学園': 8124, 'ADHD': 8125, 'ナード': 8126, 'ジョック': 8127, 'いじめ': 8128, '持ち上げ': 8129, 'カレント': 8130, 'ミスマッチ': 8131, '起こる': 8132, 'マジハッピー': 8133, '再掲': 8134, '旨': 8135, '自営業': 8136, '休ん': 8137, 'うまいっ': 8138, '極限': 8139, '七月': 8140, '餌': 8141, 'レイレイ': 8142, '進出': 8143, 'さひ': 8144, 'post': 8145, 'truth': 8146, '真実': 8147, '悦に入る': 8148, '言葉自体': 8149, '資源': 8150, '食物': 8151, '生産': 8152, '容易': 8153, '尊敬': 8154, 'モテ': 8155, '捉えよ': 8156, '外国人': 8157, '留学生': 8158, 'ぱぶ': 8159, '焦る': 8160, '時期': 8161, 'チーデスエイム': 8162, '問い': 8163, '定時': 8164, '帰れる': 8165, 'フリーランチ': 8166, '嫌っ': 8167, '下がら': 8168, 'むずすぎぃ': 8169, 'アーケード': 8170, 'よっしゃ': 8171, 'レジェンダリー': 8172, 'ビシュカー': 8173, '原点': 8174, 'へー': 8175, '遠距離': 8176, 'なんぼ': 8177, 'たのしい': 8178, '聞こえん': 8179, '生え': 8180, 'なお': 8181, '模様': 8182, 'ゆるかっ': 8183, '遮音': 8184, '音質': 8185, 'ns': 8186, '暗黙のルール': 8187, 'ド': 8188, 'ｗｗｗ': 8189, 'きっと': 8190, '両手': 8191, '両足': 8192, 'あららら': 8193, '控えめに言って': 8194, 'Deeplearning': 8195, '立ち位置': 8196, 'スリープ': 8197, 'キープ': 8198, '余ら': 8199, '浅': 8200, '粘り': 8201, '経験値': 8202, '見失う': 8203, '深まる': 8204, 'マンブー': 8205, 'ファラマーシー': 8206, 'おしまい': 8207, 'potg': 8208, 'ゴリラウルト': 8209, 'ゾンダ': 8210, 'OMENCUP': 8211, 'アメケンキャリー': 8212, 'アメケン': 8213, '馬杉': 8214, 'あび': 8215, 'フォーカスゲキアツ': 8216, 'カイザー': 8217, '対照的': 8218, 'えぐかっ': 8219, '守っ': 8220, '下ろせる': 8221, 'ｗｗ': 8222, '後退': 8223, '反射神経': 8224, 'こなし': 8225, 'ランナウェイ': 8226, '選手紹介': 8227, '合わし': 8228, 'パクパクパク': 8229, 'スリー': 8230, 'だーつ': 8231, 'ユニバーシティ': 8232, '囲ん': 8233, '材料': 8234, 'むなしい': 8235, 'らし': 8236, '画期的': 8237, '宇宙船': 8238, '反面': 8239, 'WPG': 8240, 'シャタースポット': 8241, '東西': 8242, 'はまっ': 8243, 'ペルソナ0': 8244, 'ときめきメモリアル': 8245, '回帰': 8246, 'せよ': 8247, '若いやつ': 8248, '0票': 8249, '重み': 8250, '平均寿命': 8251, '不利益': 8252, '被ら': 8253, '勝た': 8254, '増': 8255, '被り': 8256, 'ポスト': 8257, 'チラシ': 8258, '投函': 8259, '北千住': 8260, '食え': 8261, '美味い': 8262, '小学0年生': 8263, 'スプラトゥーン': 8264, '時代の流れ': 8265, '迷う': 8266, 'エブリデイファラマーシー': 8267, '自閉症': 8268, '扱う': 8269, 'd0': 8270, '算数': 8271, 'すぎん': 8272, '英雄': 8273, '半ば': 8274, '途絶える': 8275, '無念': 8276, 'pt': 8277, 'うらやま': 8278, '客': 8279, '連勝': 8280, 'まくれ': 8281, 'スカイプ': 8282, 'OPEN': 8283, '出よ': 8284, '新入生': 8285, '三つ': 8286, '過': 8287, '疎っ': 8288, 'る言': 8289, 'われ': 8290, '中華料理': 8291, 'まずさ': 8292, 'ムカムカ': 8293, '技': 8294, '釣っ': 8295, '押しつける': 8296, 'sanmer': 8297, '団子': 8298, '複数': 8299, '隊': 8300, 'ホロレンズ': 8301, 'マイクロソフト': 8302, '〆': 8303, 'ドン': 8304, '活': 8305, '準備': 8306, 'むのめんどいしね': 8307, 'ばんばん': 8308, 'ぎるしそのわかりやふい': 8309, 'メダル': 8310, '美味しい': 8311, '拙者': 8312, '候': 8313, '戻ら': 8314, '仲間意識': 8315, '受け取っ': 8316, '感情的': 8317, 'ことも': 8318, '光ら': 8319, 'ていいん': 8320, 'やけど': 8321, '各社': 8322, 'バリエーション': 8323, 'IE': 8324, 'クローン': 8325, '0w': 8326, 'l': 8327, '所感': 8328, '下位互換': 8329, '有線': 8330, '見当たら': 8331, 'ソール': 8332, '統一': 8333, '重さ': 8334, 'ワイヤー': 8335, '重く': 8336, '慣れる': 8337, '売ろ': 8338, 'ウルトゲージ': 8339, '消費': 8340, 'ローリスクハイリターン': 8341, '公式サイト': 8342, 'おなか': 8343, 'やってくん': 8344, '秒速': 8345, 'ﾏﾁﾞﾑﾘ': 8346, 'クラメ': 8347, '出し惜しみ': 8348, '絞っ': 8349, '吐い': 8350, '恥ずかしく': 8351, 'マクソル': 8352, 'リーパーホッグ': 8353, 'かまた': 8354, 'ウルトガンガン': 8355, '刺さり': 8356, 'ソル': 8357, 'ジャーメイン': 8358, '通用': 8359, '飛車': 8360, '効き': 8361, '引き分け': 8362, 'もちこん': 8363, 'ジャンプバグ': 8364, 'ふやさ': 8365, 'ふろ': 8366, 'ぐっ': 8367, '発展途上国': 8368, '地下鉄': 8369, '先導': 8370, '町中': 8371, '途上国': 8372, '古い': 8373, 'たとえば': 8374, 'いずれ': 8375, '追い抜か': 8376, 'オメンカップ': 8377, 'KHTV': 8378, '弱いっ': 8379, '使い道': 8380, 'いつみ': 8381, 'Duo': 8382, '正式': 8383, 'さも': 8384, 'やから': 8385, '終了': 8386, 'バグジャンプ': 8387, '気分転換': 8388, 'ec0': 8389, 'ヨドバシ': 8390, 'L': 8391, 'フィールド': 8392, '善': 8393, '扱っ': 8394, 'こき下ろし': 8395, '悦': 8396, '浸る': 8397, '視力': 8398, '難なく': 8399, '暮らせ': 8400, '視覚障害者': 8401, '援助': 8402, '素晴らしく': 8403, '代表監督': 8404, 'かんけい': 8405, 'えらん': 8406, 'うの': 8407, '委員': 8408, 'ワイ': 8409, '渡し': 8410, 'ススェーデン': 8411, '✈': 8412, 'uDDEF': 8413, 'ルシオナーフ': 8414, 'ダイブコンプ': 8415, '指揮': 8416, '方式': 8417, '上官': 8418, '命令': 8419, 'したがっ': 8420, '異議': 8421, '唱える': 8422, '迅速': 8423, '後作': 8424, 'ディーバ': 8425, '優しい世界': 8426, '流行る': 8427, 'ダブルスナイパーメタ': 8428, 'タンクゲンジ': 8429, '浅かっ': 8430, '仮眠': 8431, '長生き': 8432, '吐か': 8433, 'サージ': 8434, 'ああああああああああああああああああああああああああああああああああああああああ': 8435, 'あああああああああああああああああああああああああああああああああああああ': 8436, 'ああああああああ': 8437, 'ダブルキル': 8438, '豆鉄砲': 8439, 'ああああああああああああああああああああああ': 8440, '野獣先輩': 8441, '淫夢': 8442, '作り出せる': 8443, 'レンジ': 8444, '置ける': 8445, 'リーパーマジ': 8446, '腐ら': 8447, 'ワイワイトロールランクマ': 8448, 'グンニョン': 8449, '渋い': 8450, 'ナルト': 8451, 'ガチピック': 8452, 'ネパール': 8453, '落とせる': 8454, 'ジャンクラガチピック': 8455, '狭め': 8456, '首': 8457, '絞め': 8458, '死ね': 8459, 'もらお': 8460, 'むしろ': 8461, '消極': 8462, '次なん': 8463, '攻める': 8464, '傷ん': 8465, '赤石': 8466, '溜める': 8467, '延々': 8468, '這っ': 8469, 'ヒー': 8470, '逃がさ': 8471, 'くらわす': 8472, '現': 8473, 'マスターハンド': 8474, 'あっち': 8475, '会い': 8476, '旅行': 8477, 'iPad': 8478, '物理キーボード': 8479, '外出': 8480, 'Adobe': 8481, 'いじっ': 8482, '持ち運び': 8483, '闘': 8484, '会議': 8485, 'アイコン': 8486, '眼鏡': 8487, '派': 8488, 'キーワード': 8489, 'プランナー': 8490, '一向に': 8491, 'UX': 8492, '荒野': 8493, '荒野行動': 8494, '和気あいあい': 8495, 'ミラティブインストール': 8496, 'もみない': 8497, 'OpenREC': 8498, '肌': 8499, 'Esports': 8500, 'よき': 8501, '適材適所': 8502, 'はぁ': 8503, 'なり金': 8504, '当たれる': 8505, '止めよ': 8506, '分からん': 8507, '留め': 8508, '卒業式': 8509, 'バト': 8510, 'ぐら': 8511, 'ぼったくり': 8512, 'バー': 8513, 'pay': 8514, 'win': 8515, 'さがし': 8516, 'みつから': 8517, 'ヒカキン': 8518, '欲望': 8519, '薄': 8520, '使命': 8521, '反応速度': 8522, 'ハンマー': 8523, '範囲': 8524, 'とかん': 8525, '防げ': 8526, '減らし': 8527, 'すませる': 8528, '歩く': 8529, 'しに': 8530, 'デレーブ': 8531, 'とどまる': 8532, 'ワンキル': 8533, '真っ先': 8534, 'アンド': 8535, 'バッチリ': 8536, '跳ね返さ': 8537, 'チンパンジークラン': 8538, 'おきん': 8539, '失せる': 8540, 'うるか': 8541, '意志': 8542, 'nartisan': 8543, '選ぼ': 8544, 'マジオワタ': 8545, '陣': 8546, 'チャリ': 8547, '挟ん': 8548, 'br': 8549, 'アイテム': 8550, 'あがりや': 8551, 'にたいして': 8552, 'どー': 8553, '瞳': 8554, '可愛': 8555, '封鎖された渋谷で': 8556, 'いうのす': 8557, '学力': 8558, '経済学': 8559, '設ける': 8560, 'ヘリックスエアショ': 8561, 'かます': 8562, 'ｷﾞﾓﾁﾞｲｲｲｲｲｲｲｲｲｲ': 8563, '勝敗': 8564, 'アナルシ': 8565, 'ト金': 8566, 'マーク': 8567, 'あめ': 8568, 'けんさん': 8569, 'サイバーエージェント': 8570, 'fb': 8571, '切り': 8572, '切り返し': 8573, '幅広い': 8574, 'ルサンチマン': 8575, 'シスター': 8576, 'ビギナー': 8577, 'F0': 8578, 'アイフォン': 8579, '続く': 8580, '殴ら': 8581, 'ジワ': 8582, 'ルート0': 8583, '第一': 8584, '特別': 8585, 'ウチ': 8586, 'ビギナーカップ': 8587, 'チーム練習': 8588, '僕らのユリイカ': 8589, 'ちーむ': 8590, '強靭': 8591, '太もも': 8592, '肩': 8593, '胸': 8594, '取り戻し': 8595, '細く': 8596, '危険': 8597, '種目': 8598, '貧血': 8599, '真っ青': 8600, '聴き': 8601, 'NG': 8602, 'キャラデザ': 8603, '爆速': 8604, 'テクニカル': 8605, '願う': 8606, 'アサルトキャプチャ': 8607, '揺り': 8608, '無謀': 8609, 'AFB': 8610, 'LWB': 8611, 'アヌビス': 8612, '門': 8613, '削れ': 8614, '乱戦': 8615, '優先順位': 8616, '調節': 8617, '不安': 8618, '見合っ': 8619, '最中': 8620, 'つられる': 8621, 'チョークポイント': 8622, 'ファイアストライク': 8623, 'wakiyan': 8624, '解体': 8625, '振り分けれ': 8626, '溜まっ': 8627, '希薄': 8628, 'いとこ': 8629, 'ワイルドカード': 8630, 'CSGO': 8631, 'noppo': 8632, '振り回さ': 8633, 'キッズ': 8634, '見れれ': 8635, 'もた': 8636, 'ガソスタ': 8637, 'とれる': 8638, '回り込ん': 8639, '意表': 8640, '突く': 8641, 'シャターマジ': 8642, 'Kさん': 8643, '判断基準': 8644, '転ば': 8645, 'コリアンサーバー': 8646, '0試合': 8647, 'ボロボロ': 8648, 'ボーナスゲーム': 8649, 'ハイ': 8650, '意気消沈': 8651, 'ナノゲンジ': 8652, 'まら': 8653, '拡散希望': 8654, 'nRole': 8655, 'Flex': 8656, 'イン': 8657, 'フレックス': 8658, 'エイペックス': 8659, 'キーバインド': 8660, '根本的': 8661, 'いじろ': 8662, '羽田空港': 8663, '立地': 8664, 'LCC': 8665, '通せ': 8666, 'おっぱい': 8667, 'キャラクターグラ': 8668, '人気声優': 8669, 'Surefour': 8670, '当分': 8671, 'ご飯': 8672, '友達の友達': 8673, '人間不信': 8674, '他人': 8675, 'スマホアプリ': 8676, 'GamerSensei': 8677, '世界的': 8678, '可処分時間': 8679, '食': 8680, 'い合い': 8681, '超えれ': 8682, '平準': 8683, '直に': 8684, '橋本': 8685, '元知': 8686, '利権': 8687, '切り崩す': 8688, '旨味': 8689, '尽力': 8690, '黙っ': 8691, '起業家': 8692, '裁判官': 8693, '法人登記': 8694, '名義': 8695, '飲食店': 8696, 'トレガチ': 8697, '外食': 8698, '手軽': 8699, 'タンパク質': 8700, '天神': 8701, '対話': 8702, '提起': 8703, '引き起こす': 8704, '行動基準': 8705, '攻略方法': 8706, '正確': 8707, '戦慄': 8708, 'nGamerTeach': 8709, 'なきゃ': 8710, '歩き': 8711, '野菜': 8712, 'とれ': 8713, '非の打ち所': 8714, '食品': 8715, '日本中': 8716, '女子高生': 8717, 'タクシー': 8718, '偏差': 8719, '値': 8720, '翌日': 8721, '浅く': 8722, 'チーム全体': 8723, '視覚': 8724, 'たか': 8725, '一目': 8726, 'ソルマクゼニルシ': 8727, 'かない': 8728, '解釈': 8729, '堪え': 8730, '足ん': 8731, 'なかろ': 8732, 'angs': 8733, 'キングダム': 8734, 'わんちゃん': 8735, '狙お': 8736, 'トライ': 8737, 'オモシレー': 8738, 'ホッグウルト': 8739, '妨害': 8740, '収穫': 8741, '貼っ': 8742, '叩き': 8743, '割っ': 8744, 'グレネード': 8745, '細か': 8746, '見直し': 8747, 'ラスティー': 8748, '弾い': 8749, 'ゴッツンコ': 8750, '作り出し': 8751, 'ジェットスター': 8752, 'スカイマーク': 8753, '往復': 8754, '金額': 8755, 'のる': 8756, 'イースポ': 8757, '日間': 8758, '大天使': 8759, '立ち止まっ': 8760, 'ぶっ殺す': 8761, '打ち込む': 8762, 'mickie': 8763, '苦し': 8764, 'キャリアハイ': 8765, '上げれ': 8766, '付与': 8767, 'LOS': 8768, '標準': 8769, '鬱': 8770, 'ーーーーー': 8771, '平穏': 8772, '戻る': 8773, '主要': 8774, 'だー': 8775, 'モット': 8776, '火影': 8777, 'wave': 8778, 'あきち': 8779, '無効': 8780, 'チクチク': 8781, '一ダ': 8782, 'イブ': 8783, '出会っ': 8784, 'towe': 8785, 'スケジュール': 8786, 'リプ': 8787, '助け': 8788, '泊まる': 8789, 'ようがし': 8790, 'なか': 8791, 'ろう': 8792, '取り敢えず': 8793, 'とけ': 8794, '不相応': 8795, '怖く': 8796, '取り返す': 8797, 'current': 8798, 'max': 8799, 'tier': 8800, 'ルシオピック': 8801, '何とも': 8802, '防衛': 8803, '上と下': 8804, 'シーズン中': 8805, '起こす': 8806, '一点集中': 8807, 'rjm': 8808, 'ささ': 8809, '撃っ': 8810, '瓶': 8811, '物質': 8812, 'ゴリラザリア': 8813, 'つつ': 8814, '線': 8815, '向かい合っ': 8816, '木の葉返し': 8817, 'あう': 8818, 'オンファイア': 8819, '驚き': 8820, '副': 8821, '職': 8822, 'AV男優': 8823, 'ルシオキャリー': 8824, '地力': 8825, '備忘録': 8826, 'ゲンジメイン': 8827, 'グロ': 8828, 'エリ': 8829, '防ぐ': 8830, '人間業': 8831, 'にゅー': 8832, 'よーく': 8833, '攻めろ': 8834, 'いったん': 8835, 'なおせ': 8836, 'はか': 8837, 'お願い': 8838, 'サッサウィンストン': 8839, '素': 8840, '射っ': 8841, 'いたん': 8842, 'キングスロウザリア': 8843, '付き': 8844, 'くらわし': 8845, '消さ': 8846, '様子': 8847, '夫': 8848, 'しかも': 8849, '数える': 8850, '戦前': 8851, '甘え': 8852, 'タコ殴り': 8853, '快感': 8854, 'しゃべら': 8855, 'ルシオラジオ': 8856, 'ドロップ': 8857, 'ざび': 8858, 'はやる': 8859, 'EnvuUs': 8860, '息': 8861, 'ネクスト': 8862, 'ウィンストンバフマジ': 8863, 'whoru': 8864, 'フアイウ': 8865, 'るな': 8866, 'うぇい': 8867, 'ちゅ': 8868, 'よいー': 8869, '合わさっ': 8870, '惜しん': 8871, 'rip': 8872, 'フルチャージオーブ': 8873, '全弾命中': 8874, '着い': 8875, 'マーシーブースト': 8876, '一撃': 8877, '刈り取ら': 8878, 'シールド': 8879, '貫通': 8880, '何気に': 8881, '近づく': 8882, 'フランカー': 8883, '疑っ': 8884, '連': 8885, 'ザリアハルト': 8886, '幅広く': 8887, '捨てる': 8888, 'ツイートマジ': 8889, '通る': 8890, 'いれる': 8891, '素質': 8892, 'ついてん': 8893, 'フリーター': 8894, 'ゅお': 8895, '直ん': 8896, '週末': 8897, 'ｐ': 8898, 'ｖ': 8899, 'きる': 8900, '自衛': 8901, 'エグイ': 8902, '共産党': 8903, '隔離': 8904, 'スパムエロサイト': 8905, '踏ん': 8906, 'めんどくさく': 8907, 'ケータイ': 8908, 'お姉さん': 8909, '察し': 8910, 'reddit': 8911, '穴': 8912, '埋める': 8913, '人気ブログ': 8914, '特盛': 8915, '一致': 8916, '団結': 8917, '高低': 8918, 'ゼルダ': 8919, '要': 8920, 'メイウルト': 8921, '貯まる': 8922, 'どうく': 8923, 'よみ': 8924, 'とり': 8925, 'QuakeLive': 8926, 'エースコンバット': 8927, '無双': 8928, 'オナニー': 8929, 'おでん': 8930, 'キムチ': 8931, 'さん家': 8932, '下がり': 8933, 'ループ': 8934, 'カジュアルゲー': 8935, 'もみないっ': 8936, 'マスオバ': 8937, '越える': 8938, '絞ら': 8939, '後続': 8940, 'だり': 8941, '0月0日': 8942, 'Open': 8943, 'Division': 8944, 'ファミ通': 8945, 'における': 8946, 'Openrec': 8947, '仕組': 8948, 'みなのか': 8949, '虹': 8950, '継続的': 8951, '鍛える': 8952, '入場': 8953, '料っ': 8954, 'ほんの': 8955, 'ノウハウ': 8956, '無意識': 8957, 'ぱ': 8958, '平凡': 8959, '実銃': 8960, '打ちまくり': 8961, '月末': 8962, 'Whoru': 8963, '手裏剣': 8964, 'プラス': 8965, '沈め': 8966, 'どっ': 8967, 'talespin': 8968, 'シーズンハイマスター': 8969, '地域': 8970, '求': 8971, 'アサルトマップ': 8972, 'レディット': 8973, 'パスポート': 8974, 'レベリング': 8975, 'ごちゃごちゃ': 8976, 'アイアンクラッド': 8977, '自分たち': 8978, '押し付け': 8979, 'うめる': 8980, 'ンァー': 8981, 'フィニッシュ': 8982, 'スタート': 8983, '龍撃剣': 8984, '振る': 8985, '残': 8986, '射': 8987, '打ち合う': 8988, 'アサブロンズバスティオン': 8989, '突破': 8990, 'ワンマッチ': 8991, '淡々': 8992, '試合前': 8993, '頑張ろ': 8994, 'ワンポイント': 8995, 'してやり': 8996, 'iddqd': 8997, 'Q': 8998, '地区': 8999, '全勝': 9000, '正に': 9001, '体現': 9002, 'nV': 9003, '中0': 9004, '指名': 9005, '舐め': 9006, '錚々たる': 9007, 'Best': 9008, 'スッゲー': 9009, '対峙': 9010, 'ちくり': 9011, '位置取り': 9012, '神剣': 9013, '鍛え': 9014, 'ボロ': 9015, '直さ': 9016, '鈍っ': 9017, 'テンションキレキレ': 9018, '履歴': 9019, '監視': 9020, '判明': 9021, 'ハクサルゲンジ': 9022, '部門': 9023, 'プロゲーミング': 9024, '広報官': 9025, 'mendo': 9026, '笑顔': 9027, 'uncia': 9028, '粘っ': 9029, 'かよく': 9030, '間下': 9031, 'したたか': 9032, 'ゲンジウィンストン': 9033, 'ahp': 9034, '辛かっ': 9035, '爽やか': 9036, 'warrock': 9037, '経過': 9038, '文化的': 9039, '資本': 9040, 'プライベート': 9041, '暴い': 9042, 'ポジティブ': 9043, '中田': 9044, 'はいい': 9045, '手っ取り早い': 9046, 'はちま': 9047, 'なぞ': 9048, 'むって': 9049, '再来': 9050, 'むさん': 9051, '燃え上がら': 9052, 'jespa': 9053, 'たたい': 9054, '売名': 9055, '絡む': 9056, 'アンランクド': 9057, '乱れる': 9058, '戦場': 9059, '早起き': 9060, '出れ': 9061, '宿泊': 9062, '観客': 9063, '損し': 9064, '反故': 9065, '出場': 9066, '呟け': 9067, '裏話': 9068, 'ハイセンシローセンシ': 9069, '抽象': 9070, '待った': 9071, 'テリトリー': 9072, '狭': 9073, '全般': 9074, 'ブログパク': 9075, 'フリーライド': 9076, '翻訳ブログ': 9077, '一儲け': 9078, '土台': 9079, '差し': 9080, '込める': 9081, '純正': 9082, 'GearVR': 9083, 'Iphone': 9084, '目覚める': 9085, '決めれ': 9086, 'コンピューター': 9087, '集合体': 9088, 'ただただ': 9089, 'つなげる': 9090, 'マイナス': 9091, '伝播': 9092, '向ける': 9093, '怖いっ': 9094, 'Arctis': 9095, '眺める': 9096, '絡ま': 9097, '深淵': 9098, '出来事': 9099, '0km': 9100, '漕い': 9101, '年前': 9102, '懐かしい': 9103, 'シャ': 9104, 'ター': 9105, 'キメる': 9106, '有無': 9107, '浮き彫り': 9108, '帳消し': 9109, 'つめ': 9110, 'かて': 9111, '賭け': 9112, '悪いこと': 9113, 'エロイプ': 9114, '晒さ': 9115, '新チーム': 9116, '数百人': 9117, '客席': 9118, 'ガラガラ': 9119, '予選': 9120, 'コメント欄': 9121, '煎じ': 9122, 'どう役': 9123, 'チーターウイドウ': 9124, '訴求力': 9125, 'センシ': 9126, '殺せ': 9127, 'しらす': 9128, 'ぱん': 9129, 'まかせる': 9130, 'コンボ': 9131, 'ヘリックス': 9132, '斬り': 9133, 'ハルトライフ': 9134, '睨み合っ': 9135, '張り': 9136, 'がいいん': 9137, 'ボディフィットモデル': 9138, 'ステロイド': 9139, '分かる': 9140, '紅白': 9141, 'モラトリアム': 9142, 'N0': 9143, 'スタンミ': 9144, 'バンバンスクリム': 9145, 'うけ': 9146, '通算': 9147, '坊主': 9148, '早々': 9149, '遡ら': 9150, '受講': 9151, '着け': 9152, '広告代理店': 9153, '通さ': 9154, 'GO': 9155, '先行者': 9156, 'ずけ': 9157, 'やりかた': 9158, '競合': 9159, '達成': 9160, '遅かっ': 9161, '実は': 9162, 'そろい': 9163, '一喜一憂': 9164, 'ぴするほうが': 9165, '終わろ': 9166, '計画的': 9167, 'ウィンストンゲンジ': 9168, 'インフィニティ': 9169, 'レイコータワー': 9170, 'バシバシ': 9171, 'きらい': 9172, '人達': 9173, '後に': 9174, '発覚': 9175, '違約': 9176, '請求': 9177, '参加者': 9178, 'ローソン': 9179, 'セレクト': 9180, 'あたりめ': 9181, '受験生': 9182, 'ゲーミングPC': 9183, '引き離し': 9184, 'レイスフォーム': 9185, '波': 9186, '止まる': 9187, 'クールタイム': 9188, 'くさ': 9189, 'こか': 9190, '後手': 9191, '使いこなせる': 9192, '放り込ま': 9193, '組める': 9194, 'フォーオナー': 9195, '合格': 9196, '志望': 9197, '受かっ': 9198, 'アタッカー': 9199, '趣': 9200, '回転速度': 9201, 'うまけれ': 9202, 'ave': 9203, '打てれ': 9204, 'スノーボール': 9205, '回復アイテム': 9206, '散策': 9207, '待ち構える': 9208, '乗り越え': 9209, 'こけ': 9210, '脳汁': 9211, '保持': 9212, 'お見合い': 9213, 'ぼろ': 9214, '本格的': 9215, '円形': 9216, '遮ら': 9217, '進路': 9218, 'ーーー': 9219, '所詮': 9220, '補助輪': 9221, '当てはめ': 9222, '弟': 9223, '課せ': 9224, '迫る': 9225, '前半': 9226, 'ーーーー': 9227, 'コリアンランカーマクリー': 9228, 'しかた': 9229, 'デトゴールド': 9230, '真正面': 9231, 'どおり': 9232, 'スコープ': 9233, '不合理': 9234, 'ケツメイシ': 9235, '概要': 9236, '尊重': 9237, 'ペチペチ': 9238, 'ひいては': 9239, '決定力': 9240, 'たまり': 9241, 'マルチキル': 9242, '合わせる': 9243, '対抗': 9244, '策': 9245, '任せ': 9246, 'ヒーローランクマ': 9247, '先攻': 9248, 'サドンデス': 9249, 'サンマボット': 9250, 'に当たって': 9251, 'いたっ': 9252, 'ぼっ': 9253, 'おちんちん': 9254, '恵まれる': 9255, 'イリオス': 9256, 'コントロールシンメ': 9257, 'やりゃ': 9258, 'おまえら': 9259, 'ごみ': 9260, 'めん': 9261, '止まり': 9262, '後者': 9263, '前者': 9264, 'oversumo': 9265, 'エース': 9266, '紅茶': 9267, '寝落ち': 9268, 'もしも': 9269, '機械になりたい': 9270, '連れ': 9271, '治る': 9272, '風邪': 9273, '弱っ': 9274, '体調': 9275, 'カゼ': 9276, '俺氏': 9277, 'overwatcher': 9278, '中距離': 9279, 'ファニングブッパ': 9280, 'リグループ': 9281, '大嘘': 9282, 'キリキリキリキリ': 9283, '寒': 9284, '雪': 9285, 'ひまし': 9286, '疾風': 9287, 'ヘビーローテーション': 9288, 'パイプ': 9289, '配管': 9290, 'ニンジャ': 9291, '取りつかれ': 9292, 'まいまい': 9293, '麻薬': 9294, '下がろ': 9295, '追いつめ': 9296, '追いかける': 9297, '疎通': 9298, '脛': 9299, 'かじっ': 9300, 'ズルズル': 9301, 'チェックポイント': 9302, 'wpg': 9303, '曲がり角': 9304, '当たろ': 9305, '狩ら': 9306, 'あな': 9307, 'あのまま': 9308, '押し込ま': 9309, 'shadowburn': 9310, 'クレイジー': 9311, '知れ': 9312, 'カウント': 9313, '張る': 9314, 'まる': 9315, 'ult': 9316, 'daradara': 9317, '分量': 9318, 'det': 9319, 'パトカー': 9320, '鍵': 9321, '奪っ': 9322, 'ノコノコ': 9323, '地面': 9324, '突き抜け': 9325, '安らぐ': 9326, '軽減': 9327, 'ナノバスティオン': 9328, '撃た': 9329, '加算': 9330, 'ナノタンクモード': 9331, '日本国内': 9332, 'urca': 9333, 'samuraiD': 9334, 'DNG': 9335, '混乱': 9336, 'DNT': 9337, '0期メンバー': 9338, '0軍': 9339, '一軍': 9340, '二軍': 9341, 'アツイ': 9342, 'エイムガバガバ': 9343, 'パンツ一丁': 9344, 'cpu': 9345, '突き抜ける': 9346, '挑む': 9347, '嬲り': 9348, 'チャットオフ': 9349, '命中': 9350, 'ハッカー': 9351, '走っ': 9352, 'ローディング': 9353, '着信': 9354, '防弾': 9355, 'ヘルメット': 9356, 'スナイパーライフル': 9357, 'ゲット': 9358, 'すん': 9359, 'ok': 9360, '防弾チョッキ': 9361, 'ak': 9362, 'ar': 9363, '学名': 9364, 'Ryzen': 9365, '0GB': 9366, '0W': 9367, '妥協': 9368, '主体': 9369, 'MAC': 9370, '勝者総取り': 9371, 'PJS': 9372, '土俵': 9373, 'アマチュアチーム': 9374, '設立': 9375, '進む': 9376, '常勤': 9377, '職員': 9378, '能っ': 9379, '売上高': 9380, 'それだけ': 9381, 'NPO法人': 9382, '募っ': 9383, '定着': 9384, '読み': 9385, 'コントロールハルト': 9386, '春節': 9387, 'イベ': 9388, 'つっこみ': 9389, '冷た': 9390, '吐く': 9391, 'はこ': 9392, '見つかる': 9393, 'お世辞': 9394, 'ナノブガンガン': 9395, '未払い': 9396, 'ひじ': 9397, '組む': 9398, '連敗': 9399, '変わろ': 9400, 'ぶっ飛ばし': 9401, 'ディープコピー': 9402, 'シャローコピー': 9403, '激臭': 9404, 'ネームクラン': 9405, '刻み': 9406, 'はやく': 9407, 'エターナル': 9408, '右上': 9409, 'ゲンジゴリラ': 9410, '襲っ': 9411, '聴覚': 9412, '頼り': 9413, '識別': 9414, 'スワップ': 9415, '交戦': 9416, 'combox': 9417, '豚': 9418, 'faker': 9419, 'すごっ': 9420, 'けた': 9421, 'いまさら': 9422, '元気': 9423, 'イースポーツ': 9424, 'ゲキ': 9425, '臭': 9426, '試合内容': 9427, '溢れる': 9428, '集めよ': 9429, '中間層': 9430, '一月': 9431, '珍しいっ': 9432, '写輪眼': 9433, '開花': 9434, 'リラックスエイム': 9435, 'ラピッドツイッチエイム': 9436, 'ザリアソルジャー': 9437, 'Word': 9438, '霊': 9439, '圧': 9440, 'ウルトバンバン': 9441, 'ナノハルト': 9442, 'サージナノハルト': 9443, '如何': 9444, 'きまっ': 9445, 'ザリゴリ': 9446, 'ザリハルト': 9447, 'シナジーマジ': 9448, 'winwin': 9449, '構える': 9450, 'ザリアメイン': 9451, '配分': 9452, '弾薬': 9453, 'ずらす': 9454, 'ヘラ': 9455, 'ザリアマジ': 9456, 'ステレオ': 9457, 'ミキサー': 9458, '聞ける': 9459, 'マイクミュート': 9460, '申し訳な': 9461, 'いらいら': 9462, 'Discorf': 9463, 'ならん': 9464, 'xl': 9465, 'ナイトオウル': 9466, '取り分': 9467, 'タブ': 9468, 'おそう': 9469, '苦肉の策': 9470, '互角': 9471, 'チョコ': 9472, 'ピックガイジ': 9473, '妙': 9474, 'イタ飯': 9475, '自傷行為': 9476, '食べに': 9477, 'られれ': 9478, 'ブリーザー': 9479, 'ナン': 9480, 'パー': 9481, 'うって': 9482, 'フレーム': 9483, '動作': 9484, '完了': 9485, '撮れ': 9486, '解析': 9487, '月曜': 9488, 'なにより': 9489, 'クローズ': 9490, 'きく': 9491, '見やすし': 9492, '個々': 9493, 'マダ': 9494, 'むかい': 9495, '落とせ': 9496, '①': 9497, '②': 9498, '足元': 9499, '③': 9500, '確立': 9501, '説得力': 9502, '挙げれ': 9503, '活かし': 9504, 'まっとう': 9505, '従っ': 9506, '筋合い': 9507, 'いかなる': 9508, 'ウイドゥ': 9509, 'お達し': 9510, '渋々': 9511, '異文化交流': 9512, 'ハンゾーゲンジ': 9513, '言ってはいけない': 9514, 'むやみ': 9515, '割り切っ': 9516, '押しつけよ': 9517, 'まぁ': 9518, '根底': 9519, '共感': 9520, 'もとめ': 9521, '慰める': 9522, '保て': 9523, '見比べ': 9524, '上位互換': 9525, 'ヨッピー': 9526, 'モテる': 9527, 'ふーん': 9528, '中高生': 9529, 'ビビッ': 9530, 'コリアンゲンジ': 9531, '攻守': 9532, '女性問題': 9533, '女性関係': 9534, 'ディー': 9535, 'あるく': 9536, '取り戻す': 9537, '強引': 9538, '笑わせ': 9539, 'つかめ': 9540, 'もどせる': 9541, 'ヒーローツートップ': 9542, '類': 9543, 'HAYAKU': 9544, 'SA': 9545, 'ZI': 9546, 'UTTE': 9547, 'マクソ': 9548, '脅威': 9549, 'つまらない': 9550, 'PING': 9551, '黒人奴隷': 9552, 'ｓ': 9553, '加えよ': 9554, 'とめ': 9555, 'ザリアバリア': 9556, '宿': 9557, 'やらかし': 9558, 'パット': 9559, 'Mid': 9560, 'Xsoft': 9561, '硬さ': 9562, '触る': 9563, 'nFK': 9564, 'ブンブン': 9565, '振り回し': 9566, '乗り換え': 9567, 'ZA': 9568, 'Rival': 9569, 'pure': 9570, 'nArtisan': 9571, 'さわれ': 9572, 'たのも': 9573, '触り': 9574, '日頃': 9575, '衝突': 9576, '地点': 9577, 'ちんこ': 9578, '村田': 9579, '先生': 9580, '傑作': 9581, 'pi': 9582, 'ng0': 9583, '調子': 9584, '不自由': 9585, 'ワンコン': 9586, '格': 9587, '殺': 9588, '凍結': 9589, '愛情': 9590, '親密さ': 9591, '調和': 9592, '自意識': 9593, 'ロボット': 9594, '給与': 9595, 'たせ': 9596, '部下': 9597, '嫌う': 9598, '聞けば聞くほど': 9599, 'レガシー': 9600, '買い叩か': 9601, 'いびつ': 9602, '近年': 9603, '0代': 9604, '変わり': 9605, 'sudo': 9606, '民間': 9607, '淘汰': 9608, '霞が関': 9609, '官僚': 9610, '低学歴': 9611, '地方自治体': 9612, '高卒': 9613, '職種': 9614, '情報系': 9615, '課程': 9616, 'いまだに': 9617, '強い力': 9618, '日本郵政': 9619, '時価総額': 9620, 'nSaaS': 9621, '霞ヶ関': 9622, '社内': 9623, '自然言語処理': 9624, 'Python': 9625, '士農工商': 9626, 'プログラマー': 9627, 'ケーブル': 9628, '長さ': 9629, '摩擦': 9630, 'アウト': 9631, 'Instagram': 9632, '抽出': 9633, '顔面偏差値': 9634, 'Facemash': 9635, 'サーフィン': 9636, '補助': 9637, 'インターフェース': 9638, 'まね': 9639, '裾野': 9640, '広げる': 9641, '無給': 9642, 'Tfue': 9643, 'Tokyo': 9644, 'Meetup': 9645, 'ミリ秒': 9646, 'nping': 9647, '精密': 9648, '言いふらし': 9649, '大会出場': 9650, '一丸': 9651, 'フォース': 9652, '精神力': 9653, 'ザリアハルトルシオアナ': 9654, '橋上': 9655, 'ogn': 9656, 'kongdoo': 9657, '村社会': 9658, '落ち着き': 9659, '複合': 9660, 'アラ': 9661, 'けなし': 9662, 'そなえ': 9663, '刺激的': 9664, '狩': 9665, 'けっこう': 9666, 'エセダイヤ': 9667, 'はほん': 9668, 'TAB': 9669, '押そ': 9670, 'タイムアタック': 9671, '大声': 9672, 'ブルーハーツ': 9673, '歌い': 9674, 'バイク': 9675, '中二': 9676, '朝練': 9677, 'スパルタゲーマー': 9678, '怖': 9679, 'kenkyu': 9680, 'kitui': 9681, 'natama': 9682, 'ga': 9683, 'kowareru': 9684, 'ええ': 9685, 'ゅごい': 9686, '記憶力': 9687, 'たっての': 9688, 'コラボ': 9689, '在校生': 9690, '日時': 9691, 'あわ': 9692, 'エスカ': 9693, 'rei': 9694, 'nforce': 9695, '確保': 9696, 'マク': 9697, 'バイオテック': 9698, '置か': 9699, 'ran': 9700, 'ra': 9701, '倒せ': 9702, '信ぴょう性': 9703, 'ＴＬ': 9704, 'にぎわっ': 9705, 'ザリアウルト': 9706, 'はよう': 9707, '嬉しく': 9708, 'ザリアハルトホッグアナルシオ': 9709, 'ナノガッチュー': 9710, '残せる': 9711, 'ガキ': 9712, 'ゆる': 9713, 'パンダ': 9714, '滑っ': 9715, 'ビクッと': 9716, 'ほしみ': 9717, 'サッカー日本代表': 9718, '酒井高徳': 9719, '日本の常識': 9720, 'この国': 9721, 'ノリノリ': 9722, 'アナカットー': 9723, '理解不能': 9724, '寛容': 9725, '喜ん': 9726, '何も言わずに': 9727, 'もめ': 9728, '内乱': 9729, '始まら': 9730, 'こる': 9731, 'アサルトマジ': 9732, 'ライバルプレイ': 9733, 'つかう': 9734, '有効活用': 9735, 'オールマイティ': 9736, 'ピンポイント': 9737, 'ロードホッグ': 9738, '人少な': 9739, '破壊': 9740, '致命': 9741, '法': 9742, 'ソンブラマジ': 9743, '慎重': 9744, 'ぼる': 9745, 'スカ': 9746, 'ハルトハック': 9747, '逃げ惑う': 9748, '打ちまくる': 9749, 'ソンブラライバル': 9750, 'たき': 9751, 'ランクマソンブラ': 9752, 'かじゃ': 9753, '身内': 9754, '贔屓': 9755, 'クズ': 9756, '罵る': 9757, 'npt': 9758, '役立た': 9759, '罵ら': 9760, '滝廉太郎': 9761, 'ワンヒーラーデフォ': 9762, 'ノーヒーラー': 9763, '闇': 9764, '0mm': 9765, 'ハンドグリッパーニギニギ': 9766, 'nzowie': 9767, 'Price': 9768, 'Functions': 9769, 'Specification': 9770, 'Looks': 9771, '大学0年生': 9772, '光らせる': 9773, '光れ': 9774, 'かえる': 9775, '爆睡': 9776, '泊まっ': 9777, '困ら': 9778, 'タフ': 9779, 'ほぼほぼ': 9780, 'スペ': 9781, '最低条件': 9782, '小売り': 9783, 'nEA': 9784, '遠い': 9785, '手探り': 9786, 'nコン': 9787, 'トレゲンザリ': 9788, 'ごり': 9789, '電気屋': 9790, 'ROCCAT': 9791, 'KONEPURE': 9792, 'サイズ': 9793, 'njp': 9794, '活発': 9795, '動ける': 9796, '利く': 9797, 'チマチョゴリ': 9798, '専用': 9799, 'スイスロリッシュ': 9800, 'ロードホガーズ': 9801, '祝日': 9802, '頼み': 9803, '否め': 9804, 'ゴリゴリキル': 9805, '狙える': 9806, '奪い取っ': 9807, '高揚': 9808, 'あがら': 9809, 'サンプラス': 9810, 'フェデラー': 9811, 'ロディック': 9812, 'ヒューイット': 9813, '四大大会': 9814, 'ベスト0': 9815, '錦織': 9816, 'ニュース': 9817, '歯': 9818, '不便': 9819, '病気': 9820, '歯医者': 9821, '虫歯': 9822, '治療': 9823, '要望': 9824, 'ごっちゃ': 9825, '雇える': 9826, '潤う': 9827, '換え': 9828, '嘆い': 9829, 'BLeague': 9830, 'ドリームジョブ': 9831, '薄給': 9832, '興行': 9833, 'クラロワ': 9834, '洗練': 9835, '課金システム': 9836, '操作性': 9837, '類似': 9838, '算出': 9839, 'ネットゲーム': 9840, 'やすさ': 9841, 'さらなる': 9842, '課題解決': 9843, 'つなげ': 9844, '原動力': 9845, 'くるしめ': 9846, 'くちゃ': 9847, 'nLTV': 9848, 'デジタルマーケティング': 9849, 'BEE': 9850, 'nhgbsun': 9851, 'FOX': 9852, 'RABBIT': 9853, 'および': 9854, 'なろう': 9855, 'ツヨ': 9856, '貯めよ': 9857, '速さ': 9858, '作ろ': 9859, 'ベルディ': 9860, '生き残っ': 9861, '受け身': 9862, '先手': 9863, '専業': 9864, 'ぱく': 9865, 'スロウ': 9866, '早め': 9867, '当方': 9868, '貼ら': 9869, 'よね': 9870, '仕上がる': 9871, 'Hz': 9872, '通信': 9873, '進歩': 9874, 'かたい': 9875, '短': 9876, '萌え声': 9877, 'kawaii': 9878, 'バズる': 9879, 'PostTruth': 9880, '得て': 9881, '腐る': 9882, '重要視': 9883, '先見': 9884, '大切なこと': 9885, 'どんなに': 9886, '顧客': 9887, '気づけ': 9888, 'あがる': 9889, '与': 9890, 'こわい': 9891, 'キャラメルマキアート': 9892, 'つまむ': 9893, 'スカッと': 9894, 'rankuma': 9895, 'yaru': 9896, 'setsumei': 9897, 'dekinai': 9898, 'kono': 9899, 'yabasa': 9900, 'ato': 9901, 'zikan': 9902, '定量的': 9903, '調べろ': 9904, 'マジﾑﾘﾎﾟﾖ': 9905, 'かぶる': 9906, '取り返そ': 9907, '時に': 9908, 'おかしかっ': 9909, '客観': 9910, '系列': 9911, '初期メンバー': 9912, '競技人口': 9913, 'ロスター': 9914, '一秒': 9915, '窓': 9916, '体い': 9917, '真中': 9918, 'モロ': 9919, 'ウイドウメタ': 9920, '浮かば': 9921, 'ださん': 9922, 'ザンギ': 9923, 'リュウ': 9924, '読み替え': 9925, '汗': 9926, '仲': 9927, '良かろ': 9928, 'ゴミクソ': 9929, '責め': 9930, 'true': 9931, 'erite': 9932, '院試': 9933, 'し役': 9934, '握り': 9935, '錯覚': 9936, 'ちぐはぐ': 9937, '属し': 9938, 'たいてい': 9939, '排除': 9940, 'ボーダーレス': 9941, 'となりのヤングジャンプ': 9942, 'アナワンキル': 9943, '雲': 9944, 'ソルジャーウルト': 9945, '昼夜': 9946, '拮抗': 9947, '暗い': 9948, '昨日今日': 9949, 'ちまちま': 9950, 'フルパワーザリア': 9951, 'ガハハ': 9952, 'ｗｗOPww': 9953, 'ソロランクマ': 9954, 'フラグ': 9955, 'ムービー': 9956, '焼き': 9957, '教養': 9958, 'キャンパス': 9959, 'qck': 9960, '中国製': 9961, 'ローコストマウスパッド': 9962, '信者': 9963, '零': 9964, '特注': 9965, 'クソデカマウスパッド': 9966, '頼も': 9967, 'aim': 9968, 'ハル': 9969, 'ト殺': 9970, 'naim': 9971, 'こりゃ': 9972, 'Ftier': 9973, '竜神': 9974, 'シャンシャン': 9975, '切る': 9976, 'ハイライト': 9977, 'コマ': 9978, 'ソンブラコ': 9979, 'すき焼き': 9980, '言お': 9981, 'haruto': 9982, 'akita': 9983, 'nzarya': 9984, 'de': 9985, 'korosi': 9986, 'makuri': 9987, 'tai': 9988, '飯テロ': 9989, '祭り': 9990, 'かくて': 9991, '東京ドーム': 9992, 'チャリ通': 9993, '歩か': 9994, '原付': 9995, 'くず': 9996, 'ちさ': 9997, '試さ': 9998, 'サイレント': 9999, 'ジャンル': 10000, '待た': 10001, 'チャ': 10002, 'パワー': 10003, '計っ': 10004, 'よめる': 10005, '第一宇宙速度': 10006, 'あけ': 10007, 'た次元': 10008, '超越': 10009, '刑務所': 10010, '高0': 10011, '八月': 10012, '組み立て': 10013, '割ら': 10014, '別々': 10015, 'それや': 10016, '召喚': 10017, '見合い': 10018, '削る': 10019, 'リザレクト': 10020, 'ガンガンキル': 10021, 'Planetoverwatch': 10022, '抜粋': 10023, 'あくまでも': 10024, '私自身': 10025, '私見': 10026, 'スペシャリスト': 10027, '押し上げ': 10028, '富ん': 10029, 'コンポジション': 10030, 'トーナメント': 10031, 'もたらし': 10032, '支持': 10033, 'シャドー': 10034, '暴れまくる': 10035, '先取': 10036, '取り返さ': 10037, '最終ラウンド': 10038, '言い出す': 10039, 'メンタルブロンズ': 10040, '分から': 10041, '戻す': 10042, 'レートクソ': 10043, 'たのしー': 10044, 'www': 10045, '加速装置': 10046, '音速': 10047, '谷内': 10048, 'やせ': 10049, '成人式': 10050, '市長': 10051, '警備員': 10052, '踊っ': 10053, 'ばれ': 10054, 'ツイ廃': 10055, '楽しま': 10056, '判断力': 10057, '平面': 10058, 'すむ': 10059, 'fe': 10060, 'it': 10061, '内戦': 10062, 'おもろかっ': 10063, 'ルリウム': 10064, 'くみ': 10065, 'アナハルトバン': 10066, 'こおる': 10067, '州民': 10068, '繋がる': 10069, '遊ぼ': 10070, '見分け': 10071, 'n女': 10072, 'ラグスイッチ': 10073, 'ラグチーター': 10074, '無修正': 10075, 'スクリムショウ': 10076, 'BOSS': 10077, '一睡': 10078, '生活リズム': 10079, 'アンドエネルギーチャージ': 10080, '姫': 10081, '囲わ': 10082, '要求': 10083, '万国': 10084, '試合開始': 10085, '無事': 10086, '死亡': 10087, 'こわから': 10088, 'マーラインハルト': 10089, '貯めろ': 10090, '音量': 10091, '拾う': 10092, '話さ': 10093, '行きたくない': 10094, 'ござる': 10095, 'タンクウォッチ': 10096, 'ばくばく': 10097, '強制的': 10098, '陳腐': 10099, '入学': 10100, '平成': 10101, '思い出そ': 10102, '年号': 10103, 'なくし': 10104, 'スパゲッティ': 10105, 'いやー': 10106, '心地': 10107, 'se': 10108, 'ubk': 10109, '周辺機器': 10110, 'パズドラ': 10111, '廃': 10112, '人笑': 10113, '人みん': 10114, '利点': 10115, 'からいっ': 10116, 'たほう': 10117, '無名': 10118, 'お菓子': 10119, '食わ': 10120, '見えない敵': 10121, '引き寄せ': 10122, '丸腰': 10123, '全裸': 10124, '繰り出さ': 10125, '珍妙': 10126, '練習量': 10127, '全世界': 10128, 'aimbot': 10129, '施行': 10130, '犯す': 10131, 'いたちごっこ': 10132, 'ngg': 10133, '年越': 10134, '翌': 10135, '落': 10136, '◯': 10137, '自発': 10138, 'シャッター': 10139, '払え': 10140, '遊べ': 10141, '防ぎ': 10142, '切ら': 10143, '心拍数': 10144, 'キャプチャ': 10145, 'PrintScreen': 10146, 'おして': 10147, 'window': 10148, '付属': 10149, 'ペイント': 10150, 'ctrl': 10151, 'V': 10152, '動画キャプチャ': 10153, 'お気楽': 10154, 'めろ': 10155, '落ち着か': 10156, 'W': 10157, '微': 10158, 'エイムボットチーター': 10159, '沸い': 10160, '褐色': 10161, 'エロ': 10162, '魔人': 10163, '石碑': 10164, 'twitterアカウント': 10165, '安価': 10166, '化石': 10167, '半永久': 10168, 'ToS': 10169, '話しかける': 10170, '買い換えれ': 10171, 'モニタ': 10172, 'Realforce': 10173, '刑事': 10174, '大晦日': 10175, '脳味噌': 10176, '沸騰': 10177, '0連敗': 10178, '二月': 10179, '裏切り': 10180, 'ランクマクソ': 10181, 'nVC': 10182, '運ゲー': 10183, 'あいて': 10184, '境目': 10185, '仲良く': 10186, 'こし': 10187, '夢中': 10188, '浪子': 10189, 'ゝ': 10190, 'ひい': 10191, 'おっち': 10192, 'サバ': 10193, 'かくする': 10194, '芸': 10195, '雪合戦': 10196, 'シンメ': 10197, 'ヒーローメイ': 10198, '取り返せる': 10199, '気づか': 10200, '品位': 10201, '貫き通し': 10202, 'みろ': 10203, '被害者': 10204, '見せよ': 10205, '途端': 10206, '凸': 10207, '言いだす': 10208, '絶頂': 10209, '譲っ': 10210, 'オナシャス': 10211, '譲る': 10212, 'ホールホッグ': 10213, '挨拶': 10214, 'ノン': 10215, 'ドーテロフ': 10216, '先月': 10217, 'いっす': 10218, 'ガイジガイジ': 10219, '引か': 10220, 'ボソボソ': 10221, '小言': 10222, '潰せる': 10223, '野生': 10224, 'ダイヤダイヤダイヤダイヤ': 10225, '道のり': 10226, 'Road': 10227, '街コン': 10228, 'クラブ': 10229, '装っ': 10230, '出会お': 10231, '親知らず': 10232, '歯列矯正': 10233, '歯並び': 10234, '治そ': 10235, '顎': 10236, '圧迫': 10237, 'ガタガタ': 10238, '知らず': 10239, '恐怖': 10240, 'エイムイ': 10241, 'プッシュトゥトーク': 10242, 'マイマイ': 10243, 'ハナムラ': 10244, 'クラウドファンディング': 10245, '募る': 10246, 'You': 10247, 'tube': 10248, 'レイヤー': 10249, 'abema': 10250, 'テレビレイヤー': 10251, '制作': 10252, 'ドキュメンタリー': 10253, '濃い': 10254, '携わっ': 10255, 'WOWOW': 10256, '年内': 10257, 'バイラル': 10258, 'Facebook': 10259, 'CAC': 10260, '告知': 10261, '瑣末': 10262, 'ミドル': 10263, '街': 10264, '山本一成': 10265, 'issei': 10266, 'y': 10267, '名人': 10268, 'Overhype': 10269, 'カレー': 10270, 'giveaway': 10271, '食いつく': 10272, '割に': 10273, '車内': 10274, '大安売り': 10275, '切り売り': 10276, '段落': 10277, 'nGG': 10278, 'コンパニオン': 10279, '会える': 10280, '年賀状': 10281, '人間らし': 10282, 'もがい': 10283, 'abara': 10284, '一段落': 10285, 'ああああああああああああああああああああああああああああああああああああ': 10286, 'ディズニー': 10287, 'ランド': 10288, 'ぶっこ': 10289, 'ゴッド': 10290, '飲む': 10291, 'たばこ': 10292, 'エンハンサー': 10293, '減り': 10294, 'なのっ': 10295, 'ぶちのめし': 10296, '凶暴': 10297, '動物': 10298, '森': 10299, 'みると': 10300, '交代': 10301, '制': 10302, '爆音': 10303, 'FF0': 10304, '限る': 10305, 'せろ': 10306, '戦し': 10307, 'キレイ': 10308, 'サーヴェイサーヴェイサーヴェイ': 10309, '可処分所得': 10310, 'お金がない': 10311, '揉ん': 10312, 'でかく': 10313, 'Cカップ': 10314, 'weblio': 10315, '英和辞典': 10316, 'Weblio': 10317, 'nnanotube': 10318, '⇨': 10319, 'ナノチューブ': 10320, '訳出': 10321, 'ペーパー': 10322, '腫れ': 10323, '頭痛': 10324, 'iGS': 10325, 'J0昇格': 10326, 'アビスパ': 10327, 'IGS': 10328, '代': 10329, 'Scrim': 10330, '持て': 10331, '外出禁止': 10332, '令': 10333, '台湾人': 10334, '00度': 10335, '回復力': 10336, '直せる': 10337, '一時期': 10338, 'インフルエンザ': 10339, '突発': 10340, '目処': 10341, '休止': 10342, 'いそがしく': 10343, '区切り': 10344, 'Hanjo': 10345, '査定': 10346, '仕様変更': 10347, 'シーズン0': 10348, '格段': 10349, '返っ': 10350, 'ハゲ': 10351, 'ロング': 10352, 'ビン': 10353, 'いれれ': 10354, '生き残れる': 10355, 'ハルトヒール': 10356, '一連の流れ': 10357, '珍': 10358, 'いたこと': 10359, '舐めプ': 10360, '架空': 10361, '人力': 10362, 'ever': 10363, 'more': 10364, '分布': 10365, 'ntier': 10366, '分かれ目': 10367, '塩漬け': 10368, 'あてる': 10369, 'FL': 10370, 'ゼニウルト': 10371, 'リュジェホンアナ': 10372, '撃ち': 10373, 'フットサル': 10374, '蹴る': 10375, 'がたい': 10376, '練習試合': 10377, '動かさ': 10378, '不健康': 10379, '近づける': 10380, 'Mickie': 10381, 'JOK': 10382, 'ER': 10383, 'バーストヒールエグ': 10384, 'なんとかなる': 10385, 'サイクロプスオーサカ': 10386, '足ら': 10387, '補充': 10388, 'せまい': 10389, 'よぉ': 10390, '鰤': 10391, 'ごめん': 10392, '不和のオーブ': 10393, 'アナゼニ': 10394, '叫ぶ': 10395, 'グダ': 10396, 'キルゴールド': 10397, '休憩': 10398, '厨': 10399, '置き去り': 10400, 'キツイ': 10401, 'イージーゲーム': 10402, 'Razer': 10403, 'BlackWidow': 10404, 'レス': 10405, 'ヒーローピックリスト': 10406, 'NaN': 10407, 'NaNNaN': 10408, 'vain': 10409, 'てま': 10410, '錯誤': 10411, '無力感': 10412, '悩まさ': 10413, '休み': 10414, '転職': 10415, '家族': 10416, '恐ろしく': 10417, 'おいそれと': 10418, '報わ': 10419, '活動資金': 10420, '繋げ': 10421, 'テニス': 10422, 'マジシャン': 10423, '世間': 10424, '恫喝': 10425, '儲から': 10426, 'スタンス': 10427, '働かそ': 10428, '居酒屋': 10429, '契約書': 10430, '金も': 10431, '最低': 10432, '若手': 10433, 'お笑い芸人': 10434, 'おもいこん': 10435, 'ラスティ': 10436, '不可': 10437, 'scrim': 10438, 'アマ': 10439, '射出': 10440, '放物線': 10441, '運動': 10442, '格闘技': 10443, '習得': 10444, '武芸': 10445, 'ファンボ': 10446, '告白': 10447, 'てんか': 10448, 'steelseries': 10449, 'sensei': 10450, 'ざす': 10451, '複垢': 10452, 'ヘッダー': 10453, 'rgb': 10454, 'ぽんぽん': 10455, '引きこもり': 10456, 'シカト': 10457, '安息': 10458, '他校': 10459, '毎晩': 10460, '一言': 10461, '中高': 10462, 'げーと': 10463, '根付か': 10464, 'チケット': 10465, '付く': 10466, '無料配信': 10467, 'esportsleague': 10468, '開幕': 10469, 'JLeague': 10470, '輸入': 10471, '代理店': 10472, '日本製品': 10473, 'eスポ': 10474, '産学官': 10475, '日本大学': 10476, 'ハイプ': 10477, 'Do': 10478, 'ta0': 10479, '上達': 10480, '根本': 10481, '障害者': 10482, 'パーソナライズ': 10483, '0Dプリンター': 10484, '学': 10485, 'グラム': 10486, '健常者': 10487, 'nJTB': 10488, 'nmame': 10489, '表記揺れ': 10490, 'eSports': 10491, '防御': 10492, '日大': 10493, '開催場所': 10494, 'インスタ': 10495, '叩きつけ': 10496, 'ビタミンC': 10497, 'がぶ飲み': 10498, '朝晩': 10499, 'のむ': 10500, 'GreenLeaves': 10501, 'むずくね': 10502, '使い物': 10503, '激しく': 10504, '縦横': 10505, 'いね': 10506, 'ぼろぼろ': 10507, 'SOFT': 10508, '体調不良': 10509, '栄養管理': 10510, '乗り切れる': 10511, '風引': 10512, '働ける': 10513, 'マルチビタミン': 10514, 'スペシャル': 10515, 'ＢＯＸ': 10516, 'てゆーか': 10517, 'ホッ': 10518, 'グ': 10519, 'ジェネレーター': 10520, 'nTwitter': 10521, '原文': 10522, 'シンメトラメタ': 10523, '戦わ': 10524, 'ところで': 10525, 'つかさ': 10526, 'キリッ': 10527, '儚く': 10528, '孕ん': 10529, 'さつき': 10530, '暴走': 10531, '内面': 10532, '描ける': 10533, 'いちご0': 10534, '作者': 10535, 'ラブコメ': 10536, '河下水希': 10537, '機微': 10538, '風邪ひき': 10539, 'IQ': 10540, '外人': 10541, 'コケ': 10542, '遊ば': 10543, '人集': 10544, 'めんば': 10545, '囲っ': 10546, '数こ': 10547, 'なるし': 10548, 'ヌァイイイス': 10549, '言いまくっ': 10550, '冷蔵庫': 10551, 'HP': 10552, 'Shadowburn': 10553, 'リクルート': 10554, '大手': 10555, '商社': 10556, '勝ち取っ': 10557, 'キャリア': 10558, '相談': 10559, '名乗る': 10560, 'か賞': 10561, '痛々しい': 10562, '移せる': 10563, 'きれいな': 10564, 'ひとつ': 10565, '怠っ': 10566, '酔っ': 10567, '定め': 10568, 'おいしく': 10569, 'コオロギ': 10570, 'これはいい': 10571, 'イスラム教徒': 10572, '豚骨ラーメン': 10573, '食べよ': 10574, '独りよがり': 10575, '説得': 10576, '地震': 10577, 'ぼっち': 10578, '誘え': 10579, 'tweet': 10580, 'chipshajen': 10581, '振る舞い': 10582, 'ムードメーカー': 10583, 'nTaimou': 10584, 'has': 10585, 'Talespin': 10586, 'すばらしかっ': 10587, '彼ら': 10588, 'ネクラサポート': 10589, 'ヒーローオブザストーム': 10590, 'すごかっ': 10591, 'bf': 10592, 'ナ': 10593, '通せる': 10594, 'conbox': 10595, '紛らわしく': 10596, '名乗れ': 10597, 'ナゾ': 10598, '重力': 10599, 'ニュースサイト': 10600, 'メタレポートパク': 10601, 'FPSwatch': 10602, 'お気に入り': 10603, 'らいし': 10604, '復習': 10605, '消去': 10606, 'おもち': 10607, 'ゃなんなん': 10608, 'うごき': 10609, 'IGL': 10610, '未熟': 10611, 'みっちり': 10612, 'いいだせん': 10613, '糧': 10614, '雑音': 10615, 'nGLvsNP': 10616, 'リアクション': 10617, 'デス': 10618, '無くなる': 10619, 'イラ': 10620, 'ナノブソルジャー': 10621, 'ULT': 10622, '必中': 10623, 'ランクマ': 10624, '舛添': 10625, 'トランプ': 10626, '政治資金': 10627, '私用': 10628, '着服': 10629, '移民': 10630, '現地': 10631, 'オーダー': 10632, '民意': 10633, '汲み取っ': 10634, '大統領': 10635, '誕生': 10636, '専門職': 10637, 'ビザ': 10638, 'れん': 10639, 'いたか': 10640, 'さい人': 10641, 'ありがち': 10642, '経路': 10643, '探索': 10644, 'ワープ': 10645, 'アース': 10646, '戻そ': 10647, 'ルビコン': 10648, 'ロシア': 10649, '各個': 10650, '分離': 10651, '各個撃破': 10652, 'クソベイブレードメタ': 10653, 'テストプレイ': 10654, 'やばし': 10655, '孫子': 10656, '兵法': 10657, '呟こ': 10658, '呟か': 10659, 'ある時': 10660, '考察': 10661, '助ける': 10662, 'マル': 10663, 'ボウ': 10664, 'たまらな': 10665, 'BF': 10666, 'プレーヤー': 10667, 'だしね': 10668, 'メンヘラタイム': 10669, '予期': 10670, 'エラー': 10671, 'surefour': 10672, '受け流す': 10673, '歩い': 10674, 'オクフェス': 10675, '壊滅': 10676, '悦び': 10677, 'なさい': 10678, 'rogue': 10679, 'ルナティック': 10680, 'ぼこっ': 10681, 'KOKR': 10682, 'ザリアファラ': 10683, 'よすぎ': 10684, 'Shift': 10685, 'Ctrl': 10686, 'ちゃお': 10687, 'ヤニ': 10688, '泣く泣く': 10689, '田端': 10690, '扇動': 10691, '不満': 10692, '抱える': 10693, '代弁': 10694, '行え': 10695, '種': 10696, '豚肉': 10697, '美味し': 10698, '力説': 10699, '儲かり': 10700, '費用': 10701, '物販': 10702, 'ステークス': 10703, 'ホルダー': 10704, 'む人': 10705, 'ウメハラ': 10706, '意志力': 10707, 'ルフス': 10708, '池袋': 10709, '快適': 10710, 'はやい': 10711, 'gpro': 10712, 'デラックス': 10713, 'レーサー': 10714, '根源': 10715, '末端': 10716, 'ぜんぜん': 10717, 'Rogue': 10718, 'にぼ': 10719, '短期間': 10720, '今期': 10721, '行かん': 10722, 'ボルスカ': 10723, 'ぴっく': 10724, '見ろ': 10725, '点数': 10726, '定期テスト': 10727, '受かる': 10728, 'detonation': 10729, 'ダステル': 10730, 'yutapon': 10731, '逸材': 10732, 'ban': 10733, 'クレカ': 10734, 'ポイントゲット': 10735, 'dex': 10736, '区': 10737, '切りつけ': 10738, '三月': 10739, '出会う': 10740, '話せる': 10741, '平然': 10742, '年上': 10743, '苦痛': 10744, 'うんざり': 10745, 'はしゃぐ': 10746, 'センチ': 10747, 'かならず': 10748, 'おなじ': 10749, '測っ': 10750, 'テラ': 10751, 'ココ': 10752, '遭遇': 10753, 'チートトレーサー': 10754, 'ようするに': 10755, '見方': 10756, '世界大会': 10757, 'ええええええ': 10758, '手すり': 10759, '平行': 10760, '小藪': 10761, 'arhan': 10762, '並': 10763, 'チームキル': 10764, 'スカッとする': 10765, 'き服': 10766, 'スタークラフト': 10767, '段違い': 10768, '複数回': 10769, 'トネ': 10770, '仲間割れ': 10771, 'Arhan': 10772, 'PROBASTION': 10773, 'ダウン': 10774, 'クリオフリーズ': 10775, 'noob': 10776, 'Detonator': 10777, 'nDetonator': 10778, 'nUSG': 10779, '最下位': 10780, 'snake': 10781, 'MiG': 10782, 'NGA': 10783, 'VG': 10784, 'Seagull': 10785, 'しかして': 10786, 'NRGvsUSG': 10787, 'apac': 10788, 'とても': 10789, '欧米': 10790, '鼻息': 10791, 'おすぎ': 10792, '大人しく': 10793, 'スピブバリアベイブレード': 10794, 'P': 10795, 'sup': 10796, '0t': 10797, 'ank': 10798, 'デフォ': 10799, 'ＮＡ': 10800, 'ロ上': 10801, 'やかましい': 10802, 'ミュート': 10803, 'ブロックミュート': 10804, '聞こえる': 10805, 'nfps': 10806, 'ザリアｳﾙﾄ': 10807, 'サウンドカード': 10808, '指向性': 10809, '解像度': 10810, '換装': 10811, 'misfits': 10812, 'ミスフィッツ': 10813, 'ゼニルシオ': 10814, '始まり': 10815, '二日酔い': 10816, '推定': 10817, 'arcarade': 10818, 'まけ': 10819, 'くやしい': 10820, 'Dignitous': 10821, 'きた上': 10822, '光る': 10823, 'ベイブレード': 10824, 'お腹': 10825, 'すい': 10826, 'ライフ': 10827, '振り回す': 10828, '大雨洪水警報': 10829, 'ovy': 10830, 'game': 10831, '水洗い': 10832, 'みつかる': 10833, 'sh': 10834, 'add': 10835, 'er0': 10836, 'kさん': 10837, 'ノ': 10838, 'c': 10839, 'ナノブロッサム': 10840, '対戦相手': 10841, 'ペーパーマン': 10842, '五分': 10843, 'テンキーレスキーボード': 10844, '君の名は': 10845, 'ロナウジーニョ': 10846, '片目': 10847, 'プーさん': 10848, 'ホームラン競争': 10849, '目星': 10850, '台本': 10851, 'かおる': 10852, '禿げ': 10853, '愛さ': 10854, '民度': 10855, 'アイスウォール': 10856, 'T': 10857, '字': 10858, '下ろし': 10859, 'sucked': 10860, 'grammer': 10861, 'unleashed': 10862, 'LAN': 10863, 'パーティ': 10864, '主催': 10865, 'はやば': 10866, 'オブジェクト指向': 10867, '仕上げ': 10868, '串刺し': 10869, '遅れる': 10870, '向上心': 10871, 'KILL': 10872, 'DEATH': 10873, 'いたい': 10874, '迫っ': 10875, '遅い': 10876, 'onfire': 10877, 'おしえ': 10878, 'ディレクター': 10879, 'もっとも': 10880, '受け取ら': 10881, '終盤': 10882, '誰々': 10883, 'ヌーブ': 10884, '口論': 10885, '顧み': 10886, 'ブッ': 10887, 'なすりつけ': 10888, 'ワンセット': 10889, 'コミニケーション': 10890, 'とれん': 10891, '賞賛': 10892, '少ないっ': 10893, '選手権': 10894, '義務教育': 10895, 'みりゃ': 10896, '資本集約': 10897, '型': 10898, 'リターン': 10899, '球場前': 10900, '募金': 10901, '根付き': 10902, 'ベット': 10903, '施設': 10904, '一戦': 10905, 'フレンチ': 10906, 'キーン': 10907, 'ばらまい': 10908, '対応力': 10909, '汎用性': 10910, 'PTER': 10911, 'アナウルト': 10912, '攻撃手段': 10913, 'はげ': 10914, 'スペシャルフォース': 10915, '甲斐': 10916, '味わい': 10917, 'クイマ': 10918, 'あさって': 10919, '遊べる': 10920, '統制': 10921, '白猫テニス': 10922, '定型': 10923, 'fuck': 10924, 'you': 10925, '0パーセント': 10926, '凄': 10927, 'ブレスオブファイア': 10928, '爆死': 10929, 'ブレス': 10930, 'まて': 10931, 'we': 10932, '今夜': 10933, 'KUN': 10934, 'MENDOKUSAI': 10935, '進学': 10936, '年間': 10937, '延ばす': 10938, 'カタン': 10939, 'taitanfall': 10940, '夏休み': 10941, '本気出す': 10942, 'オバウォ': 10943, 'それでは': 10944, 'ばらし': 10945, '戦線': 10946, '具合': 10947, 'がとう': 10948, '放り出し': 10949, '心頭': 10950, '滅却': 10951, '0点': 10952, 'うれしー': 10953, 'wｗ': 10954, 'ある意味': 10955, '退路': 10956, '塞が': 10957, '以来': 10958, 'デスブロッサム': 10959, '塞ぐ': 10960, '意外': 10961, '気付か': 10962, '微分方程式': 10963, '解く': 10964, 'MiGArhan': 10965, '見慣れ': 10966, '示せ': 10967, '囲う': 10968, 'もてない男': 10969, '付き合える': 10970, '捧げ': 10971, '教': 10972, '最後の手段': 10973, '唯一無二': 10974, '救い': 10975, '承認欲求': 10976, 'ファイナルブロー': 10977, '強力': 10978, '社畜': 10979, 'アンチヒーロー': 10980, 'やまじ': 10981, 'コンカッシブ': 10982, 'ラッシュ': 10983, 'ハンパない': 10984, 'ルシオマーシー': 10985, 'スピードブースト': 10986, '落ち込ん': 10987, '沈む': 10988, '単発': 10989, 'ぎや': 10990, 'ガチ勢': 10991, 'YAMATON': 10992, '師匠': 10993, '罵っ': 10994, '役職': 10995, '負': 10996, '誘わ': 10997, '実名': 10998, 'ID': 10999, 'ゴールデン': 11000, '血圧': 11001, 'バスティ': 11002, '不安感': 11003, '逆転負け': 11004, 'すり減らす': 11005, '仮定': 11006, '遠回り': 11007, 'いつの間にか': 11008, '適し': 11009, '自然に': 11010, '決めつけ': 11011, 'もしか': 11012, '伸び悩ん': 11013, 'nGL': 11014, 'yamaton': 11015, 'mercy': 11016, 'GLvsDTN': 11017, 'ぽちっ': 11018, 'レ': 11019, '透明': 11020, 'バスティオンピックニキ': 11021, 'steel': 11022, '金メダル': 11023, '無責任': 11024, '冷笑': 11025, '生ま': 11026, '負けれ': 11027, 'おおく': 11028, 'サウンドバリアー': 11029, 'てよ': 11030, '表す': 11031, '浅まし': 11032, 'なぜなら': 11033, '言説': 11034, '今月中': 11035, '闇雲': 11036, 'ないと': 11037, 'はう': 11038, 'ざいし': 11039, '送り出せる': 11040, 'ワールドクラス': 11041, '別物': 11042, 'bastion': 11043, 'ゲーミングヘッドホン': 11044, '買': 11045, 'わな': 11046, '軽さ': 11047, '人ち': 11048, 'ょいちょいいいこと': 11049, 'パン': 11050, 'ありえる': 11051, 'めくれ': 11052, '集まら': 11053, '諦めよ': 11054, '内の人': 11055, '借金': 11056, '一杯': 11057, 'LINE': 11058, 'Slack': 11059, 'ことなる': 11060, 'We': 11061, 'League': 11062, 'Rhe': 11063, 'end': 11064, 'I': 11065, 'hate': 11066, '悲し': 11067, 'いっか': 11068, 'つご': 11069, 'Lets': 11070, 'go': 11071, 'dude': 11072, '来季': 11073, 'ゲシュタルト崩壊': 11074, '呼吸': 11075, '攻めよ': 11076, 'やれよ': 11077, '敗北': 11078, '浮かぶ': 11079, 'fucking': 11080, 'idiot': 11081, 'inside': 11082, 'point': 11083, 'きかさ': 11084, '荒ん': 11085, 'サドンデスルールクソ': 11086, '世界ランク': 11087, 'うろうろ': 11088, '抜け出し': 11089, '追い込ま': 11090, '地雷': 11091, '粘る': 11092, 'アドレナリン': 11093, 'どばどば': 11094, '一体感': 11095, '試合終了後': 11096, '試合終了': 11097, '陣取り': 11098, 'ダンス': 11099, '☺': 11100, 'キャッチコピー': 11101, '救う': 11102, '関': 11103, 'overbuff': 11104, 'nStylishNoob': 11105, 'Genji': 11106, '設置': 11107, '麻雀': 11108, '約束': 11109, 'ポシャっ': 11110, 'オバ': 11111, 'もて': 11112, '男女': 11113, '工学部': 11114, 'お姫様': 11115, 'うし': 11116, 'offense': 11117, 'しいか': 11118, '前線': 11119, 'nK': 11120, '副産物': 11121, 'さいは': 11122, 'lv': 11123, 'いみな': 11124, '扉': 11125, '開けれ': 11126, 'nsanma': 11127, 'どうぞ': 11128, '幸い': 11129, '渡部陽一': 11130, '教典': 11131, 'StylishNoob': 11132, 'SPYGEA': 11133, '超す': 11134, '羽生': 11135, 'をん': 11136, '対戦中': 11137, '日曜日': 11138, 'アプライド': 11139, 'お先真っ暗': 11140, '続けれ': 11141, 'nスタ': 11142, 'ヌー': 11143, 'ボイチャ': 11144, 'トレイラー': 11145, 'nDRAGONS': 11146, 'しびれ': 11147, 'くださる': 11148, 'いたし': 11149, 'ボッチプレイ': 11150, 'グーシェ': 11151, '抜群': 11152, 'KYB': 11153, '弊社': 11154, '費用対効果': 11155, '顧客層': 11156, 'オウンドメディア': 11157, '押し付けがましい': 11158, 'WinWin': 11159, 'ハロウィン': 11160, '暴動': 11161, 'メールアドレス': 11162, 'ふくざつ': 11163, 'ストロングスタイル': 11164, '盛る': 11165, '盛ら': 11166, 'もったいないっ': 11167, '運用方法': 11168, 'CEO': 11169, 'キーノート': 11170, 'プリインストール': 11171, 'デー': 11172, '推進': 11173, '成功事例': 11174, '順張り': 11175, 'マンガワン': 11176, '血と灰の女王': 11177, 'グイグイ': 11178, 'バイトリーダー': 11179, '怒号': 11180, '券売機': 11181, '世界最高': 11182, '将来的': 11183, '資産': 11184, '日本社会': 11185, '機運': 11186, '目玉': 11187, '飛び出': 11188, '人脈': 11189, 'カンファレンス': 11190, '訴える': 11191, '訴えよ': 11192, 'IP': 11193, '相場': 11194, '濃密': 11195, '近日中': 11196, 'アフィ': 11197, 'カリスマ性': 11198, '取り組む': 11199, 'はげませる': 11200, '真摯': 11201, '効い': 11202, '息苦しく': 11203, 'CtoC': 11204, '東大卒': 11205, 'てわけ': 11206, 'たどり着い': 11207, 'Fortnite': 11208, 'docs': 11209, '様々': 11210, '日光': 11211, '山登り': 11212, '焼き鳥': 11213, '女': 11214, 'ステータス': 11215, '唾液': 11216, 'tokyo': 11217, 'mk0': 11218, 'ハウツー': 11219, '事業家': 11220, '孫正義': 11221, '志': 11222, '名著': 11223, 'やらさ': 11224, '説教': 11225, '家庭': 11226, '刷り込ま': 11227, '公立': 11228, 'ぶち込ま': 11229, 'お母さん': 11230, '閉じ': 11231, '緩く': 11232, 'らい': 11233, '担保': 11234, '網': 11235, '0年後': 11236, '母数': 11237, '御茶ノ水': 11238, '喧騒': 11239, '町': 11240, '過ごし': 11241, '昼飯': 11242, 'イノシシ': 11243, '思い出': 11244, '賭博': 11245, '探せる': 11246, 'レキボ': 11247, 'つぶし': 11248, 'イニシエート': 11249, 'くえー': 11250, 'ニコ': 11251, '手綱': 11252, 'ルシモイラブリ': 11253, 'ルシゼニブリ': 11254, 'コンプ': 11255, 'tgs': 11256, 'イクイク': 11257, '甘く': 11258, '漠然と': 11259, '都会': 11260, '市場経済': 11261, '払お': 11262, 'お門違い': 11263, '漠然': 11264, '払い': 11265, 'マリファナ': 11266, 'はやり': 11267, '海外事業': 11268, 'まちがっ': 11269, '日本企業': 11270, '起業家精神': 11271, '権': 11272, '関連企業': 11273, '一社': 11274, 'Startup': 11275, 'こんなん': 11276, 'チャットサポート': 11277, '人員': 11278, '解約': 11279, '阻止': 11280, 'ワードプレス': 11281, 'らしかっ': 11282, 'ポルトガル語': 11283, 'ばっちり': 11284, '売り切り': 11285, 'パッケージ': 11286, 'KPI': 11287, 'nWordPress': 11288, '二番煎じ': 11289, '人種': 11290, '国籍': 11291, '代金': 11292, '億': 11293, '妥当': 11294, 'ツイッチユーザー': 11295, 'Mixer': 11296, 'ビットレート': 11297, 'チアー': 11298, '払出': 11299, '認証': 11300, 'プロセス': 11301, '名刺': 11302, '印': 11303, '理': 11304, '憧れる': 11305, 'あこがれる': 11306, '何と': 11307, '絡める': 11308, '公的資金': 11309, 'バリュー': 11310, '貪欲': 11311, 'ロールモデル': 11312, '湧き出る': 11313, 'アイデンテティ': 11314, '崩れ': 11315, '銀行口座': 11316, 'ロック': 11317, 'すかし': 11318, 'キャッシング': 11319, '残金': 11320, '消費者金融': 11321, '結成': 11322, 'おもしろい': 11323, 'すりゃ': 11324, '法規制': 11325, '激しいっ': 11326, 'ゲーミングチーム': 11327, '貸して': 11328, '支給': 11329, 'フォトナチーム': 11330, '作れん': 11331, '考えなおし': 11332, '市場構造': 11333, '取材': 11334, '目立っ': 11335, 'ゲーマーズコーチ': 11336, 'ゲーマーコーチーズ': 11337, 'ゲーミングコーチ': 11338, 'あよかった': 11339, 'クレジットカード': 11340, '事業者': 11341, '雇え': 11342, 'nyoutuber': 11343, '属人': 11344, 'nnote': 11345, 'PRTIMES': 11346, '並み': 11347, '対外': 11348, 'PRtimes': 11349, 'ドキッ': 11350, 'バンキング': 11351, '送金': 11352, 'ガード': 11353, '固': 11354, 'nGpro': 11355, 'WL': 11356, 'いかんせん': 11357, 'ロジ': 11358, 'G0': 11359, 'えと': 11360, '重量': 11361, '形状': 11362, '失う': 11363, '現代': 11364, '背い': 11365, '単価': 11366, '密度': 11367, '増やせる': 11368, '誕生日': 11369, '習い事': 11370, '異': 11371, '即効': 11372, 'サム': 11373, 'a0': 11374, 'yo': 11375, 'グーグルアドセンス': 11376, '入れれ': 11377, 'しめ': 11378, 'Gamewith': 11379, 'eqo': 11380, 'DEP': 11381, 'フランチャイズ': 11382, 'AMEKEN': 11383, 'やり合っ': 11384, 'タイヨー': 11385, 'デップ': 11386, 'フォトナコーチ': 11387, 'いつ文': 11388, 'かど': 11389, 'うかっ': 11390, 'ポテンシャル': 11391, '対外試合': 11392, '合わせれ': 11393, 'ミシュランガイド': 11394, '祝': 11395, 'フォトナコーチング': 11396, '教わる': 11397, 'たぶん': 11398, '積める': 11399, '初回': 11400, 'セール': 11401, '急ぎ': 11402, 'フルタイムゲーマーコーチ': 11403, 'nLOL': 11404, 'ndata': 11405, '開講': 11406, '積ん': 11407, 'くれれ': 11408, '見込み': 11409, 'RAGE': 11410, '率い': 11411, 'ホリエモン': 11412, '0億': 11413, '仕事術': 11414, '不備': 11415, '色あせ': 11416, '模索': 11417, '親会社': 11418, 'no': 11419, 'anoa': 11420, 'marubou': 11421, 'まるまる': 11422, 'リスカ': 11423, '固定': 11424, '灯': 11425, '資本金': 11426, '増資': 11427, '繰り越し': 11428, '入金': 11429, '法務局': 11430, '拒否': 11431, 'おか': 11432, '入り乱れ': 11433, '興味本位': 11434, 'した先': 11435, 'TCG': 11436, 'OPENREC': 11437, '案の定': 11438, 'いと': 11439, '優良': 11440, '乞う': 11441, '頼める': 11442, '偉く': 11443, 'ドライ': 11444, 'タイム': 11445, '部類': 11446, '当面': 11447, '取り扱っ': 11448, '営利': 11449, 'Hearthstone': 11450, '記載': 11451, '青森': 11452, '山奥': 11453, 'シェアハウス': 11454, '極貧': 11455, '結ぶ': 11456, 'マンパワー': 11457, 'フィンテック': 11458, '潰れ': 11459, '神か': 11460, '著作権': 11461, 'クソツイート': 11462, '話して': 11463, '選挙': 11464, '票': 11465, '訴求': 11466, '候補者': 11467, '得票': 11468, '若者': 11469, '歩み寄る': 11470, '脚': 11471, 'youtuber': 11472, 'DJ社長': 11473, 'アップロード': 11474, '仕上げる': 11475, 'メインロール': 11476, 'ロールキュー': 11477, '使い勝手': 11478, 'りどう': 11479, '開放': 11480, 'コーチングチケット': 11481, '安いっ': 11482, '上限': 11483, '巻き上げ': 11484, '共通点': 11485, '揶揄': 11486, '取り込める': 11487, '膨らま': 11488, '本格': 11489, '比べ物': 11490, 'nGamerCoach': 11491, 'ロッテリア': 11492, 'メニュー': 11493, '旨辛': 11494, 'チーズ': 11495, 'マトン': 11496, 'インド': 11497, 'ハンバーガー': 11498, '新感覚': 11499, 'ならい': 11500, 'けそう': 11501, '管理費': 11502, '転載': 11503, '病院': 11504, '混雑': 11505, '医師': 11506, '免許': 11507, '寡占': 11508, '市場原理': 11509, '被る': 11510, '利用者': 11511, '立たさ': 11512, 'スカイプミーティグ': 11513, 'サイゲ': 11514, 'パパ活': 11515, 'アップテンポ': 11516, '曲': 11517, '聴い': 11518, 'Oneroom': 11519, 'calc': 11520, 'scene': 11521, '不在': 11522, '迎え': 11523, '旧態依然': 11524, 'つこ': 11525, 'チャリスパ': 11526, '国際化': 11527, 'おしよせ': 11528, 'ノイアー': 11529, '盗作': 11530, '筑豊': 11531, '同感': 11532, 'シリーズ': 11533, '無料通話': 11534, 'はやら': 11535, '請求書': 11536, '御中': 11537, 'Newspicks': 11538, '女子': 11539, 'ベルギー': 11540, 'Mbappe': 11541, '下限': 11542, 'プロフェッショナル': 11543, '価格設定': 11544, 'いかが': 11545, 'ばらつき': 11546, '均一': 11547, '偏っ': 11548, '引き上げ': 11549, '任せる': 11550, 'ゴール前': 11551, 'つぶす': 11552, '宇佐美': 11553, '武藤': 11554, '得点': 11555, 'コートジボワール': 11556, 'リード': 11557, '倒れ': 11558, '勝てば官軍': 11559, 'ニコニコ': 11560, '川島': 11561, 'がんばれ': 11562, '投資家': 11563, '登録免許税': 11564, 'フランク': 11565, '堅苦しい': 11566, '堅苦し': 11567, '取り除い': 11568, '版権': 11569, 'Helck': 11570, '技能': 11571, '料金': 11572, 'ダンピング': 11573, '岡崎': 11574, '本田': 11575, '懐かしさ': 11576, '柴崎': 11577, '空手': 11578, 'お見舞い': 11579, 'ベンホロウィッツ': 11580, 'HARD': 11581, 'THINGS': 11582, '定性的': 11583, '集客': 11584, '持ち込み': 11585, '著作物': 11586, 'Gmail': 11587, '迷惑メール': 11588, 'ヤフーメール': 11589, 'メーラー': 11590, '頂き': 11591, '引っ張ろ': 11592, '一件': 11593, '限っ': 11594, '鬼の首を取ったよう': 11595, '石': 11596, '言動': 11597, 'プレスリリース': 11598, 'プレス': 11599, '悩ん': 11600, '判ら': 11601, 'Creative': 11602, 'いじる': 11603, 'HyperX': 11604, '消費者': 11605, 'だまし': 11606, '改良': 11607, '見せかけ': 11608, 'いじくり': 11609, 'KP': 11610, '中盤': 11611, '戦闘': 11612, '練習場': 11613, '炎上商法': 11614, 'アート': 11615, 'ePS': 11616, '多数決': 11617, '加担': 11618, '肯定的': 11619, 'とらえる': 11620, '通販サイト': 11621, '勝機': 11622, '論理的': 11623, 'ネット社会': 11624, '直感': 11625, 'パラメータ': 11626, '凡人': 11627, '乗っけ': 11628, 'リテラシー': 11629, '徒手空拳': 11630, 'nurio': 11631, '\u200d♂': 11632, 'KPM': 11633, '0戦': 11634, 'マレーシア人': 11635, 'LGBT': 11636, '差別的': 11637, '占め': 11638, '毒にも薬にもならない': 11639, '取り払い': 11640, '悲しかっ': 11641, 'The': 11642, 'Empire': 11643, 'of': 11644, 'Pike': 11645, '秋刀魚': 11646, 'TEP': 11647, 'Unreal': 11648, 'た事': 11649, 'mercyJPN': 11650, 'ランクマキチガイ': 11651, 'エイムヒーロー': 11652, 'つかみ': 11653, 'ゴイゴイスウ': 11654, 'くっつき': 11655, 'フォトナソロ': 11656, '動悸': 11657, 'Fissure': 11658, 'きっかけ': 11659, '対等': 11660, 'ぽい': 11661, 'がっ': 11662, '待遇': 11663, 'グダグダ': 11664, 'JP': 11665, 'Overwatcjh': 11666, '一蘭': 11667, 'かぶせ': 11668, 'エイマー': 11669, 'アジアスクリム': 11670, 'い方': 11671, '期間限定': 11672, '青じそ': 11673, '精神病院': 11674, '送り込ん': 11675, '伝説': 11676, 'オン': 11677, 'ゆかり': 11678, '毎週': 11679, '俺レベル': 11680, '起こせ': 11681, '社会実験': 11682, '在り方': 11683, '来れる': 11684, '回る': 11685, '開拓': 11686, '憧れ': 11687, 'ゲハ': 11688, '共同生活': 11689, '届ける': 11690, '安全地帯': 11691, 'サイコパス': 11692, 'doneshineshine': 11693, 'nmano': 11694, '商標登録': 11695, 'Trn': 11696, '結婚': 11697, '材': 11698, 'ジェッパ': 11699, '全角': 11700, '英': 11701, 'のっかっ': 11702, 'バーミリオン': 11703, 'イメージ通り': 11704, '果たさ': 11705, '通じ': 11706, 'さわやか': 11707, 'Note': 11708, 'はて': 11709, 'ブ位': 11710, '福岡県民': 11711, '主食': 11712, 'フォトナスク': 11713, '勤め先': 11714, 'ign': 11715, '職場': 11716, 'ルナハイスクリム': 11717, '疲労感': 11718, '倦怠感': 11719, '強制': 11720, 'バクバク': 11721, '居': 11722, '占拠': 11723, '判断ミス': 11724, '命取り': 11725, 'tumblr': 11726, '誘える': 11727, 'おもいつか': 11728, 'かに': 11729, 'watson': 11730, '正規表現': 11731, 'ざっくり': 11732, 'Karabiner': 11733, '度目': 11734, '初期化': 11735, '0年間': 11736, 'いい大学': 11737, 'レール': 11738, '沿っ': 11739, '職業選択': 11740, '組み込ま': 11741, '埋め込ま': 11742, 'ひっくり返せ': 11743, '四隅': 11744, '各所': 11745, '押さえ': 11746, '極性': 11747, '撃退': 11748, 'こだわり': 11749, 'nCSGO': 11750, 'エイムゲー': 11751, 'なおさ': 11752, 'ycs': 11753, '覚醒': 11754, '作用': 11755, '難癖': 11756, '長': 11757, '休暇': 11758, 'ぐっと': 11759, '厚く': 11760, '軽いっ': 11761, '大半': 11762, '弁護士': 11763, '人当り': 11764, 'サービスフォトナ': 11765, '加える': 11766, 'ポンプ': 11767, 'ムーブ': 11768, 'タクティカル': 11769, '女性専用車両': 11770, '車両': 11771, '凍る': 11772, 'ジェットパック': 11773, 't0': 11774, 'T0': 11775, 'ファーム': 11776, 'きょう': 11777, 'totemo': 11778, 'yjouzu': 11779, 'player': 11780, 'ウルトラライトプロ': 11781, 'ボタンバインド': 11782, 'バインド': 11783, '割り当て': 11784, 'CAG': 11785, 'ストリートファイター': 11786, 'epos': 11787, '公証役場': 11788, 'もらわ': 11789, '個人事業主': 11790, '独立採算': 11791, '価格競争': 11792, '定款': 11793, 'ピッ': 11794, '通す': 11795, '役場': 11796, '出向い': 11797, '高給': 11798, 'エリート': 11799, 'shure': 11800, '堀江貴文': 11801, '天国': 11802, 'かかわり': 11803, 'ケンカ': 11804, 'ふっかける': 11805, '操作ミス': 11806, '作業内容': 11807, 'ばくわら': 11808, 'bit': 11809, 'cash': 11810, '出資': 11811, 'es': 11812, 'ports': 11813, '背後': 11814, 'shibuya': 11815, 'gamers': 11816, '卓球部': 11817, '運動部': 11818, '下層': 11819, 'ネタバラシ': 11820, '印鑑': 11821, '印鑑証明': 11822, 'お役所仕事': 11823, '遅らさ': 11824, '憤り': 11825, 'がちがち': 11826, '整体': 11827, '血流': 11828, '寝違え': 11829, 'シャレ': 11830, '痛み': 11831, 'サノス': 11832, 'サノスモード': 11833, '祈る': 11834, 'ソロビクロイ': 11835, 'Kyuhan': 11836, '肩甲骨': 11837, '炎症': 11838, 'せいさ': 11839, 'ち安': 11840, '駐車場': 11841, 'ベンツ': 11842, 'ルナハイキル': 11843, 'nanimo': 11844, '避ける': 11845, 'モスティマイア': 11846, '減': 11847, '直ら': 11848, 'どちゃくそ': 11849, 'タイタンフォール': 11850, '集中砲火': 11851, '山上': 11852, '工場': 11853, '漁夫': 11854, '盤': 11855, '払える': 11856, '常々': 11857, '何らかの': 11858, 'District': 11859, '見栄え': 11860, '転生': 11861, 'ブリギッテ': 11862, '親富': 11863, '孝': 11864, 'ソロスク': 11865, '目指せ': 11866} [tensor(821), tensor(6193)]
[2019-10-08 04:30:36,840] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 69, in generate_seq
    res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
  File "/abetter/LSTM_model.py", line 69, in <listcomp>
    res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
KeyError: 821
172.17.0.1 - - [08/Oct/2019 04:30:36] "POST / HTTP/1.1" 500 -
^Croot@0ca109d793fb:/abetter# vi LSTM_model.py 
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 04:33:15] "GET / HTTP/1.1" 200 -
{'海外': 0, 'は': 1, '許諾': 2, 'とっ': 3, 'て': 4, 'バリバリ': 5, '動画': 6, '販売': 7, 'し': 8, 'てる': 9, 'とこ': 10, 'ある': 11, 'よ': 12, 'ね': 13, '軽減税率': 14, 'って': 15, 'ギャグ': 16, 'か': 17, 'と': 18, '思っ': 19, 'たら': 20, 'マジで': 21, '実施': 22, 'さ': 23, 'れる': 24, '施策': 25, 'な': 26, 'の': 27, '0歳': 28, 'に': 29, 'なっ': 30, 'た': 31, 'けど': 32, '敬語': 33, '使い方': 34, '全く': 35, 'わから': 36, 'ない': 37, 'こう': 38, 'みる': 39, 'スポーツ': 40, '本当に': 41, '同じ': 42, 'や': 43, '日本代表': 44, '渡航': 45, '費': 46, 'クラァン': 47, '純粋': 48, '集まり': 49, '切っ': 50, 'が': 51, 'すごい': 52, 'クリエイティブ': 53, 'を': 54, '作成': 55, 'やる': 56, 'こと': 57, '意義': 58, '社会': 59, '訴え': 60, 'かけれ': 61, 'ば': 62, '集金': 63, '可能': 64, 'という': 65, '事例': 66, '作っ': 67, '意味': 68, 'で': 69, '二重': 70, 'dafran': 71, '待機時間': 72, 'せい': 73, 'タンク': 74, 'メイン': 75, '笑う': 76, 'n': 77, '一方': 78, 'Haksal': 79, '0時間': 80, 'かけて': 81, '新': 82, '垢': 83, 'DPS': 84, '認定': 85, '終わら': 86, 'せ': 87, 'nDPS': 88, 'プロ': 89, 'ランク': 90, '練習': 91, '時間': 92, '取れ': 93, 'なく': 94, '大変': 95, 'そう': 96, '明る': 97, '単': 98, '振動': 99, 'まじ': 100, 'やばい': 101, '目': 102, 'チカチカ': 103, 'する': 104, 'mac': 105, 'バチクソバグ': 106, '電源': 107, '入れ': 108, 'なおす': 109, 'たび': 110, '異なる': 111, 'キー': 112, '0回': 113, 'タイピング': 114, '押さ': 115, '挙動': 116, '作業': 117, '効率': 118, '下がる': 119, '次': 120, 'から': 121, 'ryzencpu': 122, '格安': 123, 'ノート': 124, '買う': 125, 'つくば': 126, 'ラーメン': 127, 'うまさ': 128, 'ガチ': 129, 'note': 130, '過去': 131, '記事': 132, '見返し': 133, '思う': 134, 'ゲーム': 135, '楽しさ': 136, '部活': 137, 'みたい': 138, '体験': 139, '家': 140, '帰っ': 141, 'パソコン': 142, '起動': 143, 'だけ': 144, 'でき': 145, '年齢': 146, '場所': 147, '問わ': 148, 'ず': 149, '真剣勝負': 150, '楽しめる': 151, 'ところ': 152, 'なあ': 153, 'nteppen': 154, 'カードゲーム': 155, 'も': 156, '楽しい': 157, '人': 158, '交流': 159, 'twitter': 160, '配信': 161, '上': 162, 'しか': 163, '無く': 164, '個人的': 165, '満足度': 166, 'チーム': 167, 'FPS': 168, '圧倒的': 169, 'teppen': 170, 'AI': 171, '作り': 172, 'たく': 173, '強化学習': 174, '調べ': 175, '行動': 176, '学習': 177, 'プラットフォーム': 178, '作る': 179, '一番': 180, '要は': 181, 'ため': 182, 'API': 183, '公開': 184, 'れ': 185, 'せる': 186, '0': 187, 'プログラム': 188, '落とし込ま': 189, 'いけ': 190, 'そこ': 191, '0週間': 192, 'くらい': 193, 'かかる': 194, 'Twitch': 195, 'より': 196, 'Youtube': 197, '方': 198, 'レコメンド': 199, 'システム': 200, 'とか': 201, '結果': 202, '表示': 203, '含め': 204, 'よっぽど': 205, '優れ': 206, '新規': 207, '投稿': 208, '上位表示': 209, '知っ': 210, 'あれ': 211, 'よく': 212, '考えれ': 213, '•': 214, '動画投稿者': 215, 'チャンス': 216, '与える': 217, 'エコシステム': 218, '全体': 219, '新陳代謝': 220, '早める': 221, '量産': 222, 'モチベーション': 223, '登録者': 224, '数': 225, '者': 226, '考える': 227, 'アルゴリズム': 228, '形成': 229, 'できる': 230, 'ん': 231, 'だ': 232, '気づい': 233, 'uD': 234, 'D': 235, 'uDC': 236, '科学': 237, 'へ': 238, '興味': 239, 'パラノイア': 240, '性': 241, '牧歌的': 242, '大事': 243, '気': 244, 'なる': 245, '後で': 246, '読む': 247, '来月': 248, '中国': 249, '行き': 250, 'たいん': 251, '中国語': 252, 'わからん': 253, 'eスポーツ': 254, '企業': 255, 'について': 256, 'たい': 257, '万': 258, 'こういう': 259, '調査': 260, 'レポート': 261, 'まとめ': 262, '送っ': 263, 'くれる': 264, 'サービス': 265, 'ないん': 266, 'イラレマジ': 267, '使い': 268, 'づれ': 269, 'nIT': 270, '土方': 271, 'み': 272, '飯': 273, '資金': 274, '調達': 275, '社長': 276, '0人': 277, '来る': 278, 'マジ': 279, '楽しみ': 280, 'ｗ': 281, '漫画村': 282, '運営': 283, '経歴': 284, 'ググっ': 285, '嘘': 286, '本当': 287, '情報': 288, '大量': 289, '出': 290, 'き': 291, '遵法': 292, '意識': 293, '低い': 294, 'ガッツ': 295, '印象': 296, '半端ない': 297, '本人': 298, '努力': 299, 'あっ': 300, 'こそ': 301, 'コーチング': 302, 'ブロンズ': 303, 'グラマス': 304, 'すご': 305, 'すぎる': 306, 'いい': 307, '感じ': 308, '人数': 309, 'んで': 310, '締め': 311, 'ます': 312, '二': 313, '回': 314, '開催': 315, 'それぞれ': 316, '会社': 317, 'やっ': 318, 'ゲスト': 319, '呼ぼ': 320, 'う': 321, 'C': 322, '向け': 323, '日本': 324, '上場': 325, 'くる': 326, 'やろ': 327, '人月': 328, '0万': 329, 'マザーズ': 330, '強': 331, '応募': 332, 'いただき': 333, 'まし': 334, 'ありがとう': 335, 'ござい': 336, 'いっぱい': 337, '集まっ': 338, '僕': 339, 'おごり': 340, '焼肉': 341, 'でも': 342, 'ましょ': 343, '最高': 344, '普段': 345, '新宿': 346, '本郷': 347, '渋谷': 348, 'い': 349, '最近': 350, '新しい': 351, '会っ': 352, '業界': 353, 'なんか': 354, 'めっちゃ': 355, 'エイム': 356, 'きれい': 357, '今日': 358, 'ロケ': 359, 'ラン': 360, 'ワンショット': 361, 'キル': 362, 'ハンゾーリワーク': 363, 'オバフ': 364, '成績': 365, 'めちゃくちゃ': 366, '草': 367, '後': 368, 'ブリ': 369, '勝率': 370, '0番': 371, 'とかいう': 372, '誰か': 373, '金': 374, '出す': 375, '0円': 376, 'フォトショ': 377, '教え': 378, 'ほしい': 379, '敷居が高い': 380, 'フォートナイト': 381, 'esports': 382, 'なのか': 383, 'デュオ': 384, 'スク': 385, 'シフティ': 386, 'グリーシー': 387, '向かう': 388, '強い': 389, 'その': 390, '理由': 391, 'ブログ': 392, '書い': 393, '一緒に': 394, 'miro': 395, 'どこ': 396, 'いっ': 397, 'かき': 398, 'しない': 399, '相手': 400, 'とら': 401, '初心者': 402, 'だっ': 403, '場合': 404, '有効': 405, '先': 406, '一人': 407, '顔出し': 408, 'フォーカス': 409, 'もらっ': 410, '耐え': 411, 'ながら': 412, 'ショットガン': 413, 'ヘッド': 414, 'ぶち込む': 415, '動き': 416, '結構': 417, '敵': 418, 'ただ': 419, '打た': 420, '油断': 421, 'そこそこ': 422, '決まる': 423, 'スクアッド': 424, 'うまく': 425, 'なれ': 426, '行ける': 427, 'よう': 428, 'なり': 429, 'いって': 430, '初めて': 431, '優勝': 432, 'うれしい': 433, 'リプレイ': 434, 'チーミング': 435, '氏': 436, '取る': 437, 'やつ': 438, '多い': 439, 'わ': 440, 'フォトナマジ': 441, 'OW': 442, '似': 443, '武器': 444, 'ピック': 445, 'ポジショニング': 446, '誰': 447, '集める': 448, 'どういう': 449, '順番': 450, '顔出': 451, 'すか': 452, '要素': 453, '寄り': 454, '負け': 455, '試合': 456, '確認': 457, '全部': 458, '裏': 459, '横': 460, '体力': 461, '差': 462, '作ら': 463, 'ほとんど': 464, 'なー': 465, 'デュオスク': 466, '複数人': 467, '来ら': 468, '位置': 469, '把握': 470, '間違え': 471, '死ぬ': 472, '難しい': 473, '最後': 474, 'なぜ': 475, '急': 476, '切り替わっ': 477, '来': 478, 'やら': 479, '批評家': 480, 'もの': 481, 'に対して': 482, '文句': 483, '失敗': 484, '俺': 485, '言っ': 486, 'とおり': 487, 'っていう': 488, '簡単': 489, '実際': 490, '事業': 491, '起こし': 492, '責任': 493, 'もっ': 494, 'ビジネス': 495, 'として': 496, '成り立つ': 497, '力': 498, '必要': 499, '協会': 500, '声': 501, '上げ': 502, 'なら': 503, '自分': 504, '作れ': 505, 'そういう': 506, '行動力': 507, 'いない': 508, '外部': 509, '団体': 510, 'ばっか': 511, 'jesu': 512, 'どっか': 513, 'レンタルオフィス': 514, '借りて': 515, 'たって': 516, '安い': 517, 'コスト': 518, '儲かる': 519, 'かなっ': 520, '多分': 521, 'たり': 522, '提携': 523, '法人': 524, '登記': 525, '借りる': 526, 'ので': 527, '持つ': 528, '別': 529, '側': 530, 'スキーム': 531, '提供': 532, 'ライセンス': 533, '発行': 534, '料': 535, '当たれ': 536, 'おいしい': 537, 'ダメ': 538, '大して': 539, 'ダメージ': 540, 'グレポン': 541, '必要性': 542, '装備': 543, 'アサルト': 544, 'スナ': 545, '爆発物': 546, '回復': 547, '0つ': 548, '安定': 549, 'スカーズ': 550, '人勝': 551, '率': 552, 'べ': 553, 'え': 554, 'バケモン': 555, 'PUBG': 556, '違っ': 557, '集めれ': 558, 'まぐれ': 559, 'アンチ': 560, '運': 561, '負ける': 562, 'ほぼ': 563, '常に': 564, '忙しく': 565, 'アグレッシブ': 566, '戦える': 567, 'リーダーボード': 568, '見': 569, '上位': 570, '層': 571, '名前': 572, '倒し': 573, 'ビクロイ': 574, '当たり': 575, 'あい': 576, '多く': 577, 'まあ': 578, 'それ': 579, '以外': 580, 'あんまり': 581, 'フォトナ': 582, 'おもし': 583, 'えな': 584, 'bot': 585, 'もれなく': 586, 'フォロー': 587, '今回': 588, 'フォトナブログ': 589, 'SEO': 590, '対策': 591, 'ちゃんと': 592, 'やり': 593, '検索': 594, '予測': 595, '候補': 596, 'ワード': 597, 'タイトル': 598, '名': 599, '攻略': 600, 'アクセス': 601, '0割': 602, 'グーグル': 603, 'はてブ': 604, 'バカ': 605, '重い': 606, 'この': 607, '勉強': 608, 'aktm': 609, '人気': 610, '日本人': 611, 'OPUTO': 612, 'AKTM': 613, 'もん': 614, 'きつく': 615, 'ダスティデポ': 616, '降り': 617, '建築': 618, '無視': 619, 'ジャンプ': 620, 'まくり': 621, '天下': 622, '一': 623, '舞踏': 624, '会す': 625, 'おもろ': 626, 'すぎ': 627, '一応': 628, 'sanma': 629, 'あの': 630, '宇宙人': 631, '魚': 632, 'スキン': 633, '買お': 634, '悩む': 635, 'ユーザー': 636, '聞い': 637, '早く': 638, '変え': 639, 'いいもの': 640, 'しよう': 641, '姿勢': 642, '伝わっ': 643, '0v': 644, 's': 645, 'どう': 646, 'かも': 647, 'ブロックバスター': 648, 'なん': 649, 'だろ': 650, '方向性': 651, '違い': 652, '完成度': 653, '深さ': 654, '勝っ': 655, '好き': 656, 'えー': 657, 'アバター': 658, '早い': 659, 'オメガ': 660, 'かっこいい': 661, 'カーバイド': 662, 'チャレンジ': 663, 'ワクワク': 664, 'アプデ': 665, '神': 666, '過ぎ': 667, 'フレンド': 668, 'いっつも': 669, 'フォトナフレンド': 670, '募集': 671, '画像': 672, '屋敷': 673, '物資': 674, '量': 675, 'やばかっ': 676, '前': 677, 'gorou': 678, 'さん': 679, 'ソロ': 680, 'ラスト': 681, 's0': 682, '当たっ': 683, 'うま': 684, 'チート': 685, '天使大学': 686, 'デジハリ': 687, '中': 688, '鉄板': 689, '毎回': 690, '七': 691, '位': 692, '猛者': 693, 'がふ': 694, 'ざけてかいとるんやろなあ': 695, 'Vermillion': 696, 'まだ': 697, '健在': 698, '今季': 699, '始め': 700, '数字': 701, '引っ張ら': 702, '来期': 703, 'トップ': 704, 'G': 705, 'SR': 706, '箱': 707, '出し': 708, '時点': 709, '丸まっ': 710, '端っこ': 711, '丸まり': 712, '治ら': 713, 'キレ': 714, '速攻': 715, 'メルカリ': 716, '記憶': 717, 'パッドサーフェス': 718, '良かっ': 719, '滑る': 720, '無理': 721, 'ハヤテ': 722, '甲': 723, 'かなり': 724, 'GS': 725, 'R': 726, '表面': 727, 'ぶっちゃけ': 728, 'どっち': 729, 'そんなに': 730, '変わら': 731, '下': 732, '滑り止め': 733, 'artisan': 734, 'あと': 735, '送料': 736, '高く': 737, '関係': 738, 'パッド': 739, '丸め': 740, 'られ': 741, '送ら': 742, '残念': 743, 'リアルタイム': 744, '機械学習': 745, '処理': 746, '女の子': 747, 'データ': 748, '集め': 749, 'すげ': 750, 'これ': 751, 'トール': 752, 'LAG': 753, '変更': 754, '早': 755, 'ウケる': 756, '案外': 757, '攻め': 758, 'ああ': 759, 'いう': 760, '状況': 761, 'あり': 762, 'トレゲン': 763, 'ぶっ': 764, '刺さる': 765, 'アンチダイブ': 766, '使っ': 767, 'ウィンストン': 768, 'ラインハルト': 769, 'ウィドウ': 770, 'ザリア': 771, '機能': 772, 'いる': 773, 'かな': 774, '法則': 775, 'モード': 776, '残り': 777, '分け合っ': 778, 'じゃ': 779, '狩り': 780, '気分': 781, 'ジャンパ': 782, '飛ん': 783, '歩いてる': 784, '殺し': 785, 'そいつ': 786, '回収': 787, 'っ': 788, '無限ループ': 789, 'お': 790, '治っ': 791, 'クラッシュ': 792, '腹立つ': 793, 'PC': 794, '初期': 795, '化': 796, '最初': 797, '画面': 798, '動か': 799, '逝っ': 800, 'くさい': 801, 'みなさん': 802, 'さようなら': 803, '熱': 804, 'クーラー': 805, '付け': 806, '暖房': 807, '気づく': 808, 'かかっ': 809, 'てか': 810, 'どの': 811, 'タイヤ': 812, '対処': 813, '一切': 814, '決まら': 815, 'void': 816, '入っ': 817, 'bischu': 818, 'nLAG': 819, 'もっと強く': 820, '仕事': 821, '事務': 822, '手続き': 823, '週間': 824, '取ら': 825, '郵送': 826, '書類': 827, '待つ': 828, '一週間': 829, 'まったり': 830, 'ずっと': 831, '滞っ': 832, '展開': 833, 'ぞ': 834, 'ウルト': 835, '怒っ': 836, '増え': 837, 'もらう': 838, '地味': 839, 'でしょ': 840, 'ヒーロー': 841, '伝わら': 842, 'ねえ': 843, 'アースシャター': 844, 'どかーんっ': 845, 'メタ': 846, 'カップ麺': 847, '食っ': 848, 'おっさん': 849, '確か': 850, '警察署前': 851, '暴走族': 852, '交差点': 853, '信号': 854, '警察': 855, '煽っ': 856, '地元': 857, '人間': 858, '愚か': 859, '象徴': 860, '支援物資': 861, '群がる': 862, '見る': 863, '牛丼': 864, '無料': 865, '十分': 866, '並ん': 867, 'でる': 868, '思い出す': 869, '何で': 870, '老人': 871, 'お金': 872, '貯め': 873, 'こむ': 874, 'まで': 875, '理解': 876, 'なかっ': 877, '若い人': 878, '投資': 879, '経済活性化': 880, 'す': 881, 'べき': 882, 'だって': 883, '信じ': 884, 'vs': 885, '本質': 886, '的': 887, '部分': 888, '見え': 889, 'いや': 890, 'コミュニケーション': 891, '味方': 892, '渡す': 893, '信じる': 894, '勝利': 895, '最適': 896, '解': 897, '関わら': 898, 'あまりに': 899, 'むかつく': 900, 'Reddit': 901, 'スレ': 902, '立てる': 903, '開発': 904, '奪わ': 905, 'イライラ': 906, '以下': 907, 'meko': 908, '自爆': 909, 'うめ': 910, 'OWL': 911, 'レベル': 912, '高さ': 913, '貢献': 914, 'いろいろ': 915, '感動': 916, '年収': 917, '高い': 918, '受け': 919, 'いく': 920, 'リクナビ': 921, '日程': 922, '適当': 923, '受けて': 924, '出る': 925, 'ことは': 926, '足り': 927, '離職率': 928, '人材': 929, '獲得': 930, '払わ': 931, 'ヤバイ': 932, '就活': 933, 'サイト': 934, 'あて': 935, '，': 936, '社': 937, '内定': 938, 'やめる': 939, 'やれ': 940, 'ほど': 941, '少し': 942, 'づつわかるしいろいろ': 943, 'まじめ': 944, 'やろう': 945, '彼': 946, '大企業': 947, '受けろ': 948, '大': 949, 'けれど': 950, '給料': 951, '福利厚生': 952, '身': 953, 'つく': 954, 'スキル': 955, '研修': 956, '質': 957, '説明会': 958, '昨日': 959, 'むちゃくちゃ': 960, '疲れ': 961, '行進': 962, 'むためどうすればいいかとか': 963, '何': 964, 'メモ': 965, 'ヤバい': 966, '茨城': 967, '東京': 968, '行く': 969, 'るす': 970, 'ぎて': 971, '詰め込ん': 972, 'どる': 973, 'しんどい': 974, '専': 975, '話': 976, 'メカニカル': 977, '以前': 978, '協調性': 979, 'なけれ': 980, 'レート': 981, '落ちる': 982, '当然': 983, '低': 984, '納得': 985, 'ロール': 986, '協調': 987, 'プレイヤー': 988, '多少': 989, '当たり前': 990, '面接': 991, 'サークル': 992, '研究': 993, 'つまら': 994, '話し': 995, 'クスタウキウキ': 996, 'LAV': 997, 'クスタ': 998, 'スペース': 999, 'バニー': 1000, 'イケイケ': 1001, '普通': 1002, '学生': 1003, '有利': 1004, 'つかつか': 1005, 'つかれ': 1006, 'がち': 1007, '疲れる': 1008, '青木': 1009, '就活グッズ': 1010, '買っ': 1011, '萎える': 1012, 'マナー': 1013, 'パワポ': 1014, '印刷': 1015, 'した': 1016, '紙': 1017, 'スタバ': 1018, 'ドトール': 1019, 'うるさ': 1020, '机': 1021, '狭い': 1022, 'カフェ': 1023, 'チェーン店': 1024, '静か': 1025, 'じれる': 1026, 'うるさく': 1027, 'ください': 1028, 'ルノアール': 1029, '知り': 1030, 'ませ': 1031, '久しぶり': 1032, '筋トレ': 1033, '気持ちいい': 1034, '上腕三頭筋': 1035, '燃える': 1036, 'パンプ': 1037, '同士': 1038, '対決': 1039, '使わ': 1040, '一方的': 1041, '倒せる': 1042, '誘導': 1043, 'ミサイル': 1044, '削除': 1045, '大きな': 1046, '有能': 1047, '全て': 1048, '細かい': 1049, 'やり取り': 1050, 'ライン': 1051, '行い': 1052, 'winz': 1053, 'akm': 1054, '兄弟': 1055, 'nwinz': 1056, '個': 1057, '世界チャンピオン': 1058, 'やっぱ': 1059, '才能': 1060, '世界': 1061, '知らんけど': 1062, 'なんで': 1063, '減っ': 1064, 'のに': 1065, 'レイジ': 1066, '使う': 1067, 'パック': 1068, 'クール': 1069, '生かし': 1070, '抑える': 1071, 'そもそも': 1072, '減る': 1073, '考え方': 1074, '攻撃': 1075, 'エフェクト': 1076, 'オゲ': 1077, '言葉': 1078, '壁': 1079, 'カバー': 1080, '今': 1081, 'ダラス': 1082, '続き': 1083, 'デカ': 1084, 'かっ': 1085, '戦力': 1086, '相当': 1087, '重要': 1088, '上回る': 1089, '放出': 1090, 'ツイッター': 1091, '感じる': 1092, 'SNS': 1093, '討論': 1094, '白黒': 1095, '善悪': 1096, '存在': 1097, '主観': 1098, '依存': 1099, '肯定': 1100, '意見': 1101, 'ひたすら': 1102, 'RT': 1103, 'つっ': 1104, 'ー': 1105, 'jjonak': 1106, '唯一': 1107, 'KD': 1108, '比': 1109, '超': 1110, 'えて': 1111, 'トレーサー': 1112, '殺さ': 1113, '殺す': 1114, 'SFSvsSHD': 1115, 'むっちゃ': 1116, 'いい試合': 1117, '上海': 1118, '初勝利': 1119, 'SHD': 1120, 'マーシー': 1121, 'アーキテクト': 1122, 'バルキリー': 1123, 'カウンター': 1124, 'シーン': 1125, '出して': 1126, '笑っ': 1127, 'イーブン': 1128, '状態': 1129, 'geguri': 1130, 'pogchamp': 1131, 'げ': 1132, 'うまい': 1133, 'AKM': 1134, 'ソンブラ': 1135, '悪い': 1136, 'やばく': 1137, '萎え': 1138, '命': 1139, '犠牲': 1140, '死体': 1141, '打っ': 1142, '道連れ': 1143, 'きつ': 1144, 'そん': 1145, '永久': 1146, 'BAN': 1147, 'トロール': 1148, '許容': 1149, 'Overwatch': 1150, 'LUL': 1151, 'HARAOK': 1152, '例': 1153, 'gt': 1154, 'すれ': 1155, '単純': 1156, '計算': 1157, 'ハンゾー': 1158, '明確': 1159, '毎': 1160, 'ずつ': 1161, '落とす': 1162, 'それで': 1163, '以上': 1164, '集まる': 1165, '証明写真': 1166, '顔': 1167, 'FIssure': 1168, '起き': 1169, 'フィッシャー': 1170, '言う': 1171, 'スポンサード': 1172, 'KarQ': 1173, 'まさしく': 1174, 'プロゲーマー': 1175, 'コミュニティ': 1176, 'スケール': 1177, 'によって': 1178, 'コンテンツ': 1179, '時': 1180, '収益': 1181, '否': 1182, '変わっ': 1183, 'つまり': 1184, '多': 1185, 'acer': 1186, 'るし': 1187, '週': 1188, 'バッセン': 1189, 'いか': 1190, 'すっきり': 1191, '超える': 1192, 'タバコ': 1193, '吸う': 1194, '吸っ': 1195, 'レッドブル': 1196, '飲ん': 1197, '脳みそ': 1198, 'ポワポワ': 1199, 'エンジン': 1200, 'やめ': 1201, 'エンジニア': 1202, 'コンサル': 1203, '初任給': 1204, '五': 1205, '百': 1206, '方法': 1207, '無限': 1208, 'リソース': 1209, '広告': 1210, '運用': 1211, '欲しい': 1212, 'シェア': 1213, '仲間': 1214, '共同開発': 1215, '楽し': 1216, 'うらやましい': 1217, '日': 1218, 'RATEL': 1219, 'UI': 1220, '見せ': 1221, 'よかっ': 1222, 'ne': 1223, '素晴らしい': 1224, 'プロダクト': 1225, 'こちら': 1226, 'Shin': 1227, 'XL': 1228, '選ば': 1229, 'ピーク': 1230, '0位': 1231, 'らしい': 1232, 'こんな': 1233, '日本語': 1234, 'うから': 1235, '英語': 1236, 'スケールする': 1237, 'たかっ': 1238, 'わかり': 1239, 'やすい': 1240, '解説': 1241, 'とともに': 1242, 'クオリティ': 1243, '実現': 1244, '投げ': 1245, 'ビビら': 1246, 'Yoshi': 1247, 'haru': 1248, '面白い': 1249, 'OWpedia': 1250, '後援': 1251, 'ここ': 1252, 'プロチーム': 1253, 'イベント': 1254, '参加': 1255, '企画': 1256, 'を通じて': 1257, '発展': 1258, '意味合い': 1259, '私設': 1260, '書誌': 1261, '住所': 1262, '本当は': 1263, '倍': 1264, 'プレー': 1265, '指摘': 1266, '覚え': 1267, 'ないし': 1268, 'とりあえず': 1269, '抜き出し': 1270, '後記': 1271, '事': 1272, '個人ブログ': 1273, '読ま': 1274, '残ら': 1275, 'インターネット': 1276, 'デ': 1277, 'クソ': 1278, 'しょうが': 1279, 'アーカイブ': 1280, '読める': 1281, '書か': 1282, '無駄': 1283, 'キャラ': 1284, '性能': 1285, '引き出す': 1286, 'みんな': 1287, 'がる': 1288, 'アナ': 1289, '死に': 1290, 'にくく': 1291, 'ほう': 1292, '0倍': 1293, '楽': 1294, '分断': 1295, 'ヒーラー': 1296, 'ひきつけ': 1297, 'ゼニヤッタ': 1298, '後ろ': 1299, '死な': 1300, '不和': 1301, 'つけ': 1302, 'てれ': 1303, 'どんな': 1304, '本能': 1305, '理解度': 1306, 'もろに': 1307, '影響': 1308, 'シルゴル': 1309, 'いいんじゃない': 1310, '思え': 1311, 'ごと': 1312, 'なんて': 1313, 'わけ': 1314, 'ランキング': 1315, '参考': 1316, '空間': 1317, '能力': 1318, '云々': 1319, '特に': 1320, 'まくっ': 1321, 'に関する': 1322, '書き': 1323, '正直': 1324, '日本軍': 1325, '片道': 1326, '分': 1327, '燃料': 1328, '特攻': 1329, 'シルバー': 1330, 'ゴールド': 1331, '最大限': 1332, 'ポジション': 1333, '取れる': 1334, '敵味方': 1335, '打つ': 1336, '殺せる': 1337, '指導': 1338, '0日': 1339, '上がっ': 1340, 'プラチナ': 1341, 'リンクサ': 1342, 'わかる': 1343, '働い': 1344, '全': 1345, 'ら': 1346, '見せしめ': 1347, 'バン': 1348, '初動': 1349, 'イカれた': 1350, '行為': 1351, 'はず': 1352, 'クマ': 1353, 'なのは': 1354, 'ブリザード': 1355, '最大': 1356, 'ベータテスト': 1357, 'tabete': 1358, 'ダウンロード': 1359, '市役所': 1360, '待たさ': 1361, 'サクッと': 1362, 'かける': 1363, '書く': 1364, 'ザリーパー': 1365, '怖い': 1366, '周り': 1367, 'ちやほや': 1368, '感情': 1369, '満たす': 1370, 'ポストトゥルース': 1371, '追い求め': 1372, '代行': 1373, 'ブースト': 1374, 'じゃなくて': 1375, '自己顕示欲': 1376, '自分自身': 1377, '変化': 1378, '数値': 1379, '上下': 1380, 'のみ': 1381, '欺く': 1382, '平気': 1383, '行う': 1384, '精神': 1385, '問題': 1386, 'custa': 1387, '勝てる': 1388, '確率': 1389, 'ダイナスティ': 1390, '移籍': 1391, 'ボコボコ': 1392, 'にっこり': 1393, '当たる': 1394, 'とき': 1395, '九': 1396, '割': 1397, 'ダイヤ': 1398, 'VC': 1399, '言わ': 1400, '都合': 1401, '切り取っ': 1402, '悪者': 1403, '晒し': 1404, 'マウント': 1405, 'メンタル': 1406, 'Artisan': 1407, 'マウスパッド': 1408, 'アキバ': 1409, '大会': 1410, '履歴書': 1411, '手書き': 1412, '受ける': 1413, 'やめよ': 1414, '特筆': 1415, '資格': 1416, '自動車免許': 1417, 'いえ': 1418, 'もう': 1419, 'ツイート': 1420, '一年生': 1421, 'センス': 1422, '方向': 1423, '行っ': 1424, 'ブルドーザー': 1425, 'ぶっ殺し': 1426, 'いける': 1427, 'しおりん': 1428, '完全': 1429, '趣味': 1430, '合う': 1431, '合わせ': 1432, 'マッチ': 1433, 'ドンカツツ': 1434, '出来': 1435, 'スクアッドメンバー': 1436, '得ん': 1437, '強かっ': 1438, 'デスク': 1439, 'セットアップ': 1440, '椅子': 1441, '届い': 1442, 'バケツ': 1443, '腰': 1444, 'au': 1445, '営業': 1446, '月': 1447, '回線': 1448, '使える': 1449, '契約': 1450, 'キャズム': 1451, '新しいことを始めよう': 1452, '怪し': 1453, 'マックス': 1454, '頭': 1455, 'おかしい': 1456, 'られる': 1457, 'なかなか': 1458, '住民': 1459, 'うる': 1460, '睡眠': 1461, '起きる': 1462, '寮': 1463, '引っ越し': 1464, 'アメニティ': 1465, '失っ': 1466, 'ダンボール': 1467, '寝': 1468, '置く': 1469, '奥の手': 1470, '球': 1471, '瞬間': 1472, '陰影': 1473, '表現': 1474, '変わる': 1475, '手前': 1476, '親指': 1477, 'ピクセル': 1478, 'ボケ': 1479, 'かた': 1480, '荒く': 1481, '編集': 1482, '機械': 1483, '奴隷': 1484, 'キリヒト': 1485, '毎日': 1486, 'コメント': 1487, 'もらえ': 1488, 'うれしかっ': 1489, '住民票': 1490, 'そのまま': 1491, '元': 1492, '住ん': 1493, '他県': 1494, '委': 1495, '移そ': 1496, '必須': 1497, 'ファイル': 1498, 'PDFファイル': 1499, 'なんや': 1500, '公的': 1501, '色々': 1502, '出さ': 1503, '直後': 1504, 'また': 1505, 'だるい': 1506, '限り': 1507, 'それとも': 1508, 'ロゴデザイン': 1509, 'さくっと': 1510, 'ランサーズ': 1511, '依頼': 1512, '0件': 1513, '期待値': 1514, '収入': 1515, 'デザイナー': 1516, '業': 1517, '過酷': 1518, '悪貨が良貨を駆逐する': 1519, '典型': 1520, '調べる': 1521, 'IR': 1522, 'PR': 1523, '美男': 1524, '美女': 1525, 'ばかり': 1526, '威圧': 1527, '自己分析': 1528, 'まとめる': 1529, 'つ': 1530, 'ジュ': 1531, '聞く': 1532, '失礼': 1533, '払っ': 1534, '聞き': 1535, '有料': 1536, '利益': 1537, '折半': 1538, 'ソリューション': 1539, 'サブスク': 1540, 'ライブ': 1541, 'ドネート': 1542, '感覚': 1543, 'いけや': 1544, '持続可能': 1545, '生み出す': 1546, '稼げ': 1547, 'なんらかの': 1548, 'インセンティブ': 1549, '有名': 1550, 'インタビュー': 1551, 'おる': 1552, 'nNote': 1553, '関連': 1554, '手法': 1555, 'とる': 1556, '高所': 1557, 'ひっくり返す': 1558, '最強': 1559, 'おかげ': 1560, 'ドン勝': 1561, '涙': 1562, 'あまり': 1563, 'いろんな': 1564, '福岡': 1565, '暮らそ': 1566, '些細なこと': 1567, '十': 1568, '株式会社': 1569, 'グラディエーター': 1570, '揃っ': 1571, 'やす': 1572, 'マノ': 1573, 'てん': 1574, 'すき': 1575, '蘇生': 1576, 'かー': 1577, 'ぺやばすぎ': 1578, 'プロ選手': 1579, 'J': 1580, 'AKE': 1581, 'フラストレーション': 1582, 'たまる': 1583, '発言': 1584, 'シーガルミッキーデュオ': 1585, '別に': 1586, '補欠': 1587, 'ディス': 1588, '気に入ら': 1589, 'ラスカル': 1590, 'あ': 1591, 'あら': 1592, '終わり': 1593, 'きびし': 1594, '利他': 1595, '長期的': 1596, '生存戦略': 1597, 'なんの': 1598, '関心': 1599, '引く': 1600, '結びつい': 1601, '発達': 1602, '広範囲': 1603, '届け': 1604, '性質': 1605, '晒す': 1606, 'ぱっと': 1607, '人類の進化': 1608, '過程': 1609, '合理的': 1610, 'メリット': 1611, '強者': 1612, '卍': 1613, '直接': 1614, '面白かっ': 1615, '嬉しい': 1616, '是非': 1617, '感想': 1618, '伝え': 1619, 'あげ': 1620, 'うれ': 1621, 'ぴ': 1622, '大体': 1623, 'ゲー': 1624, 'フォー': 1625, 'ナイト': 1626, 'なし': 1627, '読め': 1628, '頼ん': 1629, 'だら': 1630, '提案': 1631, '美術': 1632, '壊れ': 1633, 'Ninja': 1634, 'SOLO': 1635, 'DUO': 1636, 'ワロタ': 1637, 'nDUO': 1638, 'かわいい': 1639, '見た目': 1640, '反し': 1641, '実力': 1642, '反映': 1643, 'シビア': 1644, 'ゲーム性': 1645, 'ヤマトン': 1646, '0勝': 1647, 'wosp': 1648, '気軽': 1649, '質問': 1650, 'でし': 1651, 'アドバイス': 1652, '元にし': 1653, 'シーズン': 1654, '十日': 1655, 'マスター': 1656, '考え': 1657, 'BR': 1658, '二位': 1659, 'どん': 1660, 'かつ': 1661, 'やたら': 1662, '建造': 1663, 'モンスター': 1664, '四': 1665, '建': 1666, '鉄筋コンクリート': 1667, 'マンション': 1668, '打ち込ん': 1669, 'キツ': 1670, 'pon': 1671, 'overwatch': 1672, '答え': 1673, '図': 1674, 'ミ': 1675, 'スっ': 1676, '東': 1677, '群': 1678, '左上': 1679, '右下': 1680, '違う': 1681, '回答': 1682, '特定': 1683, '縛っ': 1684, '条件': 1685, '満たし': 1686, '数学': 1687, '証明': 1688, '西': 1689, '逆': 1690, 'もしくは': 1691, '読ん': 1692, 'ツリー': 1693, '状': 1694, 'パターン': 1695, '出せる': 1696, 'pubg': 1697, '真面目': 1698, 'エンジョイゲーマー': 1699, '差出る': 1700, 'スクアット': 1701, 'でかい': 1702, '建造物': 1703, '戦う': 1704, 'w': 1705, 'クソアフィブログ': 1706, 'こん': 1707, '攻略サイト': 1708, 'レジェンド': 1709, 'だまさ': 1710, 'ミニガン': 1711, '笑': 1712, '発射': 1713, '秒': 1714, 'ジョーク': 1715, 'ウェブサービス': 1716, 'いかに': 1717, '経済的': 1718, '合理性': 1719, '持た': 1720, '価値': 1721, '追求': 1722, '非常': 1723, 'これから': 1724, 'がんばる': 1725, '合計': 1726, '何となく': 1727, '勘所': 1728, 'わかっ': 1729, 'GamerCoach': 1730, '他': 1731, '0か月': 1732, '悪かっ': 1733, '閉鎖': 1734, '途中': 1735, '面白く': 1736, 'そ': 1737, 'ゲーマーコーチ': 1738, '一年': 1739, '今年': 1740, '頑張る': 1741, '諸々': 1742, 'しんど': 1743, '喫煙': 1744, '三': 1745, 'Zunba': 1746, '気持ち': 1747, '辛い': 1748, 'ペット': 1749, '死ん': 1750, 'ツイー': 1751, '流れ': 1752, 'nSNS': 1753, '不': 1754, '動かし': 1755, '本来': 1756, '触れる': 1757, '触れ': 1758, 'しまう': 1759, 'よろしく': 1760, 'AutoChess': 1761, 'リスナー': 1762, 'TFT': 1763, '0万人': 1764, 'わろ': 1765, 'パクっ': 1766, '勝ち': 1767, '無知': 1768, 'バグ': 1769, '消し飛ん': 1770, 'ぬ': 1771, 'ザイル': 1772, 'くくっ': 1773, '薄氷': 1774, '一緒': 1775, '飛び込む': 1776, '利害関係': 1777, '結べ': 1778, '株': 1779, '使え': 1780, '長時間労働': 1781, 'ガシガシ': 1782, '貴重': 1783, '一日': 1784, '観戦': 1785, 'そして': 1786, '若く': 1787, '好きな人': 1788, 'やってき': 1789, 'おじさん': 1790, '視点': 1791, '一点': 1792, '尽きる': 1793, '平たく': 1794, 'ドメイン知識': 1795, 'ニーズ': 1796, '読み取っ': 1797, 'だからこそ': 1798, '盛り上げ': 1799, 'い人': 1800, '独自': 1801, '基づい': 1802, '当たら': 1803, 'すでに': 1804, '効果': 1805, '実証': 1806, 'ローカライズ': 1807, '独自性': 1808, '求める': 1809, '活動': 1810, '専門': 1811, 'discord': 1812, '置き換わる': 1813, '未来': 1814, '像': 1815, 'パクリ': 1816, '半年': 1817, '絶対': 1818, 'リリース': 1819, '当初': 1820, '評価': 1821, '緊張感': 1822, '良': 1823, '正義': 1824, '言い': 1825, 'Time': 1826, 'to': 1827, 'retire': 1828, 'ff0': 1829, 'リュック': 1830, '声優': 1831, 'ツボ': 1832, 'おかしく': 1833, 'ケルニッヒ': 1834, 'フレ': 1835, '暴言': 1836, '飛ばさ': 1837, 'ハリウッド': 1838, '第': 1839, 'ブロンゴ': 1840, 'LP': 1841, 'LOL': 1842, '対人': 1843, '戦': 1844, 'わざと': 1845, '放置': 1846, 'くれ': 1847, '下げ': 1848, '初心者狩り': 1849, '怒ら': 1850, '抜け': 1851, '厳しい': 1852, '紫電改': 1853, 'か月': 1854, '湿気': 1855, '引っ掛かり': 1856, 'やっぱり': 1857, 'ヒエン': 1858, 'ハルト': 1859, 'マップ': 1860, '少な': 1861, 'Dva': 1862, '突っ込ん': 1863, 'コントロールライン': 1864, 'よわ': 1865, '落ち': 1866, 'マウンティング': 1867, '正しい': 1868, '某': 1869, 'EMP': 1870, 'キング': 1871, 'スロー': 1872, '格下': 1873, 'チャージ': 1874, '当て': 1875, '殴っ': 1876, 'シャター': 1877, '防い': 1878, '決め': 1879, 'ハルザリデュオ': 1880, '見せつけ': 1881, '気持ち良': 1882, 'モイラ': 1883, '悪玉': 1884, 'えらい': 1885, '眠かっ': 1886, '肩身': 1887, 'せめ': 1888, '類友': 1889, '極み': 1890, 'widow': 1891, '0k': 1892, 'd': 1893, 'ファラ': 1894, 'かられ': 1895, 'クリティカル': 1896, '屈伸': 1897, '小指': 1898, '折れ': 1899, 'FFA': 1900, '神ゲー': 1901, 'しゃがみ': 1902, 'シフト': 1903, 'マウス': 1904, 'サイド': 1905, 'ボタン': 1906, '具': 1907, 'ラップリングフック': 1908, 'スパム': 1909, 'いれ': 1910, 'Widow': 1911, 'sniper': 1912, 'ググ': 1913, '探し': 1914, 'わかん': 1915, '下さい': 1916, 'Google': 1917, 'is': 1918, 'GOD': 1919, 'nGoogle': 1920, 'dominates': 1921, 'the': 1922, 'world': 1923, 'Google翻訳': 1924, '韓国語': 1925, '翻訳': 1926, '精度': 1927, '普通に': 1928, '会話': 1929, 'ビビる': 1930, 'ついで': 1931, 'OWBlog': 1932, 'デザイン': 1933, '変えよ': 1934, 'nSEO': 1935, 'HTML': 1936, 'CSS': 1937, 'Bootstrap': 1938, 'ニッチ': 1939, '対応': 1940, 'づらく': 1941, '選択': 1942, '強いる': 1943, 'ウェーブ': 1944, '回っ': 1945, 'ルート': 1946, 'タレット': 1947, 'こさ': 1948, 'にくい': 1949, '中途半端': 1950, '貯まっ': 1951, '迷い': 1952, 'づらい': 1953, '間違える': 1954, '火力': 1955, 'ヒートー': 1956, 'トールビョーン': 1957, 'ティア': 1958, 'メトラ': 1959, '次いで': 1960, 'だし': 1961, 'フィリー': 1962, 'EQO': 1963, 'シャドウバー': 1964, 'ゼニヤッタウルト': 1965, '編成': 1966, 'さす': 1967, 'ナノゼニ': 1968, 'ありか': 1969, 'しれ': 1970, '中の人': 1971, 'です': 1972, 'ハブ': 1973, '知る': 1974, '知ら': 1975, 'ブースター': 1976, '半分': 1977, '上昇': 1978, '真上': 1979, '飛ぶ': 1980, '目的': 1981, '気持ちよ': 1982, 'ぱねえ': 1983, '俳優': 1984, '目力': 1985, 'おもろい': 1986, 'ケインコスギ': 1987, 'チャンネル': 1988, 'トップチア': 1989, '池谷直樹': 1990, '苦しみ': 1991, 'ルシモイラ': 1992, '悪玉コレステロール': 1993, '飛ばし': 1994, '自慢': 1995, 'しよ': 1996, 'なちゅ': 1997, '北': 1998, 'コーチ': 1999, 'しれっと': 2000, '加入': 2001, 'しとる': 2002, '脳死': 2003, '感': 2004, 'そっち': 2005, 'ホグ': 2006, '奴': 2007, '小学生': 2008, 'ころ': 2009, 'サンダーボルト': 2010, 'ハーピイ': 2011, '設定': 2012, 'ゼニ': 2013, 'TIPS': 2014, 'どうり': 2015, 'クラメン': 2016, 'らしく': 2017, '検証': 2018, 'もっと': 2019, '入る': 2020, '反省': 2021, 'ブロック': 2022, '申請': 2023, 'ッ': 2024, 'くるん': 2025, '許可': 2026, '鼻水': 2027, 'くしゃみ': 2028, '止まら': 2029, '苦しい': 2030, 'ロン': 2031, '鯖': 2032, 'リアル': 2033, 'N': 2034, '勢い': 2035, 'アメリカ': 2036, '勢': 2037, '韓国': 2038, 'ボコっ': 2039, '同期': 2040, '就職': 2041, '旅立っ': 2042, 'uDE': 2043, 'ボディビル': 2044, '好きだから': 2045, '足': 2046, '太': 2047, '大腿四頭筋': 2048, '見える': 2049, 'rt': 2050, 'fav': 2051, 'すぐ': 2052, 'pv': 2053, '草生える': 2054, '飛燕': 2055, 'VE': 2056, 'バージョン': 2057, 'させ': 2058, '意味不明': 2059, '始めて': 2060, 'メイヘム': 2061, '虹彩': 2062, '実家': 2063, 'OP': 2064, '感謝': 2065, '土地': 2066, '戻っ': 2067, 'QOL': 2068, '爆上': 2069, 'りし': 2070, '泣い': 2071, '基本': 2072, '増やし': 2073, 'いき': 2074, 'How': 2075, 'get': 2076, 'Dia': 2077, '花粉症': 2078, 'ひどい': 2079, '政治家': 2080, '杉': 2081, '絶滅': 2082, '思わ': 2083, '深': 2084, 'ヒール': 2085, '写し': 2086, 'カメラ': 2087, '微妙': 2088, '真': 2089, '隣': 2090, '瞬': 2091, '離脱': 2092, '流行り': 2093, 'ドラゴンズ': 2094, 'フラッシュウルブズ': 2095, 'Diya': 2096, 'リップタイヤ': 2097, '時間切れ': 2098, '爆発': 2099, 'made': 2100, 'in': 2101, 'china': 2102, '埋まっ': 2103, 'フロリダ': 2104, 'OPC': 2105, 'デトネーター': 2106, 'サンシス': 2107, 'シュアフォー': 2108, 'なんと': 2109, '言えん': 2110, 'FISSURE': 2111, '大当たり': 2112, '手': 2113, '楽しく': 2114, 'スタダ': 2115, 'GG': 2116, 'そこら': 2117, 'サポート': 2118, '熱く': 2119, '丸の内': 2120, 'イタリアン': 2121, '昼間': 2122, '食い': 2123, 'だべる': 2124, '主婦': 2125, '来世': 2126, '平日': 2127, 'ちょっと': 2128, '高め': 2129, 'だいたい': 2130, '悪口大会': 2131, '集団': 2132, 'AVA': 2133, 'FF': 2134, 'わざわざ': 2135, 'アンインストール': 2136, '二度と': 2137, '復帰': 2138, '宣言': 2139, 'ブリジットクソ': 2140, 'いら': 2141, '増える': 2142, 'ベイングローリー': 2143, 'にくかっ': 2144, 'とにかく': 2145, '良質': 2146, 'ロル': 2147, 'ローセンシ': 2148, 'マック': 2149, 'トラックパッド': 2150, '操作': 2151, 'チャンピオン': 2152, '正面': 2153, '戦っ': 2154, 'レーン': 2155, 'コア': 2156, '壊し': 2157, 'ロ': 2158, 'る': 2159, '目やに': 2160, 'ハルザリ': 2161, '不明': 2162, 'ファック': 2163, 'だの': 2164, 'オーマイガー': 2165, 'ダフラン': 2166, 'いつ': 2167, 'もお': 2168, 'おっ': 2169, '熱意': 2170, '裁判': 2171, '弁護士ドットコム': 2172, 'バクマン': 2173, '岩瀬': 2174, '人間味': 2175, 'S': 2176, 'サポ': 2177, '山崎': 2178, '代打': 2179, '演説': 2180, 'イチロー': 2181, 'ファン': 2182, '反論': 2183, '中間管理職': 2184, 'トネガワ': 2185, 'ギャグ漫画': 2186, '深い': 2187, 'コミュ力': 2188, '辛いっ': 2189, '大学': 2190, 'つら': 2191, 'Tips': 2192, '空港': 2193, '予定': 2194, '夜': 2195, '助かっ': 2196, '高松空港': 2197, '松山空港': 2198, '愛媛': 2199, '香川': 2200, 'しまっ': 2201, 'なう': 2202, 'エアギア': 2203, '登場': 2204, 'ジェイク': 2205, 'ジェーーーイク': 2206, '叫ん': 2207, 'メンヘラ': 2208, 'かまってちゃん': 2209, 'ゼロ': 2210, '今度': 2211, 'ザリアピック': 2212, '年': 2213, 'こ': 2214, 'スタンダード': 2215, '役に立っ': 2216, 'おｋ': 2217, 'やっと': 2218, 'みずほ': 2219, '口座': 2220, 'ネット': 2221, 'バンク': 2222, '使用': 2223, '手数料': 2224, '振込手数料': 2225, '0時': 2226, '鬼': 2227, '仕様': 2228, '困り': 2229, '文章': 2230, 'まさか': 2231, '行': 2232, '申し込む': 2233, '羽目': 2234, '住信SBIネット銀行': 2235, '良い': 2236, 'スタートアップ': 2237, '申し込ん': 2238, '難易度': 2239, '遅れ': 2240, 'ｔ': 2241, 'サービス開始': 2242, '全然': 2243, '潮流': 2244, 'っぽい': 2245, '銀行': 2246, '修正': 2247, '箇所': 2248, 'はん': 2249, '押し': 2250, 'てぃー': 2251, '令和': 2252, '人並': 2253, 'IT': 2254, 'ってな': 2255, 'っけ': 2256, '高齢化': 2257, '軍隊': 2258, '式': 2259, '教育': 2260, 'による': 2261, 'オープン': 2262, 'マインド': 2263, '欠如': 2264, 'どうにも': 2265, 'Discord': 2266, '鯖落ち': 2267, 'ビデオ': 2268, '通話': 2269, 'サーバー': 2270, '復活': 2271, '送信': 2272, '危ない': 2273, 'やすく': 2274, 'ATM': 2275, 'パスワード': 2276, '空い': 2277, '窓口': 2278, '行か': 2279, '行け': 2280, '規制': 2281, '守ら': 2282, '昭和': 2283, '苦しめ': 2284, '現金': 2285, '盗難': 2286, 'ミス': 2287, '手元': 2288, 'ひきおろす': 2289, '円': 2290, '害悪': 2291, 'ツール': 2292, '罰金': 2293, 'かけ': 2294, 'コワーキングスペース': 2295, '意識高い': 2296, '蕁麻疹': 2297, '言え': 2298, '最新': 2299, 'ある程度': 2300, 'つい': 2301, '適応': 2302, '拡散': 2303, '新参': 2304, '聞き取れ': 2305, '見れ': 2306, 'もったいない': 2307, 'せめて': 2308, '字幕': 2309, '実装': 2310, 'くん': 2311, 'ねー': 2312, 'Skype': 2313, '音声': 2314, '認識': 2315, 'あらゆる': 2316, 'ストリーミング': 2317, 'めちゃ': 2318, 'クチャ': 2319, '起用': 2320, 'ソルジャー': 2321, '得意': 2322, 'うける': 2323, 'ダイブ': 2324, 'バック': 2325, '生かせる': 2326, '判断': 2327, '悲しい': 2328, '平地': 2329, 'Owl': 2330, '公式': 2331, 'アプリ': 2332, 'タブレット端末': 2333, 'fissure': 2334, '帝国': 2335, '竜田揚げ': 2336, 'レパートリー': 2337, 'チーム名': 2338, 'カタカナ': 2339, '文字': 2340, '集中': 2341, 'まわし': 2342, '徹夜': 2343, 'ow': 2344, 'ティルト': 2345, '下げる': 2346, 'あげる': 2347, '不眠': 2348, '回し': 2349, '落とし': 2350, 'ウホウホ': 2351, '明日': 2352, '謎': 2353, '終わっ': 2354, '寝る': 2355, 'サブ': 2356, 'Bz': 2357, 'ORANGE': 2358, 'RANGE': 2359, '聞け': 2360, '体': 2361, '育っ': 2362, '役に立つ': 2363, '自動': 2364, '生成': 2365, 'もと': 2366, 'ネイティブ': 2367, '聞き取る': 2368, 'Soon': 2369, 'スー': 2370, '為': 2371, '手が込ん': 2372, 'Youtuber': 2373, '結局': 2374, '立ち回り': 2375, 'ダーツ': 2376, '残っ': 2377, '確定': 2378, 'モーション': 2379, '反応': 2380, 'マトリクス': 2381, '貼る': 2382, '余裕': 2383, 'メンバー': 2384, '招集': 2385, '触っ': 2386, 'クイック': 2387, 'ぱすわど': 2388, '印象深い': 2389, '夢見': 2390, '拠点': 2391, '踏ま': 2392, 'きん': 2393, 'Jesl': 2394, 'なれる': 2395, '開ける': 2396, '0秒': 2397, '二日': 2398, '冊': 2399, '本読': 2400, '家探': 2401, '仲介業者': 2402, 'ボリ': 2403, '0月': 2404, '引っ越す': 2405, 'プロパイダ': 2406, 'しのう': 2407, 'アホ': 2408, '主張': 2409, '根拠': 2410, 'ソース': 2411, '無し': 2412, '一部': 2413, '記述': 2414, 'ページ': 2415, '捨て': 2416, '変える': 2417, '男': 2418, 'イーロンマスク': 2419, 'つま': 2420, '著者': 2421, 'サーベイ': 2422, '不足': 2423, '参考文献': 2424, 'ないっ': 2425, 'ていう': 2426, '加え': 2427, '過度': 2428, '原発': 2429, '批判': 2430, 'rox': 2431, 'orcas': 2432, 'ロゴ': 2433, '変換': 2434, '背景': 2435, '抜い': 2436, 'パク': 2437, 'いくら': 2438, '見つかり': 2439, 'コンテンダーズ': 2440, '非公式': 2441, '消え': 2442, 'アカデミー': 2443, 'そういや': 2444, 'リザーブ': 2445, 'つもり': 2446, 'ナメクジ': 2447, '努める': 2448, 'ESC': 2449, '流行らす': 2450, 'OASIS': 2451, '二つ': 2452, 'SUP': 2453, '低かっ': 2454, '個人': 2455, '信用': 2456, 'ドタキャン': 2457, 'オーブ': 2458, '割合': 2459, 'ヌンバニ': 2460, 'ヒット': 2461, 'スキャン': 2462, 'アリ': 2463, 'キラー': 2464, 'メイ': 2465, '強く': 2466, 'やん': 2467, 'リミテッド': 2468, '楽しかっ': 2469, '右': 2470, '左': 2471, 'ダンテ': 2472, 'xqc': 2473, 'シナトラ': 2474, '全員': 2475, '協力': 2476, 'ついて': 2477, 'ふざけ': 2478, '0分': 2479, 'タイマー': 2480, '腹': 2481, '痛かっ': 2482, 'ひゅーーーーーーーーーー': 2483, 'ーー': 2484, 'じ': 2485, 'ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ': 2486, 'ウイイレ': 2487, 'メッシ': 2488, 'クリロナ': 2489, '入れる': 2490, 'アレ': 2491, 'シーガル': 2492, '出番': 2493, 'COC': 2494, 'よー': 2495, 'hz': 2496, 'しきら': 2497, 'ディスプレイ': 2498, 'おもっ': 2499, '裸の王様': 2500, '0年': 2501, 'たっ': 2502, 'ウィンドウズ': 2503, 'Nvidia': 2504, 'かん': 2505, 'lol': 2506, 'フェーカー': 2507, 'いかん': 2508, '真ん中': 2509, 'よる': 2510, 'ヘリックスジャンプ': 2511, '躱せ': 2512, '事故死': 2513, 'リスク': 2514, '背負っ': 2515, 'ぶっちぎり': 2516, 'うまかっ': 2517, 'nas': 2518, 'ty': 2519, 'RUMATA': 2520, 'OTP': 2521, '昔': 2522, '0kg': 2523, '0cm': 2524, '適正': 2525, '体重': 2526, '表': 2527, 'ガリガリ': 2528, 'ジャスト': 2529, 'モイラウルト': 2530, '思い': 2531, 'プレッシャー': 2532, 'CTF': 2533, 'ルシオ': 2534, 'デスマラソン': 2535, 'ソルマク': 2536, 'サウンドバリア': 2537, '完璧': 2538, 'ロンドン': 2539, 'nyxl': 2540, 'もっか': 2541, 'かい': 2542, 'つえ': 2543, 'バードリングキレキレ': 2544, 'Saebyelobe': 2545, 'NYXL': 2546, 'スピットファイア': 2547, 'アツ': 2548, 'バードリングクソイケメン': 2549, 'ルシオボール': 2550, 'ルール': 2551, '対面': 2552, '殴り合い': 2553, '勝負': 2554, '勝つ': 2555, '残酷': 2556, 'トールメトラ': 2557, 'サッカー': 2558, '上がれ': 2559, 'ディフェンス': 2560, '配置': 2561, 'もんじゃ': 2562, 'タン': 2563, 'フラッグ': 2564, 'スピブ': 2565, '運べ': 2566, 'カンカン': 2567, 'ダスト': 2568, 'もらえる': 2569, 'フルパ': 2570, '現在': 2571, 'アカウント': 2572, 'ctf': 2573, 'ガイジ': 2574, 'ドール': 2575, '待っ': 2576, 'ガン': 2577, 'タキ': 2578, 'メトラビョーン': 2579, '守り': 2580, '嫌がっ': 2581, '逃げ': 2582, 'トリプルキル': 2583, '取っ': 2584, '囚人のジレンマ': 2585, '一連': 2586, '高校時代': 2587, '教師': 2588, 'ども': 2589, '怒り': 2590, '蘇っ': 2591, 'おこ': 2592, 'じゃん': 2593, '帰り': 2594, 'てえ': 2595, '久々': 2596, '大阪': 2597, 'きた': 2598, 'まんがな': 2599, 'だらだら': 2600, '暮らし': 2601, '経済': 2602, '自立': 2603, '起業': 2604, 'スモールビジネス': 2605, '労働': 2606, 'めんどく': 2607, '親夜': 2608, 'ダラダラ': 2609, 'twitch': 2610, 'シコシコ': 2611, '便利': 2612, 'ゲグリシャター': 2613, 'かわし': 2614, 'igs': 2615, 'なっちゃった': 2616, '履い': 2617, '適性': 2618, 'モイラマジ': 2619, 'ビーム': 2620, '無理やり': 2621, 'バレッジ': 2622, '安心': 2623, '打てる': 2624, '罪悪感': 2625, '迷わ': 2626, 'ポンポン': 2627, '付': 2628, '老い': 2629, 'マーシーナーフ': 2630, '以降': 2631, 'キュートマーシーアイコン': 2632, '嫌': 2633, '予感': 2634, '友達': 2635, '呼ば': 2636, '退出': 2637, '持っ': 2638, 'かれ': 2639, '飛行機': 2640, 'バリアント': 2641, 'だいぶ': 2642, 'えっ': 2643, 'つよ': 2644, '中村': 2645, '藤田': 2646, '名誉回復': 2647, 'あたり': 2648, 'ヤバ': 2649, 'ルシゼニモイラ': 2650, '弱い': 2651, '花村': 2652, 'チョーク': 2653, 'きつい': 2654, 'マーシーピック': 2655, 'パラディンズ': 2656, '連合軍': 2657, 'こいつ': 2658, '逆ギレ': 2659, '未検証': 2660, '始まっ': 2661, 'ログアウト': 2662, '低下': 2663, 'グリッチ': 2664, '発見': 2665, 'かもしれん': 2666, 'ディバ': 2667, '悪く': 2668, 'どうにか': 2669, '厳しさ': 2670, '四月': 2671, 'まとも': 2672, 'に関して': 2673, '江尻': 2674, '勝': 2675, '0敗': 2676, '後半': 2677, 'だれ': 2678, '達': 2679, '台湾': 2680, 'アジア': 2681, 'プロリーグ': 2682, '参戦': 2683, '実感': 2684, 'そうだ': 2685, '日本チーム': 2686, '応援': 2687, '伴わ': 2688, '次第に': 2689, 'ワザップ': 2690, 'フォーカース': 2691, '中央集権': 2692, 'メディア': 2693, '熱量': 2694, '生かす': 2695, '難しく': 2696, '解決': 2697, '図書館': 2698, '仕組み': 2699, '作れる': 2700, 'エンパワーメント': 2701, '連鎖': 2702, '続い': 2703, 'オバフスクレイピング': 2704, '閾値': 2705, '超え': 2706, '更新': 2707, '続ける': 2708, '戦績': 2709, '面白': 2710, 'マクリー': 2711, '変遷': 2712, '今週': 2713, '今月': 2714, '比較': 2715, 'グラ': 2716, 'マス': 2717, '近く': 2718, 'スチーム': 2719, '管理': 2720, 'MOD': 2721, 'OK': 2722, 'オート': 2723, 'チェス': 2724, 'Steam': 2725, '商用': 2726, '利用': 2727, 'ゆるく': 2728, 'Mod': 2729, 'パクる': 2730, '流行っ': 2731, 'カオス': 2732, 'ゲーム版': 2733, 'Qiita': 2734, '天命': 2735, '授け': 2736, '以内': 2737, 'クラ': 2738, 'チーム作り': 2739, 'サムネ': 2740, '職人': 2741, '泥臭く': 2742, '自己': 2743, 'ブランディング': 2744, '対極': 2745, 'ぜひとも': 2746, '意思決定': 2747, '自腹': 2748, '我々': 2749, '血税': 2750, '介護': 2751, '環境保全': 2752, '回さ': 2753, '流行らし': 2754, 'いし': 2755, '暴力': 2756, 'ノリ': 2757, '開か': 2758, 'エモい': 2759, '在留カード': 2760, '取り上げ': 2761, '選手': 2762, '嫌がらせ': 2763, '管理者': 2764, '立場': 2765, '外国人実習生': 2766, '取り上げる': 2767, '弱み': 2768, 'うえ': 2769, '最悪': 2770, 'ナチュ': 2771, '被っ': 2772, '見学': 2773, 'KR': 2774, 'すら': 2775, '明らか': 2776, 'オリーサ': 2777, 'スパイス': 2778, 'オフ会': 2779, '一つ': 2780, '深層学習': 2781, '用い': 2782, '統計': 2783, '分析': 2784, '出力': 2785, '入力': 2786, '予想': 2787, 'ツッコミどころ': 2788, '高校': 2789, '出て': 2790, '公務員': 2791, '千': 2792, '保証': 2793, 'もはや': 2794, '高校テニス': 2795, '規模': 2796, '悲惨': 2797, '◦': 2798, '事故現場': 2799, 'ゲグリ': 2800, '頑張っ': 2801, 'Taimou': 2802, 'け': 2803, 'cocco': 2804, '嫌い': 2805, 'lt': 2806, '↑': 2807, 'ワン': 2808, '会場': 2809, '歓声': 2810, '上がる': 2811, 'ボストン': 2812, 'ニューヨーク': 2813, 'ニート': 2814, '二人': 2815, '内': 2816, '大学生': 2817, '高校生': 2818, 'たしなん': 2819, 'どうして': 2820, '時給': 2821, '桁': 2822, 'mbps': 2823, '流石': 2824, 'ggwp': 2825, '研究室': 2826, 'おしゃれ': 2827, 'owl': 2828, '始まる': 2829, 'ギリギリ': 2830, 'ゼニモイラ': 2831, 'ナーフ': 2832, '名称': 2833, '連携': 2834, '賞金': 2835, '合法': 2836, '支払う': 2837, '新た': 2838, '反発': 2839, 'パズドラプロフォロワー': 2840, 'LONDON': 2841, 'KDP': 2842, 'GCB': 2843, '構成': 2844, 'APEX': 2845, 'VOID': 2846, 'ましてや': 2847, 'あんなに': 2848, 'jasper': 2849, 'チャレ': 2850, '右クリック': 2851, '上げろ': 2852, 'ドヤ': 2853, '悔しさ': 2854, 'バネ': 2855, '成り立っ': 2856, '偉い': 2857, '歪め': 2858, 'どうこう': 2859, '論調': 2860, '現実': 2861, '取り合い': 2862, '強め': 2863, '権化': 2864, '知り合い': 2865, '顔写真': 2866, '枚': 2867, 'AV': 2868, '出演': 2869, '技術的': 2870, '確実': 2871, 'ゴミ': 2872, 'さっ': 2873, '引っ越そ': 2874, 'スクリム': 2875, '重': 2876, 'フック': 2877, 'つられ': 2878, '中身': 2879, '制限': 2880, '時代': 2881, 'ゲンジ': 2882, '属': 2883, '風切り': 2884, '突っ込め': 2885, 'さよなら': 2886, 'でれー': 2887, 'ぶ': 2888, '犯罪': 2889, '仮想通貨': 2890, '度合い': 2891, '応じ': 2892, 'カルマ': 2893, 'ポイント': 2894, '増加': 2895, 'ラウンド': 2896, '等間隔': 2897, 'TOP': 2898, '次元': 2899, '身の回り': 2900, 'すべて': 2901, 'ウェーブサージ': 2902, 'バリア': 2903, '張ら': 2904, 'csgo': 2905, '詳しく': 2906, 'スマーフ': 2907, 'パーティー': 2908, '勝て': 2909, '爽快感': 2910, 'デブ': 2911, 'XQ': 2912, 'お墨付き': 2913, 'さすが': 2914, 'むに': 2915, '伸び': 2916, 'あるとき': 2917, 'ガンガン': 2918, '詰め': 2919, '取って': 2920, '逃げ道': 2921, 'ボイチェン': 2922, '許さ': 2923, 'miku': 2924, '太い': 2925, '指示': 2926, 'スタンプ': 2927, 'ギザギザ': 2928, 'がき': 2929, '教授': 2930, '面談': 2931, '論文': 2932, '本': 2933, '夢み': 2934, 'おもれ': 2935, 'えぐ': 2936, '食らわ': 2937, 'タイミング': 2938, '徹底': 2939, 'ファ': 2940, 'ラマ': 2941, '攻防': 2942, 'ポジ': 2943, 'ふけ': 2944, 'おめでとう': 2945, '間違えれ': 2946, 'デッドアイ': 2947, '警戒': 2948, 'キャップ': 2949, '番頭': 2950, '援護': 2951, '視界': 2952, '広く': 2953, '決める': 2954, '繰り返し': 2955, '延々と': 2956, 'ランクイン': 2957, '集計': 2958, '対象': 2959, '万人': 2960, '難し': 2961, 'パ': 2962, '入ら': 2963, '拷問': 2964, '時間帯': 2965, '電波': 2966, '激': 2967, 'ジャンク': 2968, '一生': 2969, 'ドラド': 2970, '力不足': 2971, '刺さっ': 2972, '田舎': 2973, 'スーパーチャージャー': 2974, '盾突き': 2975, '置い': 2976, '倒す': 2977, 'パクツイ': 2978, 'くそ': 2979, 'ジャンクラ': 2980, '間違い': 2981, 'インキャ': 2982, '所属': 2983, 'よろしくお願いします': 2984, '集まん': 2985, 'メンバー募集': 2986, 'ちゃっかり': 2987, '載せる': 2988, 'マウントゴックス': 2989, '被害額': 2990, '草草': 2991, 'シャム': 2992, '大人': 2993, '金づる': 2994, 'かわいそう': 2995, '韓国人': 2996, '国内': 2997, '他国': 2998, 'リーグ': 2999, '完成': 3000, '優位': 3001, 'なくなっ': 3002, 'シャドウ': 3003, 'バーン': 3004, 'Carpe': 3005, 'ロマン': 3006, 'わあ': 3007, 'フュージョン': 3008, 'SBB': 3009, 'ネトゲ': 3010, 'レーティング': 3011, '決まっ': 3012, 'いいね': 3013, 'アニオタ': 3014, '界隈': 3015, '学歴': 3016, '職業': 3017, '地位': 3018, 'アニメ業界': 3019, 'どれ': 3020, 'アニメ': 3021, '表現技法': 3022, '行わ': 3023, 'ダル': 3024, 'コミケ': 3025, '批評': 3026, '文': 3027, '盛ん': 3028, '血で血を洗う': 3029, 'いわ': 3030, 'weeked': 3031, '裏取り': 3032, '積極的': 3033, '着': 3034, '逃げれ': 3035, 'Dafran': 3036, '今すぐ': 3037, '入り': 3038, 'くどい': 3039, '絵': 3040, '淡白': 3041, '投票': 3042, 'ぇむって': 3043, 'マンガ': 3044, 'サイコ': 3045, '可愛さ': 3046, '独特': 3047, '織田信長': 3048, '信長': 3049, 'キルログ': 3050, '維持': 3051, 'がん': 3052, 'ばろん': 3053, 'つり革': 3054, 'つかまら': 3055, '満員電車': 3056, '思い切り': 3057, 'もたれかかっ': 3058, 'iCloud': 3059, 'オフ': 3060, '不可能': 3061, 'オフタンク': 3062, '立つ': 3063, '鳥': 3064, '濁す': 3065, 'その後': 3066, '最も': 3067, 'ちなみ': 3068, '銀だこ': 3069, '塩': 3070, 'マヨネーズ': 3071, '離れ': 3072, '弱': 3073, '一個': 3074, '東大': 3075, '地方': 3076, '駅弁': 3077, '国立': 3078, '魅力': 3079, '殴り': 3080, '合い': 3081, '佐藤かよ': 3082, '可愛い': 3083, '覚える': 3084, '苦手': 3085, '長く': 3086, '生き延びる': 3087, 'サポタン': 3088, 'ファース': 3089, 'トピック': 3090, 'つか': 3091, '市役所職員': 3092, 'ガチガチ': 3093, '固め': 3094, '税金': 3095, 'nCERO': 3096, 'A': 3097, '認め': 3098, '強気': 3099, 'っぷり': 3100, '優勝賞金': 3101, '決して': 3102, 'ガラパゴス化': 3103, 'ちまっ': 3104, '専攻': 3105, '漏れ': 3106, 'ショート': 3107, '育成': 3108, 'インフルエンサー': 3109, '支援': 3110, 'その間': 3111, 'ティーチング': 3112, '投げ銭': 3113, '稼ぐ': 3114, '素晴らし': 3115, '文字通り': 3116, '桁違い': 3117, 'グルメアプリ': 3118, '困っ': 3119, 'データベース': 3120, '頼れる': 3121, '体感': 3122, 'こんなに': 3123, '流動性': 3124, '激しい': 3125, 'nリーグ': 3126, 'ソウル': 3127, 'ラーメン屋': 3128, '見つけ': 3129, '表せ': 3130, 'マーケティング': 3131, '店': 3132, '雰': 3133, '囲': 3134, '看板': 3135, 'っぽ': 3136, 'さは': 3137, '丁': 3138, '肝心': 3139, '味': 3140, 'おざなり': 3141, 'めまい': 3142, 'スマホチェス': 3143, '0g': 3144, 'ガチャ': 3145, '回す': 3146, '0連勝': 3147, '気持ちよく': 3148, 'タイマン': 3149, '打ち': 3150, '若干': 3151, 'うち': 3152, 'ベター': 3153, '隣人': 3154, 'うるさいっ': 3155, 'プライド': 3156, '匿名': 3157, '見せる': 3158, 'パルス': 3159, '突撃': 3160, 'ビビっ': 3161, 'たまに': 3162, '竜': 3163, '撃破': 3164, '食らっ': 3165, 'させる': 3166, 'たま': 3167, '議論': 3168, '反対': 3169, 'キャラコ': 3170, 'ン': 3171, '下手': 3172, 'ゲーム内': 3173, '煽り': 3174, '煽ら': 3175, 'ムカ': 3176, '辛く': 3177, '白': 3178, '弱く': 3179, 'JAKE': 3180, '定点': 3181, 'コンカッション': 3182, 'とい': 3183, '残し': 3184, '逃げる': 3185, 'リスポーンポコポコスパム': 3186, 'ジワジワ': 3187, '戦中': 3188, 'たまらない': 3189, '吸収': 3190, '不利': 3191, '延命': 3192, '貯める': 3193, 'ヒーローキャリー': 3194, '平均': 3195, '奪う': 3196, 'らす': 3197, 'ごく楽': 3198, '称号': 3199, 'ついてる': 3200, 'ww': 3201, 'グラマスウィドウ': 3202, 'おれ': 3203, 'ちなみに': 3204, 'PV': 3205, 'フォロワー': 3206, '広報': 3207, '発信': 3208, 'リーチ': 3209, 'だから': 3210, 'もらい': 3211, '聖典': 3212, '気合い': 3213, 'もう一度': 3214, 'PS0': 3215, 'まず': 3216, 'マウサー': 3217, 'なろ': 3218, '強調': 3219, '段差': 3220, '頭ぶ': 3221, 'フレタ': 3222, '高': 3223, 'メック': 3224, 'ぶつけれ': 3225, 'オアシス': 3226, 'ルシオモイラ': 3227, 'Tviq': 3228, '好きなんだけど': 3229, 'アザ': 3230, 'ラック': 3231, 'プール': 3232, '広い': 3233, '専門性': 3234, 'がっつり': 3235, '感銘': 3236, 'ディスコード': 3237, '釣る': 3238, '同時に': 3239, '書き込ん': 3240, 'すごく': 3241, '緊張': 3242, '走る': 3243, '担当': 3244, '正直しんどい': 3245, 'っと': 3246, '破壊力': 3247, 'のう': 3248, 'ざさ': 3249, 'おかしな': 3250, 'モルテンコア': 3251, '返り討ち': 3252, 'えぐい': 3253, 'torb': 3254, '注意': 3255, '引き続け': 3256, 'トールビョーンマジ': 3257, 'ライトユーザー': 3258, '脱オタク': 3259, 'ペディア': 3260, '我': 3261, '内容': 3262, '書け': 3263, '読み返し': 3264, 'にとって': 3265, '良く': 3266, '少ない': 3267, '少なく': 3268, '教科書': 3269, '得': 3270, 'Re': 3271, 'メンバー全員': 3272, 'マーシーウルト': 3273, 'うつ': 3274, 'ぶれる': 3275, '側面': 3276, '分岐': 3277, 'nRIP': 3278, 'バイザー': 3279, 'ささる': 3280, 'グラビトンサージ': 3281, '重要性': 3282, '自信': 3283, 'タイン': 3284, '即': 3285, 'ピ': 3286, '地獄': 3287, '帯': 3288, 'saebyeolbe': 3289, '間合い': 3290, '取り': 3291, '美しく': 3292, '芸術': 3293, 'スパイ': 3294, 'ギア': 3295, 'よん': 3296, 'オバペディア': 3297, 'データセット': 3298, 'なに': 3299, '読み込ん': 3300, 'プログラミング': 3301, '奨学金': 3302, '薄く': 3303, '配る': 3304, '狭く': 3305, '太く': 3306, '配っ': 3307, '優秀': 3308, '後輩': 3309, 'しょう': 3310, 'バイト': 3311, '勿体無く': 3312, 'しんどく': 3313, 'google翻訳': 3314, '過ぎる': 3315, 'Lasty': 3316, 'イリダータ': 3317, 'ほか': 3318, '悔しく': 3319, '奇声': 3320, '上げる': 3321, '数年': 3322, 'nOverwatch': 3323, '悪影響': 3324, 'ストレス': 3325, '与え': 3326, '重度': 3327, '入院': 3328, '至る': 3329, '悪質': 3330, 'ドラッグ': 3331, '驚い': 3332, 'ってか': 3333, '軸': 3334, '盛り上げる': 3335, '営利目的': 3336, '好ま': 3337, '求め': 3338, 'かって': 3339, 'ローグ': 3340, '母体': 3341, '支配': 3342, 'コピペ': 3343, 'スクショ': 3344, 'txt': 3345, '落とし込め': 3346, 'D0': 3347, 'watch': 3348, 'アップライジング': 3349, '戦い方': 3350, 'マクロ': 3351, '調べれ': 3352, '平等': 3353, '機会': 3354, '親': 3355, 'デジタルディバイド': 3356, 'たどり着け': 3357, '個々人': 3358, '国立大学': 3359, '持ちだし': 3360, 'センター': 3361, '鑑': 3362, 'センター試験': 3363, 'やな': 3364, '受験': 3365, '不祥事': 3366, '起きれ': 3367, '試験': 3368, 'やり直し': 3369, 'おお': 3370, '日本時間': 3371, 'からか': 3372, 'うてる': 3373, 'NY': 3374, '仕方': 3375, 'おやすみなさい': 3376, '違': 3377, 'く': 3378, '龍神': 3379, '剣': 3380, 'キャンセル': 3381, '環境': 3382, 'コントロール': 3383, '活躍': 3384, 'スーパーエイム': 3385, '期待': 3386, 'Apex': 3387, 'LH': 3388, '無線マウス': 3389, '無線': 3390, 'xQc': 3391, 'シャターサージ': 3392, '返さ': 3393, 'マジゴミ': 3394, 'らっと': 3395, '局所': 3396, '源': 3397, '自体': 3398, '消し': 3399, 'ちゃう': 3400, 'イメージ': 3401, '土管': 3402, 'fleta': 3403, 'TOBI': 3404, '焦り': 3405, 'だす': 3406, 'リーパー': 3407, 'Fleta': 3408, 'ちい': 3409, '高度': 3410, '個人技': 3411, '理不尽': 3412, '生まれ': 3413, 'チップスマジ': 3414, 'やわー': 3415, 'り': 3416, 'ゅ': 3417, 'トイレ': 3418, 'HS': 3419, 'ウイドウ': 3420, 'お互い': 3421, 'ぶち': 3422, '抜き': 3423, '下手くそ': 3424, '腐っ': 3425, '引き連れ': 3426, 'げんなり': 3427, 'スピード感': 3428, 'テンセント': 3429, '忙し': 3430, '楽しむ': 3431, '向上': 3432, '打ち勝ち': 3433, '味わう': 3434, 'パブ': 3435, 'リッシャ': 3436, 'アイデア': 3437, '覇権': 3438, '握っ': 3439, 'ちゃ': 3440, 'Auto': 3441, 'Chess': 3442, 'iOS': 3443, 'パクリゲー': 3444, '進化': 3445, '段階': 3446, '広告費': 3447, 'かかわら': 3448, '件': 3449, 'すで': 3450, '本家': 3451, '運命': 3452, '土日': 3453, '追加': 3454, '発表': 3455, '合宿': 3456, 'おやすみ': 3457, '系': 3458, '視聴': 3459, '置き換える': 3460, '撃ち殺し': 3461, '暴れる': 3462, 'ごり押し': 3463, 'アップデート': 3464, '本物': 3465, 'アイデンティティ': 3466, '概念': 3467, '埋もれ': 3468, 'ルナ': 3469, '頃': 3470, 'お題': 3471, 'グループ': 3472, 'アップ': 3473, 'エゴサ': 3474, 'オススメ': 3475, '何人': 3476, '惑わさ': 3477, '描い': 3478, 'かこ': 3479, 'LimitBreaks': 3480, '青年': 3481, '勇士': 3482, '喋り': 3483, '伝える': 3484, 'ほん': 3485, 'XQQ': 3486, '態度': 3487, '有意義': 3488, 'スナイプトロール': 3489, 'pichu': 3490, 'たん': 3491, '咎め': 3492, '怪しい': 3493, 'ウォッチ': 3494, '切り替え': 3495, '待機': 3496, 'カッコ': 3497, '一覧': 3498, '隠せる': 3499, 'ユーモア': 3500, '振り返る': 3501, '回数': 3502, 'ゼニャッタ': 3503, 'てこ': 3504, 'いつう': 3505, 'め': 3506, '限界': 3507, '撤廃': 3508, '遠慮なく': 3509, 'バスティオン': 3510, '浴び': 3511, '続け': 3512, 'アーマー': 3513, '受けれ': 3514, 'カット': 3515, '0発': 3516, 'スケ': 3517, 'べし': 3518, '選び': 3519, '反則': 3520, '級': 3521, '運転手': 3522, 'じゃない方': 3523, 'セーフ': 3524, '助っ人': 3525, 'nS': 3526, 'FUCK': 3527, 'くき': 3528, '前期': 3529, '泣き': 3530, '背筋': 3531, '立て': 3532, 'どんどん': 3533, 'キチガイ': 3534, '戻し': 3535, '善意': 3536, '悪意': 3537, '役に立た': 3538, '公平': 3539, '働く': 3540, '引っ張り': 3541, 'がり': 3542, 'ノイジーマイノリティ': 3543, '回転寿司': 3544, '生ん': 3545, '文化': 3546, 'この世': 3547, 'カルビン': 3548, 'デッドアイキャンセルリロード': 3549, '大好き': 3550, '寝起き': 3551, '地震速報': 3552, '走馬灯': 3553, '見かけ': 3554, 'otp': 3555, '隠し': 3556, '通常': 3557, 'ワンチャン': 3558, 'おわ': 3559, 'コンピョーターサイエンス': 3560, 'オタク': 3561, 'たち': 3562, '学問': 3563, 'パンチ': 3564, '挟む': 3565, '節約': 3566, '壊す': 3567, '増やす': 3568, '族': 3569, 'キルタイム': 3570, 'あきまん': 3571, 'ストファイ': 3572, '開示': 3573, '透明性': 3574, '健全': 3575, 'Legal': 3576, 'action': 3577, 'will': 3578, 'e': 3579, 'taken': 3580, 'ネタ': 3581, '玉': 3582, '半径': 3583, 'メートル': 3584, '何度': 3585, '角度': 3586, 'パーセント': 3587, '反射': 3588, 'まっすぐ': 3589, '向かっ': 3590, 'クネ': 3591, '貧者': 3592, 'VR': 3593, '自己愛': 3594, '宗教': 3595, 'マクリートレーサー': 3596, 'ざる': 3597, '解消': 3598, '限定': 3599, '思わず': 3600, '高校受験': 3601, '中学生': 3602, 'アラド戦記': 3603, 'SF': 3604, '懐かし': 3605, '問題発言': 3606, '自ら': 3607, '停滞': 3608, 'みなす': 3609, '設計': 3610, '工夫': 3611, '自己満足': 3612, 'ベクトル': 3613, '違和感': 3614, '現実的': 3615, '引き起こし': 3616, '生活': 3617, '苦労': 3618, 'アフェリエイト': 3619, '一円': 3620, '奴ら': 3621, 'オブラート': 3622, '動く': 3623, 'アマチュア': 3624, '作戦': 3625, '雑魚': 3626, 'ディ': 3627, 'おら': 3628, 'トップチーム': 3629, '公表': 3630, '今後': 3631, 'おそらく': 3632, '永遠に': 3633, '広告塔': 3634, '役割': 3635, '自己紹介': 3636, 'デバイス': 3637, '乗っかっ': 3638, 'サル': 3639, 'しろ': 3640, '名乗っ': 3641, '情報発信': 3642, 'アピール': 3643, '最低限': 3644, 'ツーイト': 3645, '当時': 3646, '増し': 3647, '手のひら': 3648, 'くるくる': 3649, '有象無象': 3650, 'カス': 3651, 'そんな': 3652, '月数': 3653, '後世': 3654, '自称': 3655, 'テンション': 3656, 'そーいや': 3657, 'スら': 3658, 'フィジカル': 3659, '面': 3660, 'おせ': 3661, 'エイムカス': 3662, '明け': 3663, '同調圧力': 3664, '銃社会': 3665, '銃': 3666, '売れる': 3667, 'なくなら': 3668, 'スワット': 3669, 'みれ': 3670, 'やってくる': 3671, '確かめる': 3672, '手順': 3673, 'おかしいっ': 3674, 'くない': 3675, '去年': 3676, '年越し': 3677, 'ぶっ続け': 3678, 'ライゼスト': 3679, '年越しイベント': 3680, 'NOT': 3681, '野良連合': 3682, 'CANON': 3683, '一眼': 3684, 'じっと': 3685, '日本製': 3686, '正月': 3687, '帰れ': 3688, '後人': 3689, '切れる': 3690, 'カ能': 3691, '学生時代': 3692, '受託': 3693, '稼い': 3694, '高専': 3695, '出身': 3696, '学部': 3697, '間に合わ': 3698, 'ナチュラル': 3699, 'ゴリゴリ': 3700, 'スマーフサブ': 3701, '様相': 3702, '抑え': 3703, 'チンパンジー': 3704, '0度': 3705, 'うーん': 3706, '様': 3707, '胃': 3708, 'キリ': 3709, '光彩': 3710, 'MOBA': 3711, '相関': 3712, 'va': 3713, 'きれ': 3714, 'おろそか': 3715, 'ウルトチャージ': 3716, '攻撃力': 3717, '00倍': 3718, '速度': 3719, '量的': 3720, 'パリピ': 3721, '流': 3722, '自殺': 3723, 'なそ': 3724, '引き合い': 3725, '敗因': 3726, 'スケープゴート': 3727, 'てなんと': 3728, 'タノチー': 3729, 'あまっ': 3730, '震え': 3731, 'taiyo': 3732, 'リスポーン': 3733, 'リロード': 3734, '振り向い': 3735, '影響力': 3736, 'skyfull': 3737, 'きって': 3738, '変態': 3739, 'DANTE': 3740, 'ROY': 3741, 'AL': 3742, '何者': 3743, 'ドラミング': 3744, 'たさ': 3745, 'ｗｗｗｗｗ': 3746, 'roy': 3747, 'al': 3748, '正しく': 3749, '社会保障': 3750, '弱者救済': 3751, '社会主義': 3752, '法人税': 3753, '国家': 3754, 'プロフ': 3755, '画': 3756, '度': 3757, '笑える': 3758, '一部の人': 3759, '需要': 3760, '丁寧': 3761, '雑記': 3762, 'アメリカ代表': 3763, 'ボム': 3764, 'ぶっ飛ばす': 3765, '組ま': 3766, 'せれ': 3767, '機動力': 3768, '三拍子': 3769, 'そろっ': 3770, 'ジャンクラット': 3771, 'ニッチピックメイン': 3772, 'クリスマス': 3773, 'ビッグデータ': 3774, '教える': 3775, '偏見': 3776, 'はらま': 3777, 'nAlphaGO': 3778, 'Alpha': 3779, 'とらわれ': 3780, '普遍': 3781, '真理': 3782, 'いえる': 3783, '曖昧': 3784, '出せ': 3785, 'を通して': 3786, '事実': 3787, 'らん': 3788, 'ずれ': 3789, '近い': 3790, 'ハック': 3791, '不当': 3792, '得る': 3793, '思想': 3794, '全体最適': 3795, '資本主義': 3796, '実務': 3797, '実行': 3798, '組織': 3799, '並列': 3800, 'まとま': 3801, '扱わ': 3802, 'により': 3803, '外貨': 3804, '良貨': 3805, '駆逐': 3806, '無い': 3807, 'ミクロ': 3808, 'コード': 3809, '総合格闘技': 3810, 'こなす': 3811, 'クラウドワークス': 3812, '対': 3813, 'マッチングサイト': 3814, 'クライアント': 3815, '手抜き': 3816, 'チャットボット': 3817, '組み': 3818, '営業力': 3819, '無': 3820, '頼む': 3821, '外注': 3822, 'ろくな': 3823, '終わる': 3824, '郵便局': 3825, '挙句': 3826, '代替': 3827, '学費': 3828, '安さ': 3829, '多様性': 3830, '留学': 3831, 'ありがたさ': 3832, '潰し': 3833, 'きき': 3834, '代え': 3835, '難い': 3836, '黎明期': 3837, '専門学校': 3838, '分野': 3839, '立てよ': 3840, '相応': 3841, '覚悟': 3842, '講師': 3843, '雇う': 3844, '学校': 3845, '経営': 3846, '成り立た': 3847, '実績': 3848, 'カリキュラム': 3849, '立ち': 3850, '授業': 3851, '生徒': 3852, '経験': 3853, '現状': 3854, '乖離': 3855, '発生': 3856, '避け': 3857, '多産': 3858, '死': 3859, '芽': 3860, '体育大学': 3861, 'スポーツ選手': 3862, '暮らせる': 3863, '暴論': 3864, '挑戦': 3865, '土壌': 3866, '用意': 3867, '旧来': 3868, '生産性': 3869, '普及': 3870, '雇用': 3871, '守る': 3872, '法律': 3873, 'ツケ': 3874, 'イキリ': 3875, 'お手本': 3876, '全力': 3877, '疎ま': 3878, 'とも': 3879, 'イキリパワー': 3880, '魂': 3881, '落とさ': 3882, '下がっ': 3883, 'リンク': 3884, '一本': 3885, '出かける': 3886, '引い': 3887, '絶望': 3888, '残す': 3889, '時事': 3890, '人見': 3891, '広': 3892, 'ちげ': 3893, '前見': 3894, '横見': 3895, '狙う': 3896, '的確': 3897, 'ワンマガ': 3898, 'saebyelobe': 3899, 'マジゲーム': 3900, 'Gesture': 3901, '表明': 3902, '示し': 3903, '反響': 3904, 'ウケ': 3905, 'リポート': 3906, 'jp': 3907, 'シリーズ化': 3908, '低く': 3909, '扱い': 3910, '認知': 3911, '自宅': 3912, 'エクセル': 3913, 'MS': 3914, 'Office': 3915, '製品': 3916, 'しゃー': 3917, 'イラレ': 3918, '妹': 3919, '美人': 3920, '不完全': 3921, '締切': 3922, '決めて': 3923, '昼': 3924, '締め切り': 3925, 'グラフ': 3926, 'Radeon': 3927, '素材': 3928, '動画編集': 3929, 'youtube': 3930, '過去最高': 3931, 'エネルギー': 3932, 'クリ': 3933, '近接': 3934, '立っ': 3935, '言い訳': 3936, '歩': 3937, '客観的': 3938, '空気': 3939, 'バランス': 3940, '人格': 3941, '認める': 3942, '択': 3943, 'スピーディー': 3944, '行える': 3945, '雰囲気': 3946, '物事': 3947, '固める': 3948, '擦り': 3949, 'はっきり': 3950, '勘違い': 3951, 'ごめんなさい': 3952, '突っ込み': 3953, 'どころ': 3954, 'KOYAMA': 3955, 'ジャン': 3956, 'ロケジャン': 3957, '障碍者': 3958, '呼ん': 3959, '試合中': 3960, 'かく乱': 3961, '勝手': 3962, '存続': 3963, '兼': 3964, 'ビデオ撮影': 3965, '係': 3966, '悔し': 3967, 'いかれ': 3968, 'まさかの': 3969, '上手い': 3970, 'ドゥーム': 3971, 'ぼこぼこ': 3972, '駅前': 3973, '在日特権': 3974, '軍団': 3975, '暴れ': 3976, 'ベンチプレス': 3977, 'クラン': 3978, '撮影': 3979, '元祖': 3980, 'pray': 3981, 'for': 3982, 'us': 3983, '集結': 3984, 'メンツ': 3985, '商品': 3986, '狙っ': 3987, '龍': 3988, 'ぼんやり': 3989, 'サイクロプス': 3990, 'そうとう': 3991, 'カート': 3992, '止め': 3993, 'おもしろかっ': 3994, '恒例': 3995, '変': 3996, '子供': 3997, '精神的負担': 3998, '大き': 3999, 'スナイプ': 4000, '粘着': 4001, '車': 4002, 'ひく': 4003, '筑': 4004, '豊': 4005, '考えよ': 4006, 'フィードバック': 4007, 'ドライバ': 4008, 'マイク': 4009, '音': 4010, '拾わ': 4011, '一通り': 4012, 'トラブルシューティング': 4013, '試し': 4014, '拾っ': 4015, 'nPC': 4016, '端子': 4017, 'ケース': 4018, 'マザボ': 4019, 'それでも': 4020, 'だめ': 4021, '敗退': 4022, 'お疲れ様': 4023, 'りさん': 4024, 'クリーンインストール': 4025, 'ナンパ': 4026, 'イスラム教': 4027, '禁止': 4028, 'Tier': 4029, 'シンメトラ': 4030, 'ナンバーワン': 4031, '暇': 4032, 'Ana': 4033, 'gold': 4034, 'Grandmaster': 4035, '通し': 4036, '仮説': 4037, '思いつい': 4038, 'webサービス': 4039, '進め': 4040, '来年': 4041, '短期': 4042, 'サンマ': 4043, '解散': 4044, 'ジャンクラマジ': 4045, '深夜': 4046, '叩け': 4047, '叩い': 4048, 'wwww': 4049, 'RON': 4050, '僕達': 4051, 'どうせ': 4052, 'うん': 4053, '千円': 4054, 'かうん': 4055, '連絡': 4056, '突き詰め': 4057, '精神的': 4058, '厳しく': 4059, 'いい加減': 4060, 'ズボラ': 4061, '例えば': 4062, '風向き': 4063, '偶然': 4064, 'しかし': 4065, '将棋': 4066, 'つながら': 4067, 'しまい': 4068, '学科': 4069, '思い出し': 4070, '無能': 4071, '共': 4072, 'ボイス': 4073, '耳元': 4074, '聞か': 4075, '連呼': 4076, '既に': 4077, '程度': 4078, '自然': 4079, '表情': 4080, '報酬': 4081, '脳': 4082, '刺激': 4083, 'さらに': 4084, '追い求める': 4085, '習性': 4086, 'もてあそば': 4087, '泥沼': 4088, 'はまっている': 4089, '長文': 4090, 'まとめれ': 4091, '格上': 4092, 'ベスト': 4093, 'ハンド': 4094, '覆せ': 4095, '試合結果': 4096, '良しあし': 4097, '見分ける': 4098, '人心': 4099, '掌握': 4100, '人として': 4101, 'パフォーマンス': 4102, '引き出し': 4103, '思いやっ': 4104, '発揮': 4105, '楽勝': 4106, 'ホワイト企業': 4107, '望ん': 4108, 'ブラック企業': 4109, 'まったく': 4110, '理論': 4111, '意図': 4112, 'くみ取っ': 4113, 'or': 4114, '同様': 4115, '向き': 4116, '不向き': 4117, '動い': 4118, 'コーパス': 4119, 'つかっ': 4120, '正規': 4121, 'ノンネイティブ': 4122, '戦略': 4123, 'ゴミ箱': 4124, 'ポエム': 4125, 'チラシの裏': 4126, '乗る': 4127, '積極的休養': 4128, 'サバゲー': 4129, 'エイ': 4130, 'ム力': 4131, 'マシン': 4132, '組み合わせ': 4133, '状況判断': 4134, 'クリア': 4135, '進める': 4136, '報告': 4137, '色': 4138, '幅': 4139, '情熱': 4140, '好奇心': 4141, '定位': 4142, '判別': 4143, 'ゼンハイザー': 4144, '追わ': 4145, 'ビットコイン': 4146, '技術': 4147, 'BTC': 4148, 'BCH': 4149, 'segwit': 4150, 'こっち': 4151, '0次': 4152, '追い': 4153, 'トレード': 4154, '引っかから': 4155, '0ch': 4156, 'アフィブログ': 4157, '外し': 4158, 'フルダイブ': 4159, 'スタン': 4160, 'みに': 4161, 'ムッチャ': 4162, 'ケバブ': 4163, '店舗': 4164, '毛色': 4165, 'トルコ料理': 4166, '高学歴': 4167, 'キラキラ': 4168, '終身雇用': 4169, '年功序列': 4170, '人生': 4171, '安泰': 4172, '♫': 4173, '価値観': 4174, 'むず痒く': 4175, 'サンクコスト': 4176, '手札': 4177, '観': 4178, '高田馬場': 4179, 'インターン': 4180, '卒論': 4181, 'メーカー': 4182, 'Amazon': 4183, '業者': 4184, 'レビュー': 4185, 'のっ': 4186, '一周': 4187, '担当者': 4188, '信頼': 4189, '思える': 4190, '酒飲み': 4191, '肉': 4192, '海鮮': 4193, '原価': 4194, '直撃': 4195, 'ワイン': 4196, '飲ま': 4197, 'まさに': 4198, 'PDCA': 4199, '風': 4200, '満足': 4201, '成長': 4202, '損切り': 4203, '痛む': 4204, '心': 4205, '堀川': 4206, '痛い': 4207, 'おもしろ': 4208, 'ちー': 4209, '質問箱': 4210, '心情': 4211, '泣け': 4212, '漫画': 4213, 'ヘルク': 4214, '最終話': 4215, '苦悩': 4216, 'アン': 4217, 'ストーリー': 4218, '希望の光': 4219, '綺麗': 4220, '全巻': 4221, 'ポチる': 4222, '安全': 4223, '帰る': 4224, '未来永劫': 4225, '残る': 4226, '思考': 4227, '寄稿': 4228, '初め': 4229, '説明': 4230, '出来上がっ': 4231, '充実': 4232, '高かっ': 4233, 'なんだか': 4234, '希望': 4235, 'F': 4236, 'K0': 4237, 'ラバー': 4238, 'ホイール': 4239, 'クリック': 4240, '良さ': 4241, '気に入っ': 4242, 'rival': 4243, '諦め': 4244, 'DPI': 4245, 'ingame': 4246, '手首': 4247, '支点': 4248, 'っぱなし': 4249, '着地': 4250, '効果的': 4251, '短期的': 4252, 'スシロー': 4253, '段ボール': 4254, '取引': 4255, '人神': 4256, '00': 4257, '儲け': 4258, 'UUUM': 4259, 'アイドル': 4260, '修羅': 4261, '道': 4262, '活用': 4263, 'など': 4264, '知名度': 4265, 'ミッキー': 4266, '絡み': 4267, 'ジェフカプラン': 4268, '甘': 4269, '嘘っぱち': 4270, '発': 4271, 'DF': 4272, '冷': 4273, 'ひえ': 4274, '課税': 4275, '競馬': 4276, 'FB': 4277, '形': 4278, 'いま': 4279, 'まい': 4280, '＝': 4281, 'プレイ': 4282, '裏返し': 4283, '運営側': 4284, '表面的': 4285, 'ランクマッチ': 4286, 'オフシーズン': 4287, '長い': 4288, 'やばいっ': 4289, '営利企業': 4290, 'のす': 4291, '原因': 4292, 'DQR': 4293, 'しば': 4294, '遊ぶ': 4295, 'slack': 4296, 'ショートカット': 4297, 'コマンド': 4298, 'ワンパンマン': 4299, 'ことば': 4300, 'グレイラース': 4301, 'top': 4302, '手段': 4303, 'いくらでも': 4304, '試せ': 4305, '仮説検証': 4306, 'さしづめ': 4307, '出世': 4308, '天井': 4309, 'アラフォー': 4310, 'スタミナ': 4311, '向き合っ': 4312, '意思': 4313, 'マンネリ': 4314, '失わ': 4315, 'げーじ': 4316, 'ゃないと': 4317, '真剣': 4318, 'ジレンマ': 4319, 'ドラゴンクエストライバルズ': 4320, 'nOW': 4321, '解除': 4322, '通知': 4323, 'ズゴゴゴゴ': 4324, 'ピルロ': 4325, 'すごそ': 4326, '俯瞰': 4327, '力強い': 4328, 'バスケ': 4329, 'だして': 4330, 'ジェットコースター': 4331, '蓄え': 4332, '位置エネルギー': 4333, '解放': 4334, 'れよ': 4335, '課金': 4336, 'taigahagorrila': 4337, '予想外': 4338, 'マッチョ': 4339, 'かかり': 4340, '小学校': 4341, 'クラス': 4342, '匿名性': 4343, '相まって': 4344, '定期的': 4345, '風斬り': 4346, 'スピード': 4347, 'CPU': 4348, 'スパコン': 4349, 'sinatraa': 4350, 'ブリンク': 4351, '距離': 4352, '適切': 4353, 'ス': 4354, 'みえる': 4355, '読み返す': 4356, '人間性': 4357, '0話': 4358, 'ハロー効果': 4359, '強烈': 4360, 'じわじわ': 4361, 'webサイト': 4362, 'やったー': 4363, '返せる': 4364, 'ワンウェーブ': 4365, 'バスティオリーサハルトザリア': 4366, 'フルメンバー': 4367, 'ゃないってよくわからんけどすごい': 4368, '起こっ': 4369, 'べつ': 4370, '指導者': 4371, '小遣い': 4372, '稼ぎ': 4373, '忙しい': 4374, '社会人': 4375, '満たせる': 4376, 'web': 4377, 'ウェブサイト': 4378, '足りる': 4379, '競技': 4380, '提出': 4381, 'ステ': 4382, '会見': 4383, 'めんどい': 4384, '多様': 4385, '特徴': 4386, 'パラメタライズ': 4387, '勝者': 4388, '振る舞う': 4389, '替玉': 4390, '名古屋': 4391, 'OJA': 4392, '勝ち星': 4393, '刻ま': 4394, 'oja': 4395, 'sns': 4396, 'スポンサー': 4397, '代表': 4398, '失言': 4399, 'しな': 4400, 'やし': 4401, '見習う': 4402, 'お前': 4403, 'アザラック': 4404, 'リフトオフ': 4405, 'ぼん': 4406, 'ブラウン': 4407, 'アルターエデン': 4408, 'た人': 4409, 'Rpg': 4410, 'まるで': 4411, '社会性': 4412, 'ヤベー': 4413, '平常心': 4414, '全身': 4415, '埋め': 4416, '尽くし': 4417, 'カフェイン': 4418, '半減期': 4419, '即席': 4420, 'エンジョイ': 4421, 'チェックイン': 4422, '間に合う': 4423, 'ルーキー': 4424, 'カップ': 4425, 'ディブロ': 4426, 'そりゃ': 4427, 'つよい': 4428, 'ONE': 4429, 'モブサイコ': 4430, '投球': 4431, '裏サンデー': 4432, 'HELCK': 4433, '完結': 4434, 'やば': 4435, '迷走': 4436, 'GCWiki': 4437, 'オーバーウォッチ': 4438, '移転': 4439, 'リダイレクト': 4440, '順位': 4441, '消え去っ': 4442, 'GamerCoachWiki': 4443, '本腰': 4444, '教材': 4445, '媒体': 4446, 'テキスト': 4447, '目指し': 4448, 'Twitter': 4449, '上手く': 4450, 'できれ': 4451, 'あんま': 4452, '卒業生': 4453, '受け入れる': 4454, '無自覚': 4455, '嫉妬心': 4456, '私': 4457, '勇気': 4458, 'あなた': 4459, '許し': 4460, 'クソリプ': 4461, '辟易': 4462, '斜': 4463, '構え': 4464, '嫌儲': 4465, 'マン': 4466, 'ダサ': 4467, '異常': 4468, '最たる': 4469, 'そういった': 4470, '生まれる': 4471, '喜び': 4472, '儲ける': 4473, 'よし': 4474, '近所': 4475, 'ゴールドジム': 4476, '屋': 4477, 'メン': 4478, 'これこれ': 4479, '振っ': 4480, '家で': 4481, 'ヶ月': 4482, 'はじめて': 4483, '売上': 4484, 'ゴーツ': 4485, 'そろそろ': 4486, '飽き': 4487, 'ハク': 4488, 'バチバチ': 4489, 'Rascal': 4490, 'Akm': 4491, '喧嘩': 4492, 'クビ': 4493, '成し遂げ': 4494, 'トキシック': 4495, '天才': 4496, 'タイプ': 4497, '低め': 4498, 'ワーク': 4499, 'nDF': 4500, '温厚': 4501, '多め': 4502, 'iPhone': 4503, 'Android': 4504, 'ゲームクラブ': 4505, 'コミュニティサイト': 4506, '文中': 4507, 'GamersClub': 4508, 'mode': 4509, 'ブラジル': 4510, '語': 4511, 'トップクラス': 4512, '精神衛生上': 4513, '理想': 4514, 'そこで': 4515, '局所化': 4516, 'ユートピア': 4517, '永遠': 4518, 'まよっ': 4519, '社員': 4520, '権限': 4521, 'にかけて': 4522, '寒い': 4523, 'スプレー': 4524, '盤面': 4525, '潰さ': 4526, 'ギルド': 4527, 'アグロチンパンズ': 4528, '伝わる': 4529, 'ゼシカアンチ': 4530, 'ひとだま': 4531, 'バイキング': 4532, 'ミラー': 4533, 'マリガン': 4534, '最優先': 4535, '行こ': 4536, 'ゼシカ': 4537, 'クソゲー': 4538, 'マナ': 4539, 'バラモス': 4540, 'みならいあくま': 4541, 'はまじ': 4542, 'テンポゼシカ': 4543, 'キーカード': 4544, 'NR': 4545, '北海道': 4546, '大概': 4547, 'ガバガバ': 4548, '自己弁護': 4549, '公式アカウント': 4550, 'リツイート': 4551, '人相': 4552, '当': 4553, '入れ替え': 4554, '毎度': 4555, 'ディスる': 4556, '恥ずかしい': 4557, 'セクシービーム': 4558, 'トラ': 4559, '特技': 4560, 'アグロ': 4561, 'アグロゼシカ': 4562, '人魂': 4563, 'ミネア': 4564, 'リーダー': 4565, 'アリーナ': 4566, '占い師': 4567, 'トルネコ': 4568, '闘技': 4569, '場': 4570, '三枚': 4571, '考慮': 4572, 'わた': 4573, 'ぼう': 4574, '中国人': 4575, '女性': 4576, 'ど': 4577, 'ゆこ': 4578, 'スライド': 4579, '同情': 4580, 'スタイル': 4581, '移行': 4582, '朝': 4583, 'プレゼン': 4584, '資料': 4585, '真っ赤': 4586, 'いつも': 4587, '切れ': 4588, '失神': 4589, 'エピソード': 4590, '縛り': 4591, 'デッキ': 4592, '錬': 4593, '足りん': 4594, 'dqr': 4595, '奥': 4596, '後々': 4597, 'サイレス': 4598, '封じ': 4599, 'ガチャコッコ': 4600, 'けやり': 4601, 'レジェ': 4602, '我が': 4603, 'アグロチンパンリア': 4604, '友': 4605, 'ターン': 4606, '除去': 4607, 'アンサー': 4608, '亡者': 4609, 'ござっ': 4610, '交換': 4611, 'バンバン': 4612, '打点': 4613, '減らさ': 4614, '場面': 4615, 'のっち': 4616, '色んな': 4617, 'はぐれメタル': 4618, '何故か': 4619, 'トラップ': 4620, '顔面': 4621, '殴れる': 4622, '倒さ': 4623, '揃え': 4624, 'カード': 4625, 'アグロデッキ': 4626, 'きが': 4627, 'カミュ': 4628, 'キャラガチ': 4629, 'テリー': 4630, '序盤': 4631, '縦': 4632, '並べる': 4633, '削り': 4634, '悔しい': 4635, '先程': 4636, '並べ': 4637, '斜め': 4638, '並ぶ': 4639, 'チンパン': 4640, '研究発表': 4641, '文系': 4642, '噛み砕い': 4643, '用語': 4644, '専門用語': 4645, 'だらけ': 4646, '冒頭': 4647, 'キチ': 4648, 'よろ': 4649, '次ぐ': 4650, 'なるほど': 4651, 'なぁ': 4652, 'ソシャゲ': 4653, '観点': 4654, 'とらえ': 4655, '論': 4656, '盛り上がり': 4657, '単に': 4658, 'すく': 4659, 'リム': 4660, '消滅': 4661, 'ドラクエライバルズ': 4662, '想像': 4663, 'ドラクエ': 4664, 'ククール': 4665, '無敗': 4666, 'こっ': 4667, '上がら': 4668, 'アグロアンチ': 4669, '後なん': 4670, 'ちょいちょい': 4671, 'ドルイド': 4672, 'DQ': 4673, 'ライバル': 4674, '有り': 4675, '丸パクリ': 4676, 'たし': 4677, '引ける': 4678, 'りゅうおう': 4679, 'アンルシア': 4680, '共通': 4681, 'ぜ': 4682, 'とく': 4683, 'ノアノア': 4684, 'モチベ': 4685, 'つまん': 4686, '喜んで': 4687, '横流し': 4688, '訳し': 4689, '断捨離': 4690, '秋': 4691, '秋葉原': 4692, 'おばさん': 4693, '眠く': 4694, '必ず': 4695, '生活習慣': 4696, '秋葉': 4697, '向かい': 4698, '射程': 4699, '追尾': 4700, '野球': 4701, 'セカンドキャリア': 4702, '込み': 4703, '買い': 4704, '売り出し': 4705, '売り': 4706, '売る': 4707, '売っ': 4708, '良心': 4709, '価格': 4710, 'チャット': 4711, 'おまけ': 4712, 'つき': 4713, 'チェーン': 4714, 'たこ焼き屋': 4715, 'たろ': 4716, '惰性': 4717, '消す': 4718, '梅原': 4719, '偏差値': 4720, '必死': 4721, 'かかわる': 4722, '塾': 4723, '余地': 4724, 'ブランド': 4725, 'のち': 4726, '些末な': 4727, 'ベース': 4728, 'おい': 4729, 'Top': 4730, 'マジバケモン': 4731, 'owpedia': 4732, 'Overpedia': 4733, 'ついてれ': 4734, '一瞬': 4735, '置け': 4736, 'からっ': 4737, '先考': 4738, 'いち': 4739, 'タックル': 4740, 'クリップ': 4741, '書ける': 4742, '調整': 4743, 'karq': 4744, '待ち': 4745, 'ツイッチプライム': 4746, '登録': 4747, 'Delave': 4748, '不安定': 4749, 'おすすめ': 4750, 'しません': 4751, '糞': 4752, '実況': 4753, '百害あって一利なし': 4754, '勘弁': 4755, 'ワールドカップ': 4756, '覚えりゃ': 4757, 'China': 4758, 'イギリス': 4759, 'スウェーデン': 4760, 'オープンマイク': 4761, '鼻歌': 4762, '歌っ': 4763, 'ソンブラシンメマジ': 4764, '欄': 4765, '承認': 4766, '持ち主': 4767, '素早く': 4768, '消える': 4769, 'あたっ': 4770, '築': 4771, 'めちゃめちゃ': 4772, '揺れ': 4773, '喜ぶ': 4774, '一定': 4775, '課題': 4776, '本気': 4777, '受け取る': 4778, '決済': 4779, 'ペース': 4780, '有志': 4781, 'Web': 4782, '安く': 4783, 'ボランティア': 4784, 'につき': 4785, '負担': 4786, 'フル': 4787, 'NDA': 4788, 'はじめ': 4789, 'フィルター': 4790, '激減': 4791, 'つぶやく': 4792, '海外展開': 4793, '富裕層': 4794, 'ぜひ': 4795, '売れ': 4796, 'とどく': 4797, '廉価版': 4798, 'マルチ': 4799, '勧誘': 4800, '視線': 4801, '疲労': 4802, '食生活': 4803, 'pandas': 4804, '芸当': 4805, '熟睡': 4806, 'トレ': 4807, 'ベンチ': 4808, 'ジム': 4809, 'びびっ': 4810, 'プッシュアップバー': 4811, 'ポチっ': 4812, 'スマート': 4813, '根性': 4814, '乗り切る': 4815, 'googleアラート': 4816, 'がめ': 4817, '一文字': 4818, 'ライター': 4819, 'あろう': 4820, 'オリジナリティ': 4821, 'かけら': 4822, '真似': 4823, '語尾': 4824, '虚無': 4825, 'LoL': 4826, 'スマホゲー': 4827, 'スマホ': 4828, '打ち合わせ': 4829, 'ありとあらゆる': 4830, 'ドメイン': 4831, '流通': 4832, '細分': 4833, 'OWWC': 4834, '接戦': 4835, 'オーストラリア代表': 4836, 'BLK': 4837, 'トリル': 4838, '大差': 4839, '英語圏': 4840, 'Baconjack': 4841, 'しかり': 4842, 'wiki': 4843, '回せ': 4844, 'サーバー管理者': 4845, 'よい': 4846, '出稿': 4847, '拡大': 4848, '回せる': 4849, '作りました': 4850, '食える': 4851, '博多ラーメン': 4852, '博多': 4853, '一双': 4854, '大砲ラーメン': 4855, '商売': 4856, '物寂しい': 4857, 'やはり': 4858, '定義': 4859, 'おはよう': 4860, 'ツイッチ': 4861, '滅多': 4862, 'ない層': 4863, '広め': 4864, 'LTV': 4865, 'タレント': 4866, 'マネジメント': 4867, 'なんとなく': 4868, 'トロールチート': 4869, '自由': 4870, 'chara': 4871, '生き': 4872, 'NRhokkaidou': 4873, 'nOrisa': 4874, 'change': 4875, 'キングスロウ': 4876, '部屋': 4877, '引き': 4878, 'こもっ': 4879, '説': 4880, '布教': 4881, '返事': 4882, 'メール': 4883, 'バフ': 4884, 'ぐらい': 4885, 'もんぱ': 4886, 'ぁ': 4887, '彼氏': 4888, 'やすかっ': 4889, '各': 4890, 'Dexo': 4891, 'ねる': 4892, '起床': 4893, '動画ネタ': 4894, 'フィンガー': 4895, 'チップ': 4896, '少数派': 4897, 'きち': 4898, '感度': 4899, '振り': 4900, '腕': 4901, '振り向き': 4902, '指先': 4903, '開始': 4904, 'ハッピー': 4905, '体毛': 4906, 'Fuel': 4907, 'かっこよ': 4908, 'RJM': 4909, 'Kirihito': 4910, 'シーズンプラチナフィニッシュ': 4911, 'まして': 4912, '射精': 4913, 'えーん': 4914, '注文': 4915, 'あん': 4916, '店員': 4917, 'ブチ': 4918, '合唱': 4919, 'ヴァーヴァー': 4920, 'カナダ': 4921, 'マズ': 4922, '情報ソース': 4923, '辿っ': 4924, '抵抗': 4925, 'すっと': 4926, '感性': 4927, '食お': 4928, 'フランス領': 4929, '歴史': 4930, '合間': 4931, '街並み': 4932, 'フランス人': 4933, 'フランス': 4934, 'ハーフ': 4935, 'アメリカ人': 4936, 'マレーシア': 4937, '英語力': 4938, 'DMM': 4939, '英会話': 4940, 'TOEIC': 4941, '上げよ': 4942, '話せ': 4943, '恥じ': 4944, '追い込ん': 4945, '全盛期': 4946, 'genji': 4947, 'FS': 4948, '跳ね返す': 4949, 'ぶつかっ': 4950, '代わり': 4951, 'なおかつ': 4952, '電撃': 4953, 'ぶつから': 4954, 'ビリビリ': 4955, '何とか': 4956, 'シーズン終了': 4957, 'たつ': 4958, 'gc': 4959, 'busan': 4960, 'カ国': 4961, '次に': 4962, 'ヨーロッパ': 4963, 'パスタ': 4964, '日本食': 4965, 'くい': 4966, 'テー': 4967, 'ズーーーーーット': 4968, 'DNN': 4969, '教師なし学習': 4970, 'CG': 4971, '知識': 4972, '人工知能': 4973, '取り組め': 4974, '塊': 4975, '野良': 4976, '恐ろしい': 4977, '統率力': 4978, 'ヒラタン': 4979, '始める': 4980, '芯': 4981, '点': 4982, '一貫': 4983, 'ネガティブ': 4984, 'なくなる': 4985, '実験': 4986, 'なんj': 4987, '迷言': 4988, 'ほんと': 4989, '版': 4990, 'すいません': 4991, '筋肉': 4992, '回り': 4993, '0秒間': 4994, '転': 4995, '回転': 4996, 'フレームレート': 4997, 'fps': 4998, '高速': 4999, '実質': 5000, '疑似': 5001, '前後': 5002, '張っ': 5003, 'プロジェクタイル': 5004, '方位': 5005, '防げる': 5006, 'トルネード': 5007, '判定': 5008, '間': 5009, '周囲': 5010, '遊び': 5011, 'gs': 5012, 'r': 5013, '募': 5014, 'n0': 5015, '心なし': 5016, '九州': 5017, '関東': 5018, '呼ぶ': 5019, '自己肯定感': 5020, 'ルックス': 5021, 'こだわら': 5022, 'トゥトゥトゥトゥウィッティ': 5023, 'ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ': 5024, '稼働': 5025, '働か': 5026, '規則': 5027, '羅列': 5028, '眠い': 5029, '集中力': 5030, 'をもって': 5031, 'こなせ': 5032, '直前': 5033, 'ストレス耐性': 5034, '人格的': 5035, '思いやり': 5036, '精神的支柱': 5037, 'ゲーミングデバイス': 5038, 'こだわる': 5039, '受験勉強': 5040, 'こだわっ': 5041, 'いただけ': 5042, 'そのため': 5043, 'つかめる': 5044, 'フェティシズム': 5045, '凍ら': 5046, '蝶': 5047, '標本': 5048, '係り': 5049, 'WhatEver': 5050, '出来る': 5051, '主': 5052, '練': 5053, '高める': 5054, '頻度': 5055, 'ご': 5056, 'nRT': 5057, 'いただける': 5058, '皇帝': 5059, 'マネージャー': 5060, '人出': 5061, 'すっ': 5062, '選択肢': 5063, 'ログイン': 5064, '待ち時間': 5065, 'どなた': 5066, '今シーズン': 5067, '行き来': 5068, '期': 5069, '評論家': 5070, '墓': 5071, 'AmazonPrime': 5072, '結びつけ': 5073, 'おま国': 5074, '指': 5075, 'チョチョっと': 5076, '動かせる': 5077, '接触': 5078, '複雑': 5079, '種類': 5080, '提示': 5081, '凄い': 5082, 'ドルクエ': 5083, 'かわいく': 5084, 'ファンタジー': 5085, '王道': 5086, '存在感': 5087, 'ゴールデンタイム': 5088, 'モバイルワイファイルーター': 5089, '格安sim': 5090, '刺し': 5091, '携帯': 5092, 'LTE': 5093, 'ping': 5094, '向い': 5095, '容量': 5096, 'テザリング': 5097, '他社': 5098, 'WiMAX': 5099, '宣伝': 5100, 'ステマ': 5101, '汚染': 5102, 'ポケットワイファイ': 5103, 'ひど': 5104, 'ポケットルーター': 5105, 'ワイファイ': 5106, '打ち合い': 5107, '打て': 5108, 'ラグ': 5109, '人柱': 5110, 'オワ': 5111, '指南': 5112, '講座': 5113, 'オワチッチ': 5114, '故': 5115, 'ゾエルニキ': 5116, 'エッチ': 5117, 'そりゃあ': 5118, '杉内': 5119, '年生': 5120, '修士': 5121, '補完': 5122, 'ガチサウナ': 5123, 'ザコ': 5124, 'よって': 5125, 'どうも': 5126, 'ワンヒーラー': 5127, 'あみ': 5128, 'だむ': 5129, '求む': 5130, '不動産': 5131, '自営': 5132, '雇わ': 5133, '限度': 5134, '雇っ': 5135, 'うなぎ': 5136, '寿司': 5137, '海外旅行': 5138, '遊ん': 5139, 'たな': 5140, 'もちろん': 5141, '要するに': 5142, '落とし込み': 5143, '思いつく': 5144, '手先': 5145, 'パイ': 5146, '狭まっ': 5147, '頼ら': 5148, '傘': 5149, 'やよい軒': 5150, '最速': 5151, '平成最後': 5152, '顔だし': 5153, 'オフイベ': 5154, 'オフライン': 5155, 'ダイレクトマーケティング': 5156, 'レア': 5157, 'あるかな': 5158, '飲み': 5159, '弊': 5160, 'びっくり': 5161, '未': 5162, '初見': 5163, '確かめ': 5164, '共有': 5165, 'テスト': 5166, '付き合っ': 5167, '方い': 5168, '接続': 5169, '丸々': 5170, '単位': 5171, '直近': 5172, 'google': 5173, 'analytics': 5174, 'Photoshop': 5175, '問題解決': 5176, 'ル': 5177, 'しながら': 5178, 'シームレス': 5179, 'ヌンバーニ': 5180, '階段': 5181, '登っ': 5182, '盾': 5183, '前提': 5184, 'トレソル': 5185, '押し切れ': 5186, 'Loccat': 5187, 'Kone': 5188, 'Pure': 5189, 'Logi': 5190, 'ヘッドセット': 5191, 'Zowie': 5192, 'マウスバンジーポチ': 5193, 'アバラ': 5194, '格好': 5195, 'トーク': 5196, 'ホスト': 5197, 'mori': 5198, '森さん': 5199, 'teen': 5200, 'GTX': 5201, 'Ti': 5202, 'SLM': 5203, 'つない': 5204, 'カスタム': 5205, '転売': 5206, 'ちゃっ': 5207, '新卒': 5208, '初任': 5209, '給': 5210, '越え': 5211, 'アメリカアマゾン': 5212, '個人輸入': 5213, '転送': 5214, '仕入れ': 5215, '稼げる': 5216, 'リア垢': 5217, 'に関し': 5218, '稼が': 5219, '勝ち負け': 5220, 'なるか': 5221, 'わか': 5222, 'みっき': 5223, 'Envy': 5224, '0D': 5225, 'PS': 5226, '世界中': 5227, '強いっ': 5228, '遊戯王': 5229, 'レアカード': 5230, 'エフェクトザリア': 5231, '人気者': 5232, '流石に': 5233, '飽きる': 5234, 'ボット': 5235, 'テレポート': 5236, 'プロパイダー': 5237, '選べ': 5238, 'おも': 5239, '解決策': 5240, '長かっ': 5241, 'うんこ製造機': 5242, '憑かれ': 5243, '模試': 5244, '熱中': 5245, '学業': 5246, '専念': 5247, '今頃': 5248, '再来年': 5249, '目指す': 5250, '浪人生': 5251, '多浪': 5252, 'オバッチ': 5253, 'めたん': 5254, '❔': 5255, '睡眠時間': 5256, '日本語版': 5257, '散在': 5258, 'アーカイブス': 5259, '照らし': 5260, '総合': 5261, 'ぼやっと': 5262, '関わっ': 5263, 'づついろんな': 5264, 'Mac': 5265, '相性': 5266, '悪': 5267, 'クレア': 5268, 'できん': 5269, 'まらん': 5270, '戦記': 5271, '読も': 5272, '何もかも': 5273, '実例': 5274, 'できないよ': 5275, 'ラグランジュ': 5276, '未定': 5277, '乗数': 5278, '習っ': 5279, '実用': 5280, '感慨深い': 5281, '常識': 5282, '既存': 5283, '真似れ': 5284, '削ら': 5285, 'ヤフオク': 5286, '出品': 5287, 'ユーロ': 5288, 'たかい': 5289, '絡ん': 5290, '評判': 5291, '支障': 5292, '切り替える': 5293, 'ファイブ': 5294, 'JCG': 5295, '決勝': 5296, '見ん': 5297, 'ゲーミングハウス': 5298, 'サラッと': 5299, 'いかつ': 5300, '震える': 5301, 'tweetdeck': 5302, '予約': 5303, 'pm': 5304, 'やる気': 5305, 'まち': 5306, 'パッチ': 5307, '改変': 5308, '見つから': 5309, '動かす': 5310, 'チンパンジーゲー': 5311, '幸せ': 5312, 'ウンタラカンタラ': 5313, '面倒': 5314, 'COD': 5315, '撃ち殺す': 5316, 'ツイッターアカウント': 5317, 'BO': 5318, '期間': 5319, 'お祭り': 5320, '穏やか': 5321, '幻想': 5322, '突き止め': 5323, '仕掛け': 5324, '雨': 5325, 'けん': 5326, 'サッサ': 5327, 'K': 5328, 'グループb': 5329, 'ホッグ': 5330, '0回戦': 5331, '一位': 5332, '絶望的': 5333, 'ミロポ': 5334, '乗れる': 5335, 'デマ': 5336, 'デマ情報': 5337, '指定': 5338, '乗れ': 5339, 'ミロポジ': 5340, '乗り': 5341, 'コツ': 5342, 'ベストアンサー': 5343, 'バカゲー': 5344, 'ゴミゲー': 5345, '乗っ': 5346, '撮り': 5347, '手伝っ': 5348, 'エリア': 5349, '気持': 5350, '分かっ': 5351, '雑': 5352, '短時間': 5353, '深く': 5354, 'nXQ': 5355, 'なげ': 5356, '学べる': 5357, 'コンセプト': 5358, '狙い': 5359, '読み取る': 5360, 'しも': 5361, '解説動画': 5362, '基礎': 5363, '平然と': 5364, '不快': 5365, '要項': 5366, '貸し': 5367, 'しらん': 5368, '持ち帰る': 5369, 'イマイチ': 5370, 'za': 5371, '性格': 5372, 'S0': 5373, '一筋': 5374, '銀': 5375, '枠': 5376, 'プレースタイル': 5377, 'ちょくちょく': 5378, '六': 5379, 'ログ': 5380, '炊い': 5381, 'クリティカルヒット': 5382, 'ちょい': 5383, 'あいつ': 5384, '一体': 5385, 'コリアン': 5386, '0p': 5387, 't': 5388, '捗る': 5389, '矢': 5390, 'チン': 5391, 'ブー': 5392, '組ん': 5393, 'FU': 5394, 'CCC': 5395, 'CCCCCCCCCCCCCCCCCCCCCCCCK': 5396, 'とうとう': 5397, 'サ': 5398, 'さっき': 5399, '自前': 5400, 'スピーカー': 5401, '音楽': 5402, '流し': 5403, 'ウェイ': 5404, '人組': 5405, '一気に': 5406, '見識': 5407, 'ディナー': 5408, '食う': 5409, '吉野家': 5410, '励まさ': 5411, '配達': 5412, '受け取れ': 5413, 'なんとか': 5414, '新宿駅': 5415, '徒歩': 5416, '分の': 5417, 'SF0': 5418, '電車': 5419, '0年前': 5420, 'お話': 5421, 'いただい': 5422, '含蓄': 5423, '協賛': 5424, '自社': 5425, 'GAFA': 5426, '追いつけ': 5427, '投入': 5428, '人口': 5429, '番手': 5430, 'アップサイド': 5431, '小さ': 5432, 'PFN': 5433, '特化': 5434, '朝定食': 5435, 'エニタイム': 5436, 'マイブーム': 5437, 'アパート': 5438, 'MB': 5439, 'Legends': 5440, '幸運': 5441, '惹か': 5442, '0m': 5443, 'bs': 5444, '再インストール': 5445, 'p0p': 5446, 'ぐ': 5447, 'fk': 5448, 'あき': 5449, '乗り越える': 5450, '拳': 5451, '心地よく': 5452, '周波数': 5453, '仕掛ける': 5454, '移動': 5455, 'スタッツ': 5456, 'ランクマクソコンテンツ': 5457, 'live': 5458, '見やすい': 5459, 'a': 5460, 'スタヌ': 5461, '辞め': 5462, 'DTN': 5463, 'ドイツ': 5464, '極めよ': 5465, '舞台': 5466, 'どころか': 5467, '皮肉': 5468, '律': 5469, '泣ける': 5470, '自陣': 5471, '押し出す': 5472, 'マーシーウル': 5473, '辛': 5474, '久': 5475, '々': 5476, '高橋': 5477, 'ゲーミングメンバー': 5478, 'キーボード': 5479, '小さい': 5480, '左側': 5481, '振り向く': 5482, 'ガ': 5483, 'ツン': 5484, 'ぶつかる': 5485, 'DM': 5486, 'たい動': 5487, '経営者': 5488, '仮想敵': 5489, '大好きだよ': 5490, 'さっさと': 5491, '永': 5492, '制裁': 5493, '下り': 5494, '手足': 5495, '口': 5496, '落下': 5497, 'ｿﾝﾌﾞﾗ': 5498, '即死': 5499, '病': 5500, 'つまらな': 5501, 'れす': 5502, 'たまっ': 5503, 'サブヒーラー': 5504, 'ホットスナック': 5505, '数量': 5506, '引き抜い': 5507, '界': 5508, '読売巨人軍': 5509, '金持ち': 5510, '引き抜き': 5511, '噂': 5512, 'リアルフォース': 5513, 'キートップ': 5514, '掃除': 5515, '壊れる': 5516, '短い': 5517, '訴訟': 5518, '運営方針': 5519, 'dis': 5520, '発言内容': 5521, '否定': 5522, '焦燥感': 5523, 'ドリブン': 5524, '日々': 5525, 'ぶり': 5526, 'ぼつ': 5527, 'プロスト': 5528, 'リーマー': 5529, '帰国': 5530, 'iphone': 5531, 'アニモジ': 5532, '劇': 5533, 'エモ': 5534, '上の': 5535, 'そっ': 5536, '頑張り': 5537, '所': 5538, '変動': 5539, '統計的': 5540, '収束': 5541, '被験者': 5542, 'さあ': 5543, 'jesl': 5544, 'ふふ': 5545, '全額': 5546, 'ありがたい': 5547, '陽気': 5548, 'バス': 5549, '逃し': 5550, 'ビール': 5551, 'ドイツ語': 5552, '話しかけ': 5553, 'ドイツ人': 5554, 'ベー': 5555, 'ピザ': 5556, 'ソーセージ': 5557, '肥満': 5558, '食文化': 5559, '食べ': 5560, 'フリックエイム': 5561, '使': 5562, 'かったん': 5563, '果たして': 5564, 'バレる': 5565, 'と腹': 5566, 'オーケー': 5567, 'ワキヤン': 5568, '風土': 5569, '物価': 5570, 'XP': 5571, '壁紙': 5572, '景色': 5573, '城': 5574, '誹謗中傷': 5575, '体制': 5576, 'コーラ': 5577, 'ストロー': 5578, 'ひっくり返し': 5579, '荷物': 5580, 'くれよ': 5581, '乗り越えよ': 5582, '学会': 5583, '進ま': 5584, '出張': 5585, 'オーストリア': 5586, '弱けれ': 5587, 'しそう': 5588, '落ち着い': 5589, '半端': 5590, '上下関係': 5591, '疑問': 5592, 'アナリスト': 5593, '不問': 5594, '思いつか': 5595, 'いてる': 5596, '連続': 5597, 'てきが': 5598, 'ーホッグ': 5599, 'ほっ': 5600, 'ウィンストンガイジ': 5601, 'える': 5602, '初': 5603, '効か': 5604, '徹底的': 5605, '払う': 5606, 'ジャンク品': 5607, '新しく': 5608, '直す': 5609, 'realforce': 5610, '故障': 5611, 'ぐぐっ': 5612, '修理': 5613, '東プレ': 5614, '直し': 5615, '段': 5616, '法っ': 5617, 'タイモウ': 5618, 'アンケート': 5619, 'シュール': 5620, '素直': 5621, '表し': 5622, '吐き': 5623, '好感': 5624, '持てる': 5625, 'どんだけ': 5626, 'ファイト': 5627, '厳禁': 5628, '世の中': 5629, '競争率': 5630, '参入障壁': 5631, 'たとえ': 5632, '席': 5633, '奪い合う': 5634, '到達': 5635, 'アジアン': 5636, 'だれか': 5637, '見やすく': 5638, 'くれー': 5639, '本質的': 5640, '成熟': 5641, '市場': 5642, '突っ込む': 5643, '厳し': 5644, 'POV': 5645, '移さ': 5646, '東北': 5647, '狙わ': 5648, 'benymd': 5649, 'ff': 5650, '星': 5651, '正': 5652, '少なくとも': 5653, '細かく': 5654, '大きく': 5655, '運動神経': 5656, '未だに': 5657, 'QCK': 5658, '滑り': 5659, '滑らか': 5660, '減点': 5661, '見習っ': 5662, 'FAZE': 5663, 'アイヘン': 5664, 'トータルメイヘム': 5665, 'プロゲンジ': 5666, 'University': 5667, '放題': 5668, 'ワンパン': 5669, '突っ込ま': 5670, '再来月': 5671, '来週': 5672, 'びみょ': 5673, 'うだっ': 5674, '趣旨': 5675, '載せ': 5676, '前もって': 5677, 'ハテブ': 5678, '番目': 5679, '有名人': 5680, 'アマチュア時代': 5681, 'お勧め': 5682, '引用': 5683, 'アビューズ': 5684, '上手': 5685, '落とし込める': 5686, '具体': 5687, '大河': 5688, 'お台場': 5689, '暮らす': 5690, '済む': 5691, '薬': 5692, '飲め': 5693, '成分': 5694, 'あー': 5695, 'ろ': 5696, 'みや': 5697, 'ガーディアンエンジェル': 5698, 'ターゲット': 5699, '加わっ': 5700, '近づい': 5701, 'キリングエンジェル': 5702, 'ほしかっ': 5703, 'Uber': 5704, '大学院': 5705, '最先端': 5706, '多かっ': 5707, '生む': 5708, '自動運転': 5709, '過渡期': 5710, '換算': 5711, '目と': 5712, '単純労働': 5713, '画像解析': 5714, '代わら': 5715, 'コモディティ': 5716, 'Airbnn': 5717, '常時': 5718, '繋がり': 5719, '非': 5720, 'タクシードライバー': 5721, '築く': 5722, 'ロサンゼルス': 5723, 'ゲームメーカー': 5724, '本社': 5725, '衝撃': 5726, 'ハーバード': 5727, '基本的': 5728, '返済': 5729, '不要': 5730, '初年度': 5731, '上手けれ': 5732, 'タダ': 5733, '夢': 5734, '施設見学': 5735, '博士': 5736, '持ち': 5737, '創業': 5738, 'ゴリ': 5739, 'テック': 5740, 'ネカフェ': 5741, 'コンシューマーゲー': 5742, 'オンラインゲーム': 5743, '産業振興': 5744, '開く': 5745, '国民': 5746, 'エンタメ': 5747, '福祉': 5748, '差し置い': 5749, '驚く': 5750, 'イベンター': 5751, '継続': 5752, '流出': 5753, 'どちら': 5754, '支社': 5755, '外資': 5756, 'がよく': 5757, 'やりがい': 5758, '輝く': 5759, 'ヤベートコ': 5760, '忘れ': 5761, 'リザレク': 5762, 'chinamin': 5763, '走り': 5764, 'お山の大将': 5765, '自信満々': 5766, '強み': 5767, '人権': 5768, '上場企業': 5769, 'パルスボム': 5770, '去': 5771, '釈迦': 5772, 'ホモ': 5773, 'イケボ': 5774, '兄さん': 5775, 'macbookpro': 5776, 'bp': 5777, '薄い': 5778, 'しっかり': 5779, 'ユーチューブ': 5780, '応用': 5781, 'ユーチューバー': 5782, 'ネットリテラシー': 5783, '学べ': 5784, '描き': 5785, 'たし前': 5786, 'wikipedia': 5787, '女声': 5788, 'ESL': 5789, '体型': 5790, '研究者': 5791, '理系': 5792, 'オタサーの姫': 5793, '嫌味': 5794, '演出': 5795, 'さとし': 5796, 'もち': 5797, 'ばけん': 5798, 'ま': 5799, '減少': 5800, 'きつかっ': 5801, '発狂': 5802, 'ポジショントーク': 5803, '理念': 5804, 'そうじゃない': 5805, 'U0': 5806, '余っ': 5807, 'おっさん化': 5808, 'bor': 5809, '気力': 5810, 'おき': 5811, 'oops': 5812, 'ミュートワード': 5813, 'rpg': 5814, 'プレゼント': 5815, '抽選': 5816, 'にやけ': 5817, 'aprx': 5818, '早期': 5819, 'ひっくり返る': 5820, 'もろ': 5821, 'MVPspace': 5822, '這う': 5823, 'スクリプト': 5824, '組': 5825, 'ホント': 5826, '話し合っ': 5827, '奨励': 5828, '重大': 5829, '欠陥': 5830, 'トリーサ': 5831, 'おり': 5832, '単体': 5833, 'ボックス': 5834, 'かいし': 5835, 'しほん': 5836, 'ゲーミング': 5837, '0年ぶり': 5838, '冷静': 5839, 'コメ': 5840, '現れ': 5841, '目立つ': 5842, '離れる': 5843, 'コメ欄': 5844, 'クソワロタ': 5845, 'MVP': 5846, 'SPACE': 5847, 'ルナハイ': 5848, '二次創作': 5849, '権利': 5850, '違反': 5851, 'リュジェホン': 5852, '指揮系統': 5853, 'つながっ': 5854, '連動': 5855, 'もうい': 5856, 'ろいろ': 5857, 'まんま': 5858, '数式': 5859, '論理': 5860, 'フーリエ変換': 5861, '光学': 5862, '工学': 5863, '幾何学': 5864, '電気': 5865, '欲しかっ': 5866, '劫火': 5867, '経典': 5868, 'ドウシテコウナッタ': 5869, '懲役0年': 5870, '返し': 5871, 'だけど': 5872, '自分のために': 5873, '言えないよ': 5874, '人材不足': 5875, '込ん': 5876, '言える': 5877, 'はたして': 5878, 'ジェットストリームアタック': 5879, '検索エンジン': 5880, '引っかかる': 5881, '伸びる': 5882, '旦那': 5883, 'HAHA': 5884, '変わん': 5885, '無表情': 5886, '吐き気': 5887, '位置づける': 5888, '結びつか': 5889, '将来': 5890, '捉える': 5891, '湧い': 5892, '結びつく': 5893, '番': 5894, 'wtf': 5895, '望遠鏡': 5896, 'ルナコロ': 5897, '休まら': 5898, '大きい': 5899, '清水': 5900, 'bacon': 5901, 'jack': 5902, 'owec': 5903, 'ここら': 5904, '辺': 5905, 'くらっ': 5906, 'ばいいん': 5907, 'バスティオンラインハルト': 5908, '対処法': 5909, 'セット': 5910, '作れれ': 5911, '的外れ': 5912, '捉え': 5913, '然': 5914, 'PT': 5915, 'なんとも': 5916, 'すごいっ': 5917, 'くるし': 5918, 'チーター': 5919, '囲い': 5920, '立てて': 5921, '不手際': 5922, 'コメントアレ': 5923, 'るん': 5924, 'birdring': 5925, '超イケメン': 5926, 'エアリアル': 5927, 'バルサ': 5928, 'スタメン': 5929, 'ベタ': 5930, 'ミン': 5931, '読み方': 5932, 'ドラクエ0': 5933, 'マルティナ': 5934, '可': 5935, '愛す': 5936, 'ぎんか': 5937, 'カーブ': 5938, 'ごろ': 5939, 'FIFA': 5940, '軌道': 5941, 'シュート': 5942, 'ぜみ': 5943, 'pc': 5944, '組み立': 5945, '初期不良': 5946, '組み上げ': 5947, 'モデル': 5948, '達人': 5949, 'エーリアンウェア': 5950, '見づらく': 5951, '差し替え': 5952, 'ブラスク': 5953, 'CS': 5954, 'O0': 5955, 'ブログネタ': 5956, 'スコア': 5957, 'ワンちゃん': 5958, 'キルアシスト': 5959, 'どい': 5960, 'かれる': 5961, 'フォーラム': 5962, '書き込む': 5963, '蹴ら': 5964, 'サレンダー': 5965, 'スナイパー': 5966, '片方': 5967, '用': 5968, '源氏': 5969, 'ズンバ': 5970, '両方': 5971, '成立': 5972, '塞い': 5973, '掴み': 5974, '安定性': 5975, '左右': 5976, 'おk': 5977, 'ミラティブ': 5978, '入室': 5979, 'nTwitch': 5980, '比べ': 5981, '加速': 5982, '重視': 5983, '文脈': 5984, 'たい人': 5985, '満足感': 5986, '含む': 5987, '形式': 5988, 'スムーズ': 5989, '利する': 5990, 'ズバッと': 5991, '言い切っ': 5992, '問題点': 5993, '洗い出し': 5994, '改善': 5995, '洗い出す': 5996, '語れる': 5997, '電子機器': 5998, '語ら': 5999, '長時間': 6000, '守れ': 6001, '損益分岐点': 6002, 'nYoutube': 6003, 'において': 6004, '可能性': 6005, 'マネタイズ': 6006, '明文化': 6007, '事務所': 6008, 'シンプル': 6009, '参入': 6010, '言語': 6011, '政府': 6012, '人件費': 6013, '削減': 6014, '障害': 6015, 'プロジェクト': 6016, '名付け': 6017, 'ざっと': 6018, 'た感': 6019, 'ハローワーク': 6020, 'デバッグ': 6021, 'おもえ': 6022, 'フラワー': 6023, 'ひねくれ': 6024, 'jcg': 6025, '人少': 6026, 'ハーモニクス': 6027, '何回': 6028, 'チームワーク': 6029, '荒れる': 6030, 'デュームフィスト': 6031, '崩壊': 6032, 'リス': 6033, 'ハメ': 6034, '攻メ': 6035, 'オーストラリア': 6036, 'ダブルスナイパー': 6037, '少なかっ': 6038, '虐殺': 6039, 'ショー': 6040, '韓国代表': 6041, 'オランダ': 6042, 'ポーランド': 6043, 'Twoeasy': 6044, 'オーバー': 6045, '振り向け': 6046, 'dhu': 6047, 'dolu': 6048, 'dwu': 6049, 'ndwu': 6050, 'ームフィスト': 6051, '小': 6052, 'ギリ': 6053, '届か': 6054, '丁度': 6055, '届く': 6056, 'かしいかえん': 6057, '目安': 6058, '−': 6059, '集まれ': 6060, '気楽': 6061, '揺れる': 6062, 'AIM': 6063, 'うっと': 6064, 'おしい': 6065, 'エンジョイスクリムゲーマーズクラン': 6066, 'g': 6067, 'ベンチマーク': 6068, '最適化': 6069, '大した': 6070, 'AMD': 6071, 'マザーボード': 6072, 'GPU': 6073, '買い換える': 6074, '決まり': 6075, 'Intell': 6076, 'ゆれ': 6077, 'すぎや': 6078, '非公開': 6079, 'リスト': 6080, 'おもんない': 6081, '連鎖的': 6082, '共著': 6083, '国際': 6084, '通っ': 6085, 'シックス': 6086, 'モノマネ': 6087, '浮かし': 6088, 'やり方': 6089, '肘': 6090, 'でかす': 6091, 'みよ': 6092, 'gg': 6093, '半減': 6094, 'タクティカルバイザー': 6095, 'アナルシオ': 6096, '打ち勝と': 6097, 'envy': 6098, 'AP': 6099, 'EX': 6100, 'ｗｗｗｗｗｗｗｗｗｗ': 6101, 'B': 6102, 'スプラ': 6103, 'ちょろっと': 6104, 'Splatoon': 6105, '塗っ': 6106, 'ディープラーニング': 6107, '回路': 6108, '事象': 6109, 'ラベリング': 6110, '全自動': 6111, 'イヤホン': 6112, 'なくす': 6113, 'い説': 6114, '部': 6115, 'イ': 6116, 'グラボ': 6117, '乗': 6118, 'エイムアシストマックス': 6119, '見渡せ': 6120, 'エイムアシストバリバリ': 6121, '遅': 6122, '反撃': 6123, 'フラバン': 6124, '溜まり': 6125, '好評': 6126, 'にて': 6127, 'wordpress': 6128, 'gif': 6129, '挿入': 6130, '貼り': 6131, '読み込み': 6132, '遅く': 6133, '原理': 6134, '読み込む': 6135, '情報量': 6136, 'うい': 6137, '堂': 6138, 'ハリー': 6139, 'まとめ記事': 6140, '凄いっ': 6141, 'すね': 6142, '駅': 6143, 'バナナ': 6144, 'ジュース': 6145, '一人暮らし': 6146, 'ふと': 6147, '食べる': 6148, 'ーエモーショナル': 6149, 'エブリデイ': 6150, 'ミーティング': 6151, '遅刻': 6152, '絵師': 6153, '描く': 6154, '乳首': 6155, 'uDDFE': 6156, 'こうっ': 6157, '人たち': 6158, '相手チーム': 6159, 'moba': 6160, 'やらし': 6161, '散々': 6162, '日本勢': 6163, 'プレーオフ': 6164, '食い下がっ': 6165, '嬉しかっ': 6166, '中洲': 6167, '日常': 6168, '光景': 6169, '取り返し': 6170, 'ウィンストントレゲンノ': 6171, 'god': 6172, 'claire': 6173, 'Aetar': 6174, '坂': 6175, 'ペイ': 6176, 'へん': 6177, '国': 6178, 'ぇべ': 6179, '再開': 6180, 'からかね': 6181, 'アツフォーカスヤバ': 6182, 'ジャスパー': 6183, 'trill': 6184, 'インタビュアー': 6185, 'マリクフォルテ': 6186, 'フラッシュウルブズメイン': 6187, '当てる': 6188, 'マクリーウルト': 6189, '溜まる': 6190, 'deadeye': 6191, 'Another': 6192, 'タイ': 6193, 'モウ': 6194, 'タイモウマクリー': 6195, '神龍': 6196, '撃剣': 6197, 'タイミングリーパー': 6198, 'レイス': 6199, 'ちょうど': 6200, 'スタンスミス': 6201, 'NiP': 6202, 'ペイロード': 6203, 'ミスターグッドエイム': 6204, '正味': 6205, '姿': 6206, 'パーツ': 6207, '検討': 6208, '美し': 6209, '問う': 6210, 'しん': 6211, 'ぺー': 6212, 'お話し': 6213, '哲学': 6214, '具現化': 6215, '著': 6216, '実に': 6217, '年代': 6218, '関わり': 6219, '中心': 6220, '同': 6221, '世代': 6222, 'グロース': 6223, 'ゆるふわ': 6224, '座談会': 6225, 'メガネ': 6226, 'タッチペン': 6227, '写す': 6228, 'ソフト': 6229, 'nDiscord': 6230, '筑波': 6231, '通過': 6232, 'good': 6233, 'きそう': 6234, 'altm': 6235, '帰ろ': 6236, '恋しい': 6237, '代表選': 6238, 'ほんとに': 6239, '正念場': 6240, 'フィンランド': 6241, '抜ける': 6242, 'とっても': 6243, '同率': 6244, '直接対決': 6245, 'ベトナム': 6246, 'スペイン': 6247, '中西': 6248, 'みき': 6249, 'ちゃん': 6250, 'いちいち': 6251, '値段': 6252, '問い合わせ': 6253, '二度手間': 6254, 'よず': 6255, '慣れ': 6256, '異国': 6257, '地': 6258, '疲弊': 6259, 'リフ': 6260, '潰す': 6261, 'ハリフ': 6262, 'スター': 6263, 'ベビーディーバ': 6264, 'ナノ': 6265, 'ぶつけ': 6266, '結果的': 6267, 'わー': 6268, 'いこ': 6269, 'ハリーフックソルジャー': 6270, 'あらら': 6271, 'Aktm': 6272, 'マクリーチート': 6273, 'チームメイト': 6274, '国なん': 6275, 'だい': 6276, 'りてん': 6277, 'JPWIN': 6278, 'うめー': 6279, 'ジャパン': 6280, 'ばれー': 6281, 'ぐながらぶりんくしてるけど': 6282, 'スイッチ': 6283, '希望小売価格': 6284, 'アマゾン': 6285, '汚': 6286, 'ハイセンシ': 6287, '繊細': 6288, 'いづ': 6289, 'ゾエル': 6290, '相変わらず': 6291, '早稲田': 6292, '卒': 6293, '基づく': 6294, '論理展開': 6295, '魔境': 6296, '語っ': 6297, 'らっしゃる': 6298, 'ペンギン': 6299, '率いる': 6300, '民': 6301, '額': 6302, 'チー': 6303, '入ろう': 6304, '月日': 6305, 'きり': 6306, 'ひと': 6307, '布団': 6308, 'カメムシ': 6309, '見かける': 6310, '負荷': 6311, '長期間': 6312, '持続': 6313, '至上主義': 6314, '削っ': 6315, 'いわゆる': 6316, 'IT系': 6317, '気合': 6318, '余計': 6319, 'こなせる': 6320, 'フルタイム': 6321, 'DTNG': 6322, '回戦': 6323, 'sf0': 6324, 'ステージ': 6325, '幼少期': 6326, 'ゲーム機': 6327, '娯楽': 6328, 'サムシング': 6329, 'あああああ': 6330, 'フルスクラッチ': 6331, '行列': 6332, 'おけ': 6333, '後悔': 6334, 'くぅー': 6335, '殆ど': 6336, '戦術': 6337, '求人': 6338, '任三郎': 6339, 'ういい': 6340, '無敵': 6341, '解け': 6342, '動け': 6343, '呼び方': 6344, '正し': 6345, '寝よ': 6346, '取り戻そ': 6347, 'リア友': 6348, 'ぅぅ': 6349, 'ぅ': 6350, '見よ': 6351, 'イヤホンジャック': 6352, 'ビジネス街': 6353, 'いつき': 6354, '混ん': 6355, '開き': 6356, '何故': 6357, '0d': 6358, 'ps': 6359, 'ハンドガン': 6360, 'W杯': 6361, '人外': 6362, '登り': 6363, 'デンマーク': 6364, '司会': 6365, '気まず': 6366, 'エイムアシスト': 6367, '不自然': 6368, '不公平': 6369, '産ん': 6370, '無くし': 6371, 'なんだろう': 6372, '嫌悪感': 6373, 'コントローラー': 6374, '自由度': 6375, '補う': 6376, 'まう': 6377, 'さー': 6378, '小さく': 6379, 'シバターバリ': 6380, 'エンターテイナー': 6381, '油': 6382, 'プロレス': 6383, '構造': 6384, 'ハード': 6385, '敷居': 6386, 'インターネット上': 6387, '切り取ら': 6388, '生み出さ': 6389, '抜き取ら': 6390, 'vc': 6391, '降りる': 6392, 'ナイス': 6393, 'オチ': 6394, '向井': 6395, 'すまん': 6396, 'cross': 6397, 'modal': 6398, 'haptics': 6399, 'ツエー': 6400, 'オキュラスリフト': 6401, '売ら': 6402, 'オキュラス': 6403, '悩み': 6404, '都市': 6405, '買わ': 6406, '0億円': 6407, 'レッツワイズ': 6408, '叩きつける': 6409, '死にかけ': 6410, 'h0z0': 6411, 'ゲーマー': 6412, '定数': 6413, '奪い合い': 6414, '大義名分': 6415, '掲げ': 6416, '目線': 6417, '盛り上げよ': 6418, '要因': 6419, '送る': 6420, '遠征': 6421, 'しんどかっ': 6422, 'モニター': 6423, 'アーム': 6424, '迷っ': 6425, 'サッチャー': 6426, '名言': 6427, 'お金持ち': 6428, '貧乏': 6429, '貧乏人': 6430, '通じる': 6431, 'エモーショナル': 6432, 'くせ': 6433, 'エントリ': 6434, '名文': 6435, '嫉妬': 6436, '悪口': 6437, '無意味': 6438, 'スッと': 6439, '痛く': 6440, '進捗': 6441, 'ハースストーン': 6442, 'corento': 6443, '脱退': 6444, 'デト': 6445, '愚痴る': 6446, '愚痴っ': 6447, '毀損': 6448, '賠償金': 6449, 'デトネ': 6450, 'ロス': 6451, 'キス': 6452, 'きたす': 6453, '構築': 6454, '聖人': 6455, 'ごとき': 6456, 'キレる': 6457, 'ロルト': 6458, 'jeff': 6459, 'ズレ': 6460, 'どうしても': 6461, 'バイアス': 6462, '多数': 6463, 'ジェフ': 6464, 'ツイッター民': 6465, '上級': 6466, 'さえ': 6467, 'デベロッパー': 6468, 'ブラウザ': 6469, '視聴者': 6470, 'クラウド': 6471, 'テレビ': 6472, 'つなが': 6473, '遅延': 6474, '0K': 6475, 'つながる': 6476, '世界観': 6477, 'Stadia': 6478, '歓迎': 6479, '寝れ': 6480, 'dexo': 6481, '唐突': 6482, '心臓': 6483, '中学時代': 6484, '積み': 6485, '台': 6486, '軽く': 6487, 'PTR': 6488, 'ptr': 6489, 'デュー': 6490, 'む': 6491, 'フィスト': 6492, '負けず嫌い': 6493, 'ドゥームフィスト': 6494, 'doomfist': 6495, '速報': 6496, '書こ': 6497, 'プラン': 6498, '聞き取り': 6499, 'NELFD': 6500, '焦点': 6501, '追い詰め': 6502, 'マイナー': 6503, '事務作業': 6504, 'ゲーミングマウス': 6505, 'うすい': 6506, 'スルメ': 6507, 'スプレンダー': 6508, '日本版': 6509, 'GOSU': 6510, 'フィーリング': 6511, '除い': 6512, 'ダイブメタ': 6513, 'Fuck': 6514, 'renderrrrrrrrrr': 6515, '文字数': 6516, '多けれ': 6517, '凶悪': 6518, '古': 6519, '最新版': 6520, '未満': 6521, 'メイト': 6522, '話題': 6523, 'めんどくさい': 6524, 'ファボ': 6525, 'undertale': 6526, '雪だるま': 6527, 'cs': 6528, 'イケメン': 6529, 'コネ': 6530, 'ヤフー': 6531, '週休': 6532, '月間': 6533, '整え': 6534, '対し': 6535, 'つける': 6536, '無償': 6537, '嫌わ': 6538, '矛盾': 6539, 'これだけ': 6540, 'ねっ': 6541, 'zoel': 6542, '容姿': 6543, '捏造': 6544, 'バレ': 6545, 'ツイートパフォーマンス': 6546, '新社会人': 6547, '停止': 6548, 'Diablo': 6549, 'まさお': 6550, 'ドルディン': 6551, 'まさ': 6552, 'おどる': 6553, 'ディン': 6554, 'マイノリティ': 6555, '耳': 6556, '傾ける': 6557, 'マジョリティ': 6558, 'キャッチアップ': 6559, 'かけよ': 6560, 'といった': 6561, '項目': 6562, 'なにか': 6563, 'レイコー': 6564, '橋': 6565, 'ポン': 6566, '定石': 6567, '擬似': 6568, 'やれる': 6569, 'がっぽ': 6570, 'そや': 6571, 'せん': 6572, 'ステルスコーチ': 6573, '手腕': 6574, '拝見': 6575, '可愛かっ': 6576, 'GL': 6577, '交互': 6578, 'ざとやってんのかな': 6579, 'eac': 6580, 'CGB': 6581, 'ミスティック': 6582, 'わき': 6583, 'ラスカルジェスターニ': 6584, 'セブンス': 6585, '左前': 6586, '座っ': 6587, 'コンプレックス': 6588, 'つたない': 6589, '馬鹿': 6590, 'AOC': 6591, 'にこ': 6592, 'でか': 6593, 'ps0': 6594, 'スタヌー': 6595, 'あらし': 6596, 'あらわれ': 6597, '微分積分': 6598, '線形代数': 6599, '物理': 6600, 'ハンドガンボウガン': 6601, '湧き': 6602, 'レッドオーシャン': 6603, 'ブルーオーシャン': 6604, '計画': 6605, '織り込む': 6606, '計測': 6607, '困る': 6608, '正論': 6609, '間違っ': 6610, 'するどい': 6611, 'いつか': 6612, '弱まっ': 6613, 'か決': 6614, 'た方': 6615, '伝承': 6616, '追う': 6617, '後ブ': 6618, '割と': 6619, '樹脂': 6620, 'トンチンカン': 6621, '美しい': 6622, '対価': 6623, '不健全': 6624, '小銭': 6625, '乗せ': 6626, 'アフィカスアフィカス': 6627, '日本語字幕': 6628, '某氏': 6629, '金曜': 6630, 'ポケモン': 6631, 'スッキリ': 6632, '猛烈': 6633, 'ぃすられててたのしかった': 6634, '目立ち': 6635, '自尊心': 6636, 'したがり': 6637, '抱え': 6638, '猿': 6639, '典型例': 6640, 'ブラック': 6641, '国交省': 6642, '部署': 6643, 'delave': 6644, '悲しく': 6645, '永田町': 6646, 'じゃぶじゃぶ': 6647, '紹介': 6648, '侵害': 6649, '有る': 6650, '終バス': 6651, '弱体化': 6652, 'その他': 6653, 'てつまん': 6654, '読者': 6655, 'お客様': 6656, '飲み会': 6657, 'ふん': 6658, 'ラインハルトナーフ': 6659, 'きっ': 6660, 'かっこよく': 6661, 'ツッコミ': 6662, '流れる': 6663, '注目': 6664, '根幹': 6665, '人いれ': 6666, '日本語翻訳': 6667, '日本語訳': 6668, '付ける': 6669, 'ろか': 6670, 'グレー': 6671, 'スカイフル': 6672, '揃えろ': 6673, 'プラチナーマスター': 6674, 'しろっ': 6675, '同意': 6676, 'スカイ': 6677, 'USAOVERWATCH': 6678, 'てりゃ': 6679, '寺田心': 6680, '感情論': 6681, '平行線': 6682, '辿る': 6683, '可視': 6684, '探す': 6685, 'バオドゥーエンジン': 6686, 'DreamTeam': 6687, 'ソーシャル': 6688, '特': 6689, '不幸': 6690, 'では': 6691, '物': 6692, '報': 6693, '割れる': 6694, '進ん': 6695, 'ゲームコーチングサイト': 6696, 'adobe': 6697, '軽い': 6698, '教わり': 6699, '売買': 6700, '次第': 6701, 'エディタ': 6702, '体系': 6703, 'nUI': 6704, '入り口': 6705, '後進国': 6706, '後進': 6707, '投資ファンド': 6708, '追いつける': 6709, '推測': 6710, 'サムネイル': 6711, '偏重': 6712, '広告収入': 6713, '起因': 6714, 'サブスクモデル': 6715, '時計': 6716, '針': 6717, '先進国': 6718, 'タッグ': 6719, 'ビジネスモデル': 6720, '白紙': 6721, '投資額': 6722, '極める': 6723, '無くなっ': 6724, '合戦': 6725, 'しっくり': 6726, '捕捉': 6727, '湧く': 6728, '叩く': 6729, '風潮': 6730, 'ファーストペンギン': 6731, '血': 6732, '海': 6733, '飛び込ん': 6734, 'お絵描き': 6735, 'Ipad': 6736, '労力': 6737, 'aster': 6738, '過剰': 6739, '書き方': 6740, '国語': 6741, '書き手': 6742, '至ら': 6743, 'あいまっ': 6744, '賛否両論': 6745, '大炎上': 6746, '巻き起こし': 6747, '偉': 6748, '飛ばす': 6749, 'バズ': 6750, 'り方': 6751, '詳しい': 6752, 'もし': 6753, '通り': 6754, '莫大': 6755, '❤': 6756, '️': 6757, 'ばか': 6758, '怖がっ': 6759, '代案': 6760, '気付い': 6761, '戦法': 6762, 'デメリット': 6763, '建設': 6764, 'エモエモ': 6765, '得たい': 6766, 'したこと': 6767, '断定': 6768, '反感': 6769, '秀逸': 6770, '広める': 6771, 'あえて': 6772, 'ワンパターン': 6773, '主流': 6774, '外れ': 6775, '大々的': 6776, 'あふれ': 6777, '成功': 6778, '現行': 6779, '誰も知らない': 6780, 'astar': 6781, 'つぶやい': 6782, 'zunba': 6783, 'ryu': 6784, '規約違反': 6785, 'タブー': 6786, 'TL': 6787, '訳す': 6788, '開い': 6789, '役': 6790, '立た': 6791, 'トップレベル': 6792, '素早い': 6793, 'OverwatchBlog': 6794, '0chまとめサイト': 6795, '訳する': 6796, '特有': 6797, '言い回し': 6798, '会': 6799, '新大久保': 6800, '秒間': 6801, '必読': 6802, '難': 6803, 'しみ': 6804, 'こかさ': 6805, 'ねんね': 6806, 'DVA': 6807, 'かわいいっ': 6808, '楽しん': 6809, '効率的': 6810, 'それでいて': 6811, 'エーリアンウェアゾーン': 6812, '供給': 6813, '思い出せ': 6814, '書き留め': 6815, '親切': 6816, 'pepper': 6817, '掴ん': 6818, '還元': 6819, 'くと': 6820, '寄付': 6821, 'キャスター': 6822, '明後日': 6823, '金曜日': 6824, 'このまま': 6825, '載っけ': 6826, '総': 6827, 'プレ': 6828, 'イ人': 6829, 'まとん': 6830, 'メモリ': 6831, '0gb': 6832, '上がり': 6833, '呟き': 6834, 'いくよ': 6835, '現実世界': 6836, '出し合っ': 6837, 'クラウドソーシング': 6838, '出来上がる': 6839, 'カッコヨク': 6840, '校正': 6841, '投げる': 6842, '載っ': 6843, '揃う': 6844, 'まずは': 6845, '日本一': 6846, 'ミロ': 6847, 'コンビ': 6848, '猛威': 6849, '振るっ': 6850, 'それと': 6851, 'Sさん': 6852, 'TS': 6853, 'スパイギアデュオ': 6854, '索敵': 6855, '軽量': 6856, '空中': 6857, '充電': 6858, '受け入れ': 6859, '溢れ': 6860, 'logicool': 6861, '独占': 6862, '相対': 6863, '振れ': 6864, '極めれ': 6865, 'メジャー': 6866, 'すくなくとも': 6867, '0本': 6868, '網羅': 6869, '目標': 6870, '文章力': 6871, 'だるいっ': 6872, 'シュプリーム': 6873, '吉本': 6874, '買収': 6875, '封鎖': 6876, '封じる': 6877, 'nDva': 6878, 'プラチナファラ': 6879, '訳': 6880, '兼ね': 6881, 'クリアリング': 6882, '空': 6883, 'とぼ': 6884, 'しっ': 6885, '割り': 6886, '単語': 6887, '近距離': 6888, '戦お': 6889, 'まずい': 6890, '踏める': 6891, 'どこか': 6892, 'まとまっ': 6893, '作り出す': 6894, 'ググる': 6895, '基準': 6896, '実践': 6897, '試行': 6898, '繰り返す': 6899, '存在価値': 6900, 'つりあげよ': 6901, '教員': 6902, '世界史': 6903, '地理': 6904, 'ムダ': 6905, '受けよ': 6906, 'ゲキヤバ': 6907, '合わ': 6908, 'どこら': 6909, '囲碁': 6910, '整備': 6911, '嫌悪': 6912, '示す': 6913, '民主主義': 6914, '若年層': 6915, '爆': 6916, 'アド': 6917, '損': 6918, 'n国': 6919, 'ポスター': 6920, 'あかるい': 6921, '標榜': 6922, '既得権益': 6923, '表れ': 6924, 'トップダウン': 6925, '人民': 6926, '採用': 6927, 'スイッチングコスト': 6928, 'nシステム': 6929, '諦観': 6930, 'ボトムアップ': 6931, 'AR': 6932, '先端': 6933, '領域': 6934, '模倣': 6935, '新時代': 6936, '見込める': 6937, 'Lobi': 6938, 'HANAMURA': 6939, '広義': 6940, '可読性': 6941, '広げ': 6942, '一般的': 6943, 'クローズド': 6944, '速': 6945, 'それなら': 6946, '考': 6947, '加わら': 6948, '指標': 6949, 'エモエモエモ': 6950, '社会的地位': 6951, '攻め立て': 6952, '見つける': 6953, 'フォーエバーチャットファイト': 6954, 'バトル': 6955, '正当': 6956, '打ち倒し': 6957, '醍醐味': 6958, '戦い': 6959, 'nTop': 6960, 'かみ': 6961, '山': 6962, 'なき': 6963, 'せめぎ': 6964, '儚': 6965, 'べる': 6966, 'ぃつよ': 6967, '高けれ': 6968, '対照実験': 6969, 'イチャイチャ': 6970, '黒い': 6971, '服': 6972, '子': 6973, '可愛く': 6974, '番組': 6975, '囲ま': 6976, '写真': 6977, '撮っ': 6978, 'ねぎっ': 6979, 'たんか': 6980, '役得': 6981, '例外': 6982, '選考': 6983, 'USG': 6984, '別格': 6985, 'ゲーミングキーボード': 6986, 'テンキー': 6987, 'ロジクール': 6988, 'センサー': 6989, 'ワイヤレス': 6990, '機器': 6991, 'ワイヤレスマウス': 6992, 'zowie': 6993, 'レーザー': 6994, 'デスアダー': 6995, 'クーガー': 6996, '劣化': 6997, '至っ': 6998, 'ロケット': 6999, 'ブランド名': 7000, '止まっ': 7001, 'まま': 7002, 'ゼミ': 7003, 'ねれ': 7004, '溶け': 7005, '録画': 7006, 'ガッツリ': 7007, '一息': 7008, 'シ': 7009, 'NA': 7010, 'ぼーっ': 7011, '振り返り': 7012, '逮捕': 7013, '荒らす': 7014, 'のん': 7015, 'けさ': 7016, 'リプライ': 7017, 'いきなり': 7018, 'フオロウワウー': 7019, 'ボコ': 7020, 'ヘイト': 7021, '不正': 7022, 'っす': 7023, 'テクノロジー': 7024, 'インパクト': 7025, '私大': 7026, '人文': 7027, '図書館科学': 7028, 'しょ': 7029, 'nemus': 7030, 'ipad': 7031, 'ゲーミングディスプレイ': 7032, '面白いっ': 7033, 'ばっち': 7034, '濃度': 7035, 'apex': 7036, 'ボルスカヤ': 7037, '瀕死': 7038, 'URL': 7039, '盛り上がろ': 7040, 'ゃないしどうでもいいから': 7041, '主催者': 7042, 'レートグラマス': 7043, '伝わり': 7044, 'やすけれ': 7045, '伝われ': 7046, 'ないか': 7047, '限ら': 7048, 'あり方': 7049, '話す': 7050, 'シバー': 7051, '眠': 7052, 'エグ': 7053, 'オートエイム': 7054, '比例': 7055, 'Misfits': 7056, '不調': 7057, '多種': 7058, '数多く': 7059, 'メタソンブラ': 7060, '不可欠': 7061, '踏む': 7062, 'マッサージ': 7063, '高周波': 7064, 'ゴロゴロ': 7065, '中学': 7066, '働きかける': 7067, 'もらえれ': 7068, '上位陣': 7069, '新規性': 7070, '順序': 7071, 'オリジナル': 7072, 'USGSP': 7073, '全体的': 7074, 'potm': 7075, '浅い': 7076, 'nggwp': 7077, 'すて': 7078, 'こーち': 7079, '殺人予告': 7080, '書き込み': 7081, '教室': 7082, '黒板': 7083, 'ノー': 7084, '恨み': 7085, 'お世話': 7086, '手出': 7087, '杭': 7088, '外': 7089, 'さらさ': 7090, 'ひん': 7091, 'せいな': 7092, '皆様': 7093, '好か': 7094, 'nonke': 7095, 'gif画像': 7096, '作り方': 7097, 'レイアウト': 7098, '学ん': 7099, '繋がっ': 7100, '追え': 7101, '殿': 7102, '無職': 7103, '呼ばわり': 7104, 'さんま': 7105, 'すりー': 7106, '生きる': 7107, 'ノア': 7108, 'あさん': 7109, 'ガレリア': 7110, 'たのしみ': 7111, 'ガール': 7112, 'open': 7113, 'ゾーイ': 7114, '反転': 7115, '色味': 7116, '間隔': 7117, 'マガジン': 7118, 'きついっ': 7119, '一斉': 7120, '有用': 7121, 'hanatyan': 7122, 'ツイートマン': 7123, 'ロドホ': 7124, 'くりー': 7125, '威力': 7126, 'ブログ記事': 7127, 'STORIA': 7128, '除名': 7129, 'バカバカしい': 7130, 'ナウ': 7131, '部外者': 7132, '並び': 7133, '犯罪者': 7134, '検挙': 7135, '列挙': 7136, '習う': 7137, '存在意義': 7138, '書けれ': 7139, 'uDCA': 7140, '非営利': 7141, '取り扱い': 7142, 'とどまら': 7143, 'べく': 7144, '門戸': 7145, 'アウトプット': 7146, 'アウトソーシング': 7147, 'プレゼンス': 7148, 'いただく': 7149, '五十人': 7150, 'だるく': 7151, 'バンクーバー': 7152, 'ステージ0': 7153, '最終': 7154, 'アトランタ': 7155, 'マッチング': 7156, '領収書': 7157, '忘れる': 7158, '最新情報': 7159, 'negitaku': 7160, '流す': 7161, 'るか': 7162, '一時': 7163, 'Stocklip': 7164, '銘柄': 7165, '赤字': 7166, 'スーパーリーグ': 7167, 'ギトギト': 7168, '黒字': 7169, 'ひどかっ': 7170, '薬局': 7171, '洗浄液': 7172, '効く': 7173, '我慢': 7174, 'Gizzard': 7175, '早漏': 7176, '下ネタ': 7177, 'チンコ': 7178, '論理回路': 7179, 'ツッコミ待ち': 7180, 'もしかして': 7181, 'Zoel': 7182, '妄想': 7183, '生み出し': 7184, '詳細': 7185, '襲わ': 7186, 'ぶん': 7187, 'bkstars': 7188, 'bunny': 7189, '長引い': 7190, '単騎': 7191, 'パネエ': 7192, 'ビジョン': 7193, '追い出さ': 7194, '垂れ流し': 7195, '無価値': 7196, '作ん': 7197, 'つくん': 7198, 'たれ': 7199, 'づけ': 7200, 'まとめサイト': 7201, 'バラバラ': 7202, 'ポータルサイト': 7203, 'USGI': 7204, '相対的': 7205, '誤認': 7206, '謝罪': 7207, '老害': 7208, 'プロゲーマーズ': 7209, '構図': 7210, '入団': 7211, 'storia': 7212, 'おもう': 7213, '求めて': 7214, '焦っ': 7215, 'コンプライアンス': 7216, 'プロ意識': 7217, '薄かっ': 7218, '炎上': 7219, '方面': 7220, '叩か': 7221, 'まくる': 7222, '直訴': 7223, '出場資格': 7224, '皆さん': 7225, '落ち着こ': 7226, 'ちな': 7227, '執筆': 7228, 'ブラックジョーク': 7229, '盛り込も': 7230, '邪魔': 7231, 'センシティブな問題': 7232, '荒れ': 7233, '迷惑': 7234, '社会的': 7235, '認めよ': 7236, '炎上マーケティング': 7237, '熱い': 7238, 'これぞ': 7239, 'エンターテイメント': 7240, 'どうと': 7241, 'せっかく': 7242, '0回目': 7243, '杯': 7244, '先週': 7245, '盛り上がっ': 7246, '打ち込め': 7247, '使お': 7248, 'コリアンプロ': 7249, '生': 7250, 'だったん': 7251, 'ヘッドライン': 7252, '張り付い': 7253, 'ばす': 7254, 'クラメンデュオ': 7255, '軍': 7256, '団ラン': 7257, 'ゾ': 7258, '終電': 7259, 'オナニーマスター黒沢': 7260, '洗わ': 7261, '取り組める': 7262, 'BI': 7263, '人間らしく': 7264, '目指そ': 7265, '生計': 7266, 'ベーシックインカム': 7267, '春休み': 7268, '曜日感覚': 7269, '引っ張る': 7270, '得する': 7271, '年下': 7272, '真価': 7273, '奮い立た': 7274, '引っ張っ': 7275, '誹謗': 7276, '中傷': 7277, 'パワーワード': 7278, 'Runaway': 7279, 'セミプロ': 7280, 'ダサい': 7281, '事情': 7282, 'ahq': 7283, '再生回数': 7284, '描こ': 7285, 'プロゲーミングチーム': 7286, '搾取': 7287, '午前': 7288, 'サボっ': 7289, 'さと': 7290, 'タメ口': 7291, 'ボカロ': 7292, '山手線': 7293, '無法地帯': 7294, '返す': 7295, '足手まとい': 7296, '見れる': 7297, '赤坂': 7298, '袋': 7299, 'メイク': 7300, '緑': 7301, 'スト': 7302, 'そっくり': 7303, '意識高い系': 7304, 'katoo': 7305, 'スーパー': 7306, '熱心': 7307, 'kino': 7308, 'ko': 7309, 'mendokusai': 7310, 'neru': 7311, '驚嘆': 7312, 'お釣り': 7313, 'キリキリ': 7314, '当事者意識': 7315, '自戒': 7316, '卒業': 7317, '買える': 7318, '私立大学': 7319, '長崎': 7320, 'ウエスレヤン': 7321, '肉薄': 7322, 'Winston': 7323, '休日': 7324, '蒸し': 7325, 'ポリゴン': 7326, '0D酔い': 7327, '映像': 7328, 'ぐるぐる': 7329, '酔わ': 7330, 'したい': 7331, '自作PC': 7332, '借り': 7333, '再': 7334, 'シバター': 7335, 'メインロスター': 7336, 'cm': 7337, '吸い': 7338, '付い': 7339, 'ワンマグ': 7340, 'Effect': 7341, 'ばり': 7342, 'トレーサーエイム': 7343, 'かんたん': 7344, 'E': 7345, 'かよ': 7346, 'ナンバー0': 7347, 'ライト': 7348, 'スルメゲー': 7349, '短く': 7350, '楽しめ': 7351, '三日': 7352, '五日': 7353, '泥棒': 7354, 'uDD': 7355, '被弾': 7356, 'wifi': 7357, 'ヘルプ': 7358, 'ヘルプページ': 7359, '方針': 7360, 'ベンチャー': 7361, '促進': 7362, '行政': 7363, '下らな': 7364, 'つぶれる': 7365, '中間': 7366, '税': 7367, '利益誘導': 7368, '喜ば': 7369, 'おもちゃ': 7370, 'hirou': 7371, 'sugoi': 7372, 'スケーラビリティ': 7373, 'n中': 7374, '同義': 7375, '交通': 7376, '便': 7377, 'キャッチ': 7378, '騒い': 7379, '煩悩': 7380, 'モロに': 7381, '充て': 7382, '背': 7383, 'づらかっ': 7384, '余り': 7385, 'デスクワーク': 7386, '働き': 7387, '卓球': 7388, 'アッパー': 7389, '0才': 7390, '日本の人': 7391, '各国': 7392, '進め方': 7393, 'ハングリー精神': 7394, 'フィルタリング': 7395, 'GameWith': 7396, 'コンソール': 7397, '取り組ん': 7398, '攻略wiki': 7399, 'Dizzy': 7400, '原則': 7401, '定量': 7402, '筋': 7403, 'い道': 7404, '勝と': 7405, '死屍累々': 7406, '前日': 7407, 'ninja': 7408, 'キャリー': 7409, '一躍': 7410, 'ドリーム': 7411, 'NRG': 7412, 'アメリカンドリーム': 7413, 'おく': 7414, 'スゲー': 7415, 'パブリックドメイン': 7416, 'メリットデメリット': 7417, '語り': 7418, 'つくせ': 7419, '求めよ': 7420, '漁っ': 7421, 'nesports': 7422, '視座': 7423, 'sports': 7424, '市場規模': 7425, '語る': 7426, 'HADO': 7427, '拡張': 7428, 'スマートホン': 7429, '浸透': 7430, 'PCゲーム': 7431, '同列': 7432, '産業': 7433, '枠組み': 7434, '伴っ': 7435, '掛け合わ': 7436, 'ホン': 7437, 'それら': 7438, '広がっ': 7439, 'ウォッチャー': 7440, 'ゲームセンター': 7441, '化し': 7442, '早朝': 7443, '校': 7444, 'はやっ': 7445, 'バレー': 7446, '体罰': 7447, 'パラシュート': 7448, '0キロ': 7449, 'マッハパンチ': 7450, '繰り出し': 7451, 'ロビー': 7452, 'ナンバーゼロ': 7453, 'スタヌスパイギア': 7454, 'コンドーム': 7455, 'arduino': 7456, 'java': 7457, '世界一': 7458, 'あつめ': 7459, 'スタ': 7460, '脳内': 7461, 'オンリー': 7462, '据え置き': 7463, 'コンシューマ': 7464, 'nVR': 7465, 'しきっ': 7466, '盛り上がる': 7467, 'アーハン': 7468, 'afb': 7469, 'mano': 7470, 'ウマ': 7471, 'ばい': 7472, '練ら': 7473, 'ワンヒーラートールビョーンオリーサ': 7474, '止める': 7475, '八': 7476, '捻出': 7477, 'ミリ': 7478, '土下座': 7479, '会わ': 7480, '会う': 7481, 'シグナリング': 7482, '虚しい': 7483, 'アルデュイ': 7484, 'ノノノノ': 7485, '小手先': 7486, '其の': 7487, '凌ぎ': 7488, 'みじんこ': 7489, '生物': 7490, 'ゴミダァ': 7491, '大物': 7492, 'TitanX': 7493, 'つなぐ': 7494, 'のようなもの': 7495, '濃ゆい': 7496, '遠く': 7497, 'ついでに': 7498, 'PCケース': 7499, '買い替え': 7500, '予想通り': 7501, 'カエル': 7502, '鳴き声': 7503, 'ノコギリ': 7504, '木': 7505, '切ろ': 7506, '池': 7507, 'べた': 7508, 'みんく': 7509, '何より': 7510, '集約': 7511, '検閲': 7512, 'ストレスブースト': 7513, 'ソフトウェア': 7514, 'えん': 7515, 'インテル': 7516, '引き抜か': 7517, 'あほ': 7518, 'デトネーション': 7519, '堂々': 7520, 'てかっ': 7521, 'こいい': 7522, '酒': 7523, 'おかず': 7524, '据え': 7525, 'たひ': 7526, 'ちゃんこ': 7527, '負けん気': 7528, '男前': 7529, '単調': 7530, '耐性': 7531, '体育': 7532, '東大生': 7533, 'っしょ': 7534, 'ホワイト': 7535, '難儀': 7536, '内部': 7537, 'ネット上': 7538, '怖かっ': 7539, '腐らす': 7540, '勿体無い': 7541, '配慮': 7542, '支え': 7543, 'リア': 7544, '冷たく': 7545, '刻': 7546, '駆ける': 7547, '少女': 7548, '数少ない': 7549, '叫': 7550, 'びまくっててすげ': 7551, 'ヌルヌル': 7552, '液晶': 7553, 'アルファド': 7554, '君': 7555, 'スペック': 7556, '組め': 7557, '出せん': 7558, 'もうちょい': 7559, 'gtx': 7560, '安物': 7561, '優先': 7562, '秋田': 7563, 'ウキウキ': 7564, 'ドライバインストール': 7565, 'トリプルエックス': 7566, '申し込ま': 7567, 'インターネット接続': 7568, '復旧': 7569, '対戦': 7570, '誘っ': 7571, '₍₍': 7572, '꒪່౪̮꒪່': 7573, '⁾⁾': 7574, '浮気': 7575, 'あるある': 7576, '関わる': 7577, '自己主張': 7578, 'オラオラ': 7579, '島田': 7580, 'ハストン': 7581, 'Beta': 7582, 'Test': 7583, 'Today': 7584, 'rate': 7585, 'Games': 7586, 'Used': 7587, 'time': 7588, 'heros': 7589, 'reinhardt': 7590, 'winston': 7591, 'lucio': 7592, 'todays': 7593, 'KH': 7594, '結ん': 7595, 'かから': 7596, 'スポンサー契約': 7597, '成城石井': 7598, 'ブルジョア': 7599, '設営': 7600, 'ボクシング': 7601, '背中': 7602, '合っ': 7603, '楽しも': 7604, '修復': 7605, 'つけれ': 7606, '燃え上がる': 7607, '徳': 7608, 'らっしゃい': 7609, 'コントロールシンメトラ': 7610, '申し訳ない': 7611, '挑戦者': 7612, '海賊': 7613, 'ウォリアー': 7614, 'アグロドルイド': 7615, 'メタル': 7616, '四つ': 7617, 'ガチマッチ': 7618, 'ニルグ': 7619, 'イロハ': 7620, '教わっ': 7621, 'ダコ': 7622, 'けしからん': 7623, '稼': 7624, 'ぐのはけしからんっておもって': 7625, 'ストリートファッション': 7626, 'ごつい': 7627, '開発チーム': 7628, '試行錯誤': 7629, 'デザイン案': 7630, 'キャラクター': 7631, '込め': 7632, 'にわたって': 7633, '審査': 7634, '決済手数料': 7635, '異質': 7636, 'サブスクリプション': 7637, 'フリーミアム': 7638, 'サブスクライブ': 7639, 'Udemy': 7640, 'ボーナス': 7641, 'クエスト': 7642, 'プリースト': 7643, '挑発': 7644, '連発': 7645, 'ミッドレンジパラディン': 7646, 'クエストローグ': 7647, '九時': 7648, 'C0': 7649, '大丈夫': 7650, 'ハースゲーマーズ': 7651, 'トレビア': 7652, '競争': 7653, '激し': 7654, '送り': 7655, '若い': 7656, '磨か': 7657, '思いっきり': 7658, '過ごす': 7659, '同時': 7660, '進行': 7661, '絶対無理': 7662, 'USB': 7663, 'SSD': 7664, '行こう': 7665, '詰まっ': 7666, '聞こ': 7667, 'デイリーミッションクリア': 7668, 'ウォーロック': 7669, 'ダイナミックディスク': 7670, 'パーティション': 7671, '区切っ': 7672, 'ハードウェア': 7673, 'フォーマット': 7674, 'まみれ': 7675, '圏': 7676, 'BTO': 7677, '買え': 7678, 'OS': 7679, 'インストール': 7680, 'インスコ': 7681, 'きんわ': 7682, 'ubi': 7683, 'ジャガイモ': 7684, '炊き': 7685, 'スクワット': 7686, '上流': 7687, '受け継い': 7688, '確信': 7689, 'ディスティニードロー': 7690, '一発逆転': 7691, '動き回る': 7692, '息切れ': 7693, 'きると': 7694, 'GeForceONAIR': 7695, 'Google検索': 7696, 'ぱくる': 7697, '確': 7698, 'エモート': 7699, 'アドバンテージ': 7700, 'BIOS': 7701, '日本初': 7702, '見応え': 7703, 'pung': 7704, 'ギリートサプ': 7705, 'サイハテ': 7706, '積極': 7707, '活性化': 7708, 'もっともっと': 7709, '豊か': 7710, 'なくなり': 7711, '消え去り': 7712, '尊い': 7713, 'ニートオンリー': 7714, 'バッチ': 7715, 'リテーナー': 7716, 'フルボッコ': 7717, '阻害': 7718, '左右対称': 7719, 'いらん': 7720, '濃かっ': 7721, '痛感': 7722, '高橋さん': 7723, 'ガー': 7724, 'しぃ': 7725, 'ゆたぽん': 7726, 'zonda': 7727, '順々': 7728, '近': 7729, 'ゲージ': 7730, '組織的': 7731, '想定': 7732, '統率': 7733, '兵役': 7734, '集団行動': 7735, '室': 7736, '開成高校': 7737, 'ヤンキー': 7738, 'につれ': 7739, '真っ当': 7740, '高杉': 7741, '利き': 7742, 'amazon': 7743, '詐欺': 7744, '値下げ': 7745, '先取り': 7746, 'ユニフォーム': 7747, 'おかし': 7748, 'イカ': 7749, 'セントス': 7750, 'セン': 7751, 'トス': 7752, '要件': 7753, '寝坊': 7754, 'たて': 7755, '選ん': 7756, 'ドリームチーム': 7757, 'ナゲッツ': 7758, '親子': 7759, '一般': 7760, 'ばら': 7761, '歴': 7762, '選出': 7763, 'パッと': 7764, '反省会': 7765, '発し': 7766, 'カジュアルゲーマー': 7767, '引退': 7768, 'ディスコ': 7769, '制約': 7770, '稼ご': 7771, '延長': 7772, '稼げれ': 7773, 'オッケー': 7774, 'ボヤー': 7775, 'FPSwatcher': 7776, '褒め': 7777, '0万円': 7778, 'せいぜい': 7779, 'nFPS': 7780, 'コピー': 7781, '知名': 7782, '杉草': 7783, 'ノンケ': 7784, 'パチ': 7785, 'マリ': 7786, 'たけ': 7787, '申し訳': 7788, 'tips': 7789, '十倍': 7790, 'にらめっこ': 7791, 'ブサイク': 7792, '優劣': 7793, '自爆テロ': 7794, 'エキサイティング': 7795, '秘め': 7796, '赴く': 7797, '自作': 7798, 'る説': 7799, '濃厚': 7800, '悟空': 7801, '思い浮かべ': 7802, 'ツクモ': 7803, '最': 7804, '安': 7805, '実店舗': 7806, '買い換え': 7807, '電気店': 7808, 'ミドルスペック': 7809, 'ハイスペック': 7810, '価格差': 7811, 'コスパ': 7812, 'ぽんぽこ': 7813, '六万': 7814, '済ん': 7815, 'ミロウィンストン': 7816, '飛び出す': 7817, 'ノック': 7818, '孤立': 7819, '等しく': 7820, '休学': 7821, '再生': 7822, '略称': 7823, '改名': 7824, '由来': 7825, '本名': 7826, 'ヘッドホン': 7827, '虫': 7828, '欠点': 7829, 'アペレジェマジ': 7830, 'バトロワ': 7831, 'アベマ': 7832, 'ウルトラゲームスチャンネル': 7833, '整理': 7834, '格ゲー': 7835, '多岐': 7836, 'わたっ': 7837, 'さっぱり': 7838, '嗜好': 7839, 'シャドバ': 7840, 'AbemaTV': 7841, '放映': 7842, 'スマホユーザー': 7843, 'オンライン': 7844, 'テレビ局': 7845, '縛ら': 7846, '放送': 7847, '形態': 7848, '再現': 7849, 'ウルトラゲームス': 7850, 'SE': 7851, '周期': 7852, '独裁主義': 7853, '偽っ': 7854, '本垢': 7855, 'テンプレ': 7856, '万か': 7857, 'b': 7858, 'amd': 7859, 'ryzen': 7860, 'i': 7861, 'k': 7862, 'R0': 7863, 'サムライ': 7864, 'しゃ': 7865, 'きめ': 7866, '挙げる': 7867, '悲劇のヒロイン': 7868, '所々': 7869, 'キモい': 7870, 'オーラ': 7871, '際': 7872, 'Numlocked': 7873, 'ポンコツ': 7874, 'あんな': 7875, 'ハルク': 7876, 'Lazer': 7877, 'kittenz': 7878, 'ヘッドコーチ': 7879, 'IDDQD': 7880, 'ありえん': 7881, '行方': 7882, '溶かさ': 7883, 'numlocked': 7884, 'ハルトランク': 7885, '四位': 7886, '化け物': 7887, 'sanctum': 7888, '縦長': 7889, 'ももたん': 7890, 'クソロングチャージ': 7891, 'スプレッドシート': 7892, '滝田': 7893, '木滝': 7894, '専属': 7895, 'グルーピングアップ': 7896, '健康': 7897, 'プリセット': 7898, '保存': 7899, '取り出す': 7900, '時間的': 7901, '委託': 7902, '発動': 7903, '逆転': 7904, '中部地方': 7905, '愛知県': 7906, '県': 7907, '柵': 7908, '通らん': 7909, 'すり抜ける': 7910, 'むく': 7911, '気絶': 7912, 'スカッド': 7913, 'あそこ': 7914, 'ぶち込ん': 7915, 'ガス': 7916, '運転': 7917, 'フリーズ': 7918, '全滅': 7919, 'マチェット': 7920, '爆笑': 7921, 'クレーム': 7922, 'ヒジ': 7923, 'まっ': 7924, 'ち': 7925, '文字化け': 7926, '文字列': 7927, 'inque': 7928, '過疎': 7929, 'オンゲ': 7930, 'カスタムメイド0D0': 7931, 'スクリーム': 7932, '高台': 7933, '飛び越え': 7934, 'クレストゲーミング': 7935, 'プルプル': 7936, '招待': 7937, 'エンビー': 7938, '半': 7939, '国主': 7940, '導': 7941, '制度': 7942, '取り入れ': 7943, 'ローン': 7944, '作り上げ': 7945, '減らす': 7946, '主導': 7947, '足並み': 7948, '電子マネー': 7949, '導入': 7950, 'ゴリラ': 7951, '溶ける': 7952, 'uru': 7953, 'ca': 7954, 'FW': 7955, '対野': 7956, 'stylus': 7957, 'スタイラス': 7958, 'フルパランクマ': 7959, 'コンビニ': 7960, 'ホテル': 7961, '無人': 7962, '比べる': 7963, '成果': 7964, '生み出せる': 7965, 'まだまだ': 7966, '過労': 7967, 'いざ': 7968, 'ブラジル人': 7969, 'uDDE': 7970, 'uDDF': 7971, '欲': 7972, '金髪': 7973, 'うっ': 7974, 'ウルカ': 7975, 'オリンピック': 7976, '物理的': 7977, '足音': 7978, '聞こえ': 7979, 'どり': 7980, 'にも': 7981, 'スコ': 7982, 'だぁ': 7983, '太刀打ち': 7984, 'チョッパリヌーブ': 7985, 'ネーム': 7986, 'ダッシュ': 7987, 'うさぎ': 7988, '跳び': 7989, 'つらい': 7990, 'ウィキ': 7991, 'すり減らし': 7992, 'するり': 7993, '後衛': 7994, 'ブツブツ': 7995, '精神状態': 7996, '自身': 7997, 'STEM': 7998, 'はっ': 7999, 'owW': 8000, '採択': 8001, '発売': 8002, '休ま': 8003, 'view': 8004, '0時間後': 8005, '直感的': 8006, 'つけよ': 8007, '玄関': 8008, 'ちの': 8009, 'はいれ': 8010, '断言': 8011, '法的': 8012, '円筒': 8013, '辞書': 8014, '穴埋め': 8015, 'すう': 8016, '現代人': 8017, 'toeic': 8018, 'すみ': 8019, '詰める': 8020, 'だるかっ': 8021, 'キーロック': 8022, '死ぬかと思った': 8023, 'サンシスター': 8024, 'しそ': 8025, 'M0': 8026, '下し': 8027, '争い': 8028, '恐れる': 8029, 'フリー': 8030, 'フラバンガ': 8031, '消せ': 8032, 'ナノブ': 8033, '殴る': 8034, 'ふり': 8035, '読み切っ': 8036, '殴れ': 8037, '末': 8038, 'しゃぶら': 8039, 'ペイパル': 8040, '個人間送金': 8041, '振り込み': 8042, '毎月': 8043, '支払っ': 8044, 'バカバカし': 8045, 'さま': 8046, '監督': 8047, '作品': 8048, 'legends': 8049, '年末調整': 8050, '確定申告': 8051, 'い場所': 8052, '絞る': 8053, 'グッズ': 8054, '運営会社': 8055, '売り上げ': 8056, '損失': 8057, 'に対する': 8058, '頻繁': 8059, '共闘': 8060, '高まっ': 8061, 'ゲームイベント': 8062, 'しゃぶり': 8063, 'シャカ': 8064, '曰く': 8065, 'ずらし': 8066, '戦え': 8067, 'ぽーん': 8068, '飛ば': 8069, 'トランポリン': 8070, '先輩': 8071, 'しっぷう': 8072, '乙': 8073, 'すかー': 8074, '騒音': 8075, '苦情': 8076, '全敗': 8077, 'ファイヤ': 8078, 'ボール': 8079, 'まとめよ': 8080, '逃げられない': 8081, '押す': 8082, '残党': 8083, 'ゆっくり': 8084, '起こさ': 8085, '白星': 8086, 'immortals': 8087, 'エイリアンウェアー': 8088, 'マンスリーメレー': 8089, 'beta': 8090, 'test': 8091, 'ダイブアンチ': 8092, '通い': 8093, '最低賃金': 8094, 'インフレ': 8095, '貨幣': 8096, 'さげれ': 8097, 'ジンバブエ': 8098, 'ジンバブエドル': 8099, 'それに': 8100, 'タグ': 8101, 'りの': 8102, '追っかけ': 8103, '芋': 8104, '壊さ': 8105, '置き': 8106, '疑う': 8107, '核爆弾': 8108, '降っ': 8109, '降る': 8110, 'ひきこもる': 8111, 'はそん': 8112, 'ロー': 8113, '人的': 8114, 'シャターガード': 8115, '深まっ': 8116, '深み': 8117, '隠れる': 8118, '飛べ': 8119, '浴びる': 8120, '隠れ': 8121, 'フォーカスルシオ': 8122, 'フライングルシオ': 8123, '学園': 8124, 'ADHD': 8125, 'ナード': 8126, 'ジョック': 8127, 'いじめ': 8128, '持ち上げ': 8129, 'カレント': 8130, 'ミスマッチ': 8131, '起こる': 8132, 'マジハッピー': 8133, '再掲': 8134, '旨': 8135, '自営業': 8136, '休ん': 8137, 'うまいっ': 8138, '極限': 8139, '七月': 8140, '餌': 8141, 'レイレイ': 8142, '進出': 8143, 'さひ': 8144, 'post': 8145, 'truth': 8146, '真実': 8147, '悦に入る': 8148, '言葉自体': 8149, '資源': 8150, '食物': 8151, '生産': 8152, '容易': 8153, '尊敬': 8154, 'モテ': 8155, '捉えよ': 8156, '外国人': 8157, '留学生': 8158, 'ぱぶ': 8159, '焦る': 8160, '時期': 8161, 'チーデスエイム': 8162, '問い': 8163, '定時': 8164, '帰れる': 8165, 'フリーランチ': 8166, '嫌っ': 8167, '下がら': 8168, 'むずすぎぃ': 8169, 'アーケード': 8170, 'よっしゃ': 8171, 'レジェンダリー': 8172, 'ビシュカー': 8173, '原点': 8174, 'へー': 8175, '遠距離': 8176, 'なんぼ': 8177, 'たのしい': 8178, '聞こえん': 8179, '生え': 8180, 'なお': 8181, '模様': 8182, 'ゆるかっ': 8183, '遮音': 8184, '音質': 8185, 'ns': 8186, '暗黙のルール': 8187, 'ド': 8188, 'ｗｗｗ': 8189, 'きっと': 8190, '両手': 8191, '両足': 8192, 'あららら': 8193, '控えめに言って': 8194, 'Deeplearning': 8195, '立ち位置': 8196, 'スリープ': 8197, 'キープ': 8198, '余ら': 8199, '浅': 8200, '粘り': 8201, '経験値': 8202, '見失う': 8203, '深まる': 8204, 'マンブー': 8205, 'ファラマーシー': 8206, 'おしまい': 8207, 'potg': 8208, 'ゴリラウルト': 8209, 'ゾンダ': 8210, 'OMENCUP': 8211, 'アメケンキャリー': 8212, 'アメケン': 8213, '馬杉': 8214, 'あび': 8215, 'フォーカスゲキアツ': 8216, 'カイザー': 8217, '対照的': 8218, 'えぐかっ': 8219, '守っ': 8220, '下ろせる': 8221, 'ｗｗ': 8222, '後退': 8223, '反射神経': 8224, 'こなし': 8225, 'ランナウェイ': 8226, '選手紹介': 8227, '合わし': 8228, 'パクパクパク': 8229, 'スリー': 8230, 'だーつ': 8231, 'ユニバーシティ': 8232, '囲ん': 8233, '材料': 8234, 'むなしい': 8235, 'らし': 8236, '画期的': 8237, '宇宙船': 8238, '反面': 8239, 'WPG': 8240, 'シャタースポット': 8241, '東西': 8242, 'はまっ': 8243, 'ペルソナ0': 8244, 'ときめきメモリアル': 8245, '回帰': 8246, 'せよ': 8247, '若いやつ': 8248, '0票': 8249, '重み': 8250, '平均寿命': 8251, '不利益': 8252, '被ら': 8253, '勝た': 8254, '増': 8255, '被り': 8256, 'ポスト': 8257, 'チラシ': 8258, '投函': 8259, '北千住': 8260, '食え': 8261, '美味い': 8262, '小学0年生': 8263, 'スプラトゥーン': 8264, '時代の流れ': 8265, '迷う': 8266, 'エブリデイファラマーシー': 8267, '自閉症': 8268, '扱う': 8269, 'd0': 8270, '算数': 8271, 'すぎん': 8272, '英雄': 8273, '半ば': 8274, '途絶える': 8275, '無念': 8276, 'pt': 8277, 'うらやま': 8278, '客': 8279, '連勝': 8280, 'まくれ': 8281, 'スカイプ': 8282, 'OPEN': 8283, '出よ': 8284, '新入生': 8285, '三つ': 8286, '過': 8287, '疎っ': 8288, 'る言': 8289, 'われ': 8290, '中華料理': 8291, 'まずさ': 8292, 'ムカムカ': 8293, '技': 8294, '釣っ': 8295, '押しつける': 8296, 'sanmer': 8297, '団子': 8298, '複数': 8299, '隊': 8300, 'ホロレンズ': 8301, 'マイクロソフト': 8302, '〆': 8303, 'ドン': 8304, '活': 8305, '準備': 8306, 'むのめんどいしね': 8307, 'ばんばん': 8308, 'ぎるしそのわかりやふい': 8309, 'メダル': 8310, '美味しい': 8311, '拙者': 8312, '候': 8313, '戻ら': 8314, '仲間意識': 8315, '受け取っ': 8316, '感情的': 8317, 'ことも': 8318, '光ら': 8319, 'ていいん': 8320, 'やけど': 8321, '各社': 8322, 'バリエーション': 8323, 'IE': 8324, 'クローン': 8325, '0w': 8326, 'l': 8327, '所感': 8328, '下位互換': 8329, '有線': 8330, '見当たら': 8331, 'ソール': 8332, '統一': 8333, '重さ': 8334, 'ワイヤー': 8335, '重く': 8336, '慣れる': 8337, '売ろ': 8338, 'ウルトゲージ': 8339, '消費': 8340, 'ローリスクハイリターン': 8341, '公式サイト': 8342, 'おなか': 8343, 'やってくん': 8344, '秒速': 8345, 'ﾏﾁﾞﾑﾘ': 8346, 'クラメ': 8347, '出し惜しみ': 8348, '絞っ': 8349, '吐い': 8350, '恥ずかしく': 8351, 'マクソル': 8352, 'リーパーホッグ': 8353, 'かまた': 8354, 'ウルトガンガン': 8355, '刺さり': 8356, 'ソル': 8357, 'ジャーメイン': 8358, '通用': 8359, '飛車': 8360, '効き': 8361, '引き分け': 8362, 'もちこん': 8363, 'ジャンプバグ': 8364, 'ふやさ': 8365, 'ふろ': 8366, 'ぐっ': 8367, '発展途上国': 8368, '地下鉄': 8369, '先導': 8370, '町中': 8371, '途上国': 8372, '古い': 8373, 'たとえば': 8374, 'いずれ': 8375, '追い抜か': 8376, 'オメンカップ': 8377, 'KHTV': 8378, '弱いっ': 8379, '使い道': 8380, 'いつみ': 8381, 'Duo': 8382, '正式': 8383, 'さも': 8384, 'やから': 8385, '終了': 8386, 'バグジャンプ': 8387, '気分転換': 8388, 'ec0': 8389, 'ヨドバシ': 8390, 'L': 8391, 'フィールド': 8392, '善': 8393, '扱っ': 8394, 'こき下ろし': 8395, '悦': 8396, '浸る': 8397, '視力': 8398, '難なく': 8399, '暮らせ': 8400, '視覚障害者': 8401, '援助': 8402, '素晴らしく': 8403, '代表監督': 8404, 'かんけい': 8405, 'えらん': 8406, 'うの': 8407, '委員': 8408, 'ワイ': 8409, '渡し': 8410, 'ススェーデン': 8411, '✈': 8412, 'uDDEF': 8413, 'ルシオナーフ': 8414, 'ダイブコンプ': 8415, '指揮': 8416, '方式': 8417, '上官': 8418, '命令': 8419, 'したがっ': 8420, '異議': 8421, '唱える': 8422, '迅速': 8423, '後作': 8424, 'ディーバ': 8425, '優しい世界': 8426, '流行る': 8427, 'ダブルスナイパーメタ': 8428, 'タンクゲンジ': 8429, '浅かっ': 8430, '仮眠': 8431, '長生き': 8432, '吐か': 8433, 'サージ': 8434, 'ああああああああああああああああああああああああああああああああああああああああ': 8435, 'あああああああああああああああああああああああああああああああああああああ': 8436, 'ああああああああ': 8437, 'ダブルキル': 8438, '豆鉄砲': 8439, 'ああああああああああああああああああああああ': 8440, '野獣先輩': 8441, '淫夢': 8442, '作り出せる': 8443, 'レンジ': 8444, '置ける': 8445, 'リーパーマジ': 8446, '腐ら': 8447, 'ワイワイトロールランクマ': 8448, 'グンニョン': 8449, '渋い': 8450, 'ナルト': 8451, 'ガチピック': 8452, 'ネパール': 8453, '落とせる': 8454, 'ジャンクラガチピック': 8455, '狭め': 8456, '首': 8457, '絞め': 8458, '死ね': 8459, 'もらお': 8460, 'むしろ': 8461, '消極': 8462, '次なん': 8463, '攻める': 8464, '傷ん': 8465, '赤石': 8466, '溜める': 8467, '延々': 8468, '這っ': 8469, 'ヒー': 8470, '逃がさ': 8471, 'くらわす': 8472, '現': 8473, 'マスターハンド': 8474, 'あっち': 8475, '会い': 8476, '旅行': 8477, 'iPad': 8478, '物理キーボード': 8479, '外出': 8480, 'Adobe': 8481, 'いじっ': 8482, '持ち運び': 8483, '闘': 8484, '会議': 8485, 'アイコン': 8486, '眼鏡': 8487, '派': 8488, 'キーワード': 8489, 'プランナー': 8490, '一向に': 8491, 'UX': 8492, '荒野': 8493, '荒野行動': 8494, '和気あいあい': 8495, 'ミラティブインストール': 8496, 'もみない': 8497, 'OpenREC': 8498, '肌': 8499, 'Esports': 8500, 'よき': 8501, '適材適所': 8502, 'はぁ': 8503, 'なり金': 8504, '当たれる': 8505, '止めよ': 8506, '分からん': 8507, '留め': 8508, '卒業式': 8509, 'バト': 8510, 'ぐら': 8511, 'ぼったくり': 8512, 'バー': 8513, 'pay': 8514, 'win': 8515, 'さがし': 8516, 'みつから': 8517, 'ヒカキン': 8518, '欲望': 8519, '薄': 8520, '使命': 8521, '反応速度': 8522, 'ハンマー': 8523, '範囲': 8524, 'とかん': 8525, '防げ': 8526, '減らし': 8527, 'すませる': 8528, '歩く': 8529, 'しに': 8530, 'デレーブ': 8531, 'とどまる': 8532, 'ワンキル': 8533, '真っ先': 8534, 'アンド': 8535, 'バッチリ': 8536, '跳ね返さ': 8537, 'チンパンジークラン': 8538, 'おきん': 8539, '失せる': 8540, 'うるか': 8541, '意志': 8542, 'nartisan': 8543, '選ぼ': 8544, 'マジオワタ': 8545, '陣': 8546, 'チャリ': 8547, '挟ん': 8548, 'br': 8549, 'アイテム': 8550, 'あがりや': 8551, 'にたいして': 8552, 'どー': 8553, '瞳': 8554, '可愛': 8555, '封鎖された渋谷で': 8556, 'いうのす': 8557, '学力': 8558, '経済学': 8559, '設ける': 8560, 'ヘリックスエアショ': 8561, 'かます': 8562, 'ｷﾞﾓﾁﾞｲｲｲｲｲｲｲｲｲｲ': 8563, '勝敗': 8564, 'アナルシ': 8565, 'ト金': 8566, 'マーク': 8567, 'あめ': 8568, 'けんさん': 8569, 'サイバーエージェント': 8570, 'fb': 8571, '切り': 8572, '切り返し': 8573, '幅広い': 8574, 'ルサンチマン': 8575, 'シスター': 8576, 'ビギナー': 8577, 'F0': 8578, 'アイフォン': 8579, '続く': 8580, '殴ら': 8581, 'ジワ': 8582, 'ルート0': 8583, '第一': 8584, '特別': 8585, 'ウチ': 8586, 'ビギナーカップ': 8587, 'チーム練習': 8588, '僕らのユリイカ': 8589, 'ちーむ': 8590, '強靭': 8591, '太もも': 8592, '肩': 8593, '胸': 8594, '取り戻し': 8595, '細く': 8596, '危険': 8597, '種目': 8598, '貧血': 8599, '真っ青': 8600, '聴き': 8601, 'NG': 8602, 'キャラデザ': 8603, '爆速': 8604, 'テクニカル': 8605, '願う': 8606, 'アサルトキャプチャ': 8607, '揺り': 8608, '無謀': 8609, 'AFB': 8610, 'LWB': 8611, 'アヌビス': 8612, '門': 8613, '削れ': 8614, '乱戦': 8615, '優先順位': 8616, '調節': 8617, '不安': 8618, '見合っ': 8619, '最中': 8620, 'つられる': 8621, 'チョークポイント': 8622, 'ファイアストライク': 8623, 'wakiyan': 8624, '解体': 8625, '振り分けれ': 8626, '溜まっ': 8627, '希薄': 8628, 'いとこ': 8629, 'ワイルドカード': 8630, 'CSGO': 8631, 'noppo': 8632, '振り回さ': 8633, 'キッズ': 8634, '見れれ': 8635, 'もた': 8636, 'ガソスタ': 8637, 'とれる': 8638, '回り込ん': 8639, '意表': 8640, '突く': 8641, 'シャターマジ': 8642, 'Kさん': 8643, '判断基準': 8644, '転ば': 8645, 'コリアンサーバー': 8646, '0試合': 8647, 'ボロボロ': 8648, 'ボーナスゲーム': 8649, 'ハイ': 8650, '意気消沈': 8651, 'ナノゲンジ': 8652, 'まら': 8653, '拡散希望': 8654, 'nRole': 8655, 'Flex': 8656, 'イン': 8657, 'フレックス': 8658, 'エイペックス': 8659, 'キーバインド': 8660, '根本的': 8661, 'いじろ': 8662, '羽田空港': 8663, '立地': 8664, 'LCC': 8665, '通せ': 8666, 'おっぱい': 8667, 'キャラクターグラ': 8668, '人気声優': 8669, 'Surefour': 8670, '当分': 8671, 'ご飯': 8672, '友達の友達': 8673, '人間不信': 8674, '他人': 8675, 'スマホアプリ': 8676, 'GamerSensei': 8677, '世界的': 8678, '可処分時間': 8679, '食': 8680, 'い合い': 8681, '超えれ': 8682, '平準': 8683, '直に': 8684, '橋本': 8685, '元知': 8686, '利権': 8687, '切り崩す': 8688, '旨味': 8689, '尽力': 8690, '黙っ': 8691, '起業家': 8692, '裁判官': 8693, '法人登記': 8694, '名義': 8695, '飲食店': 8696, 'トレガチ': 8697, '外食': 8698, '手軽': 8699, 'タンパク質': 8700, '天神': 8701, '対話': 8702, '提起': 8703, '引き起こす': 8704, '行動基準': 8705, '攻略方法': 8706, '正確': 8707, '戦慄': 8708, 'nGamerTeach': 8709, 'なきゃ': 8710, '歩き': 8711, '野菜': 8712, 'とれ': 8713, '非の打ち所': 8714, '食品': 8715, '日本中': 8716, '女子高生': 8717, 'タクシー': 8718, '偏差': 8719, '値': 8720, '翌日': 8721, '浅く': 8722, 'チーム全体': 8723, '視覚': 8724, 'たか': 8725, '一目': 8726, 'ソルマクゼニルシ': 8727, 'かない': 8728, '解釈': 8729, '堪え': 8730, '足ん': 8731, 'なかろ': 8732, 'angs': 8733, 'キングダム': 8734, 'わんちゃん': 8735, '狙お': 8736, 'トライ': 8737, 'オモシレー': 8738, 'ホッグウルト': 8739, '妨害': 8740, '収穫': 8741, '貼っ': 8742, '叩き': 8743, '割っ': 8744, 'グレネード': 8745, '細か': 8746, '見直し': 8747, 'ラスティー': 8748, '弾い': 8749, 'ゴッツンコ': 8750, '作り出し': 8751, 'ジェットスター': 8752, 'スカイマーク': 8753, '往復': 8754, '金額': 8755, 'のる': 8756, 'イースポ': 8757, '日間': 8758, '大天使': 8759, '立ち止まっ': 8760, 'ぶっ殺す': 8761, '打ち込む': 8762, 'mickie': 8763, '苦し': 8764, 'キャリアハイ': 8765, '上げれ': 8766, '付与': 8767, 'LOS': 8768, '標準': 8769, '鬱': 8770, 'ーーーーー': 8771, '平穏': 8772, '戻る': 8773, '主要': 8774, 'だー': 8775, 'モット': 8776, '火影': 8777, 'wave': 8778, 'あきち': 8779, '無効': 8780, 'チクチク': 8781, '一ダ': 8782, 'イブ': 8783, '出会っ': 8784, 'towe': 8785, 'スケジュール': 8786, 'リプ': 8787, '助け': 8788, '泊まる': 8789, 'ようがし': 8790, 'なか': 8791, 'ろう': 8792, '取り敢えず': 8793, 'とけ': 8794, '不相応': 8795, '怖く': 8796, '取り返す': 8797, 'current': 8798, 'max': 8799, 'tier': 8800, 'ルシオピック': 8801, '何とも': 8802, '防衛': 8803, '上と下': 8804, 'シーズン中': 8805, '起こす': 8806, '一点集中': 8807, 'rjm': 8808, 'ささ': 8809, '撃っ': 8810, '瓶': 8811, '物質': 8812, 'ゴリラザリア': 8813, 'つつ': 8814, '線': 8815, '向かい合っ': 8816, '木の葉返し': 8817, 'あう': 8818, 'オンファイア': 8819, '驚き': 8820, '副': 8821, '職': 8822, 'AV男優': 8823, 'ルシオキャリー': 8824, '地力': 8825, '備忘録': 8826, 'ゲンジメイン': 8827, 'グロ': 8828, 'エリ': 8829, '防ぐ': 8830, '人間業': 8831, 'にゅー': 8832, 'よーく': 8833, '攻めろ': 8834, 'いったん': 8835, 'なおせ': 8836, 'はか': 8837, 'お願い': 8838, 'サッサウィンストン': 8839, '素': 8840, '射っ': 8841, 'いたん': 8842, 'キングスロウザリア': 8843, '付き': 8844, 'くらわし': 8845, '消さ': 8846, '様子': 8847, '夫': 8848, 'しかも': 8849, '数える': 8850, '戦前': 8851, '甘え': 8852, 'タコ殴り': 8853, '快感': 8854, 'しゃべら': 8855, 'ルシオラジオ': 8856, 'ドロップ': 8857, 'ざび': 8858, 'はやる': 8859, 'EnvuUs': 8860, '息': 8861, 'ネクスト': 8862, 'ウィンストンバフマジ': 8863, 'whoru': 8864, 'フアイウ': 8865, 'るな': 8866, 'うぇい': 8867, 'ちゅ': 8868, 'よいー': 8869, '合わさっ': 8870, '惜しん': 8871, 'rip': 8872, 'フルチャージオーブ': 8873, '全弾命中': 8874, '着い': 8875, 'マーシーブースト': 8876, '一撃': 8877, '刈り取ら': 8878, 'シールド': 8879, '貫通': 8880, '何気に': 8881, '近づく': 8882, 'フランカー': 8883, '疑っ': 8884, '連': 8885, 'ザリアハルト': 8886, '幅広く': 8887, '捨てる': 8888, 'ツイートマジ': 8889, '通る': 8890, 'いれる': 8891, '素質': 8892, 'ついてん': 8893, 'フリーター': 8894, 'ゅお': 8895, '直ん': 8896, '週末': 8897, 'ｐ': 8898, 'ｖ': 8899, 'きる': 8900, '自衛': 8901, 'エグイ': 8902, '共産党': 8903, '隔離': 8904, 'スパムエロサイト': 8905, '踏ん': 8906, 'めんどくさく': 8907, 'ケータイ': 8908, 'お姉さん': 8909, '察し': 8910, 'reddit': 8911, '穴': 8912, '埋める': 8913, '人気ブログ': 8914, '特盛': 8915, '一致': 8916, '団結': 8917, '高低': 8918, 'ゼルダ': 8919, '要': 8920, 'メイウルト': 8921, '貯まる': 8922, 'どうく': 8923, 'よみ': 8924, 'とり': 8925, 'QuakeLive': 8926, 'エースコンバット': 8927, '無双': 8928, 'オナニー': 8929, 'おでん': 8930, 'キムチ': 8931, 'さん家': 8932, '下がり': 8933, 'ループ': 8934, 'カジュアルゲー': 8935, 'もみないっ': 8936, 'マスオバ': 8937, '越える': 8938, '絞ら': 8939, '後続': 8940, 'だり': 8941, '0月0日': 8942, 'Open': 8943, 'Division': 8944, 'ファミ通': 8945, 'における': 8946, 'Openrec': 8947, '仕組': 8948, 'みなのか': 8949, '虹': 8950, '継続的': 8951, '鍛える': 8952, '入場': 8953, '料っ': 8954, 'ほんの': 8955, 'ノウハウ': 8956, '無意識': 8957, 'ぱ': 8958, '平凡': 8959, '実銃': 8960, '打ちまくり': 8961, '月末': 8962, 'Whoru': 8963, '手裏剣': 8964, 'プラス': 8965, '沈め': 8966, 'どっ': 8967, 'talespin': 8968, 'シーズンハイマスター': 8969, '地域': 8970, '求': 8971, 'アサルトマップ': 8972, 'レディット': 8973, 'パスポート': 8974, 'レベリング': 8975, 'ごちゃごちゃ': 8976, 'アイアンクラッド': 8977, '自分たち': 8978, '押し付け': 8979, 'うめる': 8980, 'ンァー': 8981, 'フィニッシュ': 8982, 'スタート': 8983, '龍撃剣': 8984, '振る': 8985, '残': 8986, '射': 8987, '打ち合う': 8988, 'アサブロンズバスティオン': 8989, '突破': 8990, 'ワンマッチ': 8991, '淡々': 8992, '試合前': 8993, '頑張ろ': 8994, 'ワンポイント': 8995, 'してやり': 8996, 'iddqd': 8997, 'Q': 8998, '地区': 8999, '全勝': 9000, '正に': 9001, '体現': 9002, 'nV': 9003, '中0': 9004, '指名': 9005, '舐め': 9006, '錚々たる': 9007, 'Best': 9008, 'スッゲー': 9009, '対峙': 9010, 'ちくり': 9011, '位置取り': 9012, '神剣': 9013, '鍛え': 9014, 'ボロ': 9015, '直さ': 9016, '鈍っ': 9017, 'テンションキレキレ': 9018, '履歴': 9019, '監視': 9020, '判明': 9021, 'ハクサルゲンジ': 9022, '部門': 9023, 'プロゲーミング': 9024, '広報官': 9025, 'mendo': 9026, '笑顔': 9027, 'uncia': 9028, '粘っ': 9029, 'かよく': 9030, '間下': 9031, 'したたか': 9032, 'ゲンジウィンストン': 9033, 'ahp': 9034, '辛かっ': 9035, '爽やか': 9036, 'warrock': 9037, '経過': 9038, '文化的': 9039, '資本': 9040, 'プライベート': 9041, '暴い': 9042, 'ポジティブ': 9043, '中田': 9044, 'はいい': 9045, '手っ取り早い': 9046, 'はちま': 9047, 'なぞ': 9048, 'むって': 9049, '再来': 9050, 'むさん': 9051, '燃え上がら': 9052, 'jespa': 9053, 'たたい': 9054, '売名': 9055, '絡む': 9056, 'アンランクド': 9057, '乱れる': 9058, '戦場': 9059, '早起き': 9060, '出れ': 9061, '宿泊': 9062, '観客': 9063, '損し': 9064, '反故': 9065, '出場': 9066, '呟け': 9067, '裏話': 9068, 'ハイセンシローセンシ': 9069, '抽象': 9070, '待った': 9071, 'テリトリー': 9072, '狭': 9073, '全般': 9074, 'ブログパク': 9075, 'フリーライド': 9076, '翻訳ブログ': 9077, '一儲け': 9078, '土台': 9079, '差し': 9080, '込める': 9081, '純正': 9082, 'GearVR': 9083, 'Iphone': 9084, '目覚める': 9085, '決めれ': 9086, 'コンピューター': 9087, '集合体': 9088, 'ただただ': 9089, 'つなげる': 9090, 'マイナス': 9091, '伝播': 9092, '向ける': 9093, '怖いっ': 9094, 'Arctis': 9095, '眺める': 9096, '絡ま': 9097, '深淵': 9098, '出来事': 9099, '0km': 9100, '漕い': 9101, '年前': 9102, '懐かしい': 9103, 'シャ': 9104, 'ター': 9105, 'キメる': 9106, '有無': 9107, '浮き彫り': 9108, '帳消し': 9109, 'つめ': 9110, 'かて': 9111, '賭け': 9112, '悪いこと': 9113, 'エロイプ': 9114, '晒さ': 9115, '新チーム': 9116, '数百人': 9117, '客席': 9118, 'ガラガラ': 9119, '予選': 9120, 'コメント欄': 9121, '煎じ': 9122, 'どう役': 9123, 'チーターウイドウ': 9124, '訴求力': 9125, 'センシ': 9126, '殺せ': 9127, 'しらす': 9128, 'ぱん': 9129, 'まかせる': 9130, 'コンボ': 9131, 'ヘリックス': 9132, '斬り': 9133, 'ハルトライフ': 9134, '睨み合っ': 9135, '張り': 9136, 'がいいん': 9137, 'ボディフィットモデル': 9138, 'ステロイド': 9139, '分かる': 9140, '紅白': 9141, 'モラトリアム': 9142, 'N0': 9143, 'スタンミ': 9144, 'バンバンスクリム': 9145, 'うけ': 9146, '通算': 9147, '坊主': 9148, '早々': 9149, '遡ら': 9150, '受講': 9151, '着け': 9152, '広告代理店': 9153, '通さ': 9154, 'GO': 9155, '先行者': 9156, 'ずけ': 9157, 'やりかた': 9158, '競合': 9159, '達成': 9160, '遅かっ': 9161, '実は': 9162, 'そろい': 9163, '一喜一憂': 9164, 'ぴするほうが': 9165, '終わろ': 9166, '計画的': 9167, 'ウィンストンゲンジ': 9168, 'インフィニティ': 9169, 'レイコータワー': 9170, 'バシバシ': 9171, 'きらい': 9172, '人達': 9173, '後に': 9174, '発覚': 9175, '違約': 9176, '請求': 9177, '参加者': 9178, 'ローソン': 9179, 'セレクト': 9180, 'あたりめ': 9181, '受験生': 9182, 'ゲーミングPC': 9183, '引き離し': 9184, 'レイスフォーム': 9185, '波': 9186, '止まる': 9187, 'クールタイム': 9188, 'くさ': 9189, 'こか': 9190, '後手': 9191, '使いこなせる': 9192, '放り込ま': 9193, '組める': 9194, 'フォーオナー': 9195, '合格': 9196, '志望': 9197, '受かっ': 9198, 'アタッカー': 9199, '趣': 9200, '回転速度': 9201, 'うまけれ': 9202, 'ave': 9203, '打てれ': 9204, 'スノーボール': 9205, '回復アイテム': 9206, '散策': 9207, '待ち構える': 9208, '乗り越え': 9209, 'こけ': 9210, '脳汁': 9211, '保持': 9212, 'お見合い': 9213, 'ぼろ': 9214, '本格的': 9215, '円形': 9216, '遮ら': 9217, '進路': 9218, 'ーーー': 9219, '所詮': 9220, '補助輪': 9221, '当てはめ': 9222, '弟': 9223, '課せ': 9224, '迫る': 9225, '前半': 9226, 'ーーーー': 9227, 'コリアンランカーマクリー': 9228, 'しかた': 9229, 'デトゴールド': 9230, '真正面': 9231, 'どおり': 9232, 'スコープ': 9233, '不合理': 9234, 'ケツメイシ': 9235, '概要': 9236, '尊重': 9237, 'ペチペチ': 9238, 'ひいては': 9239, '決定力': 9240, 'たまり': 9241, 'マルチキル': 9242, '合わせる': 9243, '対抗': 9244, '策': 9245, '任せ': 9246, 'ヒーローランクマ': 9247, '先攻': 9248, 'サドンデス': 9249, 'サンマボット': 9250, 'に当たって': 9251, 'いたっ': 9252, 'ぼっ': 9253, 'おちんちん': 9254, '恵まれる': 9255, 'イリオス': 9256, 'コントロールシンメ': 9257, 'やりゃ': 9258, 'おまえら': 9259, 'ごみ': 9260, 'めん': 9261, '止まり': 9262, '後者': 9263, '前者': 9264, 'oversumo': 9265, 'エース': 9266, '紅茶': 9267, '寝落ち': 9268, 'もしも': 9269, '機械になりたい': 9270, '連れ': 9271, '治る': 9272, '風邪': 9273, '弱っ': 9274, '体調': 9275, 'カゼ': 9276, '俺氏': 9277, 'overwatcher': 9278, '中距離': 9279, 'ファニングブッパ': 9280, 'リグループ': 9281, '大嘘': 9282, 'キリキリキリキリ': 9283, '寒': 9284, '雪': 9285, 'ひまし': 9286, '疾風': 9287, 'ヘビーローテーション': 9288, 'パイプ': 9289, '配管': 9290, 'ニンジャ': 9291, '取りつかれ': 9292, 'まいまい': 9293, '麻薬': 9294, '下がろ': 9295, '追いつめ': 9296, '追いかける': 9297, '疎通': 9298, '脛': 9299, 'かじっ': 9300, 'ズルズル': 9301, 'チェックポイント': 9302, 'wpg': 9303, '曲がり角': 9304, '当たろ': 9305, '狩ら': 9306, 'あな': 9307, 'あのまま': 9308, '押し込ま': 9309, 'shadowburn': 9310, 'クレイジー': 9311, '知れ': 9312, 'カウント': 9313, '張る': 9314, 'まる': 9315, 'ult': 9316, 'daradara': 9317, '分量': 9318, 'det': 9319, 'パトカー': 9320, '鍵': 9321, '奪っ': 9322, 'ノコノコ': 9323, '地面': 9324, '突き抜け': 9325, '安らぐ': 9326, '軽減': 9327, 'ナノバスティオン': 9328, '撃た': 9329, '加算': 9330, 'ナノタンクモード': 9331, '日本国内': 9332, 'urca': 9333, 'samuraiD': 9334, 'DNG': 9335, '混乱': 9336, 'DNT': 9337, '0期メンバー': 9338, '0軍': 9339, '一軍': 9340, '二軍': 9341, 'アツイ': 9342, 'エイムガバガバ': 9343, 'パンツ一丁': 9344, 'cpu': 9345, '突き抜ける': 9346, '挑む': 9347, '嬲り': 9348, 'チャットオフ': 9349, '命中': 9350, 'ハッカー': 9351, '走っ': 9352, 'ローディング': 9353, '着信': 9354, '防弾': 9355, 'ヘルメット': 9356, 'スナイパーライフル': 9357, 'ゲット': 9358, 'すん': 9359, 'ok': 9360, '防弾チョッキ': 9361, 'ak': 9362, 'ar': 9363, '学名': 9364, 'Ryzen': 9365, '0GB': 9366, '0W': 9367, '妥協': 9368, '主体': 9369, 'MAC': 9370, '勝者総取り': 9371, 'PJS': 9372, '土俵': 9373, 'アマチュアチーム': 9374, '設立': 9375, '進む': 9376, '常勤': 9377, '職員': 9378, '能っ': 9379, '売上高': 9380, 'それだけ': 9381, 'NPO法人': 9382, '募っ': 9383, '定着': 9384, '読み': 9385, 'コントロールハルト': 9386, '春節': 9387, 'イベ': 9388, 'つっこみ': 9389, '冷た': 9390, '吐く': 9391, 'はこ': 9392, '見つかる': 9393, 'お世辞': 9394, 'ナノブガンガン': 9395, '未払い': 9396, 'ひじ': 9397, '組む': 9398, '連敗': 9399, '変わろ': 9400, 'ぶっ飛ばし': 9401, 'ディープコピー': 9402, 'シャローコピー': 9403, '激臭': 9404, 'ネームクラン': 9405, '刻み': 9406, 'はやく': 9407, 'エターナル': 9408, '右上': 9409, 'ゲンジゴリラ': 9410, '襲っ': 9411, '聴覚': 9412, '頼り': 9413, '識別': 9414, 'スワップ': 9415, '交戦': 9416, 'combox': 9417, '豚': 9418, 'faker': 9419, 'すごっ': 9420, 'けた': 9421, 'いまさら': 9422, '元気': 9423, 'イースポーツ': 9424, 'ゲキ': 9425, '臭': 9426, '試合内容': 9427, '溢れる': 9428, '集めよ': 9429, '中間層': 9430, '一月': 9431, '珍しいっ': 9432, '写輪眼': 9433, '開花': 9434, 'リラックスエイム': 9435, 'ラピッドツイッチエイム': 9436, 'ザリアソルジャー': 9437, 'Word': 9438, '霊': 9439, '圧': 9440, 'ウルトバンバン': 9441, 'ナノハルト': 9442, 'サージナノハルト': 9443, '如何': 9444, 'きまっ': 9445, 'ザリゴリ': 9446, 'ザリハルト': 9447, 'シナジーマジ': 9448, 'winwin': 9449, '構える': 9450, 'ザリアメイン': 9451, '配分': 9452, '弾薬': 9453, 'ずらす': 9454, 'ヘラ': 9455, 'ザリアマジ': 9456, 'ステレオ': 9457, 'ミキサー': 9458, '聞ける': 9459, 'マイクミュート': 9460, '申し訳な': 9461, 'いらいら': 9462, 'Discorf': 9463, 'ならん': 9464, 'xl': 9465, 'ナイトオウル': 9466, '取り分': 9467, 'タブ': 9468, 'おそう': 9469, '苦肉の策': 9470, '互角': 9471, 'チョコ': 9472, 'ピックガイジ': 9473, '妙': 9474, 'イタ飯': 9475, '自傷行為': 9476, '食べに': 9477, 'られれ': 9478, 'ブリーザー': 9479, 'ナン': 9480, 'パー': 9481, 'うって': 9482, 'フレーム': 9483, '動作': 9484, '完了': 9485, '撮れ': 9486, '解析': 9487, '月曜': 9488, 'なにより': 9489, 'クローズ': 9490, 'きく': 9491, '見やすし': 9492, '個々': 9493, 'マダ': 9494, 'むかい': 9495, '落とせ': 9496, '①': 9497, '②': 9498, '足元': 9499, '③': 9500, '確立': 9501, '説得力': 9502, '挙げれ': 9503, '活かし': 9504, 'まっとう': 9505, '従っ': 9506, '筋合い': 9507, 'いかなる': 9508, 'ウイドゥ': 9509, 'お達し': 9510, '渋々': 9511, '異文化交流': 9512, 'ハンゾーゲンジ': 9513, '言ってはいけない': 9514, 'むやみ': 9515, '割り切っ': 9516, '押しつけよ': 9517, 'まぁ': 9518, '根底': 9519, '共感': 9520, 'もとめ': 9521, '慰める': 9522, '保て': 9523, '見比べ': 9524, '上位互換': 9525, 'ヨッピー': 9526, 'モテる': 9527, 'ふーん': 9528, '中高生': 9529, 'ビビッ': 9530, 'コリアンゲンジ': 9531, '攻守': 9532, '女性問題': 9533, '女性関係': 9534, 'ディー': 9535, 'あるく': 9536, '取り戻す': 9537, '強引': 9538, '笑わせ': 9539, 'つかめ': 9540, 'もどせる': 9541, 'ヒーローツートップ': 9542, '類': 9543, 'HAYAKU': 9544, 'SA': 9545, 'ZI': 9546, 'UTTE': 9547, 'マクソ': 9548, '脅威': 9549, 'つまらない': 9550, 'PING': 9551, '黒人奴隷': 9552, 'ｓ': 9553, '加えよ': 9554, 'とめ': 9555, 'ザリアバリア': 9556, '宿': 9557, 'やらかし': 9558, 'パット': 9559, 'Mid': 9560, 'Xsoft': 9561, '硬さ': 9562, '触る': 9563, 'nFK': 9564, 'ブンブン': 9565, '振り回し': 9566, '乗り換え': 9567, 'ZA': 9568, 'Rival': 9569, 'pure': 9570, 'nArtisan': 9571, 'さわれ': 9572, 'たのも': 9573, '触り': 9574, '日頃': 9575, '衝突': 9576, '地点': 9577, 'ちんこ': 9578, '村田': 9579, '先生': 9580, '傑作': 9581, 'pi': 9582, 'ng0': 9583, '調子': 9584, '不自由': 9585, 'ワンコン': 9586, '格': 9587, '殺': 9588, '凍結': 9589, '愛情': 9590, '親密さ': 9591, '調和': 9592, '自意識': 9593, 'ロボット': 9594, '給与': 9595, 'たせ': 9596, '部下': 9597, '嫌う': 9598, '聞けば聞くほど': 9599, 'レガシー': 9600, '買い叩か': 9601, 'いびつ': 9602, '近年': 9603, '0代': 9604, '変わり': 9605, 'sudo': 9606, '民間': 9607, '淘汰': 9608, '霞が関': 9609, '官僚': 9610, '低学歴': 9611, '地方自治体': 9612, '高卒': 9613, '職種': 9614, '情報系': 9615, '課程': 9616, 'いまだに': 9617, '強い力': 9618, '日本郵政': 9619, '時価総額': 9620, 'nSaaS': 9621, '霞ヶ関': 9622, '社内': 9623, '自然言語処理': 9624, 'Python': 9625, '士農工商': 9626, 'プログラマー': 9627, 'ケーブル': 9628, '長さ': 9629, '摩擦': 9630, 'アウト': 9631, 'Instagram': 9632, '抽出': 9633, '顔面偏差値': 9634, 'Facemash': 9635, 'サーフィン': 9636, '補助': 9637, 'インターフェース': 9638, 'まね': 9639, '裾野': 9640, '広げる': 9641, '無給': 9642, 'Tfue': 9643, 'Tokyo': 9644, 'Meetup': 9645, 'ミリ秒': 9646, 'nping': 9647, '精密': 9648, '言いふらし': 9649, '大会出場': 9650, '一丸': 9651, 'フォース': 9652, '精神力': 9653, 'ザリアハルトルシオアナ': 9654, '橋上': 9655, 'ogn': 9656, 'kongdoo': 9657, '村社会': 9658, '落ち着き': 9659, '複合': 9660, 'アラ': 9661, 'けなし': 9662, 'そなえ': 9663, '刺激的': 9664, '狩': 9665, 'けっこう': 9666, 'エセダイヤ': 9667, 'はほん': 9668, 'TAB': 9669, '押そ': 9670, 'タイムアタック': 9671, '大声': 9672, 'ブルーハーツ': 9673, '歌い': 9674, 'バイク': 9675, '中二': 9676, '朝練': 9677, 'スパルタゲーマー': 9678, '怖': 9679, 'kenkyu': 9680, 'kitui': 9681, 'natama': 9682, 'ga': 9683, 'kowareru': 9684, 'ええ': 9685, 'ゅごい': 9686, '記憶力': 9687, 'たっての': 9688, 'コラボ': 9689, '在校生': 9690, '日時': 9691, 'あわ': 9692, 'エスカ': 9693, 'rei': 9694, 'nforce': 9695, '確保': 9696, 'マク': 9697, 'バイオテック': 9698, '置か': 9699, 'ran': 9700, 'ra': 9701, '倒せ': 9702, '信ぴょう性': 9703, 'ＴＬ': 9704, 'にぎわっ': 9705, 'ザリアウルト': 9706, 'はよう': 9707, '嬉しく': 9708, 'ザリアハルトホッグアナルシオ': 9709, 'ナノガッチュー': 9710, '残せる': 9711, 'ガキ': 9712, 'ゆる': 9713, 'パンダ': 9714, '滑っ': 9715, 'ビクッと': 9716, 'ほしみ': 9717, 'サッカー日本代表': 9718, '酒井高徳': 9719, '日本の常識': 9720, 'この国': 9721, 'ノリノリ': 9722, 'アナカットー': 9723, '理解不能': 9724, '寛容': 9725, '喜ん': 9726, '何も言わずに': 9727, 'もめ': 9728, '内乱': 9729, '始まら': 9730, 'こる': 9731, 'アサルトマジ': 9732, 'ライバルプレイ': 9733, 'つかう': 9734, '有効活用': 9735, 'オールマイティ': 9736, 'ピンポイント': 9737, 'ロードホッグ': 9738, '人少な': 9739, '破壊': 9740, '致命': 9741, '法': 9742, 'ソンブラマジ': 9743, '慎重': 9744, 'ぼる': 9745, 'スカ': 9746, 'ハルトハック': 9747, '逃げ惑う': 9748, '打ちまくる': 9749, 'ソンブラライバル': 9750, 'たき': 9751, 'ランクマソンブラ': 9752, 'かじゃ': 9753, '身内': 9754, '贔屓': 9755, 'クズ': 9756, '罵る': 9757, 'npt': 9758, '役立た': 9759, '罵ら': 9760, '滝廉太郎': 9761, 'ワンヒーラーデフォ': 9762, 'ノーヒーラー': 9763, '闇': 9764, '0mm': 9765, 'ハンドグリッパーニギニギ': 9766, 'nzowie': 9767, 'Price': 9768, 'Functions': 9769, 'Specification': 9770, 'Looks': 9771, '大学0年生': 9772, '光らせる': 9773, '光れ': 9774, 'かえる': 9775, '爆睡': 9776, '泊まっ': 9777, '困ら': 9778, 'タフ': 9779, 'ほぼほぼ': 9780, 'スペ': 9781, '最低条件': 9782, '小売り': 9783, 'nEA': 9784, '遠い': 9785, '手探り': 9786, 'nコン': 9787, 'トレゲンザリ': 9788, 'ごり': 9789, '電気屋': 9790, 'ROCCAT': 9791, 'KONEPURE': 9792, 'サイズ': 9793, 'njp': 9794, '活発': 9795, '動ける': 9796, '利く': 9797, 'チマチョゴリ': 9798, '専用': 9799, 'スイスロリッシュ': 9800, 'ロードホガーズ': 9801, '祝日': 9802, '頼み': 9803, '否め': 9804, 'ゴリゴリキル': 9805, '狙える': 9806, '奪い取っ': 9807, '高揚': 9808, 'あがら': 9809, 'サンプラス': 9810, 'フェデラー': 9811, 'ロディック': 9812, 'ヒューイット': 9813, '四大大会': 9814, 'ベスト0': 9815, '錦織': 9816, 'ニュース': 9817, '歯': 9818, '不便': 9819, '病気': 9820, '歯医者': 9821, '虫歯': 9822, '治療': 9823, '要望': 9824, 'ごっちゃ': 9825, '雇える': 9826, '潤う': 9827, '換え': 9828, '嘆い': 9829, 'BLeague': 9830, 'ドリームジョブ': 9831, '薄給': 9832, '興行': 9833, 'クラロワ': 9834, '洗練': 9835, '課金システム': 9836, '操作性': 9837, '類似': 9838, '算出': 9839, 'ネットゲーム': 9840, 'やすさ': 9841, 'さらなる': 9842, '課題解決': 9843, 'つなげ': 9844, '原動力': 9845, 'くるしめ': 9846, 'くちゃ': 9847, 'nLTV': 9848, 'デジタルマーケティング': 9849, 'BEE': 9850, 'nhgbsun': 9851, 'FOX': 9852, 'RABBIT': 9853, 'および': 9854, 'なろう': 9855, 'ツヨ': 9856, '貯めよ': 9857, '速さ': 9858, '作ろ': 9859, 'ベルディ': 9860, '生き残っ': 9861, '受け身': 9862, '先手': 9863, '専業': 9864, 'ぱく': 9865, 'スロウ': 9866, '早め': 9867, '当方': 9868, '貼ら': 9869, 'よね': 9870, '仕上がる': 9871, 'Hz': 9872, '通信': 9873, '進歩': 9874, 'かたい': 9875, '短': 9876, '萌え声': 9877, 'kawaii': 9878, 'バズる': 9879, 'PostTruth': 9880, '得て': 9881, '腐る': 9882, '重要視': 9883, '先見': 9884, '大切なこと': 9885, 'どんなに': 9886, '顧客': 9887, '気づけ': 9888, 'あがる': 9889, '与': 9890, 'こわい': 9891, 'キャラメルマキアート': 9892, 'つまむ': 9893, 'スカッと': 9894, 'rankuma': 9895, 'yaru': 9896, 'setsumei': 9897, 'dekinai': 9898, 'kono': 9899, 'yabasa': 9900, 'ato': 9901, 'zikan': 9902, '定量的': 9903, '調べろ': 9904, 'マジﾑﾘﾎﾟﾖ': 9905, 'かぶる': 9906, '取り返そ': 9907, '時に': 9908, 'おかしかっ': 9909, '客観': 9910, '系列': 9911, '初期メンバー': 9912, '競技人口': 9913, 'ロスター': 9914, '一秒': 9915, '窓': 9916, '体い': 9917, '真中': 9918, 'モロ': 9919, 'ウイドウメタ': 9920, '浮かば': 9921, 'ださん': 9922, 'ザンギ': 9923, 'リュウ': 9924, '読み替え': 9925, '汗': 9926, '仲': 9927, '良かろ': 9928, 'ゴミクソ': 9929, '責め': 9930, 'true': 9931, 'erite': 9932, '院試': 9933, 'し役': 9934, '握り': 9935, '錯覚': 9936, 'ちぐはぐ': 9937, '属し': 9938, 'たいてい': 9939, '排除': 9940, 'ボーダーレス': 9941, 'となりのヤングジャンプ': 9942, 'アナワンキル': 9943, '雲': 9944, 'ソルジャーウルト': 9945, '昼夜': 9946, '拮抗': 9947, '暗い': 9948, '昨日今日': 9949, 'ちまちま': 9950, 'フルパワーザリア': 9951, 'ガハハ': 9952, 'ｗｗOPww': 9953, 'ソロランクマ': 9954, 'フラグ': 9955, 'ムービー': 9956, '焼き': 9957, '教養': 9958, 'キャンパス': 9959, 'qck': 9960, '中国製': 9961, 'ローコストマウスパッド': 9962, '信者': 9963, '零': 9964, '特注': 9965, 'クソデカマウスパッド': 9966, '頼も': 9967, 'aim': 9968, 'ハル': 9969, 'ト殺': 9970, 'naim': 9971, 'こりゃ': 9972, 'Ftier': 9973, '竜神': 9974, 'シャンシャン': 9975, '切る': 9976, 'ハイライト': 9977, 'コマ': 9978, 'ソンブラコ': 9979, 'すき焼き': 9980, '言お': 9981, 'haruto': 9982, 'akita': 9983, 'nzarya': 9984, 'de': 9985, 'korosi': 9986, 'makuri': 9987, 'tai': 9988, '飯テロ': 9989, '祭り': 9990, 'かくて': 9991, '東京ドーム': 9992, 'チャリ通': 9993, '歩か': 9994, '原付': 9995, 'くず': 9996, 'ちさ': 9997, '試さ': 9998, 'サイレント': 9999, 'ジャンル': 10000, '待た': 10001, 'チャ': 10002, 'パワー': 10003, '計っ': 10004, 'よめる': 10005, '第一宇宙速度': 10006, 'あけ': 10007, 'た次元': 10008, '超越': 10009, '刑務所': 10010, '高0': 10011, '八月': 10012, '組み立て': 10013, '割ら': 10014, '別々': 10015, 'それや': 10016, '召喚': 10017, '見合い': 10018, '削る': 10019, 'リザレクト': 10020, 'ガンガンキル': 10021, 'Planetoverwatch': 10022, '抜粋': 10023, 'あくまでも': 10024, '私自身': 10025, '私見': 10026, 'スペシャリスト': 10027, '押し上げ': 10028, '富ん': 10029, 'コンポジション': 10030, 'トーナメント': 10031, 'もたらし': 10032, '支持': 10033, 'シャドー': 10034, '暴れまくる': 10035, '先取': 10036, '取り返さ': 10037, '最終ラウンド': 10038, '言い出す': 10039, 'メンタルブロンズ': 10040, '分から': 10041, '戻す': 10042, 'レートクソ': 10043, 'たのしー': 10044, 'www': 10045, '加速装置': 10046, '音速': 10047, '谷内': 10048, 'やせ': 10049, '成人式': 10050, '市長': 10051, '警備員': 10052, '踊っ': 10053, 'ばれ': 10054, 'ツイ廃': 10055, '楽しま': 10056, '判断力': 10057, '平面': 10058, 'すむ': 10059, 'fe': 10060, 'it': 10061, '内戦': 10062, 'おもろかっ': 10063, 'ルリウム': 10064, 'くみ': 10065, 'アナハルトバン': 10066, 'こおる': 10067, '州民': 10068, '繋がる': 10069, '遊ぼ': 10070, '見分け': 10071, 'n女': 10072, 'ラグスイッチ': 10073, 'ラグチーター': 10074, '無修正': 10075, 'スクリムショウ': 10076, 'BOSS': 10077, '一睡': 10078, '生活リズム': 10079, 'アンドエネルギーチャージ': 10080, '姫': 10081, '囲わ': 10082, '要求': 10083, '万国': 10084, '試合開始': 10085, '無事': 10086, '死亡': 10087, 'こわから': 10088, 'マーラインハルト': 10089, '貯めろ': 10090, '音量': 10091, '拾う': 10092, '話さ': 10093, '行きたくない': 10094, 'ござる': 10095, 'タンクウォッチ': 10096, 'ばくばく': 10097, '強制的': 10098, '陳腐': 10099, '入学': 10100, '平成': 10101, '思い出そ': 10102, '年号': 10103, 'なくし': 10104, 'スパゲッティ': 10105, 'いやー': 10106, '心地': 10107, 'se': 10108, 'ubk': 10109, '周辺機器': 10110, 'パズドラ': 10111, '廃': 10112, '人笑': 10113, '人みん': 10114, '利点': 10115, 'からいっ': 10116, 'たほう': 10117, '無名': 10118, 'お菓子': 10119, '食わ': 10120, '見えない敵': 10121, '引き寄せ': 10122, '丸腰': 10123, '全裸': 10124, '繰り出さ': 10125, '珍妙': 10126, '練習量': 10127, '全世界': 10128, 'aimbot': 10129, '施行': 10130, '犯す': 10131, 'いたちごっこ': 10132, 'ngg': 10133, '年越': 10134, '翌': 10135, '落': 10136, '◯': 10137, '自発': 10138, 'シャッター': 10139, '払え': 10140, '遊べ': 10141, '防ぎ': 10142, '切ら': 10143, '心拍数': 10144, 'キャプチャ': 10145, 'PrintScreen': 10146, 'おして': 10147, 'window': 10148, '付属': 10149, 'ペイント': 10150, 'ctrl': 10151, 'V': 10152, '動画キャプチャ': 10153, 'お気楽': 10154, 'めろ': 10155, '落ち着か': 10156, 'W': 10157, '微': 10158, 'エイムボットチーター': 10159, '沸い': 10160, '褐色': 10161, 'エロ': 10162, '魔人': 10163, '石碑': 10164, 'twitterアカウント': 10165, '安価': 10166, '化石': 10167, '半永久': 10168, 'ToS': 10169, '話しかける': 10170, '買い換えれ': 10171, 'モニタ': 10172, 'Realforce': 10173, '刑事': 10174, '大晦日': 10175, '脳味噌': 10176, '沸騰': 10177, '0連敗': 10178, '二月': 10179, '裏切り': 10180, 'ランクマクソ': 10181, 'nVC': 10182, '運ゲー': 10183, 'あいて': 10184, '境目': 10185, '仲良く': 10186, 'こし': 10187, '夢中': 10188, '浪子': 10189, 'ゝ': 10190, 'ひい': 10191, 'おっち': 10192, 'サバ': 10193, 'かくする': 10194, '芸': 10195, '雪合戦': 10196, 'シンメ': 10197, 'ヒーローメイ': 10198, '取り返せる': 10199, '気づか': 10200, '品位': 10201, '貫き通し': 10202, 'みろ': 10203, '被害者': 10204, '見せよ': 10205, '途端': 10206, '凸': 10207, '言いだす': 10208, '絶頂': 10209, '譲っ': 10210, 'オナシャス': 10211, '譲る': 10212, 'ホールホッグ': 10213, '挨拶': 10214, 'ノン': 10215, 'ドーテロフ': 10216, '先月': 10217, 'いっす': 10218, 'ガイジガイジ': 10219, '引か': 10220, 'ボソボソ': 10221, '小言': 10222, '潰せる': 10223, '野生': 10224, 'ダイヤダイヤダイヤダイヤ': 10225, '道のり': 10226, 'Road': 10227, '街コン': 10228, 'クラブ': 10229, '装っ': 10230, '出会お': 10231, '親知らず': 10232, '歯列矯正': 10233, '歯並び': 10234, '治そ': 10235, '顎': 10236, '圧迫': 10237, 'ガタガタ': 10238, '知らず': 10239, '恐怖': 10240, 'エイムイ': 10241, 'プッシュトゥトーク': 10242, 'マイマイ': 10243, 'ハナムラ': 10244, 'クラウドファンディング': 10245, '募る': 10246, 'You': 10247, 'tube': 10248, 'レイヤー': 10249, 'abema': 10250, 'テレビレイヤー': 10251, '制作': 10252, 'ドキュメンタリー': 10253, '濃い': 10254, '携わっ': 10255, 'WOWOW': 10256, '年内': 10257, 'バイラル': 10258, 'Facebook': 10259, 'CAC': 10260, '告知': 10261, '瑣末': 10262, 'ミドル': 10263, '街': 10264, '山本一成': 10265, 'issei': 10266, 'y': 10267, '名人': 10268, 'Overhype': 10269, 'カレー': 10270, 'giveaway': 10271, '食いつく': 10272, '割に': 10273, '車内': 10274, '大安売り': 10275, '切り売り': 10276, '段落': 10277, 'nGG': 10278, 'コンパニオン': 10279, '会える': 10280, '年賀状': 10281, '人間らし': 10282, 'もがい': 10283, 'abara': 10284, '一段落': 10285, 'ああああああああああああああああああああああああああああああああああああ': 10286, 'ディズニー': 10287, 'ランド': 10288, 'ぶっこ': 10289, 'ゴッド': 10290, '飲む': 10291, 'たばこ': 10292, 'エンハンサー': 10293, '減り': 10294, 'なのっ': 10295, 'ぶちのめし': 10296, '凶暴': 10297, '動物': 10298, '森': 10299, 'みると': 10300, '交代': 10301, '制': 10302, '爆音': 10303, 'FF0': 10304, '限る': 10305, 'せろ': 10306, '戦し': 10307, 'キレイ': 10308, 'サーヴェイサーヴェイサーヴェイ': 10309, '可処分所得': 10310, 'お金がない': 10311, '揉ん': 10312, 'でかく': 10313, 'Cカップ': 10314, 'weblio': 10315, '英和辞典': 10316, 'Weblio': 10317, 'nnanotube': 10318, '⇨': 10319, 'ナノチューブ': 10320, '訳出': 10321, 'ペーパー': 10322, '腫れ': 10323, '頭痛': 10324, 'iGS': 10325, 'J0昇格': 10326, 'アビスパ': 10327, 'IGS': 10328, '代': 10329, 'Scrim': 10330, '持て': 10331, '外出禁止': 10332, '令': 10333, '台湾人': 10334, '00度': 10335, '回復力': 10336, '直せる': 10337, '一時期': 10338, 'インフルエンザ': 10339, '突発': 10340, '目処': 10341, '休止': 10342, 'いそがしく': 10343, '区切り': 10344, 'Hanjo': 10345, '査定': 10346, '仕様変更': 10347, 'シーズン0': 10348, '格段': 10349, '返っ': 10350, 'ハゲ': 10351, 'ロング': 10352, 'ビン': 10353, 'いれれ': 10354, '生き残れる': 10355, 'ハルトヒール': 10356, '一連の流れ': 10357, '珍': 10358, 'いたこと': 10359, '舐めプ': 10360, '架空': 10361, '人力': 10362, 'ever': 10363, 'more': 10364, '分布': 10365, 'ntier': 10366, '分かれ目': 10367, '塩漬け': 10368, 'あてる': 10369, 'FL': 10370, 'ゼニウルト': 10371, 'リュジェホンアナ': 10372, '撃ち': 10373, 'フットサル': 10374, '蹴る': 10375, 'がたい': 10376, '練習試合': 10377, '動かさ': 10378, '不健康': 10379, '近づける': 10380, 'Mickie': 10381, 'JOK': 10382, 'ER': 10383, 'バーストヒールエグ': 10384, 'なんとかなる': 10385, 'サイクロプスオーサカ': 10386, '足ら': 10387, '補充': 10388, 'せまい': 10389, 'よぉ': 10390, '鰤': 10391, 'ごめん': 10392, '不和のオーブ': 10393, 'アナゼニ': 10394, '叫ぶ': 10395, 'グダ': 10396, 'キルゴールド': 10397, '休憩': 10398, '厨': 10399, '置き去り': 10400, 'キツイ': 10401, 'イージーゲーム': 10402, 'Razer': 10403, 'BlackWidow': 10404, 'レス': 10405, 'ヒーローピックリスト': 10406, 'NaN': 10407, 'NaNNaN': 10408, 'vain': 10409, 'てま': 10410, '錯誤': 10411, '無力感': 10412, '悩まさ': 10413, '休み': 10414, '転職': 10415, '家族': 10416, '恐ろしく': 10417, 'おいそれと': 10418, '報わ': 10419, '活動資金': 10420, '繋げ': 10421, 'テニス': 10422, 'マジシャン': 10423, '世間': 10424, '恫喝': 10425, '儲から': 10426, 'スタンス': 10427, '働かそ': 10428, '居酒屋': 10429, '契約書': 10430, '金も': 10431, '最低': 10432, '若手': 10433, 'お笑い芸人': 10434, 'おもいこん': 10435, 'ラスティ': 10436, '不可': 10437, 'scrim': 10438, 'アマ': 10439, '射出': 10440, '放物線': 10441, '運動': 10442, '格闘技': 10443, '習得': 10444, '武芸': 10445, 'ファンボ': 10446, '告白': 10447, 'てんか': 10448, 'steelseries': 10449, 'sensei': 10450, 'ざす': 10451, '複垢': 10452, 'ヘッダー': 10453, 'rgb': 10454, 'ぽんぽん': 10455, '引きこもり': 10456, 'シカト': 10457, '安息': 10458, '他校': 10459, '毎晩': 10460, '一言': 10461, '中高': 10462, 'げーと': 10463, '根付か': 10464, 'チケット': 10465, '付く': 10466, '無料配信': 10467, 'esportsleague': 10468, '開幕': 10469, 'JLeague': 10470, '輸入': 10471, '代理店': 10472, '日本製品': 10473, 'eスポ': 10474, '産学官': 10475, '日本大学': 10476, 'ハイプ': 10477, 'Do': 10478, 'ta0': 10479, '上達': 10480, '根本': 10481, '障害者': 10482, 'パーソナライズ': 10483, '0Dプリンター': 10484, '学': 10485, 'グラム': 10486, '健常者': 10487, 'nJTB': 10488, 'nmame': 10489, '表記揺れ': 10490, 'eSports': 10491, '防御': 10492, '日大': 10493, '開催場所': 10494, 'インスタ': 10495, '叩きつけ': 10496, 'ビタミンC': 10497, 'がぶ飲み': 10498, '朝晩': 10499, 'のむ': 10500, 'GreenLeaves': 10501, 'むずくね': 10502, '使い物': 10503, '激しく': 10504, '縦横': 10505, 'いね': 10506, 'ぼろぼろ': 10507, 'SOFT': 10508, '体調不良': 10509, '栄養管理': 10510, '乗り切れる': 10511, '風引': 10512, '働ける': 10513, 'マルチビタミン': 10514, 'スペシャル': 10515, 'ＢＯＸ': 10516, 'てゆーか': 10517, 'ホッ': 10518, 'グ': 10519, 'ジェネレーター': 10520, 'nTwitter': 10521, '原文': 10522, 'シンメトラメタ': 10523, '戦わ': 10524, 'ところで': 10525, 'つかさ': 10526, 'キリッ': 10527, '儚く': 10528, '孕ん': 10529, 'さつき': 10530, '暴走': 10531, '内面': 10532, '描ける': 10533, 'いちご0': 10534, '作者': 10535, 'ラブコメ': 10536, '河下水希': 10537, '機微': 10538, '風邪ひき': 10539, 'IQ': 10540, '外人': 10541, 'コケ': 10542, '遊ば': 10543, '人集': 10544, 'めんば': 10545, '囲っ': 10546, '数こ': 10547, 'なるし': 10548, 'ヌァイイイス': 10549, '言いまくっ': 10550, '冷蔵庫': 10551, 'HP': 10552, 'Shadowburn': 10553, 'リクルート': 10554, '大手': 10555, '商社': 10556, '勝ち取っ': 10557, 'キャリア': 10558, '相談': 10559, '名乗る': 10560, 'か賞': 10561, '痛々しい': 10562, '移せる': 10563, 'きれいな': 10564, 'ひとつ': 10565, '怠っ': 10566, '酔っ': 10567, '定め': 10568, 'おいしく': 10569, 'コオロギ': 10570, 'これはいい': 10571, 'イスラム教徒': 10572, '豚骨ラーメン': 10573, '食べよ': 10574, '独りよがり': 10575, '説得': 10576, '地震': 10577, 'ぼっち': 10578, '誘え': 10579, 'tweet': 10580, 'chipshajen': 10581, '振る舞い': 10582, 'ムードメーカー': 10583, 'nTaimou': 10584, 'has': 10585, 'Talespin': 10586, 'すばらしかっ': 10587, '彼ら': 10588, 'ネクラサポート': 10589, 'ヒーローオブザストーム': 10590, 'すごかっ': 10591, 'bf': 10592, 'ナ': 10593, '通せる': 10594, 'conbox': 10595, '紛らわしく': 10596, '名乗れ': 10597, 'ナゾ': 10598, '重力': 10599, 'ニュースサイト': 10600, 'メタレポートパク': 10601, 'FPSwatch': 10602, 'お気に入り': 10603, 'らいし': 10604, '復習': 10605, '消去': 10606, 'おもち': 10607, 'ゃなんなん': 10608, 'うごき': 10609, 'IGL': 10610, '未熟': 10611, 'みっちり': 10612, 'いいだせん': 10613, '糧': 10614, '雑音': 10615, 'nGLvsNP': 10616, 'リアクション': 10617, 'デス': 10618, '無くなる': 10619, 'イラ': 10620, 'ナノブソルジャー': 10621, 'ULT': 10622, '必中': 10623, 'ランクマ': 10624, '舛添': 10625, 'トランプ': 10626, '政治資金': 10627, '私用': 10628, '着服': 10629, '移民': 10630, '現地': 10631, 'オーダー': 10632, '民意': 10633, '汲み取っ': 10634, '大統領': 10635, '誕生': 10636, '専門職': 10637, 'ビザ': 10638, 'れん': 10639, 'いたか': 10640, 'さい人': 10641, 'ありがち': 10642, '経路': 10643, '探索': 10644, 'ワープ': 10645, 'アース': 10646, '戻そ': 10647, 'ルビコン': 10648, 'ロシア': 10649, '各個': 10650, '分離': 10651, '各個撃破': 10652, 'クソベイブレードメタ': 10653, 'テストプレイ': 10654, 'やばし': 10655, '孫子': 10656, '兵法': 10657, '呟こ': 10658, '呟か': 10659, 'ある時': 10660, '考察': 10661, '助ける': 10662, 'マル': 10663, 'ボウ': 10664, 'たまらな': 10665, 'BF': 10666, 'プレーヤー': 10667, 'だしね': 10668, 'メンヘラタイム': 10669, '予期': 10670, 'エラー': 10671, 'surefour': 10672, '受け流す': 10673, '歩い': 10674, 'オクフェス': 10675, '壊滅': 10676, '悦び': 10677, 'なさい': 10678, 'rogue': 10679, 'ルナティック': 10680, 'ぼこっ': 10681, 'KOKR': 10682, 'ザリアファラ': 10683, 'よすぎ': 10684, 'Shift': 10685, 'Ctrl': 10686, 'ちゃお': 10687, 'ヤニ': 10688, '泣く泣く': 10689, '田端': 10690, '扇動': 10691, '不満': 10692, '抱える': 10693, '代弁': 10694, '行え': 10695, '種': 10696, '豚肉': 10697, '美味し': 10698, '力説': 10699, '儲かり': 10700, '費用': 10701, '物販': 10702, 'ステークス': 10703, 'ホルダー': 10704, 'む人': 10705, 'ウメハラ': 10706, '意志力': 10707, 'ルフス': 10708, '池袋': 10709, '快適': 10710, 'はやい': 10711, 'gpro': 10712, 'デラックス': 10713, 'レーサー': 10714, '根源': 10715, '末端': 10716, 'ぜんぜん': 10717, 'Rogue': 10718, 'にぼ': 10719, '短期間': 10720, '今期': 10721, '行かん': 10722, 'ボルスカ': 10723, 'ぴっく': 10724, '見ろ': 10725, '点数': 10726, '定期テスト': 10727, '受かる': 10728, 'detonation': 10729, 'ダステル': 10730, 'yutapon': 10731, '逸材': 10732, 'ban': 10733, 'クレカ': 10734, 'ポイントゲット': 10735, 'dex': 10736, '区': 10737, '切りつけ': 10738, '三月': 10739, '出会う': 10740, '話せる': 10741, '平然': 10742, '年上': 10743, '苦痛': 10744, 'うんざり': 10745, 'はしゃぐ': 10746, 'センチ': 10747, 'かならず': 10748, 'おなじ': 10749, '測っ': 10750, 'テラ': 10751, 'ココ': 10752, '遭遇': 10753, 'チートトレーサー': 10754, 'ようするに': 10755, '見方': 10756, '世界大会': 10757, 'ええええええ': 10758, '手すり': 10759, '平行': 10760, '小藪': 10761, 'arhan': 10762, '並': 10763, 'チームキル': 10764, 'スカッとする': 10765, 'き服': 10766, 'スタークラフト': 10767, '段違い': 10768, '複数回': 10769, 'トネ': 10770, '仲間割れ': 10771, 'Arhan': 10772, 'PROBASTION': 10773, 'ダウン': 10774, 'クリオフリーズ': 10775, 'noob': 10776, 'Detonator': 10777, 'nDetonator': 10778, 'nUSG': 10779, '最下位': 10780, 'snake': 10781, 'MiG': 10782, 'NGA': 10783, 'VG': 10784, 'Seagull': 10785, 'しかして': 10786, 'NRGvsUSG': 10787, 'apac': 10788, 'とても': 10789, '欧米': 10790, '鼻息': 10791, 'おすぎ': 10792, '大人しく': 10793, 'スピブバリアベイブレード': 10794, 'P': 10795, 'sup': 10796, '0t': 10797, 'ank': 10798, 'デフォ': 10799, 'ＮＡ': 10800, 'ロ上': 10801, 'やかましい': 10802, 'ミュート': 10803, 'ブロックミュート': 10804, '聞こえる': 10805, 'nfps': 10806, 'ザリアｳﾙﾄ': 10807, 'サウンドカード': 10808, '指向性': 10809, '解像度': 10810, '換装': 10811, 'misfits': 10812, 'ミスフィッツ': 10813, 'ゼニルシオ': 10814, '始まり': 10815, '二日酔い': 10816, '推定': 10817, 'arcarade': 10818, 'まけ': 10819, 'くやしい': 10820, 'Dignitous': 10821, 'きた上': 10822, '光る': 10823, 'ベイブレード': 10824, 'お腹': 10825, 'すい': 10826, 'ライフ': 10827, '振り回す': 10828, '大雨洪水警報': 10829, 'ovy': 10830, 'game': 10831, '水洗い': 10832, 'みつかる': 10833, 'sh': 10834, 'add': 10835, 'er0': 10836, 'kさん': 10837, 'ノ': 10838, 'c': 10839, 'ナノブロッサム': 10840, '対戦相手': 10841, 'ペーパーマン': 10842, '五分': 10843, 'テンキーレスキーボード': 10844, '君の名は': 10845, 'ロナウジーニョ': 10846, '片目': 10847, 'プーさん': 10848, 'ホームラン競争': 10849, '目星': 10850, '台本': 10851, 'かおる': 10852, '禿げ': 10853, '愛さ': 10854, '民度': 10855, 'アイスウォール': 10856, 'T': 10857, '字': 10858, '下ろし': 10859, 'sucked': 10860, 'grammer': 10861, 'unleashed': 10862, 'LAN': 10863, 'パーティ': 10864, '主催': 10865, 'はやば': 10866, 'オブジェクト指向': 10867, '仕上げ': 10868, '串刺し': 10869, '遅れる': 10870, '向上心': 10871, 'KILL': 10872, 'DEATH': 10873, 'いたい': 10874, '迫っ': 10875, '遅い': 10876, 'onfire': 10877, 'おしえ': 10878, 'ディレクター': 10879, 'もっとも': 10880, '受け取ら': 10881, '終盤': 10882, '誰々': 10883, 'ヌーブ': 10884, '口論': 10885, '顧み': 10886, 'ブッ': 10887, 'なすりつけ': 10888, 'ワンセット': 10889, 'コミニケーション': 10890, 'とれん': 10891, '賞賛': 10892, '少ないっ': 10893, '選手権': 10894, '義務教育': 10895, 'みりゃ': 10896, '資本集約': 10897, '型': 10898, 'リターン': 10899, '球場前': 10900, '募金': 10901, '根付き': 10902, 'ベット': 10903, '施設': 10904, '一戦': 10905, 'フレンチ': 10906, 'キーン': 10907, 'ばらまい': 10908, '対応力': 10909, '汎用性': 10910, 'PTER': 10911, 'アナウルト': 10912, '攻撃手段': 10913, 'はげ': 10914, 'スペシャルフォース': 10915, '甲斐': 10916, '味わい': 10917, 'クイマ': 10918, 'あさって': 10919, '遊べる': 10920, '統制': 10921, '白猫テニス': 10922, '定型': 10923, 'fuck': 10924, 'you': 10925, '0パーセント': 10926, '凄': 10927, 'ブレスオブファイア': 10928, '爆死': 10929, 'ブレス': 10930, 'まて': 10931, 'we': 10932, '今夜': 10933, 'KUN': 10934, 'MENDOKUSAI': 10935, '進学': 10936, '年間': 10937, '延ばす': 10938, 'カタン': 10939, 'taitanfall': 10940, '夏休み': 10941, '本気出す': 10942, 'オバウォ': 10943, 'それでは': 10944, 'ばらし': 10945, '戦線': 10946, '具合': 10947, 'がとう': 10948, '放り出し': 10949, '心頭': 10950, '滅却': 10951, '0点': 10952, 'うれしー': 10953, 'wｗ': 10954, 'ある意味': 10955, '退路': 10956, '塞が': 10957, '以来': 10958, 'デスブロッサム': 10959, '塞ぐ': 10960, '意外': 10961, '気付か': 10962, '微分方程式': 10963, '解く': 10964, 'MiGArhan': 10965, '見慣れ': 10966, '示せ': 10967, '囲う': 10968, 'もてない男': 10969, '付き合える': 10970, '捧げ': 10971, '教': 10972, '最後の手段': 10973, '唯一無二': 10974, '救い': 10975, '承認欲求': 10976, 'ファイナルブロー': 10977, '強力': 10978, '社畜': 10979, 'アンチヒーロー': 10980, 'やまじ': 10981, 'コンカッシブ': 10982, 'ラッシュ': 10983, 'ハンパない': 10984, 'ルシオマーシー': 10985, 'スピードブースト': 10986, '落ち込ん': 10987, '沈む': 10988, '単発': 10989, 'ぎや': 10990, 'ガチ勢': 10991, 'YAMATON': 10992, '師匠': 10993, '罵っ': 10994, '役職': 10995, '負': 10996, '誘わ': 10997, '実名': 10998, 'ID': 10999, 'ゴールデン': 11000, '血圧': 11001, 'バスティ': 11002, '不安感': 11003, '逆転負け': 11004, 'すり減らす': 11005, '仮定': 11006, '遠回り': 11007, 'いつの間にか': 11008, '適し': 11009, '自然に': 11010, '決めつけ': 11011, 'もしか': 11012, '伸び悩ん': 11013, 'nGL': 11014, 'yamaton': 11015, 'mercy': 11016, 'GLvsDTN': 11017, 'ぽちっ': 11018, 'レ': 11019, '透明': 11020, 'バスティオンピックニキ': 11021, 'steel': 11022, '金メダル': 11023, '無責任': 11024, '冷笑': 11025, '生ま': 11026, '負けれ': 11027, 'おおく': 11028, 'サウンドバリアー': 11029, 'てよ': 11030, '表す': 11031, '浅まし': 11032, 'なぜなら': 11033, '言説': 11034, '今月中': 11035, '闇雲': 11036, 'ないと': 11037, 'はう': 11038, 'ざいし': 11039, '送り出せる': 11040, 'ワールドクラス': 11041, '別物': 11042, 'bastion': 11043, 'ゲーミングヘッドホン': 11044, '買': 11045, 'わな': 11046, '軽さ': 11047, '人ち': 11048, 'ょいちょいいいこと': 11049, 'パン': 11050, 'ありえる': 11051, 'めくれ': 11052, '集まら': 11053, '諦めよ': 11054, '内の人': 11055, '借金': 11056, '一杯': 11057, 'LINE': 11058, 'Slack': 11059, 'ことなる': 11060, 'We': 11061, 'League': 11062, 'Rhe': 11063, 'end': 11064, 'I': 11065, 'hate': 11066, '悲し': 11067, 'いっか': 11068, 'つご': 11069, 'Lets': 11070, 'go': 11071, 'dude': 11072, '来季': 11073, 'ゲシュタルト崩壊': 11074, '呼吸': 11075, '攻めよ': 11076, 'やれよ': 11077, '敗北': 11078, '浮かぶ': 11079, 'fucking': 11080, 'idiot': 11081, 'inside': 11082, 'point': 11083, 'きかさ': 11084, '荒ん': 11085, 'サドンデスルールクソ': 11086, '世界ランク': 11087, 'うろうろ': 11088, '抜け出し': 11089, '追い込ま': 11090, '地雷': 11091, '粘る': 11092, 'アドレナリン': 11093, 'どばどば': 11094, '一体感': 11095, '試合終了後': 11096, '試合終了': 11097, '陣取り': 11098, 'ダンス': 11099, '☺': 11100, 'キャッチコピー': 11101, '救う': 11102, '関': 11103, 'overbuff': 11104, 'nStylishNoob': 11105, 'Genji': 11106, '設置': 11107, '麻雀': 11108, '約束': 11109, 'ポシャっ': 11110, 'オバ': 11111, 'もて': 11112, '男女': 11113, '工学部': 11114, 'お姫様': 11115, 'うし': 11116, 'offense': 11117, 'しいか': 11118, '前線': 11119, 'nK': 11120, '副産物': 11121, 'さいは': 11122, 'lv': 11123, 'いみな': 11124, '扉': 11125, '開けれ': 11126, 'nsanma': 11127, 'どうぞ': 11128, '幸い': 11129, '渡部陽一': 11130, '教典': 11131, 'StylishNoob': 11132, 'SPYGEA': 11133, '超す': 11134, '羽生': 11135, 'をん': 11136, '対戦中': 11137, '日曜日': 11138, 'アプライド': 11139, 'お先真っ暗': 11140, '続けれ': 11141, 'nスタ': 11142, 'ヌー': 11143, 'ボイチャ': 11144, 'トレイラー': 11145, 'nDRAGONS': 11146, 'しびれ': 11147, 'くださる': 11148, 'いたし': 11149, 'ボッチプレイ': 11150, 'グーシェ': 11151, '抜群': 11152, 'KYB': 11153, '弊社': 11154, '費用対効果': 11155, '顧客層': 11156, 'オウンドメディア': 11157, '押し付けがましい': 11158, 'WinWin': 11159, 'ハロウィン': 11160, '暴動': 11161, 'メールアドレス': 11162, 'ふくざつ': 11163, 'ストロングスタイル': 11164, '盛る': 11165, '盛ら': 11166, 'もったいないっ': 11167, '運用方法': 11168, 'CEO': 11169, 'キーノート': 11170, 'プリインストール': 11171, 'デー': 11172, '推進': 11173, '成功事例': 11174, '順張り': 11175, 'マンガワン': 11176, '血と灰の女王': 11177, 'グイグイ': 11178, 'バイトリーダー': 11179, '怒号': 11180, '券売機': 11181, '世界最高': 11182, '将来的': 11183, '資産': 11184, '日本社会': 11185, '機運': 11186, '目玉': 11187, '飛び出': 11188, '人脈': 11189, 'カンファレンス': 11190, '訴える': 11191, '訴えよ': 11192, 'IP': 11193, '相場': 11194, '濃密': 11195, '近日中': 11196, 'アフィ': 11197, 'カリスマ性': 11198, '取り組む': 11199, 'はげませる': 11200, '真摯': 11201, '効い': 11202, '息苦しく': 11203, 'CtoC': 11204, '東大卒': 11205, 'てわけ': 11206, 'たどり着い': 11207, 'Fortnite': 11208, 'docs': 11209, '様々': 11210, '日光': 11211, '山登り': 11212, '焼き鳥': 11213, '女': 11214, 'ステータス': 11215, '唾液': 11216, 'tokyo': 11217, 'mk0': 11218, 'ハウツー': 11219, '事業家': 11220, '孫正義': 11221, '志': 11222, '名著': 11223, 'やらさ': 11224, '説教': 11225, '家庭': 11226, '刷り込ま': 11227, '公立': 11228, 'ぶち込ま': 11229, 'お母さん': 11230, '閉じ': 11231, '緩く': 11232, 'らい': 11233, '担保': 11234, '網': 11235, '0年後': 11236, '母数': 11237, '御茶ノ水': 11238, '喧騒': 11239, '町': 11240, '過ごし': 11241, '昼飯': 11242, 'イノシシ': 11243, '思い出': 11244, '賭博': 11245, '探せる': 11246, 'レキボ': 11247, 'つぶし': 11248, 'イニシエート': 11249, 'くえー': 11250, 'ニコ': 11251, '手綱': 11252, 'ルシモイラブリ': 11253, 'ルシゼニブリ': 11254, 'コンプ': 11255, 'tgs': 11256, 'イクイク': 11257, '甘く': 11258, '漠然と': 11259, '都会': 11260, '市場経済': 11261, '払お': 11262, 'お門違い': 11263, '漠然': 11264, '払い': 11265, 'マリファナ': 11266, 'はやり': 11267, '海外事業': 11268, 'まちがっ': 11269, '日本企業': 11270, '起業家精神': 11271, '権': 11272, '関連企業': 11273, '一社': 11274, 'Startup': 11275, 'こんなん': 11276, 'チャットサポート': 11277, '人員': 11278, '解約': 11279, '阻止': 11280, 'ワードプレス': 11281, 'らしかっ': 11282, 'ポルトガル語': 11283, 'ばっちり': 11284, '売り切り': 11285, 'パッケージ': 11286, 'KPI': 11287, 'nWordPress': 11288, '二番煎じ': 11289, '人種': 11290, '国籍': 11291, '代金': 11292, '億': 11293, '妥当': 11294, 'ツイッチユーザー': 11295, 'Mixer': 11296, 'ビットレート': 11297, 'チアー': 11298, '払出': 11299, '認証': 11300, 'プロセス': 11301, '名刺': 11302, '印': 11303, '理': 11304, '憧れる': 11305, 'あこがれる': 11306, '何と': 11307, '絡める': 11308, '公的資金': 11309, 'バリュー': 11310, '貪欲': 11311, 'ロールモデル': 11312, '湧き出る': 11313, 'アイデンテティ': 11314, '崩れ': 11315, '銀行口座': 11316, 'ロック': 11317, 'すかし': 11318, 'キャッシング': 11319, '残金': 11320, '消費者金融': 11321, '結成': 11322, 'おもしろい': 11323, 'すりゃ': 11324, '法規制': 11325, '激しいっ': 11326, 'ゲーミングチーム': 11327, '貸して': 11328, '支給': 11329, 'フォトナチーム': 11330, '作れん': 11331, '考えなおし': 11332, '市場構造': 11333, '取材': 11334, '目立っ': 11335, 'ゲーマーズコーチ': 11336, 'ゲーマーコーチーズ': 11337, 'ゲーミングコーチ': 11338, 'あよかった': 11339, 'クレジットカード': 11340, '事業者': 11341, '雇え': 11342, 'nyoutuber': 11343, '属人': 11344, 'nnote': 11345, 'PRTIMES': 11346, '並み': 11347, '対外': 11348, 'PRtimes': 11349, 'ドキッ': 11350, 'バンキング': 11351, '送金': 11352, 'ガード': 11353, '固': 11354, 'nGpro': 11355, 'WL': 11356, 'いかんせん': 11357, 'ロジ': 11358, 'G0': 11359, 'えと': 11360, '重量': 11361, '形状': 11362, '失う': 11363, '現代': 11364, '背い': 11365, '単価': 11366, '密度': 11367, '増やせる': 11368, '誕生日': 11369, '習い事': 11370, '異': 11371, '即効': 11372, 'サム': 11373, 'a0': 11374, 'yo': 11375, 'グーグルアドセンス': 11376, '入れれ': 11377, 'しめ': 11378, 'Gamewith': 11379, 'eqo': 11380, 'DEP': 11381, 'フランチャイズ': 11382, 'AMEKEN': 11383, 'やり合っ': 11384, 'タイヨー': 11385, 'デップ': 11386, 'フォトナコーチ': 11387, 'いつ文': 11388, 'かど': 11389, 'うかっ': 11390, 'ポテンシャル': 11391, '対外試合': 11392, '合わせれ': 11393, 'ミシュランガイド': 11394, '祝': 11395, 'フォトナコーチング': 11396, '教わる': 11397, 'たぶん': 11398, '積める': 11399, '初回': 11400, 'セール': 11401, '急ぎ': 11402, 'フルタイムゲーマーコーチ': 11403, 'nLOL': 11404, 'ndata': 11405, '開講': 11406, '積ん': 11407, 'くれれ': 11408, '見込み': 11409, 'RAGE': 11410, '率い': 11411, 'ホリエモン': 11412, '0億': 11413, '仕事術': 11414, '不備': 11415, '色あせ': 11416, '模索': 11417, '親会社': 11418, 'no': 11419, 'anoa': 11420, 'marubou': 11421, 'まるまる': 11422, 'リスカ': 11423, '固定': 11424, '灯': 11425, '資本金': 11426, '増資': 11427, '繰り越し': 11428, '入金': 11429, '法務局': 11430, '拒否': 11431, 'おか': 11432, '入り乱れ': 11433, '興味本位': 11434, 'した先': 11435, 'TCG': 11436, 'OPENREC': 11437, '案の定': 11438, 'いと': 11439, '優良': 11440, '乞う': 11441, '頼める': 11442, '偉く': 11443, 'ドライ': 11444, 'タイム': 11445, '部類': 11446, '当面': 11447, '取り扱っ': 11448, '営利': 11449, 'Hearthstone': 11450, '記載': 11451, '青森': 11452, '山奥': 11453, 'シェアハウス': 11454, '極貧': 11455, '結ぶ': 11456, 'マンパワー': 11457, 'フィンテック': 11458, '潰れ': 11459, '神か': 11460, '著作権': 11461, 'クソツイート': 11462, '話して': 11463, '選挙': 11464, '票': 11465, '訴求': 11466, '候補者': 11467, '得票': 11468, '若者': 11469, '歩み寄る': 11470, '脚': 11471, 'youtuber': 11472, 'DJ社長': 11473, 'アップロード': 11474, '仕上げる': 11475, 'メインロール': 11476, 'ロールキュー': 11477, '使い勝手': 11478, 'りどう': 11479, '開放': 11480, 'コーチングチケット': 11481, '安いっ': 11482, '上限': 11483, '巻き上げ': 11484, '共通点': 11485, '揶揄': 11486, '取り込める': 11487, '膨らま': 11488, '本格': 11489, '比べ物': 11490, 'nGamerCoach': 11491, 'ロッテリア': 11492, 'メニュー': 11493, '旨辛': 11494, 'チーズ': 11495, 'マトン': 11496, 'インド': 11497, 'ハンバーガー': 11498, '新感覚': 11499, 'ならい': 11500, 'けそう': 11501, '管理費': 11502, '転載': 11503, '病院': 11504, '混雑': 11505, '医師': 11506, '免許': 11507, '寡占': 11508, '市場原理': 11509, '被る': 11510, '利用者': 11511, '立たさ': 11512, 'スカイプミーティグ': 11513, 'サイゲ': 11514, 'パパ活': 11515, 'アップテンポ': 11516, '曲': 11517, '聴い': 11518, 'Oneroom': 11519, 'calc': 11520, 'scene': 11521, '不在': 11522, '迎え': 11523, '旧態依然': 11524, 'つこ': 11525, 'チャリスパ': 11526, '国際化': 11527, 'おしよせ': 11528, 'ノイアー': 11529, '盗作': 11530, '筑豊': 11531, '同感': 11532, 'シリーズ': 11533, '無料通話': 11534, 'はやら': 11535, '請求書': 11536, '御中': 11537, 'Newspicks': 11538, '女子': 11539, 'ベルギー': 11540, 'Mbappe': 11541, '下限': 11542, 'プロフェッショナル': 11543, '価格設定': 11544, 'いかが': 11545, 'ばらつき': 11546, '均一': 11547, '偏っ': 11548, '引き上げ': 11549, '任せる': 11550, 'ゴール前': 11551, 'つぶす': 11552, '宇佐美': 11553, '武藤': 11554, '得点': 11555, 'コートジボワール': 11556, 'リード': 11557, '倒れ': 11558, '勝てば官軍': 11559, 'ニコニコ': 11560, '川島': 11561, 'がんばれ': 11562, '投資家': 11563, '登録免許税': 11564, 'フランク': 11565, '堅苦しい': 11566, '堅苦し': 11567, '取り除い': 11568, '版権': 11569, 'Helck': 11570, '技能': 11571, '料金': 11572, 'ダンピング': 11573, '岡崎': 11574, '本田': 11575, '懐かしさ': 11576, '柴崎': 11577, '空手': 11578, 'お見舞い': 11579, 'ベンホロウィッツ': 11580, 'HARD': 11581, 'THINGS': 11582, '定性的': 11583, '集客': 11584, '持ち込み': 11585, '著作物': 11586, 'Gmail': 11587, '迷惑メール': 11588, 'ヤフーメール': 11589, 'メーラー': 11590, '頂き': 11591, '引っ張ろ': 11592, '一件': 11593, '限っ': 11594, '鬼の首を取ったよう': 11595, '石': 11596, '言動': 11597, 'プレスリリース': 11598, 'プレス': 11599, '悩ん': 11600, '判ら': 11601, 'Creative': 11602, 'いじる': 11603, 'HyperX': 11604, '消費者': 11605, 'だまし': 11606, '改良': 11607, '見せかけ': 11608, 'いじくり': 11609, 'KP': 11610, '中盤': 11611, '戦闘': 11612, '練習場': 11613, '炎上商法': 11614, 'アート': 11615, 'ePS': 11616, '多数決': 11617, '加担': 11618, '肯定的': 11619, 'とらえる': 11620, '通販サイト': 11621, '勝機': 11622, '論理的': 11623, 'ネット社会': 11624, '直感': 11625, 'パラメータ': 11626, '凡人': 11627, '乗っけ': 11628, 'リテラシー': 11629, '徒手空拳': 11630, 'nurio': 11631, '\u200d♂': 11632, 'KPM': 11633, '0戦': 11634, 'マレーシア人': 11635, 'LGBT': 11636, '差別的': 11637, '占め': 11638, '毒にも薬にもならない': 11639, '取り払い': 11640, '悲しかっ': 11641, 'The': 11642, 'Empire': 11643, 'of': 11644, 'Pike': 11645, '秋刀魚': 11646, 'TEP': 11647, 'Unreal': 11648, 'た事': 11649, 'mercyJPN': 11650, 'ランクマキチガイ': 11651, 'エイムヒーロー': 11652, 'つかみ': 11653, 'ゴイゴイスウ': 11654, 'くっつき': 11655, 'フォトナソロ': 11656, '動悸': 11657, 'Fissure': 11658, 'きっかけ': 11659, '対等': 11660, 'ぽい': 11661, 'がっ': 11662, '待遇': 11663, 'グダグダ': 11664, 'JP': 11665, 'Overwatcjh': 11666, '一蘭': 11667, 'かぶせ': 11668, 'エイマー': 11669, 'アジアスクリム': 11670, 'い方': 11671, '期間限定': 11672, '青じそ': 11673, '精神病院': 11674, '送り込ん': 11675, '伝説': 11676, 'オン': 11677, 'ゆかり': 11678, '毎週': 11679, '俺レベル': 11680, '起こせ': 11681, '社会実験': 11682, '在り方': 11683, '来れる': 11684, '回る': 11685, '開拓': 11686, '憧れ': 11687, 'ゲハ': 11688, '共同生活': 11689, '届ける': 11690, '安全地帯': 11691, 'サイコパス': 11692, 'doneshineshine': 11693, 'nmano': 11694, '商標登録': 11695, 'Trn': 11696, '結婚': 11697, '材': 11698, 'ジェッパ': 11699, '全角': 11700, '英': 11701, 'のっかっ': 11702, 'バーミリオン': 11703, 'イメージ通り': 11704, '果たさ': 11705, '通じ': 11706, 'さわやか': 11707, 'Note': 11708, 'はて': 11709, 'ブ位': 11710, '福岡県民': 11711, '主食': 11712, 'フォトナスク': 11713, '勤め先': 11714, 'ign': 11715, '職場': 11716, 'ルナハイスクリム': 11717, '疲労感': 11718, '倦怠感': 11719, '強制': 11720, 'バクバク': 11721, '居': 11722, '占拠': 11723, '判断ミス': 11724, '命取り': 11725, 'tumblr': 11726, '誘える': 11727, 'おもいつか': 11728, 'かに': 11729, 'watson': 11730, '正規表現': 11731, 'ざっくり': 11732, 'Karabiner': 11733, '度目': 11734, '初期化': 11735, '0年間': 11736, 'いい大学': 11737, 'レール': 11738, '沿っ': 11739, '職業選択': 11740, '組み込ま': 11741, '埋め込ま': 11742, 'ひっくり返せ': 11743, '四隅': 11744, '各所': 11745, '押さえ': 11746, '極性': 11747, '撃退': 11748, 'こだわり': 11749, 'nCSGO': 11750, 'エイムゲー': 11751, 'なおさ': 11752, 'ycs': 11753, '覚醒': 11754, '作用': 11755, '難癖': 11756, '長': 11757, '休暇': 11758, 'ぐっと': 11759, '厚く': 11760, '軽いっ': 11761, '大半': 11762, '弁護士': 11763, '人当り': 11764, 'サービスフォトナ': 11765, '加える': 11766, 'ポンプ': 11767, 'ムーブ': 11768, 'タクティカル': 11769, '女性専用車両': 11770, '車両': 11771, '凍る': 11772, 'ジェットパック': 11773, 't0': 11774, 'T0': 11775, 'ファーム': 11776, 'きょう': 11777, 'totemo': 11778, 'yjouzu': 11779, 'player': 11780, 'ウルトラライトプロ': 11781, 'ボタンバインド': 11782, 'バインド': 11783, '割り当て': 11784, 'CAG': 11785, 'ストリートファイター': 11786, 'epos': 11787, '公証役場': 11788, 'もらわ': 11789, '個人事業主': 11790, '独立採算': 11791, '価格競争': 11792, '定款': 11793, 'ピッ': 11794, '通す': 11795, '役場': 11796, '出向い': 11797, '高給': 11798, 'エリート': 11799, 'shure': 11800, '堀江貴文': 11801, '天国': 11802, 'かかわり': 11803, 'ケンカ': 11804, 'ふっかける': 11805, '操作ミス': 11806, '作業内容': 11807, 'ばくわら': 11808, 'bit': 11809, 'cash': 11810, '出資': 11811, 'es': 11812, 'ports': 11813, '背後': 11814, 'shibuya': 11815, 'gamers': 11816, '卓球部': 11817, '運動部': 11818, '下層': 11819, 'ネタバラシ': 11820, '印鑑': 11821, '印鑑証明': 11822, 'お役所仕事': 11823, '遅らさ': 11824, '憤り': 11825, 'がちがち': 11826, '整体': 11827, '血流': 11828, '寝違え': 11829, 'シャレ': 11830, '痛み': 11831, 'サノス': 11832, 'サノスモード': 11833, '祈る': 11834, 'ソロビクロイ': 11835, 'Kyuhan': 11836, '肩甲骨': 11837, '炎症': 11838, 'せいさ': 11839, 'ち安': 11840, '駐車場': 11841, 'ベンツ': 11842, 'ルナハイキル': 11843, 'nanimo': 11844, '避ける': 11845, 'モスティマイア': 11846, '減': 11847, '直ら': 11848, 'どちゃくそ': 11849, 'タイタンフォール': 11850, '集中砲火': 11851, '山上': 11852, '工場': 11853, '漁夫': 11854, '盤': 11855, '払える': 11856, '常々': 11857, '何らかの': 11858, 'District': 11859, '見栄え': 11860, '転生': 11861, 'ブリギッテ': 11862, '親富': 11863, '孝': 11864, 'ソロスク': 11865, '目指せ': 11866} [tensor(1175), tensor(201)]
1175
<class 'int'>
201
<class 'int'>
[2019-10-08 04:33:18,109] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/dist-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/dist-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/abetter/app.py", line 18, in form
    maked_words = LSTM_model.generate_seq(model, start_phase=field, length=10)
  File "/abetter/LSTM_model.py", line 72, in generate_seq
    res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
  File "/abetter/LSTM_model.py", line 72, in <listcomp>
    res = "".join([index2word[int(i.to("cpu").numpy())] for i in result])
KeyError: 1175
172.17.0.1 - - [08/Oct/2019 04:33:18] "POST / HTTP/1.1" 500 -
^Croot@0ca109d793fb:/abetter# vi LSTM_model.py 
root@0ca109d793fb:/abetter# flask run --host 0.0.0.0
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [08/Oct/2019 04:34:33] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [08/Oct/2019 04:34:35] "POST / HTTP/1.1" 200 -
172.17.0.1 - - [08/Oct/2019 05:07:59] "POST / HTTP/1.1" 200 -
^Croot@0ca109d793fb:/abetter# pwd
/abetter
root@0ca109d793fb:/abetter# ls
Dockerfile  LSTM_model.py  __pycache__  app.py  i2w.pkl  model.pkl  templates  tweet.js  w2i.pkl
root@0ca109d793fb:/abetter# vi LSTM_model.py 

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
  with open("w2i.pkl", "rb")as data:
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
"LSTM_model.py" 70L, 2434C                                                                                                                                                              1,1           Top
