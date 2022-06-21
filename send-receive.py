import sys
import pika
import json
import binascii


HOST_NAME = "localhost"
QUEUE_NAME = "test1"


class RpcServer(object):

    def __init__(self):
        print(" [x] Loading model...")
        # 모듈 적용
        # self.model = self.load_model()
        print(" [x] Model loaded")
        # channel 연결
        # inferrer.init("yolov4-cj-namwon.cfg", "yolov4-cj-namwon_final.weights")
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=HOST_NAME))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='test2')
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            on_message_callback=self.on_request, queue='test1')
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()

    def on_request(self, ch, method, props, body):
        image = json.loads(body)
        #byteimage = image['content']['image'].encode()
        base64string = image['content']['image'][image['content']
                                                 ['image'].find(",") + 1:]
        byteimage = binascii.a2b_base64(base64string)

        # pred = inferrer.infer(byteimage)
        # image['content']['image'] = pred
        # response = image

        ch.basic_publish(exchange='',
                         routing_key="test2",
                         body=image)
        ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    server = RpcServer()
