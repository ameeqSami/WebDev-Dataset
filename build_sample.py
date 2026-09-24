"""
Script to build all 50 full-stack multi-file web application dataset instances.
"""
import json
import os

from builder.apps_01_10 import get_apps as get_01_10
from builder.apps_11_20 import get_apps as get_11_20
from builder.apps_21_30 import get_apps as get_21_30
from builder.apps_31_40 import get_apps as get_31_40
from builder.apps_41_50 import get_apps as get_41_50

def build_dataset():
    print("Collecting all 50 instances...")
    dataset = []
    dataset.extend(get_01_10())
    dataset.extend(get_11_20())
    dataset.extend(get_21_30())
    dataset.extend(get_31_40())
    dataset.extend(get_41_50())

    print(f"Total instances collected: {len(dataset)}")
    assert len(dataset) == 50, f"Expected 50 instances, found {len(dataset)}"

    out_file = os.path.join(os.path.dirname(__file__), "dataset.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print(f"Saved dataset.json successfully ({os.path.getsize(out_file)/1024:.2f} KB).")
    return dataset

if __name__ == "__main__":
    build_dataset()
