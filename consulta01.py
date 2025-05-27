from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from clases import *

from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()



entregas_arte = session.query(Entrega).join(Entrega.tarea).join(Tarea.curso).join(Curso.departamento).join(Curso.instructor).join(Entrega.estudiante).filter(Departamento.nombre == "Arte").all()

for entrega in entregas_arte:
    print(f"PRESENTAR: {entrega.tarea.titulo} Estudiante: {entrega.estudiante.nombre} Calificación: {entrega.calificacion} Instructor: {entrega.tarea.curso.instructor.nombre} Departamento: {entrega.tarea.curso.departamento.nombre}")