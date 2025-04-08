from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        team = {"_id": ObjectId(), "name": "Blue Team", "members": [user["_id"] for user in users]}
        db.teams.insert_one(team)

        activities = [
            {"_id": ObjectId(), "user_id": users[0]["_id"], "activity_type": "Cycling", "duration": 60},
            {"_id": ObjectId(), "user_id": users[1]["_id"], "activity_type": "Crossfit", "duration": 120},
            {"_id": ObjectId(), "user_id": users[2]["_id"], "activity_type": "Running", "duration": 90},
            {"_id": ObjectId(), "user_id": users[3]["_id"], "activity_type": "Strength", "duration": 30},
            {"_id": ObjectId(), "user_id": users[4]["_id"], "activity_type": "Swimming", "duration": 75},
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {"_id": ObjectId(), "user_id": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user_id": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user_id": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "user_id": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "user_id": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
