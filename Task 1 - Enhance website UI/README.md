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


## Recent UI/UX and Template Improvements (2025)

### General
- Upgraded the overall UI to use modern Bootstrap layouts for a clean, responsive experience.
- Improved alignment and spacing for all forms and navigation elements.
- Ensured all pages are mobile-friendly and visually consistent.

### Navbar
- Moved the "FOSSEE Workshops" title to the left.
- Centered navigation tabs: Home, Statistics, Workshop Status, Propose Workshop, Workshop Types.
- Moved the profile icon and dropdown to the right.
- Cleaned up dropdown menu for user actions.

### Registration Page
- Refactored the registration form to use Bootstrap form groups and full-width fields.
- Added tooltips and clear labels for better usability.
- Ensured all fields are vertically aligned and responsive.

### Login Page
- Improved form layout and error display.
- Restored the "Sign up" link for new users.
- Enhanced button and input styling for clarity.

### Profile Edit Page
- Redesigned the profile edit form with a card layout, clear labels, and improved spacing.
- Kept the update functionality unchanged for seamless user experience.

### Navigation Tabs
- Moved "Workshop Status", "Propose Workshop", and "Workshop Types" tabs out of the profile dropdown and back to the main navigation bar.

### Template Filters
- Added custom template filters (e.g., `add_class`, `has_group`) for improved form field styling and group checks in templates.

### Bug Fixes
- Fixed template errors related to missing filters and incorrect URL names.
- Updated template tag order to resolve Django template syntax errors.

---
For more details on setup and usage, see docs/Getting_Started.md.
