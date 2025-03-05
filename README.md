# QR Code Generator

## Installation

### 1. Using pyenv on macOS

```shell
# Install pyenv
> brew install pyenv

# Configure Terminal (Zsh) to load pyenv on startup
> echo '# Pyen' >> ~/.zshrc
> echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
> echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
> echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc

# Apply changes
> exec "$SHELL"

# Check available Python versions
> pyenv install --list

# Install Python 3.13.2
> pyenv install 3.13.2
> pyenv global 3.13.2

# Python installed by Pyenv is located in ${HOME}/.pyenv/versions

# Verify installation
> python --version
> pip --version

# Upgrade pip to the latest version
> pip install --upgrade pip
```

### 2. Install Dependencies

#### Option 1: Install dependencies from requirements.txt (Recommended)

```shell
pip install -r requirements.txt
```

#### Option 2: Install dependencies manually

```shell
> pip install "qrcode[pil]" reportlab pandas python-dotenv
```

## Configuration

### 1. Set up the `.env` file

```shell
> cp .env.example .env
> code .env # Open the file in VS Code (or use your preferred editor)
```

## Execution

### 1. Run the script

```shell
> unset CSV_FILE_PATH # Ensure environment variable is not set
> python generate_qr_pdf.py
```
