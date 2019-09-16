# coding=utf-8

from django.http import JsonResponse,HttpResponse,HttpResponseForbidden,QueryDict
import traceback,datetime,json

class JsonResponseException(JsonResponse,BaseException):
    pass


class AbstractHandler():
    def __init__(self,app_logger):

        self.app_logger = app_logger

        self.METHOD_TAB = None

    def dispatch(self, request, *args, **kwargs):

        try:
            if request.method not in  self.METHOD_TAB:
                return JsonResponse({'retcode': 1, 'reason': '不支持的 method 类型'})

            if request.method == 'GET':
                param_dict = request.GET
            elif request.method == 'POST':
                param_dict = request.POST
            elif request.method == 'PUT':
                param_dict = QueryDict(request.body)
            elif request.method == 'DELETE':
                param_dict = QueryDict(request.body)
            else:
                return JsonResponse({'retcode': 1, 'reason': u'不支持的 method 类型'})

            # json 格式的消息体，特殊的处理
            if request.path.startswith('/apijson/'):
                param_dict = json.loads(request.body)


            request.param_dict = param_dict



            method_dispatcher = self.METHOD_TAB[request.method]

            # method_dispatcher is handler
            if hasattr(method_dispatcher, '__call__'):
                handler = method_dispatcher
            # method_dispatcher is a dict, use parameter 'action' to find handler
            else:
                if 'action' not in param_dict:
                    return JsonResponse({'retcode': 1,'reason': u'需要参数`action`'})

                action = param_dict['action']
                if action not in method_dispatcher:
                    return JsonResponse({'retcode': 1,'reason': u'不支持的`action`类型'})

                handler = method_dispatcher[action]

        except:
            exc = traceback.format_exc()
            self.app_logger.error(exc)
            return JsonResponse({'retcode': 500, 'reason': exc})



        try:
            # print 'args',args
            # print 'kwargs',kwargs
            return handler(request, *args, **kwargs)


        except:
            exc = traceback.format_exc()
            self.app_logger.error(exc)
            return JsonResponse({'retcode': 500, 'reason': exc})


    def checkMandatoryParams(self, request, params):
        for param in params:
            if param not in request.param_dict:
                raise JsonResponseException({
                'retcode': 1,
                'reason': u"缺少参数`%s`" % param
                })





def nginx_accel(request,app):
    '''
    default django view, where id is an argument that identifies
    the ressource to be protected
    '''
    allowed = False

    # do your permission things here, and set allowed to True if applicable
    if allowed:
        response = HttpResponse()
        # let nginx determine the correct content type
        response['Content-Type']=""
        response['X-Accel-Redirect'] = request.get_full_path()
        return response

    return HttpResponseForbidden()

now = datetime.datetime.now
# if getattr(settings, 'USE_TZ'):
#     try:
#         from django.utils import timezone
#         now = timezone.now
#     except ImportError:
#         pass

# def now():
#     # Needs to be be a function as USE_TZ can change based on if we are testing or not.
#     _now = datetime.datetime.now
#     if getattr(settings, 'USE_TZ'):
#         try:
#             from django.utils import timezone
#             _now = timezone.now
#         except ImportError:
#             pass
#     return _now()


#性别选择
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)