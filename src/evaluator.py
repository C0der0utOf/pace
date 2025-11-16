def evaluate_policies(policies, config):
    results = []

    for policy in policies:
        policy_name = policy.get("name", "Unnamed Policy")
        rules = policy.get("rules", [])

        policy_result = {"policy": policy_name, "results": []}

        for rule in rules:
            key = rule["key"]
            expected = rule["expected"]

            actual = config.get(key, None)
            passed = actual == expected

            policy_result["results"].append({
                "rule": rule["description"],
                "key": key,
                "expected": expected,
                "actual": actual,
                "passed": passed
            })

        results.append(policy_result)
    return results

