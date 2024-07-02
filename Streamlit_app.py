import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Title of the app
st.title("Contact des députés en 3ème position des triangulaires")

# # Data for the table
# data = {
#     "Column 1": ["Row 1", "Row 2", "Row 3"],
#     "Column 2": ["Data 1", "Data 2", "Data 3"]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# Load the CSV file
csv_file = "output/votes_T1/non_desistements.csv" # input/target_deputees.csv"
df = pd.read_csv(csv_file)
columns_to_keep = ["Candidats", "reg", "dep", "circo", "groupe_nuance"]
df = df[columns_to_keep]
# df["groupe_nuance"] = df["groupe_nuance"].upper()

# Display the counter
row_count = len(df)
st.subheader(f"Triangulaires restantes: {row_count}")

# # Display the multiselect widget for filtering by column values
# filter_columns = st.multiselect("Select columns to filter by", df.columns.tolist())

# # Create a dictionary to hold the filter values for each column
# filter_values = {}
# for col in filter_columns:
#     unique_values = df[col].unique().tolist()
#     selected_values = st.multiselect(f"Select values for {col}", unique_values, default=unique_values)
#     filter_values[col] = selected_values

# # Filter the DataFrame based on selected values
# filtered_df = df.copy()
# for col, values in filter_values.items():
#     filtered_df = filtered_df[filtered_df[col].isin(values)]

# # Create GridOptionsBuilder from the dataframe
# gb = GridOptionsBuilder.from_dataframe(df)

# # Enable filtering in the grid
# gb.configure_default_column(filterable=True)

# # Create the grid options
# gridOptions = gb.build()

# # Display the interactive grid with filtering
# grid_response = AgGrid(
#     df,
#     gridOptions=gridOptions,
#     enable_enterprise_modules=False,
#     theme='streamlit',
#     height=500,
#     width='100%',  # Adjust the width here
#     fit_columns_on_grid_load=True,
#     allow_unsafe_jscode=True,  # Set to True if you use JS functions in the grid options
# )

# # Get the filtered data
# filtered_df = pd.DataFrame(grid_response['data'])



# Display the table
st.table(df)
