import csv, io
from datetime import datetime
from config import headers_types
from timeline.models import Document, Thread, Topic
from metrics.models import TopicAnnotation


# PROCESS DATA

def save_duplicated_document(info):
    filename = "duplicates.txt"
    out_file = open(filename, 'a')
    print("Duplicated document:")
    print(info)
    out_file.write(str(info)+"\n")
    out_file.close()

def document_exist(info):
    doc_search = Document.objects.filter(content=info["content"])
    if doc_search: return True
    else: return False

def store_document(info, is_news):
    doc_search = Document.objects.filter(content=info["content"])
    if document_exist(info):
        save_duplicated_document(info)
    else:
        doc = Document(content=info["content"], is_news=is_news, date=info["date"], author=info["author"])
        doc.assign_thread(info)

def clean_text(text):
    quotes = "&quot;"
    cleaned_text = text.replace(quotes,'"')
    return cleaned_text

def process_date(date_string):
    date = datetime.fromisoformat(date_string)
    date_without_timezone = date.astimezone(tz=None)
    return date_without_timezone

def process_news(column):
    # link_id,link_author,link_date,link_uri,link_url_title,link_title,link_content
    info = {}
    info["thread_number"] = int(clean_text(column[0]))
    info["author"] = int(clean_text(column[1]))
    info["date"] = process_date(column[2])
    info["uri"] = clean_text(column[3])
    info["title"] = clean_text(column[5])
    info["content"] = clean_text(column[5]) + "\n" + clean_text(column[6])
    store_document(info, is_news=True)
    return info

def process_comment(column):
    # "comment_id","comment_link_id","comment_user_id","comment_date","comment_content"
    info = {}
    info["thread_number"] = int(clean_text(column[1]))
    info["author"] = int(clean_text(column[2]))
    info["date"] = process_date(column[3])
    info["content"] = clean_text(column[4])
    store_document(info, is_news=False)
    return info

def process_topic_annotation(column):
    title = clean_text(column[0])
    content = clean_text(column[1])
    document = Document.objects.get(content=title+ "\n" + content)
    topic_name = column[2]
    topic = Topic.objects.get(name=topic_name)
    label = (column[3]=="x" or column[3]=="X")
    annotator = int(column[4])
    annotation, created = TopicAnnotation.objects.get_or_create(topic=topic,document=document,label=label,annotator=annotator)
    if created: annotation.save()
    else: print("\nWARNING: Annotation duplicated.\n\n"+str(column)+"\n\n"+str(annotation)+"\n")
    info = { "title": title, "content": content }
    return info

def process_csv_line(column, file_type):
    if file_type == "incorrect":
        return "File type "+ str(file_type) + " not recognised"
    if file_type == "news":
        info = process_news(column)
    elif file_type == "comments":
        info = process_comment(column)
    elif file_type == "topic_annotations":
        info = process_topic_annotation(column)
    return info

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

def get_file_type(header):
    file_type = "incorrect"
    for header_type in headers_types:
        if header_type["header"] in header:
            file_type = header_type["file_type"]
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
    if file_type == "incorrect": return ["Incorrect file type"]
    num_registers = get_number_of_registers(file_content)
    print("\nProcessing "+file_type+" csv file with "+str(num_registers)+" registers.")
    result = process_data(csv_reader, file_type, num_registers)
    return result
