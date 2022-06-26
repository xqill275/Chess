import pygame as p
from Chess import ChessEngine


WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 12
IMAGES = {}

def LoadImages():
    pieces = ["wp","wR","wN","wB","wK","wQ","bp","bR","bN","bB","bK","bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE,SQ_SIZE))



def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    print(len(gs.board))
    LoadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row,col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    player_move = ChessEngine.Move(playerClicks[0],playerClicks[1],gs.board)

                    print(player_move.getChessNotation())
                    gs.makeMove(player_move)
                    sqSelected = ()
                    playerClicks = []


        DrawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()



def DrawGameState(screen,gs):
    DrawBoard(screen)
    DrawPieces(screen,gs.board)

def DrawBoard(screen):
    colours = [p.Color("white"),p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            colour = colours[((r+c) % 2)]
            p.draw.rect(screen,colour,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def DrawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


if __name__ == "__main__":
    main()