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
st.image("Images\LPA Title.png")

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

# User name session
if "name" not in st.session_state:
    st.session_state["name"] = ""

# Session creation function
def session_selectbox(label, options, key, placeholder="Choose one:"):
    if key not in st.session_state or st.session_state[key] not in options:
        st.session_state[key] = options[0]
    selected = st.selectbox(label, options, index=options.index(st.session_state[key]), placeholder=placeholder)
    st.session_state[key] = selected
    return selected

class Pages:
    # Home page
    def home(self):
        img.image("Images\Lap1.jpg")

        with intro:
            st.title("Welcome")
            st.write("to the **Laptop Price Analyzer!** Whether you're a student, gamer, or working professional, our intelligent filter system helps you discover the perfect laptop based on your needs — even if you’re not a tech expert!")
            st.write("✔ Easily compare laptops by brand, specs, and price")
            st.write("✔ Understand key features like CPU, RAM, and GPU without confusion")
            st.write("✔ Save time and money by finding what truly suits you")

            start = st.button("Start Exploring", key="start")

            if start:
                st.session_state.select = "Page 1"
                st.rerun()

    # First page
    def page1(self):
        img.image("Images\Lap2.jpg")

        with intro:
            # Get User Name
            st.session_state.name = st.text_input("Enter your Name:", value=st.session_state.name)

            # Select Laptop Company
            company = session_selectbox("Select the Company:", dit_inputs["Company"], "Company")

            # Select Laptop Type
            type = session_selectbox("Select the Product Type:", dit_inputs["TypeName"], "TypeName")

            # Buttons layout
            btn_back, btn_next, err, b = st.columns([1.5, 1.5, 4.1, 3], vertical_alignment="top")

            back_clicked = btn_back.button("Back", key="page1_back")
            next_clicked = btn_next.button("Next", key="page1_next")

            if back_clicked:
                st.session_state.select = "Home"
                st.rerun()

            if next_clicked:
                if (not st.session_state.name):
                    err.error("Please Fill your Name!")
                else:
                    st.session_state.select = "Page 2"
                    st.rerun()

    # Second page
    def page2(self):
        img.image("Images\Lap3.jpg")

        with intro:
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

            # Buttons layout inside intro column
            btn_back, btn_next, err, b = st.columns([1.5, 1.5, 4, 3], vertical_alignment="top")

            back_clicked = btn_back.button("Back", key="page2_back")
            next_clicked = btn_next.button("Next", key="page2_next")

            if back_clicked:
                st.session_state.select = "Page 1"
                st.rerun()

            if next_clicked:
                st.session_state.select = "Page 3"
                st.rerun()

    # Third page
    def page3(self):
        img.image("Images\Lap4.jpg")

        with intro:
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
            memory_display = session_selectbox("Select Memory Category:", list(memory_categories.keys()), "Memory_Category")
            st.session_state["Memory_Category"] = memory_categories[memory_display]

            # Select GPU Company
            gpu_company = session_selectbox("Select GPU Company: ", dit_inputs["GPU_Company"], "GPU_Company")

            # Buttons for navigation
            btn_back, btn_next, err, b = st.columns([1.5, 1.5, 4, 3], vertical_alignment="top")

            back_clicked = btn_back.button("Back", key="page3_back")
            next_clicked = btn_next.button("Next", key="page3_next")

            if back_clicked:
                st.session_state.select = "Page 2"
                st.rerun()

            if next_clicked:
                st.session_state.select = "Page 4"
                st.rerun()

    # Fourth page
    def page4(self):
        img.image("Images\Lap5.jpg")

        with intro:
            # Select Screen Type
            if "Touchscreen" in dit_inputs["ScreenType"]:
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
            price_display = session_selectbox("Select Price Category:", list(price_categories.keys()), "Price_Category")
            st.session_state["Price_Category"] = price_categories[price_display]

            # Navigation + Search
            btn_back, btn_search, err, b = st.columns([1.5, 1.8, 4, 3], vertical_alignment="top")

            back_clicked = btn_back.button("Back", key="page4_back")
            search_clicked = btn_search.button("Search", key="search_btn")

            if back_clicked:
                st.session_state.select = "Page 3"
                st.rerun()

            if search_clicked:
                st.session_state.select = "Result"
                st.rerun()

    # Result page
    def result(self):

        # Collect user data
        user_data = [st.session_state["Company"], st.session_state["TypeName"], st.session_state["ScreenType"], st.session_state["TouchScreen"], st.session_state["CPU_Company"], st.session_state["Frequency_Category"], st.session_state["RAM_Category"], st.session_state["Memory_Category"], st.session_state["GPU_Company"], st.session_state["OpSys"], st.session_state["Price_Category"]]

        # Dataset copied
        result = df.copy()

        # Apply filters
        for col, val in zip(required_columns, user_data):
            if val != "All":
                result = result[result[col] == val]

        # Reduce columns for display
        result = result[["Company", "Product", "TypeName", "OpSys", "CPU_Company", "CPU_Type", "Frequency_GHz", "RAM_GB", "Memory", "Total_Memory", "GPU_Company", "GPU_Type", "ScreenResolution", "ScreenType", "TouchScreen", "Inches", "Weight_kg", "Price_Rs"]]

        # Display results
        b1,txt1,b2 = st.columns([1,10,4.7])
        name = st.session_state["name"]
        txt1.title(f"Hello {name}!")

        if result.empty:
            b1, txt2, btn1, btn2, btn3, b2 = st.columns([1, 10, 1.2, 1.2, 1.8, 0.5], vertical_alignment="center")

            txt2.subheader("No laptops match your search criteria.\nHere's a list of 5 random laptops for your reference:")

            # Random 5 logic
            if "random_laptops" not in st.session_state:
                st.session_state["random_laptops"] = df.sample(n=5)

            # Handle button clicks
            if btn1.button("Back", key="result_back"):
                st.session_state.select = "Page 4"
                st.rerun()

            if btn2.button("Home", key="home_btn"):
                keys_to_reset = ["name", "Company", "TypeName", "ScreenType", "TouchScreen", "CPU_Company",
                                "Frequency_Category", "RAM_Category", "Memory_Category", "GPU_Company",
                                "OpSys", "Price_Category"]
                for key in keys_to_reset:
                    st.session_state.pop(key, None)
                st.session_state.select = "Home"
                st.rerun()

            if btn3.button("Random 5", key="random_btn"):
                st.session_state["random_laptops"] = df.sample(n=5)
                st.rerun()

            # Show random laptops
            st.dataframe(st.session_state["random_laptops"], use_container_width=True, height=250)

        else:
            b1, txt2, btn1, btn2, b2 = st.columns([1, 10, 1.2, 1.2, 1], vertical_alignment="center")

            txt2.subheader("The laptops based on your search are ready!")

            if btn1.button("Back", key="result_back"):
                st.session_state.select = "Page 4"
                st.rerun()

            if btn2.button("Home", key="home_btn"):
                keys_to_reset = ["name", "Company", "TypeName", "ScreenType", "TouchScreen", "CPU_Company",
                                "Frequency_Category", "RAM_Category", "Memory_Category", "GPU_Company",
                                "OpSys", "Price_Category"]
                for key in keys_to_reset:
                    st.session_state.pop(key, None)
                st.session_state.select = "Home"
                st.rerun()

            st.dataframe(result, use_container_width=True, height=275)
  

# Calling Pages
page_calls = Pages()

# Main Container
main_container = st.container(height=500, border=True)

with main_container:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    b1,img,b2,intro,b3 = st.columns([0.2,2,0.2,2.5,0.4])

    if "select" not in st.session_state:
        st.session_state.select = "Home"

    if st.session_state.select == "Home":
        page_calls.home()
    elif st.session_state.select == "Page 1":
        page_calls.page1()
    elif st.session_state.select == "Page 2":
        page_calls.page2()
    elif st.session_state.select == "Page 3":
        page_calls.page3()
    elif st.session_state.select == "Page 4":
        page_calls.page4()
    elif st.session_state.select == "Result":
        page_calls.result()

    st.markdown('</div>', unsafe_allow_html=True)