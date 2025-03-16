import streamlit as st
import datetime

# Set page configuration
st.set_page_config(page_title="Smart Budgeting Assistant", page_icon="💰", layout="wide")

# Custom styling for aesthetics
st.markdown(
    """
    <style>
        body { background-color: #f5f7fa; }
        .stApp { background-color: #f5f7fa; }
        .css-18e3th9 { padding: 20px; }
        .stButton>button { border-radius: 10px; background-color: #4CAF50; color: white; }
        .stMetric { font-size: 20px; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("---")
st.sidebar.page_link("pages/budgeting_tool.py", label="💰 Budgeting Tool")
st.sidebar.page_link("pages/bill_remainders.py", label="⏰ Bill Reminders")
st.sidebar.page_link("pages/expense_tracker.py", label="💳 Expense Tracker")
st.sidebar.page_link("pages/SIP_and_EMI_calculator.py", label="📊 SIP & EMI Calculator")
st.sidebar.page_link("pages/fanancial_planning.py", label="📈 Financial Planning")

# Main Content
st.title("💰 Smart Budgeting Assistant")
st.markdown("---")

st.header("📌 Welcome to Your Personal Finance Manager")
st.write(
    "Track your expenses, set budgets, and plan your financial goals with AI-driven insights."
)

# Show current date
st.sidebar.markdown(f"📅 Today: {datetime.date.today().strftime('%A, %B %d, %Y')}")
