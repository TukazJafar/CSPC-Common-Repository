# CSPC — PW1 Lab A

## Setup & Usage

This project contains a radioactive decay simulation implemented in Python.

The project uses a Conda environment named `cspc` with Python 3.11, NumPy, and pytest.

### Create the environment

From the repository root:

```bash
conda env create -f "PW1/Lab A/environment.yml"
```

Activate the environment:

```bash
conda activate cspc
```

### Run the tests

Go to the Lab A directory:

```bash
cd "PW1/Lab A"
```

Run:

```bash
pytest -v
```

The test suite contains three tests covering the initial atom count, rejection of a negative decay rate, and agreement with the analytical decay law.

### Run the performance benchmark

From `PW1/Lab A`:

```bash
python speed.py
```

The benchmark compares the pure-Python loop implementation with the vectorised NumPy implementation.

---

## Correctness

The simulation models radioactive decay.

Each atom has a probability of decaying during a short time step. The simulation provides two implementations:

* `simulate_loop` — a pure-Python implementation that loops over individual atoms.
* `simulate` — a vectorised NumPy implementation.

The expected analytical law is:

```text
N(t) = N0 * exp(-lam * t)
```

The test suite contains three tests:

1. `test_starts_at_N0` checks that the simulation starts with `N0` atoms.
2. `test_rejects_negative_rate` checks that a negative decay rate raises `ValueError`.
3. `test_matches_law` runs the simulation with multiple random seeds, calculates the average final number of atoms, and checks that it is close to the analytical result.

All three tests pass:

```text
3 passed
```

---

## Performance

The performance benchmark uses:

```text
N0 = 20000
steps = 200
lam = 0.4
dt = 0.05
seed = 0
```

The measured results on this computer were:

```text
Loop time: 0.175003 seconds
NumPy time: 0.000231 seconds
Speedup: 757.82x
```

The NumPy implementation was measured to take less time than the pure-Python loop for this benchmark.

The speedup is calculated as:

```text
loop time / NumPy time
```

Therefore:

```text
0.175003 / 0.000231 ≈ 757.82
```

The benchmark uses `time.perf_counter()` to measure execution time.

---

## Reproducibility

The simulation accepts a `seed` argument and uses NumPy's random number generator:

```python
rng = np.random.default_rng(seed)
```

Using the same seed makes the random simulation reproducible.

The tests use multiple seeds when checking the average behaviour of the sim
