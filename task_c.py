"""Task C: minimum number of rejected deliveries (LeetCode 435 style)."""
from typing import List
from delivery import Delivery
from task_a import max_deliveries


def min_rejected(deliveries: List[Delivery]) -> int:
    """n - k, where k is the Task A maximum. O(n log n)."""
    return len(deliveries) - len(max_deliveries(deliveries))
