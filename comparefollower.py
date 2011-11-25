"""
A script to check the diff betweet the followers of two users


-----------------------------------------------------------------------------
"THE NERD-WARE LICENSE" (Revision 1):
<viirus@pherth.net> wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me/us a beer, mate or some food in return
Phillip Thelen
-----------------------------------------------------------------------------
"""

import tweepy
import sys

def compareFollowers():
	args = sys.argv
	if len(args) < 3:
		sys.exit(2)
	user1 = args[1]
	user2 = args[2]
	#User 1:
	followers1 = getFollowers(user1)
	print "Got the Followers of " + user1

	#User 2:
	followers2 = getFollowers(user2)
	print "Got the Followers of " + user2

	u1diff = [follower for follower in followers1 if not follower in followers2]
	print "People who only follow " + user1
	print u1diff
	print "\n\n"
	u2diff = [follower for follower in followers2 if not follower in followers1]
	print "People who only follow " + user2
	print u2diff

def getFollowers(user):
	return [follower.screen_name for follower in tweepy.Cursor(tweepy.API().followers, user=user).items()]

if __name__ == "__main__":
	compareFollowers()
