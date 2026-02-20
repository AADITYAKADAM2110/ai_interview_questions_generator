from agents.workers.junior import junior_agent
from agents.workers.mid import mid_agent
from agents.workers.senior import senior_agent
from variables import role, experience_level

def main():
    print("Interview Question Generator\n")

    if experience_level == '1':
        response = junior_agent.run()
        print(f"\nGenerating interview questions for {role}...")
        print(response)
        

    elif experience_level == '2':
        response = mid_agent.run()
        print(f"\nGenerating interview questions for {role}...")
        print(response)
        

    elif experience_level == '3':
        response = senior_agent.run()
        print(f"\nGenerating interview questions for {role}...")
        print(response)
        
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        


if __name__ == "__main__":
    main()
