from typing import Annotated, Any, TypedDict

from pydantic import Field

from django_jsonrpc.openrpc.document._base import OpenRPCModel
from django_jsonrpc.openrpc.document.common import (
    OpenRpcTag,
    OpenRcpContentDescriptorObject,
    OpenRpcErrorObject,
    OpenRpcLinkObject,
    OpenRpcExamplePairingObject,
    OpenRpcExampleObject,
)



class OpenRpcComponents(OpenRPCModel):
    """
    Holds a set of reusable objects for different aspects of the OpenRPC.
    All objects defined within the components object will have no effect on
    the API unless they are explicitly referenced from properties outside the
    components object..
    """
    schemas: Annotated[
        dict[str, Any] | None,
        Field(default=None),
        """
        An object to hold reusable Schema Objects.
        """
    ] = None
    links: Annotated[
        dict[str, OpenRpcLinkObject] | None,
        Field(default=None),
        """
        An object to hold reusable Link Objects.
        """
    ] = None
    errors: Annotated[
        dict[str, OpenRpcErrorObject] | None,
        Field(default=None),
        """
        An object to hold reusable Error Objects.
        """
    ] = None
    examples: Annotated[
        dict[str, OpenRpcExampleObject] | None,
        Field(default=None),
        """
        An object to hold reusable Example Objects.
        """
    ] = None
    examplePairings: Annotated[
        dict[str, OpenRpcExamplePairingObject] | None,
        Field(default=None),
        """
        An object to hold reusable Example Pairing Objects.
        """
    ] = None
    contentDescriptors: Annotated[
        dict[str, OpenRcpContentDescriptorObject] | None,
        Field(default=None),
        """
        An object to hold reusable Content Descriptor Objects.
        """
    ] = None
    tags: Annotated[
        dict[str, OpenRpcTag] | None,
        Field(default=None),
        """
        An object to hold reusable Tag Objects.
        """
    ] = None

class _OpenRpcComponentsTD(TypedDict, total=False):
    schemas: dict[str, Any] | None
    links: dict[str, OpenRpcLinkObject] | None
    errors: dict[str, OpenRpcErrorObject] | None
    examples: dict[str, OpenRpcExampleObject] | None
    examplePairings: dict[str, OpenRpcExamplePairingObject] | None
    contentDescriptors: dict[str, OpenRcpContentDescriptorObject] | None
    tags: dict[str, OpenRpcTag] | None