import time

from decay import simulate_loop, simulate


N0 = 20000
steps = 200
lam = 0.4
dt = 0.05
seed = 0


start = time.perf_counter()
simulate_loop(N0, lam, dt, steps, seed)
loop_time = time.perf_counter() - start


start = time.perf_counter()
simulate(N0, lam, dt, steps, seed)
numpy_time = time.perf_counter() - start


speedup = loop_time / numpy_time


print(f"Loop time: {loop_time:.6f} seconds")
print(f"NumPy time: {numpy_time:.6f} seconds")
print(f"Speedup: {speedup:.2f}x")