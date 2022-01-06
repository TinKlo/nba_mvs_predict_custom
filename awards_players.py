import pandas as pd
from tqdm import tqdm
import time
from nba_api.stats.endpoints import playerawards


def players_awards(players_ID):
    players_awards = pd.DataFrame()
    error_awards = []
    for ID in tqdm(players_ID):
        try:
            time.sleep(0.05)
            award = playerawards.PlayerAwards(player_id=ID)
            award.get_data_frames()[0]
            players_awards = pd.concat([players_awards,award.get_data_frames()[0]],axis=0,ignore_index=True)
        except:
            error_awards.append(ID)
    for ID in tqdm(error_awards):
        time.sleep(0.05)
        award = playerawards.PlayerAwards(player_id=ID)
        award.get_data_frames()[0]
        players_awards = pd.concat([players_awards,award.get_data_frames()[0]],axis=0,ignore_index=True)
    with open("players_awards.pkl","wb") as f:
        pickle.dump(players_awards,f)
    return print('sucesso')

source_file = pd.read_csv('players_id.csv')

players_awards(source_file)