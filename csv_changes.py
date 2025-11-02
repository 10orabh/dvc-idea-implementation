import pandas as pd 

df = pd.read_csv("data/people.csv")

new_data = {
    "Name": ["Arushi", "Dipaali"],
    "Age": [38, 26],
    "City": ["Indore", "Maheshwar"]
}
new_df = pd.DataFrame(new_data)
df = pd.concat([df, new_df], ignore_index=True)

df.to_csv("data/people.csv", index=False)