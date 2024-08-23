def Debug(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(args, kwargs)
            print(str(e))

    return wrapper
