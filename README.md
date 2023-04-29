# Car Inventory Management System

This is a simple car inventory management system implemented using Python and MySQL. It provides a command-line interface (CLI) for viewing and searching car inventory data stored in a MySQL database.

## Features

- Display a list of cars available in the inventory
- Search for cars based on various attributes such as mark, type of carburetor, number of places, transmission, and price of location per day
- Dynamically update the displayed cars based on the search criteria

## Files Description

The application consists of the following files:

* `main.py`: The main entry point of the application. It sets up the main window and handles the sign up and login      functionality.
* `signup.py`: Defines the SignupWindow class, which handles user sign up. It connects to the database and inserts user data - upon successful sign up.
* `login.py`: Defines the LoginWindow class, which handles user login. It connects to the database and verifies user credentials.
* `inventory.py`: Defines the CarInventory class, which displays the car inventory. It fetches car data from the database and  dynamically generates car cards.

## Getting Started

### Dependencies

- Python 3.x
- tkinter: The standard Python interface to the Tk GUI toolkit.
- ttkthemes: A package that provides themed widgets for tkinter.
- customtkinter: a python UI-library based on Tkinter, which provides new, modern and fully customizable widgets.
- mysql-connector-python: A Python driver for connecting to MySQL databases.
- Pillow: A library for handling image processing tasks.
- XAMPP: A cross-platform web server solution that includes Apache, MySQL, PHP, and Perl.

### Usage

To run the project, make sure you have Python installed on your system along with the required dependencies. You also need to set up a MySQL database using XAMPP.

1. Clone the project repository.

2. Install the required Python dependencies using pip:

3. Download and install XAMPP.

4. Start the XAMPP control panel and ensure that the Apache and MySQL services are running.

5. put the "carinventory" and "users" databases in the data folder of XAMPP using the default path, copy the "carinventory" database folder to the "data" folder in the XAMPP installation directory (e.g., C:\xampp\mysql for Windows or /Applications/XAMPP/mysql for Mac), then restart the MySQL service.

6. Make sure you have a MySQL database set up with the necessary tables. You can find the SQL script to create the tables in the database.sql file.

7. Run the `main.py` file to start the application:

8. The main window of the application will appear. You can click on the "Sign Up" button to create a new account or click on the "Login" button to log in with an existing account.

9. After logging in, the car inventory window will open, displaying the available cars. You can search for cars based on different attributes using the provided search functionality.

10. Explore the features of the application and interact with the user interface to manage car rentals.

## Contributing

- YOUNESS KASSIDE (Creator, Lead Developer)

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


