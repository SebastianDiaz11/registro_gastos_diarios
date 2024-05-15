import sqlite3
import datetime

# Conexión a la base de datos 
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Creación de la tabla 
cursor.execute('''CREATE TABLE expenses (
                    id INTEGER PRIMARY KEY,
                    amount REAL NOT NULL,
                    date TEXT NOT NULL,
                    description TEXT
                )''')

def add_expense(amount, description):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor.execute('INSERT INTO expenses (amount, date, description) VALUES (?, ?, ?)', (amount, date, description))
    conn.commit()
    print("Gasto registrado correctamente.")

def delete_expense(expense_id):
    cursor.execute('DELETE FROM expenses WHERE id=?', (expense_id,))
    expense = conn.commit()
    if expense:
        cursor.execute('DELETE FROM contacts WHERE id=?', (expense_id,))
        conn.commit()
        print("Contacto eliminado correctamente.")
    else:
        print("No hay contacto registrado con ese ID.")

def display_expenses():
    cursor.execute('SELECT * FROM expenses')
    expenses = cursor.fetchall()
    if expenses:
        print("\nLista de gastos:")
        for expense in expenses:
            print(f"ID: {expense[0]}, Cantidad: ${expense[1]}, Fecha: {expense[2]}, Descripción: {expense[3]}")
    else:
        print("No hay gastos registrados.")
        
def total_expenses():
    cursor.execute('SELECT SUM(amount) FROM expenses')
    total = cursor.fetchone()[0]
    if total:
        print(f"\nGastos totales: {total}")
    else:
        print("No hay gastos registrados.")

# Menu
while True:
    print("\n1. Registrar gasto")
    print("2. Mostrar gastos")
    print("3. Eliminar gasto")
    print("4. Calcular gastos totales")
    print("5. Salir")

    choice = input("Ingrese el número de la opción que desea realizar: ")

    if choice == '1':
        amount = float(input("Ingrese la cantidad gastada: "))
        description = input("Ingrese una breve descripción del gasto: ")
        add_expense(amount, description)
    elif choice == '2':
        display_expenses()
    elif choice == '3':
        expense_id = int(input("Ingrese el ID del gasto que desea eliminar: "))
        delete_expense(expense_id)
    elif choice == '4':
        total_expenses()
    elif choice == '5':
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")