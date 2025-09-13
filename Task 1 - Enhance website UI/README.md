# **Workshop Booking**

> This website is for coordinators to book a workshop(s), they can book a workshop based on instructors posts or can propose a workshop date based on their convenience.


### Features
* Statistics
    1. Instructors Only
        * Monthly Workshop Count
        * Instructor/Coordinator Profile stats
        * Upcoming Workshops
        * View/Post comments on Coordinator's Profile
    2. Open to All
        * Workshops taken over Map of India
        * Pie chart based on Total Workshops taken to Type of Workshops.

* Workshop Related Features
    > Instructors can Accept, Reject or Delete workshops based on their preference, also they can postpone a workshop based on coordinators request.

## Quick start 

1) Navigate to the folder

```bat
cd Task 1 - Enhance website UI
```

2) Install dependencies

```bat
pip install -r requirements.txt
```

3) Run migrations and start the server

```bat
python manage.py migrate
python manage.py runserver
```

4) Visit the app

- http://127.0.0.1:8000/
- Public statistics: http://127.0.0.1:8000/statistics/public


For detailed setup, see `docs/Getting_Started.md`.

### Live Demo link

https://drive.google.com/file/d/1k_KLMx4F4qGJFEgFAnQ88Avek2BwKpAs/view?usp=sharing

## 2025 UI Refresh – What Changed

This pass focused on a cohesive dark theme, mobile usability, and polishing high-traffic pages while keeping existing behavior intact.

### Global theme
- Introduced a dark, layered gradient theme and centralized styling in `workshop_app/static/workshop_app/css/base.css` (loaded last).
- New utilities and components:
    - `card-dark` (gradient cards with subtle border/shadow)
    - `rounded-xl` (softer 28px radii)
    - `table-soft` (subtle borders and separators)
    - Dark forms, buttons, alerts, dropdown menus
- Footer is no longer fixed; it sits at the bottom naturally via the layout flex column.

### Navigation (desktop unchanged, mobile improved)
- Desktop: brand on the left, nav in the center, profile menu on the right.
- Mobile:
    - Added a left-side hamburger button that opens a slide-out drawer (off-canvas) with all nav links.
    - Username is hidden to avoid overlap; only the profile icon shows.
    - Profile dropdown opens as an overlay and no longer expands the navbar.

### Statistics – Public page
- Charts open in a Bootstrap modal (bar for state, pie for type) to avoid in-card sizing glitches.
- Data is injected via `json_script` to avoid inline template parsing issues.
- Chart rendering is deferred until the modal is shown and is cleaned up on close.
- Mobile refinements:
    - “Charts” title uses responsive spacing (`mb-2 mb-lg-0`).
    - Buttons wrap under the title on small screens with clear spacing and equal widths.

### Workshop Status pages
- Both Instructor and Coordinator views were refreshed:
    - Dark cards, improved table readability, consistent badges/buttons.
    - Better empty/edge states without changing page behavior.

### Workshop Types list
- Wrapped table in a dark card with a visible but soft border.
- Removed row hover greying; switched to subtle striped rows.
- Replaced multiple `<tbody>` blocks with a single one to eliminate a thick separator line.
- Pagination spacing cleaned up.

### Propose Workshop
- The note/alert uses a theme-matching blue and is readable on the dark background.
- Increased card radius using `rounded-xl` and themed the modal dark.

### Backend/statistics data fixes
- Rewrote aggregation to avoid pandas edge cases and produce correct chart data:
    - `WorkshopManager.get_workshops_by_state()` and `.get_workshops_by_type()` now use `collections.Counter`, sort outputs, and account for unknown/empty states.
- Views pass a `stats_payload` dict to templates and render it via `json_script`.

### Polished defaults
- Toastr messages are queued from the base template using a JSON data attribute.
- Dropdowns, alerts, tables, and forms have consistent dark styling across the site.

---

## Developer notes (file touchpoints)

- `workshop_app/templates/workshop_app/base.html`
    - Ensures theme CSS loads last; adds mobile hamburger and off‑canvas menu (#mobileDrawer), backdrop, and small JS controller.
    - Hides username on mobile (`d-none d-lg-inline`) and overlays the profile dropdown.
- `workshop_app/static/workshop_app/css/base.css`
    - Core theme variables, dark components, utilities, and mobile drawer styles.
    - Mobile rules for charts header layout and profile dropdown overlay.
    - Footer changed to non‑fixed.
- `statistics_app/templates/statistics_app/workshop_public_stats.html`
    - Charts header made responsive; buttons moved to a modal workflow; uses `json_script` for data.
- `statistics_app/templates/statistics_app/paginator.html`
    - Compact, theme-consistent pagination.
- `workshop_app/models.py`
    - Counter-based stats aggregation for state/type.
- `statistics_app/views.py`
    - Provides `stats_payload` to the public statistics page.
- `workshop_app/templates/workshop_app/workshop_status_instructor.html`
- `workshop_app/templates/workshop_app/workshop_status_coordinator.html`
    - Refreshed to the dark card/table style and improved readability.
- `workshop_app/templates/workshop_app/propose_workshop.html`
    - Themed alert/modal and increased card radius.
- `workshop_app/templates/workshop_app/workshop_type_list.html`
    - Dark card wrapper, softer separators, single `<tbody>`, and cleaned classes.
- `workshop_app/templates/workshop_app/partials/nav_items.html` (new)
    - Single source of truth for nav links shared by the top bar and mobile drawer.

---


