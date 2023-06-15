numbers = [1,3,5]
doubled = [num * 2 for num in numbers]

print(doubled)

friends = ["Ralph", "San", "Samanta", "Sebastian", "Jen"]
friends_start_s = [ x for x in friends if x.startswith("S")]

print(friends_start_s)

print("friends id :",id(friends)," friends_start_s if:",id(friends_start_s))
friends_start_s = friends
print("friends id :",id(friends)," friends_start_s if:",id(friends_start_s))
friends_start_s.append("Lukas") # to jest to samo co friends
print("friends:", friends)
# friends_start_s = []
# for friend in friends:
#     if friend.startswith("S"):
#         friends_start_s.append(friend)
#
#
# print(friends_start_s) ,