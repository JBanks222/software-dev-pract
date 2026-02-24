"""
Jalen Banks
lab 8, API
Feb 24 , 2026
"""
# Example 1: Dataframe using pandas
import pandas as pd

dict_ = {
    'a':[11,21,31],
    'b':[12,22,32],
}

# create a dataframe using pandas
df = pd.DataFrame(dict_)

# head method of the dataframe communictes with the API to get the first few rows of the dataframe
print("\n example 1:simple API")
print(df.head())    

# mean method calculates and returns the mean of a df
print(f"the mean value is = \n{df.mean()}")

# Example 2: Get NBA team from static.py file

from static import get_teams

nba_teams = get_teams()

# testing
print(f"the first two teams: {nba_teams[:2]}")

# step 2, create dataframe
df_teams = pd.DataFrame(nba_teams)
print("\n ALL TEAMS IN THE DATAFRAME")
print(df_teams.head())

# step 3, working with the data in df_teams
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print("\n WARRIORS TEAM INFO")
print(df_warriors)

# example 3: working with external API

#step 1, data collection
# download the pickle file

import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

file_name = "Golden_State.pkl"

print("\n downloading the pickle file...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
        print("File downloaded successfully.")
else:
    print(f"Error: Failed to download file. Status code: {response.status_code}")

# step 2, create dataframe from the pickle file
games = pd.read_pickle(file_name)
print("\n GAMES DATAFRAME")
print("\nGames from pickle file:")
print(games.head())

# step 3, working with the data in games dataframe
# fitler the GSW vs Raptors
warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]

gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains('vs')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains('@')]   

# testing
print("\n GSW home games")
print(gsw_home_vs_raptors)
# calculate the average of the home and away matches

home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"\nAverage PLUS_MINUS for home games: {home_avg_plus}")
print(f"Average PLUS_MINUS for away games: {away_avg_plus}")
print(f"Average PTS for home games: {home_avg_pts}")
print(f"Average PTS for away games: {away_avg_pts}")

import matplotlib.pyplot as plt

metrics = ['PLUS_MINUS', 'PTS']
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8,5))
plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label='Home', color='blue')
plt.bar([i + bar_width/2 for i in x], away_values, width=bar_width, label='Away', color='red')
plt.xticks(x, metrics)
plt.xlabel('Metrics')
plt.ylabel('Average Values')
plt.title('GSW vs Raptors: Home and Away Performance')
plt.legend()
plt.show(block=True)

input("Press Enter to exit...")