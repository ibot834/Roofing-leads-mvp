import requests
import pandas as pd

# Paste your API URL here from the Pima County API Explorer
url = "https://gisdata.pima.gov/arcgis1/rest/services/GISOpenData/Addresses/MapServer/3/query?where=1%3D1&outFields=*&outSR=4326&f=json"

response = requests.get(url)
data = response.json()

# Extract features (i.e. address records)
records = [feature["attributes"] for feature in data["features"]]

# Convert to DataFrame and save to CSV
df = pd.DataFrame(records)
df.to_csv("pima_addresses_sample.csv", index=False)

print("CSV saved: pima_addresses_sample.csv")
