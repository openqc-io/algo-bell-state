"""Auto-generated template for bell-state.

Migrated from legacy openqc-algorithms JSON. The QASM is inlined so the
sandbox (no file/network access) can execute it without reading circuit.qasm.
"""


_QASM = "OPENQASM 2.0;\ninclude \"qelib1.inc\";\nqreg q[2];\ncreg c[2];\nh q[0];\ncx q[0], q[1];\nmeasure q -> c;"


class AlgorithmTemplate:

    def build(self, input_data, ctx):
        return {
            "type": "circuit",
            "qasm_code": _QASM,
        }

    def interpret(self, raw_result, input_data):
        counts = raw_result.get("counts", {})
        total = sum(counts.values()) or 1
        probabilities = {state: c / total for state, c in counts.items()}
        return {
            "counts": counts,
            "probabilities": probabilities,
            "total_shots": total,
        }
