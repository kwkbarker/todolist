import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pg8000

engine = create_engine(
    # connect to postgres cloud
    'postgresql://postgres:postgres@/cloudsql/barker-todolist:us-east4:todolist-db',
    # 'postgresql+pg8000://kwkbarker:kwkbarker@/todolist-db?unix_sock=/cloudsql/barker-todolist:us-east4:todolist-db/.s.PGSQL.5432',
    # # connect to sqlite db
    # 'sqlite:///todolist.db',

    # connect to postres cloud w/ URL.create
    # sqlalchemy.engine.url.URL.create(
    #     drivername="postgresql+pg8000",
    #     username='kwkbarker',
    #     password='kwkbarker',
    #     database='todolist-db',
    #     query={
    #         "unix-sock": "{}/{}/.s.PGSQL.5432".format(
    #             "/cloudsql",
    #             "barker-todolist:us-east4:todolist-db"
    #         )
    #     }
    # ), 
    convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()