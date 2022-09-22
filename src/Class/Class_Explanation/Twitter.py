users = [
    {'Name': 'Hadiza',
     'Age': 21,
     'Gender': 'Female',
     'Username': 'deezah',
     'is_verified': True,
     'Tweets': [
         {'Content': 'PO for President', 'Likes': 450, 'Retweets': 233},
         {'Content': 'Atiku for President', 'Likes': 4, 'Retweets': 2},
     ]
     },

    {'Name': 'Ibrahim',
     'Age': 32,
     'Gender': 'Male',
     'Username': 'ibro',
     'is_verified': False,
     'Tweets': [
         {'Content': 'Programming is fun', 'Likes': 34, 'Retweets': 12},
     ]
     },

    {'Name': 'James',
     'Age': 25,
     'Gender': 'Male',
     'Username': 'amez',
     'is_verified': True,
     'Tweets': [
         {'Content': 'Love is life', 'Likes': 66, 'Retweets': 89},
         {'Content': 'Only Rachael I know', 'Likes': 97, 'Retweets': 21},
     ]
     },

    {'Name': 'Rachael',
     'Age': 21,
     'Gender': 'Female',
     'Username': 'betty',
     'is_verified': False,
     'Tweets': [
         {'Content': '.', 'Likes': 1450, 'Retweets': 2330},
         {'Content': 'Amezing grace', 'Likes': 2000, 'Retweets': 1542},
     ]
     },

    {'Name': 'Elijah',
     'Age': 17,
     'Gender': 'Male',
     'Username': 'el_d_si',
     'is_verified': False,
     'Tweets': [
         {'Content': '#Osun decides', 'Likes': 450, 'Retweets': 233},
     ]
     },

    {'Name': 'Doris',
     'Age': 16,
     'Gender': 'Female',
     'Username': 'anything',
     'is_verified': False,
     'Tweets': [
         {'Content': 'I love Chimamanda Adichie', 'Likes': 450, 'Retweets': 233},
         {'Content': 'Feminism is the goal', 'Likes': 4000, 'Retweets': 2450},
     ]
     },

    {'Name': 'Jacob',
     'Age': 37,
     'Gender': 'Male',
     'Username': 'elder_j',
     'is_verified': True,
     'Tweets': [
         {'Content': 'Reflection ismy goal', 'Likes': 5, 'Retweets': 3},
         {'Content': 'How to get more likes on twitter', 'Likes': 1, 'Retweets': 1},
     ]
     },

    {'Name': 'Derrick',
     'Age': 29,
     'Gender': 'Male',
     'Username': 'standby_gen',
     'is_verified': False,
     'Tweets': [
     ]
     },

    {'Name': 'Mubarak',
     'Age': 47,
     'Gender': 'Male',
     'Username': 'whistle',
     'is_verified': True,
     'Tweets': [
         {'Content': 'PO for President', 'Likes': 450, 'Retweets': 233},
         {'Content': 'Atiku for President', 'Likes': 4, 'Retweets': 2},
     ]
     }
]

no_of_users = (len(users))
usernames = {user['Username'] for user in users}
female_users = [user['Name'] for user in users if user['Gender'] == 'Female']
inactive_users = [user for user in users if len(user['Tweets']) == 0]
number_of_inactive_users = len([user for user in users if len(user['Tweets']) == 0])
name_age_of_users = [{'Name': user['Name'], 'Age': user['Age']} for user in users]
avg_age_of_users = round(sum(user['Age'] for user in users) / len(users))

print(no_of_users)
print(usernames)
print(female_users)
print(inactive_users)
print(name_age_of_users)
print(avg_age_of_users)

print(max(users, key=lambda x: x['Age']))
print(max(users, key=lambda x: len(x['Tweets'])))
# print(max(users, key = lambda x: x[['Likes']]))

print(max([user['Age'] for user in users]))
print(sum([user['Age'] for user in users]) / len(users))

print(any(user['is_verified'] for user in users))
print(all(user['is_verified'] for user in users))
# print(any(user['Gender' : 'Female'] for user in users))~

