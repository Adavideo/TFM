from .examples import news_content, example_reference_documents, comments_content


tree_name = "test_comments10"

# TERMS
example_terms = ['000', '015', '100', '28', '300', '40', '75', '80', '850', 'abandona', 'abuelos', 'acceso', 'actividad', 'además', 'adicción', 'adrián', 'afirma', 'africanos', 'afroamericana', 'agua', 'agujeros', 'ahora', 'aliados', 'alimentos', 'alta', 'amenazas', 'aprueba', 'argumentado', 'asintomáticos', 'asociados', 'audiencia', 'aunque', 'autodenominada', 'autorizaciones', 'avala', 'ayuda', 'ayuso', 'azúcar', 'años', 'beneficio', 'berlín', 'bienes', 'caducan', 'caliente', 'casa', 'casamientos', 'causa', 'centenar', 'centro', 'centros', 'cereales', 'christian', 'cierne', 'cifras', 'cigarrillos', 'ciudadana', 'cobrarlo', 'combatir', 'comedor', 'comida', 'comidas', 'comparación', 'compañías', 'computará', 'comunes', 'comunidad', 'comunitaria', 'comunitarias', 'concesiones', 'conlleva', 'conseguido', 'consumo', 'continente', 'convertir', 'corazón', 'coronavirus', 'corriente', 'costumbres', 'cotidianos', 'covid19', 'creciente', 'crisis', 'crónicos', 'cualquier', 'cuenta', 'cultivado', 'cuyas', 'cánceres', 'dar', 'dará', 'debe', 'deberíamos', 'decir', 'demuestra', 'denuncia', 'desayuno', 'descendiente', 'diabetes', 'diarias', 'dictamina', 'discurso', 'disponen', 'drosten', 'duermen', 'duraderas', 'década', 'día', 'días', 'educación', 'ejercicio', 'electricidad', 'elevadas', 'embargo', 'enfermedades', 'enfrenta', 'enraizados', 'esclavos', 'espacio', 'espectro', 'esperar', 'espíritu', 'estiramientos', 'estrategia', 'euros', 'exceden', 'excelente', 'expertos', 'explicaciones', 'explotación', 'fallecimientos', 'falta', 'familias', 'fin', 'financiación', 'forma', 'funerales', 'física', 'gato', 'generación', 'generada', 'generaron', 'gobierno', 'gratis', 'graves', 'habilidad', 'habitual', 'hacia', 'harto', 'hecho', 'hidráulicos', 'hijos', 'hipertensión', 'hito', 'hogares', 'hospitales', 'hábitos', 'ideología', 'imitar', 'importancia', 'imposible', 'improrrogable', 'indemnizar', 'ineludible', 'infantil', 'infecciones', 'infectados', 'influencia', 'infradotada', 'infrafinanciada', 'ingrediente', 'ingreso', 'iniciativa', 'inmunidad', 'innegociable', 'institucional', 'integral', 'internet', 'investigación', 'junio', 'junto', 'labrar', 'lado', 'leves', 'llega', 'llegados', 'lobby', 'longevidad', 'límite', 'madrid', 'mantener', 'mantiene', 'mantienen', 'material', 'mayor', 'mecha', 'medio', 'meditación', 'miedo', 'milenarios', 'mirado', 'mismo', 'modificarlos', 'momentos', 'muchas', 'muevan', 'multitudinarios', 'máximo', 'médicos', 'mínimo', 'necesidad', 'necesitadas', 'niega', 'numerosa', 'número', 'obesidad', 'obligación', 'oculto', 'oraciones', 'padres', 'pandemia', 'parecer', 'patrimonio', 'países', 'peligroso', 'personal', 'personas', 'pesar', 'plato', 'plazo', 'poblaciones', 'población', 'poca', 'pocos', 'podrían', 'potencias', 'preexistentes', 'prendió', 'preparadas', 'prevalencia', 'previa', 'previas', 'primeros', 'principal', 'principalmente', 'producen', 'progreso', 'próximos', 'puede', 'públicos', 'quedarán', 'realiza', 'refrescos', 'región', 'relaciones', 'relación', 'relajación', 'relajarse', 'relativamente', 'resfriados', 'residencias', 'residente', 'respiración', 'respirar', 'responsables', 'resto', 'reuniones', 'reversión', 'ritos', 'rivales', 'rojas', 'sagradas', 'saltos', 'salud', 'saludables', 'sanitarios', 'santo', 'seguridad', 'según', 'serie', 'si', 'siglo', 'sinagogas', 'siquiera', 'sistema', 'social', 'solidaridad', 'soslayar', 'sujeto', 'suma', 'supone', 'sánchez', 'sólo', 'tan', 'tantos', 'tasa', 'tener', 'tercio', 'test', 'tiempo', 'tierra', 'tiranía', 'tranquilos', 'transmitidos', 'tras', 'tratar', 'tres', 'unidos', 'valor', 'vecinal', 'vida', 'viernes', 'virólogo', 'vivienda', 'washington', 'xvii', 'yogui', 'yogures', 'áfrica', 'última']

