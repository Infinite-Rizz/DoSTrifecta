import time
import sys
from itertools import repeat
from multiprocessing import Pool, cpu_count

def f(x, runtime=1, sleeptime=0, busycycles=100000):
    timeout = time.time() + runtime
    cnt = 0
    while True:
        if sleeptime and cnt % busycycles == 0:
            time.sleep(sleeptime)
        x*x
        cnt += 1

if __name__ == '__main__':
    runtime = 5 if len(sys.argv) <= 1 else float(sys.argv[1])
    sleeptime = 0.0 if len(sys.argv) <= 2 else float(sys.argv[2])
    busycycles = 100000 if len(sys.argv) <= 3 else int(sys.argv[3])
    processes = cpu_count() if len(sys.argv) <= 4 else int(sys.argv[4]) if 0 < int(sys.argv[4]) <= cpu_count() else cpu_count()
    pool = Pool(processes)
    pool.starmap(f, zip(range(processes), repeat(runtime), repeat(sleeptime), repeat(busycycles)))