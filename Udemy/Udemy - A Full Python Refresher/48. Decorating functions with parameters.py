import functools
user = {"username": "jose", "access_level": "guest"}
# user = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args,**kwargs):
        if user["access_level"] == "admin":
            return func(*args,**kwargs)
        else:
            print(f"No admin permission for {user['username']}")

    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "supersecure_secure_passowrd"


print(get_password("billing"))
print(get_password.__name__)