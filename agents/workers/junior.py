from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from utils.llm_client import call_llm
from agents import Agent
from prompts.systemprompt import systemprompt
from prompts.junior_userprompt import junior_user_prompt




junior_agent = Agent(
    name = "Junior Agent",
    description = "A junior agent that generates technical, behavioral questions and evaluation rubrics based on the given role",
    llm_call = call_llm,
    system_prompt = systemprompt,
    user_prompt = junior_user_prompt
)


