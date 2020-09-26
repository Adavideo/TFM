from .examples import news_content, example_documents


example_labeled_documents = news_content

example_documents_to_label = [
    '#4 Cuéntame tu,  a mi no me consta.',
    '!Brutal! {lol}',
    '#310 No. Las guardo para cuando tenga que ir a currar.',
    'basta jugar fallout para darse cuenta',
    '#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...',
    '#355 Transpasar anticuerpos? Que dices chalao...',
    'Pantomima Full - Gatos.\nhttps://youtu.be/8kbXfAuvdxA']

example_clusters_documents = example_documents_to_label + news_content
