from kafka import KafkaProducer

def on_send_success(record_metadata):
    print('Event sent successfully:')
    print(f'Topic: {record_metadata.topic}')
    print(f'Partition: {record_metadata.partition}')
    print(f'Offset: {record_metadata.offset}')

def on_send_error(ex):
    print(f'Error occurred while sending event: {str(ex)}')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.send('quickstart-events', b'message-from-python').add_callback(on_send_success).add_errback(on_send_error)

for n in range(3):
    message = 'additional message {} from python'.format(n)
    producer.send('quickstart-events', bytearray(message, 'utf-8'))

producer.flush()