# bidding game
from click import clear
from Auction_bid import logo

print(logo)

bids = {}

bidding_finished = False


def find_height_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The Winner is {winner} with a bid of {highest_bid}')


while not bidding_finished:
    name = input("What is your name: ")
    price = int(input("What is your price: "))
    bids[name] = price
    continue1 = input(
        "Are there any other bidders? Type 'Yes' or 'No'.").lower()
    if continue1 == "no":
        bidding_finished = True
        find_height_bidder(bidding_record=bids)
    elif continue1 == "yes":
        clear()
