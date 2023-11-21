import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

locale.setlocale(locale.LC_NUMERIC, 'id_ID')

st.title("View DataBase")

st.write("CRUD Operations:")
# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Menampilkan worksheet Buku Besar
# df = conn.read(
#     worksheet="Bigbooks",
#     ttl="10m",
#     usecols=[0, 1, 2, 3, 4, 5],
#     nrows=10,
# )

#st.dataframe(df)

sql = 'SELECT * FROM Bigbooks;'
data = conn.query(sql = sql)
st.dataframe(data)

# Taking actions based on user input
if st.button("Total Pemasukan"):
    sql = 'SELECT SUM("in") as "Pemasukan" FROM Bigbooks;'
    total_pemasukan = conn.query(sql=sql, ttl=10)  # default ttl=3600 seconds / 60 min
    st.dataframe(total_pemasukan)

if st.button("Total Pengeluaran"):
    sql = 'SELECT SUM("out") as "Pengeluaran" FROM Bigbooks;'
    total_pengeluaran = conn.query(sql=sql, ttl=10)  # default ttl=3600 seconds / 60 min
    st.dataframe(total_pengeluaran)

if st.button("Uang Kas Terakhir"):
    sql = 'SELECT SUM("out") as "Pengeluaran" FROM Bigbooks;'
    total_pengeluaran = conn.query(sql=sql, ttl=10)  # default ttl=3600 seconds / 60 min
    sql = 'SELECT SUM("in") as "Pemasukan" FROM Bigbooks;'
    total_pemasukan = conn.query(sql=sql, ttl=10)  # default ttl=3600 seconds / 60 min
    total_kas = total_pemasukan.values - total_pengeluaran.values
    st.write("Uang kas Terakhir adalah Rp.{} dengan pemasukan {} dan pengeluaran {}".format(locale.format_string("%d", total_kas[0, 0], grouping=True), total_pemasukan.values[0, 0], total_pengeluaran.values[0, 0]))

input1 = st.text_input('Masukan Tahun Awal')
input2 = st.text_input('Masukan Tahun Akhir')

def filter_data(df, min_year, max_year):
    # Menggunakan parameter variabel dalam query
    result = df.query('@min_year <= date <= @max_year')
    return result

if st.button("Hasil Range Tahun"):
    filtered_df = filter_data(data, input1, input2)
    st.dataframe(filtered_df)

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