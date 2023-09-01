import requests
import pandas as pd



# every cyclist has (bib, name, cost, score)
# dict(bib) -> (name, cost, score)
# -> sort dict by score?

# Algo -> not optimal (rider of cost 5 + rider of cost 0 might be worse choice than rider of cost 2 + rider of cost 3)
# 1. sort by score; budget = 20; team_score = 0;
# 2. add rider with highest score and 0 cost as secret weapon
# 3. add rider with highest score and cost <= budget to team; budget -= cost; team_score += score
# 4. repeat 3. x times
# 5. add rider with lowest score and cost = initial budget-20 as kluns
# 6. repeat 1-5. for buget = 21, 22, 23, 24, 25

startlist = {}

# import url into table
def import_url(url):
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[0]
    print(df)



# add cyclists to startlist
def populate_startlist():
    return