from collections import Callable


class Event:
    def __init__(self, menu, name: str, callback: Callable):
        self.menu = menu
        self.name = name
        self.callback = callback

    def __repr__(self):
        return f'Event({self.name}, {self.callback.__name__})'

    def __str__(self):
        return f'Event: {self.name}'

    async def fire(self, *args, **kwargs):
        await self.callback(*args, **kwargs)
