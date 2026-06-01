# Custom error

You have an able to create your own error, or use exist in your code, see below example


``` python
from django_jsonrpc import BaseController
from django_jsonrpc.core import PrcError, InternalError

class DoesntSupprotError(RpcError):
    code: int = -4000
    message: str = "Doesn't support"

class MyController(BaseController):

    def method_default_error(self) -> RpcError | ...:
        ...
        
        if flag:
            return InternalError(data="Doesn't support")

        ...

    def method_custom_error(self) -> RpcError | ...:
        ...

        if flag:
            return DoesntSupprotError()

        ...

``` 
