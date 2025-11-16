import json
from rich.console import Console
from rich.table import Table

def write_report(results, output_file):
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    # Pretty console output
    console = Console()
    table = Table(title="Policy-as-Code Evaluation Results")

    table.add_column("Policy")
    table.add_column("Rule")
    table.add_column("Passed")

    for policy in results:
        for res in policy["results"]:
            table.add_row(
                policy["policy"],
                res["rule"],
                "✅ PASS" if res["passed"] else "❌ FAIL"
            )

    console.print(table)

