board = ['' for _ in range(9)]
print (board)

def print_board():
    print("_________")
    for i in range (0,9,3):
        print('|',board[i],'|',board[i+1],'|',board[i+2],'|')
        print('_________')

print_board()
