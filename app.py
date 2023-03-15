from fastapi import FastAPI
import sys, os
sys.path.append(os.path.dirname((__file__)) + "/nflFiles/")
from nflGameLines import *
from nflGetData import *

app = FastAPI()

@app.get("/")
def home():
    return {"Data":"Set"}

@app.get("/nfl/gamelines")
def get_lines():
    return {"Data":nfl_game_lines}
a = 0
@app.get("/nfl/{team}/{year}")
def get_stats(team,year):
    results = []
    try:
        x = NflTeam()
        results = x.get_stats(team,year)
        return {"Team_Stats":results[0],"Opp_Team":results[1]}
    except:
        data = 'wait'
        return {"Data":data}
    print(results)
