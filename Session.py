import os
import re
import pickle
import time
import hashlib
import json
from hashlib import md5
from flask import request
import user_agents as ua
from urllib.parse import urljoin
from collections import UserDict


browser_formats = [
        ('Chrome', 'html'),
        ('Firefox', 'html'),
        ('Safari', 'html'),
        ('Internet Explorer', 'html'),
        ('Edge', 'html'),
        ('Opera', 'html'),
        ('Android Browser', 'wml'),
        ('BlackBerry', 'wml')
        ]

env_dict = {
        "HTTP_USER_AGENT": os.environ.get("HTTP_USER_AGENT", ''),
        "HTTP_ACCEPT":  os.environ.get("HTTP_ACCEPT", ''),
        "HTTP_HOST":  os.environ.get("HTTP_HOST"),
        "REQUEST_URI": os.environ.get("REQUEST_URI"),
        "QUERY_STRING": os.environ.get("QUERY_STRING"),
        "REMOTE_ADDR": os.environ.get("REMOTE_ADDR"),
        "REMOTE_PORT": os.environ.get("REMOTE_PORT")
        }

def getClientType():
    '''Return the client type and file extension'''

    user_agent = ua.parse(env_dict["HTTP_USER_AGENT"])
    for browser, format in browser_formats:
        if user_agent.browser.family == browser:
            if format == 'html':
                return ('html', 'html')
            elif format == 'xml':
                return ('xml', 'xml')
            elif format == 'wml' and 'wml' in env_dict["HTTP_ACCEPT"]:
                return ('wml', 'wml')
    return ("html", "html")


def getContentType():
    '''Return the content type of the client's content file'''

    try:
        with open(getClientType()[0] + "/contentType.txt") as file:
            contentType = file.read()
    except FileNotFoundError:
        raise SessionError("Missing content type file")
    return contentType

def redirect(URL):
    '''Redirect the client to a relative URL'''

    print ("Location: {}".format(urljoin( "http://" + env_dict[ "HTTP_HOST" ] + env_dict["REQUEST_URI"], URL )))

class SessionError(Exception):
    '''User defined exception'''

    def __init__(self, error):
        '''set the error message'''

        self.error = error

    def __str__(self):
        '''return printable message'''

        return self.error

class Session (UserDict):
    '''keeps track of http session'''

    def __init__(self, createNew = None):
        '''create a new session or load an existing session'''

        if not createNew:

            query_string = request.args.to_dict()

            if "ID" not in query_string:
                raise SessionError("NO  ID  GIVEN")

            self.sessionID = query_string["ID"][0]
            self.fileName = os.getcwd()+"/session/."+self.sessionID

            if not self.sessionExists():
                raise SessionError("Noneexistant ID given")

            UserDict.__init__(self, self.loadSession())

        else:
            self.sessionID = self.generateID()
            self.fileName = os.getcwd()+ "/session/." + self.sessionID
            print("{}".format(self.fileName))

            if self.sessionExists():
                raise SessionError("session already exists")

            UserDict.__init__(self)

            self.data["ID"] = self.sessionID
            self.data["agent"], self.data["extensions"] = getClientType()
            self.data["content type"] = getContentType()
            self.data["cart"] = {}


    def sessionExists(self):
        '''Determine if the specified session file exists'''

        return os.path.exists(self.fileName)

    def loadSession(self):
        '''return unpickled dictionary of existing session'''

        if self.sessionExists():
            sessionFile = open(self.fileName)
            data = pickle.load(sessionFile)
            sessionFile.close()
            return data

    def saveSession(self):
        sessionFile = open(self.fileName, "w")
        pickle.dump(self.data, sessionFile)
        sessionFile.close()

    def deleteSession(self):
        '''Delete session file'''

        os.remove(self.fileName)


    def generateID(self):
        '''Generate a unique ID'''

        seed = str(time.time()) + os.environ["REMOTE_ADDR"] + os.environ[ "REMOTE_PORT" ]
        ID = hashlib.md5(seed.encode()).hexdigest()

        return ID
