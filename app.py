# Adding the libraries
import streamlit as st
import pandas as pd

# Full page
st.set_page_config(page_title="LPA", page_icon=r"Images\Laptop Price Analyzer Logo.png", layout="wide")

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

# Session creation function
def session_selectbox(label, options, key, placeholder="Choose one:"):
    # If the current session value is not in options, reset to first option
    if key not in st.session_state or st.session_state[key] not in options:
        st.session_state[key] = options[0]
    selected = st.selectbox(label, options, index=options.index(st.session_state[key]), placeholder=placeholder)
    st.session_state[key] = selected
    return selected

class Pages:
    # Home page
    def home():
        pass

    # First page
    def page1(self):
        # Get User Name
        name = st.text_input("Enter your Name: ")

        # Select Laptop Company
        company = session_selectbox("Select the Company:", dit_inputs["Company"], "Company")

        # Select Laptop Type
        type = session_selectbox("Select the Product Type:", dit_inputs["TypeName"], "TypeName")

    # Second page
    def page2(self):
        # Select OS Type
        operating_system = session_selectbox("Select Operating System:", dit_inputs["OpSys"], "OpSys")
        
        # Select CPU Company
        cpu_company = session_selectbox("Select CPU Company:", dit_inputs["CPU_Company"], "CPU_Company")

        # Select Frequency Range
        frequency_categories = {
            "All": "All",
            "Low Frequency (Below 1.8 Ghz)": "Low Frequency",
            "Average Frequency (Below 2.8 Ghz)": "Average Frequency",
            "High Frequency (2.8 & above)": "High Frequency"
        }
        frequency_display = session_selectbox("Select CPU Frequency Category:", list(frequency_categories.keys()), "Frequency_Category")
        st.session_state["Frequency_Category"] = frequency_categories[frequency_display]
        

    # Third page
    def page3(self):
        # Select RAM Range
        ram_categories = {
            "All": "All",
            "Low RAM (Below 4 Gb)": "Low RAM",
            "Average RAM (Below 16 Gb)": "Average RAM",
            "High RAM (16 Gb & above)": "High RAM"
        }
        ram_display = session_selectbox("Select RAM Category:", list(ram_categories.keys()), "RAM_Category")
        st.session_state["RAM_Category"] = ram_categories[ram_display] 

        # Select Memory Range
        memory_categories = {
            "All": "All",
            "Low Memory (Below 512 Gb)": "Low Memory",
            "Average Memory (Below 1024 Gb)": "Average Memory",
            "High Memory (1024 Gb & above)": "High Memory"
        }
        memory_display = session_selectbox("Select Memory Category:",list(memory_categories.keys()), "Memory_Category")
        st.session_state["Memory_Category"] = memory_categories[memory_display]

        # Select GPU Company
        gpu_company = session_selectbox("Select GPU Company: ", dit_inputs["GPU_Company"], "GPU_Company")

    # Fourth page
    def page4(self):
        # Select Screen Type
        dit_inputs["ScreenType"].remove("Touchscreen")
        screen_type = session_selectbox("Select the Screen Type: ", dit_inputs["ScreenType"], "ScreenType")

        # Select Touch Screen or not
        touch_screen = session_selectbox("Touch Screen: ", dit_inputs["TouchScreen"], "TouchScreen")
        
        # Select Price Range
        price_categories = {
            "All": "All",
            "Low Price (Below ₹40,000)": "Low Budget",
            "Average Price (Below ₹70,000)": "Average Budget",
            "High Price (₹70,000 & above)": "High Budget"
        }
        price_display = session_selectbox("Select Price Category:",list(price_categories.keys()), "Price_Category")
        st.session_state["Price_Category"] = price_categories[price_display]

        # Search button
        if st.button("Search"):
            # User data collection listed
            user_data = [st.session_state["Company"], st.session_state["TypeName"], st.session_state["ScreenType"], st.session_state["TouchScreen"], st.session_state["CPU_Company"], st.session_state["Frequency_Category"], st.session_state["RAM_Category"], st.session_state["Memory_Category"], st.session_state["GPU_Company"], st.session_state["OpSys"], st.session_state["Price_Category"]]

            # Dataset copied
            result = df.copy()
            
            # Search function
            for col,val in zip(required_columns,user_data):
                if val != "All":
                    result = result[result[col] == val]
            
            result = result[["Company", "Product", "TypeName", "OpSys", "CPU_Company", "CPU_Type", "Frequency_GHz", "RAM_GB", "Memory", "Total_Memory", "GPU_Company", "GPU_Type", "ScreenResolution", "ScreenType", "TouchScreen", "Inches", "Weight_kg", "Price_Rs"]]

            # Session storing of results
            st.session_state["search_result"] = result

# Calling Pages
page_calls = Pages()
# page_calls.page1()
# page_calls.page2()
# page_calls.page3()
# page_calls.page4()

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