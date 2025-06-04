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
company = st.selectbox("Select the Company: ", companies)

# Select Laptop Type
types = list(df["TypeName"].unique())
types.sort()
types.insert(0, "All")
type = st.selectbox("Select the Product Type: ", types)

# Select Screen Type
screen_types = list(df["ScreenType"].unique())
screen_types.sort()
screen_types.insert(0, "All")
screen_type = st.selectbox("Select the Screen Type: ", screen_types)

# Select Touch Screen or not
touch_screens = list(df["TouchScreen"].unique())
touch_screens.sort()
touch_screens.insert(0, "All")
touch_screen = st.selectbox("Touch Screen: ", touch_screens)

# Select CPU Company
cpu_companies = list(df["CPU_Company"].unique())
cpu_companies.sort()
cpu_companies.insert(0, "All")
cpu_company = st.selectbox("Select CPU Company: ", cpu_companies)

# Select Frequency Range
frequency_categories = list(df["Frequency_Category"].unique())
frequency_categories.insert(0, "All")
frequency_category = st.selectbox("Select Frequency Category: ", frequency_categories)

# Select RAM Range
ram_categories = list(df["RAM_Category"].unique())
ram_categories.insert(0, "All")
ram_category = st.selectbox("Select RAM Category: ", ram_categories)

# Select Memory Range
memory_categories = list(df["Memory_Category"].unique())
memory_categories.insert(0, "All")
memory_category = st.selectbox("Select Memory Category: ", memory_categories)

# Select GPU Company
gpu_companies = list(df["GPU_Company"].unique())
gpu_companies.sort()
gpu_companies.insert(0, "All")
gpu_company = st.selectbox("Select GPU Company: ", gpu_companies)

# Select OS Type
operating_systems = list(df["OpSys"].unique())
operating_systems.sort()
operating_systems.insert(0, "All")
operating_system = st.selectbox("Select Operating System: ", operating_systems)

# Select Price Range
price_categories = list(df["Price_Category"].unique())
price_categories.insert(0, "All")
price_category = st.selectbox("Select Price Category: ", price_categories)