import csv, io
from .input_output_files import store_text_in_file, count_existing_files

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

def process_csv_line(column, file_type, data_name, file_number):
    if file_type == "news":
        result = process_news(column)
        text = result["title"] + "\n" + result["content"]
        store_text_in_file(text, file_type, data_name, file_number)
    elif file_type == "comments":
        result = process_comment(column)
        store_text_in_file(result["content"], file_type, data_name, file_number)
    else:
        result = "File type "+ str(file_type) + " not recognised"
    return result

def process_data(csv_reader, file_type, data_name, total_num_registers):
    result = []
    existing_files = count_existing_files(type=file_type)
    file_number = existing_files + 1
    for column in csv_reader:
        r = process_csv_line(column, file_type, data_name, file_number)
        result.append(r)
        register = file_number - existing_files
        completed = 100.0 * register / total_num_registers
        print(str(register)+" of "+str(total_num_registers)+" registers. "+str(completed)+"% completed")
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
        data_name = file.name.split('.')[0]
        num_registers = get_number_of_registers(file_content)
        print("\nProcessing "+file_type+" csv file with "+str(num_registers)+" registers.")
        result = process_data(csv_reader, file_type, data_name, num_registers)
    return result
