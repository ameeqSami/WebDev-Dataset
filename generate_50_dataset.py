import json
import os
import sys

from builder.apps_01_10 import get_apps as get_01_10
from builder.apps_11_20 import get_apps as get_11_20
from builder.apps_21_30 import get_apps as get_21_30
from builder.apps_31_40 import get_apps as get_31_40
from builder.apps_41_50 import get_apps as get_41_50

def main():
    print("Collecting dataset examples...")
    dataset = []
    dataset.extend(get_01_10())
    dataset.extend(get_11_20())
    dataset.extend(get_21_30())
    dataset.extend(get_31_40())
    dataset.extend(get_41_50())

    print(f"Total instances collected: {len(dataset)}")

    # Strict validation
    assert len(dataset) == 50, f"Expected 50 instances, found {len(dataset)}"
    for idx, item in enumerate(dataset, 1):
        assert "instruction" in item and len(item["instruction"].strip()) > 0
        assert "input" in item and item["input"] == ""
        assert "output" in item and len(item["output"].strip()) > 0
        assert "<!-- FILE:" in item["output"]

    output_path = os.path.join(os.path.dirname(__file__), "dataset.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    main()
