import geographics
import DataBase
import pyttsx3

# variables
post = None


def filter_posts_by_location(dt, location):
    return sorted(dt, key=lambda post: geographics.get_distance(post['user']['Location'], location))


def filter_posts_by_problem(posts, problem_type):
    return [post for post in posts if post["type of problem"] == problem_type]


def filter_posts_by_age(posts, age):
    return [post for post in posts if post["user"]["Age"] == age]


def filter_posts_by_gender(posts, gender):
    return [post for post in posts if post["user"]["gender"] == gender]


def filter_posts_by_hours(posts, hours):
    return [post for post in posts if post["hours"] == hours]


def filter_posts_need_pro(posts):
    return [post for post in posts if post["need professional"]]


def create_empty_post():
    global post
    post = dict()


def add_title(post, title):
    post["title"] = title


def add_hours(post, hours):
    post["hours"] = hours


def add_complaint(post, complaint):
    post["complaint"] = complaint


def add_user(post, user):
    post["user"] = user


def add_type_of_problem(post, type_of_problem):
    post["type of problem"] = type_of_problem


def add_need_professional(post, need_professional):
    post["need professional"] = need_professional


def submit_post(post):
    if len(post) != len(DataBase.BOB_POST):
        return
    for keys in post:
        if post[keys] is None:
            return
    DataBase.posts.append(post)


def txt_to_speech(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()
