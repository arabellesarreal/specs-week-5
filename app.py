import streamlit as st
import pandas as pd

df = pd.read_csv("~data-proj-5\\data-proj-5\\starter\\supermarket.csv")

st.title("Super Market Stats")

st.subheader("Top Ten Performing Stores")

topTenStores = df.sort_values(by=['store_sales'], ascending = False).head(10)
st.bar_chart(data = topTenStores, x = 'store_id' , y = 'store_sales')

st.subheader("Top Five Performing Areas")

topTenAreas = df.groupby('store_area')['store_sales'].sum().sort_values(ascending = False).head(5)
tenAreas = topTenAreas.to_frame().reset_index()
st.bar_chart(data = tenAreas, x = 'store_area', y = 'store_sales')

st.subheader("Average Daily Customer Count")
avgDailyCust = df['daily_customer_count'].mean()
st.markdown(":blue[" + str(avgDailyCust) + "]")

st.subheader("Total Sales")
totalSales = df['store_sales'].sum()
st.markdown(":green[" + str(totalSales) + "]")