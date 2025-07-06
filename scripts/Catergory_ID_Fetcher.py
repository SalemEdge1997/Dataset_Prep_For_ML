import requests
import pandas as pd

def fetch_catergory_ids(api_key):
    """
    Fetches YouTube video category IDs and their corresponding titles.
    
    Args:
        api_key (str): Your YouTube Data API key.
        
    Returns:
        pd.DataFrame: A DataFrame containing category IDs and titles.
    """
    url = "https://www.googleapis.com/youtube/v3/videoCategories"
    params = {
        "part": "snippet",
        "regionCode": "GB",  # Change as needed
        "key": api_key
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        categories = data.get("items", [])
        
        # Extracting category ID and title
        category_data = {
            "category_id": [cat["id"] for cat in categories],
            "title": [cat["snippet"]["title"] for cat in categories]
        }
        
        return pd.DataFrame(category_data)
    else:
        raise Exception(f"Error fetching data: {response.status_code} - {response.text}")
    
print(fetch_catergory_ids('AIzaSyB8tXI5xDwvDZyiaPWERnP_vOOLdeDDabU'))    
