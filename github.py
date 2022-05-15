import os
import subprocess
from datetime import datetime, timedelta

# Calculate date range from a year ago to today
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# Function to create a new file and commit it
def make_commit(date):
    filename = f"commit_file_{date.strftime('%Y%m%d')}.txt"
    
    # Create a new file
    with open(filename, "w") as file:
        file.write(f"This is a commit for {date.strftime('%Y-%m-%d')}")

    # Add the file
    subprocess.run(["git", "add", filename])

    # Commit with a custom date
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date.strftime("%Y-%m-%dT%H:%M:%S")
    subprocess.run(["git", "commit", "-m", f"Commit for {date.strftime('%Y-%m-%d')}"], env=env)

# Make a commit for each day
date = start_date
while date < end_date:
    make_commit(date)
    date += timedelta(days=1)

# Push the commits
subprocess.run(["git", "push"])
