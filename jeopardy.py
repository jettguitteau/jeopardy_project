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

    return df[df["Question"].apply(
        lambda q: all(word in q.lower() for word in input_words)
    )]

# Call the function and apply resutls only to the question column.
filtered_jeopardy = filter_questions_by_words(jeopardy)
print(filtered_jeopardy['Question'])

