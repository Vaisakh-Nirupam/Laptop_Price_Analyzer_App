# Adding the libraries
import pandas as pd

# Full page
st.set_page_config(page_title="LAP", page_icon=r"", layout="wide")

# Loading the dataset
df  = pd.read_csv(r"Dataset\Laptop_Price_Improved.csv")

# Displaying the dataset
st.title("Laptop Price Analyzer!")
st.write(df)

