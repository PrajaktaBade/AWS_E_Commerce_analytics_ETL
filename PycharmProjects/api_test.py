import requests
import pandas as pd

# 1. Define API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# 2. Make GET request
response = requests.get(url)

# 3. Check response
if response.status_code == 200:
    data = response.json()  # Convert to Python dict/list
    print(f"Retrieved {len(data)} records from API")

    # 4. Load into Pandas DataFrame
    df = pd.DataFrame(data)

    # 5. Simple data check
    print(df.head())

    # 6. Save to CSV (simulating ETL load step)
    df.to_csv("api_posts.csv", index=False)
    print("Data saved to api_posts.csv")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
