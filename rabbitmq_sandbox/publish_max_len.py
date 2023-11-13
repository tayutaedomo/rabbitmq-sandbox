import os
import argparse
import pika

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')


def send_message(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()

    args = {
        "x-message-ttl" : 5 * 60 * 1000,
        "x-max-length": 2,
        "x-overflow": "reject-publish", # or "drop-head"
    }
    channel.queue_declare(queue=queue_name, arguments=args)

    channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    print(f"Sent: {queue_name}, {message}")

    connection.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a message to RabbitMQ")
    parser.add_argument("message", nargs='?', default="default_message", help="Message to send")
    args = parser.parse_args()

    send_message("max_len", args.message)
