
import re
from concept_keywords import CONCEPT_KEYWORDS

def extract_concepts(question: str) -> list:
    """
    Extracts concepts from the question using keyword-based matching.
    Returns a list of concepts found.
    """
    question_lower = question.lower()
    concepts = set()

    for keyword, concept in CONCEPT_KEYWORDS.items():
        if re.search(rf'\b{re.escape(keyword)}\b', question_lower):
            concepts.add(concept)

    if not concepts:
        concepts.add("General Knowledge")

    return list(concepts)
