from tkinter import ttk
from pages import vigenere_page
from pages import vigenere_extended_page
from pages import playfair_page


class Menu:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x200")
        self.frame = ttk.Frame(self.root)

    def layout_frame(self):
        menu_frame = self.frame
        menu_frame.pack(expand=False)

        header = ttk.Label(menu_frame, text="Tugas Keamanan Komputer ( Kriptografi )")
        header.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

        menu1 = ttk.Label(menu_frame, text="Vigenere Cipher")
        menu1.grid(column=0, row=1, padx=10, pady=10)
        btnmenu1 = ttk.Button(menu_frame, text="go", command=self.toVigenereCipher)
        btnmenu1.grid(column=1, row=1, padx=10, pady=5)

        menu2 = ttk.Label(menu_frame, text="Extended Vigenere Cipher")
        menu2.grid(column=0, row=2, padx=10, pady=10)
        btnmenu2 = ttk.Button(
            menu_frame, text="go", command=self.toVigenereExtendedCipher
        )
        btnmenu2.grid(column=1, row=2, padx=10, pady=5)

        menu3 = ttk.Label(menu_frame, text="Playfair Cipher")
        menu3.grid(column=0, row=3, padx=10, pady=10)
        btnmenu3 = ttk.Button(menu_frame, text="go", command=self.toPlayfair)
        btnmenu3.grid(column=1, row=3, padx=10, pady=5)

    def layout_frame2(self):
        self.frame = ttk.Frame(self.root)
        menuframe = self.frame
        menuframe.pack(expand=True)
        menu1 = ttk.Label(menuframe, text="Enkripsi Arudji")
        menu1.grid(column=0, row=0, padx=10, pady=10)
        btnmenu1 = ttk.Button(menuframe, text="go", command=self.enkripsi1)
        btnmenu1.grid(column=1, row=0, padx=10, pady=10)

    def enkripsi1(self):
        self.frame.destroy()
        self.layout_frame2()
        print("aruji")

    def toVigenereCipher(self):
        self.frame.destroy()
        vigenere = vigenere_page.Vigenere_page(self.root)
        vigenere.main_layout()

    def toVigenereExtendedCipher(self):
        self.frame.destroy()
        vigenere = vigenere_extended_page.VigenereExtended(self.root)
        vigenere.main_layout()

    def toPlayfair(self):
        self.frame.destroy()
        playfair = playfair_page.playfair_page(self.root)
        playfair.main_layout()
