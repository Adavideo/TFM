from config import batch_size


def get_number_of_batches(num_documents, size=batch_size):
    num_batches = int(num_documents / size)
    # Add one more batch when the division is not exact
    if not ( num_documents % size ) == 0:
        num_batches += 1
    print("Number of documents: "+str(num_documents)+" batches: "+str(num_batches))
    return num_batches

def get_batch_limits(batch_number, size=batch_size):
    end = size * batch_number
    start = end - size
    print("Batch "+str(batch_number)+" - starts at document "+str(start))
    return start, end
