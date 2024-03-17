# GRRN-Chatbox

## Description

This is a chatbox that is built using HTML, CSS, and JavaScript. It is a simple chatbox that allows users to send messages to each other. The chatbox is built using the following technologies:

- HTML
- CSS
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Websockets](https://websockets.fastapi.tiangolo.com/)
- [Sqlalchemy](https://www.sqlalchemy.org/)

The chatbox is built using the FastAPI framework, which is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It is built on top of Starlette for the web parts and Pydantic for the data parts. The chatbox uses websockets to allow for real-time communication between the server and the client. The chatbox also uses Sqlalchemy to interact with a SQLite database to store the messages that are sent by the users.

## Installation

To install the chatbox, you will need to have Python 3.7+ installed on your machine. You can download Python from the following [link](https://www.python.org/downloads/). Once you have Python installed, you can install the chatbox by following the steps below:

1. Clone the repository to your local machine using the following command:

```bash
git clone
```

2. Change into the directory of the repository using the following command:

```bash
cd GRRN-Chatbox
```

3. Create a virtual environment using the following command:

For virtualenv:

```bash
python -m venv venv
```

For conda:

```bash
conda create --name venv
```

For pipenv:

```bash
pipenv install
```

4. Activate the virtual environment using the following command:

For virtualenv:

```bash
source venv/bin/activate
```

For conda:

```bash
conda activate venv
```

For pipenv:

```bash
pipenv shell
```

5. Install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

6. Run the chatbox using the following command:

```bash
python main.py
```

7. Open your web browser and navigate to the following URL:

```bash
http://localhost:8000/<1 or 2>
```

## Usage

To use the chatbox, you can open the chatbox in your web browser and enter your name in the input field at the bottom of the page. Once you have entered your name, you can start sending messages to other users by typing your message in the input field at the bottom of the page and pressing the "Send" button. You can also view the messages that have been sent by other users in the chatbox. The chatbox will display the messages in real-time, so you can see the messages as they are sent by other users.

## Contributing

If you would like to contribute to the chatbox, you can do so by following the steps below:

1. Fork the repository to your own GitHub account by clicking the "Fork" button at the top of the page.
2. Clone the repository to your local machine using the following command:

```bash
git clone
```

3. Change into the directory of the repository using the following command:

```bash
cd GRRN-Chatbox
```

4. Create a new branch for your changes using the following command:

```bash
git checkout -b <branch-name>
```

5. Make your changes to the code and commit them to the repository using the following commands:

```bash
git add .
git commit -m "Your commit message here"
```

6. Push your changes to your fork of the repository using the following command:

```bash
git push origin <branch-name>
```

7. Open a pull request on the original repository by navigating to the "Pull Requests" tab at the top of the page and clicking the "New Pull Request" button.
8. Fill in the details of your pull request and click the "Create Pull Request" button to open the pull request.
9. Wait for the pull request to be reviewed by the maintainers of the repository. Once the pull request has been reviewed and approved, it will be merged into the original repository.
10. Congratulations! You have successfully contributed to the chatbox.
11. If you have any questions or need help with contributing to the chatbox, please feel free to reach out to the maintainers of the repository.
12. Thank you for your contribution!
