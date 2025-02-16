import pandas as pd
import os

# Ensure the output directory exists
output_dir = "_output"
os.makedirs(output_dir, exist_ok=True)

# Get all CSV files in the directory
files = [f for f in os.listdir() if f.endswith('.csv')]

# Initialize count
count = 0
chunk_size = 100000  # Adjust this based on available memory

# Process each CSV file in chunks
for file in files:
    try:
        for chunk in pd.read_csv(file, dtype=str, on_bad_lines="skip", encoding="utf-8", chunksize=chunk_size):
            count += chunk.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False).any(), axis=1).sum()
        print(f"Processed {file} successfully.")

    except FileNotFoundError:
        print(f"Warning: {file} not found.")
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Print the total count
print(f"Total lines containing 'GitHub': {count}")

# Save the result to a text file
with open(os.path.join(output_dir, "github_count.txt"), "w") as f:
    f.write(f"Total lines containing 'GitHub': {count}\n")
