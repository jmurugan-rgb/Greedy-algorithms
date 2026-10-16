"""Task A: maximum number of compatible deliveries for one driver (greedy)."""
from typing import List
from delivery import Delivery


def max_deliveries(deliveries: List[Delivery]) -> List[Delivery]:
    """Earliest-finish-time-first. O(n log n) for the sort, O(n) for the scan."""
    selected = []
    last_finish = float("-inf")
    for d in sorted(deliveries, key=lambda d: (d.finish, d.start)):
        if d.start >= last_finish:      # touching endpoints are allowed
            selected.append(d)
            last_finish = d.finish
    return selected
