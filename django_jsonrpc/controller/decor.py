from collections.abc import Callable
from functools import wraps
from typing import Any


def _decorate(
    func: Callable[..., Any],
    rpc_name: str,
    summary: str | None = None,
    description: str | None = None,
    tags: list[str] | None = None,
) -> Callable[..., Any]:
    # Keep an explicit RPC alias on the callable, because class attribute
    # names are used during registry collection and cannot be renamed here.
    setattr(func, "__rpc_method_name__", rpc_name)
    setattr(func, "__rpc_method_summary__", summary)
    setattr(func, "__rpc_method_description__", description)
    setattr(func, "__rpc_method_tags__", tags)

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        return func(*args, **kwargs)

    setattr(wrapper, "__rpc_method_name__", rpc_name)
    setattr(wrapper, "__rpc_method_summary__", summary)
    setattr(wrapper, "__rpc_method_description__", description)
    setattr(wrapper, "__rpc_method_tags__", tags)

    return wrapper


def simple_decorator(
    func: Callable[..., Any],
) -> Callable[..., Any]:

    return _decorate(
        func,
        rpc_name=func.__name__,
        description=func.__doc__,
    )


def parametrized_decorator(
    func: Callable[..., Any],
    *,
    name: str | None = None,
    summary: str | None = None,
    description: str | None = None,
    tags: list[str] | None = None,
) -> Callable[..., Any]:
    rpc_name = name if isinstance(name, str) else func.__name__
    return _decorate(
        func,
        rpc_name,
        summary,
        description,
        tags,
    )


def jsonrpc_method(
    name_or_func: str | Callable | None = None,
    *,
    summary: str | None = None,
    description: str | None = None,
    tags: list[str] | None = None,
) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        return parametrized_decorator(
            func,
            name=name_or_func if isinstance(name_or_func, str) else None,
            summary=summary,
            description=description,
            tags=tags,
        )

    if callable(name_or_func):
        return simple_decorator(
            name_or_func,
        )

    return decorator