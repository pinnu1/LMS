import streamlit as st

from data.dummy_loader import load_dummy_data
from modules.db import MockDatabase
from modules.auth import admin_login, user_login
from modules.navigation import sidebar_excel_navigation

# Pages
from modules.pages.reports_page import reports_page
from modules.pages.books_page import books_master_page
from modules.pages.memberships_page import memberships_master_page
from modules.pages.active_issues_page import active_issues_page
from modules.pages.overdue_returns_page import overdue_returns_page
from modules.pages.reference_images_page import reference_images_page

from modules.pages.transactions_page import transactions_page
from modules.pages.issue_requests_page import issue_requests_page
from modules.pages.pay_fine_page import pay_fine_page
from modules.pages.confirmation_page import confirmation_page
from modules.pages.user_management_page import user_management_page


# -----------------------------------------------------------
# Streamlit Config
# -----------------------------------------------------------
st.set_page_config(page_title="Library Management System", layout="wide")


# -----------------------------------------------------------
# Init Session State
# -----------------------------------------------------------
def init_state():
    if "page" not in st.session_state:
        st.session_state["page"] = "select_login"

    if "auth_role" not in st.session_state:
        st.session_state["auth_role"] = None

    if "user" not in st.session_state:
        st.session_state["user"] = None

    # Init DB once
    if "db" not in st.session_state:
        books, memberships, issues, fines = load_dummy_data()
        st.session_state["db"] = MockDatabase(books, memberships, issues, fines)


# -----------------------------------------------------------
# App Router
# -----------------------------------------------------------
def main():
    init_state()
    db = st.session_state["db"]
    page = st.session_state["page"]
    role = st.session_state.get("auth_role")

    # ---------------------- LOGIN PAGE ----------------------
    if page == "select_login":
        st.title("📖 Library Management System")
        st.caption("Enterprise Modular Streamlit App (Excel Flow Based)")

        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                admin_login()

        with col2:
            with st.container(border=True):
                user_login()

        return  # stop here (no sidebar navigation until login)

    # ---------------------- AUTH CHECK ----------------------
    if not role:
        st.session_state["page"] = "select_login"
        st.rerun()

    # ---------------------- SIDEBAR MENU --------------------
    sidebar_excel_navigation()

    # ---------------------- ROUTING -------------------------
    if page in ["home_admin", "home_user", "reports"]:
        reports_page(db)

    elif page == "books_master":
        books_master_page(db)

    elif page == "movies_master":
        st.title("🎬 Master List of Movies")
        st.info("This module is not implemented yet. (Placeholder)")

    elif page == "memberships_master":
        memberships_master_page(db)

    elif page == "active_issues":
        active_issues_page(db)

    elif page == "overdue_returns":
        overdue_returns_page(db)

    elif page == "transactions":
        transactions_page(db)

    elif page == "issue_requests":
        issue_requests_page(db)

    elif page == "pay_fine":
        pay_fine_page(db)

    elif page == "confirmation":
        confirmation_page()

    elif page == "user_management":
        # optional: restrict only for admin
        if role != "admin":
            st.error("Unauthorized: User Management is only for Admin.")
        else:
            user_management_page()

    elif page == "reference_images":
        reference_images_page()

    else:
        st.warning("⚠️ Page not implemented or invalid route")
        st.write("Current page:", page)


# -----------------------------------------------------------
# Run
# -----------------------------------------------------------
if __name__ == "__main__":
    main()
