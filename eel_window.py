import eel

from Utillties import DataBase, geographics
import pyttsx3

eel.init("web")


# Exposing the random_python function to javascript
@eel.expose
def is_eldery():
    global post
    return DataBase.current_user["profile"] == DataBase.SURVIVOR


def log_user():
    pass


# variables
post = None


@eel.expose
def filter_posts_by_location(dt, location):
    return sorted(dt, key=lambda post: geographics.get_distance(post['user']['Location'], location))


@eel.expose
def filter_posts_by_problem(posts, problem_type):
    return [p for p in posts if p["type of problem"] == problem_type]


@eel.expose
def filter_posts_by_age(posts, age):
    return [p for p in posts if p["user"]["Age"] == age]


@eel.expose
def filter_posts_by_gender(posts, gender):
    return [p for p in posts if p["user"]["gender"] == gender]


@eel.expose
def filter_posts_by_hours(posts, hours):
    return [p for p in posts if p["hours"] == hours]


@eel.expose
def filter_posts_need_pro(posts):
    return [p for p in posts if p["need professional"]]


@eel.expose
def create_empty_post():
    global post
    post = dict()


@eel.expose
def add_title(title):
    post["title"] = title


@eel.expose
def add_hours(hours):
    post["hours"] = hours


@eel.expose
def add_complaint(complaint):
    post["complaint"] = complaint


@eel.expose
def add_user(user):
    post["user"] = user


@eel.expose
def add_type_of_problem(type_of_problem):
    post["type of problem"] = type_of_problem


@eel.expose
def add_need_professional(need_professional):
    post["need professional"] = need_professional


@eel.expose
def submit_post():
    if len(post) != len(DataBase.BOB_POST):
        return
    for keys in post:
        if post[keys] is None:
            return
    DataBase.posts.append(post)


@eel.expose
def txt_to_speech(word):
    global post
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


# Start the index.html file
eel.start("index.html")
