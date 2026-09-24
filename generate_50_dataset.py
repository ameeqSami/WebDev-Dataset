import json
import os
import sys

from builder.apps_01_10 import get_apps as get_01_10
from builder.apps_11_20 import get_apps as get_11_20
from builder.apps_21_30 import get_apps as get_21_30
from builder.apps_31_40 import get_apps as get_31_40
from builder.apps_41_50 import get_apps as get_41_50
from builder.apps_51_60 import get_apps as get_51_60
from builder.apps_61_70 import get_apps as get_61_70
from builder.apps_71_80 import get_apps as get_71_80
from builder.apps_81_90 import get_apps as get_81_90
from builder.apps_91_100 import get_apps as get_91_100

def main():
    print("Collecting dataset examples (100 instances)...")
    dataset = []
    dataset.extend(get_01_10())
    dataset.extend(get_11_20())
    dataset.extend(get_21_30())
    dataset.extend(get_31_40())
    dataset.extend(get_41_50())
    dataset.extend(get_51_60())
    dataset.extend(get_61_70())
    dataset.extend(get_71_80())
    dataset.extend(get_81_90())
    dataset.extend(get_91_100())

    print(f"Total instances collected: {len(dataset)}")

    # Strict validation
    assert len(dataset) == 100, f"Expected 100 instances, found {len(dataset)}"
    for idx, item in enumerate(dataset, 1):
        assert "instruction" in item and len(item["instruction"].strip()) > 0, f"Instance {idx} missing instruction"
        assert "input" in item and item["input"] == "", f"Instance {idx} input must be empty string"
        assert "output" in item and len(item["output"].strip()) > 0, f"Instance {idx} missing output"
        assert "<!-- FILE:" in item["output"], f"Instance {idx} missing file delimiters in output"

    output_path = os.path.join(os.path.dirname(__file__), "dataset.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"Successfully generated {output_path}")
    print(f"File size: {file_size_kb:.2f} KB")

    # Verify parse
    with open(output_path, "r", encoding="utf-8") as f:
        verified = json.load(f)
        assert len(verified) == 100
    print("Verification complete: 100 valid JSON instances confirmed!")

if __name__ == "__main__":
    main()
