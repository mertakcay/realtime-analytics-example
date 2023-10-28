from confluent_kafka import Producer
import socket
topic = "examplekafka-stat"

conf = {'bootstrap.servers': 'localhost:9094',
        'client.id': socket.gethostname()}

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

for i in range(100):
    producer.produce(topic, key="key", value=f"{str(i)} - spark", callback=acked)

    # Wait up to 1 second for events. Callbacks will be invoked during
    # this method call if the message is acknowledged.
    producer.poll(1)