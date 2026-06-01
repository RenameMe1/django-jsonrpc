from typing import Annotated, TypedDict
from pydantic import Field

from django_jsonrpc.openrpc.document._base import OpenRPCModel
from django_jsonrpc.openrpc.document.external_docs import OpenRpcExternalDoc

__all__ = [
    "OpenRpcTag",
]


class _OpenRpcTagTD(TypedDict, total=False):
    name: str
    description: str | None
    externalDocs: OpenRpcExternalDoc | None


class OpenRpcTag(OpenRPCModel):

    """
    Adds metadata to a single tag that is used by the Method Object. 
    It is not mandatory to have a Tag Object per tag defined in the Method Object instances.
    """

    name: Annotated[
        str,
        """
        REQUIRED. The name of the tag.
        """
    ]
    description: Annotated[
        str | None,
        Field(default=None),
        """A verbose explanation for the tag. The Markdown syntax MAY be used
        for rich text representation.
        """
    ] = None
    externalDocs: Annotated[
        OpenRpcExternalDoc | None,
        Field(default=None),
        """Additional external documentation for this tag.
        """
    ] = None