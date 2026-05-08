# Python Environment Setup Commands

## Python Installation Check & Global Python

```
# Run a local script
python script.py

# Check Python installation
python --version

# Alternatives if python doesn't work
py --version
python3 --version

# Install packages (individual)
python -m pip install ipykernel
python -m pip install matplotlib
python -m pip install numpy
python -m pip install pandas
python -m pip install sympy

# Install all packages at once
python -m pip install ipykernel matplotlib numpy pandas sympy
```



## Virtual Environment (venv)

```
# Navigate to project folder
cd "C:\YourProjectFolder"

# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate on Windows (Command Prompt)
.venv\Scripts\activate.bat

# Activate on macOS/Linux
source .venv/bin/activate

# Fix execution policy error on Windows (PowerShell)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Verify venv is active (Windows)
where python

# Verify venv is active (macOS/Linux)
which python

# Install packages in venv
python -m pip install numpy pandas matplotlib ipykernel

# Manually register venv as Jupyter kernel
python -m ipykernel install --user --name myVenv --display-name "Python (myVenv)"
```



# Conda Environment
```
# Create environment with latest Python
conda create -n myEnv python

# Create environment with specific Python version
conda create -n myEnv python=3.13

# List all environments
conda env list

# Activate environment
conda activate myEnv

# Install packages in conda environment
conda install numpy pandas matplotlib ipykernel sympy

# Create another environment
conda create -n test_env python=3.11

# Remove an environment
conda remove -n test_env --all

# Get environment paths
conda info --envs
```



## VS Code Shortcuts

```
# Open command palette
Ctrl+Shift+P

# Command to type in command palette
Python: Select Interpreter

# Open a new terminal
Terminal → New Terminal
```

