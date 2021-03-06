"""
Name: S Swetha

Sub: Artificial Intelligence

Project II

Phase II

"""

import nltk	
import sys
from collections import Counter

# This function returns a list of variable, corresponding to players who satisfy the criteria : strike rate > 150.0
def parse_for_sr(m,num):
	toreturn = {}

	# strike rate is in the 7th column
	for i in m:
		for j in m[i]['bats']:
			temp = m[i]['bats'][j]
			k = float(temp[6])
			if k > num:
				toreturn[i] = j
	#print toreturn
	return  toreturn


# the function to make the model and answer the query, given the properly formatted strings
def make_model_and_answer1(v, query,dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print m.evaluate(query, g)
	
def generate_and_solve_query1(m):
	
	#find all pom teams
	pm = []
	for i in m['pom']:
		temp = m['pom'][i]
		pm.append(temp[1]);

	#find win teams
	w = []
	for i in m['wint']:
		temp = m['wint'][i]
		w.append(temp[0]);

	# this is for the predicate "srate"
	temp_strin2 = 'pom => {'
	for i in pm:
		temp_strin2 += i +  ','

	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'


	#now for the predicate "gtsix"
	temp_strin3 = 'wint => {'
	for i in w:
		temp_strin3 += i + ','

	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'

	v = temp_strin2 + temp_strin3
	
	# now forming the query
	query = 'all x (pom(x) -> wint(x))'
	
	make_model_and_answer1(v, query, m['pom'])



def make_model_and_answer3(v, query,dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	
	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])

	print m.evaluate(query, g)

	

def generate_and_solve_query3(M):
	
	cp1 = []
	cm1 =[]
	cp2 = []
	cm2 = []
	
	for i in M:
		for j in M[i]:
			if j != 'lose' and j != 'win' :
				for k in M[i][j]['bats'].keys():
						#print L
						#print M[i][j]['bats'][L]
						for player in M[i][j]['bats'][k]:
							if float(M[i][j]['bats'][k][player][6]) > 200:
								#print player
								cm1.append(i+str(j));
								cp1.append(player);
							if int(M[i][j]['bats'][k][player][4]) < int(M[i][j]['bats'][k][player][5]):
								cm2.append(i+str(j));
								cp2.append(player);
	

			
			
	#print cm1,cp1,cm2,cp2
	#c1, c2 are lists of tuples with match,player with sr> 200 , hits respectively
	c1 = zip(cm1,cp1)
	c2 = zip(cm2,cp2)

	temp_strin2 = 'sr => {'
	temp_strin2 += ",".join("(%s,%s)" % tup for tup in c1)
	temp_strin2 += '} \n'
	
	temp_strin3 = 'hit => {'
	temp_strin3 += ",".join("(%s,%s)" % tup for tup in c2)
	temp_strin3 += '} \n'
	
	#print temp_strin2
	#print temp_strin3

	v = temp_strin2 + temp_strin3
	#print v
	# now forming the query
	query = 'all x all y (sr(x,y) -> hit(x,y))'
	
	make_model_and_answer3(v, query, M)
	


def make_model_and_answer2(v, query,dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])

	print m.evaluate(query, g)


	
def generate_and_solve_query2(M):

	match = [];
	
	for i in M:
		L = M[i]['lose']
		for j in M[i]:
			if j != 'lose' and j != 'win' :
				#print M[i][j]['bats'].keys(),L
				for k in M[i][j]['bats'].keys():
					if k == L :
						#print L
						#print M[i][j]['bats'][L]
						for player in M[i][j]['bats'][L]:
							if M[i][j]['bats'][L][player][1] == '0':
								#print player
								match.append(i);

	allm = ['m1','m2','m4','m5']

	# this is for the predicate "srate"
	temp_strin2 = 'lose => {'
	for i in match:
		temp_strin2 += i +  ','

	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'


	#now for the predicate "gtsix"
	temp_strin3 = 'allm => {'
	for i in allm:
		temp_strin3 += i + ','

	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'

	v = temp_strin2 + temp_strin3
	#print v
	# now forming the query
	query = 'all x (allm(x) & ( allm(x) -> lose(x) ))'
	
	make_model_and_answer2(v, query, M)



