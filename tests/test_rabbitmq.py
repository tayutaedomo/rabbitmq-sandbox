import os
import pika
import pytest

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')


@pytest.fixture(scope="function")
def test_queue():
    queue_name = "test_queue"
    yield queue_name

    # Cleanup
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_delete(queue=queue_name)
    connection.close()

def send_message(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    connection.close()

def receive_message(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
    connection.close()
    return body

def test_message_send_receive(test_queue):
    test_message = "Hello, RabbitMQ!"
    send_message(test_queue, test_message)
    received_message = receive_message(test_queue)
    assert received_message.decode() == test_message
