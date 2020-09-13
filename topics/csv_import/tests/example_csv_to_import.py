
csv_path = 'csv_import/tests/example.csv'
csv_name = "example.csv"
csv_size = 5467

csv_documents = [
'''Title: Ayuso denuncia que Madrid ha estado &quot;infrafinanciada&quot; e &quot;infradotada&quot; de material<br>
      Ayuso denuncia que Madrid ha estado &quot;infrafinanciada&quot; e &quot;infradotada&quot; de material
Sobre las elevadas cifras de fallecimientos en las residencias ha argumentado que en la región &quot;hay muchas más residencias&quot; y &quot;una mayor longevidad&quot; que en el resto.''',
'''Title: África, el continente que Estados Unidos ignora<br>
      África, el continente que Estados Unidos ignora
A pesar de tener una numerosa población afroamericana descendiente de los esclavos llegados desde el siglo XVII, Estados Unidos no ha cultivado muchas relaciones con África y cuenta con pocos aliados en el continente. Washington ha mirado hacia África principalmente ante amenazas a su seguridad y por miedo a la creciente influencia de potencias rivales, pero no mantiene una estrategia integral ni ha conseguido labrar relaciones duraderas con los países africanos.''',
'''Title: &quot;¿Qué les habría pasado si hubiesen tenido que pagar su atención hospitalaria en un sistema privado?&quot;<br>
      &quot;¿Qué les habría pasado si hubiesen tenido que pagar su atención hospitalaria en un sistema privado?&quot;
Esta pandemia demuestra más que cualquier ideología o discurso la necesidad y la importancia ineludible de los bienes públicos : hospitales, investigación, educación ... Es decir, el valor de todo lo que no debe estar sujeto a la tiranía de la explotación y el beneficio.''',
'''Title: El coronavirus llega a los indios Navajo: una reserva registra más fallecidos que 13 Estados juntos<br>
      El coronavirus llega a los indios Navajo: una reserva registra más fallecidos que 13 Estados juntos
El espectro de la pandemia se cierne sobre una comunidad que se enfrenta a un sistema de salud con agujeros en la financiación crónicos, falta de personal y de hospitales y otros centros sanitarios, una mayor prevalencia de enfermedades preexistentes como la diabetes -en comparación con otras poblaciones-, y donde un tercio de los hogares no disponen siquiera de agua corriente y otros tantos no tienen ni electricidad ni acceso a Internet. Todo esto en la autodenominada Tierra del Progreso, Estados Unidos.''',
'''Title: Sobredosis de azúcar (Documental)<br>
      Sobredosis de azúcar (Documental)
El 80% de este ingrediente está oculto en los alimentos cotidianos, como los &quot;saludables&quot; cereales de desayuno, yogures, refrescos o comidas preparadas. Según los expertos el consumo de azúcar se puede convertir en una adicción. Para algunos médicos, el azúcar es tan peligroso como los cigarrillos, y la causa principal de una serie de enfermedades graves, como la obesidad infantil, la diabetes, enfermedades del corazón, hipertensión y muchos cánceres comunes. Sin embargo el lobby del azúcar niega cualquier relación entre azúcar y enfermedades.''',
'''Title: Los tribunales allanan la nacionalización de decenas de centrales hidroeléctricas<br>
      Los tribunales allanan la nacionalización de decenas de centrales hidroeléctricas
La Audiencia dictamina que el límite de 75 años de las concesiones supone &quot;un plazo máximo improrrogable&quot; que, además, conlleva para las compañías la obligación de indemnizar al Estado si lo exceden, lo que avala la reversión del más de medio centenar de saltos hidráulicos cuyas autorizaciones caducan en los próximos años o lo han hecho en la última década.''',
'''Title: Lo que aprendemos (y nos queda por aprender) de los gatos en el confinamiento<br>
      Lo que aprendemos (y nos queda por aprender) de los gatos en el confinamiento
“Por un lado, su forma de relajarse, de estar tranquilos, de respirar. Y por otro, su habilidad para mantener una excelente forma física, aunque se muevan en muy poco espacio y tengan relativamente poca actividad, porque duermen mucho. Eso, al parecer, se debe a los estiramientos. El gato es un yogui que realiza la respiración y la meditación junto con estiramientos  que le mantienen en forma. Eso es lo que deberíamos tratar de imitar, ahora que estamos en casa y tenemos tiempo, ese ejercicio, esos estiramientos y esa relajación que producen.''',
'''Title: Los coronavirus conocidos responsables de un resfriado podrían generar inmunidad también contra el Covid19 [DEU]<br>
      Los coronavirus conocidos responsables de un resfriado podrían generar inmunidad también contra el Covid19 [DEU]
Según el virólogo residente en Berlín Christian Drosten, los infectados de covid19 leves o asintomáticos podrían estar asociados con infecciones previas con coronavirus responsables de resfriados que generaron una inmunidad previa.'''
]

example_csv = {
    "path": csv_path,
    "name": csv_name,
    "size": csv_size,
    "documents": csv_documents
}
