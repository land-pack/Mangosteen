# Mangosteen
A useful api server, which basic on flask、rabbitmq、docker、nginx、gunicorn、fabric、centos、supervisor


As we all know after build a application, we need to deploy it, but as we work at a team, which means we have to share our code and we also need to deploy it on different enviroment. 

Typical, we do it with following steps.

* 1.Coding
* 2.Prepare enviroment
* 3.Deploy
* 4.Run
* 5.Repeat
* 6.Check logs
* 7.Monitor

So, It's complex, right? we just need to focus one thing would be better. for example.

	fab -f fabfile/online_conf.py deploy

And if you want to check whether a cache still available. just do it

	fab -f fabfile/online_conf.py redis-cli get ttl my_cache

### Build your project in docker
Before you do that you should configure your env and your docker's registry.
Also you need to run your remote docker daemon, and a fix-directory in '/data/code'
by default. there are some env you need to configure or you can just simply put it
on your `fabfile.py`.


    fab d_build



###How our project's structure look like?

	.
	├── Dockerfile
	├── demo
	│   ├── app
	│   │   ├── __init__.py
	│   │   ├── __init__.pyc
	│   │   ├── api
	│   │   │   ├── README.md
	│   │   │   ├── __init__.py
	│   │   │   ├── __init__.pyc
	│   │   │   ├── hello.py
	│   │   │   └── hello.pyc
	│   │   ├── cache
	│   │   ├── core
	│   │   │   ├── __init__.py
	│   │   │   ├── __init__.pyc
	│   │   │   ├── color.py
	│   │   │   ├── color.pyc
	│   │   │   ├── event.py
	│   │   │   ├── event.pyc
	│   │   │   ├── log.py
	│   │   │   └── log.pyc
	│   │   ├── events
	│   │   │   ├── __init__.py
	│   │   │   ├── __init__.pyc
	│   │   │   ├── bar.py
	│   │   │   └── bar.pyc
	│   │   ├── jobs
	│   │   │   ├── __init__.py
	│   │   │   ├── __init__.pyc
	│   │   │   ├── foo.py
	│   │   │   └── foo.pyc
	│   │   ├── lib
	│   │   └── utils
	│   ├── config
	│   │   ├── default_log.ini
	│   │   ├── event_log.ini
	│   │   └── job_log.ini
	│   ├── event.py
	│   ├── job.py
	│   ├── manage.py
	│   └── tests
	│       ├── send.py
	│       ├── test_callback.py
	│       └── test_core_event.py
	├── fabfile
	├── logs
	│   ├── default.log
	│   ├── event.log
	│   └── job.log
	└── requirements.txt
