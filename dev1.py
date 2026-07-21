import sqlite3

connection=sqlite3.connect('beginner_expenses.db')

cursor=connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS expenses(
               id INTEGER PRIMARY KEY,
               item TEXT,
               amount REAL
               )
""")

connection.commit()


def add_expense():
  item=input("What did you buy?")
  amount=float(input("How much did it cost?"))

  cursor.execute("INSERT INTO expenses (item, amount) VALUES (?, ?)", (item, amount))

  connection.commit()
  print("Expense added\n")


def view_expenses():
  cursor.execute("SELECT * FROM expenses")
  expenses=cursor.fetchall()

  if len(expenses)==0:
    print("No expenses found\n")
    return
  
  print("\nID | Item | Amount")
  print("---------------------")
  for expense in expenses:
    print(expense[0], "|", expense[1], "|", expense[2])

  print()



def show_total():
  cursor.execute("SELECT SUM(amount) FROM expenses")
  total=cursor.fetchone()[0]

  if total is None:
    total=0
  print("Your total spending is: ₹", total, "\n")


while True:
    print("--- SIMPLE EXPENSE TRACKER ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total spending")
    print("4. Exit")


    choice=input("Enter your choice")

    if choice=="1":
      add_expense()
    elif choice=="2":
      view_expenses()
    elif choice=="3":
      show_total()
    elif choice=="4":
      print("Goodbye!")
      break
    else:
      print("Please enter a number from 1 to 4.\n")

connection.close()