import time
from setup_consumer import set_queue


def my_callback(channel, method, properties, body):
    print(f"Processando mensagem: {body}")
    time.sleep(5)
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print(f"Mensagem {body} processada com sucesso!")


def consumer():
    channel = set_queue()
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='queue',
                          on_message_callback=my_callback,
                          auto_ack=False)
    print('Esperando por mensagens. Pressione CTRL+C para sair.')
    channel.start_consuming()


if __name__ == '__main__':
    consumer()
