import sys
from db import init_db
from cli import cli
from game import start_game

def main():
    if '--init-db' in sys.argv:
        init_db()
        print("Database initialized.")
    elif '--cli' in sys.argv:
        cli()
    else:
        start_game()

if __name__ == "__main__":
    main()
