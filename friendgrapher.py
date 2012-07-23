import tweepy
import simplejson as json

#param id can be string or int
def getFriends(id):
	q=tweepy.api.friends(user_id=id,cursor=-1)
	list_users=q[0]
	while len(q[0])>0:
		q=tweepy.api.friends(user_id=id,cursor=q[1][1])
		list_users=list_users+q[0]
	list_dict_users=[]
	#add input id to the user list in index 0
	this_user=tweepy.api.get_user(id)
	list_dict_users.append({"id": this_user.id,
								"screen_name": this_user.screen_name,
								"name": this_user.name,
								"followers_count": this_user.followers_count,
								"friends_count": this_user.friends_count,
								"statuses_count": this_user.statuses_count})
	for i in list_users:
		list_dict_users.append({"id": i.id,
								"screen_name": i.screen_name,
								"name": i.name,
								"followers_count": i.followers_count,
								"friends_count": i.friends_count,
								"statuses_count": i.statuses_count})
	return list_dict_users

def create_dataset(list_users,output_form=0):
	if output_form==0:
		json_dict  = { "nodes" : list_users}
	elif output_form==1:
		list_links=[]
		for l in range(1,len(list_users)):
			list_links.append({"source":l,"target":0,"value":1})
		json_dict  = { "nodes" : list_users, "links" : list_links}
	
	return json.dumps(json_dict)
