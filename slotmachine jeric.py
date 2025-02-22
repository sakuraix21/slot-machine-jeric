import random

symbols = ['Grand', 'Major', 'Mini']

def spin():
    return [random.choice(symbols) for _ in range(3)]

def play():
    balance = 1000
    while balance > 0:
        bet = int(input(f"Your balance: {balance}. Enter bet: "))
        if bet < 1 or bet > balance:
            print("Invalid bet!")
            continue
        result = spin()
        print(f"Spin: {result}")
        if len(set(result)) == 1:
            print(f"You win! Payout: {bet * 10}")
            balance += bet * 10 - bet
        else:
            print("You lose.")
            balance -= bet
        if balance == 0:
            print("Out of money. Game over!")
            break
        if input("Do You Want to Play again? (yes/no): ").lower() != 'yes':
            break

play()
