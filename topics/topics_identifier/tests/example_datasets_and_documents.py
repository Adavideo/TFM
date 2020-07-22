
# DOCUMENTS

example_documents = [
    '#4 Cuéntame tu,  a mi no me consta.',
    '!Brutal! {lol}',
     'Pero más allá del estado de alarma y sus publicaciones en el BOE, ¿qué ley han sacado ahora mismo que penalice o prohíba algo de esto?\n\nQue para eso hace falta el parlamento.',
     '#310 No. Las guardo para cuando tenga que ir a currar.',
     '#23 Pujol ya era expresidente antes que Torra llegara y le retiraron la pensión (injustamente)  hace unos años. No te enteras de nada. \n\n\nQuien sí la cobra es Montilla que es el origen de todos los problemas aunque no lo sepas porque no sabes nada anterior a 2010 (y de después la mitad). \n\n\nY también cobran los expresidentes de todas esas regiones  deficitarias e improductivas que tanto os gustan.\n\n\nPor cierto  , para sueldo subido el de Colau, ¿era el 40%?',
     'basta jugar fallout para darse cuenta',
     '#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...',
     '#355 Transpasar anticuerpos? Que dices chalao...',
     'Pantomima Full - Gatos.\nhttps://youtu.be/8kbXfAuvdxA',
     '#13 explícale que es la que hace que las empresas privadas no suban precios']

# TREE

tree_name = "test_comments10"

# TREE LEVEL 0

cluster0_level0 = {
    "terms" : "['currar', 'ir', 'guardo', '310']",
    "reference_doc": "#310 No. Las guardo para cuando tenga que ir a currar.",
    "documents": ['#4 Cuéntame tu,  a mi no me consta.', '!Brutal! {lol}', '#310 No. Las guardo para cuando tenga que ir a currar.', 'Pantomima Full - Gatos.\nhttps://youtu.be/8kbXfAuvdxA']
}

cluster1_level0 = {
    "terms" : "['elegantemente', 'melón', 'abrir', 'forma', 'evidente', 'peor', 'niegan', 'si', '21']",
    "reference_doc": "#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...",
    "documents": ['#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...']
}

cluster2_level0 = {
    "terms" : "['chalao', 'dices', 'anticuerpos', 'transpasar', '355']",
    "reference_doc": "#355 Transpasar anticuerpos? Que dices chalao...",
    "documents": ['basta jugar fallout para darse cuenta', '#355 Transpasar anticuerpos? Que dices chalao...']
}

cluster3_level0 = {
    "terms" : "['precios', 'suban', 'privadas', 'empresas', 'explícale', '13', 'hace']",
    "reference_doc": "#13 explícale que es la que hace que las empresas privadas no suban precios",
    "documents": ['Pero más allá del estado de alarma y sus publicaciones en el BOE, ¿qué ley han sacado ahora mismo que penalice o prohíba algo de esto?\n\nQue para eso hace falta el parlamento.', '#23 Pujol ya era expresidente antes que Torra llegara y le retiraron la pensión (injustamente)  hace unos años. No te enteras de nada. \n\n\nQuien sí la cobra es Montilla que es el origen de todos los problemas aunque no lo sepas porque no sabes nada anterior a 2010 (y de después la mitad). \n\n\nY también cobran los expresidentes de todas esas regiones  deficitarias e improductivas que tanto os gustan.\n\n\nPor cierto  , para sueldo subido el de Colau, ¿era el 40%?', '#13 explícale que es la que hace que las empresas privadas no suban precios']
}

tree_level0 = {
    "description": "Test dataset with 10 documents",
    "terms": "['13', '2010', '21', '23', '310', '355', '40', '8kbxfauvdxa', 'abrir', 'ahora', 'alarma', 'allá', 'anterior', 'anticuerpos', 'aunque', 'años', 'basta', 'be', 'boe', 'brutal', 'chalao', 'cierto', 'cobra', 'cobran', 'colau', 'consta', 'cuenta', 'currar', 'cuéntame', 'darse', 'deficitarias', 'después', 'dices', 'elegantemente', 'empresas', 'enteras', 'evidente', 'explícale', 'expresidente', 'expresidentes', 'fallout', 'falta', 'forma', 'full', 'gatos', 'guardo', 'gustan', 'hace', 'https', 'improductivas', 'injustamente', 'ir', 'jugar', 'ley', 'llegara', 'lol', 'melón', 'mismo', 'mitad', 'montilla', 'niegan', 'origen', 'pantomima', 'parlamento', 'penalice', 'pensión', 'peor', 'precios', 'privadas', 'problemas', 'prohíba', 'publicaciones', 'pujol', 'regiones', 'retiraron', 'sabes', 'sacado', 'sepas', 'si', 'suban', 'subido', 'sueldo', 'todas', 'torra', 'transpasar', 'youtu']",
    "documents": example_documents,
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
        ]
}
cluster1_level1 = {
    "num_children" : 2,
    "terms" : "['chalao', 'dices', 'anticuerpos', 'transpasar', '355']",
    "reference_doc": "#355 Transpasar anticuerpos? Que dices chalao...",
    "documents": [
        "#355 Transpasar anticuerpos? Que dices chalao...",
        "#13 explícale que es la que hace que las empresas privadas no suban precios"
        ]
}

tree_level1 = {
    "name": tree_name,
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
