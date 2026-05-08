# Python Environment Setup Commands

## Global Python

\```
python --version
python -m pip install ipykernel matplotlib numpy pandas sympy
\```

## Virtual Environment (venv)

\```bash
# Create and activate
python -m venv .venv
.\.venv\Scripts\activate.ps1  # Windows PowerShell

# Install packages
python -m pip install numpy pandas matplotlib ipykernel

# Register kernel
python -m ipykernel install --user --name myVenv --display-name "Python (myVenv)"
\```

## Conda

\```bash
conda create -n myEnv python
conda activate myEnv
conda install numpy pandas matplotlib ipykernel sympy
conda env list
\```

## VS Code Shortcuts

- `Ctrl+Shift+P` → `Python: Select Interpreter`