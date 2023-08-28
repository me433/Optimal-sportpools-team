import requests
import pandas as pd



# every cyclist has (bib, name, cost, score)
# dict(bib) -> (name, cost, score)

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