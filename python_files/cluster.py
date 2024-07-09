import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('./dataset/Ankle boot/Ankle boot_1.csv')

# Sort the DataFrame by 'SSIM' column in descending order
df_sorted = df.sort_values(by='SSIM', ascending=False)

# Initialize an empty list to store the rows with the least cost function in each group
selected_rows = []

# Group the sorted DataFrame into chunks of 100 rows each
for i in range(0, len(df_sorted), 100):
    chunk = df_sorted.iloc[i:i+100]
    # Find the row with the minimum 'costfunction' in the current chunk
    min_cost_row = chunk.loc[chunk['costfunction'].idxmin()]
    # Append the row to the selected_rows list
    selected_rows.append(min_cost_row)

# Convert the selected rows into a DataFrame
selected_df = pd.DataFrame(selected_rows)

# Write the selected DataFrame to a new CSV file
selected_df.to_csv('./clustered_data/Ankle_boot.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'selected_rows.csv'.")
