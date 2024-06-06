import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import math
import numpy as np
from nba_api.stats.static import players,teams
from nba_api.stats.endpoints import playergamelog,playercareerstats,leagueleaders,leaguedashplayerclutch,leaguedashplayershotlocations,playerawards,playernextngames,playerprofilev2,shotchartdetail,winprobabilitypbp,playerdashboardbylastngames,boxscoresummaryv2,boxscoretraditionalv2,leaguegamefinder
import requests
from bs4 import BeautifulSoup

#top 50 per game rankings

def top_50_ppg(): #provides top 50 in ppg
    top_50 = leagueleaders.LeagueLeaders(
        per_mode48='PerGame',
        season='2023-24',
        season_type_all_star='Regular Season',
        stat_category_abbreviation='PTS'
    ).get_data_frames()[0][:50]
    return top_50

def top_50_apg(): #provides top 50 in apg
    top_50 = leagueleaders.LeagueLeaders(
        per_mode48='PerGame',
        season='2023-24',
        season_type_all_star='Regular Season',
        stat_category_abbreviation='AST'
    ).get_data_frames()[0][:50]
    return top_50

def top_50_rpg(): #provides top 50 in rpg
    top_50 = leagueleaders.LeagueLeaders(
        per_mode48='PerGame',
        season='2023-24',
        season_type_all_star='Regular Season',
        stat_category_abbreviation='REB'
    ).get_data_frames()[0][:50]
    return top_50

def top_50_spg(): #provides top 50 in steals per game
    top_50 = leagueleaders.LeagueLeaders(
        per_mode48='PerGame',
        season='2023-24',
        season_type_all_star='Regular Season',
        stat_category_abbreviation='STL'
    ).get_data_frames()[0][:50]
    return top_50

def top_50_bpg(): #provides top 50 in blocks per game
    top_50 = leagueleaders.LeagueLeaders(
        per_mode48='PerGame',
        season='2023-24',
        season_type_all_star='Regular Season',
        stat_category_abbreviation='BLK'
    ).get_data_frames()[0][:50]
    return top_50

def top_50_tpg(): #provides top 50 in turnovers per game
    top_50 = leagueleaders.LeagueLeaders(
        per_mode48='PerGame',
        season='2023-24',
        season_type_all_star='Regular Season',
        stat_category_abbreviation='TOV'
    ).get_data_frames()[0][:50]
    return top_50

def top_50_eff(): #provides top 50 in efficiency
    top_50 = leagueleaders.LeagueLeaders(
        per_mode48='PerGame',
        season='2023-24',
        season_type_all_star='Regular Season',
        stat_category_abbreviation='EFF'
    ).get_data_frames()[0][:50]
    return top_50

def sga_ppg_rank(): #returns shai's placement as a str
    top_50_list = top_50_ppg()['PLAYER']
    ctr=0
    for player in top_50_list:
        if player == 'Shai Gilgeous-Alexander':
            return ctr+1
        ctr=ctr+1
    return "Not Top 50 in PPG."

def sga_apg_rank(): #returns shai's placement as a str
    top_50_list = top_50_apg()['PLAYER']
    ctr=0
    for player in top_50_list:
        if player == 'Shai Gilgeous-Alexander':
            return ctr+1
        ctr=ctr+1
    return "Not Top 50 in APG."

def sga_rpg_rank(): #returns shai's placement as a str
    top_50_list = top_50_rpg()['PLAYER']
    ctr=0
    for player in top_50_list:
        if player == 'Shai Gilgeous-Alexander':
            return ctr+1
        ctr=ctr+1
    return "Not Top 50 in RPG."

def sga_spg_rank(): #returns shai's placement as a str
    top_50_list = top_50_spg()['PLAYER']
    ctr=0
    for player in top_50_list:
        if player == 'Shai Gilgeous-Alexander':
            return ctr+1
        ctr=ctr+1
    return "Not Top 50 in SPG."

def sga_bpg_rank(): #returns shai's placement as a str
    top_50_list = top_50_bpg()['PLAYER']
    ctr=0
    for player in top_50_list:
        if player == 'Shai Gilgeous-Alexander':
            return ctr+1
        ctr=ctr+1
    return "Not Top 50 in BPG."

def sga_tpg_rank(): #returns shai's placement as a str
    top_50_list = top_50_tpg()['PLAYER']
    ctr=0
    for player in top_50_list:
        if player == 'Shai Gilgeous-Alexander':
            return ctr+1
        ctr=ctr+1
    return "Not Top 50 in TOVPG."

