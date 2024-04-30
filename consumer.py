import threading
import time

from app import set_channel_and_queue


def process_message(body):
    print(f"Processando mensagem: {body}")
    time.sleep(10)
    print("Mensagem processada com sucesso!")


def my_callback(ch, method, properties, body):
    threading.Thread(target=process_message,
                     args=(body.decode('utf-8'),)).start()


def consumer(batch_size=2):
    channel = set_channel_and_queue()
    channel.basic_qos(prefetch_count=batch_size)
    while True:
        method_frame, header_frame, body = channel.basic_get(queue='test_q',
                                                             auto_ack=True)
        print("method_frame", method_frame)
        if method_frame:
            my_callback(None, method_frame, None, body)
        else:
            time.sleep(1)


if __name__ == '__main__':
    consumer()
