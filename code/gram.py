"""
Name: S Swetha

Sub: Artificial Intelligence

Project II

Phase II

"""

import nltk	
import sys
from collections import Counter

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
verb = [];
nns = [];
matchNum = [];
inn = [];
team = [];

#
# function to add the contents of file, after proper parsing, to the given dictionary
def add_to_dict(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		#b = temp[1:]
		if a not in dictionary:
			dictionary.append(a);


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
	if query.find('hit') >= 0:
		#print 'bat kiya'	
		if query.find('four') >= 0: #and query.find('fourth') < 0:
			score = 1;

		elif query.find('six') >= 0:
			score = 2;

		elif query.find('one') >= 0:
			score = 3;
	
		elif query.find('two') >= 0:
			score = 4;

		if query.find('bowler') >= 0:
			bowler = True

		if query.find('overs') >= 0:
			ov = True
		if query.find('over') >= 0 and query.find('overs') < 0:
			ov = False

		if query.find('ball') >= 0:
			b = True

		temp = query.split(',');
		#print temp
		for i in temp:
			if 'over' in i:
				t = i.split()
				for j in t:
					if isfloat(j):
						num = True
						#find over
						onum = j
			if 'six' in i or 'four' in i or 'one' in i or 'two' in i:
				#print 'in'
				t = i.split()
				#print t
				for j in t:
					if isfloat(j):
						#num = True
						#find over
						Runnum = j
						print Runnum
			
			
	#print score,bowler,ov,num
	#print name[0]	
		for p,q in dictionary.iteritems():
			#print p,q
			#print name[0] in q
			if score == 1 and 'FOUR' in q and name[0] in q :
				over = p
				rec[p] = q
				#print p
			if score == 2 and 'SIX' in q and name[0] in q:
				over = p
				rec[p] = q
				#print p
			if score == 3 and '1 run' in q and name[0] in q :
				over = p
				rec[p] = q
			if score == 4 and '2 runs' in q and name[0] in q :
				over = p
				rec[p] = q


		if bowler:
			for p,q in rec.iteritems():
				t = q.split()
				for i in t:
					if i != 'to':
						print i,
					else:
						break
		#print query.find('which ball')				
		if num and query.find('which ball') >= 0:
			#print 'came', rec 
			for i in rec.keys():
				t = i.split('.')
				#print int(t[0]),int(onum)
				if int(t[0]) == int(onum):
					#print 'y'
					print t[1];
		elif not num :
			for p,q in rec.iteritems():
				print p

		if Runnum :
			count = Runnum
			for p,q in rec.iteritems():
				count -= 1;
				if not count:	
					print 'Yes!' 



	
	# dismissal for all questions
	elif query.find('out') >= 0:
		for p,q in dictionary.iteritems():
			#print 'OUT' in q
			if name[0] in q and 'OUT' in q:
				rec[p] = q
		for p in rec.keys():
			last = p
		if query.find('which over') >= 0:
			for p in rec.keys():
				print last.split('.')[0]
				
		
		elif query.find('which ball') >= 0:
				print int((last.split('.')[1])) 
				

		if query.find('which bowler') >= 0 or query.find('dismissed by whom') >= 0:
			#for p,q in rec.iteritems():
			t = dictionary[last].split()
			for i in t:
				if i != 'to':
					print i,
				else:
					break
		print ''
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
	
	temp = temp.split(',')
	#total
	
	total = nltk.word_tokenize(query)
	stag = nltk.pos_tag(total)
	#first part grammar
	text = nltk.word_tokenize(temp[0])
	s = nltk.pos_tag(text)
	if s[1][1] == 'JJ':
		matchNum.append(s[1][0])
	elif s[2][1] == 'JJ':
		matchNum.append(s[2][0])
	#print matchNum

	#second part grammar
	text2 = nltk.word_tokenize(temp[1])
	s2 = nltk.pos_tag(text2)
	name.append(s2[0][0])#found name so find team!!

	if name[0] in Ipf:
		team.append('India')
	else:
		team.append('New Zealand')
	
	#print 'team hai:'+str(team)
	c = 0;
	#get the verb VBD
	for i in s2:
		c += 1;
		if i[1] == 'VBD':
			verb.append(i[0])  
			#print i[0] #is verb
			nns.append(s2[c][0]);
			#print s2[c][0]

		#if i[1] == 'NNS':# plural noun
		#	print i[0]
		#	nns.append(i[0])
		if i[1] == 'WDT':
			ques = i[0]
			#print s2[c][0]
	
	if 'bowled' in verb:
		#print "mil gaya"
		inn.append('bowl')
	else:
		inn.append('bat')
			
	#print stag


def main():
	
	#lim = 0;
	"""for p,q in dictionary.iteritems():
		if lim < 20:
			print q
			lim += 1;
	"""	

	ipf = ' dataset/player_profile/indian_players_profile.txt'
	npf = ' dataset/player_profile/nz_players_profile.txt'
	add_to_dict( Ipf, ipf);
	add_to_dict( Npf, npf);

	print "\n/*********************************************************************************************************************************************/\n\nWelcome To Question Answering System!\nPlease enter Query and press enter\nTo Exit PRESS Q\n\n/*********************************************************************************************************************************************/\n"
	k = 1;
	
	while k == 1:
		query = raw_input("Pls enter the query:\n");
		if query == 'q' or query == 'Q':
			return			
		makeTokens(query);

		#now see which file to open
		#first find m#, then find inn
	
		if matchNum[0] == 'first':
			mn = 1
		if matchNum[0] == 'second':
			mn = 2
		if matchNum[0] == 'third':
			mn = 3
		if matchNum[0] == 'fourth':
			mn = 4
		if matchNum[0] == 'fifth':
			mn = 5

	
		#print inn
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
		#print 'com_M'+str(mn)+'_'+str(fname)
		with open(' dataset/com_M'+str(mn)+'_'+str(fname),'rU') as fin:       
			for line in fin:                  # for each line of the file
				line=line.strip()             # remove CR/LF
				if line:                      # skip blank lines
				    data.append(line)

	
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

		Q = query.split(',');
		c = 0
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
	

if __name__ == "__main__":
	main()
