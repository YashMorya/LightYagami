from LightYagami import DB_URI
from SQLAlchemy import create_engine
from SQLAlchemy.ext.declarative import declarative_base
from SQLAlchemy.orm import scoped_session, sessionmaker


def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
