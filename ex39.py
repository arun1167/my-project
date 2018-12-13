# creating the mapping of state of abbreviation
states={
	'Bihar' : 'BR',
	'Jharkhand' : 'JH',
	'Odhissa' : 'OS',
	'West Bengal' : 'WB',
	'Uttar Pradesh' : 'UP',
	'Madhya Pradesh':'MP',
	'Chatteshgarh' : 'CG'
	}
# create basic set of state and some cities of them
cities={
		'JH':'Ranchi',
		'JH':'Bokaro Steel city',
		'OS':'Puri',
		'UP':'Gorakhpur',
		'MP':'Sagar',
		'CG':'Raipur',
		'WB':'Kolkatta',
		'WB':'Khagpur'		
		}
# add some more cities
cities['UP']='Lakhnow'
cities['BR']='Patna'
# printout some cities
print "="*10
print "Bihar State has :",cities['JH']
print "Odhissa states has :",cities['OS']
# printout some states
print "="*10
print "Bihar's abbreviation is :",states['Bihar']
print "Jharkhand's abbreviation is :",states['Jharkhand']
# do it by using the state then cities dict
print "="*10
print "Bihar has :",cities[states['Bihar']]
print "Jharkhand has :",cities[states['Jharkhand']]
#print every state abbrevation
print "="*10
for state,abbrev in states.items():
	print "%s is abbrevated %s" %(state,abbrev)
# print every city in state
print "="*10
for abbrev,city in cities.items():
	print "%s state has %s city" %(abbrev,city)
# now do both at the same time
for state,abbrev in states.items():
	print "%s is abbrivated in %s and has city is %s" %(state,abbrev,cities[abbrev])
print "="*10
# safely gte the stae moght be not here
state=states.get('Bihar',None)
if not state:
	print "Sorry, no Bihar"
# get city a default vales

city=cities.get('BK','Backchod not exist')
print "The city for the state 'BK' is : %s" %city

































