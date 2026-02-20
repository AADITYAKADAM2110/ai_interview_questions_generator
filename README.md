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
LLM: llama-3.3-70b-versatile
Streamlit (UI)
Pydantic (output schema validation)
uv (package management)

Current Update:
Worker agents are built and tested
A temparory solution to direct agents: if-else logic

Next Steps:
Create Supervisor agent and replace current if-else logic to direct agents and orchestrate the system
Implement Schemas for structured outputs
build a funtioning UI using Streamlit
Improve the Documentation

Note: This README represents the initial design intent and will be expanded as implementation progresses.
