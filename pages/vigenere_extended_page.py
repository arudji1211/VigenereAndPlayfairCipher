from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from model import vignere_extended
from pages import menu
import os


class VigenereExtended:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.frame = ttk.Frame(self.root, width=300)

    def main_layout(self):
        v_frame = self.frame
        v_frame.pack(expand=False)
        header = ttk.Label(v_frame, text="Vigenere Cipher Extended")
        header.grid(column=0, row=0, padx=10, pady=15, columnspan=4)

        KeyLabel = ttk.Label(v_frame, text="Masukkan Key")
        KeyLabel.grid(column=0, row=1, padx=5, pady=5)
        keyForm = ttk.Entry(v_frame)
        keyForm.grid(column=1, row=1, padx=5, pady=5)

        LabelForm = ttk.Label(
            v_frame, text="Silahkan Upload File yang ingin di encrypt"
        )
        LabelForm.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

        def select_file():
            filetypes = (("All files", "*.*"), ("text files", "*.txt"))

            fileInput = fd.askopenfilename(
                title="Open a file", initialdir="/", filetypes=filetypes
            )

            with open(fileInput, "rb") as file:
                data = bytearray(file.read())
            encrypted_data = vignere_extended.Vignere_extended.encrypt_data(
                keyForm.get(), data
            )
            with open(
                os.path.dirname(fileInput)
                + "/encrypted_"
                + os.path.basename(fileInput),
                "wb",
            ) as file:
                file.write(encrypted_data)
            showinfo(title="Selected File", message="File telah selesai di enkripsi")

        def select_fileD():
            filetypes = (("All files", "*.*"), ("text files", "*.txt"))

            fileInput = fd.askopenfilename(
                title="Open a file", initialdir="/", filetypes=filetypes
            )

            with open(fileInput, "rb") as file:
                data = bytearray(file.read())
            encrypted_data = vignere_extended.Vignere_extended.decrypt_data(
                keyForm.get(), data
            )
            with open(
                os.path.dirname(fileInput)
                + "/decrypted_"
                + os.path.basename(fileInput),
                "wb",
            ) as file:
                file.write(encrypted_data)
            showinfo(title="Selected File", message="File telah selesai di enkripsi")

        bUpload = ttk.Button(v_frame, text="Select File", command=select_file)
        bUpload.grid(column=3, row=3, padx=10, pady=10)
        LabelDecryptForm = ttk.Label(
            v_frame, text="Silahkan Upload File yang ingin di decrypt"
        )
        LabelDecryptForm.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
        bUpload = ttk.Button(v_frame, text="Select File", command=select_fileD)
        bUpload.grid(column=3, row=4, padx=10, pady=10)

        def KembaliB():
            self.frame.destroy()
            modelMenu = menu.Menu(self.root)
            modelMenu.layout_frame()

        btnKembali = ttk.Button(v_frame, text="Kembali", command=KembaliB)
        btnKembali.grid(column=3, row=5, padx=10, pady=10)
