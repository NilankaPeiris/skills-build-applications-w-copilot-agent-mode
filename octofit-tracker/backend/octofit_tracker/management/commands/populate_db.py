from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from bson import ObjectId
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User.objects.create(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User.objects.create(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User.objects.create(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User.objects.create(_id=ObjectId(), username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
            User.objects.create(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]

        # Create teams
        blue_team = Team.objects.create(_id=ObjectId(), name='Blue Team')
        gold_team = Team.objects.create(_id=ObjectId(), name='Gold Team')
        blue_team.members.add(users[0], users[1], users[2])
        gold_team.members.add(users[3], users[4])

        # Create activities
        activities = [
            Activity.objects.create(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity.objects.create(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity.objects.create(_id=ObjectId(), user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity.objects.create(_id=ObjectId(), user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity.objects.create(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard.objects.create(_id=ObjectId(), user=users[0], score=100),
            Leaderboard.objects.create(_id=ObjectId(), user=users[1], score=90),
            Leaderboard.objects.create(_id=ObjectId(), user=users[2], score=95),
            Leaderboard.objects.create(_id=ObjectId(), user=users[3], score=85),
            Leaderboard.objects.create(_id=ObjectId(), user=users[4], score=80),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout.objects.create(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout.objects.create(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout.objects.create(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout.objects.create(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
