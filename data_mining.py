#Import packages
import pandas as pd
import time
from tqdm import tqdm
from nba_api.stats.endpoints import commonallplayers
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

all_players = pd.read_csv('./all_players.csv')
all_players

# Create list of all the player IDs
players_ids = all_players['PERSON_ID']
players_ids

#Test getting stats for 1 player
career = playercareerstats.PlayerCareerStats(player_id=76001)
player_career = career.get_data_frames()[0]
player_career

# initial an empty dataframe
players_stats = pd.DataFrame()
# save fail queries
error_log = []
# extracting stats
for ID in tqdm(players_ids):
    try:
        time.sleep(1) # avoid too many queries submitted at the same time
        career = playercareerstats.PlayerCareerStats(player_id=ID)
        player_career = career.get_data_frames()[0]
        players_stats = pd.concat([players_stats,player_career],axis=0,ignore_index=True)
    except:
        error_log.append(ID)

players_stats
#Export player_stats into a csv
players_stats.to_csv('player_data.csv')
#Export list of players that errrored out
error_df = pd.DataFrame(error_log)
error_df.to_csv('error_log.csv')