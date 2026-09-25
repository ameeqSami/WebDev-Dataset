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

# WebDev-Dataset: 100 Full-Stack Web Apps for LLM Fine-Tuning

A fine-tuning dataset of **100 complete, working, multi-file full-stack web applications**.

Each sample contains a full project — backend routes, database schema, HTML frontend, CSS styling, and JavaScript — all in a single training example. This teaches a model to generate a whole working project, not just isolated snippets.

---

## Dataset Overview

- **Total Samples:** 100 unique full-stack web applications
- **File:** `dataset.json` (~462 KB)
- **Format:** Alpaca JSON (`instruction` / `input` / `output`)
- **Code:** Every sample is fully runnable with no placeholders or skipped logic

---

## Format

```json
[
  {
    "instruction": "Build a full-stack ... web app using Flask and SQLite ...",
    "input": "",
    "output": "<!-- FILE: database.py -->\n...\n<!-- FILE: app.py -->\n...\n<!-- FILE: templates/index.html -->\n...\n<!-- FILE: static/style.css -->\n...\n<!-- FILE: static/script.js -->\n..."
  }
]
```

### Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `instruction` | `string` | The prompt describing what app to build, the tech stack, and file structure |
| `input` | `string` | Always empty `""` |
| `output` | `string` | The complete multi-file source code |

### File Delimiter

Files inside the `output` are separated by:

```
<!-- FILE: path/to/file.ext -->
[source code]

<!-- FILE: path/to/another_file.ext -->
[source code]
```

---

## Tech Stack

Each app has 4-5 files:

```
├── database.py         # SQLite connection and table setup
├── app.py / main.py    # Flask or FastAPI routes
├── templates/
│   └── index.html      # HTML frontend
└── static/
    ├── style.css        # CSS styling
    └── script.js        # JavaScript (Fetch API)
```

- **Backend:** Python - Flask or FastAPI
- **Database:** SQLite3
- **Frontend:** HTML5, Vanilla CSS, Vanilla JavaScript (ES6+ async/await)

---

## App Catalog (100 Apps)

<details>
<summary><b>Batch 1: Productivity, Project Management & Habits (Apps 01-10)</b></summary>

1. Inventory & Order Management *(Flask + SQLite)*
2. Kanban Task Board *(FastAPI + SQLite)*
3. Markdown Note Taker with Tags *(Flask + SQLite)*
4. Personal Budget & Expense Tracker *(Flask + SQLite)*
5. Recipe Box & Weekly Meal Planner *(FastAPI + SQLite)*
6. Habit Tracker & Daily Streaks *(Flask + SQLite)*
7. Mini CRM & Sales Pipeline *(FastAPI + SQLite)*
8. Appointment & Booking Scheduler *(Flask + SQLite)*
9. Help Desk & IT Support Tickets *(Flask + SQLite)*
10. Community Polling & Voting *(FastAPI + SQLite)*
</details>

<details>
<summary><b>Batch 2: Education, Fitness & E-Commerce (Apps 11-20)</b></summary>

11. Flashcard Study System *(Flask + SQLite)*
12. Job Application Tracker *(Flask + SQLite)*
13. URL Shortener & Click Analytics *(FastAPI + SQLite)*
14. Fitness Workout Log & PR Tracker *(Flask + SQLite)*
15. E-Commerce Product Catalog & Cart *(Flask + SQLite)*
16. Community Discussion Forum *(Flask + SQLite)*
17. Live Event Q&A Dashboard *(FastAPI + SQLite)*
18. Digital Bookmark & Link Archiver *(Flask + SQLite)*
19. Student Gradebook & GPA Calculator *(Flask + SQLite)*
20. Project Time Tracking & Timesheets *(FastAPI + SQLite)*
</details>

<details>
<summary><b>Batch 3: Real Estate, Media & Dev Tools (Apps 21-30)</b></summary>

21. Real Estate Property Listings *(Flask + SQLite)*
22. Library Book Checkout System *(Flask + SQLite)*
23. Simple Blog with Comments *(Flask + SQLite)*
24. Weather & Air Quality Station *(Flask + SQLite)*
25. User Authentication & Session Portal *(Flask + SQLite)*
26. Password Vault & Secret Stash *(FastAPI + SQLite)*
27. Movie & Series Watchlist *(Flask + SQLite)*
28. Employee Directory & Teams *(Flask + SQLite)*
29. Cloud Asset & File Metadata Catalog *(FastAPI + SQLite)*
30. Code Snippet Pastebin *(Flask + SQLite)*
</details>

