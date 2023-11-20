import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.title("View DataBase")

st.write("CRUD Operations:")
# Establishing a Google Sheets connection
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read(
    worksheet="Buku Besar",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)

st.dataframe(df)

# Taking actions based on user input
if st.button("New Worksheet"):
    conn.create(worksheet="Orders", data=orders)
    st.success("Worksheet Created 🎉")

if st.button("Calculate Total Orders Sum"):
    sql = 'SELECT SUM("TotalPrice") as "TotalOrdersPrice" FROM Orders;'
    total_orders = conn.query(sql=sql, ttl=10)  # default ttl=3600 seconds / 60 min
    st.dataframe(total_orders)

if st.button("Update Worksheet"):
    conn.update(worksheet="Orders", data=updated_orders)
    st.success("Worksheet Updated 🤓")

if st.button("Clear Worksheet"):
    conn.clear(worksheet="Orders")
    st.success("Worksheet Cleared 🧹")