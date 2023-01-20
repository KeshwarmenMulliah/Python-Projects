import imapclient
import schedule
import time

def check_email():
    #Getting the object that connects to the server
    imap_obj = imapclient.IMAPClient('imap.gmail.com',ssl=True)

    #Logging in 
    imap_obj.login('keshwarmenmulliah@gmail.com', 'acenixrntkzgnnhz')

    imap_obj.select_folder('INBOX', readonly=True)
    UIDs = imap_obj.search(['UNSEEN'])
    if len(UIDs) != 0:
        new_em = True 
    else:
        new_em = False

schedule.every(5).minutes.do(check_email)

while True:
    schedule.run_pending()
    time.sleep(1)
