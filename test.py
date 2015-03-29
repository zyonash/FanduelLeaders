# DFS Up to Date Scoring (Famduel only at the moment)
# Author: Zachary Yonash

import urllib2
import re
import operator
from bs4 import BeautifulSoup
from player import Player

response = urllib2.urlopen("http://espn.go.com/nba/boxscore?gameId=400579369")
html = response.read()
soup = BeautifulSoup(html)


# ESPN Box Score table rows are broken down into "even" IDs and "odd" IDs
list_of_even_players = []
list_of_odd_players = []

# Needed for sifting out the few entries that aren't players
_digits = re.compile('\d')

def set_even_players():
    all_even_tags = soup.find_all("tr", class_="even")
    for even_tag in all_even_tags:
        if not bool(_digits.search(even_tag.contents[1].contents[0].get_text())) and "DNP" not in even_tag.contents[2].contents[0]:
            x = Player(even_tag.contents[1].contents[0].get_text())
            x.set_minutes(even_tag.contents[2].contents[0])
            x.set_rebounds(even_tag.contents[8].contents[0])
            x.set_assists(even_tag.contents[9].contents[0])
            x.set_steals(even_tag.contents[10].contents[0])
            x.set_blocks(even_tag.contents[11].contents[0])
            x.set_turnovers(even_tag.contents[12].contents[0])
            x.set_points(even_tag.contents[15].contents[0])
            list_of_even_players.append(x)

def set_odd_players():
    all_odd_tags = soup.find_all("tr", class_="odd")
    for odd_tag in all_odd_tags:
        if not bool(_digits.search(odd_tag.contents[1].contents[0].get_text())) and "DNP" not in odd_tag.contents[2].contents[0]:
            x = Player(odd_tag.contents[1].contents[0].get_text())
            x.set_minutes(odd_tag.contents[2].contents[0])
            x.set_rebounds(odd_tag.contents[8].contents[0])
            x.set_assists(odd_tag.contents[9].contents[0])
            x.set_steals(odd_tag.contents[10].contents[0])
            x.set_blocks(odd_tag.contents[11].contents[0])
            x.set_turnovers(odd_tag.contents[12].contents[0])
            x.set_points(odd_tag.contents[15].contents[0])
            list_of_odd_players.append(x)

set_even_players()
set_odd_players()

dict = {}

for play in list_of_even_players:
    dict[play.name] = (float(play.get_rebounds()) * 1.2 + float(play.get_assists()) * 1.5 + float(play.get_steals()) * 2 + float(play.get_blocks()) * 2 - float(play.get_turnovers()) + float(play.get_points()))

for play in list_of_odd_players:
    dict[play.name] = (float(play.get_rebounds()) * 1.2 + float(play.get_assists()) * 1.5 + float(play.get_steals()) * 2 + float(play.get_blocks()) * 2 - float(play.get_turnovers()) + float(play.get_points()))

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

for sorted in sorted_dict:
    print "Player: " + sorted[0]
    print "Fanduel Points: " + str(sorted[1])

''' DEBUG

for play in list_of_even_players:
    print play.name
    print play.get_minutes() + " Minutes"
    print play.get_rebounds() + " Rebounds"
    print play.get_assists() + " Assists"
    print play.get_steals() + " Steals"
    print play.get_blocks() + " Blocks"
    print play.get_turnovers() + " Turnovers"
    print play.get_points() + " Points"
    print "Fanduel Points: " + str((float(play.get_rebounds()) * 1.2 + float(play.get_assists()) * 1.5 + float(play.get_steals()) * 2 + float(play.get_blocks()) * 2 - float(play.get_turnovers()) + float(play.get_points())))
    print "\n"
'''


