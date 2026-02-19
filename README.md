Interview Question Generator – Agentic AI System

Overview
This project will implement an AI-powered interview question generator system, which will be designed to help interviewers quickly create high-quality technical and behavioral interview questions along with clear evaluation rubrics.

The system will take:
a job role (open-ended text), and
a candidate experience level (Junior / Mid / Senior)

and it will generate:
a concise set of technical questions
behavioral questions
experience-calibrated evaluation rubrics

The focus of this project is on system design, architecture, and explainability, rather than UI complexity.

Problem Statement:
Interviewers often struggle to design role-appropriate interview questions consistently, calibrate difficulty based on experience level, evaluate candidates using clear, structured criteria
This system aims to reduce that friction by using an LLM to assist interviewers while keeping human judgment in the loop.

Tech Stack:
Python
OpenAI SDK 
LLM: llama3-70b-8192
Streamlit (UI)
Pydantic (output schema validation)
uv (package management)

Next Steps:
Implement agent classes and supervisor logic
Define prompt templates and output schemas
Build minimal Streamlit UI
Expand documentation with:
design decisions
limitations
future improvements

Note: This README represents the initial design intent and will be expanded as implementation progresses.
