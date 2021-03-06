"""
Name: S Swetha

Sub: Artificial Intelligence

Project II

Phase II

"""
import os
import nltk	
import sys
from collections import Counter
from nltk.corpus import wordnet as wn
#sys.stdout = open('file', 'w')


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
data1=[];
dictionary1 = {};
Ipf = [];
Npf = [];
name = [];
verb = [];
mcn = [];
nns = [];
matchNum = [];
inn = [];
sp = []
team = [];
commentary = [];
PowerplayI = {'0.1': '28, 2', '35.1':'24, 0'}
PowerplayN = {'0.1': '65, 2', '35.1':'24, 0'}
m4 = False

Npp1 = [35.1, 40.0]
Ipp1 = [34.1, 39.0]

Npp2 = [34.1, 38.0]
Ipp2 = [29.1, 33.0]

Npp3 = [34.1, 39.0]
Ipp3 = [35.1, 40.0]

Npp4 = [35.1, 40.0]
Ipp4 = [35.1, 40.0]

Npp5 = [35.1, 40.0]
Ipp5 = [33.1, 38.0]

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



# function to add the contents of file, after proper parsing, to the given dictionary
def add_to_dict1(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		#b = temp[1:]
		if a not in dictionary:
			dictionary.append(a);
seen = []

def pp(m):
	if m == 1:
		return Npp1,Ipp1
		
	if m == 2:
		return Npp2,Ipp2
		
	if m == 3:
		return Npp3,Ipp3
		
	if m == 4:
		return Npp4,Ipp4
		
	if m == 5:
		return Npp5,Ipp5
		

act = {}
uover = []
def isactive(p):
	over = []
	run = 0;
	for i,j in dictionary.iteritems():
		if p in j:
			over.append(i.split('.')[0])
	
	myset = set(over)
	for i in myset: 
		uover.append(i)
	#print uover
	

	for i in uover:
		for j in range(1,6):
			index = str(i)+'.'+str(j) 
			if name[0] in dictionary[index]:
				req = dictionary[index].split(',')[1]
				req.split(' ')
				
				if isfloat(req[1]):
					run += int(req[1])
				elif 'FOUR' in req:
					run += 4
				elif 'SIX' in req:
					run += 6

		act[i] = run
		run = 0
	seen.append(p.split('.')[0])

def isinteresting(inn):
	#see both innings
	over = []
	run = 0;
	interest = {}
	if inn == 1:
		for i in range(0,49):
			for j in range(1,6):
				index = str(i)+'.'+str(j) 
			
				req = dictionary[index].split(',')[1]
				req.split(' ')
			
				if isfloat(req[1]):
					run += int(req[1])
				elif 'FOUR' in req:
					run += 4
				elif 'SIX' in req:
					run += 6

			interest[i] = run
			run = 0
		#seen.append(p.split('.')[0])
	else:
		for i in range(0,49):
			for j in range(1,6):
				index = str(i)+'.'+str(j) 
			
				req = dictionary1[index].split(',')[1]
				req.split(' ')
			
				if isfloat(req[1]):
					run += int(req[1])
				elif 'FOUR' in req:
					run += 4
				elif 'SIX' in req:
					run += 6

			interest[i] = run
			run = 0
		#seen.append(p.split('.')[0])

	return interest
	

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
	print 'solving...'
	
	#print query,query.find('four')
	# hit runs for all questions
	#print name[0]+str('name')
	#print query.find('When')
	if query.find('dismissed') >= 0:
		for p,q in dictionary.iteritems():
			if name[0] in q and 'OUT' in q and query.find('When') >= 0:
				rec[p] = q;
			if name[0] in q and 'OUT' in q and query.find('How') >= 0:
				rec[p] = q;
				#print q
				#print 'run out'
		if rec:	
			print rec.keys()[len(rec.keys())-1],
			print rec[rec.keys()[len(rec.keys())-1]]
		else:
			print 'not OUT'
		return
	
	if query.find('best boundary') >= 0:
		prob = {}
		prob1 = {}
		for p,q in dictionary.iteritems():
			#if 'FOUR' in q and ('clean' or 'classy' or 'excellent' or 'grace' or 'quick'):
			#	print p
			if 'FOUR' in q and ('excellent' in q):
				prob[p] = 1
			if 'FOUR' in q and ('quick' in q):
				prob[p] = 0.8
			if 'FOUR' in q and ('classy' in q):
				prob[p] = 0.7
			if 'FOUR' in q and ('clean'in q):
				prob[p] = 0.6
			if 'FOUR' in q and ('grace' in q):
				prob[p] = 0.5

		for p,q in dictionary1.iteritems():
			#if 'FOUR' in q and ('clean' or 'classy' or 'excellent' or 'grace' or 'quick'):
			#	print p
			if 'FOUR' in q and ('excellent' in q):
				prob1[p] = 1
			if 'FOUR' in q and ('quick' in q):
				prob1[p] = 0.8
			if 'FOUR' in q and ('classy' in q):
				prob1[p] = 0.7
			if 'FOUR' in q and ('clean' in q):
				prob1[p] = 0.6
			if 'FOUR' in q and ('grace' in q):
				prob1[p] = 0.5

		#for p,q in dictionary1.iteritems():
		#	if 'FOUR' in q and ('clean' or 'classy' or 'excellent' or 'grace' or 'quick'):
		#		print p
		maxi = 0
		maxov = 0
		flag = 0
		for p,q in prob.iteritems():
			if int(q) >= maxi:
				maxi = int(q)
				maxov = int(float(p))
				flag = 1
		
		for p,q in prob1.iteritems():
			if int(q) >= maxi:
				maxi = int(q)
				maxov = int(float(p))
				flag = 2
		print maxov,
		if flag == 1:
			print 'Indian Inninngs'
		else:
			print 'New Zealand Innings' 

		return 

	if query.find('active') >= 0:		
		isactive(name[0])
		maxi = 0
	
		for p,q in act.iteritems():
			if int(q) >= maxi:
				maxi = int(q)
				maxov = int(p)
		print maxov
		return

	if query.find('interesting over') >= 0:
		In1 = isinteresting(1)
		In2 = isinteresting(2)
		maxi = 0
		flag = 0
	
		for p,q in In1.iteritems():
			if int(q) >= maxi:
				maxi = int(q)
				maxov = int(p)
				flag = 1
		for p,q in In2.iteritems():
			if int(q) >= maxi:
				maxi = int(q)
				maxov = int(p)
				flag = 2
		print maxov,
		if flag == 1:
			print 'Indian Inninngs'
		else:
			print 'New Zealand Innings' 
		return

	if query.find('powerplay') >= 0:
		pplay = pp(m)
		if query.find('umpire') >= 0 and query.find('signal') >= 0:
			#print m	
			print pplay[0][0],pplay[1][0]
				
			
		elif query.find('bowlers') >= 0 and query.find('immediately after') >= 0:
			for p,q in dictionary.iteritems():
				if int(float(p)) <= 10:
					#find next 4 bowler names 
					sp.append(q.split('to')[0])

				elif int(float(p)) >= int(float(pplay[1][0])) and int(float(p)) <= int(float(pplay[1][1])):
					#find next 4 bowler names 
					sp.append(q.split('to')[0])
			for p,q in dictionary1.iteritems():
				if int(float(p)) <= 10:
					#find next 4 bowler names 
					sp.append(q.split('to')[0])
				elif int(float(p)) >= int(float(pplay[0][0])) and int(float(p)) <= int(float(pplay[0][1])):
					#find next 4 bowler names 
					sp.append(q.split('to')[0])
		
			myset = set(sp)
			for i in myset: print i

							
		return



			
	d = []
	d1 = []
	if query.find('weather') >= 0:
		with open(commentary[0]+'_InnI','rU') as fin:       
			for line in fin:                  # for each line of the file
				line=line.strip()             # remove CR/LF
				if line:                      # skip blank lines
				    d.append(line)
		
		with open(commentary[0]+'_InnN','rU') as fin:       
			for line in fin:                  # for each line of the file
				line=line.strip()             # remove CR/LF
				if line:                      # skip blank lines
				    d1.append(line)



		for i in d:
			#print i
			if 'rain ' in i:
				print i
				print
			if 'sun ' in i:
				print i
				print
			if 'forecast ' in i:
				print i
				print
			if ' light ' in i:
				print i
				print
			if ' day ' in i:
				print i
				print
			if 'breeze ' in i:
				print i
				print
			if 'monsoon ' in i:
				print i
				print
			if 'sky ' in i:
				print i
				print

		for i in d1:
			#print i
			if 'rain ' in i:
				print i
				print
			if 'sun ' in i:
				print i
				print
			if 'forecast ' in i:
				print i
				print
			if ' light ' in i:
				print i
				print
			if ' day ' in i:
				print i
				print
			if 'breeze ' in i:
				print i
				print
			if 'monsoon ' in i:
				print i
				print
			if 'sky ' in i:
				print i
				print

		return
	# Wides and No balls for all questions
	elif query.find('wide') >= 0 or query.find('no ball') >= 0:
		wo = []
		maxi =[]
		nbo = []
		for p,q in dictionary.iteritems():
				#print 'wide' in q.split(',')[1]
				if query.find('wide') >= 0 and name[0] in q and 'wide' in q.split(',')[1]:
					#print  p#print 'wide'
					wideRec[p] = q
				elif query.find('no ball') >= 0 and name[0] in q and 'no ball' in q.split(',')[1]:
					#print  p#print 'wide'
					nbRec[p] = q

		for p in wideRec.keys():
				wo.append(int(p.split('.')[0]))
		for p in nbRec.keys():
				nbo.append(int(p.split('.')[0]))
		#print nbo

		if query.find('which over') >= 0 and query.find('maximum') >= 0:
			maxwide = 0
			maxnb = 0
			for i  in Counter(wo).items():
				if int(i[1]) > maxwide:
					maxwide = i[1]
					
			for i  in Counter(wo).items():
				if i[1] == maxwide:
					maxi.append(i[0]);

			for i  in Counter(nbo).items():
				if int(i[1]) > maxnb:
					maxnb = i[1]
					
			for i  in Counter(nbo).items():
				if i[1] == maxnb:
					maxi.append(i[0]);
			print maxi

		elif query.find('which over') >= 0 and query.find('minimum') >= 0:
			maxwide = 10
			maxnb = 10
			for i  in Counter(wo).items():
				if int(i[1]) < maxwide:
					maxwide = i[1]
					
			for i  in Counter(wo).items():
				if i[1] == maxwide:
					maxi.append(i[0]);
			for i  in Counter(nbo).items():
				if int(i[1]) < maxnb:
					maxnb = i[1]
					
			for i  in Counter(nbo).items():
				if i[1] == maxnb:
					maxi.append(i[0]);
			print maxi
					
		elif query.find('which over') >= 0 and query.find('wide') >= 0:
			for p in wideRec.keys():
				print  p.split('.')[0]
		elif query.find('which over') >= 0 and query.find('no ball') >= 0:
			for p in nbRec.keys():
				print  p.split('.')[0]

# Make tokens for given query
def makeTokens(query):
	print "tokenizing..."
	temp = query
	#nltk.corpus.brown.tagged_words()
	
	#temp = temp.split(',')
	#total
	
		#first part grammar
	text = nltk.word_tokenize(temp)
	stag = nltk.pos_tag(text)
	#print stag
	for i in stag:
		if i[1] == 'CD':
			matchNum.append(int(i[0]))
			mcn.append(int(i[0]))
		elif i[1] == 'JJ':
			matchNum.append(i[0])
		elif i[1] == 'NNP':
			name.append(i[0]);
		
	#print matchNum,mcn,name

	#second part grammar
	#text2 = nltk.word_tokenize(temp[1])
	#s2 = nltk.pos_tag(text2)
	#print s2
	#name.append(s2[0][0])#found name so find team!!
	
	if name and name[0] in Ipf:
		team.append('India')
	elif name:
		team.append('New Zealand')
	
	c = 0;
	#get the verb VBD
	for i in stag:
		c += 1;
		if i[1] == 'VBD':
			verb.append(i[0])  
			#print i[0] #is verb
			#nns.append(s2[c][0]);
			#print s2[c][0]

		#if i[1] == 'NNS':# plural noun
		#	print i[0]
		#	nns.append(i[0])
		if i[1] == 'WDT':
			ques = i[0]
			#print s2[c][0]
	
	if 'bowled' in verb:
		inn.append('bowl')
	else:
		inn.append('bat')
			


def main():
	
	
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

	#lim = 0;
	"""for p,q in dictionary.iteritems():
		if lim < 20:
			print q
			lim += 1;
	"""	

	ipf = ' dataset/player_profile/indian_players_profile.txt'
	npf = ' dataset/player_profile/nz_players_profile.txt'
	add_to_dict1( Ipf, ipf);
	add_to_dict1( Npf, npf);

	#print "\n/*********************************************************************************************************************************************/\n\nWelcome To Question Answering System!\nPlease enter Query and press enter\nTo Exit PRESS Q\n\n/*********************************************************************************************************************************************/\n"
	global m
	#k = 1;
	
	#while k == 1:
	query = raw_input("Pls enter the query:\n");
	if query == 'q' or query == 'Q':
		return			
	makeTokens(query);

	#now see which file to open
	#first find m#, then find inn
	mn = 0

	if matchNum[0] == 'first':
		mn = 1
	elif matchNum[0] == 'second':
		mn = 2
	elif matchNum[0] == 'third':
		mn = 3
	elif matchNum[0] == 'fourth':
		mn = 4
	elif matchNum[0] == 'fifth':
		mn = 5

	if mn == 0:
		m = mcn[0]
	else:
		m = mn
	if m == 4:
		m4 = True
	

	#print inn
	if name:
		if inn[0] == 'bowl':
			if team[0] == 'India':
				fname = 'InnN'
			else:
				fname = 'InnI'
		else:
			if team[0] == 'India':
				fname = 'InnI'
			else:
				fname = 'InnN'

	
	#decide to open which file
	if name:
		with open(' dataset/com_M'+str(m)+'_'+str(fname),'rU') as fin:       
			for line in fin:                  # for each line of the file
				line=line.strip()             # remove CR/LF
				if line:                      # skip blank lines
				    data.append(line)
	else:
		commentary.append(' dataset/com_M'+str(m))
		with open(' dataset/com_M'+str(m)+'_InnI','rU') as fin:       
			for line in fin:                  # for each line of the file
				line=line.strip()             # remove CR/LF
				if line:                      # skip blank lines
				    data.append(line)
		with open(' dataset/com_M'+str(m)+'_InnN','rU') as fin:       
			for line in fin:                  # for each line of the file
				line=line.strip()             # remove CR/LF
				if line:                      # skip blank lines
				    data1.append(line)

	c = 0;
	for line in data:
		c += 1;
		temp = line[:]
		temp = temp.split(',')
		if isfloat(str(temp[0])):
			a = temp[0]
			b = data[c]
			if a not in dictionary:
				dictionary[a] = b
	c = 0;
	for line in data1:
		c += 1;
		temp = line[:]
		temp = temp.split(',')
		if isfloat(str(temp[0])):
			a = temp[0]
			b = data1[c]
			if a not in dictionary1:
				dictionary1[a] = b
	
	
	solve(query)
	

if __name__ == "__main__":
	main()
