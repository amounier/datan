import requests
from bs4 import BeautifulSoup

url = "https://datan.fr/deputes"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# elements = soup.find_all("div", class_="col-md-6 col-xl-4 sorting-item rn")
elements = soup.find_all("div", class_="col-md-6 col-xl-4 sorting-item rn")

for element in elements:
    name = element.find("h3", class_="card-title").text.strip()
    constituency = element.find("span", class_="d-block").text.strip()
    # party = element.find("div", class_="card-footer").text.strip()
    img = element.find("img", class_="img-lazy").get("data-src")

    print("Name:", name)
    print("Constituency:", constituency)
    print("Img link:", img)
    print("---")