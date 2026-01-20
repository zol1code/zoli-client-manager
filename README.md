#Zoli Client Manager | Freelance Suite

A professional business management dashboard designed for freelancers and small digital agencies. This project is a core product of **Zoli Code**, focused on financial visibility and client management.

---

Purpose
Managing freelance projects requires more than just coding; it requires business intelligence. This tool was developed to solve:
- **Financial Tracking:** Real-time visibility of total revenue.
- **Cash Flow Management:** Clear distinction between "Paid" and "Pending" services.
- **Tax Automation:** A Python-based backend logic to simulate Irish tax provisions (VAT/Income Tax).

---

Tech Stack

### Frontend (User Interface)
- **React.js:** Used for a reactive UI and state management (`useState`).
- **Tailwind CSS:** Modern "Emerald & Amber" theme, providing a mobile-first, responsive design.
- **FontAwesome:** For professional iconography.

### Backend (Business Logic)
- **Python 3:** Handles heavy data processing and financial reporting.
- **Modules:** `datetime` for timestamped reports and custom math logic for tax estimation.

---

Engineering Decisions
- **Hybrid Architecture:** Separation of concerns between the **React Frontend** (User Interaction) and **Python Backend Logic** (Data Processing).
- **Localization:** Configured for the **Irish Market** (€ currency and 20% Income Tax simulation).
- **Mobile-First Dev:** Entirely developed using mobile environments (iOS), demonstrating extreme adaptability and technical agility.

---

Features
- **Dynamic Dashboard:** Add new services and see the "Total Revenue" update instantly.
- **Status Badges:** Visual indicators for project health.
- **Financial Reporting:** A Python script (`generate_report.py`) that processes raw data into a clean business summary.

---

How to Run

### Web Dashboard
Simply open the `index.html` file in any browser or visit the live link:
> **[INSERT YOUR GITHUB PAGES LINK HERE]**

### Python Report
To see the business intelligence logic in action, run:
```bash
python generate_report.py


