from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class AgentTool:
    tool_name: str
    tool_description: str
    run: Callable[[], str]

    def __call__(self) -> str:
        return self.run()


@dataclass
class Agent:
    name: str
    description: str
    llm_call: Callable[..., str]
    system_prompt: str
    user_prompt: str
    tools: list[Any] = field(default_factory=list)

    def run(self) -> str:
        return self.llm_call(
            system_prompt=self.system_prompt,
            user_prompt=self.user_prompt,
        )

    def as_tool(self, tool_name: str, tool_description: str) -> AgentTool:
        return AgentTool(
            tool_name=tool_name,
            tool_description=tool_description,
            run=self.run,
        )
