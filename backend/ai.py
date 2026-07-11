from database import load_knowledge

def analyze_claim(claim):

    knowledge = load_knowledge()

    claim = claim.lower()

    for keyword in knowledge:
        if keyword in claim:
            return knowledge[keyword]

    return None

