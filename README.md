
# Question to Concept Mapping

This project provides a Python-based solution for extracting concepts from a given set of questions based on a predefined keyword-to-concept mapping. It is designed to be easily extensible for different subjects and concept categories.

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Setup](#setup)
5. [Usage](#usage)
6. [Output](#output)
7. [Extending and Customizing](#extending-and-customizing)
8. [Contributing](#contributing)

## Description

The "Question to Concept Mapping" tool is designed to automate the process of identifying key concepts within educational questions. It reads questions from subject-specific CSV files, applies a rule-based concept extraction logic using a comprehensive keyword dictionary, and then generates an output CSV file with questions mapped to their identified concepts. This can be particularly useful for categorizing questions, building knowledge graphs, or aiding in educational content organization.

## Features

* **Subject-Specific Processing**: Processes questions for different subjects (e.g., ancient history, math, physics, economics) based on command-line arguments.
* **Keyword-Based Concept Extraction**: Utilizes a configurable dictionary of keywords to concepts for flexible and scalable concept identification.
* **CSV Input/Output**: Reads questions from CSV files and outputs the results, including identified concepts, into new CSV files, ensuring easy integration with other data workflows.
* **Modular Design**: Clear separation of concerns with dedicated modules for CSV reading, concept extraction, and keyword definitions.
* **Extensible**: Easily add new subjects or extend the concept mapping by modifying simple Python dictionary files.

## Project Structure

The project is organized into several Python files, each serving a specific purpose:

```
.
├── main.py
├── concept_extractor.py
├── concept_keywords.py
├── csv_reader.py
└── resources/
    ├── ancient_history.csv  (example input)
    ├── economics.csv        (example input)
    ├── math.csv             (example input)
    └── physics.csv          (example input)
├── output_concepts_ancient_history.csv  (example output)
├── output_concepts_economics.csv        (example output)
├── output_concepts_math.csv             (example output)
└── output_concepts_physics.csv          (example output)
```

* **`main.py`**:
    * This is the main script that orchestrates the entire process.
    * It parses command-line arguments to determine which subject's questions to process.
    * It reads the input CSV file for the specified subject using `csv_reader.py`.
    * It iterates through each question, calls `concept_extractor.py` to identify concepts, and prints the extracted concepts to the console.
    * Finally, it writes the question, question number, and identified concepts into a new output CSV file (e.g., `output_concepts_math.csv`).

* **`concept_extractor.py`**:
    * Contains the `extract_concepts(question: str) -> list` function.
    * This function takes a question string as input.
    * It converts the question to lowercase and uses regular expressions to search for keywords defined in `concept_keywords.py`.
    * If a keyword is found, its corresponding concept is added to a set to ensure uniqueness.
    * If no specific concepts are identified, it defaults to "General Knowledge".
    * It returns a list of unique concepts found in the question.

* **`concept_keywords.py`**:
    * Defines the `CONCEPT_KEYWORDS` dictionary.
    * This dictionary is the core knowledge base for concept extraction.
    * Each key in the dictionary is a keyword (or a phrase) to be searched for in questions, and its corresponding value is the concept associated with that keyword.
    * Example: `"harappan": "Harappan Civilization"`, `"profit": "Profit and Loss"`.

* **`csv_reader.py`**:
    * Contains the `read_subject_csv(subject: str) -> list` function.
    * This utility function handles reading CSV files.
    * It constructs the file path to the subject-specific CSV within the `resources` directory.
    * It includes error handling to check if the file exists.
    * It uses Python's `csv.DictReader` to read the CSV into a list of dictionaries, where each dictionary represents a row with column headers as keys.

* **`resources/`**:
    * A directory containing example input CSV files for different subjects (`ancient_history.csv`, `economics.csv`, `math.csv`, `physics.csv`).
    * These CSV files are expected to have at least two columns: `'Question Number'` and `'Question'`.

* **`output_concepts_*.csv`**:
    * These files are generated automatically when `main.py` is run.
    * Each file will contain three columns: `'Question Number'`, `'Question'`, and `'Concepts'`. The 'Concepts' column will list all identified concepts for a given question, separated by semicolons.

## Setup

To set up and run this project, follow these steps:

### Prerequisites

* **Python 3.x**: Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the Repository (if applicable) or Download the Files**:
   If this project is part of a repository, clone it:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```
   Otherwise, ensure all provided files (`main.py`, `concept_extractor.py`, `concept_keywords.py`, `csv_reader.py`, and the `resources` folder with its CSVs) are in the same directory on your local machine.

2. **Create the `resources` Directory**:
   If it doesn't already exist, create a folder named `resources` in the same directory as your Python scripts. Place your input CSV files (e.g., `ancient_history.csv`, `math.csv`, etc.) inside this `resources` folder.

   Example structure:
   ```
   your_project_folder/
   ├── main.py
   ├── concept_extractor.py
   ├── concept_keywords.py
   ├── csv_reader.py
   └── resources/
       ├── ancient_history.csv
       ├── economics.csv
       ├── math.csv
       └── physics.csv
   ```

3. **No external libraries are required** beyond standard Python modules, so no `pip install` commands are necessary.

## Usage

To run the concept mapping script, open your terminal or command prompt, navigate to the project's root directory (where `main.py` is located), and execute the `main.py` script with the `--subject` argument.

The `--subject` argument is **required** and accepts one of the following values: `ancient_history`, `math`, `physics`, `economics`. These values correspond to the names of the CSV files in your `resources` directory (e.g., `ancient_history` corresponds to `ancient_history.csv`).

### Command Line Examples

1. **Process questions for 'math'**:
   ```bash
   python main.py --subject math
   ```

2. **Process questions for 'ancient_history'**:
   ```bash
   python main.py --subject ancient_history
   ```

3. **Process questions for 'physics'**:
   ```bash
   python main.py --subject physics
   ```

4. **Process questions for 'economics'**:
   ```bash
   python main.py --subject economics
   ```

### Running the Script

Upon execution, the script will:
* Print a message indicating the number of questions loaded for the specified subject.
* For each question, it will print the question number and the concepts identified from it to the console.
* Generate a new CSV file in the project's root directory, named `output_concepts_<subject_name>.csv` (e.g., `output_concepts_math.csv`), containing all processed questions and their extracted concepts.

## Output

After running the script, an output CSV file will be generated in the same directory as `main.py`. The filename will follow the pattern `output_concepts_<subject>.csv`.

Each output CSV file will have the following columns:

* **Question Number**: The original question number from the input CSV.
* **Question**: The full text of the question.
* **Concepts**: A string containing all identified concepts for that question, separated by semicolons (`;`). If no specific concepts are found based on the `concept_keywords.py`, it will default to "Concept Not Identified" or "General Knowledge" depending on the `concept_extractor.py` logic.

### Example Output (`output_concepts_math.csv`)

| Question Number | Question                                     | Concepts                          |
| :-------------- | :------------------------------------------- | :-------------------------------- |
| 1               | What is the profit percentage on a sale?     | Profit and Loss; Percentage       |
| 2               | A mixture of milk and water...               | Mixtures and Alligation           |
| 3               | Calculate the compound interest...           | Compound Interest                 |
| 4               | Find the ratio of apples to oranges.         | Ratio and Proportion              |
| 5               | How many combinations are possible?          | Combinatorics                     |

## Extending and Customizing

The modular design of this project makes it easy to extend its functionality and customize the concept extraction logic.

### Adding New Subjects

1. **Create a new CSV file**: In the `resources/` directory, create a new CSV file named after your subject (e.g., `my_new_subject.csv`).
2. **Format the CSV**: Ensure the CSV has at least two columns: `'Question Number'` and `'Question'`.
3. **Update `main.py` (Optional but Recommended)**:
   While not strictly necessary if you run the script directly with `--subject my_new_subject`, it's good practice to update the `choices` list in `main.py`'s `ArgumentParser` to include your new subject. This provides better argument validation.
   ```python
   # In main.py
   parser.add_argument('--subject', required=True, choices=['ancient_history', 'math', 'physics', 'economics', 'my_new_subject'], help='Subject to process')
   ```

### Adding New Concepts and Keywords

To expand the concept mapping, you only need to modify the `concept_keywords.py` file.

1. **Open `concept_keywords.py`**.
2. **Add new entries to the `CONCEPT_KEYWORDS` dictionary**:
   * The key should be the keyword (or short phrase) that you expect to find in a question. It's best to use lowercase for keywords for case-insensitive matching.
   * The value should be the corresponding concept name you want to associate with that keyword.

   Example:
   ```python
   # concept_keywords.py

   CONCEPT_KEYWORDS = {
       # ... existing entries ...
       "new_keyword": "New Concept Category",
       "another phrase": "Another Specific Concept",
       "energy conservation": "Physics - Energy Conservation"
   }
   ```
   Remember that the `concept_extractor.py` uses `re.search(rf'\b{re.escape(keyword)}\b', question_lower)` for matching. The `\b` ensures whole-word matching, and `re.escape()` handles special characters in your keywords.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please consider:

1. **Forking the repository**.
2. **Creating a new branch** for your feature or bug fix.
3. **Implementing your changes**.
4. **Ensuring all existing functionality still works** as expected.
5. **Adding new tests** if applicable.
6. **Updating the `concept_keywords.py`** or adding new subject CSVs if your changes introduce new concepts or subjects.
7. **Submitting a Pull Request** with a clear description of your changes.
