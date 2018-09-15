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


###How our project's structure look like?