def sga_eff_rank(): #returns shai's placement as a str
    top_50_list = top_50_eff()['PLAYER']
    ctr=0
    for player in top_50_list:
        if player == 'Shai Gilgeous-Alexander':
            return ctr+1
        ctr=ctr+1
    return "Not Top 50 in EFF."



def ppg_graph():
    if isinstance(sga_ppg_rank(),str):
        return 'NOT TOP50'
    else:
        df = top_50_ppg()
        stand_out_bar_index = sga_ppg_rank() -1
        fig = px.bar(df, x=df.index + 1, y='PTS', color='GP', title='LEAGUE LEADERS IN PTS', hover_name='PLAYER', labels={'x':'RANK'})
        #fig.update_traces(marker=dict(color=['rgba(255, 0, 0, 0.8)' if i == stand_out_bar_index else 'rgba(0, 0, 0, 0.6)' for i in range(len(df))]))
        fig.write_html('ppg.html')
        return 'TOP50'


def apg_graph():
    if isinstance(sga_apg_rank(),str):
        return 'NOT TOP50'
    else:
        df = top_50_apg()
        stand_out_bar_index = sga_apg_rank() -1
        fig = px.bar(df, x=df.index + 1, y='AST', color='GP', title='LEAGUE LEADERS IN AST', hover_name='PLAYER', labels={'x':'RANK'})
        #fig.update_traces(marker=dict(color=['rgba(255, 0, 0, 0.8)' if i == stand_out_bar_index else 'rgba(0, 0, 0, 0.6)' for i in range(len(df))]))
        fig.write_html('apg.html')
        return 'TOP50'

def rpg_graph():
    if isinstance(sga_rpg_rank(),str):
        return 'NOT TOP50'
    else:
        df = top_50_rpg()
        stand_out_bar_index = sga_rpg_rank() -1
        fig = px.bar(df, x=df.index + 1, y='REB', color='GP', title='LEAGUE LEADERS IN REB', hover_name='PLAYER', labels={'x':'RANK'})
        #fig.update_traces(marker=dict(color=['rgba(255, 0, 0, 0.8)' if i == stand_out_bar_index else 'rgba(0, 0, 0, 0.6)' for i in range(len(df))]))
        fig.write_html('rpg.html')
        return 'TOP50'

def spg_graph():
    if isinstance(sga_spg_rank(),str):
        return 'NOT TOP50'
    else:
        df = top_50_spg()
        stand_out_bar_index = sga_spg_rank() -1
        fig = px.bar(df, x=df.index + 1, y='STL', color='GP', title='LEAGUE LEADERS IN STL', hover_name='PLAYER', labels={'x':'RANK'})
        #fig.update_traces(marker=dict(color=['rgba(255, 0, 0, 0.8)' if i == stand_out_bar_index else 'rgba(0, 0, 0, 0.6)' for i in range(len(df))]))
        fig.write_html('spg.html')
        return 'TOP50'

def bpg_graph():
    if isinstance(sga_bpg_rank(),str):
        return 'NOT TOP50'
    else:
        df = top_50_bpg()
        stand_out_bar_index = sga_bpg_rank() -1
        fig = px.bar(df, x=df.index + 1, y='BLK', color='GP', title='LEAGUE LEADERS IN BLK', hover_name='PLAYER', labels={'x':'RANK'})
        #fig.update_traces(marker=dict(color=['rgba(255, 0, 0, 0.8)' if i == stand_out_bar_index else 'rgba(0, 0, 0, 0.6)' for i in range(len(df))]))
        fig.write_html('bpg.html')
        return 'TOP50'

def tpg_graph():
    if isinstance(sga_tpg_rank(),str):
        return 'NOT TOP50'
    else:
        df = top_50_tpg()
        stand_out_bar_index = sga_tpg_rank() -1
        fig = px.bar(df, x=df.index + 1, y='TOV', color='GP', title='LEAGUE LEADERS IN TOV', hover_name='PLAYER', labels={'x':'RANK'})
        #fig.update_traces(marker=dict(color=['rgba(255, 0, 0, 0.8)' if i == stand_out_bar_index else 'rgba(0, 0, 0, 0.6)' for i in range(len(df))]))
        fig.write_html('tpg.html')
        return 'TOP50'

