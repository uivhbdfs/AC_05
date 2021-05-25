import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    chan = connection.channel()

    chan.queue_declare(queue='user_fetch')

    def callback(ch, method, properties, body):
        print(" [x] Received %r \n\n\n" % body.decode('utf-8'))

    chan.basic_consume(queue='user_fetch', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    chan.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)