# database.py
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Definindo o caminho para criar o banco de dados na pasta 'gerenciador_tarefas'
project_root = os.path.dirname(os.path.dirname(__file__))  # Sobe um nível acima de utilidadesCeV
db_path = os.path.join(project_root, 'gerenciador_tarefas.db')
engine = create_engine(f'sqlite:///{db_path}')
Base = declarative_base()

# Modelo de Tarefa
class Tarefa(Base):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)
    completa = Column(Boolean, default=False)

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Configuração da sessão
Session = sessionmaker(bind=engine)
session = Session()
