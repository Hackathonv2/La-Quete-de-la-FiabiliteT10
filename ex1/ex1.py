import re
import sys

if __name__ == "__main__":
    storage_infos = list()
    lines = sys.stdin.readlines()
    for line in lines:
        name = re.findall(r"[a-z]+", line)[0]
        values = re.findall(r"[0-9]+", line)
        storage_infos.append((name, (int(values[0]) * (int(values[1]) + int(values[2])))))
    storage_infos.sort(key=lambda x: x[1])
    print(storage_infos[0][0])
