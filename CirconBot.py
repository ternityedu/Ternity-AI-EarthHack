import os
import dotenv

from openai import OpenAI
import requests

dotenv.load_dotenv()
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

# Create two assistants, one an investor with knowledge of research from Big 4 consulting firms, the other a scholar with knowledge of research from academic journals. Both will consider Novelty (How different is it from existing solutions?) from the kinds of solutions they've seen in their respective fields.

# Investor assistant
investor = client.beta.assistants.create(
  instructions="You are an advisor to VC investor who invests in sustainable business ideas with a recent focus on circular economy ideas. I will give you problems and solutions for circular economy ideas. Your task is to evaluate innovative circular economy business opportunities and startup pitches. You are to make decision-making for investors sharper, more efficient, and possibly less prone to their behavioral biases.",
  # Ask to focus on Financial Impact (What financial value can it create for businesses?) and Feasibility and Scalability of Implementation (How likely is it to succeed and how scalable is it?) from an economic and business perspective.
  model="gpt-4-1106-preview",
  tools=[{"type": "retrieval"}]
)

# Upload a file with an "assistants" purpose
file = client.files.create(
  file=open("knowledge.pdf", "rb"),
  purpose='assistants'
)

# Load in list of consulting research


# Add the file to the assistant
assistant = client.beta.assistants.create(
  instructions="You are a customer support chatbot. Use your knowledge base to best respond to customer queries.",
  model="gpt-4-1106-preview",
  tools=[{"type": "retrieval"}],
  file_ids=[file.id]
)

# Scholar assistant
scholar = client.beta.assistants.create(
  instructions="...",
  # Ask to focus on Environmental Impact (How much does it benefit the planet? Energy impact?) and Feasibility and Scalability of Implementation (How likely is it to succeed and how scalable is it?) from an technological and scientific perspective.
  model="gpt-4-1106-preview",
  tools=[{"type": "retrieval"}]
)

def get_assistant_response(assistant, prompt):
    response = client.Completion.create(
        model="gpt-4-1106-preview", 
        prompt=prompt, 
        max_tokens=1000,
    )
    return response.choices[0].text

def combined_evaluation(problem, solution):
    # Investor evaluates the idea
    investor_prompt = f"Evaluate this circular economy idea from an investment perspective:\nProblem: {problem}\nSolution: {solution}"
    investor_evaluation = get_assistant_response(investor, investor_prompt)

    # Scholar evaluates the idea
    scholar_prompt = f"Evaluate this circular economy idea from a scholarly perspective:\nProblem: {problem}\nSolution: {solution}"
    scholar_evaluation = get_assistant_response(scholar, scholar_prompt)

    # Combine the evaluations
    combined_response = f"Investor's Evaluation:\n{investor_evaluation}\n\nScholar's Evaluation:\n{scholar_evaluation}"
    return combined_response

def main():
    problem = input("Enter the circular economy problem: ")
    solution = input("Enter your solution: ")

    print("\nCombined Evaluation:")
    print(combined_evaluation(problem, solution))

