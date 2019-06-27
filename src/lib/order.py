from dataclasses import dataclass
from typing import Optional

from src.lib.cargo import Cargo
from src.lib.stock import Stock


@dataclass(eq=True)
class Order(object):
    source: Stock
    destination: Stock
    cargo: Cargo

    loading_time: Optional[int]

    def __lt__(self, other):
        return self.loading_time < other.loading_time
