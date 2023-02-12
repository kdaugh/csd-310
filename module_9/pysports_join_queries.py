#Kevin Daugherty
#February 11, 2023
#Module 9.2 Assignment
#Creating a join for player and team tables

#import statements
import mysql.connector
from mysql.connector import errorcode

#database configure object
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
#block for handling errors
try:
    db = mysql.connector.connect(**config) #connect to the pysports database

    cursor = db.cursor()

    #Inner join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #fetch results from the cursor object
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")

    #display player data 
    for player in players:
        print("  Player ID:  {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0],player[1],player[2],player[3]))

    input("\n\n  Press any key to continue... ")    

#error handling
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    #close the connection to MySQL
    db.close()