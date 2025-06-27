import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Sample data for tile roofs
data = pd.DataFrame({
    "Address": [
        "1234 E Desert St, Tucson, AZ",
        "5678 W Tile Ln, Tucson, AZ",
        "9101 N Roof View Rd, Tucson, AZ"
    ],
    "Latitude": [32.2226, 32.2500, 32.2300],
    "Longitude": [-110.9747, -110.9500, -110.9800],
    "Year Built": [1995, 1987, 2001],
    "Home Value": [425000, 390000, 510000],
    "Visited": ["No", "No", "No"],
    "Notes": ["", "", ""]
})

st.title("🧠 Roofing Lead Tracker MVP")
st.markdown("Map, track, and manage high-value tile roof leads in Tucson.")

# Map
st.subheader("🏘️ Map of Tile Roof Leads")
map_center = [data["Latitude"].mean(), data["Longitude"].mean()]
m = folium.Map(location=map_center, zoom_start=12)

for _, row in data.iterrows():
    popup = f"{row['Address']}<br>Year: {row['Year Built']}<br>Value: ${row['Home Value']:,.0f}"
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=popup,
        icon=folium.Icon(color="green" if row["Visited"] == "Yes" else "blue")
    ).add_to(m)

st_data = st_folium(m, width=700, height=500)

# Visit log
st.subheader("📋 Visit Log & Notes")
selected_address = st.selectbox("Select a home to update", data["Address"])

if selected_address:
    idx = data[data["Address"] == selected_address].index[0]
    visited = st.selectbox("Visited?", ["No", "Yes"], index=0 if data.at[idx, "Visited"] == "No" else 1)
    note = st.text_area("Notes", value=data.at[idx, "Notes"])
    if st.button("Update Entry"):
        data.at[idx, "Visited"] = visited
        data.at[idx, "Notes"] = note
        st.success("Entry updated!")

# Data table
st.subheader("📄 Lead Table")
st.dataframe(data)

# Download CSV
st.download_button("📥 Download Updated List", data.to_csv(index=False), file_name="roofing_leads.csv")
