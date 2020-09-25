from .example_documents import comments_content, news_content

news_titles = [
    "El Gobierno aprueba el Ingreso Mínimo y dará hasta 1.015 euros a 850.000 familias",
    "Yo alucino con la obsesión de las terrazas"
]

news_uris = [
    "El-Gobierno-aprueba-el-Ingreso-Minimo",
    "Yo-alucino-con-la-obsesion-de-las-terrazas"
]


# EXAMPLE THREADS

thread0_documents_content = [
    news_content[0],
    comments_content[0],
    comments_content[1],
    comments_content[2],
    comments_content[3],
    comments_content[4],
]

thread0 = { "thread_number":0,
            "title": news_titles[0],
            "uri": news_uris[0],
            "documents_content": thread0_documents_content }

thread1_documents_content = [
    news_content[1],
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
    comments_content[4],
]
