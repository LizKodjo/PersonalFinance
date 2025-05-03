from model.user import User

# fake data till I create database
_users = [
    User(fullname="Tom Jones", email="test@test.com"),
    User(fullname="Joe Bloggs", email="joe@test.com")
]


def get_all() -> list[User]:
    """Return all users"""
    return _users


def get_one(id: int) -> User | None:
    for _user in _users:
        if _user.id == id:
            return _user
    return None

# stubs


def create(user: User) -> User:
    """Add an User"""
    return user


def modify(user: User) -> User:
    """Partially modify a user"""
    return user


def replace(user: User) -> User:
    """Completely replace a user"""
    return user


def delete(id: int) -> bool:
    """Delete a user; return None if it existed"""
    return None
