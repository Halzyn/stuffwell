from pony import orm

from db import setup_db

db = setup_db()


class User(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    discord_id = orm.Required(str)
    quotes = orm.Set("Quote")


class Quote(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    user = orm.Required(User)
    text = orm.Required(str)


db.generate_mapping(create_tables=True)


@orm.db_session
def list_quotes(discord_user):
    user = get_user(discord_user)
    result = []
    for quote in user.quotes:
        result.append(f"\n{quote.id}: {quote.text}")
    return "".join(result)


@orm.db_session
def add_quote(discord_user, text):
    user = get_user(discord_user)
    Quote(user=user, text=text)


def get_user(user):
    if User.exists(discord_id=str(user.id)):
        return User.get(discord_id=str(user.id))
    return User(discord_id=str(user.id))
