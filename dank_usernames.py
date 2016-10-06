

def search_username(name):
   global wordlist
   potential_usernames = []
   chance = []
   name = list(name.lower())
   for item in wordlist:
      verify = 0
      chance = []
      check = list(item.strip())
      for item2 in check:
         if item2 in name:
            chance.append(name.index(item2))
      if len(chance) != len(check):
         continue
      for item3 in chance:
         if item3 < verify:
            chance = []
            break
         verify = item3
      if chance and verify == chance[-1]:
         potential_usernames.append("".join(check))
         continue
   ret_list = sorted(potential_usernames,key=len)
   return ret_list[-1]


wordlist = open('wordlist','r').readlines() 

print(len(wordlist))
name = input("Enter name: ")

result = search_username(name)

print(result)
