from typing import Annotated, TypedDict
from pydantic import Field

from django_jsonrpc.openrpc.document._base import OpenRPCModel

__all__ = [
    "OpenRpcReferenceObject",
]


_OpenRpcReferenceObjectTD = TypedDict(
    "_OpenRpcReferenceObjectTD",
    {
        "$ref": str,
    },
    total=False,
)


class OpenRpcReferenceObject(OpenRPCModel):
    ref: Annotated[
        str,
        Field(serialization_alias="$ref"),
        """REQUIRED. The reference string..
        """
    ]