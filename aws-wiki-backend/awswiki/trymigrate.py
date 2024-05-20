# trymigrate.py


import subprocess
import time

def check_migration():
    while True:
        try:
            subprocess.run(["python", "manage.py", "migrate"], check=True)
            print("Migration completed successfully!")
            break 
        except subprocess.CalledProcessError as e:
            print("Migration failed:", e)
            print("Retrying in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    check_migration()
