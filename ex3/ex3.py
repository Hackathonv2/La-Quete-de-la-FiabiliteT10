import functools
import re
import sys
import math

if __name__ == "__main__":
    servers_fail_ratio = [int(value) for value in re.findall(r"[0-9]+", sys.stdin.readlines()[1])]
    base_lcm = functools.reduce(math.lcm, servers_fail_ratio)
    best_lcm = base_lcm
    best_server_to_upgrade = None
    for index, value in enumerate(servers_fail_ratio):
        servers_fail_ratio[index] += 1
        new_lcm = functools.reduce(math.lcm, servers_fail_ratio)
        if new_lcm > best_lcm:
            best_lcm = new_lcm
            best_server_to_upgrade = index
        servers_fail_ratio[index] -= 1
    print(best_server_to_upgrade if best_server_to_upgrade is not None else -1)
