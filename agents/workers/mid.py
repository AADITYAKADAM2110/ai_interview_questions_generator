from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

try:
    from utils.llm_client import call_llm
    from agents import Agent
    from prompts.systemprompt import systemprompt
    from prompts.mid_userprompt import build_mid_user_prompt
except ImportError as e:
    print(f"Error importing modules: {e}")
    raise


def run_mid_agent(role: str) -> str:
    mid_agent = Agent(
        name="Mid Agent",
        description="A Mid level agent that generates technical, behavioral questions and evaluation rubrics based on the given role",
        llm_call=call_llm,
        system_prompt=systemprompt,
        user_prompt=build_mid_user_prompt(role),
    )
    try:
        return mid_agent.run()
    except Exception as e:
        print(f"Error running mid agent: {e}")
        raise
