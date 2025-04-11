from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Insert sample users
        db.users.insert_many([
            {"email": "john.doe@example.com", "name": "John Doe", "age": 25},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30}
        ])

        # Insert sample teams
        db.teams.insert_many([
            {"name": "Team Alpha", "members": ["John Doe", "Jane Smith"]}
        ])

        # Insert sample activities
        db.activity.insert_many([
            {"user": "John Doe", "activity_type": "Running", "duration": 30},
            {"user": "Jane Smith", "activity_type": "Cycling", "duration": 45}
        ])

        # Insert sample leaderboard entries
        db.leaderboard.insert_many([
            {"user": "John Doe", "score": 100},
            {"user": "Jane Smith", "score": 150}
        ])

        # Insert sample workouts
        db.workouts.insert_many([
            {"name": "Push-ups", "description": "Do 20 push-ups"},
            {"name": "Sit-ups", "description": "Do 30 sit-ups"}
        ])

        self.stdout.write(self.style.SUCCESS('Database populated with sample data using pymongo.'))
#