from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from agents.workers.junior import junior_agent_tool
from agents.workers.mid import mid_agent_tool
from agents.workers.senior import senior_agent_tool


class SupervisorAgent:
    def run(self, role: str, experience_level: str) -> str:
        if experience_level.lower() == "junior":
            return junior_agent_tool()
        elif experience_level.lower() == "mid":
            return mid_agent_tool()
        elif experience_level.lower() == "senior":
            return senior_agent_tool()
        else:
            raise ValueError(f"Invalid experience level: {experience_level}")