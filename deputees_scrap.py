import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://datan.fr/deputes"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# elements = soup.find_all("div", class_="col-md-6 col-xl-4 sorting-item rn")
elements = soup.find_all("div", class_="col-md-6 col-xl-4 sorting-item rn")

# for element in elements:
#     name = element.find("h3", class_="card-title").text.strip()
#     constituency = element.find("span", class_="d-block").text.strip()
#     # party = element.find("div", class_="card-footer").text.strip()
#     img = element.find("img", class_="img-lazy").get("data-src")

#     print("Name:", name)
#     print("Constituency:", constituency)
#     print("Img link:", img)
#     print("---")


# Create an empty list to store the data
data = []

# Iterate over the elements and extract the desired information
for element in elements:
    name = element.find("h3", class_="card-title").text.strip()
    constituency = element.find("span", class_="d-block").text.strip()
    party = element.find("div", class_="card-footer").text.strip()
    img_element = element.find("img", class_="img-lazy")
    img_link = img_element.get("data-src") if img_element else ""
    deputy_id = img_link.split("/")[-1].split("_")[-1].split(".")[0]

    # Append the extracted data to the list
    data.append({"Name": name, "Constituency": constituency, "Party": party, "Image Link": img_link, "Deputy ID": deputy_id})

# Create a pandas DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("output/deputees_information.csv", index=False, encoding="utf-8")