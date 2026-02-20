from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from utils.llm_client import call_llm
from agents import Agent
from prompts.systemprompt import systemprompt
from prompts.mid_userprompt import mid_user_prompt




mid_agent = Agent(
    name = "Mid Agent",
    description = "A Mid level agent that generates technical, behavioral questions and evaluation rubrics based on the given role",
    llm_call = call_llm,
    system_prompt = systemprompt,
    user_prompt = mid_user_prompt
)



