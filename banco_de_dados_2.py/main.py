import os
from sqlalchemy import Integer, create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Setup database
db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    ra = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    idade = Column(String)
    email = Column(String)

    def __init__(self, ra: int, nome: str, idade: str, email: str) -> None:
        self.ra = ra
        self.nome = nome
        self.idade = idade
        self.email = email

# Create the database tables
Base.metadata.create_all(bind=db)

# Input loop to add alunos
for i in range(2):
    ra = int(input("Digite seu RA: "))  # Changed to int
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu email: ")

    aluno = Aluno(ra=ra, nome=nome, idade=idade, email=email)
    session.add(aluno)

# Commit the session once after all additions
session.commit()

# Query and print all alunos
lista_alunos = session.query(Aluno).all()
for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.idade} - {aluno.email}")
