import pandas as pd
import glob

###
data = pd.read_csv('games/games.csv').sort_values(by='white_rating')

data1 = data[:5015]
data2 = data[5015:10030]
data3 = data[10030:15045]
data4 = data[15045:]

datalist = [data1, data2, data3, data4]
columns = ['opening_name']

###
c = 1
for i in datalist:

    df = pd.DataFrame(i['opening_name'].value_counts(), columns=columns)
    df[:10].to_csv(f"result{c}.csv")

    fd = open(f'result{c}.csv', 'a')
    my_list = i["white_rating"].values
    ###
    sum_my_list = sum(my_list[int(0.1*len(my_list)):int(0.9*len(my_list))])
    fd.write(f'----------        {int(sum_my_list/len(my_list))}        ----------')
    fd.close()
    c += 1

###
df1 = pd.DataFrame(data['opening_name'].value_counts(), columns=columns)
df1[:10].to_csv(r'result.csv')
fd1 = open('result.csv', 'a')
fd1.write('--------------------------------------------------------------------------')
fd1.close()

###
files = glob.glob('*.csv')
files.sort()
combined = pd.DataFrame()

for file in files:
    data = pd.read_csv(file)
    combined = pd.concat([combined, data])

combined.to_csv('games/file_.csv')