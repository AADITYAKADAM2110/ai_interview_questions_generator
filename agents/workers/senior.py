from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

try:
    from utils.llm_client import call_llm
    from agents import Agent
    from prompts.systemprompt import systemprompt
    from prompts.senior_userprompt import build_senior_user_prompt
except ImportError as e:
    print(f"Error importing modules: {e}")
    raise


def run_senior_agent(role: str) -> str:
    senior_agent = Agent(
        name="Senior Agent",
        description="A senior agent that generates technical, behavioral questions and evaluation rubrics based on the given role",
        llm_call=call_llm,
        system_prompt=systemprompt,
        user_prompt=build_senior_user_prompt(role),
    )
    try:
        return senior_agent.run()
    except Exception as e:
        print(f"Error running senior agent: {e}")
        raise