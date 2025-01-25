import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------- Data Loading ---------------------- #

def load_data(file_path):
    """
    Loads student quiz data from a CSV file into a Pandas DataFrame.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(file_path)

# ---------------------- Data Analysis ---------------------- #

def explore_data(df):
    """
    Explores the dataset by displaying summary statistics and unique values.

    Parameters:
        df (DataFrame): Input DataFrame.
    """
    print("\n--- Dataset Info ---\n")
    print(df.info())
    print("\n--- Summary Statistics ---\n")
    print(df.describe())
    print("\n--- Unique Quiz Titles ---\n")
    print(df['quiz_title'].unique())

# ---------------------- Visualizations ---------------------- #

def plot_average_scores_by_quiz(df):
    """
    Creates a bar chart comparing average final scores by quiz title.

    Parameters:
        df (DataFrame): Input DataFrame.
    """
    avg_scores = df.groupby('quiz_title')['final_score'].mean().sort_values()
    plt.figure(figsize=(10, 6))
    avg_scores.plot(kind='barh', color='skyblue')
    plt.title('Average Final Scores by Quiz Title')
    plt.xlabel('Average Final Score')
    plt.ylabel('Quiz Title')
    plt.tight_layout()
    plt.show()

def plot_accuracy_distribution(df):
    """
    Creates a histogram showing the distribution of accuracy.

    Parameters:
        df (DataFrame): Input DataFrame.
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(df['accuracy'].str.rstrip('%').astype(float), kde=True, color='green', bins=10)
    plt.title('Accuracy Distribution')
    plt.xlabel('Accuracy (%)')
    plt.ylabel('Frequency')
    plt.show()

def plot_speed_vs_final_score(df):
    """
    Creates a scatter plot showing the relationship between speed and final score.

    Parameters:
        df (DataFrame): Input DataFrame.
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['speed'], y=df['final_score'], hue=df['quiz_title'], palette='tab10')
    plt.title('Speed vs Final Score')
    plt.xlabel('Speed')
    plt.ylabel('Final Score')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def plot_question_attempts_by_quiz(df):
    """
    Creates a bar chart showing total questions attempted per quiz.

    Parameters:
        df (DataFrame): Input DataFrame.
    """
    total_questions = df.groupby('quiz_title')['total_questions'].sum().sort_values()
    plt.figure(figsize=(10, 6))
    total_questions.plot(kind='bar', color='coral')
    plt.title('Total Questions Attempted by Quiz Title')
    plt.xlabel('Quiz Title')
    plt.ylabel('Total Questions')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# ---------------------- Main Execution ---------------------- #

def main():
    # Load the dataset
    file_path = 'quiz_results_cleaned.csv'
    df = load_data(file_path)

    # Explore the dataset
    explore_data(df)

    # Visualizations
    print("\n--- Creating Visualizations ---\n")
    plot_average_scores_by_quiz(df)
    plot_accuracy_distribution(df)
    plot_speed_vs_final_score(df)
    plot_question_attempts_by_quiz(df)

if __name__ == "__main__":
    main()
