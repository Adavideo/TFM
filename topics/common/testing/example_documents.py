from .dates import get_date

example_date = get_date('2020-05-29 11:00:25')

example_author = 189575

news_content = [
    '''El Gobierno aprueba el Ingreso Mínimo y dará hasta 1.015 euros a 850.000 familias 100.000 de esos hogares serán los primeros en cobrarlo en junio. Habrá test de patrimonio y no computará la vivienda habitual. Sánchez suma otro hito.''',
    '''Ayuso denuncia que Madrid ha estado "infrafinanciada" e "infradotada" de material,Sobre las elevadas cifras de fallecimientos en las residencias ha argumentado que en la región "hay muchas más residencias" y "una mayor longevidad" que en el resto.''',
    '''A pesar de tener una numerosa población afroamericana descendiente de los esclavos llegados desde el siglo XVII, Estados Unidos no ha cultivado muchas relaciones con África y cuenta con pocos aliados en el continente. Washington ha mirado hacia África principalmente ante amenazas a su seguridad y por miedo a la creciente influencia de potencias rivales, pero no mantiene una estrategia integral ni ha conseguido labrar relaciones duraderas con los países africanos.''',
    '''Esta pandemia demuestra más que cualquier ideología o discurso la necesidad y la importancia ineludible de los bienes públicos : hospitales, investigación, educación ... Es decir, el valor de todo lo que no debe estar sujeto a la tiranía de la explotación y el beneficio.''',
    '''El espectro de la pandemia se cierne sobre una comunidad que se enfrenta a un sistema de salud con agujeros en la financiación crónicos, falta de personal y de hospitales y otros centros sanitarios, una mayor prevalencia de enfermedades preexistentes como la diabetes -en comparación con otras poblaciones-, y donde un tercio de los hogares no disponen siquiera de agua corriente y otros tantos no tienen ni electricidad ni acceso a Internet. Todo esto en la autodenominada Tierra del Progreso, Estados Unidos.''',
    '''El 80% de este ingrediente está oculto en los alimentos cotidianos, como los "saludables" cereales de desayuno, yogures, refrescos o comidas preparadas. Según los expertos el consumo de azúcar se puede convertir en una adicción. Para algunos médicos, el azúcar es tan peligroso como los cigarrillos, y la causa principal de una serie de enfermedades graves, como la obesidad infantil, la diabetes, enfermedades del corazón, hipertensión y muchos cánceres comunes. Sin embargo el lobby del azúcar niega cualquier relación entre azúcar y enfermedades''',
    '''La Audiencia dictamina que el límite de 75 años de las concesiones supone "un plazo máximo improrrogable" que, además, conlleva para las compañías la obligación de indemnizar al Estado si lo exceden, lo que avala la reversión del más de medio centenar de saltos hidráulicos cuyas autorizaciones caducan en los próximos años o lo han hecho en la última década.''',
    '''Por un lado, su forma de relajarse, de estar tranquilos, de respirar. Y por otro, su habilidad para mantener una excelente forma física, aunque se muevan en muy poco espacio y tengan relativamente poca actividad, porque duermen mucho. Eso, al parecer, se debe a los estiramientos. El gato es un yogui que realiza la respiración y la meditación junto con estiramientos  que le mantienen en forma. Eso es lo que deberíamos tratar de imitar, ahora que estamos en casa y tenemos tiempo, ese ejercicio, esos estiramientos y esa relajación que producen.''',
    '''Según el virólogo residente en Berlín Christian Drosten, los infectados de covid19 leves o asintomáticos podrían estar asociados con infecciones previas con coronavirus responsables de resfriados que generaron una inmunidad previa.''',
    '''Hay explicaciones a esta alta tasa de infecciones: ritos milenarios de esta comunidad están tan enraizados en sus hábitos y costumbres que es innegociable modificarlos. Las tres oraciones diarias son comunitarias e imposible de soslayar, las reuniones en las sinagogas, sagradas. Casamientos y funerales son momentos multitudinarios. Hábitos transmitidos de generación en generación, de abuelos a padres y a hijos, que están en el centro mismo de la vida personal y comunitaria.''',
    '''El comedor vecinal del número 28 de Espíritu Santo llega a su fin. Tras más de 40 días de dar comida gratis a personas necesitadas Adrián Rojas, quien prendió la mecha de esta iniciativa, abandona harto de esperar una ayuda institucional que no llega. "No se puede combatir la crisis social generada por el coronavirus sólo con solidaridad ciudadana", afirma. Desde el viernes, 300 personas al día se quedarán sin su plato de comida caliente'''
]

comments_content = [
 '#4 Cuéntame tu,  a mi no me consta.',
 '!Brutal! {lol}',
 'Pero más allá del estado de alarma y sus publicaciones en el BOE, ¿qué ley han sacado ahora mismo que penalice o prohíba algo de esto?\n\nQue para eso hace falta el parlamento.',
 '#310 No. Las guardo para cuando tenga que ir a currar.',
 '#23 Pujol ya era expresidente antes que Torra llegara y le retiraron la pensión (injustamente)  hace unos años. No te enteras de nada. \n\n\nQuien sí la cobra es Montilla que es el origen de todos los problemas aunque no lo sepas porque no sabes nada anterior a 2010 (y de después la mitad). \n\n\nY también cobran los expresidentes de todas esas regiones  deficitarias e improductivas que tanto os gustan.\n\n\nPor cierto  , para sueldo subido el de Colau, ¿era el 40%?',
 'basta jugar fallout para darse cuenta',
 '#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...',
 '#355 Transpasar anticuerpos? Que dices chalao...',
 'Pantomima Full - Gatos.\nhttps://youtu.be/8kbXfAuvdxA',
 '#13 explícale que es la que hace que las empresas privadas no suban precios',
 'bla, bla']

example_documents = news_content

all_example_content = news_content + comments_content

example_reference_documents = [
    [ news_content[4], news_content[6], news_content[8] ],
    [ news_content[8] ]
]
