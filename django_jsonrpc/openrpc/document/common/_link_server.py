from typing import Annotated, TypedDict
from pydantic import Field

from django_jsonrpc.openrpc.document._base import OpenRPCModel
from django_jsonrpc.openrpc.document.server import OpenRpcServerObjectVariable


__all__ = [
    "OpenRpcLinkObjectServer",
]


class _OpenRpcLinkObjectServerTD(TypedDict):
    url: str
    name: str | None
    description: str | None
    summary: str | None
    variables: dict[str, OpenRpcServerObjectVariable] | None


class OpenRpcLinkObjectServer(OpenRPCModel):

    """A server object to be used by the target method."""

    url: Annotated[
        str,
        Field(
            description=(
            "REQUIRED. A URL to the target host. This URL supports Server "
            "Variables and MAY be relative, to indicate that the host location "
            "is relative to the location where the OpenRPC document is being "
            "served. Server Variables are passed into the Runtime Expression to "
            "produce a server URL."
            )
        ),
    ]
    name: Annotated[
        str | None,
        Field(
            default=None,
            description=(
            "An optional string describing the name of the server."
            "GitHub Flavored Markdown syntax MAY be used for rich text representation."
            )
        ),
    ] = None
    description: Annotated[
        str | None,
        Field(
            default=None,
            description=(
            "An optional string describing the host designated by the URL."
            "GitHub Flavored Markdown syntax MAY be used for rich text representation."
            )
        ),
    ] = None
    summary: Annotated[
        str | None,
        Field(
            default=None,
            description=(
            "A short summary of what the server is."
            )
        ),
    ] = None
    variables: Annotated[
        dict[str, OpenRpcServerObjectVariable] | None,
        Field(
            default=None,
            description=(
            "A map between a variable name and its value. The value is passed "
            "into the Runtime Expression to produce a server URL."
            )
        ),
    ] = None
