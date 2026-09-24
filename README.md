---
license: mit
task_categories:
  - text-generation
language:
  - en
tags:
  - code
  - web-development
  - full-stack
  - python
  - flask
  - fastapi
  - sqlite
  - html
  - css
  - javascript
  - instruction-tuning
  - llm-finetuning
pretty_name: Full-Stack WebDev Multi-File Dataset (100 Apps)
size_categories:
  - n<1K
---

# 🚀 WebDev-Dataset: 100 Full-Stack Web Application Prompts for LLM Fine-Tuning

[![Dataset Format](https://img.shields.io/badge/Format-Alpaca%20JSON-blue.svg)](dataset.json)
[![Samples](https://img.shields.io/badge/Samples-100%20Complete%20Apps-brightgreen.svg)](dataset.json)
[![Tech Stack](https://img.shields.io/badge/Stack-Flask%20%7C%20FastAPI%20%7C%20SQLite%20%7C%20Vanilla%20JS-orange.svg)](dataset.json)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

A curated, production-ready instruction fine-tuning dataset containing **100 complete, working, multi-file full-stack web applications**. 

Unlike standard coding datasets that only output isolated single-file snippets or algorithmic functions, this dataset teaches models to generate **cohesive, end-to-end multi-file software projects**—spanning backend API routing, database schema initialization and queries, semantic frontend templates, custom CSS styling, and asynchronous client-side JavaScript.

---

## 📑 Table of Contents

- [Dataset Overview](#-dataset-overview)
- [Dataset Format & Schema](#-dataset-format--schema)
- [Multi-File Output Delimiter](#-multi-file-output-delimiter)
- [Technology Stacks & Architectures](#-technology-stacks--architectures)
- [Complete 100-App Catalog](#-complete-100-app-catalog)
- [Quick Start: Loading & Fine-Tuning](#-quick-start-loading--fine-tuning)
  - [Using Hugging Face Datasets](#using-hugging-face-datasets)
  - [Fine-tuning with Unsloth / LLaMA-Factory](#fine-tuning-with-unsloth--llama-factory)
- [Extracting Code into Project Directories](#-extracting-code-into-project-directories)
- [Dataset Generation & Extension](#-dataset-generation--extension)
- [License](#-license)

---

## 🌟 Dataset Overview

- **Total Samples:** 100 unique, hand-crafted full-stack application blueprints.
- **Dataset File:** `dataset.json` (~462 KB).
- **Format:** Instruction / Input / Output (Alpaca / ShareGPT compatible).
- **Code Completeness:** 100% runnable code with zero placeholders or skipped implementations. Every backend route connects directly to SQLite and corresponding frontend fetch calls.

---

## 📊 Dataset Format & Schema

The dataset is formatted in standard Alpaca JSON structure:

```json
[
  {
    "instruction": "Detailed task prompt outlining the application goals, technical stack, and required file layout...",
    "input": "",
    "output": "<!-- FILE: database.py -->\n...\n<!-- FILE: app.py -->\n...\n<!-- FILE: templates/index.html -->\n...\n<!-- FILE: static/style.css -->\n...\n<!-- FILE: static/script.js -->\n..."
  }
]
```

### Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `instruction` | `string` | The user prompt specifying domain requirements, backend framework, SQLite data models, and desired multi-file structure. |
| `input` | `string` | Empty string `""` (standard instruction format). |
| `output` | `string` | Complete multi-file source code organized with explicit file boundaries. |

---

## 🗂️ Multi-File Output Delimiter

All files inside the `output` string are separated by standard HTML comment file delimiters:

```text
<!-- FILE: path/to/file.ext -->
[Source code for file]

<!-- FILE: path/to/another_file.ext -->
[Source code for another file]
```

This format provides clean separation for:
1. Tokenizers and LLM attention mechanisms to distinguish file transitions.
2. Automated evaluation scripts and parsers to write generated code directly to disk.

---

## 🛠️ Technology Stacks & Architectures

Each application features a complete 4-to-5 file architecture:

```
├── database.py         # SQLite connection factory & table creation
├── app.py / main.py    # Flask or FastAPI REST endpoints & HTML routing
├── templates/
│   └── index.html      # Semantic HTML UI with proper meta tags
└── static/
    ├── style.css       # Clean, modern, responsive CSS design
    └── script.js       # Asynchronous Fetch API client logic
```

### Stacks Covered
- **Backend Frameworks:** Python (Flask, FastAPI)
- **Database:** SQLite3 (standard library, zero external DB configuration required)
- **Frontend:** Semantic HTML5, Vanilla CSS3 (flexbox, grid, custom color palettes), Vanilla JavaScript (ES6+ async/await, Fetch API)

---

## 📚 Complete 100-App Catalog

The dataset covers 100 diverse domains across 10 modular batches:

<details>
<summary><b>Batch 1: Productivity, Project Management & Habits (Apps 01–10)</b></summary>

1. **Inventory & Order Management** *(Flask + SQLite)*
2. **Kanban Task Board** *(FastAPI + SQLite)*
3. **Markdown Note Taker with Tags** *(Flask + SQLite)*
4. **Personal Budget & Expense Tracker** *(Flask + SQLite)*
5. **Recipe Box & Weekly Meal Planner** *(FastAPI + SQLite)*
6. **Habit Tracker & Daily Streaks** *(Flask + SQLite)*
7. **Mini CRM & Sales Pipeline** *(FastAPI + SQLite)*
8. **Appointment & Booking Scheduler** *(Flask + SQLite)*
9. **Help Desk & IT Support Tickets** *(Flask + SQLite)*
10. **Community Polling & Voting** *(FastAPI + SQLite)*
</details>

<details>
<summary><b>Batch 2: Education, Fitness & E-Commerce (Apps 11–20)</b></summary>

11. **Flashcard Study System** *(Flask + SQLite)*
12. **Job Application Tracker** *(Flask + SQLite)*
13. **URL Shortener & Click Analytics** *(FastAPI + SQLite)*
14. **Fitness Workout Log & PR Tracker** *(Flask + SQLite)*
15. **E-Commerce Product Catalog & Cart** *(Flask + SQLite)*
16. **Community Discussion Forum** *(Flask + SQLite)*
17. **Live Event Q&A Dashboard** *(FastAPI + SQLite)*
18. **Digital Bookmark & Link Archiver** *(Flask + SQLite)*
19. **Student Gradebook & GPA Calculator** *(Flask + SQLite)*
20. **Project Time Tracking & Timesheets** *(FastAPI + SQLite)*
</details>

<details>
<summary><b>Batch 3: Real Estate, Media & Dev Tools (Apps 21–30)</b></summary>

21. **Real Estate Property Listings** *(Flask + SQLite)*
22. **Library Book Checkout System** *(Flask + SQLite)*
23. **Simple Blog with Comments** *(Flask + SQLite)*
24. **Weather & Air Quality Station** *(Flask + SQLite)*
25. **User Authentication & Session Portal** *(Flask + SQLite)*
26. **Password Vault & Secret Stash** *(FastAPI + SQLite)*
27. **Movie & Series Watchlist** *(Flask + SQLite)*
28. **Employee Directory & Teams** *(Flask + SQLite)*
29. **Cloud Asset & File Metadata Catalog** *(FastAPI + SQLite)*
30. **Code Snippet Pastebin** *(Flask + SQLite)*
</details>

<details>
<summary><b>Batch 4: Freelance, Dining & Community (Apps 31–40)</b></summary>

31. **Freelance Project Milestone & Invoice Tracker** *(Flask + SQLite)*
32. **Restaurant Table Reservation & Menu** *(FastAPI + SQLite)*
33. **Podcast Episode Tracker** *(Flask + SQLite)*
34. **Vehicle Maintenance & Fuel Mileage Log** *(Flask + SQLite)*
35. **Daily Journal & Mood Tracker** *(Flask + SQLite)*
36. **SaaS Feature Request & Upvote Board** *(FastAPI + SQLite)*
37. **Classroom Quiz Maker & Tester** *(Flask + SQLite)*
38. **Hotel Room Reservation Engine** *(Flask + SQLite)*
39. **Donation & Fundraising Campaign Tracker** *(FastAPI + SQLite)*
40. **Pet Adoption & Shelter Registry** *(Flask + SQLite)*
</details>

<details>
<summary><b>Batch 5: Health, Commerce & Utilities (Apps 41–50)</b></summary>

41. **Vinyl & Music Collection Curator** *(Flask + SQLite)*
42. **Pharmacy Prescription Reminder** *(FastAPI + SQLite)*
43. **Conference Agenda & Speaker Schedule** *(Flask + SQLite)*
44. **Newsletter Subscription & Audience Manager** *(Flask + SQLite)*
45. **Warehouse Shipment & Logistics Tracking** *(FastAPI + SQLite)*
46. **Smart Home Appliance Controller** *(Flask + SQLite)*
47. **Travel Itinerary Planner & Packing Checklist** *(Flask + SQLite)*
48. **Customer Feedback & NPS Survey** *(FastAPI + SQLite)*
49. **Digital Contact & Business Card Rolodex** *(Flask + SQLite)*
50. **Online Timed Auction & Bidding System** *(FastAPI + SQLite)*
</details>

<details>
<summary><b>Batch 6: Memberships, Events & Dev Platforms (Apps 51–60)</b></summary>

51. **Gym Membership & Member Check-in Tracker** *(Flask + SQLite)*
52. **Event Ticketing & RSVP Guest Manager** *(FastAPI + SQLite)*
53. **Bug Bounty & Vulnerability Disclosure Log** *(Flask + SQLite)*
54. **API Key & Webhook Developer Token Manager** *(FastAPI + SQLite)*
55. **Freelance Gig & Services Marketplace Catalog** *(Flask + SQLite)*
56. **Online Book Club & Reading Goal Shelf** *(Flask + SQLite)*
57. **Community Equipment Rental & Tool Library** *(FastAPI + SQLite)*
58. **Medical Clinic Patient Triage & Intake Portal** *(Flask + SQLite)*
59. **Crypto Asset Portfolio & Watchlist Tracker** *(FastAPI + SQLite)*
60. **Artisanal Coffee Shop Barista Order Queue** *(Flask + SQLite)*
</details>

<details>
<summary><b>Batch 7: Operations, Culture & Environment (Apps 61–70)</b></summary>

61. **SaaS Software License & Renewal Spend Tracker** *(FastAPI + SQLite)*
62. **Art Gallery Exhibition & Contemporary Showcase** *(Flask + SQLite)*
63. **Employee Shift & Weekly Roster Scheduler** *(FastAPI + SQLite)*
64. **E-Commerce RMA Product Returns Desk** *(Flask + SQLite)*
65. **Podcast Sponsorship & Audio Ad Campaign Pipeline** *(Flask + SQLite)*
66. **Language Learning Vocabulary Builder & Flash Quiz** *(FastAPI + SQLite)*
67. **Indoor Plant & Garden Care Watering Log** *(Flask + SQLite)*
68. **Infrastructure Ping & Health Monitor** *(FastAPI + SQLite)*
69. **Car Rental Fleet & Reservation Engine** *(Flask + SQLite)*
70. **Crowdfunding Backer & Tiered Campaign Tracker** *(Flask + SQLite)*
</details>

<details>
<summary><b>Batch 8: Community, Property & Hobbies (Apps 71–80)</b></summary>

71. **Alumni Network Directory & Mentorship Hub** *(Flask + SQLite)*
72. **Home Renovation & Contractor Expense Log** *(FastAPI + SQLite)*
73. **Community Food Pantry & Donation Inventory** *(Flask + SQLite)*
74. **Scientific Paper Reference & Citation Library** *(Flask + SQLite)*
75. **Conference Booth Badge Scanner & Lead Capture** *(FastAPI + SQLite)*
76. **Apartment Tenant Repair Maintenance Request Portal** *(Flask + SQLite)*
77. **Video Game Backlog & Achievement QuestLog** *(Flask + SQLite)*
78. **Dog Daycare & Pet Boarding Reservation** *(FastAPI + SQLite)*
79. **Recipe Macro & Nutritional Calorie Calculator** *(Flask + SQLite)*
80. **Micro-SaaS Product Launch Waitlist & Referral Leaderboard** *(FastAPI + SQLite)*
</details>

<details>
<summary><b>Batch 9: Logistics, Entertainment & Workflows (Apps 81–90)</b></summary>

81. **Music Festival Stage Lineup & Timetable Scheduler** *(Flask + SQLite)*
82. **Warehouse Handheld SKU & Bin Location Locator** *(FastAPI + SQLite)*
83. **Academic Course Syllabus & Homework Submission Portal** *(Flask + SQLite)*
84. **Monthly Gourmet Subscription Box Preference Picker** *(Flask + SQLite)*
85. **Veterinary Clinic Vaccine Record & Booster Log** *(FastAPI + SQLite)*
86. **Coworking Space Hot-Desk Floorplan Booking** *(Flask + SQLite)*
87. **Professional Photography Session Inquiry & Portfolio** *(Flask + SQLite)*
88. **Print-On-Demand Order Fulfillment Status Queue** *(FastAPI + SQLite)*
89. **Local Neighborhood Lost & Found Bulletin Board** *(Flask + SQLite)*
90. **Corporate Employee Expense Reimbursement Approval** *(FastAPI + SQLite)*
</details>

<details>
<summary><b>Batch 10: Specialities, Tools & Status (Apps 91–100)</b></summary>

91. **Antique & Art Appraisal Valuation Request Desk** *(Flask + SQLite)*
92. **Sports League Tournament Bracket & Match Scores** *(FastAPI + SQLite)*
93. **Enterprise IT Asset Laptop & Peripheral Checkout** *(Flask + SQLite)*
94. **Reserve Wine Cellar Inventory & Tasting Notes** *(Flask + SQLite)*
95. **Public SaaS System Status Page & Incident Broadcast** *(FastAPI + SQLite)*
96. **Banquet Catering Menu & Headcount Planner** *(Flask + SQLite)*
97. **Bicycle Repair Shop Work Order Workbench** *(FastAPI + SQLite)*
98. **Residential Solar Panel Generation & Savings Monitor** *(Flask + SQLite)*
99. **DesignProof Client Mockup Review & Annotation** *(FastAPI + SQLite)*
100. **Self-Hosted Read-Later Queue & Bookmarklet Saver** *(Flask + SQLite)*
</details>

---

## ⚡ Quick Start: Loading & Fine-Tuning

### Using Hugging Face Datasets

```python
from datasets import load_dataset

# Load local JSON dataset
dataset = load_dataset("json", data_files="dataset.json")
print(dataset["train"][0])
```

### Fine-tuning with Unsloth / LLaMA-Factory

Format the dataset using an Alpaca prompt template:

```python
def formatting_prompts_func(example):
    instructions = example["instruction"]
    outputs = example["output"]
    texts = []
    for inst, out in zip(instructions, outputs):
        text = f"### Instruction:\n{inst}\n\n### Response:\n{out}"
        texts.append(text)
    return {"text": texts}

formatted_dataset = dataset.map(formatting_prompts_func, batched=True)
```

---

## 📂 Extracting Code into Project Directories

To unpack any model output or dataset instance into physical project files on disk, use the following Python utility:

```python
import os
import re

def extract_files(output_string, target_dir="./generated_app"):
    pattern = r"<!-- FILE: (.*?) -->\n(.*?)(?=(?:<!-- FILE:|\Z))"
    matches = re.findall(pattern, output_string, re.DOTALL)
    
    for relative_path, file_content in matches:
        full_path = os.path.join(target_dir, relative_path.strip())
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(file_content.strip() + "\n")
        print(f"Created: {full_path}")

# Example usage on sample 0
import json
with open("dataset.json", "r", encoding="utf-8") as f:
    sample_app = json.load(f)[0]

extract_files(sample_app["output"], target_dir="./my_app")
```

---

## 🔄 Dataset Generation & Extension

The repository includes a modular generator structure:

```
├── builder/
│   ├── apps_01_10.py
│   ├── apps_11_20.py
│   ├── apps_21_30.py
│   ├── apps_31_40.py
│   ├── apps_41_50.py
│   ├── apps_51_60.py
│   ├── apps_61_70.py
│   ├── apps_71_80.py
│   ├── apps_81_90.py
│   └── apps_91_100.py
├── generate_50_dataset.py     # Main build & validation script
└── dataset.json               # Compiled dataset artifact
```

To re-compile and validate all 100 applications after editing or adding modules:

```bash
python generate_50_dataset.py
```

---

## 📄 License

This dataset is released under the **MIT License**. You are free to use, modify, fine-tune on, and distribute this dataset for research and commercial purposes.
