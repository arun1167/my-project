class song(object):
	
	def __init__(self,lyrics):
		self.lyrics=lyrics
	
	def sing_me_a_song(self):
			for line in self.lyrics:
				print line

happy_bday=song(["Happy bithday to you",
				 "I do't want to get sued",
				 "So i got stop right there"])

bulls_on_parade=song(["They really around the family",
						"with pocket fullof shells"])
print "**********************************************"
happy_bday.sing_me_a_song()
print "**********************************************"
bulls_on_parade.sing_me_a_song()
print "**********************************************"

