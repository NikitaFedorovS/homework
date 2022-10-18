import pandas as pd

data = pd.read_csv('Baesovsky1.csv')

df_Color = (data['Color'].value_counts())
df_Type = data['Type'].value_counts()
df_Origrin = data['Origrin'].value_counts()


# check color_type_origin
def color_type_prigin(x):
    df_yes = pd.DataFrame(data[data['Stolen?'] == 'Yes'][x].value_counts())
    df_yes.rename(columns={x: 'Yes'}, inplace=True)
    df_yes['No'] = [0, 0]

    df_no = pd.DataFrame(data[data['Stolen?'] == 'No'][x].value_counts())
    df_no.rename(columns={x: 'No'}, inplace=True)
    df_no['Yes'] = [0, 0]

    df_yes1 = pd .DataFrame(data[data['Stolen?'] == 'Yes'][x].value_counts()/5)
    df_yes1.rename(columns={x: 'Yes'}, inplace=True)
    df_yes1['No'] = [0, 0]

    df_no1 = pd.DataFrame(data[data['Stolen?'] == 'No'][x].value_counts()/5)
    df_no1.rename(columns={x: 'No'}, inplace=True)
    df_no1['Yes'] = [0, 0]

    df_frequency = df_yes1 + df_no1
    return df_frequency


print(color_type_prigin('Color') + '\n')
print(color_type_prigin('Type') + '\n')
print(color_type_prigin('Origin') + '\n')
print('----------\n')

print(color_type_prigin('Color')['Yes']['Red']*color_type_prigin('Type')['Yes']['SUV']*color_type_prigin('Origin')['Yes']['Domestic'])
print(color_type_prigin('Color')['No']['Red']*color_type_prigin('Type')['No']['SUV']*color_type_prigin('Origin')['No']['Domestic'])