def make_model_and_answer4(v, query,dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])

	print m.evaluate(query, g)


	
def generate_and_solve_query4(M):

	match = [];
	
	for i in M:
		L = M[i]['win']
		for j in M[i]:
			if j != 'lose' and j != 'win' :
				#print M[i][j]['bats'].keys(),L
				for k in M[i][j]['bats'].keys():
					if k == L :
						#print L
						#print M[i][j]['bats'][L]
						for player in M[i][j]['bats'][L]:
							#print int(M[i][j]['bats'][L][player][4]),float(M[i][j]['bats'][L][player][6])
							if int(M[i][j]['bats'][L][player][4]) > 0 and float(M[i][j]['bats'][L][player][6]) < 100  :
								#print player
								match.append(i);

	
	allm = ['m1','m2','m4','m5']

	# this is for the predicate "srate"
	temp_strin2 = 'lose => {'
	for i in match:
		temp_strin2 += i +  ','

	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'


	#now for the predicate "gtsix"
	temp_strin3 = 'allm => {'
	for i in allm:
		temp_strin3 += i + ','

	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'

	v = temp_strin2 + temp_strin3
	#print v
	# now forming the query
	query = 'all x (allm(x) & (allm(x)->lose(x)))'
	
	make_model_and_answer4(v, query, M)



def make_model_and_answer5(v, query,dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])

	print m.evaluate(query, g)


	
def generate_and_solve_query5(M):

	hitp = []
	hitm = []
	wickp = []
	wickm = []

	for i in M:
		for j in M[i]:
			if j != 'lose' and j != 'win' :
				#print M[i][j]['bats'].keys(),L
				for k in M[i][j]['bats'].keys():
					#print k
					for player in M[i][j]['bats'][k]:
						#print int(M[i][j]['bats'][L][player][4]),float(M[i][j]['bats'][L][player][6])
						if int(M[i][j]['bats'][k][player][1]) > 50 :
							#print j
							hitp.append(player);
							hitm.append(i);
				for k in M[i][j]['bowl'].keys():
					#print k
					for player in M[i][j]['bowl'][k]:
						#print int(M[i][j]['bats'][L][player][4]),float(M[i][j]['bats'][L][player][6])
						if int(M[i][j]['bowl'][k][player][3]) > 0 :
							#print j
							wickp.append(player);
							wickm.append(i);

	
	c1 = zip(hitp,hitm)
	c2 = zip(wickp,wickm)

	temp_strin2 = 'hit => {'
	temp_strin2 += ",".join("(%s,%s)" % tup for tup in c1)
	temp_strin2 += '} \n'
	
	temp_strin3 = 'wick => {'
	temp_strin3 += ",".join("(%s,%s)" % tup for tup in c2)
	temp_strin3 += '} \n'
	
	#print temp_strin2
	#print temp_strin3

	v = temp_strin2 + temp_strin3
	#print v
	# now forming the query
	query = 'exists x all y (hit(x,y) -> wick(x,y))'
	make_model_and_answer5(v, query, M)
	


