from django.core.files.uploadedfile import InMemoryUploadedFile


def mock_file(example_file):
    file = open(example_file["path"], 'r')
    in_memory_file = InMemoryUploadedFile(
                        file=file, field_name="file",
                        name=example_file["name"], content_type=example_file["type"],
                        size=example_file["size"], charset=example_file["charset"])
    return in_memory_file
