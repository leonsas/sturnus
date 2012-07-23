import urllib
import simplejson as json


def getFollowers(tweets):
	for l in range(0,13):
		base_search_url="https://api.twitter.com/1/users/lookup.json?user_id="
		i=l*100
		for i in range(i,i+100):
			base_search_url=base_search_url+str(tweets[i]["user_id"])+","
			
		search = urllib.urlopen(base_search_url)
		print search.info()
		list_results = json.loads(search.read())
		for r in list_results:
				node= [result for result in tweets if result["user_id"] == r["id"]]
				node[0]["followers"]=r["followers_count"]
				
		print "Next loop L"
	fo=open("samplewithfollowers","w")
	fo.write(json.dumps(tweets))
	fo.close()
	raise Exception
	return dict[0]["followers_count"]
	
	
def buildNodes():
		nodes =[]
		f=open("samplejson.txt","r")
		a=f.readline()
		tweetlist=json.loads(a)
		
		#tweet by tweet and append some info to node
		for o in tweetlist:
			nodes.append({"username":o["from_user_name"],
						  "user_id":o["from_user_id"],
						  "to_user_id":o["to_user_id"],
						  "to_user_name":o["to_user_name"]})
		#				  
		getFollowers(nodes)
						  
		#fo.write(json.dumps(nodes))
		return "wrote"