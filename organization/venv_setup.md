# Virtual environment setup
_Version: 1.0, Last change: 24.04.2024_

This is a tutorial on how to set up a virtual environment and install dependencies for the project.
After doing it you can start coding.

At this point you should have Python installed.
Additionally, this tutorial works only for Windows users.

### 1. Check your Python version
The version of your Python should be 3.10 or higher.
You can check the version by running the following command in your terminal:
```bash
python --version
```
If it is lower than 3.10, you should install a newer version.
I assume you can do it. 
If you cannot, please contact me.

### 2. Create a virtual environment
To create a virtual environment, run the following command in your terminal (you must be in a project directory):
```bash
python -m venv venv
```

### 3. Activate the virtual environment
To activate the virtual environment, run the following command in your terminal:
```bash
.venv/scripts/activate
```

### 4. Install dependencies
To install dependencies, run the following command in your terminal:
```bash
pip install -r requirements.txt
```
At this point you should have all the dependencies installed and you can start coding.
