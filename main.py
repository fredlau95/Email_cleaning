import imaplib
import email
from email.header import decode_header

# account credentials
# change username to your email and pass
username='email-address'
password='Password'

# IMAP server for outlook/hotmail/live
server = 'outlook.office365.com'

# IMAP server for gmail/googlemail
# For connecting to gmail, you need to allow less secure apps or it wont work
# server = 'imap.gmail.com'

# create an IMAP4 class with SSL
M = imaplib.IMAP4_SSL(server)
# authenticate
M.login(username, password)


# show a list of available folders
print("Available folders: ")
folders = M.list()
print(folders)




# select SPAM folder
M.select('Junk')


typ, [data_ids] = M.search(None, 'ALL')

data_count = len(data_ids)
print("Number of emails: ", data_count)

if data_count == 0:
    print("No emails to delete")
else:
    if isinstance(data_ids, bytes):
        data_ids = data_ids.decode()

data_ids = ',' .join(data_ids.split(' '))


M.store(data_ids, '+FLAGS', '\\Deleted')

# Expunge the deleted emails
M.expunge()

M.close()
print("Logging out")

M.logout()




