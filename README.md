# Interview Question Generator – Agentic AI System

# Overview
This project will implement an AI-powered interview question generator system, which will be designed to help interviewers quickly create high-quality technical and behavioral interview questions along with clear evaluation rubrics.

# Setup & Installation

## Prerequisites
-Python 3.10+
-uv package manager
-A Groq API key (free tier)

## Clone the repository
git clone <your-repo-url>
cd interview-question-generator

## Create virtual environment & install dependencies
uv venv
uv pip install -r requirements.txt

## Environment Configuration
Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key_here

## Run the Application Locally
streamlit run app.py
The application will start locally and open in your browser.

# Dependencies 
Key dependencies used in this project:
groq – LLM API client (free)
streamlit – UI layer
pydantic – structured output validation
python-dotenv – environment variable management
uv – package and environment management
All dependencies are listed in requirements.txt.

# Application Architecture & Data Flow

## High-level flow:

User enters:
Job role (free text)
Experience level (Junior / Mid / Senior)
Input is validated and normalized
Supervisor routes the request to the appropriate worker agent
Worker agent generates:
Technical questions
Behavioral questions
Evaluation rubrics
Supervisor validates output structure
Output is rendered in the UI and made available for download

# Technical Documentation
## Prompt Tuning Strategy
A single base system prompt defines:
Role seriousness
Experience calibration
Output constraints
Worker agents reuse the same prompt with experience-specific calibration
Prompts explicitly prohibit:
Numerical scoring
Answer evaluation
Model answers
This minimizes drift and keeps behavior predictable.

## Difficulty Calibration Logic
Difficulty is calibrated using explicit experience-level constraints:

Junior (0–2 years):
Fundamentals
Learning mindset
Simple reasoning and debugging

Mid (3–5 years):
Applied knowledge
Trade-offs
Problem-solving

Senior (6+ years):
System design
Architecture
Ownership and decision-making
Calibration is enforced through prompt instructions, not post-processing.

## Structured Output Schema
Each output must include:
Technical Interview Questions
Behavioral Interview Questions
Evaluation Rubrics
Rubrics must use Strong / Average / Weak indicators only.
Numerical scoring and automated evaluation are explicitly disallowed.

# Problem Statement:
Interviewers often struggle to design role-appropriate interview questions consistently, calibrate difficulty based on experience level, evaluate candidates using clear, structured criteria
This system aims to reduce that friction by using an LLM to assist interviewers while keeping human judgment in the loop.

# Tech Stack:
Python
OpenAI SDK 
LLM: llama-3.3-70b-versatile
Streamlit (UI)
Pydantic (output schema validation)
uv (package management)

# Limitations
No Candidate Answer Evaluation

Dependence on LLM Output Quality

No Persistent Memory or Context Retention

Limited Role-Specific Depth for Highly Niche Roles

Single-Language Support

No Custom Rubric Configuration

Note: This project intentionally focuses on design quality, robustness, and clarity, rather than feature breadth.
The system demonstrates a practical, production-oriented approach to agentic AI.
