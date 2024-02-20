# Notes CLI

Notes CLI is a command-line application that allows users to manage notes and categorize them.

## Installation

1. Clone the repository:

git clone https://github.com/arkir9/notes-app-cli-project.git


2. Navigate to the project directory:

cd notes-cli

3. Install the required dependencies:

Pipenv install

4. Run the program using pipenv shell:

Pipenv shell

### Listing Notes

To list all notes, use the `list` command:

python3 cli.py list

### Deleting a Note

To delete a note, use the `delete` command followed by the title of the note:

python3 cli.py delete "Title of the Note"

### Searching Notes

To search for notes containing a specific keyword, use the `search` command followed by the keyword:

python3 cli.py search "Keyword"

### Searching Notes by Category

To search for notes within a specific category, use the `search_category` command followed by the category name:

python3 cli.py search_category "Category Name"