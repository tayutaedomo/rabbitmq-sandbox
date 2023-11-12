import pika
from unittest.mock import Mock, patch

def send_message(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters("dummy"))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    connection.close()

@patch('pika.BlockingConnection')
def test_send_message(mock_connection):
    mock_channel = Mock()
    mock_connection.return_value.channel.return_value = mock_channel

    send_message("test_queue", "Hello, RabbitMQ!")

    mock_channel.queue_declare.assert_called_once_with(queue="test_queue")
    mock_channel.basic_publish.assert_called_once_with(
        exchange='',
        routing_key='test_queue',
        body='Hello, RabbitMQ!'
    )
