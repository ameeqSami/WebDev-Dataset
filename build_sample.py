"""
Script to build all 100 full-stack multi-file web application dataset instances.
"""
import json
import os

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

def build_dataset():
    print("Collecting all 100 instances...")
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
    assert len(dataset) == 100, f"Expected 100 instances, found {len(dataset)}"

    out_file = os.path.join(os.path.dirname(__file__), "dataset.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print(f"Saved dataset.json successfully ({os.path.getsize(out_file)/1024:.2f} KB).")
    with open(out_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)
        print(f"Validated: Exactly {len(loaded)} instances loaded successfully.")
    return loaded

if __name__ == "__main__":
    build_dataset()
