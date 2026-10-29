def fun(m):
    for i in range(m):
        yield i


for n in fun(5):
    print(n)

def my_generator():
    yield "Hello world!!"
    yield "Python"

g = my_generator()
print(type(g))
print(next(g))
print(next(g))
for i in my_generator():
    print(i)

def inf_sequence():
    n = 0
    while True:
        yield n
        n+=1

g = inf_sequence()
for _ in range(10):
    print(next(g))


def is_even(a):
    for n in a:
        if n % 2 == 0:
            yield n


mylist = [2, 4, 5, 3, 7, 8]
print(list(is_even(mylist)))


def count_keyword(txt, keyword):
    for w in txt.split():
        if w == keyword:
            yield True


txt = "geeks for geeks"
s = count_keyword(txt, "geeks")
print(sum(s))



def count_up():
    for i in range(3):
        yield i

gen = count_up()
print(list(gen))