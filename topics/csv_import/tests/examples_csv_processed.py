from common.testing.dates import get_date

news_header = '''link_id,link_author,link_date,link_uri,link_url_title,link_title,link_content'''
#news_header = '''"link_id","link_author","link_date","link_uri","link_url_title","link_title","link_content"'''
comments_header = '''"comment_id","comment_link_id","comment_user_id","comment_date","comment_content"'''
incorrect_header_example = "comment_link_id","comment_date","comment_content","other_stuff"

news_example1 = ['3297522', '189575', '2020-04-24 19:45:33', 'valencia', 'Caso bla bla bla', 'La Audiencia de València bla bla bla', 'La Audiencia provincial de València Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.']
news_title1 = 'La Audiencia de València bla bla bla'
news_content1 = 'La Audiencia provincial de València Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

news_example_with_quotes = ['3297522', '189575', '2020-04-24 19:45:33', 'valencia', 'Caso bla bla bla', 'La Audiencia de &quot;València&quot; bla bla bla', 'La Audiencia provincial de &quot;València&quot; Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.']

news_title_with_quotes = 'La Audiencia de "València" bla bla bla'
news_content_with_quotes = 'La Audiencia provincial de "València" Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

comment_example1 = ['29610167', '3298601', '2831', '2020-04-26 02:54:45', '!Brutal! {lol}']
comment_content1 = '!Brutal! {lol}'

comment_example_with_quotes = ['29610167', '3298601', '2831', '2020-04-26 02:54:45', '!Brutal! &quot;{lol}']
comment_content_with_quotes = '!Brutal! "{lol}'


example_processed_news = {
    "thread_number": int(news_example1[0]),
    "author": int(news_example1[1]),
    "date": get_date(news_example1[2]),
    "uri": news_example1[3],
    "title": news_example1[5],
    "content": news_example1[5]+"\n"+news_example1[6]
}

processed_news_with_quotes = {
    "thread_number": int(news_example_with_quotes[0]),
    "author": int(news_example_with_quotes[1]),
    "date": get_date(news_example_with_quotes[2]),
    "uri": news_example_with_quotes[3],
    "title": news_title_with_quotes,
    "content": news_title_with_quotes+"\n"+news_content_with_quotes
}

# "comment_id","comment_link_id","comment_user_id","comment_date","comment_content"
comment_example1 = ['29610167', '3298601', '2831', '2020-04-26 02:54:45', '!Brutal! {lol}']

example_processed_comment = {
    "thread_number": int(comment_example1[1]),
    "author": int(comment_example1[2]),
    "date": get_date(comment_example1[3]),
    "content": comment_example1[4]
}
