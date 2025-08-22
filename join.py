import pandas as pd

# Load your CSV files
airdates = pd.read_csv('csv/airdates.csv')
categories = pd.read_csv('csv/categories.csv')
documents = pd.read_csv('csv/documents.csv')
clues = pd.read_csv('csv/clues.csv')

# Convert the airdate column to datetime format (make sure it's in the correct format in your CSV)
airdates['airdate'] = pd.to_datetime(airdates['airdate'], errors='coerce')

# Filter the rows where the airdate is after the year 2000
filtered_airdates = airdates[airdates['airdate'].dt.year > 2000]

# Merge the filtered airdates with clues to get only the relevant clues
merged_clues_airdates = pd.merge(clues, filtered_airdates, on='game', how='inner')

# Merge with documents to get the clue and answer
merged_clues_airdates_docs = pd.merge(merged_clues_airdates, documents, on='id', how='inner')

# Merge with categories to add category information (left join to keep all clues)
final_merged = pd.merge(merged_clues_airdates_docs, categories, on='id', how='left')

# Save the filtered data to a new CSV
final_merged.to_csv('filtered_data.csv', index=False)

print("Filtered data has been saved to 'filtered_data.csv'")

