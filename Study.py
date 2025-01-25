import requests
import pandas as pd
import json
from flatten_json import flatten

# ---------------------- Utility Functions ---------------------- #

def fetch_api_data(url):
    """
    Fetches JSON data from a given API URL.
    
    Parameters:
        url (str): The API endpoint.

    Returns:
        dict or list: JSON response data.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data from {url}, status code: {response.status_code}")

def flatten_data(data):
    """
    Flattens nested JSON data using the flatten_json library.

    Parameters:
        data (list or dict): JSON data to flatten.

    Returns:
        list: Flattened data.
    """
    return [flatten(item) for item in data]

def clean_json(data, keys_to_remove):
    """
    Recursively removes specified keys from JSON data.

    Parameters:
        data (dict or list): JSON data to clean.
        keys_to_remove (list): Keys to remove from the JSON data.

    Returns:
        dict or list: Cleaned JSON data.
    """
    if isinstance(data, dict):
        return {key: clean_json(value, keys_to_remove) 
                for key, value in data.items() if key not in keys_to_remove}
    elif isinstance(data, list):
        return [clean_json(item, keys_to_remove) for item in data]
    else:
        return data

def filter_json(data, required_keys):
    """
    Filters JSON data to retain only the specified keys.

    Parameters:
        data (dict or list): JSON data to filter.
        required_keys (list): Keys to retain in the JSON data.

    Returns:
        dict or list: Filtered JSON data.
    """
    if isinstance(data, dict):
        return {key: filter_json(value, required_keys) for key, value in data.items() if key in required_keys}
    elif isinstance(data, list):
        return [filter_json(item, required_keys) for item in data]
    else:
        return data

# ---------------------- Data Processing Functions ---------------------- #

def process_api_1(url):
    """
    Processes data from API 1 by fetching, flattening, and cleaning it.

    Parameters:
        url (str): API endpoint.

    Returns:
        dict: Cleaned and filtered JSON data.
    """
    data = fetch_api_data(url)
    required_keys = ["id", "title", "negative_marks", "correct_answer_marks", "questions_count", "max_mistake_count"]
    question_keys = ["id", "description", "topic", "detailed_solution"]
    option_keys = ["id", "description", "is_correct", "unanswered"]

    filtered_data = filter_json(data["quiz"], required_keys)

    if "questions" in data["quiz"]:
        filtered_data["questions"] = []
        for question in data["quiz"]["questions"]:
            filtered_question = filter_json(question, question_keys)
            if "options" in question:
                filtered_question["options"] = [filter_json(option, option_keys) for option in question["options"]]
            filtered_data["questions"].append(filtered_question)

    return filtered_data

def process_api_2(url):
    """
    Processes data from API 2 by fetching, flattening, and cleaning it.

    Parameters:
        url (str): API endpoint.

    Returns:
        dict: Cleaned JSON data.
    """
    data = fetch_api_data(url)
    cleaned_data = {
        "User_ID": data.get("user_id"),
        "Quiz_ID": data.get("quiz_id"),
        "Score": data.get("score"),
        "Accuracy": data.get("accuracy"),
        "Speed": data.get("speed"),
        "Final_Score": data.get("final_score"),
        "Correct_ans": data.get("correct_answers"),
        "Incorrect_ans": data.get("incorrect_answers"),
        "response_map": data.get("response_map"),
        "quiz_title": data.get("quiz", {}).get("title")
    }
    return cleaned_data

def process_quiz_results(url):
    """
    Processes quiz results data from a given API URL by flattening and cleaning it.

    Parameters:
        url (str): API endpoint.

    Returns:
        DataFrame: Cleaned and processed data as a Pandas DataFrame.
    """
    data = fetch_api_data(url)
    flattened_data = flatten_data(data)
    df = pd.DataFrame(flattened_data)

    # Columns to remove
    columns_to_remove = [
        'submitted_at', 'created_at', 'updated_at', 'score', 'trophy_level', 'source', 'type',
        'started_at', 'ended_at', 'rank_text', 'mistakes_corrected', 'initial_mistake_count',
        'quiz_name', 'quiz_description', 'quiz_difficulty_level', 'quiz_topic', 'quiz_time',
        'quiz_is_published', 'quiz_created_at', 'quiz_updated_at', 'quiz_duration', 'quiz_end_time',
        'quiz_shuffle', 'quiz_show_answers', 'quiz_lock_solutions', 'quiz_is_form', 'quiz_show_mastery_option',
        'quiz_reading_material', 'quiz_quiz_type', 'quiz_is_custom', 'quiz_banner_id', 'quiz_exam_id',
        'quiz_show_unanswered', 'quiz_ends_at', 'quiz_lives', 'quiz_live_count', 'quiz_coin_count',
        'quiz_questions_count', 'quiz_daily_date', 'quiz_max_mistake_count', 'quiz_reading_materials', 'user_id'
    ]

    # Remove columns starting with 'response_map'
    columns_to_remove += [col for col in df.columns if col.startswith('response_map')]

    cleaned_df = df.drop(columns=columns_to_remove, errors='ignore')
    return cleaned_df.sort_values(by='quiz_id')

# ---------------------- Main Execution ---------------------- #

def main():
    api_1_url = "https://www.jsonkeeper.com/b/LLQT"
    api_2_url = "https://api.jsonserve.com/rJvd7g"
    quiz_results_url = "https://api.jsonserve.com/XgAgFJ"

    # Process APIs
    print("Processing API 1 data...")
    api_1_cleaned_data = process_api_1(api_1_url)
    with open('api_1_cleaned.json', 'w') as f:
        json.dump(api_1_cleaned_data, f, indent=4)
    print("API 1 data saved to api_1_cleaned.json")

    print("Processing API 2 data...")
    api_2_cleaned_data = process_api_2(api_2_url)
    with open('api_2_cleaned.json', 'w') as f:
        json.dump(api_2_cleaned_data, f, indent=4)
    print("API 2 data saved to api_2_cleaned.json")

    print("Processing quiz results...")
    quiz_results_df = process_quiz_results(quiz_results_url)
    quiz_results_df.to_csv('quiz_results_cleaned.csv', index=False)
    print("Quiz results saved to quiz_results_cleaned.csv")

if __name__ == "__main__":
    main()
