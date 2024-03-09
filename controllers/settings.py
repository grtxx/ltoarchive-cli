import re
import sys


class Settings:

    def __init__( self ):
        self.settings = []
        self.commands = []
        self.cmdlineopts = [
            { "short": "s", "long": "server", "default": "http://127.0.0.1" },
            { "short": "p", "long": "port", "default": "8000" },
            { "short": "n", "long": "copynumber", "default": "0" },
            { "short": "d", "long": "domain", "default": "" }
        ]
        self.parseArgs()

    def get( self, name ):
        if name in self.settings:
            return self.settings[ name ]
        else:
            return ""
        
    def getCommand( self, num ):
        if num < len( self.commands ):
            return self.commands[num]
        else:
            return ""

    def parseArgs( self ):
        self.settings = {}
        self.commands = []
        i = 1
        for p in self.cmdlineopts:
            if "default" in p:
                self.settings[ p["long"] ] = p["default"]
        while i < len( sys.argv ):
            if ( sys.argv[i][:1] == "-" ):
                for p in self.cmdlineopts:
                    if ( sys.argv[i] == "-%s" % p["short"] ):
                        if ( i + 1 < len( sys.argv ) ):
                            self.settings[ p["long"] ] =  sys.argv[i+1]
                        i = i + 1
                    grps = re.match( r"--%s=(.*)$" % p["long"], sys.argv[i] )
                    if ( grps ):
                        self.settings[ p["long"] ] = grps.groups(1)[0]
            else:
                self.commands.append( sys.argv[i] )
            i = i + 1
        pass
