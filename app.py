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

# Get User Name
name = st.text_input("Enter your Name: ")

# Select Laptop Company
companies = list(df["Company"].unique())
companies.sort()
companies.insert(0, "All")
company = st.selectbox("Select the Company: ", companies, index=0, placeholder="Choose one:")

# Select Laptop Type
types = list(df["TypeName"].unique())
types.sort()
types.insert(0, "All")
type = st.selectbox("Select the Product Type: ", types, index=0, placeholder="Choose one:")

# Select Screen Type
screen_types = list(df["ScreenType"][df["ScreenType"]!="Touchscreen"].unique())
screen_types.sort()
screen_types.insert(0, "All")
screen_type = st.selectbox("Select the Screen Type: ", screen_types, index=0, placeholder="Choose one:")

# Select Touch Screen or not
touch_screens = list(df["TouchScreen"].unique())
touch_screens.sort()
touch_screens.insert(0, "All")
touch_screen = st.selectbox("Touch Screen: ", touch_screens, index=0, placeholder="Choose one:")

# Select CPU Company
cpu_companies = list(df["CPU_Company"].unique())
cpu_companies.sort()
cpu_companies.insert(0, "All")
cpu_company = st.selectbox("Select CPU Company: ", cpu_companies, index=0, placeholder="Choose one:")

# Select Frequency Range
frequency_categories = ["All", 
                        "Low Frequency (Below 1.8 Ghz)", 
                        "Average Frequency (Below 2.8 Ghz)", 
                        "High Frequency (2.8 & above)"]
frequency_category = st.selectbox("Select CPU Frequency Category: ", frequency_categories, index=0, placeholder="Choose one:")

# Select RAM Range
ram_categories = ["All",
                  "Low RAM (Below 4 Gb)",
                  "Average RAM (Below 16 Gb)",
                  "High RAM (16 Gb & above)"]
ram_category = st.selectbox("Select RAM Category: ", ram_categories, index=0, placeholder="Choose one:")

# Select Memory Range
memory_categories = ["All",
                     "Low Memory (Below 512 Gb)",
                     "Average Memory (Below 1024 Gb)",
                     "High Memory (1024 Gb & above)"]
memory_category = st.selectbox("Select Memory Category: ", memory_categories, index=0, placeholder="Choose one:")

# Select GPU Company
gpu_companies = list(df["GPU_Company"].unique())
gpu_companies.sort()
gpu_companies.insert(0, "All")
gpu_company = st.selectbox("Select GPU Company: ", gpu_companies, index=0, placeholder="Choose one:")

# Select OS Type
operating_systems = list(df["OpSys"].unique())
operating_systems.sort()
operating_systems.insert(0, "All")
operating_system = st.selectbox("Select Operating System: ", operating_systems, index=0, placeholder="Choose one:")

# Select Price Range
price_categories = ["All",
                     "Low Price (Below ₹40,000)",
                     "Average Price (Below ₹70,000)",
                     "High Price (₹70,000 & above)"]
price_category = st.selectbox("Select Price Category: ", price_categories, index=0, placeholder="Choose one:")