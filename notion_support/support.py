# Notion Support
#
# An automated support ticket and issue tracker for Notion.so 
# Website: https://www.notion.support/

import math
import random
import time

def main():
    console_log()
    email_event_handler()
    notion_communication()
    support_email_refresh()
    ticket_resolution()

def console_log():
    print("Notion.Support")

def email_event_handler():
    print("This is where the email will live.")

def notion_communication():
    print("How we talk with the unofficial Notion.so API.")

# Refreshed after X minutes and Y seconds.
def support_email_refresh():
    refresh_time = random.randint(1, 100)
    print("Refresh Time: " + str(refresh_time) + " seconds")

def ticket_resolution():
    ticket_number = 000
    print("Ticket #" + str(ticket_number) + " has been closed.")

main()
