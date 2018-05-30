#Adwords Python Script Written by Simerdeep Singh Jolly (unityid :- sjolly)
import sys
import csv
import math
from random import shuffle
import random
#Adwords.py

#Finds Advertisers matching the keyword
def FindAdvertisers(query,bidders):
	advertisers = [i for i in bidders if i[1] == query]
	return advertisers

#Finds Advertisers having budget available to bid
def FindAdvertisersWithBudgets(advertisers,budget):
	advertisersWithBudget = []
	for i in advertisers:
		#print budget[i[0]]
		#print float(i[2])
		if budget[i[0]] >= float(i[2]):
			advertisersWithBudget.append(i)
	return advertisersWithBudget

#Greedy Selection Algorithm
def GreedySelection(advertisersWithBudget):
	m = max(i[2] for i in advertisersWithBudget)
	selected = [i for i in advertisersWithBudget if i[2] == m]
	return selected	[0]	

#Msvv Selection Algorithm	
def MSVVSelection(advertisersWithBudget,budget,initialBudget):
	max = 0.0
	selected = []
	for i in advertisersWithBudget:
		xu = (initialBudget[i[0]]-budget[i[0]])/initialBudget[i[0]]
		#print xu
		func = 1 - math.exp(xu-1)
		#print func
		#print (float(i[2]) * func)
		if (float(i[2]) * func) > max:
			max = (float(i[2]) * func)
			selected = i
	return selected
	
#
def BalanceSelection(advertisersWithBudget,budget):
	max = 0
	for i in advertisersWithBudget:
		if budget[i[0]] > max:
			max = budget[i[0]]
			selected = i
	return selected

#load the bidders and queries


#choice = raw_input("Approach = ")
def main(argv):
	choice = str(argv)
	cDict = {"greedy":1,"msvv":2,"balance":3}
	algoNum = cDict.get(choice)
	#print algoNum

	if not algoNum:
		print "Wrong Choice"
	else:
		#load Datasets from file
		#Queries
		queries = []
		fQueries = open("queries.txt")
		for i in fQueries:
			queries.append(i.replace("\n",""))
		
		#data Bidders
		bidders = []
		fBidders = open("bidder_dataset.csv")
		try:
			reader = csv.reader(fBidders)  
			for row in reader:   
				bidders.append(row)    
		finally:
			fBidders.close()     

		#Dictionary to store mapping of advertisers against budgets
		budget = {}
		for i in bidders[1:]:
			if(i[3]):
				budget[i[0]] = float(i[3])
		initialBudget = budget.copy()
		#print budget
		
		optimalSum = sum(budget.values())
		# Finds the total revenue using the algorithm
		revenue = 0.0
		for q in queries:
			advertisers = FindAdvertisers(q,bidders)
			advertisersWithBudget = FindAdvertisersWithBudgets(advertisers,budget)
			if len(advertisersWithBudget) >= 1:
				if algoNum == 1:#Greedy
					selectedBidder = GreedySelection(advertisersWithBudget)
				elif algoNum == 2:#MSVV
					selectedBidder = MSVVSelection(advertisersWithBudget,budget,initialBudget)
				else:#Balance
					selectedBidder = BalanceSelection(advertisersWithBudget,budget)
				revenue = revenue + float(selectedBidder[2])
				budget[selectedBidder[0]] = budget[selectedBidder[0]] - float(selectedBidder[2])
		print "Revenue:" + str(revenue)

		#Competitive Ratio:
		revenueList = []
		random.seed(0)
		#print optimalSum
		for i in range(0,100):
			revenue = 0.0
			shuf = shuffle(queries)
			budget = initialBudget.copy()
			for q in queries:
				advertisers = FindAdvertisers(q,bidders)
				advertisersWithBudget = FindAdvertisersWithBudgets(advertisers,budget)
				if len(advertisersWithBudget) >= 1:
					if algoNum == 1:#Greedy
						selectedBidder = GreedySelection(advertisersWithBudget)
					elif algoNum == 2:#MSVV
						selectedBidder = MSVVSelection(advertisersWithBudget,budget,initialBudget)
					else:#Balance
						selectedBidder = BalanceSelection(advertisersWithBudget,budget)
					revenue = revenue + float(selectedBidder[2])
					budget[selectedBidder[0]] = budget[selectedBidder[0]] - float(selectedBidder[2])
			#print revenue
			revenueList.append(revenue)
		print "Competitive Ratio:" + str(reduce(lambda x, y: x + y, revenueList) / (len(revenueList)*optimalSum))

if __name__ == "__main__":
	if(len(sys.argv) == 2):  
		main(sys.argv[1])
	else :
		print "Invalid no. of arguments"









