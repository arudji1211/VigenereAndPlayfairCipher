# Ubah list menjadi string
my_list = ["az", "bz"]
my_string = " ".join(my_list).upper()

# Pecah string menjadi array
bigs = my_string.split()

# Iterasi dan ambil huruf pertama
for char in bigs:
    print(char[0])
