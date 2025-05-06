class MyszkowskiCipher:
    def __init__(self, key):
        self.key = key.upper()
        self._create_key_order()

    def _create_key_order(self):
        # Map each letter to a list of positions
        key_positions = {}
        for i, char in enumerate(self.key):
            if char not in key_positions:
                key_positions[char] = []
            key_positions[char].append(i)

        # Sort letters and store their grouped column positions
        sorted_unique_letters = sorted(key_positions.keys())
        self.column_order = [key_positions[char] for char in sorted_unique_letters]

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace(" ", "")
        num_columns = len(self.key)
        num_rows = (len(plaintext) + num_columns - 1) // num_columns

        # Fill the matrix row-wise
        matrix = [[''] * num_columns for _ in range(num_rows)]
        for i in range(num_rows * num_columns):
            row = i // num_columns
            col = i % num_columns
            if i < len(plaintext):
                matrix[row][col] = plaintext[i]
            else:
                matrix[row][col] = 'X'  # Padding

        # Read by grouped columns (repeated letters processed row-wise together)
        ciphertext = ""
        for group in self.column_order:
            for row in range(num_rows):
                for col in group:
                    ciphertext += matrix[row][col]

        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        num_columns = len(self.key)
        num_rows = (len(ciphertext) + num_columns - 1) // num_columns

        # Prepare empty matrix
        matrix = [[''] * num_columns for _ in range(num_rows)]
        total = num_rows * num_columns
        index = 0

        # Fill the matrix by grouped columns row-by-row
        for group in self.column_order:
            for row in range(num_rows):
                for col in group:
                    if index < len(ciphertext):
                        matrix[row][col] = ciphertext[index]
                        index += 1

        # Read the matrix row by row
        plaintext = ""
        for row in matrix:
            plaintext += ''.join(row)

        return plaintext