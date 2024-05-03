import pika


def set_queue():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('rabbitmq', port=5672))

    channel = connection.channel()
    channel.exchange_declare(exchange='exchange',
                             exchange_type='fanout')
    channel.queue_declare(queue='queue')
    channel.queue_bind(exchange='exchange',
                       queue='queue',
                       routing_key='tasks')

    return channel
