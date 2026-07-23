import streamlit as st

st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")

price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
vat = price * 0.07

net_price = price - vat
vat = price * 0.07
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()

st.write("นางสาวรุ้งลาวัลย์ ปัญญาบาล เลขที่ 3  ม.4/15")
