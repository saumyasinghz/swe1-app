import os

# At the top with other imports
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Update ALLOWED_HOSTS
ALLOWED_HOSTS = [
    "djangotutorial-dev222.us-east-1.elasticbeanstalk.com",
    ".elasticbeanstalk.com",  # Allow all EB domains
]

# At the bottom, add static files configuration
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')