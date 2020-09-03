

def loading_files_errors(model, vectorizer, level):
    error = ""
    if not model:
        error += "model"
    if not model and not vectorizer:
        error += " and "
    if not vectorizer:
        error += "vectorizer"
    if not model or not vectorizer:
        error += " not loaded for level "+str(level)
    print("\n"+error+"\n")
    return error
