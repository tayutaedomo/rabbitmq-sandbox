import os
import argparse
import pika

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')


def send_message(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()

    # TTL (milliseconds)
    args = {"x-message-ttl" : 2 * 60 * 1000}
    channel.queue_declare(queue=queue_name, arguments=args)

    channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    print(f"Sent: {queue_name}, {message}")

    connection.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a message to RabbitMQ")
    parser.add_argument("message", nargs='?', default="default_message", help="Message to send")
    args = parser.parse_args()

    send_message("auto_act", args.message)
