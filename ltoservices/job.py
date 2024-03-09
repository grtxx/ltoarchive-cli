
from ltoservices.baseservice import BaseService

class jobService(BaseService):

    def list( self ):
        data = self.LTO.sendRequest('GET', "/api/v1/job/list" )
        if ( data["status"] == 200 ):
            return data["data"]["data"]
        else:
            return None

    def cont( self, jobid: int ) -> bool:
        data = self.LTO.sendRequest('PATCH', "/api/v1/job/%d/continue" % jobid, None, None, True )
        if ( data["status"] == 200 ):
            return True
        else:
            return False

    def pause( self, jobid: int ) -> bool:
        data = self.LTO.sendRequest('PATCH', "/api/v1/job/%d/pause" % jobid, None, None, True )
        if ( data["status"] == 200 ):
            return True
        else:
            return False

