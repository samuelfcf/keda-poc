import pika


def set_channel_and_queue():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('rabbitmq', port=5672))

    channel = connection.channel()
    channel.queue_declare(queue='test_q')

    return channel
