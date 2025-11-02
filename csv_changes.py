import pandas as pd 

df = pd.read_csv("data/people.csv")

new_data = {
    "Name": ["Vikram", "Sneha"],
    "Age": [30, 28],
    "City": ["Chennai", "Bangalore"]
}
new_df = pd.DataFrame(new_data)
df = pd.concat([df, new_df], ignore_index=True)

df.to_csv("data/people.csv", index=False)