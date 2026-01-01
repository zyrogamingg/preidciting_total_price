import pickle 
import streamlit as st
import pandas as pd 
with open("final_model.pkl","rb") as f:
    final_model = pickle.load(f)

st.markdown("Tax is $1.14 and already included in prices")
item = st.selectbox("Select Item", ["Sandwich", "Coffee", "Cake"])
portion = st.selectbox("select size",["small","medium","large"])
quantity = st.number_input("Quantity", min_value=1, step=1)
location = st.selectbox("Location", ["Takeaway(2$)", "In-store"])
payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Digital Wallet"])
total_spent =0
if portion == "small" and item == "Sandwich":
    total_spent = 4.14
elif portion == "small" and item =="Coffee":
    total_spent=3.14
elif portion == "small" and item == "Cake":
    total_spent=6.14
elif portion == "medium" and item == "Sandwich":
    total_spent = 5.66
elif portion == "medium" and item =="Coffee":
    total_spent=4.74
elif portion == "medium" and item == "Cake":
    total_spent=9.21
elif portion == "large" and item == "Sandwich":
    total_spent = 6.14
elif portion == "large" and item =="Coffee":
    total_spent=5.14
elif portion == "large" and item == "Cake":
    total_spent=11.14


fee = 2 if location == "Takeaway(2$)" else 0



if st.button("predict your total"):
  totall = fee+(total_spent*quantity)
  if totall >= 15:
        totall -= 1.5
  st.write(f"Total price: {totall:.2f}")

    
#host on streamlit cloud
#chatbot page to chat with your data(data we give it)
#kaggle.com (place where we can get csv files)
