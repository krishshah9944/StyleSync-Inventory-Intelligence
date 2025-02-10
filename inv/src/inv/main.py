#!/usr/bin/env python
import sys
import warnings
import os
from dotenv import load_dotenv
from inv.crew import Inv

# Load the .env file from the correct directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

print("Groq API Key:", os.getenv("GROQ_API_KEY"))
print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    print("Starting run function...")  # Debugging statement
    
    city = input("Enter city: ")
    csv_path = input("Enter path to inventory CSV file: ")

    inputs = {
        'city': city,
        'inventory_csv': csv_path
    }
    if not os.path.exists(csv_path):
        print(f"❌ Error: CSV file not found at {csv_path}")
        return

    # ✅ Pass city and csv_path when creating the Inv object
    inventory_crew = Inv(city, csv_path)  

    # ✅ Now call kickoff properly
    inventory_crew.crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "city": input("Enter city for training: "),
        "inventory_csv": input("Enter path to inventory CSV for training: ")
    }
    try:
        Inv().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Inv().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        "city": input("Enter city for testing: "),
        "inventory_csv": input("Enter path to inventory CSV for testing: ")
    }
    try:
        Inv().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
    print("run")
