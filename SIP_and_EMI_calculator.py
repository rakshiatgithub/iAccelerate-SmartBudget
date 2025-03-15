import streamlit as st

st.title("📊 SIP & EMI Calculator")

def calculate_sip(principal, rate, years):
    return principal * ((1 + rate / 100) ** years)

def calculate_emi(principal, rate, tenure):
    r = rate / (12 * 100)
    if r == 0 or tenure == 0:
        return 0
    emi = (principal * r * ((1 + r) ** tenure)) / (((1 + r) ** tenure) - 1)
    return emi

col1, col2 = st.columns(2)
principal = col1.number_input("Principal Amount", min_value=0.0, format="%.2f")
rate = col2.number_input("Annual Interest Rate (%)", min_value=0.0, format="%.2f")
years = col1.number_input("Number of Years", min_value=1, step=1)
tenure = col2.number_input("Loan Tenure (Months)", min_value=1, step=1)

col1, col2 = st.columns(2)
if col1.button("Calculate SIP"):
    st.success(f"💰 Future Investment Value: {calculate_sip(principal, rate, years):,.2f}")
if col2.button("Calculate EMI"):
    st.success(f"📉 Monthly EMI Payment: {calculate_emi(principal, rate, tenure):,.2f}")
