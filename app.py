# Adding the libraries
import streamlit as st
import pandas as pd

# Full page
st.set_page_config(page_title="LAP", page_icon=r"", layout="wide")

# Loading the dataset
df = pd.read_csv(r"Dataset\Laptop_Price_Improved.csv")

# Displaying the dataset
st.title("Laptop Price Analyzer!")
st.write(df.head())

# Dataset Columns:
all_columns = ["Company", "Product", "TypeName", "Inches", "ScreenResolution", "ScreenType", "TouchScreen", "CPU_Company", "CPU_Type", "Frequency_GHz", "Frequency_Category", "RAM_GB", "RAM_Category", "Memory", "Total_Memory", "Memory_Category", "GPU_Company", "GPU_Type", "OpSys", "Weight_kg", "Price_Rs", "Price_Category"]

# Useable Columns
required_columns = ["Company", "TypeName", "ScreenType", "TouchScreen", "CPU_Company", "Frequency_Category", "RAM_Category", "Memory_Category", "GPU_Company", "OpSys", "Price_Category"]

# User Input Collection
loopable_columns = ["Company", "TypeName", "ScreenType", "TouchScreen", "CPU_Company", "GPU_Company", "OpSys"]
dit_inputs = {}
for i in loopable_columns:
    dit_inputs[i] = list(df[i].unique())
    dit_inputs[i].sort()
    dit_inputs[i].insert(0, "All")


with st.form("Specs_Data"):

    # Get User Name
    name = st.text_input("Enter your Name: ")

    # Select Laptop Company
    company = st.selectbox("Select the Company: ", dit_inputs["Company"], index=0, placeholder="Choose one:")

    # Select Laptop Type
    type = st.selectbox("Select the Product Type: ", dit_inputs["TypeName"], index=0, placeholder="Choose one:")

    # Select Screen Type
    dit_inputs["ScreenType"].remove("Touchscreen")
    screen_type = st.selectbox("Select the Screen Type: ", dit_inputs["ScreenType"], index=0, placeholder="Choose one:")

    # Select Touch Screen or not
    touch_screen = st.selectbox("Touch Screen: ", dit_inputs["TouchScreen"], index=0, placeholder="Choose one:")

    # Select CPU Company
    cpu_company = st.selectbox("Select CPU Company: ", dit_inputs["CPU_Company"], index=0, placeholder="Choose one:")

    # Select Frequency Range
    frequency_categories = ["All", "Low Frequency (Below 1.8 Ghz)", "Average Frequency (Below 2.8 Ghz)", "High Frequency (2.8 & above)"]
    frequency_category = st.selectbox("Select CPU Frequency Category: ", frequency_categories, index=0, placeholder="Choose one:")

    # Select RAM Range
    ram_categories = ["All","Low RAM (Below 4 Gb)", "Average RAM (Below 16 Gb)","High RAM (16 Gb & above)"]
    ram_category = st.selectbox("Select RAM Category: ", ram_categories, index=0, placeholder="Choose one:")

    # Select Memory Range
    memory_categories = ["All", "Low Memory (Below 512 Gb)", "Average Memory (Below 1024 Gb)", "High Memory (1024 Gb & above)"]
    memory_category = st.selectbox("Select Memory Category: ", memory_categories, index=0, placeholder="Choose one:")

    # Select GPU Company
    gpu_company = st.selectbox("Select GPU Company: ", dit_inputs["GPU_Company"], index=0, placeholder="Choose one:")

    # Select OS Type
    operating_system = st.selectbox("Select Operating System: ", dit_inputs["OpSys"], index=0, placeholder="Choose one:")

    # Select Price Range
    price_categories = ["All", "Low Price (Below ₹40,000)", "Average Price (Below ₹70,000)", "High Price (₹70,000 & above)"]
    price_category = st.selectbox("Select Price Category: ", price_categories, index=0, placeholder="Choose one:")

    # Submit button
    if st.form_submit_button("Submit"):
        # User data collection listed
        user_data = [company, type, screen_type, touch_screen, cpu_company, frequency_category, ram_category, memory_category, gpu_company, operating_system, price_category]