def eff_graph():
    if isinstance(sga_eff_rank(),str):
        return 'NOT TOP50'
    else:
        df = top_50_eff()
        stand_out_bar_index = sga_eff_rank() -1
        fig = px.bar(df, x=df.index + 1, y='EFF', color='GP', title='LEAGUE LEADERS IN EFF', hover_name='PLAYER', labels={'x':'RANK'})
        #fig.update_traces(marker=dict(color=['rgba(255, 0, 0, 0.8)' if i == stand_out_bar_index else 'rgba(0, 0, 0, 0.6)' for i in range(len(df))]))
        fig.write_html('eff.html')
        return 'TOP50'



def sga_mvp_odds(): #returns sga MVP odds as dict, according to sportsbook
    url = "https://www.vegasinsider.com/nba/odds/mvp/"
    response = requests.get(url)
    mvp_odds_list =[]

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the tr element with data-name="shai gilgeous-alexander"
        shai_row = soup.find('tr', {'data-name': 'shai gilgeous-alexander'})
        #if present, search for first 6 odds
        if shai_row:
            for i in range(0,6):
                #strips data from row, adds to list
                mvp_odds_list.append((shai_row.find_all('span', class_='data-value')[i].text.strip()))
        else:
            print("Row for 'Shai Gilgeous-Alexander' not found. He is no longer in the MVP race.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        
    keywords = ['365', 'FD', 'MGM', 'CSR', 'PB', 'DK']
    # Create a dictionary using a for loop
    mvp_odds_dict = {}
    for key, value in zip(keywords, mvp_odds_list):
        mvp_odds_dict[key] = value

    return mvp_odds_dict

def sga_last5_performance(): #returns sga per game performance in the last 5 as a dict, according to stats
    #create last 5 games with SGA
    sga_last5 = playerdashboardbylastngames.PlayerDashboardByLastNGames(player_id='1628983', last_n_games='5').get_data_frames()[0]
    #listwords includes stats represented
    listwords = ['PTS', 'MIN', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'W_PCT']
    #loop assigns a value in chronological order
    column_list = [sga_last5[column].values[0] for column in listwords]
    #keywords includes desired presentation
    keywords = ['PPG', 'MPG', 'RPG', 'APG', 'SPG', 'BPG', 'TOV', 'FG%', '3PT%', 'FT%', 'WIN%']
    #res_keywords is used for PCT
    res_keywords = ['FG%', '3PT%', 'FT%', 'WIN%']
    sga_last5_dict = {}
    #loop takes key word and divides stats by 5 (games), for PCT just times 100
    for key, value in zip(keywords, column_list):
        if key in res_keywords:
            sga_last5_dict[key] = value*100 
        else:
            sga_last5_dict[key] = round(value/5,1)
    return sga_last5_dict

def sga_last5_opp_team_record(): #returns combined record of opposing last 5 teams for okc as str
    recent_games = playergamelog.PlayerGameLog(player_id='1628983').get_data_frames()[0]
    last_id = recent_games['MATCHUP']
    last5_teams = []
    for i in range(0,5):
        last5_teams.append(last_id[i])
        last5_teams[i] = last5_teams[i][-3:]

    total_w=0
    total_l=0
    for i in range(0,5):
        team_id = teams.find_team_by_abbreviation(last5_teams[i])['id']
        team = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id, season_nullable='2023-24', season_type_nullable='Regular Season').get_data_frames()[0]
        team_record = team['WL'].values
        for j in range(0,len(team_record)):
            if team_record[j] == 'W':
                total_w=total_w+1
            else:
                total_l=total_l+1
    return str(total_w) + ' - ' + str(total_l)

def sga_next_game(): #returns str of sga's next game time and date
    sga_next_game_data = playernextngames.PlayerNextNGames(player_id='1628983', number_of_games='1').get_data_frames()[0]
    home = sga_next_game_data['HOME_TEAM_ABBREVIATION'].values[0]
    away = sga_next_game_data['VISITOR_TEAM_ABBREVIATION'].values[0]
    time = sga_next_game_data['GAME_TIME'].values[0]
    date = sga_next_game_data['GAME_DATE'].values[0]
    if home == 'OKC':
        enemy = away
    else:
        enemy = home
    return f"SGA and the OKC Thunder will be taking on {enemy} at {time} EST on {date}"



