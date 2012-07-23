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
	print "screenname: %s" % screenname
	id = None
	if screenname:
		user=tweepy.api.get_user(screen_name=screenname)
		id=user.id
		print id
	
	return render_to_response('base.html',
                                   {"user_id":id},
                                 context_instance=RequestContext(request)
                                )
	
def json_server(request, user_id=None):
    retStr=str(friendgrapher.create_dataset(friendgrapher.getFriends(user_id)))
    return HttpResponse(retStr)
		

def json_builder(request,user_id):

	return render_to_response('force-no-links.html',
							   {'user_id':user_id,
							   },
							 context_instance=RequestContext(request)
							)
