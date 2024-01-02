
print("Welcome to the secret auction program.")

# Create an empty dictionary to store bidder information
bidders = {}
maximum_amount = 0

while True:
    #clear()      (remove the # to pass Angela's test)
    player_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid for this item?: $"))
    any_more_bidders = input("Are there any other bidders? (Type Y or N): ").upper()

    # Add bidder's information to the dictionary
    bidders[player_name] = bid_amount #add info to the dictionary
				# the key of bidders Dictionary[player_name] returns the bid_amount

    if any_more_bidders != "Y":
        break
		#else:        #else: False is implied. Doesn't need to be typed.
				#True

# Print the bidders and their bids
for player, amount in bidders.items():
    # print(f"Player: {player} bid an amount of: {amount}")
    if amount >= maximum_amount:
        maximum_amount = amount
        highest_bidder = player
        # print(f"Maximum bid so far is: {maximum_amount}")

print(f"The winner is {highest_bidder} with a bid of ${maximum_amount}.")