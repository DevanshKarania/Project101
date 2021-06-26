import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "UepZXsOHZJIAAAAAAAAAAaN6Y4XEjKT7Vc6iWnFuJxtgTVVxlk4bRQmstXhuKFmV"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter file path to upload to dropbox: ")

    transferData.uploadFiles(file_from, file_to)
    print("File uploaded")

main()
