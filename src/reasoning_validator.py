# reasoning_validator.py


def validate_reasoning(response):

    required_sections = [

        "FACTS",

        "ASSUMPTIONS",

        "REASONING",

        "SELF-CORRECTION",

        "VERIFICATION",

        "FINAL ANSWER"
    ]

    missing_sections = []

    for section in required_sections:

        if section not in response.upper():

            missing_sections.append(section)

    return {
        "valid": len(missing_sections) == 0,
        "missing_sections": missing_sections
    }
