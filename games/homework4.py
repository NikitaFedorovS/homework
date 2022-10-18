import pandas as pd

ds = pd.read_csv('exams.csv')


# mean
def mean_race(ds_mean):
    score = ds_mean.groupby('gender')['math_score', 'reading_score', 'writing_score'].mean()
    score['meam_score'] = (score['math_score'] + score['reading_score'] + score['writing_score']) / 3
    return f'\n {score} \n________________________________________________________________________________\n'


# group by race
def group_race(x):
    x = ds.query(f"race_ethnicity == '{x}'")
    return x


# to csv
with open(f'group_race.txt', 'w', encoding='utf-8') as file:
    for i in sorted(list(set(ds.race_ethnicity))):
        file.write(f'{i}')
        file.write(mean_race(group_race(i)))
