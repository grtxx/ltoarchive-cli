import json
from ltoservices.baseservice import BaseService

class systemService(BaseService):

    def destinations( self ):
        data = self.LTO.sendRequest('GET', "/api/v1/destinations" )
        if ( data["status"] == 200 ):
            return data["data"]["data"]["destinations"]
        else:
            return None


    def tasks( self ):
        data = self.LTO.sendRequest('GET', "/api/v1/tasks" )
        if ( data["status"] == 200 ):
            return data["data"]["data"]["tasks"]
        else:
            return None
