from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        try:
            print("Creating sample users...")
            user1 = User.objects.create(email="john.doe@example.com", name="John Doe", age=25)
            print(f"Created user: {user1}")
            user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", age=30)
            print(f"Created user: {user2}")

            print("Creating sample teams...")
            team1 = Team.objects.create(name="Team Alpha", members=["John Doe", "Jane Smith"])
            print(f"Created team: {team1}")

            print("Creating sample activities...")
            Activity.objects.create(user=user1, activity_type="Running", duration=30)
            print("Created activity for user1")
            Activity.objects.create(user=user2, activity_type="Cycling", duration=45)
            print("Created activity for user2")

            print("Creating sample leaderboard entries...")
            Leaderboard.objects.create(user=user1, score=100)
            print("Created leaderboard entry for user1")
            Leaderboard.objects.create(user=user2, score=150)
            print("Created leaderboard entry for user2")

            print("Creating sample workouts...")
            Workout.objects.create(name="Push-ups", description="Do 20 push-ups")
            print("Created workout: Push-ups")
            Workout.objects.create(name="Sit-ups", description="Do 30 sit-ups")
            print("Created workout: Sit-ups")

            self.stdout.write(self.style.SUCCESS('Database populated with sample data.'))
        except Exception as e:
            logger.error(f"Error populating database: {e}")
