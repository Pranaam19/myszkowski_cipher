class MyszkowskiCipher:
    """
    Implementation of the Myszkowski Cipher, a transposition cipher similar to the 
    Incomplete Columnar Cipher but with a unique handling of repeated letters in the key.
    """
    
    def __init__(self, key):
        """
        Initialize the cipher with a key.
        
        Args:
            key (str): The keyword used for the transposition.
        """
        self.key = key.upper()
        self._create_key_order()
    
    def _create_key_order(self):
        """
        Create the key order for the transposition.
        Letters with the same value in the key are processed together.
        """
        # Create a dictionary mapping each unique letter in the key to its position(s)
        key_positions = {}
        for i, char in enumerate(self.key):
            if char not in key_positions:
                key_positions[char] = []
            key_positions[char].append(i)
        
        # Sort the unique letters in the key
        sorted_unique_letters = sorted(key_positions.keys())
        
        # Create the final order of columns to read
        self.column_order = []
        for letter in sorted_unique_letters:
            self.column_order.append(key_positions[letter])
    
    def encrypt(self, plaintext):
        """
        Encrypt a message using the Myszkowski Cipher.
        
        Args:
            plaintext (str): The message to encrypt.
            
        Returns:
            str: The encrypted message.
        """
        # Remove spaces and convert to uppercase for simplicity
        plaintext = plaintext.upper().replace(" ", "")
    
        num_columns = len(self.key)
        num_rows = (len(plaintext) + num_columns - 1) // num_columns
    
    # Create the matrix and fill it with the plaintext
        matrix = [[''] * num_columns for _ in range(num_rows)]
    
        for i in range(num_rows * num_columns):
            row = i // num_columns
            col = i % num_columns
            if i < len(plaintext):
                matrix[row][col] = plaintext[i]
            else:
                matrix[row][col] = 'X'  # Fill remaining cells with 'X'
    
    # Read the ciphertext according to the column order
        ciphertext = ""
        for positions in self.column_order:
            for position in positions:
                for row in range(num_rows):
                    ciphertext += matrix[row][position]
    
        return ciphertext

    
    def decrypt(self, ciphertext):
        """
        Decrypt a message that was encrypted using the Myszkowski Cipher.
        
        Args:
            ciphertext (str): The encrypted message.
            
        Returns:
            str: The decrypted message.
        """
        ciphertext = ciphertext.upper()
        
        # Calculate dimensions of the matrix
        num_columns = len(self.key)
        num_rows = (len(ciphertext) + num_columns - 1) // num_columns
        
        # Create an empty matrix
        matrix = [[''] * num_columns for _ in range(num_rows)]
        
        # Fill the matrix according to the column order
        index = 0
        for positions in self.column_order:
            for position in positions:  # Process columns with the same letter together
                for row in range(num_rows):
                    if row * num_columns + position < len(ciphertext) and index < len(ciphertext):
                        matrix[row][position] = ciphertext[index]
                        index += 1
        
        # Read the plaintext row by row
        plaintext = ""
        for row in range(num_rows):
            for col in range(num_columns):
                if matrix[row][col] != '':
                    plaintext += matrix[row][col]
        
        return plaintext
