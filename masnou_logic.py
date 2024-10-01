import datetime
import random
from more_itertools import grouper
from rich.table import Table
from rich.console import Console


class Masnou:
    def __init__(self) -> None:
        self.side = "white"
        self.time = datetime.datetime.now()

    def create_tournament(self, players: list[dict], options: dict):
        self.players = players
        self.table = [
            {"id": player["ID_no"], "name": player["Name"], "matches": [], "score": 0}
            for player in players
        ]
        self.rounds_history = []
        self.ids = [player["id"] for player in self.table]
        self.cola = []
        self.groups = {}
        # get the number of players thayt will start playing to determine how many will be on the queue
        # self.assign(options["num_players_board"])
        self.create_pairings(options["num_players_board"])

    def add_player(self, data: dict, score: int | float = 0):
        if data["ID_no"] in self.ids:
            return None
        if data.get("ID_no") is None or data.get("Name") is None:
            return None
        self.table.append(
            {"id": data["ID_no"], "name": data["Name"], "matches": [], "score": score}
        )

        self.players.append(data)
        self.ids.append(data["ID_no"])
        self.cola.append(data["ID_no"])

        return True

    def delete_player(self, id):
        self.table = [player for player in self.table if player["id"] != id]
        self.ids = [player["id"] for player in self.table]
        if id in self.cola:
            self.cola.remove(id)
            return
        for key, spot in self.groups.items():
            for index, player in enumerate(spot):
                if player == id:
                    if len(self.cola) > 0:
                        self.groups[key][index] = self.cola[0]
                        self.cola.pop(0)
                        return
                    else:
                        other_player = 1 if index == 0 else 0
                        self.cola.insert(0, spot[other_player])
                        self.groups.pop(key)
                        return

    def assign(self, num_players):
        first = self.ids[:num_players]
        if len(self.players) == num_players:
            self.cola = []
        else:
            self.cola = self.ids[num_players:]
        self.groupers = grouper(first, 2)
        self.groups: dict = dict(enumerate([list(x) for x in self.groupers]))

    def run_test(self):
        for _ in range(40):
            s = random.randint(0, 4)
            w = random.randint(0, 2)
            self.update(s, w)

    def temp_table(self):
        return sorted(
            [[d["id"], d["name"], d["score"]] for d in self.table],
            key=lambda x: x[2],
            reverse=True,
        )

    def find_player(self, id) -> int:
        for index, player in enumerate(self.table):
            if player["id"] == id:
                return index
        return 0

    def change_side(self):
        self.side = "black" if self.side == "white" else "black"

    def show_table(self):
        table = Table(title="results")
        table.add_column("Id")
        table.add_column("Name")
        table.add_column("W")
        # table.add_column("L")
        # table.add_column("T")
        table.add_column("Score")
        for x in self.table:
            table.add_row(
                str(x["id"]),
                x["name"],
                str(self.count_result("w", x["matches"])),
                str(x["score"]),
            )
        console = Console()
        console.print(table)

    def return_table(self):
        table = []
        for row in self.table:
            table.append([row["id"], row["name"], row["score"]])
        table = sorted(table, key=lambda x: x[2], reverse=True)
        return table

    def get_name_from_id(self, id):
        for player in self.table:
            if player["id"] == id:
                return player["name"]
        return None

    def groups_to_table(self):
        print(self.table)
        table = []
        for row in self.groups:
            table.append(
                [
                    row,
                    self.groups[row][0],
                    self.get_name_from_id(self.groups[row][0]),
                    self.groups[row][1],
                    self.get_name_from_id(self.groups[row][1]),
                ]
            )
        return table

    def sort_cola_randomly(self):
        random.shuffle(self.cola)

    def get_cola_names(self):
        cola = []
        for player in self.cola:
            cola.append(self.get_name_from_id(player))
        return cola

    def count_result(self, result: str, matches: list[dict]):
        temp_results = []
        for match in matches:
            temp_results.append(match["result"])
        number = temp_results.count(result)
        return number

    def handle_tight(self, spot: int):
        leaver = self.groups[spot][0]
        stayer = self.groups[spot][1]
        outcome = self.get_outcome(3)
        self.cola.append(leaver)
        self.groups[spot][0] = self.cola[0]
        self.cola.pop(0)
        for p in [leaver, stayer]:
            self.table[self.find_player(p)]["score"] += 0.5
            self.table[self.find_player(p)]["matches"].append(
                {"w": leaver, "b": stayer, "result": "t", "time": 2, "outcome": outcome}
            )

    def update(self, spot: int, winner: int):
        print("Updating", spot, winner)
        if winner == 2:
            self.handle_tight(spot)
            return
        loser = 0 if winner == 1 else 1
        loser_id = self.groups[spot][loser]
        winner_id = self.groups[spot][winner]
        white = self.groups[spot][0]
        black = self.groups[spot][1]
        outcome = self.get_outcome(winner)
        self.cola.append(loser_id)
        # in case sides are swaped to white the winner will take white
        if self.side == "white":
            self.groups[spot][0] = winner_id
            self.groups[spot][1] = self.cola[0]
        else:
            self.groups[spot][0] = self.cola[0]
            self.groups[spot][1] = winner_id
        self.cola.pop(0)
        self.table[self.find_player(winner_id)]["score"] += 1
        self.table[self.find_player(winner_id)]["matches"].append(
            {"w": white, "b": black, "result": "w", "time": 2, "outcome": outcome}
        )
        self.table[self.find_player(loser_id)]["matches"].append(
            {"w": white, "b": black, "result": "l", "time": 2, "outcome": outcome}
        )
        self.rounds_history.append(
            [
                spot,
                white,
                self.get_name_from_id(white),
                1 if winner_id == white else 0,
                1 if winner_id == black else 0,
                black,
                self.get_name_from_id(black),
            ]
        )

    def get_outcome(self, winner: int):
        outcome = ""
        if winner == 0:
            outcome = "1-0"
        elif winner == 1:
            outcome = "0-1"
        else:
            outcome = "1-1"
        return outcome

    def delete_tournament(self):
        self.table = []
        self.groups = {}
        self.cola = []

    def create_pairings(self, number_pairings):
        groups = []
        pairings = {}
        # stores players. in case the number of players in the category is odd it will remove a player from the category
        temporary_leftover = []
        for player in self.players[0:number_pairings]:
            if player["Category"] not in pairings:
                pairings[player["Category"]] = []
                pairings[player["Category"]].append(player["ID_no"])
            else:
                pairings[player["Category"]].append(player["ID_no"])
        for category, players in pairings.items():
            if len(players) % 2 != 0:
                temporary_leftover.append(players.pop(0))
            if len(players) > 0:
                category_groups = grouper(players, 2)
                for group in category_groups:
                    groups.append(list(group))
        # take the temporary leftover if any and
        if len(temporary_leftover) == 1:
            self.cola.append(temporary_leftover.pop(0))
        if len(temporary_leftover) > 1 and len(temporary_leftover) % 2 != 0:
            self.cola.append(temporary_leftover.pop(0))
            leftover_groups = grouper(temporary_leftover, 2)
            for group in leftover_groups:
                groups.append(list(group))
            temporary_leftover = []
        if len(temporary_leftover) > 0 and len(temporary_leftover) % 2 == 0:
            leftover_groups = grouper(temporary_leftover, 2)
            for group in leftover_groups:
                groups.append(list(group))
        self.groups = dict(enumerate(groups))
        self.cola = self.cola + [
            player["ID_no"] for player in self.players[number_pairings:]
        ]
        print(self.cola)