level0_terms = example_terms
level1_terms = ['75', 'acceso', 'además', 'agua', 'agujeros', 'asintomáticos', 'asociados', 'audiencia', 'autodenominada', 'autorizaciones', 'avala', 'años', 'berlín', 'caducan', 'centenar', 'centros', 'christian', 'cierne', 'comparación', 'compañías', 'comunidad', 'concesiones', 'conlleva', 'coronavirus', 'corriente', 'covid19', 'crónicos', 'cuyas', 'diabetes', 'dictamina', 'disponen', 'drosten', 'década', 'electricidad', 'enfermedades', 'enfrenta', 'espectro', 'exceden', 'falta', 'financiación', 'generaron', 'hecho', 'hidráulicos', 'hogares', 'hospitales', 'improrrogable', 'indemnizar', 'infecciones', 'infectados', 'inmunidad', 'internet', 'leves', 'límite', 'mayor', 'medio', 'máximo', 'obligación', 'pandemia', 'personal', 'plazo', 'poblaciones', 'podrían', 'preexistentes', 'prevalencia', 'previa', 'previas', 'progreso', 'próximos', 'resfriados', 'residente', 'responsables', 'reversión', 'saltos', 'salud', 'sanitarios', 'según', 'si', 'siquiera', 'sistema', 'supone', 'tantos', 'tercio', 'tierra', 'unidos', 'virólogo', 'última']

# LEVEL DOCUMENTS
level0_documents = news_content
level1_documents = [ news_content[4], news_content[6], news_content[8] ]

tree_documents = [ level0_documents, level1_documents ]

# PREDICTED CLUSTERS

example_predicted_clusters_level0 = [0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 2]
example_predicted_clusters_level1 = [0, 0, 0]
example_predicted_clusters = [ example_predicted_clusters_level0, example_predicted_clusters_level1 ]


# CLUSTERS DOCUMENTS

documents_cluster0_level0 = [
    news_content[0], news_content[1], news_content[2],
    news_content[3], news_content[4], news_content[5],
    news_content[7], news_content[9]
]

documents_cluster1_level0 = [ news_content[6] ]

documents_cluster2_level0 = [ news_content[8], news_content[10] ]

documents_cluster0_level1 = level1_documents

clusters_documents_level0 = [ documents_cluster0_level0, documents_cluster1_level0 , documents_cluster2_level0 ]
clusters_documents_level1 = [ documents_cluster0_level1 ]
clusters_documents = [ clusters_documents_level0, clusters_documents_level1 ]


# LEVEL 0 CLUSTERS

cluster0_level0 = {
    "num_cluster": 0,
    "num_children" : 0,
    "terms" : "['progreso', 'tierra', 'autodenominada', 'internet', 'acceso', 'electricidad', 'tantos', 'corriente', 'agua', 'siquiera', 'disponen', 'tercio', 'poblaciones', 'comparación', 'diabetes', 'preexistentes', 'enfermedades', 'prevalencia', 'sanitarios', 'centros', 'personal', 'falta', 'crónicos', 'financiación', 'agujeros', 'salud', 'sistema', 'enfrenta', 'comunidad', 'cierne', 'espectro', 'hospitales', 'pandemia', 'unidos', 'mayor', 'hogares']",
    "reference_doc": example_reference_documents[0][0],
    "documents": documents_cluster0_level0,
    "children": []
}

cluster1_level0 = {
    "num_cluster": 1,
    "num_children" : 0,
    "terms" : "['década', 'última', 'hecho', 'próximos', 'caducan', 'autorizaciones', 'cuyas', 'hidráulicos', 'saltos', 'centenar', 'medio', 'reversión', 'avala', 'exceden', 'si', 'indemnizar', 'obligación', 'compañías', 'conlleva', 'además', 'improrrogable', 'máximo', 'plazo', 'supone', 'concesiones', 'años', '75', 'límite', 'dictamina', 'audiencia']",
    "reference_doc": example_reference_documents[0][1],
    "documents": documents_cluster1_level0,
    "children": []
}

cluster2_level0 = {
    "num_cluster": 2,
    "num_children" : 0,
    "terms" : "['previa', 'inmunidad', 'generaron', 'resfriados', 'responsables', 'coronavirus', 'previas', 'infecciones', 'asociados', 'podrían', 'asintomáticos', 'leves', 'covid19', 'infectados', 'drosten', 'christian', 'berlín', 'residente', 'virólogo', 'según']",
    "reference_doc": example_reference_documents[0][2],
    "documents": documents_cluster2_level0,
    "children": []
}


# LEVEL 1 CLUSTERS

cluster0_level1 = {
    "num_cluster": 0,
    "num_children" : 3,
    "terms" : "['previa', 'inmunidad', 'generaron', 'resfriados', 'responsables', 'coronavirus', 'previas', 'infecciones', 'asociados', 'podrían', 'asintomáticos', 'leves', 'covid19', 'infectados', 'drosten', 'christian', 'berlín', 'residente', 'virólogo', 'según']",
    "reference_doc": example_reference_documents[1][0],
    "documents": documents_cluster0_level1,
    "children": [ cluster0_level0, cluster1_level0, cluster2_level0 ]
}


# REFERENCE DOCUMENTS

example_reference_documents = [
    level1_documents,
    [ cluster0_level1["reference_doc"] ]
]


# TREES

tree_level0 = {
    "terms": level0_terms,
    "documents": level0_documents,
    "predicted_clusters": example_predicted_clusters_level0,
    "clusters": [ cluster0_level0, cluster1_level0, cluster2_level0 ],
    "reference_documents": example_reference_documents[0]
}

tree_level1 = {
    "terms": level1_terms,
    "documents": level1_documents,
    "clusters": [ cluster0_level1 ],
    "predicted_clusters": example_predicted_clusters_level1,
    "reference_documents": example_reference_documents[1]
}

example_tree = [tree_level0, tree_level1]


comments_clusters = [
    { "documents": comments_content[:8] } ,
    { "documents": [ comments_content[8] ] },
    { "documents": comments_content[9:11] }
]
