import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Files/nflTeams.csv')

nfl_dict = {"name":"name","abv":"abv"}
nfl_dicts = []

urls = []


df = pd.read_csv(filename)
names = pd.DataFrame(df).iterrows()

x = 0

for i in names:
    nfl_dict = {"name": i[1][0], "abv": i[1][1], "{}".format(i[1][1]):x}
    nfl_dicts.append(nfl_dict)
    x += 1

print(nfl_dicts)

#Nfl Players

#Nfl Fun Facts