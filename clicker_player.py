from clicker_ui import *

from random import randint
import json


def handle_new_data(new_name, players, current_player):
    current_player.last_player = False
    really_new_player = True
    for pl in players:
        if new_name.lower() == pl.name.lower():
            current_player = pl
            really_new_player = False
    if really_new_player:
        current_player = Player(name=new_name)
        players.append(current_player)
    return players, current_player


def read_players_from_file(screen):
    players = []
    try:
        file = open('players.json', 'r')
        new_dict = json.load(file)
        file.close()
        for val in new_dict.values():
            val = json.loads(val)
            players.append(Player(name=val['name'],
                                  id_num=int(val['id_num']),
                                  hand_power=int(val['hand_power']),
                                  last_player=bool(val['last_player']),
                                  targets_killed=int(val['targets_killed']),
                                  afk_power=float(val['afk_power'])))
    except json.JSONDecodeError and FileNotFoundError:
        pass
    if not players:
        new_data, new_name = change_player(screen)
        if not new_data:
            players.append(Player(name='Sample Name',
                                  last_player=True))
        else:
            players.append(Player(name=new_name,
                                  last_player=True))
    return players


def define_current_player(players):
    for pl in players:
        if pl.last_player:
            return pl


def write_players_to_file(players):
    with open('players.json', 'w') as file:
        dic = {}
        for i, pl in enumerate(players):
            dic[i] = pl.to_json()
        json.dump(dic, file)


class Player:

    def __init__(self,
                 name='Sample Name',
                 id_num=randint(1, 1000),
                 hand_power=1,
                 last_player=False,
                 targets_killed=0,
                 afk_power=0.0):
        self.name = name
        self.id_num = id_num
        self.hand_power = hand_power
        self.afk_power = afk_power
        self.last_player = last_player
        self.targets_killed = targets_killed

    def to_json(self):
        return json.dumps(self.__dict__)


if __name__ == '__main__':
    print('This module is not for direct run!')
