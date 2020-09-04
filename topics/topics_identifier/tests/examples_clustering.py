from timeline.tests.example_documents import comments_content, news_content
from .example_trees import clusters_documents


example1 = {
    "documents": comments_content,
    "predicted_clusters": [0, 0, 3, 0, 3, 2, 1, 2, 0, 3],
    "clusters_documents": clusters_documents[0]
}

example1_documents = comments_content

example2_clusters_documents = [
    [],
    [],
    ['El Gobierno aprueba el Ingreso Mínimo y dará hasta 1.015 euros a 850.000 familias 100.000 de esos hogares serán los primeros en cobrarlo en junio. Habrá test de patrimonio y no computará la vivienda habitual. Sánchez suma otro hito.',
     'Yo alucino con la obsesión de las terrazas Ni colegios, ni residencias, ni ERTEs, ni ingreso mínimo vital, ni visitas a familiares, ni encuentros en casas y mucho menos bibliotecas o museos. Lo único que importa son las terrazas.'],
    []
]

example2 = {
    "documents": news_content,
    "clusters_documents": example2_clusters_documents,
    "predicted_clusters": [ 2, 2 ]
}
