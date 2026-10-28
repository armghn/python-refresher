def run_on_zoj(f):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        now = datetime.now()
        minute = now.minute
        print(now)
        if minute % 2 == 0:
            f(*args, **kwargs)
        else:
            print("Shhh!")

    return wrapper

@run_on_zoj
def say_hello():
    print("Hello there!")

@run_on_zoj
def say_bye():
    print("Bye Bye!")


say_hello()
say_bye()