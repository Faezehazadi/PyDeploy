from fastapi import FastAPI, HTTPException
from data import chess_pieces

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Welcome to the Chess Pieces API! This API provides information about six chess pieces: pawn, bishop, knight, rook, queen, and king."
    }

@app.get("/pieces")
def get_pieces():
    return list(chess_pieces.keys())

@app.get("/pieces/{piece_name}")
def get_piece_info(piece_name: str):
    piece_name = piece_name.lower()
    if piece_name not in chess_pieces:
        raise HTTPException(status_code=404, detail="Chess piece not found")
    return chess_pieces[piece_name]
