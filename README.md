

<p align= "center">
 <img src="./static/logo_blue.png" alt="Darasa Logo" width="150/">
 </p>

 <h1 align="center">Darasa To-Do List Application</h1>

---
## Project Overview

Darasa To-Do List is a multi-interface task management application built with **Python**, supporting both a **Flask-based Web App** and a **Tkinter Desktop GUI**. This project focuses on implementing key **Data Structures** — Stack, Queue, Dictionary, and Arrays (Lists) — in a real-world context.

Users can **add**, **edit**, **delete**, **mark as complete**, **search tasks**, and even **undo actions**. It demonstrates how academic data structure concepts translate into practical, user-friendly applications.

---

## 👥 Team Members & Responsibilities

| Team Member  | Files/Modules                        | Role                                                        |
| ------------ | ------------------------------------ | ----------------------------------------------------------- |
| **👨🏼‍💻Amani**    | `app.py`, `gui_app.py`, `index.html` | Admin merge handling from different branches, Flask and Tkinter integration, frontend-backend connections |
| **👨🏼‍💻Ray**      | `task_db.py`                         | Database management (CRUD with SQLite)                      |
| **👨🏼‍💻Davis**    | `queue_tasks.py`                     | Queue logic for task management                             |
| **👨🏼‍💻Jeremiah** | `stack_undo.py`                      | Undo feature using Stack                                    |
| **👩🏼‍💻Jolene**   | `dictionary_tags.py`                 | Task tagging using Dictionary                               |
| **👨🏼‍💻Jakes**    | `arrays_util.py`                     | Sorting and searching using Arrays (Lists)                  |

---
```
📂 Darasa_todo
│
├── data_structures/                  # Core logic for data structures
│   ├── arrays_util.py                # Sorting & searching tasks (Jakes)
│   ├── queue_tasks.py                # Queue operations (Davis)
│   ├── stack_undo.py                 # Undo operations using Stack (Jeremiah)
│   ├── dictionary_tags.py            # Task tagging system using Dictionary (Jolene)
│   └── task_db.py                    # Database CRUD logic (Ray)
│
├── templates/                        # HTML Templates for Flask Web App
│   └── index.html                    # Main web interface (Amani)
│
├── gui_app.py                        # Tkinter GUI Application (Amani)
├── app.py                            # Flask Web Backend (Amani)
├── darasa_todo.db                    # SQLite Database file
└── README.md                         # Project Documentation
```
---

## 🔧 Data Structures Breakdown

| Operation       | Data Structure       | Module               |
| --------------- | -------------------- | -------------------- |
| **Create**      | Queue                | `queue_tasks.py`     |
| **Read/Search** | Arrays (Lists)       | `arrays_util.py`     |
| **Update**      | Stack (Undo support) | `stack_undo.py`      |
| **Delete**      | Stack (Undo support) | `stack_undo.py`      |
| **Tags**        | Dictionary           | `dictionary_tags.py` |

---

## 💻 Features

* ✅ **Add/Edit/Delete Tasks**
* ✅ **Search Tasks**
* ✅ **Mark Tasks as Done**
* ✅ **Undo Task Actions**
* ✅ **Tagging System**
* ✅ **Sort Tasks**
* ✅ **Cross-Platform: Web & Desktop GUI**

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/ICS-2025-GROUP-D/dsa-sem-project-darasa-to-do-list.git
cd dsa-sem-project-darasa-to-do-list
```

### 2. Install Dependencies

```bash
pip install flask pillow
```

### 3. Run the Flask Web App

```bash
python app.py
# Visit http://127.0.0.1:5000 or http://localhost:5000
```

### 4. Run the Desktop GUI App

```bash
python gui_app.py
```

---

## 📌 Notes

* **Database**: SQLite (`darasa_todo.db`)
* **Frontend**: TailwindCSS for the web, Tkinter for the GUI
* **Backend**: Python with Flask and SQLite

### Recommended `.gitignore`

```
darasa_todo.db
__pycache__/
*.pyc
```

---

## 🏆 Project Highlights

This project is a **practical demonstration of data structures in action**, offering both a **web-based** and a **desktop experience**. It emphasizes modular design, clear team collaboration, and real-world usability — making it a perfect academic showcase.

---

## 🌱 Future Extensions (Optional Ideas)

* Task scheduling with deadlines
* Notification system
* Enhanced tag filtering
* User authentication

---

## 📣 License

Open for educational purposes. Contributions are welcome!



