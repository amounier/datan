import pandas as pd
import requests
from tqdm import tqdm
import os

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("output/RN_deputees_information.csv")

# Iterate over the rows of the DataFrame
for index, row in tqdm(df.iterrows(), total=len(df)):
    # Extract the image link and deputy ID from the row
    img_link = row["Image Link"]
    deputy_id = row["Deputy ID"]

    # Send a GET request to the image link
    response = requests.get(img_link)

    # Check if the request was successful
    if response.status_code == 200:
        # Construct the file path for the downloaded image
        file_path = os.path.join("output/RN_deputees_img", f"{deputy_id}.png")

        # Save the image content to the file
        with open(file_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to download image for Deputy ID: {deputy_id}")

print("Image download completed.")