import requests
import time
from pprint import pprint
import json

AppInfo= 'eyJEYk5hbWUiOiJORzAwMDEiLCJPcmdJZCI6IjU0NzE4MTEyMTAwMDAwMSIsIk9yZ05hbWUiOiIiLCJPQ29kZSI6IiIsIlVzZXJJZCI6IjYzMTE4MTExNTAwMDAwMSIsIlVzZXJLZXkiOiIiLCJVc2VyTmFtZSI6IiIsIlRva2VuS2V5IjoiIiwiQXBwS2V5IjoiRDMxQjdGOTEtMzA2OC00QTQ5LTkxRUUtRjNFMTNBRTVDNDhDIiwiQXBwU2VjcmV0IjoiMTAzQ0I2MzktODQwQy00RTRGLTg4MTItMjIwRUNFM0M0RTREIiwiRGJTZXJ2ZXJOYW1lIjoiIiwiU2Vzc2lvbktleSI6IiIsIlVOYW1lIjoiIn0='
Sign = '481fbed44e4a225ed66b2282d80bc858,http://218.108.53.106:8066/custom,1565166611000,D31B7F91-3068-4A49-91EE-F3E13AE5C48C,NG0001'

class login:
    def login(self,phone,orgid,password):
        res = requests.post(f'http://218.108.53.106:8066/custom/api/GCW/SysUser/PostLogin',
                            headers = {
                                'AppInfo':AppInfo,
                                'Sign':Sign
                            },
                            data={
                                'uname_login':phone,
                                'orgid':orgid,
                                'password':password,

                            })
        retObj = res.json()
        pprint(retObj, width=60)

        # sessionid = res.cookies['sessionId']
        # self.sessionid = sessionid

        return retObj



class  PVoucherAuxiliaryType:
    def addPVoucherAuxiliaryType(self,TypeId,EnabledMark,BaseName):
        nowTimeRandom = time.time()
        res = requests.post(f'http://218.108.53.106:8066/custom/api/GCW/PVoucherAuxiliaryType/PostUpdateAuxiliary',
                            headers = {
                                'AppInfo':AppInfo,
                                'Sign':Sign
                            },
                            data={
                                'TypeId':TypeId,
                                'UpdateList[0][EnabledMark]':EnabledMark,
                                'UpdateList[0][BaseName]':BaseName,
                                'nowTimeRandom':nowTimeRandom

                            })
        retObj = res.json()
        pprint(retObj, width=60)

    def listPVoucherAuxiliaryType(self, uid, orgid, typeId,CodeOrName):
        nowTimeRandom = time.time()
        res = requests.get(f'http://218.108.53.106:8066/custom/api/GCW/PVoucherAuxiliaryType/GetAuxiliaryQueryList',
                            headers={
                                'AppInfo': AppInfo,
                                'Sign': Sign
                            },
                            params={
                                'uid': uid,
                                'orgid':orgid,
                                'typeId':typeId,
                                'CodeOrName':CodeOrName,
                                'nowTimeRandom':nowTimeRandom

                            })
        retObj = res.json()
        pprint(retObj, width=60)


# retObj = login().login('18868876754','460190419000001','d0dcbf0d12a6b1e7fbfa2ce5848f3eff')
# retObj1 = PVoucherAuxiliaryType().addPvoucher('460190419000001','0','234')
retObj2 = PVoucherAuxiliaryType().listPVoucherAuxiliaryType('460190419000001','460190419000001','460190419000001','')

