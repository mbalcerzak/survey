import pandas as pd
import json


def get_questions():
    '''Creates JSON dict with questions for a colon cancer questionnaire'''

    # path = 'data/ICHOM_PROM_colon_cancer.csv'
    path = 'data/Cancer.csv'
    df = pd.read_csv(path)

    df = df[['Number','Question']].loc[df['Number'] > 0]
    df['Number'] = df['Number'].apply(lambda x: int(x))

    questions = dict(zip([int(x) for x in df['Number']],df['Question']))

    with open('data/questions.json', 'w') as f:
        json.dump(questions, f)


if __name__ == "__main__":
    get_questions()