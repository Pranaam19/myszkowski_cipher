# Myszkowski Cipher

This project implements the Myszkowski Cipher, a transposition cipher similar to the Incomplete Columnar Cipher but with a unique handling of repeated letters in the key.

## Overview

The Myszkowski Cipher was invented by Émile Victor Théodore Myszkowski. It works by arranging the plaintext in a grid under the key, then reading off the columns in the order determined by the alphabetical order of the key letters. The unique feature is that columns with identical key letters are read together.

## Features

- Command-line interface for encryption and decryption
- Web interface for interactive use
- Pure Python implementation

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

```bash
python src/main.py --key YOUR_KEY --mode encrypt --text "YOUR TEXT"
python src/main.py --key YOUR_KEY --mode decrypt --text "YOUR ENCRYPTED TEXT"
```

### Web Interface

```bash
python src/app.py
```

Then open your browser and navigate to http://localhost:5000

## Example

### Key: TOMATO
### Plaintext: HELLO WORLD

The grid would look like:

```
T O M A T O
5 3 2 1 5 3
-----------
H E L L O W
O R L D _ _
```

The numbers represent the order in which the columns are read.

Reading by column order: `LLDHEORWLO_`

## Project Structure

```
myszkowski_cipher/
├── README.md
├── requirements.txt
└── src/
    ├── app.py              # Web application
    ├── cipher.py           # Cipher implementation
    ├── main.py             # Command-line interface
    ├── static/
    │   ├── css/
    │   │   └── style.css   # Styles for web interface
    │   └── js/
    │       └── script.js   # JavaScript for web interface
    └── templates/
        └── index.html      # HTML template for web interface
```

## License

MIT
