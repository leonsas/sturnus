Array.prototype.splitBy = function(n) {
/* get: number of items per array
return: array of n-sized arrays with the items (last array may contain less then n) */
    for (var r=[], i=0; i<this.length; i+=n)
        r.push(this.slice(i, i+n));
    return r;
}
function getFriendsNumber(screen_name,fn){
lookupurl='http://api.twitter.com/1/users/lookup.json?screen_name=' + screen_name
$.getJSON(lookupurl+'&callback=?',  function(json)
		{	
		fn(json[0].friends_count);
		});
}
function getRateLimit(jquery_selection){

var url='https://api.twitter.com/1/account/rate_limit_status.json'
$.getJSON(url+'?callback=?',function(json){
//make it return so it can be reused
jquery_selection.text(json.remaining_hits);
});
}
//Call fn with a dictionary of the resulting json
function getUserFriends(screen_name,fn){
user_list=[]
var url='http://api.twitter.com/1/friends/ids.json?cursor=-1&screen_name=' + screen_name + '&callback=?';   
var id_list =[]

function getUserChunkInfo(id_list){
	/*transforms the list of numerical ids to a list of twitter user objects */
	lookupBase='http://api.twitter.com/1/users/lookup.json?user_id='
	lookupurl=lookupBase;
	for(var i=0;i<id_list.length;i++){
	lookupurl=lookupurl+id_list[i]+','
	}
	$.getJSON(lookupurl+'&callback=?',  function(json)
		{	
			user_list=user_list.concat(json);
			dict={};
		dict["nodes"]=user_list;
		fn(dict);
		});
}


$.getJSON(url,  function(json)
{	
	id_list=json.ids
	id_list.splitBy(100).forEach(getUserChunkInfo);
	
});
	
	
}