from .examples import news_content, comments_content, example_terms


tree_name = "test_comments10"

# TREE LEVEL 0

cluster0_level0 = {
    "num_children" : 0,
    "terms" : "['currar', 'ir', 'guardo', '310']",
    "reference_doc": "#310 No. Las guardo para cuando tenga que ir a currar.",
    "documents": [
        '#4 Cuéntame tu,  a mi no me consta.',
        '!Brutal! {lol}',
        '#310 No. Las guardo para cuando tenga que ir a currar.',
        'Pantomima Full - Gatos.\nhttps://youtu.be/8kbXfAuvdxA'],
    "children": []
}

cluster1_level0 = {
    "num_children" : 0,
    "terms" : "['elegantemente', 'melón', 'abrir', 'forma', 'evidente', 'peor', 'niegan', 'si', '21']",
    "reference_doc": "#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...",
    "documents": [
        '#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...'],
    "children": []
}

cluster2_level0 = {
    "num_children" : 0,
    "terms" : "['chalao', 'dices', 'anticuerpos', 'transpasar', '355']",
    "reference_doc": "#355 Transpasar anticuerpos? Que dices chalao...",
    "documents": [
        'basta jugar fallout para darse cuenta',
        '#355 Transpasar anticuerpos? Que dices chalao...'],
    "children": []
}

cluster3_level0 = {
    "num_children" : 0,
    "terms" : "['precios', 'suban', 'privadas', 'empresas', 'explícale', '13', 'hace']",
    "reference_doc": "#13 explícale que es la que hace que las empresas privadas no suban precios",
    "documents": [
        'Pero más allá del estado de alarma y sus publicaciones en el BOE, ¿qué ley han sacado ahora mismo que penalice o prohíba algo de esto?\n\nQue para eso hace falta el parlamento.',
        '#23 Pujol ya era expresidente antes que Torra llegara y le retiraron la pensión (injustamente)  hace unos años. No te enteras de nada. \n\n\nQuien sí la cobra es Montilla que es el origen de todos los problemas aunque no lo sepas porque no sabes nada anterior a 2010 (y de después la mitad). \n\n\nY también cobran los expresidentes de todas esas regiones  deficitarias e improductivas que tanto os gustan.\n\n\nPor cierto  , para sueldo subido el de Colau, ¿era el 40%?',
        '#13 explícale que es la que hace que las empresas privadas no suban precios'],
    "children": []
}

level0_terms = example_terms

tree_level0 = {
    "terms": level0_terms,
    "documents": comments_content,
    "predicted_clusters": [0, 0, 3, 0, 3, 2, 1, 2, 0, 3],
    "clusters": [ cluster0_level0, cluster1_level0, cluster2_level0, cluster3_level0 ],
}

# TREE LEVEL 1

cluster0_level1 = {
    "num_children" : 2,
    "terms" : "['elegantemente', 'melón', 'abrir', 'forma', 'evidente', 'peor', 'niegan', 'si', '21']",
    "reference_doc": "#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...",
    "documents": [
        "#310 No. Las guardo para cuando tenga que ir a currar.",
        "#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente..."
        ],
    "children": [ cluster0_level0, cluster1_level0 ]
}
cluster1_level1 = {
    "num_children" : 2,
    "terms" : "['chalao', 'dices', 'anticuerpos', 'transpasar', '355']",
    "reference_doc": "#355 Transpasar anticuerpos? Que dices chalao...",
    "documents": [
        "#355 Transpasar anticuerpos? Que dices chalao...",
        "#13 explícale que es la que hace que las empresas privadas no suban precios"
        ],
    "children": [ cluster2_level0, cluster3_level0 ]
}

level1_terms = ['13', '21', '310', '355', 'abrir', 'anticuerpos', 'chalao', 'currar', 'dices', 'elegantemente', 'empresas', 'evidente', 'explícale', 'forma', 'guardo', 'hace', 'ir', 'melón', 'niegan', 'peor', 'precios', 'privadas', 'si', 'suban', 'transpasar']

tree_level1 = {
    "terms": level0_terms,
    "documents": [
        "#310 No. Las guardo para cuando tenga que ir a currar.",
        "#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...",
        "#355 Transpasar anticuerpos? Que dices chalao...",
        "#13 explícale que es la que hace que las empresas privadas no suban precios"
        ],
    "clusters": [ cluster0_level1, cluster1_level1 ],
    "predicted_clusters": [0, 0, 1, 1],
}

example_tree = [tree_level0, tree_level1]

# DOCUMENTS CLUSTERS

documents_clusters_level0 = [
    {'document': comments_content[0], 'cluster_number': 0},
    {'document': comments_content[1], 'cluster_number': 0},
    {'document': comments_content[2], 'cluster_number': 3},
    {'document': comments_content[3], 'cluster_number': 0},
    {'document': comments_content[4], 'cluster_number': 3},
    {'document': comments_content[5], 'cluster_number': 2},
    {'document': comments_content[6], 'cluster_number': 1},
    {'document': comments_content[7], 'cluster_number': 2},
    {'document': comments_content[8], 'cluster_number': 0},
    {'document': comments_content[9], 'cluster_number': 3}]

documents_clusters_level1 = [
    {'document': cluster0_level1["documents"][0], 'cluster_number': 0},
    {'document': cluster0_level1["documents"][1], 'cluster_number': 0},
    {'document': cluster1_level1["documents"][0], 'cluster_number': 1},
    {'document': cluster1_level1["documents"][1], 'cluster_number': 1}]


example_documents_clusters = [ documents_clusters_level0, documents_clusters_level1 ]
