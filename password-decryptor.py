import os
import subprocess

def decrypt_pdf(input_path, output_path, password):
    """
    Decrypt a single PDF file using qpdf.
    """
    try:
        subprocess.run(
            ['qpdf', '--password=' + password, '--decrypt', input_path, output_path],
            check=True
        )
        print(f"Successfully decrypted {input_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to decrypt {input_path}: {e}")

def decrypt_pdfs_in_folder(folder_path, password):
    print(f"Decrypting PDF files in {folder_path}...")

    # Ensure the output directory exists
    output_folder = os.path.join(folder_path, 'decrypted')
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf') or filename.endswith('.PDF'):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            decrypt_pdf(input_path, output_path, password)

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decrypt PDF files in a folder.')
    parser.add_argument('-d', '--directory', help='Path to the directory containing the PDF files', required=True)
    parser.add_argument('-p', '--password', help='Password for the PDF files', required=True)

    args = parser.parse_args()

    directory = args.directory
    password = args.password

    # Decrypt all PDF files in the folder
    decrypt_pdfs_in_folder(directory, password)
