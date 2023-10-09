class playfair:
    def membuat_matrix(self, key):
        alphabet = "abcdefghiklmnopqrstuvwxyz"
        matrix = [["" for _ in range(5)] for _ in range(5)]
        baris = 0
        kolom = 0
        key_char = set()

        for char in key:
            if baris < 5 and kolom < 5:
                if char not in key_char:
                    matrix[kolom][baris] = char
                    key_char.add(char)
                    baris += 1
                    if baris == 5:
                        baris = 0
                        kolom += 1

        for char in alphabet:
            if baris < 5 and kolom < 5:
                if char not in key_char:
                    matrix[kolom][baris] = char
                    key_char.add(char)
                    baris += 1
                    if baris == 5:
                        baris = 0
                        kolom += 1

        return matrix

    def teksToBigram(plaintext):
        bigrams = []
        i = 0
        while i < len(plaintext):
            if i + 1 < len(plaintext):
                if plaintext[i] != plaintext[i + 1]:
                    bigrams.append(plaintext[i] + plaintext[i + 1])
                    i += 2
                else:
                    bigrams.append(plaintext[i] + "x")
                    i += 1

            else:
                bigrams.append(plaintext[i] + "x")
                i += 2

        return bigrams

    def bigramtoText(bigram):
        out = ""
        counterx = 0
        for i in range(len(bigram)):
            if i + 1 < len(bigram):
                if bigram[i][0] == bigram[i + 1][0] and bigram[i][1].lower() == "x":
                    out += bigram[i][0]
                    counterx += 1
                else:
                    out += bigram[i]
            else:
                out += bigram[i]

        return out.lower()

    # cari kolom matrix
    def barisMatrix(char, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if char == matrix[i][j]:
                    return (i, j)

    # jika lebih dari 5 kembalikan ke 0

    # enkripsi

    def decrypt(self, matrix, bigram):
        bigram_enc = []
        data = bigram.split()
        for char in data:
            temp = ""
            char = char.lower()
            baris1, kolom1 = self.barisMatrix(char[0], matrix)
            baris2, kolom2 = self.barisMatrix(char[1], matrix)

            # persyaratan pertama
            if kolom1 == kolom2:
                baris1 -= 1
                baris2 -= 1
                temp += matrix[(baris1 % 5)][kolom1]
                temp += matrix[(baris2 % 5)][kolom2]
            # persyaratan kedua
            elif baris1 == baris2:
                kolom1 -= 1
                kolom2 -= 1
                temp += matrix[baris1][kolom1 % 5]
                temp += matrix[baris1][kolom2 % 5]
            else:
                # persyaratan ketiga
                # if kolom1 < kolom2:
                #   temp += matrix[baris1][kolom2]
                #    temp += matrix[baris2][kolom1]
                # elif kolom1 > kolom2:
                temp += matrix[baris1][kolom2]
                temp += matrix[baris2][kolom1]
            bigram_enc.append(temp)

            # arr to text
            out = ""

        return bigram_enc

    def encrypt(self, matrix, bigram):
        bigram_enc = []
        for char in bigram:
            temp = ""
            baris1, kolom1 = self.barisMatrix(char[0], matrix)
            baris2, kolom2 = self.barisMatrix(char[1], matrix)

            # persyaratan pertama
            if kolom1 == kolom2:
                baris1 += 1
                baris2 += 1
                temp += matrix[(baris1 % 5)][kolom1]
                temp += matrix[(baris2 % 5)][kolom2]
            # persyaratan kedua
            elif baris1 == baris2:
                kolom1 += 1
                kolom2 += 1
                temp += matrix[baris1][kolom1 % 5]
                temp += matrix[baris1][kolom2 % 5]
            else:
                # persyaratan ketiga
                # if kolom1 < kolom2:
                #   temp += matrix[baris1][kolom2]
                #    temp += matrix[baris2][kolom1]
                # elif kolom1 > kolom2:
                temp += matrix[baris1][kolom2]
                temp += matrix[baris2][kolom1]
            bigram_enc.append(temp)

            # arr to text

        return " ".join(bigram_enc).upper()

    def preprosesTeks(text):
        text = text.lower()
        text = text.replace(" ", "")
        text = text.replace("j", "")
        return text
