# Django jsonrpc implementation

## Advantages

- Complete support jsonrpc 2.0 (Request, Notificatin, Batch)
- Auto generation openrpc.json 1.3.2 version
- Auto generation OpenRPC documentation (like swagger)
- Async support

## Create methods

We provide several methods creating methods. 

- Using `method_` prefix
- Using `jsonrpc_method` decorator

``` python

from django-jsonrpc import BaseController

class EchoController(BaseController):
    
    def method_echo_hello(self, name) -> str:
        return f"hello {name}"

```

## Adding several controllers to one controller

``` python
from django-jsonrpc import RouteController

class PrintController(BaseController):

    def method_print_hello(self, name) -> None:
        print(f"hello {name}")

route = RouteController(
    'jsonrpc',
    controllers=[
        PrintController,
        EchoController,
    ]
    
)
```

## Generation openrpc.json and OpenRpc documentation

``` python
from django_jsonrpc.controller.openrpc.collectors import OpenRpcCollector

collector = OpenRpcCollector(
    PrintController,
    EchoController,
    title='My mini API'
)


urlpatterns = [
    path('echorpc', EchoController,as_view)
    path('jsonrpc', route.as_view()),
    path('openrpc.json', OpenRpcJsonView.as_view(collector=collector)),
    path('docs', OpenRpcDocView.as_view()),
]

````
