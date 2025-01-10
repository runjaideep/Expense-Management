import streamlit as st
import pandas as pd

from datetime import datetime
import requests

API_URL = "http://localhost:8000"

st.title("Expense Management System")

tab1, tab2, tab3 = st.tabs(["Add/Update Expenses","Category Analytics","Monthly Analytics"])

with tab1:
    selected_dt = st.date_input("Enter the date", datetime(2024,8,1), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_dt}")
    if response.status_code == 200:
        existing_expenses = response.json()
        st.write(existing_expenses)
    else:
        st.error("Something went wrong")
        existing_expenses = []

    categories = ["Rent","Food","Shopping","Entertainment","Other"]

    with st.form(key="Expense Form"):
        expenses = []
        for i in range(5):

            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1,col2,col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount",min_value=0.0, step = 1.0, value = amount, key=f"amount_{i}",label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category",options=categories, index = categories.index(category), key=f"category_{i}",label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="notes",value=notes,key=f"notes_{i}",label_visibility="collapsed")

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input,
            })

        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount']>0]
            response = requests.post(f"{API_URL}/expenses/{selected_dt}",json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expense added")
            else:
                st.error("Failed to add expense")

with tab2:
    st.title("Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        start_dt = st.date_input("Enter the start date", datetime(2020, 8, 1))
    with col2:
        end_dt = st.date_input("Enter the end date", datetime(2024,8,10))

    if st.button("Generate Analysis"):
        payload = {
            "start_date": start_dt.strftime("%Y-%m-%d"),
            "end_date": end_dt.strftime("%Y-%m-%d"),
        }

        response = requests.post(f"{API_URL}/analytics/category",json=payload)
        response = response.json()
        #st.write(response)
        data = {
            "Category": list(response.keys()),
            "Total":[response[category]["total"] for category in response],
            "Percentage":[response[category]["percentage"] for category in response]
        }
        df = pd.DataFrame(data)
        df_sorted = df.sort_values("Percentage",ascending=False)
        st.title("Expense Analysis")
        st.bar_chart(df_sorted.set_index("Category")['Percentage'])
        df_sorted['Total']=df_sorted['Total'].map("{:.2f}".format)
        df_sorted['Percentage'] = df_sorted['Percentage'].map("{:.2f}".format)
        st.table(df_sorted)


with tab3:
    st.title("Monthly Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        start_dt = st.date_input("Enter the start date", datetime(1990, 1, 1))
    with col2:
        end_dt = st.date_input("Enter the end date", datetime(1990,12,31))

    if st.button("Generate Monthly Analysis"):
        payload = {
            "start_date": start_dt.strftime("%Y-%m-%d"),
            "end_date": end_dt.strftime("%Y-%m-%d"),
        }

        response = requests.post(f"{API_URL}/analytics/month",json=payload)
        response = response.json()
        #st.write(response)
        data = {
            "Month": list(response.keys()),
            "Total":[response[month]["total"] for month in response],
            "Percentage":[response[month]["percentage"] for month in response]
        }
        df = pd.DataFrame(data)
        df_sorted = df.sort_values("Month",ascending=True)
        st.title("Monthly Expense Analysis")
        st.bar_chart(df_sorted.set_index("Month")['Percentage'])
        df_sorted['Total']=df_sorted['Total'].map("{:.2f}".format)
        df_sorted['Percentage'] = df_sorted['Percentage'].map("{:.2f}".format)
        st.table(df_sorted)
