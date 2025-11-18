import pandas as pd
import os

# --- Configuration ---
INPUT_FILE = 'pokemon.csv'
OUTPUT_FILE = 'pokemon_data.json'

def convert_csv_to_json_file(input_csv_path: str, output_json_path: str) -> None:
    """
    Reads a CSV file and converts its contents into a structured JSON file.

    :param input_csv_path: The path to the source CSV file.
    :param output_json_path: The path where the JSON file will be saved.
    """
    try:
        # 1. Read the CSV file into a pandas DataFrame.
        # pandas is the industry standard for this type of data manipulation.
        df = pd.read_csv(input_csv_path)

        # 2. Convert the DataFrame to a JSON file directly.
        # orient='records': Formats the data as a list of dictionaries (one dictionary per row), 
        # which is the most common and useful structure for APIs and modern data consumption.
        # indent=4: Ensures the JSON is human-readable (pretty-printed).
        df.to_json(
            output_json_path, 
            orient='records', 
            indent=4, 
            force_ascii=False
        )

        print(f"✅ Data successfully written to {output_json_path}")

    except FileNotFoundError:
        print(f"🚩 Error: Input file not found at {input_csv_path}. Terminating operation.")
    except pd.errors.EmptyDataError:
        print("🚩 Error: CSV file is empty. No data to convert.")
    except Exception as e:
        print(f"🚩 An unexpected error occurred: {e}")

# --- Execution ---
if __name__ == "__main__":
    # Ensure the input file exists before attempting conversion.
    if os.path.exists(INPUT_FILE):
        convert_csv_to_json_file(INPUT_FILE, OUTPUT_FILE)
    else:
        # Fallback in case the environment did not place the file correctly.
        print(f"🚩 Critical Error: The source file '{INPUT_FILE}' is missing from the environment. Cannot initiate conversion.")