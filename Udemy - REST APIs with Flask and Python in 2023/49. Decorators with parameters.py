import functools
user = {"username": "jose", "access_level": "guest"}
# user = {"username": "jose", "access_level": "admin"}

def make_secure(acces_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args,**kwargs):
            if user["access_level"] == acces_level:
                return func(*args,**kwargs)
            else:
                print(f"No {acces_level} permission for {user['username']}")

        return secure_function

    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())
print("\n")

user = {"username": "anna", "access_level": "admin"}
print(get_admin_password())
print(get_dashboard_password())
print("\n")

user = {"username": "kuba", "access_level": "user"}
print(get_admin_password())
print(get_dashboard_password())