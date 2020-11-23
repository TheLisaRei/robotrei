# simple json back memory
# TODO: replace with db later
import json
from collections import MutableMapping
from pathlib import Path
from typing import Iterator


class Memory(MutableMapping):
    UNKNOWN_RESPONSE = "something lisa has not told me about yet :("

    _data = {}

    def __init__(self, path: str = 'resources/memory.json'):
        self._path = Path(path)

        if self._path.exists():
            with self._path.open('r') as json_source:
                self._data = json.load(json_source)

    def knows(self, key: str) -> bool:
        return key in self._data

    def get(self, key: str) -> str:
        if key not in self._data:
            return Memory.UNKNOWN_RESPONSE.format(key=key)

        return self._data[key]

    def set(self, key: str, value: str):
        self._data[key] = value
        self.save()

    def delete(self, key: str):
        del self._data[key]
        self.save()

    def save(self):
        with self._path.open('w') as outfile:
            json.dump(self._data, outfile)

    # Attribute access
    def __getattr__(self, attr):
        return self.get(attr)

    # MutableMapping
    def __setitem__(self, k: str, v: str) -> None:
        self.set(key=k, value=v)

    def __delitem__(self, k: str) -> None:
        self.delete(key=k)

    def __getitem__(self, k: str) -> str:
        return self.get(key=k)

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[str]:
        return self._data.keys()
