Array.prototype.splitBy = function(n) {
/* get: number of items per array
return: array of n-sized arrays with the items (last array may contain less then n) */
    for (var r=[], i=0; i<this.length; i+=n)
        r.push(this.slice(i, i+n));
    return r;
}
var results = [];
var Twitter = {
	searchBaseURL: 'http://search.twitter.com/search.json',
	search: function(options, fn){
		/* 'query' is required
		'until' defaults to current date formatted for twitterAPI */
		var default_options = {
			//'page' : 1,
			'url': false,
			'rpp' : 100,
			'until' : function(){var d = new Date(); return (d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate());}()
		}
		
		/*If an option is not passed, set it to the default_option */
		for(var index in default_options) {
		if(typeof options[index] == "undefined") options[index] = default_options[index];
		}
		
		//refactor this quicky, first time add all the options. second+ time just use the returnURL
		if (options.url){
			var lookupURL = this.searchBaseURL + options.url;
		}
		else{
			var lookupURL = this.searchBaseURL +"?q=" + options.query + "&" + "rpp=" + options.rpp;
		}
		$.getJSON(lookupURL+'&callback=?',  function(json)
			{	
			if (!json.error){
			console.log(json);
			results = results.concat(json.results);
			Twitter.search({url: json.next_page},fn);
			}
			else{
			console.log(results);
			fn();
			}
			});
	}
}

function resultsToIDs(results_list){
	var id_list=[]
	for(var i in results_list){
		id_list.push(results_list[i].from_user_id)
	}
	return id_list
}

var user_list=[]
function getUsers(id_list, fn){
	
	function splitAndQ(mID_list){
	/*transforms the list of numerical ids to a list of twitter user objects */
	var lookupBase='http://api.twitter.com/1/users/lookup.json?user_id='
	var lookupurl=lookupBase;
	for(var i=0;i<mID_list.length;i++){
	lookupurl=lookupurl+mID_list[i]+','
	}
	$.getJSON(lookupurl+'&callback=?',  function(json)
		{	
			user_list=user_list.concat(json);
			console.log("splitandQ")
			fn()
		});
	}
	
	id_list.splitBy(100).forEach(splitAndQ);
	
	
}



//maps and lookup--quick/ very dirty below
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