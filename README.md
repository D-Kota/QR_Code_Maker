# QR Code Maker

A simple Python script that generates QR codes from URLs. This tool allows you to quickly create QR codes for any web address with an easy-to-use command-line interface.

## Features

- Generate QR codes for any URL
- Automatic file naming based on the URL
- Continuous operation mode - generate multiple QR codes in one session
- Simple command-line interface
- Works in Jupyter notebooks or as a standalone Python script

## Requirements

- Python 3.x
- qrcode library
- Pillow (PIL)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/QR_Code_Maker.git
cd QR_Code_Maker
```

2. Install required dependencies:
```bash
pip install qrcode[pil]
```

## Usage

### In Jupyter Notebook

1. Open `QR_Code_Maker.ipynb` in Jupyter Notebook or Google Colab
2. Run the code cell
3. Enter a URL when prompted
4. The QR code will be generated and displayed
5. Enter another URL or type 'exit' to quit

### As a Python Script

```bash
python qr_code_maker.py
```

Then follow the prompts to enter URLs.

## How It Works

1. The script prompts you for a URL
2. It generates a QR code for that URL
3. The QR code is saved as a PNG file with a name based on the URL
4. The QR code is displayed (in notebooks) or saved to disk
5. The process repeats until you type 'exit'

## File Naming

Generated QR codes are automatically named using the format:
```
qr_code_[sanitized_url].png
```

Special characters in URLs are replaced with underscores to create valid filenames.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
