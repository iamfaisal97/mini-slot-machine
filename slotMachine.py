import random

# 1. get input from the user

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Specify the number of rows and columns

ROWS = 3
COLS = 3 

# Symbols

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = [] # tells the winning lines

    for line in range(lines): #we have every line in the line , we are looping through every row
        symbol = columns[0][line] # the symbol we wanna check is whatever symbol is in the first column of the current row
        for column in columns: #we now know the symbol we gonna check, now loop through every single column and check every symbol
            symbol_to_check = column[line] #now we loop through every single column and check for that symbol
            if symbol != symbol_to_check: # if symbol not the same, break out
                break
        else:
            winnings+= values[symbol] * bet
            winning_lines.append(line + 1) 
    return winnings, winning_lines #we return total amount they won and what lines they won on

# Outcome

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):  # _ anonymous variable
            all_symbols.append(symbol)


    columns = []    # Columns     #1. Define the column list
    for _ in range(cols): # for col in range(cols)  2. Generate a column for every single column we have, for example if we have 3 column we have to do everything inside the code 3 times 
        column = []
        current_symbols = all_symbols[:]                     #
        for _ in range(rows): # for row in range(rows)       #
            value = random.choice(current_symbols)          # This code block is picking random values for each row
            current_symbols.remove(value)                  #
            column.append(value)                           #

        columns.append(column)

    return columns



#transposing  
# [A, B C,] =  [A , A , A]   make row to vertical
# [A, A, A]    [B , A  , B]
# [A, B, A]   [ C , A , A ]

def print_slot_machine(columns): 
    for row in range(len(columns[0])): # loop through every single row we have,for every single row we loop through every column ,
        for i, column in enumerate(columns):  # for every column we only print the current row we are on
            if i != len(columns) - 1:
             print(column[row], end=" | ")
            else :
                print(column[row], end="")
        
        print()

    

def deposit():
    while True:
        amount = input("What would you like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else :
                print('Amount must be greater than 0')
        else:
            print("Please enter a number")
    return amount

    
    # User input on getting the number of lines    

def get_number_of_lines():
    while True:
        lines = input("Enter the number of line to bet on (1-" + str(MAX_LINES) + ") ? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines.')
        else:
            print("Please enter a number.")
    return lines
 
 # User input on getting the bet amount   
 
def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else :
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")
    return amount 


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is $:{balance}")
        else :
            break

    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to :${total_bet}')


     
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit() 
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
          break
        balance += spin(balance)

    print(f"You left with ${balance}")
    
main()
     