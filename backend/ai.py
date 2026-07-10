from database import load_knowledge

def analyze_claim(claim):

    knowledge = load_knowledge()

    claim = claim.lower()

    if claim in knowledge:
        return knowledge[claim]

    return None
