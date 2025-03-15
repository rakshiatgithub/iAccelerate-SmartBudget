import streamlit as st

st.title("💰 Budgeting Tool")

if 'budget' not in st.session_state:
    st.session_state.budget = 0

st.session_state.budget = st.number_input("Set Monthly Budget", min_value=0.0, format="%.2f")

total_expenses = sum(exp["amount"] for exp in st.session_state.expenses) if 'expenses' in st.session_state else 0

st.metric(label="💸 Current Budget", value=st.session_state.budget)
st.metric(label="📉 Total Expenses", value=total_expenses)

if total_expenses > st.session_state.budget:
    st.warning("⚠️ You have exceeded your budget!")
