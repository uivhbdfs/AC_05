import pika
import requests
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
chan = connection.channel()

chan.queue_declare(queue='user_fetch')

response = requests.get("https://jsonplaceholder.typicode.com/users")

userlst = response.json()

for user in userlst: 
    chan.basic_publish(exchange='', routing_key='user_fetch', body=json.dumps(user))

print(" [x] Sent 'Users Fetched!'")
connection.close()