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
# consulto los objetos de tipo tarea luego lo uno con la tabla de entrega,estudiante y filtro los nombres con un in que me sirve para poner el arreglo de estudaintes que cree previamente.
tareas = session.query(Tarea).join(Entrega).join(Estudiante).filter(Estudiante.nombre.in_(nombres_estudiantes)).all()
#con el for presente los datos
for tarea in tareas:
    print(f"Tarea: {tarea.titulo} -> Número de entregas: {len(tarea.entregas)}")