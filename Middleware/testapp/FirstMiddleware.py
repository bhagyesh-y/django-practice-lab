from django.http import HttpResponse

class FirstMiddleWare(object):
    def __init__(self,get_response):
        self.get_response=get_response
        # one time configuration and initialization
        
    def __call__(self,request):
        #  code to be executed for each request before
        # the view and later middleware are called
        print("This line is executed before the Helloview")
        
        response = self.get_response(request)
        print("This line is executed after the hello view")
        return response
    def process_exeception(self,request,exception):
        return HttpResponse('<h1> Something went wrong.....</h1>')
        
            