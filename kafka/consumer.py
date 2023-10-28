from confluent_kafka import Consumer

conf = {'bootstrap.servers': 'localhost:9094',
        'group.id': 'kafka-stat',
        'auto.offset.reset': 'smallest'}

topics = ['examplekafka-stat']

consumer = Consumer(conf)
running=True
MIN_COMMIT_COUNT = 10
try:
    consumer.subscribe(topics)

    msg_count = 0
    while running:
        msg = consumer.poll(timeout=0.5)
        if msg is None: continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                    (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            print(msg.value())
            msg_count += 1
            if msg_count % MIN_COMMIT_COUNT == 0:
                consumer.commit(asynchronous=True)
finally:
    # Close down consumer to commit final offsets.
    consumer.close()