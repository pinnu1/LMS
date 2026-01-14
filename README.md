# 📚 Library Management System (LMS) — Streamlit App

An **Enterprise-style modular Library Management System** built using **Python, Streamlit, Pandas, and Plotly**. This application replicates the logic and workflows of a multi-sheet Excel-based system while providing a modern, interactive web interface.

---

## 🚀 Features

### 🔐 Authentication
* **Dual-Role Access:** Separate login flows for **Admin** and **User**.
* **Session Management:** Secure routing using `st.session_state`.

### 📖 Inventory & Membership
* **Master Book List:** Add, view, and update book availability.
* **Membership Management:** Track active/inactive memberships and add new members.

### 🔄 Book Workflows
* **Active Issues:** Real-time tracking of books currently checked out.
* **Overdue Returns:** Automatic identification of overdue books for admin monitoring.
* **Smart Transactions:** Search by Title, Author, or Category with a streamlined issue/confirmation flow.

### 💰 Financials
* **Fine Calculation:** Automated logic based on return dates.
* **Fine Ledger:** Record and track fine payments seamlessly.

### 📊 Analytics Dashboard
* **KPI Summary:** Total Books, Active Issues, Memberships, and Revenue.
* **Data Visualization:** Interactive Plotly charts showing book distribution by category.

---

## 🏗️ Project Structure

```text
library_management_system/
│
├── app.py                   # Main entry point
├── requirements.txt         # Project dependencies
├── README.md                # Documentation
│
├── assets/                  # UI screenshots and images
│   ├── excel_reports.png
│   ├── excel_memberships.png
│   └── excel_user_management.png
│
├── data/                    # Data handling logic
│   └── dummy_loader.py
│
├── modules/                 # Core business logic
│   ├── auth.py
│   ├── db.py
│   ├── utils.py
│   ├── navigation.py
│   └── transactions_flow.py
│
└── pages/                   # Modular UI pages
    ├── reports_page.py
    ├── books_page.py
    ├── memberships_page.py
    ├── active_issues_page.py
    ├── overdue_returns_page.py
    ├── transactions_page.py
    ├── issue_requests_page.py
    ├── pay_fine_page.py
    ├── confirmation_page.py
    ├── user_management_page.py
    └── reference_images_page.py.

⚙️ Installation & Setup
1️⃣ Clone the Repository
Bash

git clone <your-github-repo-url>
cd library_management_system
2️⃣ Set Up Virtual Environment
Bash

# Create environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
3️⃣ Install Dependencies
Bash

pip install -r requirements.txt

Run the Application
Bash

python -m streamlit run app.py
