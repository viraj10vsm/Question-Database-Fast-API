import pandas as pd
import json

# Define a function to convert CSV to JSON
def csv_to_json(csv_file_path, json_file_path=None):
    try:
        # Read the CSV file with appropriate encoding (ISO-8859-1 for non-UTF-8 content)
        df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')  # You can also try 'cp1252' if needed

        # Select and rename the relevant columns to match your MongoDB Question model fields
        df = df[['question', 'answer', 'category', 'difficulty', 'role']]

        # Convert the DataFrame to a list of dictionaries
        questions = df.to_dict(orient='records')

        # Optionally save the output to a JSON file
        if json_file_path:
            with open(json_file_path, 'w') as json_file:
                json.dump(questions, json_file, indent=4)

        # Return the JSON structure as a list of dictionaries
        return questions

    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# File paths
csv_file_path = "C:/Users/viraj/Desktop/Software Questions.csv"  # Your CSV file path
json_file_path = 'C:/Users/viraj/Desktop/questions.json'  # Path to save the output JSON

# Convert the CSV data to JSON and optionally save it
questions_json = csv_to_json(csv_file_path, json_file_path)

# Output the converted JSON to the console
if questions_json:
    print(questions_json)
