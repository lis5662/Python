def ensure_correct_info(*args):
    print(args)
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Note sure who you are"

ensure_correct_info() # Not sure who you are

ensure_correct_info(1, True, "Steele", "Colt")