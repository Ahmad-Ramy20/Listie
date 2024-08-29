## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Ahmad-Ramy20/Listie.git
    cd Listie
    ```
2. Install Flask:
    ```bash
    pip install flask
    ```

## Usage

Run the application:

# Listie

Listie is your new bestie, a task management application built with Flask. It allows you to add, mark as complete, remove, and clear tasks. You can save lists and access them later. It also allows you to customize it with different themes to fit your liking.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Add Task**: Users can add new tasks to the list.
- **Mark Task as Complete**: Users can mark tasks as complete.
- **Remove Task**: Users can remove tasks from the list.
- **Clear Tasks**: Users can clear all tasks.
- **Save List**: Users can save a list of tasks to a text file.
- **Open Saved List**: Users can open and edit a list of tasks from a text file.
- **Duplicate Alert**: Recognizes duplicate tasks and shows an alert.
- **Choose Theme**: Users can choose from five different-colored themes.

## Technologies Used
- **Flask**: A micro web framework for Python used to build the web application.
- **JavaScript**: If any JavaScript is used for front-end interactivity.
- **HTML/CSS**: Markup and styling for the front-end of the application.
- **Python**: is the core programming language used to develop the application logic.
- **File I/O**: Reading from and writing tasks to text files.
- **Git**: Version control to manage the codebase.

## Prerequisites

- Python 3.x
- Flask
- Web browser

## Installation

1. Clone the repository:
    ```bash | cmd
    git clone https://github.com/yourusername/listie.git
    cd listie
    ```
2. Install Flask:
    ```bash | cmd
    pip install flask
    ```

## Usage

Run the application:

1. In the project's directory, run:
   ```bash | cmd
   python app.py

2. Open your web browser and go to: http://127.0.0.1:5000/

3. Typa a task | Open an old list (type --name+(.txt)--, put the list file in the same folder as app.py).

4. Click "Add" button.

5. Complete task | remove task | clear all tasks.

6. Save task/s to a file (type --name+(.txt)--, put the list file in the same folder as app.py).



## File Structure
app.py: The main Flask application.

script.js: The JS code for interactive entities.

templates/
index.html: The HTML template for displaying tasks.

styles/
styles.css: The CSS file for app styling and layout.

tasks.txt: The file where tasks are stored.

## Example
To add a task, enter the task in the input field and submit the form. The task will be added to the list. You can then mark it as complete or remove it from the list. You can finally save it into a text file.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
