from pony import orm


def setup_db():
    db = orm.Database()
    db.bind(
        provider="postgres",
        user="stuffwell",
        password="stuffwell",
        host="localhost",
        port="5432",
        database="stuffwell",
    )
    return db
