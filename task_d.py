"""Task D: counterexample showing greedy G (by decreasing profit) is not optimal."""
from itertools import permutations

# name: (ready_time R, profit P)
DELIVERIES = {"A": (0, 10), "B": (0, 9), "C": (1, 8)}


def value(schedule):
    """schedule: {name: slot}. V = sum P / (1 + (T - R))."""
    return sum(DELIVERIES[j][1] / (1 + schedule[j] - DELIVERIES[j][0]) for j in schedule)


def greedy_G():
    schedule, used = {}, set()
    for j in sorted(DELIVERIES, key=lambda j: -DELIVERIES[j][1]):
        t = DELIVERIES[j][0]
        while t in used:
            t += 1
        schedule[j] = t
        used.add(t)
    return schedule


def brute_force_best():
    best, best_s = -1, None
    names = list(DELIVERIES)
    for slots in permutations(range(6), len(names)):
        s = dict(zip(names, slots))
        if all(s[j] >= DELIVERIES[j][0] for j in s) and value(s) > best:
            best, best_s = value(s), s
    return best_s


if __name__ == "__main__":
    g = greedy_G()
    better = {"A": 0, "C": 1, "B": 2}
    print("Greedy G:", g, "V(G) =", value(g))
    print("Better S:", better, "V(S) =", value(better))
    b = brute_force_best()
    print("Brute-force optimum:", b, "V =", value(b))
