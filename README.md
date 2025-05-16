# GTransact

## About
GTransact is a desktop application for managing GCash cash-in and cash-out transactions. It provides a simple interface for recording, updating, and tracking transactions, making it ideal for small businesses or GCash agents. The app automates service charge calculation and ensures transaction data is organized and easy to manage.

## Key Features
* **Record Transaction:** Allows users to insert new transactions into the database.
* **Update Transaction:** Update an existing transaction based on the reference number.
* **Delete Transaction:** Delete a transaction using the reference number.
* **Clear Form:** Clears all form inputs and resets the summary display.
* **Auto Calculation:** Transaction fee is automatically calculated as 1% of the amount entered.
* **Tabular Display:** Displays all recorded transactions in a table format.

## Tech Stack
- **Python 3.x** - Programming Language
- **Tkinter** - GUI Framework
- **MySQL** - Database 
- **mysql-connector-python**

## Getting Started
1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install mysql-connector-python
   ```
4. Set up the MySQL database
   ```bash
   mysql -u root -p < Database/mysql.txt
   ```
5. Run the application

## Usage Notes
1. Choose transaction type (Cash In/Out) in the app.
2. Enter the mobile number (11 digits), amount, and reference number (13 digits).
3. The service charge is auto-calculated.
4. The date field auto-fills with the current date.
5. Use the buttons to add, update, or delete transactions.
6. All transactions appear in the table below the form.

## Project Structure
- `Source/main.py` — Main application code (Tkinter GUI, MySQL logic)
- `Database/mysql.txt` — SQL commands to set up the database and table
- `README.md` — Project documentation