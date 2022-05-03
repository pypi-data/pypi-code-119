from contextlib import ExitStack, contextmanager
from typing import ContextManager, Iterator, TypeVar

_T = TypeVar("_T", covariant=True)


class CommandContextMixIn:
    def __init__(self) -> None:
        super().__init__()
        self._in_main_context = False
        self._main_context = ExitStack()

    @contextmanager
    def main_context(self) -> Iterator[None]:
        assert not self._in_main_context

        self._in_main_context = True
        try:
            with self._main_context:
                yield
        finally:
            self._in_main_context = False

    def enter_context(self, context_provider: ContextManager[_T]) -> _T:
        assert self._in_main_context

        return self._main_context.enter_context(context_provider)
