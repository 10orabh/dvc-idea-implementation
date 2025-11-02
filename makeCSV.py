import pandas as pd
import os

# Create a folder name
folder_name = "data"

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create data
data = {
    "Name": ["Sourabh", "Rahul", "Priya", "Anita"],
    "Age": [25, 22, 24, 27],
    "City": ["Delhi", "Mumbai", "Pune", "Jaipur"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# new data 

# Create the file path using os.path.join
file_path = os.path.join(folder_name, "people.csv")

# Save the DataFrame as a CSV file
df.to_csv(file_path, index=False)

print(f"CSV file saved successfully at: {file_path}")
