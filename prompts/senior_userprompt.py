from variables import role

senior_user_prompt = f"""
Job Role: {role}
Experience Level: Senior (4+ years)

Your task is to generate a small, high-quality set of interview questions and evaluation rubrics based on the above job role and experience level.

Follow the GENERAL INSTRUCTIONS, EXPERIENCE LEVEL CALIBRATION, QUESTION GUIDELINES, EVALUATION RUBRICS, OUTPUT FORMAT, and SCOPE LIMITATIONS provided in the system prompt.

Output should be in clear, structured Markdown with appropriate headings for each section.

Output structure:
Technical Interview Questions
1. Question 1
...
Behavioral Interview Questions
1. Question 1
...
Evaluation Rubrics
...

Evaluation rubrics should use ONLY the following levels:
- Strong
- Average
- Weak

"""