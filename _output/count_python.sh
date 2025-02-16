#!/bin/bash

# Initialize count
count=0

# Loop through all CSV files in the current directory
for file in *.csv; do
  # Count occurrences of 'python' (case insensitive)
  count=$((count + $(grep -i "python" "$file" | wc -l)))
done

# Print result
echo "Number of lines containing 'python' in CSV files: $count"
