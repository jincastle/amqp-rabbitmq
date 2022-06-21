# amqp-rabbitmq

<aside>
🐳 Publishe/Subscribe의 핵심은 하나의 메시지를 관심이 있는 여러 개의 Subscriber에게 전달

</aside>

[래퍼런스](https://www.rabbitmq.com/tutorials/tutorial-three-python.html)

## producer는 메세지를 보내는 어플리케이션

- RabbitMQ에서 메시징 모델의 중심생각은 Producer는 결코 어떤 메시지라도 큐에 직접 전송하지 않는다는 것
- Producer는 오직 메시지를 exchange에게 전송할 뿐

## queue는 메시지를 저장하는 buffer

## consumer는 메세지를 받는 사용자 어플리케이션

## exchange

- exchange는 producer로 부터 메시지를 받고, 다른 측면에서 그 메시지를 queue에 건네준다.
- exchange 는 전달받은 메시지를 가지고 무엇을 할지 정확하게 알아야만 한다
- exchange type 종류 : direct, topic, headers, fanout

- Listring exchanges
  서버상에서 exchange들을 리스트업하기 위한 명령어
  ```python
   rabbitmqctl list_exchanges
  ```
- Nameless exchange
  channel.basicPublish(””, “hello”, null, message.getBytes()); // 첫번째 파라미터가 exchange 이름 이다

## Temporary queues

큐가 이름을 갖는 것은 아주 중요한데, 작업자에게 동일한 큐를 지정해야 하기 때문에

하지만 로거의 경우에는 그렇지 않다. 우리 로거의 부분이 아닌 모든 메세지를 듣기 원하지, 단지 메시지들의 교집합만 원하는게 아니다 우리는 또한 오래된 로그가 아닌 현재 나오고 있는 로그에 관심이 있다.

- 먼저 rabbit에 연결할 때 마다 새로운 빈큐가 필요
- 두번째로 consumer의 연결을 종료하면 큐는 자동적으로 삭제되어야 한다

## **Bindings**

이미 fanout exchange와 큐를 생성

큐에서 메세지들을 전달할려면 exchange에게 지시를 해야한다

큐와 exchange의 관계를 binding이다

- 사용하고 있는 바인딩 리스트를 보려면
  ```python
  rabbitmqctl list_bindings
  ```

## Putting it all together

이름없는 exchange 대신에 우리 logs exchange에 메시지들을 게시하는 것

발송할때, routingkey를 적용할 필요가 있지만 fanout exchange인 경우에는 무시해도 된다.
