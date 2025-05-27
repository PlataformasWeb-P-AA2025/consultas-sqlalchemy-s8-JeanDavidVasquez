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

# consulto los objetos de tipo departamento luego lo uno con la tabla de curso,tarea y entrega y los filtro los que son menores a 0.3
resultados = session.query(Departamento).join(Curso).join(Tarea).join(Entrega).filter(Entrega.calificacion <= 0.3).all()
#los presento con el for y el len es para contar cuantos cuersos tiene ese departamento
for departamento in resultados:
    print(f"Departamento: {departamento.nombre} - Número de cursos: {len(departamento.cursos)}")
