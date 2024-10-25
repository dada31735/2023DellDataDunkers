# -*- coding: utf-8 -*-
"""Another copy of pascal-siakam-stats-challenge.ipynb

# Pascal Siakam Statistics

Submitted by: Dumitru Gliga and Noah Walsh

## Introduction

Pascal Siakam took an unconventional road to stardom. He didn't grow up playing basketball, but instead began only when he was in high school.

In this notebook we will use statistics from [Basektball Reference](https://www.basketball-reference.com).

## Challenges

1. Plot some of Pascal Siakam's statistics over time, such as points per game or rebounds per game. Are there any patterns?
1. Pascal has taken on more of a leadership role with the Toronto Raptors since they won a championship in 2019, meaning that he has more responsibility, plays more minutes, and takes more shots. Plot a graph that contains some or all of the previous stats, but also contains his Minutes Per Game. What does this tell us about how Pascal is playing now that he is the "star" of the team?
1. We can also take a look at how "efficient" he is as he evolves by looking at his shooting percentages for different types of shots (we’ll start with 2-pointers and 3-pointers). Plot his shooting percentage by year for his career. What trends do you notice?
1. How does Pascal Siakam's efficiency change as he becomes a superstar? Plot a graph containing his Minutes Per Game, 2 Pt % and 3 Pt % over time. What do you notice? Does a higher usage lead to a greater or lesser efficiency?
1. If you were the General Manager and looking at these trends, what would you prioritize to maximize the talents of Pascal Siakam?
1. Using the 2016 Draft Class, plot a graph of the Total Career Points of the first round draft picks. Is Plascal Siakam near the top?
1. Find the top 5 total point scorers of that draft class. For each, find their player page and then plot their Points Per Game for their careers thus far.
"""

import pandas as pd
import plotly.express as px
per_game = pd.read_html('https://www.basketball-reference.com/players/s/siakapa01.html')[2]
draft_class = pd.read_html('https://www.basketball-reference.com/draft/NBA_2016.html')[0]
per_gameHB = pd.read_html ('https://www.basketball-reference.com/players/h/hieldbu01.html')[2]
per_gameJB = pd.read_html ('https://www.basketball-reference.com/players/b/brownja02.html')[2]
per_gameBI = pd.read_html ('https://www.basketball-reference.com/players/i/ingrabr01.html#per_game')[1]
per_gameDS = pd.read_html ('https://www.basketball-reference.com/players/s/sabondo01.html')[2]
draft_class = draft_class.fillna(0)
draft_class = draft_class.drop([30, 31]).reset_index(drop=True)
draft_class.columns = draft_class.columns.droplevel()
draft_class.columns = ['Rk','Pk','Tm','Player','College','Yrs','G','MP','PTS','TRB','AST','FG%','3P%','FT%','MPPG','PTSPG','TRBPG','ASTPG','WS','WS/48','BPM','VORP']
for column in draft_class.columns:
    draft_class[column] = pd.to_numeric(draft_class[column], errors='ignore')
print('Libraries and data imported')
print(per_game.head())

per_gameHB.drop_duplicates("Season", keep="first").reset_index(drop=True)

