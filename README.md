# Pioneer Delivery Algorithm Portfolio — Part I: Greedy Algorithms
CS 413 — Analysis of Algorithms

## Language
Python 3 (standard library only; no compile step).

## How to run
```
python3 run_tests.py                 # all required test cases for Tasks A, B, C
python3 main.py deliveries.txt       # run Tasks A, B, C on a data file
python3 main.py deliveries.txt a     # only Task A  (use b or c for the others)
python3 task_d.py                    # Task D counterexample (computed and brute-force verified)
```

## Input file format
One delivery per line: `id start_time finish_time` (whitespace separated, integer times,
start < finish). Blank lines and lines starting with `#` are ignored. Sample (`deliveries.txt`):
```
# id start finish
D01 10 13
D02 2 5
D03 4 7
D04 1 8
D05 8 11
D06 11 14
D07 13 16
```
Sample output on this file: Task A selects D02, D05, D06 (3 deliveries); Task B needs 3 drivers
(Driver 1: D04 D06; Driver 2: D02 D05 D07; Driver 3: D03 D01); Task C rejects 4.

## Program organization
| File | Purpose |
|---|---|
| `delivery.py` | `Delivery` dataclass, input-file parser, helper to build test data |
| `task_a.py` | `max_deliveries()` — greedy interval selection |
| `task_b.py` | `assign_drivers()` — greedy assignment with a min-heap |
| `task_c.py` | `min_rejected()` — reuses Task A |
| `task_d.py` | Task D counterexample, with brute-force verification |
| `main.py` | Command-line driver / output formatting |
| `run_tests.py` | Required test cases, plus checks that schedules are conflict-free |

## Task A — Maximum deliveries for one driver
1. **Greedy choice:** sort by finish time (earliest first); repeatedly take the delivery with the
   earliest finish time that starts at or after the finish of the last selected delivery
   (start ≥ last finish, so touching endpoints are allowed).
2. **Why optimal (exchange argument):** Let g1 be the greedy first pick (earliest finish overall)
   and let O = o1, o2, … be any optimal schedule sorted by time. Since f(g1) ≤ f(o1), replacing o1
   by g1 creates no conflict with o2, so the result is still feasible and still optimal. Thus some
   optimal solution contains g1. After removing g1 and every delivery overlapping it, the remaining
   problem is the same problem on deliveries starting at or after f(g1), and its optimal solution
   is the rest of O. By induction, greedy's picks can be swapped in one at a time, so greedy
   size = optimal size.
3. **Running time:** sorting O(n log n) + one linear scan O(n) = **O(n log n)**.

## Task B — Minimum number of drivers
1. **Priority queue contents:** one entry `(finish_time, driver_number)` per driver in use —
   the finish time of that driver's most recent delivery. The min-heap's top is the driver who
   becomes free earliest.
2. **Driver selection:** process deliveries in order of start time. If the heap's top finish time
   ≤ the new delivery's start, pop that driver and give them the delivery; otherwise hire a new
   driver. Push the (new finish, driver) entry back.
3. **Why minimum:** a new driver is hired only when the delivery's start time s is earlier than
   the finish of *every* current driver's last delivery. Since deliveries are processed by start
   time, all of those d drivers' current deliveries started ≤ s and are still running at s, so
   together with the new one there are d+1 deliveries all overlapping at time s. Any schedule
   needs ≥ d+1 drivers (the depth of overlap), so the greedy count equals the lower bound.
4. **Running time:** sort O(n log n); each of the n deliveries does ≤ 1 heap pop and 1 push,
   each O(log n). Total **O(n log n)**.

## Task C — Minimum rejected deliveries
1. **Relation to Task A:** keeping the largest compatible set is the same as rejecting the fewest.
   The accepted set must be mutually compatible, so Task A's maximum is exactly what we keep.
2. **Answer:** if the maximum compatible set has size k, then **n − k** deliveries must be
   rejected (can't keep more than k; and rejecting the other n − k achieves it).
3. **Running time:** Task A in O(n log n) plus O(1) subtraction = **O(n log n)**.

## Required test results (`python3 run_tests.py`)
**Task A** (max selected) — all PASS

| Test | Intervals | Expected | Got |
|---|---|---|---|
| 1 | none | 0 | 0 |
| 2 | (1,3) | 1 | 1 |
| 3 | (1,3),(3,5),(5,7) | 3 | 3 |
| 4 | (1,5),(2,6),(3,7) | 1 | 1 |
| 5 | (5,7),(1,3),(3,5),(2,4) | 3 | 3 |
| 6 | (1,4),(2,4),(4,6) | 2 | 2 |

**Task B** (min drivers; schedules verified to have no overlaps and to cover every delivery) — all PASS

| Test | Intervals | Expected | Got |
|---|---|---|---|
| 1 | none | 0 | 0 |
| 2 | (1,3) | 1 | 1 |
| 3 | (1,3),(3,5),(5,7) | 1 | 1 |
| 4 | (1,5),(2,6),(3,7) | 3 | 3 |
| 5 | (1,4),(2,5),(4,7),(5,8) | 2 | 2 |
| 6 | (5,8),(1,4),(2,5),(4,6),(6,9) | 2 | 2 |

**Task C** (min rejected) — all PASS

| Test | Intervals | Expected | Got |
|---|---|---|---|
| 1 | none | 0 | 0 |
| 2 | (1,3) | 0 | 0 |
| 3 | (1,3),(3,5),(5,7) | 0 | 0 |
| 4 | (1,5),(2,6),(3,7) | 2 | 2 |
| 5 | (5,7),(1,3),(3,5),(2,4) | 1 | 1 |
| 6 | (1,2),(2,3),(3,4),(1,3) | 1 | 1 |

## Task D — When a greedy choice fails
Greedy G: go through deliveries by decreasing profit; put each in the earliest free slot ≥ its
ready time. Value of a delivery is P / (1 + delay).

**1. Counterexample data** (profits distinct)

| Delivery | Ready R | Profit P |
|---|---|---|
| A | 0 | 10 |
| B | 0 | 9 |
| C | 1 | 8 |

**2. Greedy G** (order A, B, C)
- A: earliest slot ≥ 0 is slot 0 → delay 0 → V = 10
- B: slot 0 taken; earliest slot ≥ 0 is slot 1 → delay 1 → V = 9/2 = 4.5
- C: slot 1 taken; earliest slot ≥ 1 is slot 2 → delay 1 → V = 8/2 = 4

**V(G) = 10 + 4.5 + 4 = 18.5**

**3. Better schedule S:** A → slot 0, C → slot 1, B → slot 2.
- A: delay 0 → 10
- C: delay 0 → 8
- B: delay 2 → 9/3 = 3

**V(S) = 10 + 8 + 3 = 21 > 18.5**

**4. Conclusion:** S is a valid schedule (each slot ≥ ready time, all slots distinct) with strictly
higher value than G's, so G does not always produce an optimal schedule. The flaw: G lets the higher-profit B take slot 1 first, but pushing B back one more slot costs only 1.5 (4.5 → 3), while it lets C run on time, gaining 4 (4 → 8). The delay penalty is relative (divides by 1 + delay), so profit order alone is the wrong criterion. `python3 task_d.py` confirms by
brute force that 21 is the true optimum for this instance.
