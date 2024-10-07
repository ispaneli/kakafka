import os
import logging
from random import random
from time import sleep

from kafka import KafkaProducer

from producer_tools import (
    avro_serialization,
    user_generator
)


logger = logging.getLogger(__name__)
USER_TOPIC = os.getenv('KAFKA_USER_TOPIC')
producer = KafkaProducer(
    bootstrap_servers=[os.getenv('KAFKA_BOOTSTRAP_SERVERS')],
    value_serializer=avro_serialization
)


def main():
    try:
        for user_data in user_generator():
            producer.send(USER_TOPIC, user_data)
            producer.flush()

            sleep(random())

    except Exception as e:
        logger.exception(e)
        producer.close()


if __name__ == "__main__":
    main()
