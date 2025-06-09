import argparse
from csv_reader import read_subject_csv
import csv
import os
from concept_extractor import extract_concepts

def main():
    parser = argparse.ArgumentParser(description="Intern Test Task: Question to Concept Mapping")
    parser.add_argument('--subject', required=True, choices=['ancient_history', 'math', 'physics', 'economics'], help='Subject to process')
    args = parser.parse_args()

    data = read_subject_csv(args.subject)
    print(f"Loaded {len(data)} questions for subject: {args.subject}")

    for row in data:
        question_number = row['Question Number']
        question_text = row['Question']
        concepts = extract_concepts(question_text)
        if concepts:
            concept_str = ', '.join(concepts)
        else:
            concept_str = 'Concept Not Identified'
        print(f"Question {question_number}: {concept_str}")

    output_filename = f'output_concepts_{args.subject}.csv'
    with open(output_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Question Number', 'Question', 'Concepts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            question_number = row['Question Number']
            question_text = row['Question']
            concepts = extract_concepts(question_text)
            if concepts:
                concept_str = '; '.join(concepts)
            else:
                concept_str = 'Concept Not Identified'
            writer.writerow({
                'Question Number': question_number,
                'Question': question_text,
                'Concepts': concept_str
            })
    

if __name__ == "__main__":
    main()
