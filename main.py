# imports
import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

# load our environment variables for sensitive content
load_dotenv()

# get variables needed
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASSWD = os.getenv("GMAIL_PASSWD")
GOODNOTES_MAIL = os.getenv("GOODNOTES_MAIL")
EXPORT_DIR = os.getenv("EXPORT_DIR")

# check for file in hasImported.txt file
def hasImported(fileName):
    with open("hasImported.txt", 'rb') as file:
        # read the file
        for line in file.readlines():
            # convert line (class byte) to class str using utf-8
            str_line = line.decode("utf-8");
            # if it contains it, return true
            if fileName in str_line:
                print(f'{fileName} already in exported list')
                return True

    # if it doesn't contain it, add it to the file, return false
    with open("hasImported.txt", "a") as file:
        file.write(f'{fileName}\n')
        print(f'{fileName} added to exported list')
        return False

# send mail through gmail
def sendMail(msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(GMAIL_USER, GMAIL_PASSWD)
        smtp.send_message(msg)
        print("Message sent!")


if __name__ == "__main__":
    # get files
    files = os.listdir(EXPORT_DIR)
    for file in files:
        if not hasImported(file):
            msg = EmailMessage()
            msg['Subject'] = f'Sending {file} to GoodNotes'
            msg['From'] = GMAIL_USER
            msg['To'] = GOODNOTES_MAIL

            with open(f'{EXPORT_DIR}/{file}', 'rb') as f:
                file_data = f.read()
                file_name = file

            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            sendMail(msg)
