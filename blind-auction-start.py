print('''
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
''')

from replit import clear
#HINT: You can call clear() to clear the output in the console.
bidder_list = {}
other_bidders = str("yes")
while other_bidders == "yes":
  bidder_name = input("What's your name?:")
  bidder_bid = input("What's your bid?:")
  bidder_list[bidder_name] = bidder_bid
  other_bidders = input("Are there any other bidders ? Type 'yes' or 'no'.")
  if other_bidders == "yes" :
    clear()
  else:
    max_value = max(bidder_list.values())
    max_value_key = max(bidder_list.keys())
    print(f"The winner is {max_value_key}  with a bid of ${max_value}")

  
  
