import streamlit as st
import pandas as pd

# Title of the app
st.title("Two Columns Table Example")

# # Data for the table
# data = {
#     "Column 1": ["Row 1", "Row 2", "Row 3"],
#     "Column 2": ["Data 1", "Data 2", "Data 3"]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# Load the CSV file
csv_file = "input/target_deputees.csv"
df = pd.read_csv(csv_file)

# Display the counter
row_count = len(df)
st.subheader(f"Triangulaires restantes: {row_count}")

# Display the table
st.table(df)
