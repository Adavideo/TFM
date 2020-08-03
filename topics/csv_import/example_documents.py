from .dates import get_date

# DOCUMENTS

example_documents = ['#4 Cuéntame tu,  a mi no me consta.', '!Brutal! {lol}',
 'Pero más allá del estado de alarma y sus publicaciones en el BOE, ¿qué ley han sacado ahora mismo que penalice o prohíba algo de esto?\n\nQue para eso hace falta el parlamento.',
 '#310 No. Las guardo para cuando tenga que ir a currar.',
 '#23 Pujol ya era expresidente antes que Torra llegara y le retiraron la pensión (injustamente)  hace unos años. No te enteras de nada. \n\n\nQuien sí la cobra es Montilla que es el origen de todos los problemas aunque no lo sepas porque no sabes nada anterior a 2010 (y de después la mitad). \n\n\nY también cobran los expresidentes de todas esas regiones  deficitarias e improductivas que tanto os gustan.\n\n\nPor cierto  , para sueldo subido el de Colau, ¿era el 40%?',
 'basta jugar fallout para darse cuenta',
 '#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...',
 '#355 Transpasar anticuerpos? Que dices chalao...',
 'Pantomima Full - Gatos.\nhttps://youtu.be/8kbXfAuvdxA',
 '#13 explícale que es la que hace que las empresas privadas no suban precios']

example_date = get_date('2020-05-29 11:00:25')

example_news = {
        "number": 3297522,
        "author": 189575,
        "date": example_date,
        "uri": 'valencia',
        "title": 'La Audiencia de València',
        "content": 'La Audiencia de València\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.'
    }
