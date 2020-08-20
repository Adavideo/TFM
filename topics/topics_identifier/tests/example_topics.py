from topics_identifier.models import Topic

# Examples of the result when clustering for the topic "prueba"

topic = Topic(name="prueba")

example_topics_cluster_terms = [
    ['importa', 'único', 'museos', 'bibliotecas', 'menos', 'casas', 'encuentros', 'familiares', 'visitas', 'vital', 'ertes', 'residencias', 'colegios', 'terrazas', 'obsesión', 'alucino', 'mínimo', 'ingreso'],
    ['parlamento', 'falta', 'hace', 'prohíba', 'penalice', 'mismo', 'ahora', 'sacado', 'ley', 'boe', 'publicaciones', 'alarma', 'allá'],
    ['currar', 'ir', 'guardo', '310']
]

example_reference_documents = [
    'Yo alucino con la obsesión de las terrazas Ni colegios, ni residencias, ni ERTEs, ni ingreso mínimo vital, ni visitas a familiares, ni encuentros en casas y mucho menos bibliotecas o museos. Lo único que importa son las terrazas.',
    'Pero más allá del estado de alarma y sus publicaciones en el BOE, ¿qué ley han sacado ahora mismo que penalice o prohíba algo de esto?\n\nQue para eso hace falta el parlamento.',
    '#310 No. Las guardo para cuando tenga que ir a currar.'
]
