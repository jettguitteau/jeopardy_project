import pandas as pd

# Ensure that the whole column's content is visible. 
pd.set_option('display.max_colwidth', None)

# Import jeopardy.csv as a DataFrame.
jeopardy = pd.read_csv('jeopardy.csv')

# Column names contain white space that needs to be stripped. 
jeopardy.columns = jeopardy.columns.str.strip()

# Defining a function that allows for input to search for a user's desired words in question list. 
def filter_questions_by_words(df):
    words_requested = input("Enter words to search for, separated by spaces: ").split()
    input_words = [word.lower() for word in words_requested]

    filtered_jeopardy = df[df["Question"].apply(
        lambda q: all(word in q.lower() for word in input_words)
    )]

    print(filtered_jeopardy['Question'])

# Removing special characters from question values, and converting to numeric. 
jeopardy.Value = jeopardy.Value.str.replace("$", "").str.replace(",", "")
jeopardy.Value = pd.to_numeric(jeopardy.Value, errors="coerce")

# Added function to categorize question difficulty based on value. 
def categorize_difficulty(value):
    if pd.isna(value):
        return "Unknown"
    elif value <= 600:
        return "Easy"
    elif value <= 1200:
        return "Medium"
    else:
        return "Hard"

# Applied prior function to create difficulty column to jeopardy data. 
jeopardy["Difficulty"] = jeopardy["Value"].apply(categorize_difficulty)

# Defined function to count unique answers when given input filtering for terms in a question. 
def count_unique_answers(df):
    words_to_search = input("Enter words to search for, separated by spaces: ").split()
    words_input = [word.lower() for word in words_to_search]

    search_pattern = ' '.join(words_input)

    filtered_df = df[df['Question'].str.contains(search_pattern, case=False, na=False)]

    answer_counts = filtered_df['Answer'].value_counts(dropna=True)

    return answer_counts
