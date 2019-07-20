# -*- coding: utf-8 -*-
"""
@author: SIMRAN SAHA
Confirmation regarding model working better than a random selection of accounts
or not

The following is a simple test that was done over a period of a single day.
5 accounts each were followed via 2 methods: one using a set of RULES
and second, 'randomly'. At the end of the 1 DAY period, 1 account that was
followed randomly followed-back against 0 accounts chosen using the rules.

Using a short 1 day period  to perform this test may or may not have yielded 
the correct result but below is a short demonstration on how this can be 
performed over a longer period and greater no. of accounts and obtain
more reliable results.
"""

#importing necessary library to access the twitter API and setting up a
#connection
import tweepy
consumer_key = 'tHaeI3Vfg3B5BxDdAEnmb5qHp'
consumer_secret = 'bazSR24b793Th2lByeyc7bA319ZTWnx7CvwMVzVzhuCERQbjTn'

access_token = '1140113387952586752-JUA8pQaeQp6z6inciK8TjuqsxwwxL1'
access_token_secret = 'i4stpoFuZJQNMY8xiM9FNpyT02j70lSyiJhL0yChjG7Jd'

auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Using a popular twitter user to get access to a pool of followers
users = api.followers_ids('gdb')

#user-defined functions to save IDs of followed users
def save_id1(ID):
    f1=open('output2.txt', 'a')
    f1.write(str(ID) + "\r\n")

def save_id2(ID):
    f1=open('output3.txt', 'a')
    f1.write(str(ID) + "\r\n")
    
#PART 1: Using pre-defined principles to select an account to follow based on
#mutual interests, no. of friends, activity on twitter etc
#(CHECK FILE data_scraping.ipynb FOR MORE DETAILS ON CODE BETWEEN LINE. NO
#38 AND 73)

interests = ['machine', 'learning', 'computer', 'science', 'programming', 'AI', 
             'artificial', 'intelligence', 'deep', 'nlp', 'processing', 'data', 
             'cs', 'statistics', 'statistic', 'maths', 'mathematics', 'scientist',
             'programmer', 'computing']

c = 0
for k in users[0:70]:
    try:
        follower1 = api.get_user(id = k)
        is_protected1 = follower1.protected
        status_count1 = follower1.statuses_count
        
        if not is_protected1 and status_count1:
            follower_bio = follower1.description.lower()
            follower_favourites_count = follower1.favourites_count
            follower_friends_count = follower1.friends_count
            dlast_status = follower1.status.created_at
            last_status = dlast_status.strftime('%m-%d-%Y')   
            if (last_status > '04-01-2019'):
                is_active = 1
            else:
                is_active = 0
                
            if any(interest in follower_bio for interest in interests) \
                            and follower_favourites_count > 20 \
                            and follower_friends_count > 100:
                                print ('case is working')
                                api.create_friendship(id = follower1.id)
                                print ('doing friendhsip....')
                                save_id1(follower1.id)
                                c = c+1
            if c == 5:
                break
    except tweepy.TweepError as ec:
        print (ec)
        continue 
    
#PART 2: Making a random selection of accounts from the same 0:70 range as 
#in PART 1 and following them
        
#function get_list() takes a text file and returns line-by-line converted from
#string to integer.
def get_list (fname):
    with open(fname) as f:    
        content_list = f.readlines()
        #print(content_list)
    
    content_list = [x.strip() for x in content_list]
    list1 = content_list[::2]
    for i in range(0, len(list1)): 
        list1[i] = int(list1[i])
    return list1

#output2.txt and list content contains list of users followed based on MODEL-RULES
content = get_list('output2.txt')
print(content)

import random
c1 = 5
while (c1):
    try:
        random_user = random.choice(users[0:70])
        #print (random_user)
        #print (type(random_user))
        if random_user in content:
            c1 = c1+1
            continue
        api.create_friendship(id = random_user)
        print ('doing friendship....')
        save_id2(random_user)
    except tweepy.TweepError as e:
        print (e)
        continue
    c1 = c1-1

#output3.txt and list list2 contains list of users followed RANDOMLY
list2 = get_list('output3.txt')
print(list2)
  
#checking count of people following back in each case after 1 DAY
c_mod = 0
c_rand = 0
followers = api.followers_ids()
for i in content:
    if i in followers:
        c_mod = c_mod + 1
for i in list2:
    if i in followers:
        c_rand = c_rand + 1

print ('Count of follow-backs from people chosen via rules: ', c_mod)
print ('Count of follow-backs from people chosen randomly: ',c_rand) 

'''following output was recieved:
    
    Count of follow-backs from people chosen via rules:  0
    Count of follow-backs from people chosen randomly:  1
'''