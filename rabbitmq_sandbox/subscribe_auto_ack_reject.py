import os
import datetime
import pika

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')
MAX_RETRIES = 3

def callback(ch, method, properties, body):
    try:
        message = body.decode()

        print(f"{datetime.datetime.now()}, Received {message}")

        if message == "raise_error":
            raise Exception("Manually raised exception!")

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Error: {e}")

        print (f"properties: {properties}")
        print (f"properties.headers: {properties.headers}")
        headers = properties.headers or {}
        retry_count = headers.get('x-retry-count', 0) + 1
        print(f"Retry count: {retry_count}")

        if retry_count > MAX_RETRIES:
            print(f"Max retries exceeded for message: {body}")
            ch.basic_ack(delivery_tag=method.delivery_tag)
            return

        # Requeue
        headers = properties.headers or {}
        headers['x-retry-count'] = retry_count
        properties = pika.BasicProperties(headers=headers)
        ch.basic_publish(exchange='', routing_key=method.routing_key, properties=properties, body=body)
        ch.basic_reject(delivery_tag=method.delivery_tag, requeue=False)


def subscribe(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()

    # TTL (milliseconds)
    args = {"x-message-ttl" : 2 * 60 * 1000}
    channel.queue_declare(queue=queue_name, arguments=args)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

    print('Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()


if __name__ == "__main__":
    subscribe("auto_ack")
