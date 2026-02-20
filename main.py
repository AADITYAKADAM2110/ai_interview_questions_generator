from agents.supervisor.supervisor import SupervisorAgent
from schemas.validator import validate_output


def main(role: str, experience_level: str):
    supervisor_agent = SupervisorAgent()
    response = supervisor_agent.run(role, experience_level)
    validate_output(response)
    print(response)
    return response


if __name__ == "__main__":
    main("Software Engineer", "Mid")
