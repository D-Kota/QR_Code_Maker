#!/usr/bin/env python3
"""
QR Code Generator
A simple tool to generate QR codes from URLs
"""

import qrcode
import os
from typing import Optional


def generate_qr_code(url: str, output_dir: str = ".") -> Optional[str]:
    """
    Generates a QR code for the given URL and saves it to a file.
    
    Args:
        url: The URL to encode in the QR code
        output_dir: Directory to save the QR code image (default: current directory)
    
    Returns:
        The filename of the saved QR code, or None if an error occurred
    """
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% or less errors can be corrected
            box_size=10,  # How many pixels each "box" of the QR code will be
            border=4,  # How many boxes thick the border around the QR code will be
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Generate a filename from the URL, replacing non-alphanumeric chars with underscores
        safe_url_name = "".join(
            c for c in url if c.isalnum() or c in ['.', '_', '-']
        ).replace('/', '_').replace(':', '_').replace('?', '_').replace('=', '_')
        
        filename = f"qr_code_{safe_url_name}.png"
        
        # Ensure the filename is not excessively long
        if len(filename) > 200:
            filename = filename[:200] + '.png'

        # Create full path
        filepath = os.path.join(output_dir, filename)
        
        # Save the image
        img.save(filepath)
        print(f"✓ QR code for '{url}' saved as '{filename}'")
        
        return filename
        
    except Exception as e:
        print(f"✗ Error generating QR code for '{url}': {e}")
        return None


def main():
    """Main function to run the QR code generator"""
    print("=" * 60)
    print("QR Code Generator".center(60))
    print("=" * 60)
    print("\nThis tool generates QR codes from URLs.")
    print("Enter URLs one at a time, or type 'exit' to quit.\n")
    
    while True:
        user_url = input("Enter a URL (or 'exit' to quit): ").strip()
        
        if user_url.lower() == 'exit':
            print("\nThank you for using QR Code Generator!")
            break
        elif user_url:
            generate_qr_code(user_url)
            print()  # Add blank line for readability
        else:
            print("No URL entered. Please try again.\n")


if __name__ == "__main__":
    main()
