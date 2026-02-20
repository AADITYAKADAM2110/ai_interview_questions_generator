REQUIRED_SECTIONS = [
    "### Technical Interview Questions",
    "### Behavioral Interview Questions",
    "### Evaluation Rubrics"
]

def validate_output(output: str):
    for section in REQUIRED_SECTIONS:
        if section not in output:
            raise ValueError(f"Missing required section: {section}")
    
    if any(word in output.lower() for word in ["points", "%", "score", "marks"]):
        raise ValueError("Evaluation rubrics should not contain points or scores.")

    return output
