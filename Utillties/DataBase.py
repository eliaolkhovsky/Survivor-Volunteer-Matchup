import json

# consts
SURVIVOR = "survivor"
VOLUNTEER = "volunteer"
MALE = "m"
FEMALE = "f"

# database files
USERS_DIRECTORY = "Users\\"
POSTS_DIRECTORY = "Posts\\"

USERS_FILE = USERS_DIRECTORY + "users.json"
POSTS_FILE = POSTS_DIRECTORY + "posts.json"

GROCERIES = "groceries"
MED = "medical"
TECH = "technical"
MENTAL = "mental"
TREMP = "driving"
TYPES_OF_PROBLEMS = [GROCERIES, MED, TECH, MENTAL, TREMP]

# Example Users
'''
user = {"first_name": "",
        "user_name": "",
        "password": "",
        "last_name": "",
        "id": "",
        "Gender": "",
        "Location": "",
        "Age": 0,
        "profile": "",
        "Skills": [],
        "matched": []
        }

post = {"user": user,
        "hours": "",
        "complaint": "",
        "title": "",
        "type of problem": "",
        "need professional": "",
        }
'''

BOB = {"first_name": "Bob",
       "last_name": "boblovsky",
       "username": "bobthesexy",
       "password": "AADFBGHtbjkwrhjhjhvf64356454@@@#$%",
       "id": "328273784",
       "Gender": MALE,
       "Location": "0213.11325,565.89786",
       "Age": 57,
       "profile": SURVIVOR,
       "Skills": [],
       "matched": []
       }
LINA = {"first_name": "Alina",
        "last_name": "Segal",
        "username": "linathewristcutter",
        "password": "sujmnf6ygtr6666A@",
        "id": "21656548",
        "Gender": FEMALE,
        "Location": "2165.18548,84654.8489",
        "Age": 45,
        "profile": SURVIVOR,
        "Skills": [],
        "matched": []
        }
DAN = {"first_name": "Dan",
       "last_name": "Hefetz",
       "username": "danik",
       "password": "A@dasdw5465",
       "id": "146165454",
       "Gender": MALE,
       "Location": "216165.45487,132154.4554",
       "Age": 19,
       "profile": VOLUNTEER,
       "Skills": [TECH],
       "matched": [LINA]
       }

BOB_POST = {"user": BOB,
            "hours": (1200, 1600),
            "complaint": "I don't remember if she's dead and it's all dementia again but "
                         "I swear I saw her cheating on me!",
            "title": "My wife is a bitch",
            "type of problem": MENTAL,
            "need professional": True,
            }

# variables
posts = [BOB_POST]
users = [BOB, LINA, DAN]
current_user = DAN


def save_users():
    with open(USERS_FILE, "w") as usersData:
        json.dump(users, usersData)


def load_users():
    global users
    with open(USERS_FILE, "r") as userData:
        db = json.load(userData)
    users = db


def save_posts():
    with open(POSTS_FILE, "w") as postData:
        json.dump(posts, postData)


def load_posts():
    global posts
    with open(POSTS_FILE, "r") as postData:
        db = json.load(postData)
    posts = db
