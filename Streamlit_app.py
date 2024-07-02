import streamlit as st
import pandas as pd
# from st_aggrid import AgGrid, GridOptionsBuilder

# Function to create clickable links
def make_clickable(link):
    return f'<a href="{link}" target="_blank">Twitter</a>'

# Title of the app
st.title("Contact des députés non désistés en 3ème position des triangulaires")

st.markdown("Méthode: les scénarios de désistements sont à stratégies de reports d’[enquêtes sur les législatives de 2022](https://harris-interactive.fr/wp-content/uploads/sites/6/2022/06/Harris-x-Toluna-pour-M6-et-RTL-Jour-du-vote-au-2nd-tour-des-elections-legislatives-2022.pdf)")

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
columns_to_keep = ["Candidats", "Nuance", "Contact"] #"reg", "dep", "circo", "groupe_nuance","Contact"]
df = df[columns_to_keep]
# df["groupe_nuance"] = df["groupe_nuance"].upper()

# Rename columns using the rename method
df.rename(columns={'Nuance': 'Groupe'}) #, 'Contact': 'Twitter Profile'}, inplace=True)

# Apply the function to the 'Profile' column
# df['Contact'] = df['Contact'].apply(make_clickable)
df['Contact'] = df['Contact'].apply(lambda x: make_clickable(x) if pd.notnull(x) and x.startswith('http') else '')


# Display the counter
row_count = len(df)
st.subheader(f"Triangulaires restantes: {row_count}")

st.subheader(f"Visuels scénarios de désistements")
st.image("output/votes_T2_projections/S1_cut.png")
st.image("output/votes_T2_projections/S2_cut.png")
st.image("output/votes_T2_projections/S3_cut.png")
st.image("output/votes_T2_projections/S4_cut.png")
st.image("output/votes_T2_projections/S5_cut.png")


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



# # Display the table
# st.table(df)
# Display the table using st.markdown with unsafe_allow_html=True
st.subheader(f"Tableau contacts candidats")
st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

