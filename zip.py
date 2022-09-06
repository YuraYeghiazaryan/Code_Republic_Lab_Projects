import tkinter as tk
import os
import json

def get_path():
    file = path.get()
    file1 = open(rf'{file}', 'r')
    text = file1.read()
    t = text.split()
    words = {}

    if compress_is.get():
        z_words = {}
        for i in t:
            words[i] = words.get(i, 0) + 1

        var = 0
        for i in words:
            if words[i] > 1:
                z_words[i] = chr(ord('A') + var)
                var += 1
        file1.close()

        with open(rf'{file}', "w") as new_file1:
            for i in t:
                if i in z_words:
                    new_file1.write(z_words[i] + ' ')
                else:
                    new_file1.write(i + ' ')
        words_z = dict([val, key] for key, val in z_words.items())

        with open(rf'{file}'[:-4] + '_zip.txt', 'w') as file_for_decompress:
            json.dump(words_z, file_for_decompress)
            
    else:
        with open(rf'{file}'[:-4] + '_zip.txt') as file_for_decompress:
            words_z = json.load(file_for_decompress)
            with open(rf'{file}', "w") as new_file1:
                for i in t:
                    if i in words_z:
                        new_file1.write(words_z[i] + ' ')
                    else:
                        new_file1.write(i + ' ')
            os.remove(rf'{file}'[:-4] + '_zip.txt')


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func


root = tk.Tk()
root.title('Trivial Compression')
root.geometry('400x300+350+200')
root.resizable(False, False)
tk.Label(root, text='Enter your file path', font=('Arial', 15)).pack()
path = tk.Entry(root)
path.pack()

tk.Label(root, text='What do you want to do this file', font=('Arial', 20)).pack()

compress_is = tk.IntVar()
tk.Radiobutton(root, text='Compression', variable=compress_is, value=1).pack()
tk.Radiobutton(root, text='Decompression', variable=compress_is, value=0).pack()

start = tk.Button(root, text='Start', command=combine_funcs(get_path, exit))
start.pack()

root.mainloop()
