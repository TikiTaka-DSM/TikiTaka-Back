import base64
from io import BytesIO


def decode_base64_to_file(file_bytes):
    return BytesIO(base64.b64decode(file_bytes))
