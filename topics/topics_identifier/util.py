import os
texts_path = "data/texts/"
texts_import_path = texts_path+"to_classify/"
text_datasets_path = "data/text_datasets/"
clusters_path = "data/clusters/"

def count_existing_files(directory="", type=""):
    if not directory:
        if type == "text_dataset":
            directory = text_datasets_path
        else:
            directory = texts_import_path
    number_of_files = len(os.listdir(directory))
    return number_of_files

def store_file(filename, content):
    out_file = open(filename, 'w')
    out_file.write(content)
    out_file.close()

def store_text_in_file(text, file_number):
    filename = texts_import_path + "text" + str(file_number) + ".txt"
    store_file(filename, text)

def store_text_dataset(dataset):
    file_number = count_existing_files(text_datasets_path) + 1
    filename = text_datasets_path + "text_dataset" + str(file_number)
    store_file(filename, str(dataset))

def store_clustered_documents(clustered_documents):
    file_number = count_existing_files(clusters_path) + 1
    filename = clusters_path + "clusters_" + str(len(clustered_documents)) + "_" + str(file_number) + ".txt"
    out_file = open(filename, 'w')
    count = 0
    for cluster in clustered_documents:
        out_file.write("Cluster "+str(count)+". Terms: ")
        out_file.write(str(cluster["terms"])+"\n")
        for document in cluster["documents"]:
            out_file.write(document+"\n")
        out_file.write("\n")
        count += 1
    out_file.close()
