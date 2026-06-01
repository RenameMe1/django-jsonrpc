from typing import Annotated, TypedDict
from pydantic import Field

from django_jsonrpc.openrpc.document._base import OpenRPCModel
from django_jsonrpc.openrpc.document.common._example import OpenRpcExampleObject
from django_jsonrpc.openrpc.document.common._reference import OpenRpcReferenceObject


__all__ = [
    "OpenRpcExamplePairingObject",
]

class _OpenRpcExamplePairingObjectTD(TypedDict, total=False):
    name: str
    description: str | None
    params: list[OpenRpcExampleObject | OpenRpcReferenceObject]
    result: OpenRpcExampleObject | OpenRpcReferenceObject | None


class OpenRpcExamplePairingObject(OpenRPCModel):
    """The Example Pairing object consists of a set of example params and
    result. The result is what you can expect from the JSON-RPC service
    given the exact params.
    """
    name: Annotated[
        str,
        Field(description=("REQUIRED. Name for the example pairing.")),
    ]
    description: Annotated[
        str | None,
        Field(
            default=None,
            description=("A verbose explanation of the example pairing."),
        ),
    ] = None
    params: Annotated[
        list[OpenRpcExampleObject | OpenRpcReferenceObject],
        Field(
            description=("REQUIRED. Example parameters.")
        ),
    ]
    result: Annotated[
        OpenRpcExampleObject | OpenRpcReferenceObject | None,
        Field(
            default=None,
            description=(
                "Example result. When not provided, the example pairing "
                "represents usage of the method as a notification."
            )
        ),
    ] = None