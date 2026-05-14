# Bell State

> Create a maximally entangled Bell pair (|00> + |11>) / sqrt(2) using a Hadamard gate followed by a CNOT.

## At a glance

| | |
|---|---|
| Slug | `bell-state` |
| Qubits | 2 |
| Industries | foundational |
| Techniques | gate |
| Difficulty | beginner |
| Computation model | gate |
| Access | `open` |
| License | Apache-2.0 |

## Circuit

```qasm
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0], q[1];
measure q -> c;
```

## How to run

```python
from openqc import OpenQC
qc = OpenQC(api_key="your-key")
result = qc.algorithm.run("bell-state")
print(result)
```

```bash
openqc algorithm run bell-state
```

## References

- https://en.wikipedia.org/wiki/Bell_state

---
Maintained by the OpenQC team. See [CONTRIBUTING.md](https://github.com/openqc-io/algorithms-index/blob/main/CONTRIBUTING.md) for how to propose changes.
