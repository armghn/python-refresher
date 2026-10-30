class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('sample.txt', 'w') as f:
    f.write("This is a sample text")
    print(f.closed)    #must return False

#File will close here!

print(f.closed)   #must return True
