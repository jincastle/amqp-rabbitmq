from datetime import datetime
import pika

HOST_NAME = "localhost"
QUEUE_NAME = "test1"


def main():
    # BlockingConnection은 예상 응답이 반환될 때까지 차단하는 메서드를 제공하는 Pika의 비동기 코어 위에 레이어를 만듭니다.
    # RabbitMQ에 연결하는 데 필요한 모든 연결 매개변수를 지정하기 위한 클래식 개체
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST_NAME))
    # 채널 연결
    channel = connection.channel()

    # queue_declare 대기열을 선언하고 필요한 경우 생성(대기열을 생성하거나 확인)
    channel.queue_declare(queue=QUEUE_NAME)

    msg = f"[{datetime.now()}] hello, snowdeer !!"
    # basic_publish 정된 교환, 라우팅 키 및 본문을 사용하여 채널에 게시합니다.*****
    # 간단히 말하면 메세지 보내는 코드
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=msg)
    print(f"Sent message.\n{msg}")
    # 연결 끈기
    connection.close()


if __name__ == '__main__':
    main()
