import gofile


def upload_file(file):
    server = gofile.getServer()
    print(f"The server is {server}")

    url = gofile.uploadFile(file)
    print(f"The link of the file is {url}")


if __name__ == "__main__":
    upload_file("exampleFile.txt")
