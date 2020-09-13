default_document_limit = 10000
tree_name_max_length = 25
terms_max_length = 20000
reference_documents_max_length = 25000
max_tree_level = 1


def check_max_length(type, content):
    if type=="Reference document":
        max_length = reference_documents_max_length
    if type=="Terms":
        max_length = terms_max_length

    if (len(content)>max_length):
        print("\n"+type+" exceeds the limit of "+str(max_length))
        print("Length: "+str(len(content))+"\n")
