
# List of friends of friends...
ff_list = {
    1 : [2, 4, 5],#[2,4,5,3]
    2 : [1, 4, 6],
    3 : [4, 5],#[4,5,1]
    4 : [1, 2, 3, 6],
    5 : [1, 3, 6],
    6 : [2, 4, 5]
}
# schoolfriend=1, neighbour =2, college mate=3, collegue =4, relative =5, teacher/ student=6, employee/employer=7
hr_list = {
    1 : [4,2,3],#[4,2,3,4]
    2 : [4,4,5],
    3 : [2,1],#[2,1,4]
    4 : [2,4,2,7],
    5 : [3,1,1],
    6 : [5,7,1]
}

 
def get_friend_suggestions(user_id):
	'''
	@param user_id - currently logged in user
	Find the list of suggested friends for a user along with
	the friends that are mutual to the suggested friend.
	'''
	suggested_friends = {}
	sugg_fcount ={}
	tempp=''
	for f in ff_list:
	    sugg_fcount[f] = 0;
	# Get the friends of the current user.
	friends = ff_list[user_id]
 
	for friend in friends:
		# Friends friends list.
	    ffriends = ff_list[friend]
	    for ff in ffriends:
	    	# If the friendsFriend(ff) is not us, and not our friend, he can be suggested
	        if ff != user_id and ff not in friends:
	        	# The key is the suggested friend
	            suggested_friends[ff] = {'mutual_friends' : []}
	            for f in ff_list[ff]:
	            	# If he is a friend of the current user, he is a mutual friend
	                if f in friends:
	                    suggested_friends[ff]['mutual_friends'].append(f)
	for ff in suggested_friends:
	    print ff,":",suggested_friends[ff]
	for ff in suggested_friends:
	    k=len(suggested_friends[ff]['mutual_friends'])
	    for l in range(0, k):
	        i=suggested_friends[ff]['mutual_friends'][l]
	        if hr_list[user_id][ff_list[user_id].index(i)] == hr_list[i][ff_list[i].index(ff)]:
	            print "NEW SUGGESTION",ff,": through",i
	            tempp = input("accept?\n")
	            if tempp == "y":
	                ff_list[user_id].append(ff)
	                ff_list[ff].append(user_id)
	                temppp = input("relation\n")
	                hr_list[user_id].append(temppp)
	                hr_list[ff].append(temppp)
	                
	                  
	
#change user_id_input in the below code to run this code for different accounts.... 
# a working example has been depected.... use as input the following 
# "y"\n 4\n "n"\n "n"\n "n"\n "n"\n
# to see all functionality of this code

user_id_input = 3
print "Suggested Friends and Mutual Friends for user {}".format(user_id_input)
#print
get_friend_suggestions(user_id_input)
print "\nSuggested Friends and Mutual Friends for user {}".format(user_id_input)
get_friend_suggestions(user_id_input)
user_id_input = 2
print "\nSuggested Friends and Mutual Friends for user {}".format(user_id_input)
get_friend_suggestions(user_id_input)

print "DONE"
