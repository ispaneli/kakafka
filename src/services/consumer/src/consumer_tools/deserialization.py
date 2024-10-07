import io
import os

from fastavro import schemaless_reader
from fastavro.schema import load_schema


AVRO_SCHEMA = load_schema(os.getenv('KAFKA_AVRO_SCHEMA_PATH'))


def avro_deserialization(avro_bytes: bytes) -> dict[str, ...]:
    """
    Deserializes a byte string containing Avro-encoded data into a Python dictionary.

    :param bytes avro_bytes: A byte string containing the Avro-encoded data to be deserialized.
    :return: A dictionary representing the deserialized Avro data,
             following the structure defined in the Avro schema.
    :rtype: dict[str, ...]
    """
    with io.BytesIO(avro_bytes) as avro_io:
        record = schemaless_reader(avro_io, AVRO_SCHEMA)

    return record
