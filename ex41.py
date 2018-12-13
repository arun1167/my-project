import random
from urllib import urlopen
import sys

WORD_URL="http://learncodethehardway.org/words.txt"
WORDS=[]

PHRASES={
	"class %%%(%%%):":
	"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef _init_(self,***)":
	"class %%% has-a _init_ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self,@@@)":
	"class %%% has-a fucntion named *** that takes off and @@@ parameters.",
	"***=%%%()":
	"set *** to an instance of the class %%%.",
	"***.***(@@@)":
	"From *** to get the *** function, and call it with parameters self, @@@.",
	"***.***='***'":
	"from *** to get *** attribute and set it to '***'."
		}

# do they waht to drill phrases first

PHRASE_FIRST=False
if len(sys.argv)==2 and sys.argv[1]=="english":
	PHRASE_FIRST=true

#load up the word from website
for word in urlopen(WORD_URL).readline():
	WORDS.append(word.strip())

def convert(snippet,phrase):
	class_names=[w.capitalize() for w in
				 random.sample(WORDS,snippet.count("###"))]
	other_names=random.sample(WORDS,snippet.count("***"))
	results=[]
	param_names=[]

	for i in range(0,snippet.count("@@@")):
		param_count=random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS,param_count)))

	for sentence in snippet,phrase:
		result=sentence[:]

		for word in class_names:
			result=result.replace("###",word,1)

	#fake other names
		for word in other_names:
			result=result.replace("***",word,1)

	#fake parameter list
		for word in param_names:
			result=result.replace("@@@",word,1)

		results.append(result)
	return results
#keep going until hit CTRL+D
try:
	while True:
		snippets=PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase=PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question,answer=answer,question

			print question

			raw_input("> ")
			print "ANSWER:  %s\n\n" %answer
except EOFError:
	print "\nBye"

