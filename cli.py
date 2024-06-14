from models import Player, Vehicle

def display_menu():
    print("1. Create Player")
    print("2. Delete Player")
    print("3. Display All Players")
    print("4. Find Player by ID")
    print("5. Create Vehicle")
    print("6. Delete Vehicle")
    print("7. Display All Vehicles")
    print("8. Find Vehicle by ID")
    print("9. View Vehicles by Player ID")
    print("0. Exit")

def cli():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter player name: ")
            Player.create(name)
            print(f"Player '{name}' created.")
        elif choice == '2':
            player_id = input("Enter player ID: ")
            if Player.delete(player_id):
                print(f"Player with ID '{player_id}' deleted.")
            else:
                print(f"No player found with ID '{player_id}'.")
        elif choice == '3':
            players = Player.get_all()
            if players:
                for player in players:
                    print(f"ID: {player[0]}, Name: {player[1]}")
            else:
                print("No players found.")
        elif choice == '4':
            player_id = input("Enter player ID: ")
            player = Player.find_by_id(player_id)
            if player:
                print(f"ID: {player[0]}, Name: {player[1]}")
            else:
                print(f"No player found with ID '{player_id}'.")
        elif choice == '5':
            name = input("Enter vehicle name: ")
            player_id = input("Enter player ID: ")
            if Player.find_by_id(player_id):
                Vehicle.create(name, player_id)
                print(f"Vehicle '{name}' created for player ID '{player_id}'.")
            else:
                print(f"No player found with ID '{player_id}'.")
        elif choice == '6':
            vehicle_id = input("Enter vehicle ID: ")
            if Vehicle.delete(vehicle_id):
                print(f"Vehicle with ID '{vehicle_id}' deleted.")
            else:
                print(f"No vehicle found with ID '{vehicle_id}'.")
        elif choice == '7':
            vehicles = Vehicle.get_all()
            if vehicles:
                for vehicle in vehicles:
                    print(f"ID: {vehicle[0]}, Name: {vehicle[1]}, Player ID: {vehicle[2]}")
            else:
                print("No vehicles found.")
        elif choice == '8':
            vehicle_id = input("Enter vehicle ID: ")
            vehicle = Vehicle.find_by_id(vehicle_id)
            if vehicle:
                print(f"ID: {vehicle[0]}, Name: {vehicle[1]}, Player ID: {vehicle[2]}")
            else:
                print(f"No vehicle found with ID '{vehicle_id}'.")
        elif choice == '9':
            player_id = input("Enter player ID: ")
            vehicles = Vehicle.find_by_player_id(player_id)
            if vehicles:
                for vehicle in vehicles:
                    print(f"ID: {vehicle[0]}, Name: {vehicle[1]}, Player ID: {vehicle[2]}")
            else:
                print(f"No vehicles found for player ID '{player_id}'.")
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli()
