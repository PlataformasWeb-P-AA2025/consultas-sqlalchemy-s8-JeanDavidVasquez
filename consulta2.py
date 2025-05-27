from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from sqlalchemy import func
from clases import *

from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


resultados = session.query(Departamento).join(Curso).join(Tarea).join(Entrega).filter(Entrega.calificacion <= 0.3).all()

for departamento in resultados:
    print(f"Departamento: {departamento.nombre} - Número de cursos: {len(departamento.cursos)}")
