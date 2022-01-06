import pandas as pd 
import numpy as np
from tqdm import tqdm
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from nba_api.stats.endpoints import commonallplayers
from nba_api.stats.endpoints import playercareerstats
import time

print('Starting')


def get_players():
    all_players = commonallplayers.CommonAllPlayers(timeout=2000).get_data_frames()[0]
    all_players['TO_YEAR'] = all_players['TO_YEAR'].astype('int64')
    all_players = all_players[all_players['TO_YEAR']>=2000]
    print(all_players.head(5))
    # extract all IDs
    players_ID = all_players['PERSON_ID']
    # initial an empty dataframe
    players_stats = pd.DataFrame()
    # save fail queries
    error_log = []
    # extracting stats
    all_players.to_csv('all_players.csv')
    players_ID.to_csv('players_id.csv')
    for ID in tqdm(players_ID):
        try:
            time.sleep(0.5) # avoid too many queries submitted at the same time
            career = playercareerstats.PlayerCareerStats(player_id=ID)
            player_career = career.get_data_frames()[0]
            players_stats = pd.concat([players_stats,player_career],axis=0,ignore_index=True)
            player_stats.to_csv('player_stats.csv')
        except:
            error_log.append(ID)
    # errors = error_teams.to_csv('error_teams.csv')
    with open("player_stats.pkl","wb") as f:
        pickle.dump(player_stats,f)

get_players()

print(finished)