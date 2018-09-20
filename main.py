import sqlite3

conn = sqlite3.connect('cars.db')
c = conn.cursor()

'''function to create a table name myCars in the cars database'''
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS myCars(primaryID INTEGER PRIMARY KEY AUTOINCREMENT, Year INTEGER NOT NULL, Make TEXT, Model TEXT, Color TEXT, price INTEGER NOT NULL)')
    c.execute('SELECT * FROM myCars')
    data = c.fetchall()
    print(data)
    conn.commit()

'''function to add a row of data into the myCars table'''
def addRowOfData():
        year = int(input("What year is the car?"))
        make = str(input("What make is the car?")).upper()
        model = str(input("What model is the car?")).upper()
        color = str(input("What color is the car?")).upper()
        price = int(input("What is the price?"))
        c.execute("INSERT INTO myCars (year, make, model, color, price) VALUES (?, ?, ?, ?, ?)",
              (year, make, model, color, price))
        c.execute('SELECT * FROM myCars WHERE make = ?', (make, ))
        for row in c.fetchall():
            print(row)
            conn.commit()

'''function to update a row within the table'''
def updateRow():
    while True:
        option = int(input("What would you like to update?\n 1. Year of car?\n 2. Make of car?\n 3. Model of car?\n 4. Color of car?\n 5. Price of car?\n 6. Return to Main Menu"))
        if option == 1:
            oldYear = int(input("What year do you need to update?"))
            newYear = int(input("What is the new year?"))
            c.execute('UPDATE myCars SET year = ? WHERE year = ?', (newYear, oldYear))
            conn.commit()
            print("The year has been updated!\n")
        if option == 2:
            oldMakeOfCar = input("What Make do you need to update?").upper()
            newMakeOfCar = input("What do you need to update it to?").upper()
            c.execute('UPDATE myCars SET make = ? WHERE make = ?', (newMakeOfCar, oldMakeOfCar))
            conn.commit()
            print("The Make has been updated!\n")
        if option == 3:
            oldModelOfCar = input("What Make do you need to update?").upper()
            newModelOfCar = input("What do you need to update it to?").upper()
            c.execute('UPDATE myCars SET model = ? WHERE model = ?', (newModelOfCar, oldModelOfCar))
            conn.commit()
            print("The Model has been updated!\n")
        if option == 4:
            oldColor = input("What Make do you need to update?").upper()
            newColor = input("What color do you need to update it to?").upper()
            c.execute('UPDATE myCars SET color = ? WHERE color = ?', (newColor, oldColor))
            conn.commit()
            print("The Color has been updated!\n")
        if option == 5:
            oldPrice = input("What Make do you need to update?").upper()
            newPrice = input("What do you need to update it to?").upper()
            c.execute('UPDATE myCars SET price = ? WHERE price = ?', (newPrice, oldPrice))
            conn.commit()
            print("The price has been updated!\n")
        elif option == 6:
            print("Back to the main menu!")
            return

'''function to delete a row within the table'''
def deleteRow():
    carToDelete = int(input("What ID would you like to delete from the table?"))
    c.execute('DELETE FROM myCars WHERE primaryID = ?', (carToDelete, ))
    conn.commit()

'''function to display the table data'''
def displayAllRows():
    c.execute('SELECT * FROM myCars')
    data = c.fetchall()
    print("Here is your table data: ")
    print(data)

'''function to display a single row as chosen'''
def displaySingleRow():
    singleRow = int(input("Which car do you want to display?(Enter the ID number)"))
    c.execute('SELECT * FROM myCars WHERE primaryID = ?', (singleRow, ))
    print("Here is the row you selected: ")
    for row in c.fetchall():
        print(row)

'''Main code that runs the program'''
print("*****************************\nWelcome to the Cars database!\n*****************************")
while True:
    option = int(input("\nSelect an option to begin:\n 1. Initiate a cars table\n 2. Add a row of car data\n 3. Update a row of car data\n 4. Delete a row of car data\n 5. Display all rows of car data\n 6. Display a single row of car data\n 7. Exit\n"))

    if option == 1:
        print("You have created a Car Table!")
        create_table()

    elif option == 2:
        addRowOfData()
        print("You have added the data to the table!")

    elif option ==3:
        print("You have chosen to update a row!")
        updateRow()

    elif option ==4:
        deleteRow()
        print("The row has been deleted!")

    elif option == 5:
        displayAllRows()

    elif option == 6:
        displaySingleRow()

    elif option == 7:
        conn.close()
        exit()

