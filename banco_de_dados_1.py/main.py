import os
from sqlalchemy import Integer, create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Creating the database
db = create_engine("sqlite:///meubanco.db")

# Connection with the database
Session = sessionmaker(bind=db)
session = Session()

# Creating base for declarative model
Base = declarative_base()

class Usuario(Base):
    # Defining table name
    __tablename__ = "usuarios"

    # Defining attributes of the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

# Creating the table in the database
Base.metadata.create_all(bind=db)

# Saving to the database
usuario = Usuario(nome="Marta", email="marta@gmail.com", senha="123")  # type: ignore
session.add(usuario)
session.commit()

# Showing content of the database
lista_usuarios = session.query(Usuario).all()  # type: ignore

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")
