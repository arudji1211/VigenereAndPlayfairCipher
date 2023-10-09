from tkinter import ttk
import tkinter as tk
from model import playfair
from pages import menu


class playfair_page:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.frame = ttk.Frame(self.root)

    def main_layout(self):
        v_frame = self.frame
        v_frame.pack(expand=False)

        header = ttk.Label(v_frame, text="Playfair Cipher")
        header.grid(column=0, row=0, padx=10, pady=15, columnspan=3)

        inputLabel = ttk.Label(v_frame, text="Key")
        inputLabel.grid(row=1, padx=10, pady=5, column=0, columnspan=3)

        inputFormKey = tk.Entry(v_frame)
        inputFormKey.grid(row=2, padx=5, pady=10, column=0, columnspan=3)

        #####
        inputLabel = ttk.Label(v_frame, text="Plaintext")
        inputLabel.grid(row=3, padx=10, pady=5, column=0, columnspan=3)

        inputFormEnc = tk.Text(v_frame, width=40, height=8)
        inputFormEnc.grid(row=4, padx=5, pady=10, column=0, columnspan=3)

        inputLabel = ttk.Label(v_frame, text="Ciphertext")
        inputLabel.grid(row=5, padx=10, pady=5, column=0, columnspan=3)

        inputFormDec = tk.Text(v_frame, width=40, height=8)
        inputFormDec.grid(row=6, padx=5, pady=10, column=0, columnspan=3)
        ##

        modelPlay = playfair.playfair

        def EncryptB():
            text = inputFormEnc.get("1.0", tk.END)
            inputFormDec.delete("1.0", tk.END)
            matr = modelPlay.membuat_matrix(
                modelPlay, modelPlay.preprosesTeks(inputFormKey.get())
            )
            bigram = modelPlay.preprosesTeks(text)
            bigram = modelPlay.teksToBigram(bigram.strip())
            print(bigram)
            inputFormDec.insert("1.0", modelPlay.encrypt(modelPlay, matr, bigram))

        def DecryptB():
            text = inputFormDec.get("1.0", tk.END)
            inputFormEnc.delete("1.0", tk.END)
            matr = modelPlay.membuat_matrix(
                modelPlay, modelPlay.preprosesTeks(inputFormKey.get().strip())
            )
            inputFormEnc.insert(
                "1.0",
                modelPlay.bigramtoText(
                    modelPlay.decrypt(modelPlay, matr, text.strip())
                ),
            )

        def KembaliB():
            self.frame.destroy()
            modelMenu = menu.Menu(self.root)
            modelMenu.layout_frame()

        btnEncrypt = tk.Button(v_frame, text="Encrypt", command=EncryptB)
        btnEncrypt.grid(column=0, row=7, padx=10, pady=5)
        btnDecrypt = tk.Button(v_frame, text="Kembali", command=KembaliB)
        btnDecrypt.grid(column=1, row=7, padx=10, pady=5)
        btnKembali = tk.Button(v_frame, text="Decrypt", command=DecryptB)
        btnKembali.grid(column=2, row=7, padx=10, pady=5)
