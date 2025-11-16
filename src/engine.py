from policy_loader import load_policies
from evaluator import evaluate_policies
from report_writer import write_report
import yaml
import json

def run_engine(config_file):
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    policies = load_policies("policies")
    results = evaluate_policies(policies, config)
    write_report(results, "reports/example_report.json")

    return results


if __name__ == "__main__":
    results = run_engine("configs/sample_config.yml")
    print(json.dumps(results, indent=2))

