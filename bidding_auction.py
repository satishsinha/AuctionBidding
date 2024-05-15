from replit import clear #HINT: You can call clear() to clear the output in the console.


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
auction_dict = {}
def auction_data(name, price):
    new_data = {}
    new_data["Name"] = name 
    new_data["Price"] = price 
    auction_dict[name] = price
    
def find_winner(winner):
    lowest_bid = float('inf')
    win = ""  # Initialize win with an empty string
    for bidder in winner:
        amount = winner[bidder] 
        if amount < lowest_bid:
            lowest_bid = amount
            win = bidder      
    if win:  # Check if win has a value
        print(f"Winner is {win} with bid amount of ${lowest_bid}")
    else:
        print("No bids were made.")       
       
any_other_bidder = True
while any_other_bidder:
    auction_name = input("Enter your name: ")
    auction_price = int(input("Enter bidding Price(in $): "))

    auction_data(name=auction_name, price=auction_price) 
    any_other = input("Type 'yes' if any other bidder is available. Otherwise type 'no'.\n")
    if any_other == "no":
        any_other_bidder = False
        find_winner(winner=auction_dict)
    elif any_other == "yes":
        clear() #only clear the terminal
         
     