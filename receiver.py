import pika

HOST_NAME = "localhost"
QUEUE_NAME = "snowdeer_queue"


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST_NAME))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)
    # 메세지 callback으로 호출

    def callback(ch, method, properties, body):
        print("Message is Arrived %r" % body)

        # basic_consume을 브로커에 보내고 consumer_tag에 대한 메시지를 소비자 콜백에 바인딩
    channel.basic_consume(queue=QUEUE_NAME,
                          on_message_callback=callback,
                          auto_ack=True)

    try:
        print("Waiting for messages.")
        # start_consuming:모든 소비자가 취소될 때까지 I/O 이벤트를 처리하고 타이머와 basic_consume 콜백을 전달
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Ctrl+C is Pressed.')


if __name__ == '__main__':
    main()
