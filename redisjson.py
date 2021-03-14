from rejson import Client, Path


redis_json_client = Client(host='localhost', port=6379, decode_responses=True)

# Set the key `obj` to some object
json_sample = {
   'answer': 42,
   'arr': [None, True, 3.14],
   'truth': {
       'coord': 'out there'}
}

redis_json_client.jsonset('obj', Path.rootPath(), json_sample)

# Get something
print ('Is there anybody... {}?'.format(redis_json_client.jsonget('obj', Path('.truth.coord'))))

# Delete something (or perhaps nothing), append something and pop it
redis_json_client.jsondel('obj', Path('.arr[0]'))
redis_json_client.jsonarrappend('obj', Path('.arr'), 'something')
print('{} popped!'.format(redis_json_client.jsonarrpop('obj', Path('.arr'))))

# Update something else
redis_json_client.jsonset('obj', Path('.answer'), 2.17)

# And use just like the regular redis-py client
jp = redis_json_client.pipeline()
jp.set('foo', 'bar')
jp.jsonset('baz', Path.rootPath(), 'qaz')
jp.execute()

# If you use non-ascii character in your JSON data, you can add the no_escape flag to JSON.GET command
obj_non_ascii = {
 'non_ascii_string': 'hyvää'
}
redis_json_client.jsonset('non-ascii', Path.rootPath(), obj_non_ascii)
print ('{} is a non-ascii string'.format(redis_json_client.jsonget('non-ascii', Path('.non_ascii_string'), no_escape=True)))