from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from utils.llm_client import call_llm
from agents import Agent
from prompts.systemprompt import systemprompt
from prompts.senior_userprompt import senior_user_prompt




senior_agent = Agent(
    name = "Senior Agent",
    description = "A senior agent that generates technical, behavioral questions and evaluation rubrics based on the given role",
    llm_call = call_llm,
    system_prompt = systemprompt,
    user_prompt = senior_user_prompt
)