<details>
<summary><b>Batch 4: Freelance, Dining & Community (Apps 31-40)</b></summary>

31. Freelance Project Milestone & Invoice Tracker *(Flask + SQLite)*
32. Restaurant Table Reservation & Menu *(FastAPI + SQLite)*
33. Podcast Episode Tracker *(Flask + SQLite)*
34. Vehicle Maintenance & Fuel Mileage Log *(Flask + SQLite)*
35. Daily Journal & Mood Tracker *(Flask + SQLite)*
36. SaaS Feature Request & Upvote Board *(FastAPI + SQLite)*
37. Classroom Quiz Maker & Tester *(Flask + SQLite)*
38. Hotel Room Reservation Engine *(Flask + SQLite)*
39. Donation & Fundraising Campaign Tracker *(FastAPI + SQLite)*
40. Pet Adoption & Shelter Registry *(Flask + SQLite)*
</details>

<details>
<summary><b>Batch 5: Health, Commerce & Utilities (Apps 41-50)</b></summary>

41. Vinyl & Music Collection Curator *(Flask + SQLite)*
42. Pharmacy Prescription Reminder *(FastAPI + SQLite)*
43. Conference Agenda & Speaker Schedule *(Flask + SQLite)*
44. Newsletter Subscription & Audience Manager *(Flask + SQLite)*
45. Warehouse Shipment & Logistics Tracking *(FastAPI + SQLite)*
46. Smart Home Appliance Controller *(Flask + SQLite)*
47. Travel Itinerary Planner & Packing Checklist *(Flask + SQLite)*
48. Customer Feedback & NPS Survey *(FastAPI + SQLite)*
49. Digital Contact & Business Card Rolodex *(Flask + SQLite)*
50. Online Timed Auction & Bidding System *(FastAPI + SQLite)*
</details>

<details>
<summary><b>Batch 6: Memberships, Events & Dev Platforms (Apps 51-60)</b></summary>

51. Gym Membership & Member Check-in Tracker *(Flask + SQLite)*
52. Event Ticketing & RSVP Guest Manager *(FastAPI + SQLite)*
53. Bug Bounty & Vulnerability Disclosure Log *(Flask + SQLite)*
54. API Key & Webhook Developer Token Manager *(FastAPI + SQLite)*
55. Freelance Gig & Services Marketplace Catalog *(Flask + SQLite)*
56. Online Book Club & Reading Goal Shelf *(Flask + SQLite)*
57. Community Equipment Rental & Tool Library *(FastAPI + SQLite)*
58. Medical Clinic Patient Triage & Intake Portal *(Flask + SQLite)*
59. Crypto Asset Portfolio & Watchlist Tracker *(FastAPI + SQLite)*
60. Artisanal Coffee Shop Barista Order Queue *(Flask + SQLite)*
</details>

<details>
<summary><b>Batch 7: Operations, Culture & Environment (Apps 61-70)</b></summary>

61. SaaS Software License & Renewal Spend Tracker *(FastAPI + SQLite)*
62. Art Gallery Exhibition & Contemporary Showcase *(Flask + SQLite)*
63. Employee Shift & Weekly Roster Scheduler *(FastAPI + SQLite)*
64. E-Commerce RMA Product Returns Desk *(Flask + SQLite)*
65. Podcast Sponsorship & Audio Ad Campaign Pipeline *(Flask + SQLite)*
66. Language Learning Vocabulary Builder & Flash Quiz *(FastAPI + SQLite)*
67. Indoor Plant & Garden Care Watering Log *(Flask + SQLite)*
68. Infrastructure Ping & Health Monitor *(FastAPI + SQLite)*
69. Car Rental Fleet & Reservation Engine *(Flask + SQLite)*
70. Crowdfunding Backer & Tiered Campaign Tracker *(Flask + SQLite)*
</details>

<details>
<summary><b>Batch 8: Community, Property & Hobbies (Apps 71-80)</b></summary>

