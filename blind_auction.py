#blind auction
from project3.blind_auction_art import logo
print("\nBLIND AUCTION HOUSE")
print(logo)
condition = True
bid_dictionary={}

while(condition):
    name=input("\nEnter your name -->")
    bid=float(input("Enter your bid amount -->$"))
    bid_dictionary[name]=bid 
    
    condition1=(input("\nIs there any other bidder who wants to bid (yes/no) -->")).lower()
    if(condition1=="yes"):
        condition=True
    else:
        condition=False

maximum=0
max_bidder=""
for i in bid_dictionary:
    maximum1=bid_dictionary[i]
    # for j in bid_dictionary:
    #     if(bid_dictionary[j]>maximum):
    #         maximum=bid_dictionary[j]
    #         max_bidder=j
    # alternative with complexity of o(n)
    if (maximum1>maximum):
        maximum=maximum1
        max_bidder=i

print(f"\nThe winner is {max_bidder} with a bid of ${maximum}")

