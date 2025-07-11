# Darasa To-Do List Application

A to-do list application built with Flask and Python, implementing various data structures for efficient task management.

## Features

- Create, Read, Update, and Delete tasks
- Search functionality for tasks
- Task status toggling
- Queue-based task management
- Responsive web interface
- SQLite database for data persistence

## Data Structures Implemented

1. **Queue** - For task queue management
2. **Arrays** - For task storage and searching
3. **Dictionary** - For task tagging and categorization
4. **Stack** - For undo operations

## Prerequisites

- Python 3.x
- Flask
- SQLite3

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ICS-2025-GROUP-D/dsa-sem-project-darasa-to-do-list.git
cd darasa-to-do-list
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install required dependencies:

```bash
pip install flask
```

## Running the Application

1. Start the Flask server:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

## Project Structure

```
├── app.py              # Main Flask application
├── gui_app.py          # GUI version of the application
├── darasa_todo.db      # SQLite database
├── data_structures/    # Data structure implementations
│   ├── arrays_util.py
│   ├── dictionary_tags.py
│   ├── queue_tasks.py
│   ├── stack_undo.py
│   └── task_db.py
├── static/            # Static files
│   └── logo_white.png
└── templates/         # HTML templates
    └── index.html
```

## Usage

- **Add Task**: Enter task description in the input field and click "Add"
- **Delete Task**: Click the delete button next to any task
- **Edit Task**: Click the edit button to modify task description
- **Toggle Status**: Click the checkbox to mark task as complete/incomplete
- **Search Tasks**: Use the search bar to filter tasks

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is created as part of a semester project for Data Structures & Algorithms course.

## Acknowledgments

- Flask framework
- Data Structures & Algorithms course team
