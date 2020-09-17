
def get_batch_options(documents_options, batch_number, size):
    if not documents_options["batches"] or not batch_number:
        batch_options = None
    else:
        batch_options = { "number": batch_number, "size": size }
    return batch_options

def get_number_of_batches(num_documents, size):
    num_batches = int(num_documents / size)
    if not ( num_documents % size ) == 0:
        num_batches += 1
    return num_batches
