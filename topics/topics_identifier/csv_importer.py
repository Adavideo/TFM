import csv, io
from .util import store_text_in_file, count_existing_files

# PROCESS DATA

def clean_text(text):
    quotes = "&quot;"
    cleaned_text = text.replace(quotes,'"')
    return cleaned_text

def process_news(column):
    title = clean_text(column[5])
    content = clean_text(column[6])
    result = { "title": title, "content": content}
    return result

def process_comment(column):
    content = clean_text(column[4])
    result = { "content": content}
    return result

def process_csv_line(column, file_type, file_number):
    if file_type == "news":
        result = process_news(column)
        text = result["title"] + "\n" + result["content"]
        store_text_in_file(text, file_number)
    elif file_type == "comments":
        result = process_comment(column)
        store_text_in_file(result["content"], file_number)
    else:
        result = "File type "+ str(file_type) + " not recognised"
    return result

def process_data(io_string, file_type):
    result = []
    file_number = count_existing_files(type="text") + 1
    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        r = process_csv_line(column, file_type, file_number)
        result.append(r)
        file_number += 1
    return result


# IDENTIFY FILE TYPE

def get_headers_types():
    headers_types = [ {"file_type":"news", "header": '"link_id","link_author","link_date","link_uri","link_url_title","link_title","link_content"'},
                      {"file_type":"comments", "header": '"comment_id","comment_link_id","comment_user_id","comment_date","comment_content"'},
                    ]
    return headers_types

def get_file_type(header):
    file_type = "incorrect"
    headers_types = get_headers_types()
    for header_type in headers_types:
        if header_type["header"] in header:
            file_type = header_type["file_type"]
    return file_type


# READ AND PROCESS CSV FILE

def process_csv(file):
    file_content = file.read().decode('UTF-8')
    io_string = io.StringIO(file_content)
    header = next(io_string)
    file_type = get_file_type(header)
    if file_type == "incorrect":
        result = ["Incorrect file type"]
    else:
        result = process_data(io_string, file_type)
    return result
