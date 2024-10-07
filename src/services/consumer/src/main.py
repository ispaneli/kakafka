import os
from datetime import datetime

from kafka import KafkaConsumer

from consumer_tools import avro_deserialization


consumer = KafkaConsumer(
    os.getenv('KAFKA_USER_TOPIC'),
    bootstrap_servers=[os.getenv('KAFKA_BOOTSTRAP_SERVERS')],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='user-group',
    value_deserializer=avro_deserialization
)


def main():
    for user_record in consumer:
        user_record.value['date_of_birth'] = datetime.fromtimestamp(
            user_record.value['date_of_birth']
        ).date()

        source = f"'{user_record.topic}':{user_record.partition}"
        dt = datetime.fromtimestamp(user_record.timestamp / 1_000)
        user_data = user_record.value

        print(f">>> New consumed `User` (source={source}; dt={dt}): {user_data}")

if __name__ == "__main__":
    main()
