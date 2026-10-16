"""Runs all required test cases for Tasks A, B, C (plus validity checks)."""
from delivery import from_intervals
from task_a import max_deliveries
from task_b import assign_drivers
from task_c import min_rejected

A = [([], 0), ([(1, 3)], 1), ([(1, 3), (3, 5), (5, 7)], 3), ([(1, 5), (2, 6), (3, 7)], 1),
     ([(5, 7), (1, 3), (3, 5), (2, 4)], 3), ([(1, 4), (2, 4), (4, 6)], 2)]
B = [([], 0), ([(1, 3)], 1), ([(1, 3), (3, 5), (5, 7)], 1), ([(1, 5), (2, 6), (3, 7)], 3),
     ([(1, 4), (2, 5), (4, 7), (5, 8)], 2), ([(5, 8), (1, 4), (2, 5), (4, 6), (6, 9)], 2)]
C = [([], 0), ([(1, 3)], 0), ([(1, 3), (3, 5), (5, 7)], 0), ([(1, 5), (2, 6), (3, 7)], 2),
     ([(5, 7), (1, 3), (3, 5), (2, 4)], 1), ([(1, 2), (2, 3), (3, 4), (1, 3)], 1)]


def compatible(seq):
    return all(seq[i].finish <= seq[i + 1].start for i in range(len(seq) - 1))


def run():
    ok = True
    print("Task A"); 
    for i, (iv, exp) in enumerate(A, 1):
        sel = max_deliveries(from_intervals(iv))
        p = len(sel) == exp and compatible(sel)
        ok &= p
        print(f"  Test {i}: expected {exp}, got {len(sel)}  {'PASS' if p else 'FAIL'}")
    print("Task B")
    for i, (iv, exp) in enumerate(B, 1):
        ds = from_intervals(iv)
        sch = assign_drivers(ds)
        p = (len(sch) == exp and all(compatible(v) for v in sch.values())
             and sum(len(v) for v in sch.values()) == len(ds))
        ok &= p
        print(f"  Test {i}: expected {exp}, got {len(sch)}  {'PASS' if p else 'FAIL'}")
    print("Task C")
    for i, (iv, exp) in enumerate(C, 1):
        got = min_rejected(from_intervals(iv))
        p = got == exp
        ok &= p
        print(f"  Test {i}: expected {exp}, got {got}  {'PASS' if p else 'FAIL'}")
    print("ALL PASSED" if ok else "SOME FAILED")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if run() else 1)
