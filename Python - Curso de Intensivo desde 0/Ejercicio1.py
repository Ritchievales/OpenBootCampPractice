import os

def printFilesInDirectory(directory):
    content = os.listdir(directory)

    for element in content:
        path = os.path.join(directory, element)
        if os.path.isfile(path):
            file_size = getSize(os.path.getsize(path))
            print(file_size, element)
        elif os.path.isdir(path):
            printFilesInDirectory(path)

def getSize(bytes):
    values = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while bytes >= 1024 and index < len(values) -1:
        bytes = bytes/1024
        index += 1
    return f"{bytes:.2f} {values[index]}"

if __name__ == "__main__":
    directory = os.path.expanduser("~/Downloads")
    printFilesInDirectory(directory)
