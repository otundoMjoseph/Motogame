import sqlite3

class Player:
    @staticmethod
    def create(name):
        conn = sqlite3.connect('motogame.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO player (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(player_id):
        conn = sqlite3.connect('motogame.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM player WHERE id = ?", (player_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('motogame.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM player")
        players = cursor.fetchall()
        conn.close()
        return players

    @staticmethod
    def find_by_id(player_id):
        conn = sqlite3.connect('motogame.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM player WHERE id = ?", (player_id,))
        player = cursor.fetchone()
        conn.close()
        return player

class Vehicle:
    @staticmethod
    def create(name, player_id):
        conn = sqlite3.connect('motogame.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO vehicle (name, player_id) VALUES (?, ?)", (name, player_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(vehicle_id):
        conn = sqlite3.connect('motogame.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM vehicle WHERE id = ?", (vehicle_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('motogame.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vehicle")
        vehicles = cursor.fetchall()
        conn.close()
        return vehicles

    @staticmethod
    def find_by_id(vehicle_id):
        conn = sqlite3.connect('motogame.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vehicle WHERE id = ?", (vehicle_id,))
        vehicle = cursor.fetchone()
        conn.close()
        return vehicle

    @staticmethod
    def find_by_player_id(player_id):
        conn = sqlite3.connect('motogame.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vehicle WHERE player_id = ?", (player_id,))
        vehicles = cursor.fetchall()
        conn.close()
        return vehicles
