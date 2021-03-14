import redis
import json

redis = redis.Redis( host= 'localhost', port= '6379')

redis.set('mykey', 'Hello from Python!')
value = redis.get('mykey')
print(value)

redis.zadd('vehicles', {'car' : 0})
redis.zadd('vehicles', {'bike' : 0})
vehicles = redis.zrange('vehicles', 0, -1)
print(vehicles)

# Work with djson

data = {
    'foo': 'bar'
}

r = redis.StrictRedis()
r.execute_command('JSON.SET', 'doc', '.', json.dumps(data))
reply = json.loads(r.execute_command('JSON.GET', 'doc'))
print(reply)