import requests

from pprint import pprint
import json

API_SERVER = '127.0.0.1'
class APIBase:

    def login(self,username,password):
        res = requests.post(f'http://{API_SERVER}/api/mgr/loginReq',
                      data={
                          'username' : username,
                          'password' : password
                      })

        retObj = res.json()
        pprint(retObj,width=60)

        sessionid = res.cookies['sessionid']
        self.sessionid = sessionid

        return retObj,sessionid


class CourseMgr(APIBase):

    def __init__(self,sessionid=None):
        self.sessionid = sessionid

    def add_course(self,name,desc,idx):
        res = requests.post(f'http://{API_SERVER}/api/mgr/sq_mgr/',
                      data={
                          'action':"add_course",
                          'data'  : f'''
                          {{
                              "name":"{name}",
                              "desc":"{desc}",
                              "display_idx":"{idx}"
                          }}
                          '''
                      },
                      cookies={'sessionid':self.sessionid})

        retObj = res.json()
        pprint(retObj,width=60)

        return retObj


    def list_course(self,pagenum,pagesize):
        res = requests.get(f'http://{API_SERVER}/api/mgr/sq_mgr/',
                           params={
                               'action':"list_course",
                               'pagenum':pagenum,
                               'pagesize':pagesize
                           },
                            cookies={'sessionid':self.sessionid})
        retObj = res.json()
        pprint(retObj,width=60)

        return retObj


    def modify_course(self,cid,newname,newdesc,newidx):
        res = requests.put(f'http://{API_SERVER}/api/mgr/sq_mgr/',
                      data={
                          'action':"modify_course",
                          'id': cid,
                          'newdata'  : f'''
                          {{
                              "name":"{newname}",
                              "desc":"{newdesc}",
                              "display_idx":"{newidx}"
                          }}
                          '''
                      },
                      cookies={'sessionid':self.sessionid})

        retObj = res.json()
        pprint(retObj,width=60)

        return retObj



    def delete_course(self,cid):
        res = requests.delete(f'http://{API_SERVER}/api/mgr/sq_mgr/',
                              data={
                                  'action':"delete_course",
                                  'id': cid
                              },
                                cookies={'sessionid':self.sessionid})


        retObj = res.json()
        pprint(retObj,width=60)

        return retObj



class TeacherMgr(APIBase):

    def __init__(self,sessionid=None):
        self.sessionid = sessionid

    def add_teacher(self,
                    username,
                    password,
                    realname,
                    desc,
                    courses,
                    display_idx):

        res = requests.post(f'http://{API_SERVER}/api/mgr/sq_mgr/',
                      data={
                          'action':"add_teacher",
                          'data'  : f'''
                          {{
                              "username":"{username}",
                              "password":"{password}",
                              "realname":"{realname}",
                              "desc":"{desc}",
                              "courses":{json.dumps(courses)},
                              "display_idx":"{display_idx}"
                          }}
                          '''
                      },
                      cookies={'sessionid':self.sessionid},
                        )

        retObj = res.json()
        pprint(retObj,width=60)

        return retObj


    def list_teacher(self,pagenum,pagesize):
        res = requests.get(f'http://{API_SERVER}/api/mgr/sq_mgr/',
                           params={
                               'action':"list_teacher",
                               'pagenum':pagenum,
                               'pagesize':pagesize
                           },
                            cookies={'sessionid':self.sessionid})
        retObj = res.json()
        pprint(retObj,width=60)

        return retObj


    def modify_teacher(self,
                       tid,
                       username,
                       password,
                       realname,
                       desc,
                       courses,
                       display_idx
                       ):
        res = requests.put(f'http://{API_SERVER}/api/mgr/sq_mgr/',
                      data={
                          'action':"modify_teacher",
                          'id': tid,
                          'newdata'  : f'''
                          {{
                              "username":"{username}",
                              "password":"{password}",
                              "realname":"{realname}",
                              "desc":"{desc}",
                              "courses":{json.dumps(courses)},
                              "display_idx":"{display_idx}"
                          }}
                          '''
                      },
                      cookies={'sessionid':self.sessionid})

        retObj = res.json()
        pprint(retObj,width=60)

        return retObj



    def delete_teacher(self,tid):
        res = requests.delete(f'http://{API_SERVER}/api/mgr/sq_mgr/',
                              data={
                                  'action':"delete_teacher",
                                  'id': tid
                              },
                                cookies={'sessionid':self.sessionid})


        retObj = res.json()
        pprint(retObj,width=60)

        return retObj