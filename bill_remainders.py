import streamlit as st
import datetime
import pandas as pd

st.title("⏰ Bill Reminders")

if 'reminders' not in st.session_state:
    st.session_state.reminders = []

bill_name = st.text_input("Enter Bill Name")
bill_date = st.date_input("Select Due Date", min_value=datetime.date.today())

if st.button("Set Reminder"):
    if bill_name:
        st.session_state.reminders.append({"bill": bill_name, "due_date": bill_date})
        st.success(f"Reminder set for {bill_name} on {bill_date}")

if st.session_state.reminders:
    st.write("### Upcoming Bills")
    st.dataframe(pd.DataFrame(st.session_state.reminders))
