import gofile


def upload_file(file):
    server = gofile.getServer()
    print(f"The server is {server}")
