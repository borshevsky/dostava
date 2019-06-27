from dataclasses import dataclass
from src.lib.cargo import Stock, Cargo

@dataclass
class Order(object):
    source: Stock
    destination: Stock
    cargo: Cargo
