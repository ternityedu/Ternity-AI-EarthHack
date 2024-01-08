import pandas as pd
import utils

# change data_filename for texting dataset
DATA_FILENAME = 'AI EarthHack Dataset.csv'
CLEANED_DATASET = 'dataset_cleaned.pkl'
WORDCLOUD_FILENAME = 'wordcloud.png'


try:
    df = pd.read_pickle(CLEANED_DATASET)
except FileNotFoundError:
    df = utils.load_csv(DATA_FILENAME)
    # Apply the text cleaning function to 'problem' and 'solution' columns
    df['cleaned_problem'] = df['problem'].apply(utils.clean_text)
    df['cleaned_solution'] = df['solution'].apply(utils.clean_text)

    # Display the cleaned DataFrame
    # print(df[['id', 'cleaned_problem', 'cleaned_solution']])
    df.to_pickle(CLEANED_DATASET)


# Assuming 'cleaned_problem' and 'cleaned_solution' columns are available in the DataFrame
# text_combined = ' '.join(df['cleaned_problem'] + ' ' + df['cleaned_solution'])
text_combined = ' '.join(df['cleaned_solution'])
utils.createWordCloud(text_combined, 'solution_' + WORDCLOUD_FILENAME)

text_combined = ' '.join(df['cleaned_problem'])
utils.createWordCloud(text_combined, 'problem_' + WORDCLOUD_FILENAME)
