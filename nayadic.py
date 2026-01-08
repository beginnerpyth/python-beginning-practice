#month = {
#    'mam':"kak",
 #   "sas" : "lal",
 #   "pap":"kak",
 #   "waw":"oo",
#}
#print(month["mam"])
#print(month.get("jaja","not a valid key"))
#i=1
mila = " "
guess = "kk"
out_of_guesses = False
guesses_count=0
guess_limit=3

while mila!= guess and not(out_of_guesses):
    if  guesses_count<guess_limit:
        mila = input("enter a name")
        guesses_count = +1
        
    else:
        out_of_guesses=True

if out_of_guesses:
    print("you lost")
else:
    print("you won")