def sga_season_highs(): 
    sga_szn_log = playergamelog.PlayerGameLog(player_id='1628983',season='2023-24').get_data_frames()[0]
    listwords = ['PTS', 'MIN', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FGM', 'FGA', 'FG_PCT', 'FG3A', 'FG3M', 'FG3_PCT', 'PLUS_MINUS']
    column_list = [max(sga_szn_log[column].values) for column in listwords]
    keywords = ['PTS', 'MIN', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FGM', 'FGA', 'FG%', '3PTA', '3PTM', '3PT%', '+/-']
    res_keywords = ['FG%', '3PT%', 'WIN%']
    sga_szn_dict ={}
    for key, value in zip(keywords, column_list):
        if key in res_keywords:
            sga_szn_dict[key] = value*100
        else:
            sga_szn_dict[key] = value
    return sga_szn_dict

def sga_season_avg():
    sga_szn_stats = playergamelog.PlayerGameLog(player_id='1628983',season='2023-24').get_data_frames()[0]
    listwords = ['PTS', 'MIN', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FG_PCT', 'FG3_PCT','FT_PCT']
    column_list = [sga_szn_stats[column].sum() for column in listwords]
    keywords = ['PTS', 'MIN', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FG%', 'FG3%','FT%']
    sga_szn_dict = {}
    res_keywords = ['FG%', 'FG3%','FT%']
    for key, value in zip(keywords, column_list):
        if key in res_keywords:
            sga_szn_dict[key] = (value/len(sga_szn_stats))*100
        else:
            sga_szn_dict[key] = round((value)/len(sga_szn_stats),1)
    return sga_szn_dict

def sga_career_avg():
    sga_career_stats = playercareerstats.PlayerCareerStats(player_id='1628983').get_data_frames()[0]
    listwords = ['PTS', 'MIN', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FG_PCT', 'FG3_PCT','FT_PCT']
    column_list = [sga_career_stats[column].sum() for column in listwords]
    avg_gp = sga_career_stats['GP'].sum()/len(sga_career_stats)
    keywords = ['PTS', 'MIN', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FG%', 'FG3%','FT%']
    sga_career_dict = {}
    res_keywords = ['FG%', 'FG3%']
    for key, value in zip(keywords, column_list):
        if key in res_keywords:
            sga_career_dict[key] = (value/len(sga_career_stats))*100
        else:
            sga_career_dict[key] = round(((value/len(sga_career_stats))/avg_gp),1)
    return sga_career_dict

def sga_career_high():
    sga_career_log = playergamelog.PlayerGameLog(player_id='1628983',season='ALL').get_data_frames()[0]
    listwords = ['PTS', 'MIN', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FGM', 'FGA', 'FG_PCT', 'FG3A', 'FG3M', 'FG3_PCT', 'PLUS_MINUS']
    column_list = [max(sga_career_log[column].values) for column in listwords]
    keywords = ['PTS', 'MIN', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FGM', 'FGA', 'FG%', '3PTA', '3PTM', '3PT%', '+/-']
    res_keywords = ['FG%', '3PT%', 'WIN%']
    sga_career_dict ={}
    for key, value in zip(keywords, column_list):
        if key in res_keywords:
            sga_career_dict[key] = value*100
        else:
            sga_career_dict[key] = value
    return sga_career_dict





#sga_awards = playerawards.PlayerAwards(player_id='1628983').get_data_frames()[0]

#sga_career_stats = playercareerstats.PlayerCareerStats(player_id='1628983').get_data_frames()[0]
#sga_szn_log = playergamelog.PlayerGameLog(player_id='1628983',season='2023-24').get_data_frames()[0]

#sga_shotchart = shotchartdetail.ShotChartDetail(team_id='1610612760',player_id='1628983').get_data_frames()[0]




'''ppg_graph()
apg_graph()
rpg_graph()
spg_graph()
bpg_graph()
tpg_graph()
eff_graph()'''

'''print(sga_season_avg())'''

'''print(sga_career_avg())'''

'''print(sga_last5_opp_team_record())'''

'''print(sga_next_game())'''

'''print(sga_last5_performance())'''


'''mvp_list = sga_mvp_odds()

print(mvp_list['365'])
print(mvp_list['FD'])
print(mvp_list['MGM'])
print(mvp_list['CSR'])
print(mvp_list['PB'])
print(mvp_list['DK'])'''




'''i=""
while i != 'q':
    i = input("A for PPG ranking \n B for AST ranking \n C for REB ranking \n D for STL ranking \n E for BLK ranking \n" +
          "F for TOV ranking \n G for EFF ranking")
    if(i=="A"):
        print(sga_ppg_rank())
    elif(i=="B"):
        print(sga_apg_rank())
    elif(i=="C"):
        print(sga_rpg_rank())
    elif(i=="D"):
        print(sga_spg_rank())
    elif(i=="E"):
        print(sga_bpg_rank())
    elif(i=="F"):
        print(sga_tpg_rank())
    elif(i=="G"):
        print(sga_eff_rank())'''
