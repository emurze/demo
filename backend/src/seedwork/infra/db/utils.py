import uuid
from typing import Any


def to_uuid(model_id: Any) -> uuid.UUID:
    return uuid.UUID(str(model_id))
