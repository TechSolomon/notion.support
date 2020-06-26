# Notion Support
#
# An automated support ticket and issue tracker for Notion.so
# Website: https://www.notion.support/

# Importing libraries
import imaplib, email, os, datetime, dotenv, email.header

dotenv.load_dotenv(".env/environment.env")
imap_url = "imap.gmail.com"


def process_mailbox(M):
    """
    Do something with emails messages in the folder.  
    For the sake of this example, print some headers.
    """
    rv, data = M.search(None, "ALL")
    if rv != "OK":
        print("No messages found!")
        return
    for num in data[0].split():
        rv, data = M.fetch(num, "(RFC822)")
        if rv != "OK":
            print("ERROR getting message", num)
            return
        msg = email.message_from_string(data[0][1].decode())
        decode = email.header.decode_header(msg["Subject"])[0]
        subject = decode[0]
        print("Message %s: %s" % (num, subject))
        print("Raw Date:", msg["Date"])
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg["Date"])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple)
            )
            print("Local Date:", local_date.strftime("%a, %d %b %Y %H:%M:%S"))


def get_mailbox_contents(mailbox):
    rv, data = con.select(mailbox)

    if rv == "OK":
        print("processing mailbox ¯\_(ツ)_/¯ \n")
        process_mailbox(con)
    else:
        print("-=-=-=-=-=-=-=-=-=-=-")
        print("(╯°□°）╯︵ ┻━┻")
        print(rv)
        print("-=-=-=-=-=-=-=-=-=-=-")
        print(data)
        print("-=-=-=-=-=-=-=-=-=-=-")


# this is done to make SSL connnection with GMAIL
con = imaplib.IMAP4_SSL(imap_url)

# logging the user in
con.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))

# unpacking tuple of two items
rv, mailboxes = con.list()

if rv == "OK":
    print("mailboxes: ")
    for mailbox in mailboxes:
        mailbox = mailbox.decode()
        print(mailbox + "\n")

    get_mailbox_contents('"INBOX"')

# Example Email: email@example.com
print("Notion Support")
