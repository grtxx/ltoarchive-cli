
from ltoservices.baseservice import BaseService

class jobService(BaseService):

    def list( self ):
        data = self.LTO.sendRequest('GET', "/api/v1/job/list" )
        if ( data["status"] == 200 ):
            return data["data"]["data"]
        else:
            return None

