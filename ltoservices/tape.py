
from ltoservices.baseservice import BaseService

class tapeService(BaseService):

    def list( self ):
        data = self.LTO.sendRequest('GET', "/api/v1/tape/list" )
        if ( data["status"] == 200 ):
            return data["data"]["data"]
        else:
            return None


    def create( self, label, copyNumber ):
        dt = { 'label': label, 'copyNumber': copyNumber }
        data = self.LTO.sendRequest( 'PUT', "/api/v1/tape/new", data=dt, auth=True )
        return data["data"]


    def updateContent( self, label ):
        dt = {}
        data = self.LTO.sendRequest( 'PATCH', "/api/v1/tape/%s/updatecontent" % ( label ), data=dt, auth=True )
        return data["data"]


    def clone( self, label, label2 ):
        dt = {}
        data = self.LTO.sendRequest( 'PATCH', "/api/v1/tape/%s/cloneto/%s" % ( label, label2 ), data=dt, auth=True )
        return data["data"]


    def drop( self, label ):
        dt = {}
        data = self.LTO.sendRequest( 'DELETE', "/api/v1/tape/%s/drop" % ( label ), data=dt, auth=True )
        return data["data"]


    def getWorkerCount( self ):
        dt = {}
        data = self.LTO.sendRequest( 'GET', "/api/v1/tape/workercount", data=dt, auth=True )
        return data["data"]


    def setWorkerCount( self, wc ):
        dt = { 'worker-count': wc }
        data = self.LTO.sendRequest( 'PATCH', "/api/v1/tape/workercount", data=dt, auth=True )
        return data["data"]
