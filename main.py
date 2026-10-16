"""Pioneer Delivery scheduler. Usage: python main.py <datafile> [a|b|c|all]"""
import sys
from delivery import parse_deliveries
from task_a import max_deliveries
from task_b import assign_drivers
from task_c import min_rejected


def report_a(ds):
    sel = max_deliveries(ds)
    print("Task A: maximum deliveries for one driver")
    for d in sel:
        print(f"  {d.id}  start={d.start}  finish={d.finish}")
    print(f"Total deliveries completed: {len(sel)}")


def report_b(ds):
    sched = assign_drivers(ds)
    print("Task B: minimum drivers")
    for driver, items in sched.items():
        print(f"Driver {driver}: " + " ".join(d.id for d in items))
    print(f"Minimum drivers required: {len(sched)}")


def report_c(ds):
    print("Task C: minimum rejected deliveries")
    print(f"Minimum rejected: {min_rejected(ds)}")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    ds = parse_deliveries(argv[1])
    which = argv[2].lower() if len(argv) > 2 else "all"
    if which in ("a", "all"): report_a(ds); print()
    if which in ("b", "all"): report_b(ds); print()
    if which in ("c", "all"): report_c(ds)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
