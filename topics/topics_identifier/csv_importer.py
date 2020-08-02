import csv, io
from topics_identifier.models import Document

# PROCESS DATA

def store_document(text, file_type):
    if file_type == "news":
        news = True
    else:
        news = False
    doc, created = Document.objects.get_or_create(content=text, is_news=news)
    if created:
        doc.save()

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

def process_csv_line(column, file_type):
    if file_type == "news":
        result = process_news(column)
        text = result["title"] + "\n" + result["content"]
        store_document(text, file_type)
    elif file_type == "comments":
        result = process_comment(column)
        store_document(result["content"], file_type)
    else:
        result = "File type "+ str(file_type) + " not recognised"
    return result

def show_progress(num_register, total):
    completed = 100.0 * num_register / total
    progress = str(num_register)+" of "+str(total)+" registers. "+str(completed)+"% completed"
    print(progress)
    return progress

def process_data(csv_reader, file_type, total_num_registers):
    result = []
    num_register = 1
    for column in csv_reader:
        r = process_csv_line(column, file_type)
        result.append(r)
        show_progress(num_register, total_num_registers)
        num_register += 1
    return result


# IDENTIFY FILE TYPE

def get_headers_types():
    headers_types = [
        {"file_type":"comments", "header": '"comment_id","comment_link_id","comment_user_id","comment_date","comment_content"'},
        {"file_type":"news", "header": '"link_id","link_author","link_date","link_uri","link_url_title","link_title","link_content"'},
        {"file_type":"news2", "header": '"link_author","link_id","link_date","link_uri","link_url_title","link_title","link_content"'},
    ]
    return headers_types

def get_file_type(header):
    file_type = "incorrect"
    headers_types = get_headers_types()
    for header_type in headers_types:
        if header_type["header"] in header:
            file_type = header_type["file_type"]
    if file_type == "news2":
        file_type = "news"
    return file_type


# READ AND PROCESS CSV FILE

def get_csv_reader_and_header(file_content):
    io_string = io.StringIO(file_content)
    header = next(io_string)
    csv_reader = csv.reader(io_string, delimiter=',', quotechar='"')
    return csv_reader, header

def get_number_of_registers(file_content):
    csv_reader, _ = get_csv_reader_and_header(file_content)
    registers = sum(1 for row in csv_reader)
    return registers

def process_csv(file):
    file_content = file.read().decode('UTF-8')
    csv_reader, header = get_csv_reader_and_header(file_content)
    file_type = get_file_type(header)
    if file_type == "incorrect":
        result = ["Incorrect file type"]
    else:
        num_registers = get_number_of_registers(file_content)
        print("\nProcessing "+file_type+" csv file with "+str(num_registers)+" registers.")
        result = process_data(csv_reader, file_type, num_registers)
    return result
