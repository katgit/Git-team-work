import pandas as pd
import os

# --- 1. Create a pandas DataFrame ---
def create_sample_dataframe():
    """
    Creates a sample pandas DataFrame with some numerical and categorical data.
    """
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
        'Age': [25, 30, 35, 28, 22, 40, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Boston', 'Los Angeles', 'Chicago', 'Boston'],
        'Score': [85.5, 90.0, 78.2, 92.1, 88.0, 75.6, 95.0, 81.3]
    }
    df = pd.DataFrame(data)
    print("--- Created DataFrame ---")
    print(df)
    print("\n")
    return df

# --- 2. Summarize the DataFrame ---
def summarize_dataframe(dataframe):
    """
    Generates descriptive statistics for the DataFrame.
    """
    print("--- DataFrame Summary (Descriptive Statistics) ---")
    print(dataframe.describe(include='all')) # include='all' to include non-numeric columns
    print("\n")

# --- 3. Save the DataFrame as a CSV file ---
def save_dataframe_to_csv(dataframe, filename="sample_data.csv"):
    """
    Saves the given DataFrame to a CSV file.
    """
    try:
        dataframe.to_csv(filename, index=False) # index=False prevents writing the DataFrame index as a column
        print(f"DataFrame successfully saved to '{filename}'")
    except IOError as e:
        print(f"Error saving DataFrame to CSV: {e}")

if __name__ == "__main__":
    # Create the DataFrame
    my_dataframe = create_sample_dataframe()

    # Summarize the DataFrame
    summarize_dataframe(my_dataframe)

    # Define the CSV filename
    csv_file_name = "my_sample_dataframe.csv"

    # Save the DataFrame to CSV
    save_dataframe_to_csv(my_dataframe, csv_file_name)

    # Optional: Verify the file exists and read it back (for demonstration)
    if os.path.exists(csv_file_name):
        print(f"\n--- Verifying '{csv_file_name}' by reading it back ---")
        try:
            read_df = pd.read_csv(csv_file_name)
            print(read_df)
        except pd.errors.EmptyDataError:
            print(f"The CSV file '{csv_file_name}' is empty.")
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
    else:
        print(f"\nVerification failed: '{csv_file_name}' was not found.")
