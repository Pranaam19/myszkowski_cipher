#!/usr/bin/env python3

import argparse
from cipher import MyszkowskiCipher

def main():
    parser = argparse.ArgumentParser(description='Myszkowski Cipher - A transposition cipher')
    parser.add_argument('--key', '-k', required=True, help='The key for the cipher')
    parser.add_argument('--mode', '-m', choices=['encrypt', 'decrypt'], required=True, 
                        help='Mode: encrypt or decrypt')
    parser.add_argument('--text', '-t', required=True, help='Text to encrypt or decrypt')
    
    args = parser.parse_args()
    
    cipher = MyszkowskiCipher(args.key)
    
    if args.mode == 'encrypt':
        result = cipher.encrypt(args.text)
        print(f"Encrypted text: {result}")
    else:  # decrypt
        result = cipher.decrypt(args.text)
        print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()
