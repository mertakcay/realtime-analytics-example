from confluent_kafka import Producer
import datetime

import socket
import json
import random
import time


topic = "druid_topic"

conf = {'bootstrap.servers': 'localhost:9094',
        'client.id': socket.gethostname()}

currency_list = ["BTC", "ETH", "SOL", "DOGE"]
pair_list = ["USD", "EUR", "BTC", "ETH"]

producer = Producer(conf)


def json_producer_util(message):
    return json.dumps(message).encode('utf-8')


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


for i in range(100):
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_currency_idx = random.randint(0, len(currency_list)-1)
    random_pair_idx = random.randint(0, len(pair_list)-1)
          
    example_data = {"timestamp": time_stamp,
                    "currency": currency_list[random_currency_idx],
                    "pair": pair_list[random_pair_idx],
                    "price": random.random()}
    time.sleep(0.5)
    print(example_data)
    
    producer.produce(topic, key="key", value=json_producer_util(example_data), callback=acked)

    # Wait up to 1 second for events. Callbacks will be invoked during
    # this method call if the message is acknowledged.
    producer.poll(1)
