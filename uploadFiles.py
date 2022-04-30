import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BDBd8fb4Lx808yOlJlDV3ScmUPHQFe8hEhLJJ2X789HjITP_-TpmzFVVwxn2nk8fJoWIbVGzYPGt1u4YYQAsj9McJdMC8-v5dFrdM5J--bwZPmGOYeDNc8Hx2NMOXfIqL8gv67SViOhV'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ") 



    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")
   


main()







	

	
	
