from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, func
from sqlalchemy import or_, not_

from sqlalchemy import func
from clases import *
# bueno aqui importo las funciones
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
#creo las sesiones
Session = sessionmaker(bind=engine)
session = Session()

nombres_estudiantes = ["Jennifer Bolton", "Elaine Perez", "Heather Henderson", "Charles Harris"]

tareas = session.query(Tarea).join(Entrega).join(Estudiante).filter(Estudiante.nombre.in_(nombres_estudiantes)).all()

for tarea in tareas:
    print(f"Tarea: {tarea.titulo} -> Número de entregas: {len(tarea.entregas)}")