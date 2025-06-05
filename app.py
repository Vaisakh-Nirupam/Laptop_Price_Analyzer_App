# Adding the libraries
import streamlit as st
import pandas as pd

# Full page
st.set_page_config(page_title="LAP", page_icon=r"", layout="wide")

# Adding styles
with open(r"css\Style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Loading the dataset
df = pd.read_csv(r"Dataset\Laptop_Price_Improved.csv")

# Displaying the dataset
st.title("Laptop Price Analyzer!")

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


# with st.form("Specs_Data"):

class Pages:
    # First page
    def page1(self):
        # Get User Name
        name = st.text_input("Enter your Name: ")

        # Select Laptop Company
        company = st.selectbox("Select the Company: ", dit_inputs["Company"], index=0, placeholder="Choose one:")

        # Select Laptop Type
        type = st.selectbox("Select the Product Type: ", dit_inputs["TypeName"], index=0, placeholder="Choose one:")

    # Second page
    def page2(self):
        # Select OS Type
        operating_system = st.selectbox("Select Operating System: ", dit_inputs["OpSys"], index=0, placeholder="Choose one:")
        
        # Select CPU Company
        cpu_company = st.selectbox("Select CPU Company: ", dit_inputs["CPU_Company"], index=0, placeholder="Choose one:")

        # Select Frequency Range
        frequency_categories = {
            "All": "All",
            "Low Frequency (Below 1.8 Ghz)": "Low Frequency",
            "Average Frequency (Below 2.8 Ghz)": "Average Frequency",
            "High Frequency (2.8 & above)": "High Frequency"
        }
        frequency_display = st.selectbox("Select CPU Frequency Category:",list(frequency_categories.keys()),index=0,placeholder="Choose one:")
        frequency_category = frequency_categories[frequency_display]

    # Third page
    def page3(self):
        # Select RAM Range
        ram_categories = {
            "All": "All",
            "Low RAM (Below 4 Gb)": "Low RAM",
            "Average RAM (Below 16 Gb)": "Average RAM",
            "High RAM (16 Gb & above)": "High RAM"
        }
        ram_display = st.selectbox("Select RAM Category:",list(ram_categories.keys()),index=0,placeholder="Choose one:")
        ram_category = ram_categories[ram_display]

        # Select Memory Range
        memory_categories = {
            "All": "All",
            "Low Memory (Below 512 Gb)": "Low Memory",
            "Average Memory (Below 1024 Gb)": "Average Memory",
            "High Memory (1024 Gb & above)": "High Memory"
        }
        memory_display = st.selectbox("Select Memory Category:",list(memory_categories.keys()),index=0,placeholder="Choose one:")
        memory_category = memory_categories[memory_display]

        # Select GPU Company
        gpu_company = st.selectbox("Select GPU Company: ", dit_inputs["GPU_Company"], index=0, placeholder="Choose one:")

    # Fourth page
    def page4(self):
        # Select Screen Type
        dit_inputs["ScreenType"].remove("Touchscreen")
        screen_type = st.selectbox("Select the Screen Type: ", dit_inputs["ScreenType"], index=0, placeholder="Choose one:")

        # Select Touch Screen or not
        touch_screen = st.selectbox("Touch Screen: ", dit_inputs["TouchScreen"], index=0, placeholder="Choose one:")
        
        # Select Price Range
        price_categories = {
            "All": "All",
            "Low Price (Below ₹40,000)": "Low Budget",
            "Average Price (Below ₹70,000)": "Average Budget",
            "High Price (₹70,000 & above)": "High Budget"
        }
        price_display = st.selectbox("Select Price Category:",list(price_categories.keys()),index=0,placeholder="Choose one:")
        price_category = price_categories[price_display]

# Submit button
if st.form_submit_button("Search"):
    # User data collection listed
    user_data = [company, type, operating_system, cpu_company, frequency_category, ram_category, memory_category, gpu_company, screen_type, touch_screen, price_category]

    # Dataset copied
    result = df.copy()
    
    # Search function
    for col,val in zip(required_columns,user_data):
        if val != "All":
            result = result[result[col] == val]
    
    result = result[["Company", "Product", "TypeName", "OpSys", "CPU_Company", "CPU_Type", "Frequency_GHz", "RAM_GB", "Memory", "Total_Memory", "GPU_Company", "GPU_Type", "ScreenResolution", "ScreenType", "TouchScreen", "Inches", "Weight_kg", "Price_Rs"]]

    # Session storing of results
    st.session_state["search_result"] = result

# Search result display
if "search_result" in st.session_state:
    result = st.session_state["search_result"]
    if result.empty:
        st.warning("No laptops match your search criteria.")
        if st.button("Random 5"):
            st.write(df.sample(n=5))
    else:
        st.success("Laptops Based on your Search:")
        st.write(result)