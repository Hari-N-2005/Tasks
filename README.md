# Tasks Overview

This repository contains three deliverables for Python completed as part of the internship tasks. Use this README to navigate to each task and understand what it includes.

## Task 1 — Enhance website UI
Path: `Task 1 - Enhance website UI/`

A Django-based UI/UX refresh of the Workshop Booking site with a cohesive dark theme and mobile improvements.

Highlights:
- Global dark theme and centralized CSS (`workshop_app/static/workshop_app/css/base.css`)
- Mobile-only hamburger + left slide-out drawer for navigation
- Profile name hidden on mobile (icon-only), dropdown overlays navbar (no layout jump)
- Charts moved to a modal on the public statistics page; data injected via `json_script`
- Mobile layout fixes for the Charts header and buttons
- Workshop Types table visual fixes (single `<tbody>`, thinner separators)
- Footer no longer fixed; sticks to the bottom via layout
- Status pages and Propose Workshop polished to match the theme

Instructions and detailed changes: See `Task 1 - Enhance website UI/README.md`.

Live Demo link : https://drive.google.com/file/d/1k_KLMx4F4qGJFEgFAnQ88Avek2BwKpAs/view?usp=sharing

---

## Task 2 — Prompt for AI
Path: `Task 2 - Prompt for AI.md`

A carefully crafted prompt that positions an AI as a supportive coding tutor. The prompt:
- Encourages positive, student-friendly language
- Guides with questions and hints rather than providing full solutions
- Suggests practical debugging steps
- Avoids revealing answers, focusing on building problem-solving skills

The file also includes rationale and design choices for the prompt structure and tone.

---

## Task 3 — Research Plan
Path: `Task 3 - Research Plan.md`

A short research plan for evaluating open-source AI models to analyze student Python code and generate reflective guidance. It discusses:
- Candidate models (e.g., Code Llama, StarCoder)
- Evaluation criteria (concept detection, feedback clarity, avoidance of full solutions)
- Validation via a rubric and representative student misconceptions
- Trade‑offs (accuracy vs. steerability; size/cost vs. accessibility)

---

## How to run Task 1 locally (optional)
From the `Task 1 - Enhance website UI/` folder:

```bat
cd Task 1 - Enhance website UI
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

For more details, see `Task 1 - Enhance website UI/README.md`.