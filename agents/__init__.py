from dataclasses import dataclass
from typing import Callable


@dataclass
class Agent:
    name: str
    description: str
    llm_call: Callable[..., str]
    system_prompt: str
    user_prompt: str

    def run(self) -> str:
        return self.llm_call(
            system_prompt=self.system_prompt,
            user_prompt=self.user_prompt,
        )
