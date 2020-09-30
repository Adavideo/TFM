from .example_documents import comments_content, news_content

news_titles = [
    '''El Gobierno aprueba el Ingreso Mínimo y dará hasta 1.015 euros a 850.000 familias''',
    '''Ayuso denuncia que Madrid ha estado "infrafinanciada" e "infradotada" de material,Sobre las elevadas cifras de fallecimientos en las residencias ha argumentado que en la región "hay muchas más residencias" y "una mayor longevidad" que en el resto.''',
    '''África, el continente que Estados Unidos ignora''',
    '''¿Qué les habría pasado si hubiesen tenido que pagar su atención hospitalaria en un sistema privado?''',
    '''El coronavirus llega a los indios Navajo: una reserva registra más fallecidos que 13 Estados juntos''',
    '''El virus llega a los indios Navajo: una reserva registra más fallecidos que 13 estados juntos''',
    '''Sobredosis de azúcar (Documental)''',
    '''Los tribunales allanan la nacionalización de decenas de centrales hidroeléctricas''',
    '''Lo que aprendemos (y nos queda por aprender) de los gatos en el confinamiento''',
    '''Los coronavirus conocidos responsables de un resfriado podrían generar inmunidad también contra el Covid19 [DEU]''',
    '''El coronavirus golpea más fuerte en comunidades de judíos ultraortodoxos de Nueva York''',
    '''La situación es insostenible. Abandono para que los responsables de gobernar se hagan cargo de todo esto'''
]


news_uris = [
    "El-Gobierno-aprueba-el-Ingreso-Minimo",
    "ayuso-denuncia-madrid-ha-estado-infrafinanciada-infradotada",
]


# EXAMPLE THREADS

thread0_documents_content = [
    news_content[0],
    comments_content[0],
    comments_content[1],
]

thread0 = { "thread_number":0,
            "title": news_titles[0],
            "uri": news_uris[0],
            "documents_content": thread0_documents_content }

thread1_documents_content = [
    news_content[1],
    comments_content[2],
    comments_content[3],
]

thread1 = { "thread_number":1,
            "title": news_titles[1],
            "uri": news_uris[1],
            "documents_content": thread1_documents_content }

example_threads = [ thread0, thread1 ]

all_threads_content = [
    news_content[0],
    news_content[1],
    comments_content[0],
    comments_content[1],
    comments_content[2],
    comments_content[3],
]
