import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 599))

# Title and icon
pygame.display.set_caption("Chess @Pratik")
icon = pygame.image.load("icons/thumbnail.png")
pygame.display.set_icon(icon)

# chess board image
chess_board_img = pygame.image.load("icons/chess_board.png")
chess_board_x = 0
chess_board_y = 0

def chess_board():
    screen.blit(chess_board_img, (chess_board_x, chess_board_y))

# pawn image load and display
# white pieces
pawn_w_img = pygame.image.load("icons/pawn_w.png")
king_w_img = pygame.image.load("icons/king_w.png")
queen_w_img = pygame.image.load("icons/queen_w.png")
bishop_w_img = pygame.image.load("icons/bishop_w.png")
knight_w_img = pygame.image.load("icons/knight_w.png")
rook_w_img = pygame.image.load("icons/rook_w.png")

# black pieces
pawn_b_img = pygame.image.load("icons/pawn_b.png")
king_b_img = pygame.image.load("icons/king_b.png")
queen_b_img = pygame.image.load("icons/queen_b.png")
bishop_b_img = pygame.image.load("icons/bishop_b.png")
knight_b_img = pygame.image.load("icons/knight_b.png")
rook_b_img = pygame.image.load("icons/rook_b.png")

# mapping locations and user inputs
map_to_index = {
   "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7
}

def pieces(piece, x, y):
    screen.blit(piece, (x, y))

# Making textbox to input user text
font = pygame.font.Font(None, 32)
user_input = ''

text_box = pygame.Rect(640, 100, 140, 32)
color = pygame.Color('black')

def player_white():
    text_render = font.render(user_input, True, (101, 67, 33))
    screen.blit(text_render, (text_box.x + 5, text_box.y + 5))
    text_box.w = max(text_render.get_width() + 10, 100)

# 64 locations of all the cells in the board
# for assigning locations to user inputs
mapping_location = {
    (0, 7) : (66, 66), (1, 7) : (132, 66), (2, 7) : (198, 66), (3, 7) : (264, 66), (4, 7) : (330, 66), (5, 7) : (396, 66), (6, 7) : (462, 66), (7, 7) : (528, 66),
    (0, 6) : (66, 132), (1, 6) : (132, 132), (2, 6) : (198, 132), (3, 6) : (264, 132), (4, 6) : (330, 132), (5, 6) : (396, 132), (6, 6) : (462, 132), (7, 6) : (528, 132), 
    (0, 5) : (66, 198), (1, 5) : (132, 198), (2, 5) : (198, 198), (3, 5) : (264, 198), (4, 5) : (330, 198), (5, 5) : (396, 198), (6, 5) : (462, 198), (7, 5) : (528, 198), 
    (0, 4) : (66, 264), (1, 4) : (132, 264), (2, 4) : (198, 264), (3, 4) : (264, 264), (4, 4) : (330, 264), (5, 4) : (396, 264), (6, 4) : (462, 264), (7, 4) : (528, 264), 
    (0, 3) : (66, 330), (1, 3) : (132, 330), (2, 3) : (198, 330), (3, 3) : (264, 330), (4, 3) : (330, 330), (5, 3) : (396, 330), (6, 3) : (462, 330), (7, 3) : (528, 330), 
    (0, 2) : (66, 396), (1, 2) : (132, 396), (2, 2) : (198, 396), (3, 2) : (264, 396), (4, 2) : (330, 396), (5, 2) : (396, 396), (6, 2) : (462, 396), (7, 2) : (528, 396), 
    (0, 1) : (66, 462), (1, 1) : (132, 462), (2, 1) : (198, 462), (3, 1) : (264, 462), (4, 1) : (330, 462), (5, 1) : (396, 462), (6, 1) : (462, 462), (7, 1) : (528, 462), 
    (0, 0) : (66, 528), (1, 0) : (132, 528), (2, 0) : (198, 528), (3, 0) : (264, 528), (4, 0) : (330, 528), (5, 0) : (396, 528), (6, 0) : (462, 528), (7, 0) : (528, 528)
}

# key press events
# getting previous and next location for selected cell
def key_press_occurs():
    if key_press == True and len(user_input) == 4:
        col1, row1, col2, row2 = list(user_input.strip().lower())
        row1 = int(row1) - 1
        row2 = int(row2) - 1
        col1 = map_to_index[col1]
        col2 = map_to_index[col2]
        (column_in, row_in) = mapping_location[(col1, row1)]
        (column_out, row_out) = mapping_location[(col2, row2)]
        print((column_in, row_in), (column_out, row_out))


# Game loop
running = True
while running:
    key_press = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                key_press = True
                user_input += event.unicode
                print("need_value")

            if event.key == pygame.K_SPACE:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                user_input = user_input[:-5]
    key_press_occurs()

    # Giving color to background
    screen.fill((230, 230, 230))

    # display chess board
    chess_board()

    # Displaying items
    # white pieces
    pieces(rook_w_img, 66, 66)
    pieces(knight_w_img, 132, 66)
    pieces(bishop_w_img, 198, 66)
    pieces(queen_w_img, 264, 66)
    pieces(king_w_img, 330, 66)
    pieces(bishop_w_img, 396, 66)
    pieces(knight_w_img, 462, 66)
    pieces(rook_w_img, 528, 66)
    pieces(pawn_w_img, 66, 132)
    pieces(pawn_w_img, 132, 132)
    pieces(pawn_w_img, 198, 132)
    pieces(pawn_w_img, 264, 132)
    pieces(pawn_w_img, 330, 132)
    pieces(pawn_w_img, 396, 132)
    pieces(pawn_w_img, 462, 132)
    pieces(pawn_w_img, 528, 132)

    # black pieces
    pieces(pawn_b_img, 66, 462)
    pieces(pawn_b_img, 132, 462)
    pieces(pawn_b_img, 198, 462)
    pieces(pawn_b_img, 264, 462)
    pieces(pawn_b_img, 330, 462)
    pieces(pawn_b_img, 396, 462)
    pieces(pawn_b_img, 462, 462)
    pieces(pawn_b_img, 528, 462)
    pieces(rook_b_img, 66, 528)
    pieces(knight_b_img, 132, 528)
    pieces(bishop_b_img, 198, 528)
    pieces(queen_b_img, 264, 528)
    pieces(king_b_img, 330, 528)
    pieces(bishop_b_img, 396, 528)
    pieces(knight_b_img, 462, 528)
    pieces(rook_b_img, 528, 528)

    # border for text_box
    pygame.draw.rect(screen, color, text_box, 2)

    # show_score(textx, texty)
    player_white()

    # Updating the window
    pygame.display.update()