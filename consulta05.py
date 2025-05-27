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

#seleccion un titulo de un curso luego calculo el promedio de la calificacion despues uno la tabla de curso con la tabla de tarea
#despues unos la taba detarea cib ka de entrega y agrupo los resultados por titulo y asi calculo el promedio
resultados = session.query(Curso.titulo, func.avg(Entrega.calificacion)).join(Curso.tareas).join(Tarea.entregas).group_by(Curso.titulo).all()
#presento datos con el for
for titulo, promedio in resultados:
    print(f"Curso: {titulo} - Promedio calificaciones entregas: {promedio:.2f}")
