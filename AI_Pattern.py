import getpass
import os
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
import json

# Assuming Groq API key setup (if not set in environment already)
if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

# Define the LLM model using Groq
llm = ChatGroq(model="llama3-8b-8192")

# Load your files
with open("api_1_cleaned.json") as f1, open("api_2_cleaned.json") as f2:
    quiz_data = json.load(f1)
    user_data = json.load(f2)

# Prepare documents based on quiz data
documents = []
for question in quiz_data["questions"]:
    content = f"Question: {question['description']}\nAnswer Choices: " + ', '.join([opt['description'] for opt in question['options']])
    documents.append(Document(page_content=content, metadata={"question_id": question["id"], "topic": question["topic"]}))

# Define a prompt template for the task at hand
prompt = ChatPromptTemplate.from_template("""
Task: Analyze the performance of a student based on quiz results and propose actionable improvement steps.

Student Data:
- User ID: {user_id}
- Quiz Title: {quiz_title}
- Correct Answers: {correct_answers}
- Incorrect Answers: {incorrect_answers}
- Accuracy: {accuracy}
- Performance Trends: {performance_trends}
- Weak Areas: {weak_areas}
- Improvement Suggestions: {suggestions}

Quiz Data (for context):
{context}

Please provide insights on the student's performance and suggest improvement strategies.
Propose actionable steps for the user to improve, such as suggested topics, question types, or difficulty levels to focus on.
""")

# Create the chain to process and generate answers
chain = create_stuff_documents_chain(llm, prompt)

# Extract performance data from user_data
performance_trends = []
weak_areas = []
suggestions = []

for question_id, answer_id in user_data["response_map"].items():
    question = next((q for q in quiz_data["questions"] if str(q["id"]) == question_id), None)
    if question is None:
        continue
    option = next((opt for opt in question["options"] if str(opt["id"]) == answer_id), None)
    if option is None:
        continue

    if option["is_correct"]:
        performance_trends.append(f"Correct answer on topic {question['topic']}")
    else:
        weak_areas.append(f"Incorrect answer on question about {question['topic']}")
        suggestions.append(f"Review the topic {question['topic']} for better understanding.")

# Create the prompt inputs
inputs = {
    "user_id": user_data["User_ID"],
    "quiz_title": user_data["quiz_title"],
    "correct_answers": user_data["Correct_ans"],
    "incorrect_answers": user_data["Incorrect_ans"],
    "accuracy": user_data["Accuracy"],
    "performance_trends": performance_trends,
    "weak_areas": weak_areas,
    "suggestions": suggestions,
    "context": documents
}

# Run the chain to get the insights and improvement plan
result = chain.invoke(inputs)

# Output the result
print(result)