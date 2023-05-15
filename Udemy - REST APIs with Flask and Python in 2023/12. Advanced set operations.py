friends = {"Bob", "Ralph", "Anna",}
abroad = {"Bob","Jacob"}

local_friends = friends.difference(abroad)
all_fiends = friends.union(abroad)
both_friends = friends.intersection(abroad)
print(local_friends)    #{'Ralph', 'Anna'}
print(all_fiends)       #{'Jacob', 'Ralph', 'Anna', 'Bob'}
print(both_friends)     #{'Bob'}