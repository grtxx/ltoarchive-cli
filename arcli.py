#!/usr/bin/python3.6m

import json
from ltoarchive import LTOArchive
from controllers.settings import Settings



class LTOArchiveClient:

    def __init__( self ):
        self.settings = Settings()
        self.LTO = LTOArchive( "%s:%s" % ( self.settings.get("server"), self.settings.get("port") ) )

    def domainCommands( self ):
        if self.settings.getCommand(1) == "list":
            print( self.LTO.domain.list() )

        if self.settings.getCommand(1) == "create":
            if self.settings.getCommand(2) != "":
                print( self.LTO.domain.create( self.settings.getCommand(2) ) )

        if self.settings.getCommand(1) == "drop":
            if self.settings.getCommand(2) != "":
                print( self.LTO.domain.drop( self.settings.getCommand(2) ) )


    def jobCommands( self ):
        if self.settings.getCommand(1) == "list":
            print( json.dumps( self.LTO.job.list(), indent=2 ) )
            return True
        elif self.settings.getCommand(1) == "continue":
            if ( self.settings.getCommand(2) != "" ):
                print( json.dumps( self.LTO.job.cont( int(self.settings.getCommand(2)) ), indent=2 ) )
            else:
                print( "Job ID is required" )
            return True        
        elif self.settings.getCommand(1) == "pause":
            if ( self.settings.getCommand(2) != "" ):
                print( json.dumps( self.LTO.job.pause( int(self.settings.getCommand(2)) ), indent=2 ) )
            else:
                print( "Job ID is required" )
            return True


    def tapeCommands( self ):
        if self.settings.getCommand(1) == "list":
            print( json.dumps( self.LTO.tape.list(), indent=2 ) )
            return True
        elif self.settings.getCommand(1) == "add":
            if self.settings.getCommand(2) != "" and self.settings.get('copynumber') != "":
                print( self.LTO.tape.create( self.settings.getCommand(2), self.settings.get('copynumber') ) )
                return True
        elif self.settings.getCommand(1) == "updatecontent":
            print( self.LTO.tape.updateContent( self.settings.getCommand(2) ) )
            return True
        elif self.settings.getCommand(1) == "clone":
            print( self.LTO.tape.clone( self.settings.getCommand(2), self.settings.getCommand(3) ) )
            return True
        elif self.settings.getCommand(1) == "drop":
            if self.settings.getCommand(2) != "":
                print( self.LTO.tape.drop( self.settings.getCommand(2) ) )
                return True
        elif self.settings.getCommand(1) == "workercount":
            if ( self.settings.getCommand(2) == "get" ):
                print( self.LTO.tape.getWorkerCount() )
                return True
            elif ( self.settings.getCommand(2) == "set" ):
                print( self.LTO.tape.setWorkerCount( self.settings.getCommand(3) ) )
                return True


    def projectCommands( self ):
        if self.settings.getCommand(1) == "check":
            print( self.LTO.project.check( self.settings.get('domain'), self.settings.getCommand(2) ) )


    def systemCommands( self ):        
        if self.settings.getCommand(1) == "destinations":
            print( json.dumps( self.LTO.system.destinations(), indent=2 ) )
            return True
        elif self.settings.getCommand(1) == "tasks":
            print( json.dumps( self.LTO.system.tasks(), indent = 2 ) )
            return True


    def router( self ):
        ret = False

        if ( self.settings.getCommand(0) == "domain" ):
            ret = self.domainCommands()
        elif ( self.settings.getCommand(0) == "tape" ):
            ret = self.tapeCommands()
        elif ( self.settings.getCommand(0) == "project" ):
            ret = self.projectCommands()
        elif ( self.settings.getCommand(0) == "job" ):
            ret = self.jobCommands()
        elif ( self.settings.getCommand(0) == "system" ):
            ret = self.systemCommands()

        if ( not ret == True ):
            print( "Unknown command" )


main = LTOArchiveClient()
main.router()
