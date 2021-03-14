# python_redis_demp

The purpose of this demo is to demonstrate how can be used reddis with python
Source: 
* https://developer.redislabs.com/develop/python/
* https://github.com/RedisJSON/redisjson-py

1. pip3 install redis
1. pip freeze > requirements.txt
1. docker run --name my-redis-container -p 6379:6379 -d redis

---

# REDIS JSON

https://oss.redislabs.com/redisjson/#launch-redisjson-with-docker

run docker
  
`docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest`

pip install rejson

