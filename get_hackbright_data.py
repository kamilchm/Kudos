#!flask/bin/python

import json
import urllib2

from flask.ext.sqlalchemy import SQLAlchemy 
from flask import session 

import app
from app.models import User, Post, UserTeam, Team

db = app.db

HACKBRIGHT_DATA_JSON_URL = "app/static/hackbright_users.txt"

def create_user(first_name, last_name, nickname, email, list_of_teams, mobile, photo, bio, username,twitter,facebook,github,linkedin):

    #When readding data - check to see if user already exists based on email. If yes, update columns, if no, insert new_user


    new_user=User(
        photo=photo,
        firstname=first_name,
        lastname=last_name,
        nickname=nickname,
        email=email, 
        phone=mobile,
        about_me=bio,
        username=username,
        twitter=twitter,
        facebook=facebook,
        github=github,
        linkedin=linkedin,
        )


    db.session.add(new_user) 
    db.session.commit()
    #need to commit first to get new_user.id
    
    user_id = new_user.id

    for team in list_of_teams:
        new_users_teams=UserTeam(
            user_id=user_id,
            team_id=team,
            )
        db.session.add(new_users_teams)
        db.session.commit()


def create_teams(all_teams):
    teams = all_teams.keys()
    for team in teams:
        new_team=Team(teamname=team)
        db.session.add(new_team)
        db.session.commit()

def main():
    raw_data = open(HACKBRIGHT_DATA_JSON_URL).read()
    print "got raw data: "
    print raw_data
    users = json.loads(raw_data)['users']
    #users = json.loads('{"users":[{"one":"baz", "two":null, "three":1.0, "four": 2}]}')
    print "got users: "
    print users

    print "Creating users with emails:",

    all_teams = {}
    for user in users:

        user_first_name = user['first_name']
        user_last_name = user['last_name']
        user_nickname = user['nickname']
        user_email = user['email']
        user_list_of_teams = user['teams']
        user_mobile_phone = user['mobile_phone']
        user_photo = user['picture']
        user_bio = user['bio']
        username = user['username']
        user_twitter = user['twitter']
        user_facebook = user['facebook']
        user_github = user['github']
        user_linkedin = user['linkedin']


        for team in user_list_of_teams:
            if team not in all_teams:
                all_teams[team] = 1

        create_user(
            user_first_name,
            user_last_name,
            user_nickname,
            user_email,
            user_list_of_teams,
            user_mobile_phone, 
            user_photo,
            user_bio,
            username,
            user_twitter,
            user_facebook,
            user_github,
            user_linkedin,
        )

    
    create_teams(all_teams)

    print "Done."

#add this so when it's imported, does not run. 
if __name__ == '__main__':
    main()
