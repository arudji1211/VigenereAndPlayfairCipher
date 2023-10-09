from tkinter import ttk
import tkinter as tk
from model import vigenere
from pages import menu


class Vigenere_page:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.frame = ttk.Frame(self.root, width=300)

    def main_layout(self):
        v_frame = self.frame
        v_frame.pack(expand=False)

        header = ttk.Label(v_frame, text="Vigenere Cipher")
        header.grid(column=0, row=0, padx=10, pady=15, columnspan=3)

        # key
        inputKeyLabel = ttk.Label(v_frame, text="Masukkan Secret Key")
        inputKeyLabel.grid(row=1, padx=10, pady=5, column=0, columnspan=3)

        KeyForm = ttk.Entry(v_frame)
        KeyForm.grid(row=2, padx=10, pady=5, columnspan=3)

        inputLabel = ttk.Label(v_frame, text="Plaintext")
        inputLabel.grid(row=3, padx=10, pady=5, column=0, columnspan=3)

        inputFormEnc = tk.Text(v_frame, width=40, height=8)
        inputFormEnc.grid(row=4, padx=5, pady=10, column=0, columnspan=3)

        inputLabel = ttk.Label(v_frame, text="Ciphertext")
        inputLabel.grid(row=5, padx=10, pady=5, column=0, columnspan=3)

        inputFormDec = tk.Text(v_frame, width=40, height=8)
        inputFormDec.grid(row=6, padx=5, pady=10, column=0, columnspan=3)

        modelVig = vigenere.Vigenere

        # button encrypt
        def EncryptB():
            text = inputFormEnc.get("1.0", tk.END)
            inputFormDec.delete("1.0", tk.END)
            inputFormDec.insert("1.0", modelVig.encrypt(text, KeyForm.get()))

        def DecryptB():
            text = inputFormDec.get("1.0", tk.END)
            inputFormEnc.delete("1.0", tk.END)
            inputFormEnc.insert("1.0", modelVig.decrypt(text, KeyForm.get()))

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
