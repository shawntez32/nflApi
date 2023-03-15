import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Files/nflTeams.csv')

nfl_dict = {"name":"name","abv":"abv"}
nfl_dicts = []

urls = ["ATL","BUF","CAR","CHI","CIN","CLE","CLT","CRD","DAL","DEN","DET","Gnb","HTX","JAx","Kan","MIA","MIN","NOR","Nwe","NYG","NYJ","OTI","PHI","PIT","rai","RAM","rav","SDG","SEA","SFo","Tam","WAS"]


print(len(urls))

#Nfl Players

#Nfl Fun Facts