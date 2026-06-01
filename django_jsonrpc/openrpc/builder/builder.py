import logging

from django_jsonrpc.openrpc.document._openrpc_document import OpenRpcDocument
from django_jsonrpc.openrpc.document.info import OpenRpcInfo
from django_jsonrpc.openrpc.document._base import OPENRPC_VERSION
from django_jsonrpc.openrpc.document.method import OpenRpcMethod
from django_jsonrpc.openrpc.document.common import OpenRpcReferenceObject
from django_jsonrpc.openrpc.document.info import OpenRpcContact, OpenRpcLicense
from django_jsonrpc.openrpc.document.server import OpenRpcServer
from django_jsonrpc.openrpc.document.external_docs import OpenRpcExternalDoc
from django_jsonrpc.openrpc.document.components import OpenRpcComponents

logger = logging.getLogger(__name__)

class OpenRpcBuilder:

    document: OpenRpcDocument

    def __init__(
        self,
        title: str = "OpenRPC API title",
        version: str = "1.0.0",
        description: str | None = None,
        terms_of_service: str | None = None,
        contact: OpenRpcContact | None = None,
        license: OpenRpcLicense | None = None,
    ):
        info = OpenRpcInfo(
            title=title,
            description=description,
            version=version,
            terms_of_service=terms_of_service,
            contact=contact,
            license=license,
        )

        self.document = OpenRpcDocument(
            openrpc=OPENRPC_VERSION,
            info=info,

        )

    def add_method(self, method: OpenRpcMethod | OpenRpcReferenceObject):
        """Add method entry to the document.
        """
        self.document.methods.append(method)
    
    def add_server(self, server: OpenRpcServer):
        """Add server entry to the document.
        """
        if self.document.servers is None:
            self.document.servers = []

        self.document.servers.append(server)

    def add_external_doc(self, external_doc: OpenRpcExternalDoc):
        """Add external doc entry to the document.
        """
        if self.document.external_docs is None:
            self.document.external_docs = external_doc
        else:
            ValueError("External doc already exists")
    
    def add_schema(self, schema: str):
        """Add schema entry to the document.
        """
        self.document.schema = schema

    def add_components(self, components: OpenRpcComponents):
        """Add components entry to the document.
        """
        if self.document.components is None:
            self.document.components = components
        else:
            ValueError("Components already exists")

    def build_json(self) -> str:
        return self.document.model_dump_json(
            exclude_none=True,
            by_alias=True,
            indent=4,
        )
