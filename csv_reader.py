import csv
import os

def read_subject_csv(subject: str) -> list:
    """
    Reads the CSV file for the given subject from the resources folder.
    Returns a list of dictionaries (one per row).
    """
    filename = os.path.join(os.path.dirname(__file__), 'resources', f'{subject}.csv')
    if not os.path.exists(filename):
        raise FileNotFoundError(f"CSV file for subject '{subject}' not found at {filename}")
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
