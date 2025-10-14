import streamlit as st
import uuid
import json
import os

from utils.persistence import save_data, load_data
from config import FILES, DATA_DIR

DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

FILES = {
    "budget": os.path.join(DATA_DIR, "budget.json"),
}

if "budget_store" not in st.session_state:
    st.session_state.budget_store = load_data(FILES["budget"], {"incomes": [], "budgets": [], "expenses": [], "payments": []})

def budget_page():
    st.title("💰 Budget Tracker")
    tabs = st.tabs(["💵 Log Income", "📊 Budget Categories", "📉 Log Expenses", "📋 Summary Sheet"])

    with tabs[0]:
        st.subheader("💵 Add Income")
        with st.form("income_form"):
            source = st.text_input("Source name")
            amount = st.number_input("Amount", min_value=0.0, format="%f")
            submit = st.form_submit_button("➕ Add Income")
            if submit and source and amount:
                st.session_state.budget_store.setdefault("incomes", []).append({"id": str(uuid.uuid4()), "source": source, "amount": float(amount)})
                save_data(FILES["budget"], st.session_state.budget_store)
                st.success(f"Added income: {source} — ₦{amount:,.2f}")

        if st.session_state.budget_store.get("incomes"):
            st.markdown("**Your incomes**")
            for inc in st.session_state.budget_store["incomes"]:
                st.write(f"• {inc['source']} — ₦{inc['amount']:,.2f}")

    with tabs[1]:
        st.subheader("📊 Budget Categories (Planned Allocations)")
        with st.form("budget_cat_form"):
            cat = st.text_input("Category name")
            amt = st.number_input("Amount", min_value=0.0, format="%f")
            color = st.color_picker("Color tag", value="#b3e5fc")
            add = st.form_submit_button("➕ Add Category")
            if add and cat and amt:
                st.session_state.budget_store.setdefault("budgets", []).append({"id": str(uuid.uuid4()), "category": cat, "amount": float(amt), "color": color})
                save_data(FILES["budget"], st.session_state.budget_store)
                st.success(f"Added category: {cat} — ₦{amt:,.2f}")

        if st.session_state.budget_store.get("budgets"):
            for b in st.session_state.budget_store["budgets"]:
                st.markdown(f"- {b['category']} — ₦{b['amount']:,.2f}")

    with tabs[2]:
        st.subheader("📉 Log Expense")
        with st.form("expense_form"):
            name = st.text_input("Expense name")
            amt = st.number_input("Amount", min_value=0.0, format="%f")
            color = st.color_picker("Color tag", value="#ffccbc")
            submit = st.form_submit_button("➕ Add Expense")
            if submit and name and amt:
                st.session_state.budget_store.setdefault("expenses", []).append({
                    "id": str(uuid.uuid4()),
                    "expense": name,
                    "amount": float(amt),
                    "color": color,
                    "paid": False
                })
                save_data(FILES["budget"], st.session_state.budget_store)
                st.success(f"Logged expense: {name} — ₦{amt:,.2f}")

    with tabs[3]:
        st.subheader("📋 Financial Summary")
        incomes = st.session_state.budget_store.get("incomes", [])
        expenses = st.session_state.budget_store.get("expenses", [])
        total_income = sum(i["amount"] for i in incomes)
        total_exp = sum(e["amount"] for e in expenses)
        net = total_income - total_exp

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("💰 Total Income", f"₦{total_income:,.2f}")
        c2.metric("📉 Total Expenses", f"₦{total_exp:,.2f}")
        c3.metric("💼 Net Balance", f"₦{net:,.2f}")

        if expenses:
            st.markdown("### 🥧 Expense Breakdown")
            labels = [e["expense"] for e in expenses]
            sizes = [e["amount"] for e in expenses]
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
        else:
            st.info("No expenses yet — add some to see a breakdown.")

budget_page()