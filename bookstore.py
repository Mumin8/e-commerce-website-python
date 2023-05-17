import sys
import time
import Session


try:
    session = Session.Session(1)
except Session.SessionError as message:
    time.sleep(1)
    Session.redirect("bookstore.py")
    sys.exit()
nextPage = "allBooks.py? ID=%s" % session["ID"]
session.saveSession()
Session.redirect(nextPage)
