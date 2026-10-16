"""Delivery data model and input-file parsing."""
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Delivery:
    id: str
    start: int
    finish: int


def parse_deliveries(path: str) -> List[Delivery]:
    """Read deliveries from a text file: one 'id start finish' per line.
    Blank lines and lines starting with '#' are ignored."""
    deliveries = []
    with open(path) as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 3:
                raise ValueError(f"line {lineno}: expected 'id start finish'")
            d = Delivery(parts[0], int(parts[1]), int(parts[2]))
            if d.start >= d.finish:
                raise ValueError(f"line {lineno}: start must be < finish")
            deliveries.append(d)
    return deliveries


def from_intervals(intervals) -> List[Delivery]:
    """Build deliveries D1..Dn from a list of (start, finish) tuples (for tests)."""
    return [Delivery(f"D{i + 1}", s, f) for i, (s, f) in enumerate(intervals)]