def make_model_and_answer6(v, query,dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	#print m
	g = nltk.Assignment(dom, [])

	print m.evaluate(query, g)

	

	
def generate_and_solve_query6(M):

	over = []
	match1 = [];
	wick = []
	match2 = []

	for i in M:
		for j in M[i]:
			if j != 'lose' and j != 'win' :
				#print M[i][j]['bowl'].keys() 
				for k in M[i][j]['bowl'].keys():
					#print k
					#print M[i][j]['bats'][L]
					for player in M[i][j]['bowl'][k]:
						#print int(M[i][j]['bowl'][k][player][3])#,float(M[i][j]['bowl'][k][player][3])
						if float(M[i][j]['bowl'][k][player][0]) > 7:
							#print player
							over.append(player);
							match1.append(str(i));
						if int(M[i][j]['bowl'][k][player][3]) <= 0:
							wick.append(player);
							match2.append(str(i));

	c1 = zip(match1,over)
	c2 = zip(match2,wick)

	temp_strin2 = 'over => {'
	temp_strin2 += ",".join("(%s,%s)" % tup for tup in c1)
	temp_strin2 += '} \n'
	
	temp_strin3 = 'wick => {'
	temp_strin3 += ",".join("(%s,%s)" % tup for tup in c2)
	temp_strin3 += '} \n'
	
	#print temp_strin2
	#print temp_strin3

	v = temp_strin2 + temp_strin3
	#print v
	# now forming the query
	query = 'all x exists y (over(x,y) -> wick(x,y))'
	
	make_model_and_answer6(v, query, M)
	

def make_model_and_answer7(v, query,dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	#print m
	g = nltk.Assignment(dom, [])

	print m.evaluate(query, g)


	
def generate_and_solve_query7(M):

	econ = [];
	match1 = [];
	wick = [];
	match2 = [];
	
	for i in M:
		for j in M[i]:
			if j != 'lose' and j != 'win' :
				#print M[i][j]['bowl'].keys() 
				for k in M[i][j]['bowl'].keys():
					#print k
					#print M[i][j]['bats'][L]
					for player in M[i][j]['bowl'][k]:
						#print int(M[i][j]['bowl'][k][player][3])#,float(M[i][j]['bowl'][k][player][3])
						if float(M[i][j]['bowl'][k][player][4]) > 8 :
							#print player
							econ.append(player);
							match1.append(i);
						if int(M[i][j]['bowl'][k][player][3]) <= 0 :
							wick.append(player);
							match2.append(i);

	c1 = zip(match1,econ)
	c2 = zip(match2,wick)

	temp_strin2 = 'over => {'
	temp_strin2 += ",".join("(%s,%s)" % tup for tup in c1)
	temp_strin2 += '} \n'
	
	temp_strin3 = 'wick => {'
	temp_strin3 += ",".join("(%s,%s)" % tup for tup in c2)
	temp_strin3 += '} \n'
	
	v = temp_strin2 + temp_strin3
	#print v

	query = 'all x exists y ((over(x,y) -> wick(x,y)))'

	#query = 'all x exists y (over(x,y) & (wick(x,y) -> over(x,y)))'	#for all matches
	make_model_and_answer7(v, query, M)




def make_model_and_answer8(v, query,dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])

	print m.evaluate(query, g)

	
	
def generate_and_solve_query8(M):

	match1 = [];
	centp = [];
	match2 = [];
	lost = [];
	
	for i in M:
		if i != 'm3':
			L = M[i]['lose']
			match2.append(i);
			lost.append(L);
			for j in M[i]:
				if j != 'lose' and j != 'win' :
					#print M[i][j]['bats'].keys(),L
					for k in M[i][j]['bats'].keys():
						for player in M[i][j]['bats'][k]:
							if int(M[i][j]['bats'][k][player][1]) >= 100:
								#print player
								centp.append(k);
								match1.append(i);
	
	

	c1 = zip(match1,centp)
	c2 = zip(match2,lost)
		
	temp_strin2 = 'cent => {'
	temp_strin2 += ",".join("(%s,%s)" % tup for tup in c1)
	temp_strin2 += '} \n'
	
	temp_strin3 = 'lost => {'
	temp_strin3 += ",".join("(%s,%s)" % tup for tup in c2)
	temp_strin3 += '} \n'
	
	v = temp_strin2 + temp_strin3
	#print v

	query = 'exists x all y (cent(x,y)->lost(x,y))'
	make_model_and_answer8(v, query, M)
	

# A9 For  all  matches, right  handed bowlers claim more wickets than left handed bowlers. 
def make_model_and_answer9(v, query,dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	
	print m.evaluate(query, g)
	
	
	
	
def generate_and_solve_query9(M,Ip,Np):

	Ib = []
	Nb = []
	Rb = {}
	Rbm = []
	Lb = {}
	Lbm = []
	
	for i in M:
		Rb[i] = []
		Lb[i] = []
		for j in M[i]:
			if j != 'lose' and j != 'win' :
				#print M[i][j]['bats'].keys(),L
				for k in M[i][j]['bowl'].keys():
					for player in M[i][j]['bowl'][k]:
						if player in Np.keys():
							#if player not in Nb:
							Nb.append(player);
							#print "Np",Np[player][-1]
							if Np[player][-1][0] == 'R':
								#Rb.append(player)
								Rb[i].append(player);
								#Rbm.append(i)
							if Np[player][-1][0] == 'L':
								Lb[i].append(player)
								#Lbm.append(i)
					
						if player in Ip.keys():
							#if player not in Ib:
							Ib.append(player);
							#print "Ip",Ip[player][-1]
							if Ip[player][-1][0] == 'R':
								#print player
								Rb[i].append(player)
								#Rbm.append(i)
							else:
								Lb[i].append(player)
								#Lbm.append(i)

	

	Rw = {}
	Lw = {}
	rw = 0
	lw = 0
	for i in M:
		rw = 0
		lw = 0
		for j in M[i]:
			if j != 'lose' and j != 'win' :
				for k in M[i][j]['bowl'].keys():
					for player in M[i][j]['bowl'][k]:
						if player in Rb[i]:
							#print i,"r"
							rw += int(M[i][j]['bowl'][k][player][3])
						else:
							#print i,"l"
							lw +=  int(M[i][j]['bowl'][k][player][3])
		#print rw,lw
		Rw[i] = rw
		Lw[i] = lw
	#print rw,lw
			
	res = []
	#print Rw,Lw			
	
	for i in Rw:		
		if int(Rw[i]) > int(Lw[i]):
			res.append(i)
	#else:
	#	res.append(0)
	#print res

	temp_strin4 = 'moreWickets => {'
	for i in res:
		temp_strin4 += str(i) +  ','

	temp_strin4 = temp_strin4[:-1]  #removing the extra "," character
	temp_strin4 += '} \n'

	temp_strin5 = 'exp => {'
	for i in Rw:
		temp_strin5 += str(i) +  ','

	temp_strin5 = temp_strin5[:-1]  #removing the extra "," character
	temp_strin5 += '} \n'
	
	v = temp_strin4 + temp_strin5
	#print v

	query = 'all x ( exp(x) -> moreWickets(x))'
	make_model_and_answer9(v, query, M)



#A10 6 age
def make_model_and_answer10(v, query,dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	
	print m.evaluate(query, g)
	

	


#Q 10
def generate_and_solve_query10(M,Ip,Np):

	match = [];
	runs = {}
	remPlayer =[]
	req = []
	Age = []
	
	for i in M:
		for j in M[i]:
			if j != 'lose' and j != 'win' :
				#print M[i][j]['bats'].keys(),L
				for k in M[i][j]['bats'].keys():
					for player in M[i][j]['bats'][k]:
						#if int(M[i][j]['bats'][k][player][1]) >= 100:
						#print player
						if player in Np.keys():
							#print player
							#print player,Np[player][4]
							age = int(str(Np[player][4][0])+str(Np[player][4][1]))
							if age < 26:
								if player not in Age: 
									Age.append(player);
								if player not in runs.keys() and player not in remPlayer:
									runs[player] = []
								if (int(M[i][j]['bats'][k][player][1]) <= 0 ):
									del runs[player]
									remPlayer.append(player)
								elif player in runs.keys():
									runs[player].append(int(M[i][j]['bats'][k][player][1])) 
						if player in Ip.keys():
							#print player,Ip[player][4]
							age = int(str(Ip[player][4][0])+str(Ip[player][4][1]))
							if age < 26:
								if player not in Age: 
									Age.append(player);

								if player not in runs.keys() and player not in remPlayer:
									runs[player] = []
								if (int(M[i][j]['bats'][k][player][1]) <= 0 ):
									if player in runs.keys():
										del runs[player]
									remPlayer.append(player)
								elif player in runs.keys():
									runs[player].append(int(M[i][j]['bats'][k][player][1])) 

	for i in runs.keys():
		l = runs[i]
		run = 0
		for j in l:
			run += j
		runs[i] = run

	#print runs
	for i in runs.keys():
		if runs[i] > 250:
			req.append(i)
	#print req
	#print Age
	
	temp_strin2 = 'req => {'
	for i in req:
		temp_strin2 += i +  ','

	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'

	v = temp_strin2 

	temp_strin3 = 'Age => {'
	for i in Age:
		temp_strin3 += i +  ','

	temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
	temp_strin3 += '} \n'

	v = temp_strin2 + temp_strin3 
	#print v
	# now forming the query
	query = 'exists x ( req(x) -> Age(x) )'
	
	make_model_and_answer10(v, query, M)





def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b



data=[]; # will hold the lines of the file
dictionary = {};
Ipf = [];
Npf = [];
name = [];
nouns = [];
verbs = [];
ques = [];
desc = [];
conn = [];
ad = [];
nns = [];
Num = [];
inn = [];
team = [];
um = un = em = ep = False;
#
# function to add the contents of file, after proper parsing, to the given dictionary
def add_to_dict(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b

# To solve the query
def solve(query):

	rec = {}
	wideRec ={}
	nbRec = {}
	runo = [];
	Runnum = 0
	score  = 0
	bowler = False
	ov = False
	num = False
	onum = 0;
	b = False
	#print 'solving...'
	
	if query.find(' and') >= 0:
		conn.append(' and');
		desc = query.split(' and');
		#print nltk.pos_tag(nltk.word_tokenize(desc[0]))
		#print nltk.pos_tag(nltk.word_tokenize(desc[1]))
		#print desc[0]
		#print desc[1]
	elif query.find('consists of') >= 0:
		conn.append('consists of');
		desc = query.split('consists of');
		#print desc[0]
		#print desc[1]
	elif query.find(' than') >= 0:
		conn.append(' than');
		desc = query.split(' than');
	elif query.find('is given to') >= 0:
		conn.append('is given to');
		desc = query.split('is given to');
		#print desc[0]
		#print desc[1]
	elif query.find('contains') >= 0:
		conn.append('contains');
		desc = query.split('contains');
		#print desc[0]
		#print desc[1]
	elif query.find('if') >= 0 and query.find('then') >= 0:
		conn.append('if');
		start = query.find('if');
		end = query.find('then');
		antecedent = query[start+3:end];
		consequent = query[end+5:];
		#print consequent
	print 'conn',conn
	
	#tokenize each desc
	total = nltk.word_tokenize(desc[0])
	stag = nltk.pos_tag(total)
	print 'predicates are:',
	for i in stag:
		if i[1].find('N') == 0:
			print i[0],
		if i[1].find('V') == 0:
			print i[0],
		if i[1] == 'CD':
			print i[0],
		if i[1].find('J') == 0:
			print i[0],
		
	print
	
	#	print stag
	
	
	total = nltk.word_tokenize(desc[1])
	stag = nltk.pos_tag(total)
	#print stag
	print 'predicates are:',
	for i in stag:
		if i[1].find('N') == 0:
			print i[0],
		if i[1].find('V') == 0:
			print i[0],
		if i[1] == 'CD':
			print i[0],
		if i[1].find('J') == 0:
			print i[0],
		
	print

	#got the connectors, predicates and quantifiers
	
	
# Make tokens for given query
def makeTokens(query):
	print "tokenizing..."
	temp = query
	
	#total
	total = nltk.word_tokenize(query)
	stag = nltk.pos_tag(total)
	
	if query.find('For all matches') >= 0 or ('In any of the matches'):
		um =  True
	elif query.find('For all innings') >= 0:
		un =  True
	elif query.find('There exists a match') >= 0:
		em =  True
	elif query.find('There exists player') >= 0:
		ep =  True

	print stag

	for i in stag:
		if i[1] == 'CD':
			Num = int(i[0])
		if i[1].find('V') == 0:
			verbs.append(i[0]);
		if i[1].find('N') == 0:
			nouns.append(i[0]);
		if i[1].find('J') == 0:
			ad.append(i[0]);
		if i[1].find('W') == 0:
			ques.append(i[0]);

	print 'verbs',verbs
	print 'adj',ad
	print 'noun',nouns
	
	#print matchNum
		


def main():

	


	m = {

		'm1' : {
			'bats' : {},'bowl' : {}
			},
		'm2' : {
			'bats' : {},'bowl' : {}
			}
		}
	m1 = {
		'pom' : {},
		'wint' : {},
		'lose' : {}
		}

	M = {

		'm1' : {
			'1' : {
				'bats': {
					'New Zealand' : {}
					},
				'bowl': {
					'India' : {}
					}
				},
			'2' : {
				'bats': {
					'India' : {}
					},
				'bowl': {
					'New Zealand' : {}
					}	
				},
			'lose' : 'India',
			'win' : 'New Zealand'
			},

		'm2' : {
			'1' : {
				'bats': {
					'New Zealand' : {}
					},
				'bowl': {
					'India' : {}
					}
				},
			'2' : {
				'bats': {
					'India' : {}
					},
				'bowl': {
					'New Zealand' : {}
					}	
				},
			'lose' : 'India',
			'win' : 'New Zealand'
			},

		'm3' : {
			'1' : {
				'bats': {
					'New Zealand' : {}
					},
				'bowl': {
					'India' : {}
					}
				},
			'2' : {
				'bats': {
					'India' : {}
					},
				'bowl': {
					'New Zealand' : {}
					}	
				},
			'lose' : 'None',
			'win' : 'None'
			},

		'm4' : {
			'1' : {
				'bats': {
					'India' : {}
					},
				'bowl': {
					'New Zealand' : {}
					}
				},
			'2' : {
				'bats': {
					'New Zealand' : {}
					},
				'bowl': {
					'India' : {}
					}	
				},
			'lose' : 'India',
			'win' : 'New Zealand'
			},

	
		'm5' : {
			'1' : {
				'bats': {
					'New Zealand' : {}
					},
				'bowl': {
					'India' : {}
					}
				},
			'2' : {
				'bats': {
					'India' : {}
					},
				'bowl': {
					'New Zealand' : {}
					}	
				},
			'lose' : 'India',
			'win' : 'New Zealand'
			}

		}
	Ipf = {}
	Npf = {}
	names = {}
	Toss = {}

	c = 1
	for i in range(1,5):
		f+str(c) = 'dataset/match'+str(i)+'/odi'+str(i)+'_inni1_bat.txt'
		f+str(c+1) = 'dataset/match'+str(i)+'/odi'+str(i)+'_inni2_bat.txt'
		f+str(c+2) = 'dataset/match'+str(i)+'/odi'+str(i)+'_inni1_bowl.txt'
		f+str(c+3) = 'dataset/match'+str(i)+'/odi'+str(i)+'_inni2_bowl.txt'
		c = c+ 4

	Pom = ' dataset/pom.txt'
	WinT = ' dataset/winTeam.txt' 
	l = ' dataset/lose.txt'
	ipf = ' dataset/player_profile1/indian_players_profile.txt'
	npf = ' dataset/player_profile1/nz_players_profile.txt'
	n = ' dataset/Names.txt'
	toss = ' dataset/toss.txt'

	add_to_dict( M['m1']['1']['bats']['New Zealand'], f1 );
	add_to_dict( M['m1']['2']['bats']['India'], f2 );

	add_to_dict( M['m1']['1']['bowl']['India'], f3 );
	add_to_dict( M['m1']['2']['bowl']['New Zealand'], f4 );

	add_to_dict( M['m2']['1']['bats']['New Zealand'], f5 );
	add_to_dict( M['m2']['2']['bats']['India'], f6 );

	add_to_dict( M['m2']['1']['bowl']['India'], f7 );
	add_to_dict( M['m2']['2']['bowl']['New Zealand'], f8 );

	add_to_dict( M['m3']['1']['bats']['New Zealand'], f9 );
	add_to_dict( M['m3']['2']['bats']['India'], f10 );

	add_to_dict( M['m3']['1']['bowl']['India'], f11 );
	add_to_dict( M['m3']['2']['bowl']['New Zealand'], f12 );

	add_to_dict( M['m4']['1']['bats']['India'], f13 );
	add_to_dict( M['m4']['2']['bats']['New Zealand'], f14 );

	add_to_dict( M['m4']['1']['bowl']['New Zealand'], f15 );
	add_to_dict( M['m4']['2']['bowl']['India'], f16 );

	add_to_dict( M['m5']['1']['bats']['New Zealand'], f17 );
	add_to_dict( M['m5']['2']['bats']['India'], f18 );

	add_to_dict( M['m5']['1']['bowl']['India'], f19 );
	add_to_dict( M['m5']['2']['bowl']['New Zealand'], f20 );

	add_to_dict( Ipf, ipf);
	add_to_dict( Npf, npf);
	add_to_dict( names, n);
	add_to_dict( Toss, toss);
	#print M['m1']['2'].keys()

	add_to_dict( m['m1']['bats'], f1 );
	add_to_dict( m['m1']['bats'], f2 );

	add_to_dict( m['m1']['bowl'], f3 );
	add_to_dict( m['m1']['bowl'], f4 );

	add_to_dict( m['m2']['bats'], f5 );
	add_to_dict( m['m2']['bats'], f6 );

	add_to_dict( m['m2']['bowl'], f7 );
	add_to_dict( m['m2']['bowl'], f8 );

	add_to_dict( m1['pom'], Pom);
	add_to_dict( m1['wint'], WinT);

	add_to_dict( m1['lose'], l);

	

	
	#print "\n/*********************************************************************************************************************************************/\n\nWelcome To Question Answering System!\nPlease enter Query and press enter\nTo Exit PRESS Q\n\n/*********************************************************************************************************************************************/\n"
	#k = 1;
	
	#while k == 1:
	query = raw_input("Pls enter the query:\n");
	if query == 'q' or query == 'Q':
		return			
	makeTokens(query);

	print "Now generating query.."

	

	Q = query.split(',');
	c = 0
	Q1 = query
	for i in Q:
		if c == 0:
			c = 1
		elif c == 1:
			Q1 = str(i)
			c += 1
		else:
			 Q1 = Q1 + str(i)

		
	#print Q1 
	solve(Q1)
		
	
	#print verb, nns,name[0];

	
	if query.find('Player of match award') >= 0 and query.find('player of winning team') >= 0:
		#goto q1 print 'q1'
		generate_and_solve_query1(m1)
	elif query.find('losing side') >= 0 and query.find('at least 1 ducks') >= 0 and query.find('batting innings') >= 0:
		generate_and_solve_query2(M)
	elif query.find('strike rate') >= 0 and query.find('above 200.0') >= 0 and query.find('hit more sixes than fours') >= 0:	
		generate_and_solve_query3(M)
	elif query.find('winning side') >= 0 and query.find('contains at least 1 player') >= 0 and query.find('hit at least 1 boundary') >= 0 and query.find('strike rate') and query.find('below 100'):	
		generate_and_solve_query4(M)
	elif query.find('scored more than 50 runs') >= 0 and query.find('at least 1 wicket') >= 0 and query.find('same match') >= 0:
		generate_and_solve_query5(M)
	elif query.find('bowled more than 7 overs') >= 0 and (query.find('failed to get any wicket') >= 0 or query.find('no wicket') >= 0 ) :
		generate_and_solve_query6(M)
	elif  query.find('bowler') >= 0 and (query.find('failed to get any wicket') >= 0 or query.find('no wicket') >= 0 or query.find('not claim any wicket') >= 0 ) and (query.find('more than 8 runs per over') >= 0 or query.find('economy more than 8') >= 0):	
		generate_and_solve_query7(M)

	elif  query.find('batsman') >= 0 and (query.find('scored hundred') >= 0 or query.find('century') >= 0) and (query.find('team lost') >= 0):	
		generate_and_solve_query8(M)

	elif query.find('right handed bowlers') >= 0 and (query.find('more wickets') >= 0) and query.find('than left handed bowlers') >= 0:
		generate_and_solve_query9(M,Ipf,Npf)
	
	elif query.find('less than 26 years') >= 0 and query.find('scored more than 250 runs') >= 0 and query.find('without any ducks') >= 0:
		generate_and_solve_query10(M,Ipf,Npf)
 
	
	
# Part 2
if __name__ == "__main__":
	main()