"""### Pascal Siakam Per Game Columns

|Column|Meaning|
|-|-|
|Season|If listed as single number, the year the season ended|
|Age|Player's age on February 1 of the season|
|Tm|Team|
|Lg|League|
|Pos|Position|
|G|Games|
|GS|Games Started|
|MP|Minutes Played Per Game|
|FG|Field Goals Per Game|
|FGA|Field Goal Attempts Per Game|
|FG%|Field Goal Percentage|
|3P|3-Point Field Goals Per Game|
|3PA|3-Point Field Goal Attempts Per Game|
|3P%|3-Point Field Goal Percentage|
|2P|2-Point Field Goals Per Game|
|2PA|2-Point Field Goal Attempts Per Game|
|2P%|2-Point Field Goal Percentage|
|eFG%|Effective Field Goal Percentage (since a 3-point field goal is worth more)|
|FT|Free Throws Per Game|
|FTA|Free Throw Attempts Per Game|
|FT%|Free Throw Percentage|
|ORB|Offensive Rebounds Per Game|
|DRB|Defensive Rebounds Per Game|
|TRB|Total Rebounds Per Game|
|AST|Assists Per Game|
|STL|Steals Per Game|
|BLK|Blocks Per Game|
|TOV|Turnovers Per Game|
|PF|Personal Fouls Per Game|
|PTS|Points Per Game|

### NBA 2016 Draft Class Columns

|Column|Meaning|
|-|-|
|Rk|Rank|
|Pk|Overall Pick|
|Tm|Team|
|Yrs|Seasons that player has appeared in the NBA|
|G|Games|
|MP|Minutes Played|
|PTS|Points|
|TRB|Total Rebounds|
|AST|Assists|
|FG%|Field Goal Percentage|
|3P%|3-Point Field Goal Percentage|
|FT%|Free Throw Percentage|
|MPPG|Minutes Played Per Game|
|PTSPG|Points Per Game|
|TRBPG|Total Rebounds Per Game|
|ASTPG|Assists Per Game|
|WS|Win Shares, an estimate of the number of wins contributed by a player|
|WS/48|Win Shares Per 48 Minutes (league average is about .100)|
|BPM|Box Plus/Minus, estimate of points per 100 possessions a player contributed above a league-average player, translated to an average team|
|VORP|Value over Replacement Player, estimate of points per 100 TEAM possessions a player contributed above a replacement-level (-2.0) player, translated to an average team and prorated to an 82-game season|

## Analysis
"""

px.bar(per_game, x='Age', y=['MP', 'FGA', 'FG', 'PTS'], barmode='group', title='Pascal Siakam Confidence').update_layout(yaxis_title='Percentage')

"""Here we can see that as he got older, more confident and just ,in general, became the star of the team (specifically in 2019 when he took more of a leadership role) he got more confident. When he got more confident, he went for more attempts which lead him to get better and thus have more field goals which directly lead to more points per game."""

px.scatter(per_game, x='MP', y=['2P%', '3P%'], title="Pascal Siakam's 2 point % and 3 point % relating to minutes played", color='Age')

"""Here we can see that as Pascal got older and became the star of the team(thus having to be a leader and play more) his 3 point % improved significantly while his 2 point % remained fairly stable. This can be attributed to multiple factors such as 3 points being more and more essential in the game of basketball (this also explains the drop in 2 point %) ,the fact that as he got to play more he got more consistent with his 3 point % and that as he played more he developped other skills which all helped him developpe his game IQ meaning that he took smarter shots.

If I were the manager I would prioritize putting Pascal in offensive positions where he constantly gets to go for more shots because as we saw Pascal is the type of Player who ,as he plays more, he evolves into a better player and adapts to the changes of the game of basketball as a whole.

****
"""

px.scatter(draft_class, x='Pk', y='PTS', hover_name='Player', title='Picks relating to total points scored', trendline='ols')

"""Here we would expect a fairly good correlation between overall pick and points as one would think that the top prospects would performe the best and yet, we see that this is rarely the case there are alot of outliers, such as Pascal, who is the player with the 3rd most overall points despite being the 27th pick during the 2016 draft. We also see that very little players actually reach the trend line and that instead we have alot of outliers who do much better than expected.

"""

px.line(per_gameHB, x='Age', y='PTS', title='Buddy Hill Points per Game')

px.line(per_gameJB, x='Age', y='PTS', title='Jaylen Brown Points per Game')

px.line(per_gameBI, x='Age', y='PTS', title='Brandon Ingram Points per Game')

px.line(per_gameDS, x='Age', y='PTS', title='Domantas Sabonis Points per Game')
"""