71. Alumni Network Directory & Mentorship Hub *(Flask + SQLite)*
72. Home Renovation & Contractor Expense Log *(FastAPI + SQLite)*
73. Community Food Pantry & Donation Inventory *(Flask + SQLite)*
74. Scientific Paper Reference & Citation Library *(Flask + SQLite)*
75. Conference Booth Badge Scanner & Lead Capture *(FastAPI + SQLite)*
76. Apartment Tenant Repair Maintenance Request Portal *(Flask + SQLite)*
77. Video Game Backlog & Achievement QuestLog *(Flask + SQLite)*
78. Dog Daycare & Pet Boarding Reservation *(FastAPI + SQLite)*
79. Recipe Macro & Nutritional Calorie Calculator *(Flask + SQLite)*
80. Micro-SaaS Product Launch Waitlist & Referral Leaderboard *(FastAPI + SQLite)*
</details>

<details>
<summary><b>Batch 9: Logistics, Entertainment & Workflows (Apps 81-90)</b></summary>

81. Music Festival Stage Lineup & Timetable Scheduler *(Flask + SQLite)*
82. Warehouse Handheld SKU & Bin Location Locator *(FastAPI + SQLite)*
83. Academic Course Syllabus & Homework Submission Portal *(Flask + SQLite)*
84. Monthly Gourmet Subscription Box Preference Picker *(Flask + SQLite)*
85. Veterinary Clinic Vaccine Record & Booster Log *(FastAPI + SQLite)*
86. Coworking Space Hot-Desk Floorplan Booking *(Flask + SQLite)*
87. Professional Photography Session Inquiry & Portfolio *(Flask + SQLite)*
88. Print-On-Demand Order Fulfillment Status Queue *(FastAPI + SQLite)*
89. Local Neighborhood Lost & Found Bulletin Board *(Flask + SQLite)*
90. Corporate Employee Expense Reimbursement Approval *(FastAPI + SQLite)*
</details>

<details>
<summary><b>Batch 10: Specialities, Tools & Status (Apps 91-100)</b></summary>

91. Antique & Art Appraisal Valuation Request Desk *(Flask + SQLite)*
92. Sports League Tournament Bracket & Match Scores *(FastAPI + SQLite)*
93. Enterprise IT Asset Laptop & Peripheral Checkout *(Flask + SQLite)*
94. Reserve Wine Cellar Inventory & Tasting Notes *(Flask + SQLite)*
95. Public SaaS System Status Page & Incident Broadcast *(FastAPI + SQLite)*
96. Banquet Catering Menu & Headcount Planner *(Flask + SQLite)*
97. Bicycle Repair Shop Work Order Workbench *(FastAPI + SQLite)*
98. Residential Solar Panel Generation & Savings Monitor *(Flask + SQLite)*
99. DesignProof Client Mockup Review & Annotation *(FastAPI + SQLite)*
100. Self-Hosted Read-Later Queue & Bookmarklet Saver *(Flask + SQLite)*
</details>

---

## Loading the Dataset

```python
from datasets import load_dataset

dataset = load_dataset("json", data_files="dataset.json")
print(dataset["train"][0])
```

---

## Fine-Tuning (Alpaca Format)

```python
def format_prompt(example):
    instructions = example["instruction"]
    outputs = example["output"]
    texts = []
    for inst, out in zip(instructions, outputs):
        text = f"### Instruction:\n{inst}\n\n### Response:\n{out}"
        texts.append(text)
    return {"text": texts}

formatted = dataset.map(format_prompt, batched=True)
```

Works directly with **Unsloth**, **LLaMA-Factory**, and any Alpaca-compatible trainer.

---

## Extracting Generated Code to Files

```python
import os, re, json

def extract_files(output_string, target_dir="./generated_app"):
    pattern = r"<!-- FILE: (.*?) -->\n(.*?)(?=(?:<!-- FILE:|\Z))"
    matches = re.findall(pattern, output_string, re.DOTALL)
    for path, content in matches:
        full_path = os.path.join(target_dir, path.strip())
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Created: {full_path}")

with open("dataset.json", "r", encoding="utf-8") as f:
    sample = json.load(f)[0]

extract_files(sample["output"], target_dir="./my_app")
```

---

## License

MIT License - free to use, modify, and fine-tune on for any purpose.
