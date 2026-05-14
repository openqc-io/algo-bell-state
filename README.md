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

### Python SDK

```python
from openqc import OpenQC

qc = OpenQC(api_key="oqc_...")           # see openqc.io → Settings → API Keys
result = qc.algorithm.run("bell-state", input_data={})
print(result)
```

`input_data` is required (use `{}` if the algorithm takes no parameters).
`run()` polls until the job completes; pass `wait=False` to return the job id immediately.

### HTTP API

```bash
curl -X POST https://openqc.io/v1/jobs/algorithms/bell-state/run \
  -H "Authorization: Bearer $OPENQC_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"input_data": {}, "backend": "auto"}'
```

Returns a job id; poll `GET /v1/jobs/{job_id}` until `status=completed`.

### CLI

A dedicated `openqc algorithm run ...` command is on the roadmap (Phase 9). Until then, use the SDK or HTTP examples above.

## References

- https://en.wikipedia.org/wiki/Bell_state

---
Maintained by the OpenQC team. See [CONTRIBUTING.md](https://github.com/openqc-io/algorithms-index/blob/main/CONTRIBUTING.md) for how to propose changes.
