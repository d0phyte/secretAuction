#windows cmd admin mode -> py -m pip install replit
from replit import clear

bidders = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? ")
    bid = float(input("What is your bid? £"))
    bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if other_bidders.lower() == "no" or other_bidders.lower() == "n":
        bidding_finished = True
    else:
        clear()

highest_bid = 0
winner = ""

for bidder, bid in bidders.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = bidder

print(f"The winner is {winner} with a bid of £{highest_bid}")
