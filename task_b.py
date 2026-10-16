"""Task B: minimum number of drivers (greedy + min-heap)."""
import heapq
from typing import Dict, List
from delivery import Delivery


def assign_drivers(deliveries: List[Delivery]) -> Dict[int, List[Delivery]]:
    """Process deliveries by start time. Heap holds (finish_time, driver_number)
    of each driver's most recent delivery. O(n log n)."""
    schedules: Dict[int, List[Delivery]] = {}
    heap = []  # (finish_time, driver_no)
    for d in sorted(deliveries, key=lambda d: (d.start, d.finish)):
        if heap and heap[0][0] <= d.start:          # earliest-free driver is free
            _, driver = heapq.heappop(heap)
        else:                                        # hire a new driver
            driver = len(schedules) + 1
            schedules[driver] = []
        schedules[driver].append(d)
        heapq.heappush(heap, (d.finish, driver))
    return schedules
