# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:40:39 2024

@author: Paulr
"""

import sqlite3

ADD_CHOICE = 1
SHOW_CHOICE = 2
SEARCH_CHOICE = 3
MODIFY_CHOICE = 4
DELETE_CHOICE = 5
QUIT_CHOICE = 6

def main():
    create_db()
    
    choice = 0
    
    while choice != QUIT_CHOICE:
        display_menu()
        try:
            choice = int(input('Enter your choice: '))
            if choice == ADD_CHOICE:
                name = input('Enter player name: ')
                wins = int(input('Enter number of wins: '))
                losses = int(input('Enter number of losses: '))
                ties = int(input('Enter number of ties: '))
                add_player(name, wins, losses, ties)
                
            elif choice == SHOW_CHOICE:
                display_players()
            elif choice == SEARCH_CHOICE:
                name = input('Enter the name of the player to search: ')
                search(name)
            elif choice == MODIFY_CHOICE:
                name = input('Enter the name of the player to modify: ')
                modify(name)
            elif choice == DELETE_CHOICE:
                name = input('Enter the name of the player to delete: ')
                delete(name)
            elif choice == QUIT_CHOICE:
                print('Exiting the program...')
            else:
                print('Error: invalid selection.')
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    
def display_menu():
    print('\nPlayer Database Management App\n')
    print('  CHOICE MENU  ')
    print('1) Add a player')
    print('2) Show the list of players')
    print('3) Search for a player in the list')
    print('4) Modify a player')
    print('5) Delete a player from the list')    
    print('6) Quit')

def create_db():
    conn = sqlite3.connect('players_data.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Player (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            wins INTEGER NOT NULL,
            losses INTEGER NOT NULL,
            ties INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_player(name, wins, losses, ties):
    conn = sqlite3.connect('players_data.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Player (name, wins, losses, ties)
        VALUES (?, ?, ?, ?)
    ''', (name, wins, losses, ties))
    conn.commit()
    conn.close()

def display_players():
    conn = sqlite3.connect('players_data.db')
    cur = conn.cursor()
    cur.execute('''
        SELECT name, wins, losses, ties, (wins + losses + ties) as games
        FROM Player
        ORDER BY wins DESC
    ''')
    players = cur.fetchall()
    conn.close()
    for player in players:
        print(f'Name: {player[0]}, Wins: {player[1]}, Losses: {player[2]}, Ties: {player[3]}, Total Games: {player[4]}')

def search(name):
    conn = sqlite3.connect('players_data.db')
    cur = conn.cursor()
    cur.execute('''
        SELECT name, wins, losses, ties, (wins + losses + ties) as games
        FROM Player
        WHERE name = ?
    ''', (name,))
    player = cur.fetchone()
    conn.close()
    if player:
        print(f'Name: {player[0]}, Wins: {player[1]}, Losses: {player[2]}, Ties: {player[3]}, Total Games: {player[4]}')
    else:
        print('Player not found.')

def modify(name):
    conn = sqlite3.connect('players_data.db')
    cur = conn.cursor()
    cur.execute('''
        SELECT id
        FROM Player
        WHERE name = ?
    ''', (name,))
    player = cur.fetchone()
    if player:
        wins = int(input('Enter new number of wins: '))
        losses = int(input('Enter new number of losses: '))
        ties = int(input('Enter new number of ties: '))
        cur.execute('''
            UPDATE Player
            SET wins = ?, losses = ?, ties = ?
            WHERE id = ?
        ''', (wins, losses, ties, player[0]))
        conn.commit()
        print('Player updated.')
    else:
        print('Player not found.')
    conn.close()

def delete(name):
    conn = sqlite3.connect('players_data.db')
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM Player
        WHERE name = ?
    ''', (name,))
    if cur.rowcount > 0:
        print('Player deleted.')
    else:
        print('Player not found.')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
