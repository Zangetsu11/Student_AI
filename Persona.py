import pandas as pd
import random

# ---------------------- Persona Generator ---------------------- #

def generate_student_persona_from_csv(csv_path):
    """
    Generates a student persona based on the provided CSV data.

    Args:
        csv_path (str): Path to the CSV file containing student performance data.

    Returns:
        dict: A dictionary containing the student persona details.
    """
    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Calculate insights from the data
    total_quizzes = df['quiz_id'].nunique()
    avg_accuracy = df['accuracy'].str.rstrip('%').astype(float).mean()
    avg_speed = df['speed'].mean()
    strong_subjects = df[df['accuracy'].str.rstrip('%').astype(float) > 90]['quiz_title'].unique()
    weak_subjects = df[df['accuracy'].str.rstrip('%').astype(float) < 70]['quiz_title'].unique()

    name = "7ZXdz3zHuNcdg9agb5YpaOGLQqw2" 

    # Short biography or summary
    bio = (
        f"{name} is a dedicated student who has participated in {total_quizzes} quizzes. "
        "They excel in certain subjects but struggle with others, as shown by their performance data. "
        "They are committed to improving their skills and achieving academic success."
    )

    # Summary of goals, motivations, and challenges
    goals = (
        f"Improve overall accuracy from the current average of {avg_accuracy:.2f}% to above 95%. "
        "Develop speed and precision to answer questions under timed conditions."
    )
    motivations = (
        "Motivated by a desire to excel academically and secure a place in a prestigious university. "
        "Inspired by the opportunity to make a meaningful contribution to their field of interest."
    )
    challenges = (
        f"Struggles with topics in quizzes like {', '.join(weak_subjects)}. "
        "Needs to focus on time management and dealing with exam pressure."
    )


    # Relevant quotes
    quotes = [
        "Mistakes are proof that you are trying.",
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "Don’t let what you cannot do interfere with what you can do. - John Wooden"
    ]

    # Combine all details into a persona dictionary
    persona = {
        "Name": name,
        "Biography": bio,
        "Goals": goals,
        "Motivations": motivations,
        "Challenges": challenges,
        "Strengths": list(strong_subjects),
        "Weaknesses": list(weak_subjects),
        "Quotes": random.choice(quotes)
    }

    return persona

# ---------------------- Main Execution ---------------------- #

def main():
    csv_path = "quiz_results_cleaned.csv"  # Update with the correct path to your CSV file
    persona = generate_student_persona_from_csv(csv_path)

    print("\n--- Student Persona ---\n")
    for key, value in persona.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        elif isinstance(value, list):
            print(f"{key}: " + "\n  ".join(value))
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
