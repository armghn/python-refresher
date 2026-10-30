from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        my_file = open(file, mode)    # = __enter__ method of class
        yield my_file                 # Yield the file object to the with block, then resume execution when the block finishes.
    finally:
        my_file.close()               # = __exit__ method of class


with open("sample.txt", "w") as f:
    f.write("Hello! This is a sample text!")
    print(f.closed)

print(f.closed)