import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///biblioteca.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Obras(Base):
    __tablename__ = 'obras'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), index=True)
    editora = Column(String(150))
    autor = Column(String(200))
    foto = Column(String(250))
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self) -> str:
        return '<Obras {titulo}>'.format(titulo=self.titulo)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
