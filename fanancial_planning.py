import streamlit as st

st.title("📈 Financial Planning")

goal_amount = st.number_input("Enter Savings Goal", min_value=0.0, format="%.2f")

total_expenses = sum(exp["amount"] for exp in st.session_state.expenses) if 'expenses' in st.session_state else 0
savings_needed = max(0, goal_amount - total_expenses)

st.success(f"You need to save {savings_needed} more to reach your goal.")
