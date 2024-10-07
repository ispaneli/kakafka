import os
import io

from fastavro import schemaless_writer
from fastavro.schema import load_schema


AVRO_SCHEMA = load_schema(os.getenv('KAFKA_AVRO_SCHEMA_PATH'))


def avro_serialization(data: dict[str, ...]) -> bytes:
    """
    Serializes a given dictionary of data into Avro binary format using a predefined schema.

    :param dict[str, ...] data: A dictionary containing the data to be serialized.
                                The structure of the dictionary should match the predefined Avro schema.
    :return: A byte string containing the Avro-encoded data.
    :rtype: bytes
    """
    avro_bytes = io.BytesIO()
    schemaless_writer(avro_bytes, AVRO_SCHEMA, data)

    return avro_bytes.getvalue()
