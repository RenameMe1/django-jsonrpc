from typing import Annotated, TypedDict
from pydantic import Field

from django_jsonrpc.openrpc.document._base import OpenRPCModel

__all__ = [
    "OpenRpcReferenceObject",
]


class _OpenRpcReferenceObjectTD(TypedDict):
    ref: str


class OpenRpcReferenceObject(OpenRPCModel):
    ref: Annotated[
        str,
        Field(serialization_alias="$ref"),
        """REQUIRED. The reference string..
        """
    ]