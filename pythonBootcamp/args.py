def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Not sure who you are!"


print(ensure_correct_info("hello", "graham"))
print(ensure_correct_info(1, "Steele", True, "Colt"))
