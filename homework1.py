import pandas as pd
import numpy as np

#  check the correct

correct = pd.read_csv('industry_ANZSIC.csv')

industry_code_name = dict(zip(correct.industry_code_ANZSIC.unique(), correct.industry_name_ANZSIC.unique()))


def industry1(unit, file):
    industry_2 = []

    for i in np.array(file[[str(unit)]])[1:]:
        industry_2.append(i[0])

    return dict(zip(correct.variable, industry_2))


industry_variable_unit = industry1('unit', correct)

print(industry_code_name)

#  check the mistake

mistake = pd.read_csv('mistake1.csv').values


def comparison(corrdict, n, m):
    flag = True
    for i in range(len(mistake)):
        if corrdict[mistake[i][n]] != mistake[i][m]:
            flag = False
            if mistake[i - n][m] == mistake[i + n][m]:
                mistake[i][m], mistake[i][n] = mistake[i + n][m], mistake[i + n][n]
                print(i + 2)
            else:
                print(f'Сами ищите свою ошибку! Cтрока №{i + 2}')

    if flag:
        print('correct')


comparison(industry_code_name, 1, 2)

frame = pd.DataFrame(mistake)
frame.to_csv('mistake1.csv', index=False)