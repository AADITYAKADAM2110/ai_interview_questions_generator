from agents.supervisor.supervisor import SupervisorAgent
from schemas.validator import validate_output
from variables import role, experience_level


def main():
    supervisor_agent = SupervisorAgent()
    response = supervisor_agent.run(role, experience_level)
    validate_output(response)
    print(response)
        


if __name__ == "__main__":
    main()
