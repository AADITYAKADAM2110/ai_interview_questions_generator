from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from agents.workers.junior import run_junior_agent
from agents.workers.mid import run_mid_agent
from agents.workers.senior import run_senior_agent


class SupervisorAgent:
    def run(self, role: str, experience_level: str) -> str:
        level = experience_level.lower()
        if "junior" in level:
            return run_junior_agent(role)
        if "mid" in level:
            return run_mid_agent(role)
        if "senior" in level:
            return run_senior_agent(role)
        raise ValueError(f"Invalid experience level: {experience_level}")
