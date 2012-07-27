from django.http import HttpResponse
from django.template import Context
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
import urllib
import simplejson as json
from node_builder import buildNodes
import friendgrapher
import tweepy
	
def home(request,screenname=None):

	id = None
	if screenname:
		user=tweepy.api.get_user(screen_name=screenname)
		id=user.id
	
	
	return render_to_response('base.html',
                                   {"user_id":id},
                                 context_instance=RequestContext(request)
                                )
	
def json_server(request, user_id=None):
    print "getting info: %s" % (str(user_id))
    #get all the info from the friends, and send it as a json
    retStr=str(friendgrapher.create_dataset(friendgrapher.getFriends(user_id)))
    #retStr="{\"locs\":[{\"lat\":0,\"lng\":0},{\"lat\":6,\"lng\":61},{\"lat\":39,\"lng\":31}]}"
    return HttpResponse(retStr)
		

def json_builder(request,user_id):

	return render_to_response('force-no-links.html',
							   {'user_id':user_id,
							   },
							 context_instance=RequestContext(request)
							)
def map_test(request, screenname=None):
	print "map_test"
	
	
	return render_to_response('maps.html',
                                   
							 context_instance=RequestContext(request)
							)
							
def testing_twitlib(request):
	return render_to_response('twitlib.html',
							 context_instance=RequestContext(request)
							)
def usingjs_view(request):
	return render_to_response('bubble-js.html',
							 context_instance=RequestContext(request)
							)