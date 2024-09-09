import chess
import chess.svg
import chess.pgn
import json
from io import StringIO
import random

with open("all.json", "r", encoding="utf-8", errors="ignore") as f:
    data = json.load(f)
    index = random.randint(0, len(data) - 1)
    data = data[index]

def to_svg():
    game_data = get_board(data)
    if game_data is None:
        board = chess.Board()
        return {"svg": chess.svg.board(board, size=670).encode("utf-8")}
    board = game_data["board"]
    game_data["svg"] = chess.svg.board(board, size=670).encode("utf-8")
    return game_data


def get_board(data):
    pgn = StringIO(data["pgn"])
    title = data["title"]
    moves = []
    game = chess.pgn.read_game(pgn)
    if game is None:
        return None
    for move in game.mainline_moves():
        moves.append(move.uci())
    board = game.board()
    return {
        "fen": board.fen(), 
        "moves": moves, "board": board, "title": title, "turn": "Blancas" if board.turn else "Negras"}

