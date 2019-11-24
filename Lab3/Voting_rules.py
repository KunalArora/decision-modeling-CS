#!/usr/bin/env python
# coding: utf-8

# In[25]:


import operator
import csv

# helpers
def VoteCounter(preferences):
    counts_dict = {}
    for preference in preferences:
        try:
            counts_dict[preference[0]] += 1
        except KeyError:
            counts_dict[preference[0]] = 1
    return counts_dict


def PreferenceCounter(a, b, preferences):
    a_pref = 0
    b_pref = 0
    for preference in preferences:
        if preference.index(a) < preference.index(b):
            a_pref += 1
        else:
            b_pref += 1
    return a_pref, b_pref

# voting rules
def MajorityRule(preferences):
    votes = VoteCounter(preferences)
    num_voters = len(preferences)
    for candidate, count in votes.items():
        if count > 0.5*num_voters:
            return candidate
    return None

def Plurality(preferences):
    votes = VoteCounter(preferences)
    num_voters = len(preferences)
    max_votes = max(votes.values())
    winners = []
    for candidate, count in votes.items():
        if count == max_votes:
            return candidate
    return None

def PluralityRunoff(preferences):
    votes = VoteCounter(preferences)
    num_voters = len(preferences)
    max_votes = max(votes.values())
    
    if max_votes > 0.5*num_voters:
        return [x for x, count in votes.items() if count==max_votes]

    top2 = [x for x, count in sorted(votes.items(), key=lambda x: x[1], reverse=True)][:2]
    # print(top2)
    a_pref, b_pref = PreferenceCounter(top2[0], top2[1], preferences)
    if a_pref > b_pref:
        return top2[0]
    return top2[1]

def CondorcetVoting(preferences):
    candidates = sorted(preferences[0])
    for candidate1 in candidates:
        condorcet = True
        for candidate2 in candidates:
            if candidate1==candidate2:
                continue
            a_pref, b_pref = PreferenceCounter(candidate1, candidate2, preferences)
            if a_pref < b_pref:
                condorcet = False
                break
        if condorcet:
            return candidate1
    return None

def BordaVoting(preferences):
    borda_score = {candidate:0 for candidate in preferences[0]}
    for preference in preferences:
        for i, candidate in enumerate(preference):
            borda_score[candidate] += i+1
    
    return min(borda_score.items(), key=operator.itemgetter(1))[0]

if __name__ == "__main__":
    """
    5 voters : ['a', 'b', 'c', 'd']
    4 voters : ['a', 'c', 'b', 'd']
    2 voters : ['d', 'b', 'a', 'c']
    6 voters : ['d', 'b', 'c', 'a']
    8 voters : ['c', 'b', 'a', 'd']
    2 voters : ['d', 'c', 'b', 'a']
    """ 
    with open('preferences.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        preferences = list(list(rec) for rec in csv.reader(f, delimiter=','))


    print("MajorityRule :", MajorityRule(preferences))
    print("Plurality :", Plurality(preferences))
    print("PluralityRunoff :", PluralityRunoff(preferences))
    print("Condorcet :", CondorcetVoting(preferences))
    print("Borda :", BordaVoting(preferences))


# In[26]:





# In[7]:





# In[ ]:




