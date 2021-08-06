"""
# func based middleware

def my_middleware(get_response):
    # one time initialization
    print("one-time initiallization")
    def my_function(request):
        print("this is before view")
        response = get_response(request)
        print('this is after view')
        return response
    print('before func return')
    return my_function
"""



"""
# the below is class based custom middlewares

class MyMiddleware1:
    def __init__(self, get_response):
        self.get_response = get_response
        print('init 1', get_response)

    def __call__(self, request):
        print('before the view 1')
        response = self.get_response(request)
        print('after view 1')
        return response

class MyMiddleware2:
    def __init__(self, get_response):
        self.get_response = get_response
        print('init 2', get_response)

    def __call__(self, request):
        print('before the view 2 ')
        response = self.get_response(request)
        print('after view 2')
        return response
"""


"""
# utilizing pre defined process_view function in middleware

from django.shortcuts import HttpResponse

class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, *args, **kwargs):
        # if this function returns none then the view will work
        # other wise this function will return the http response
        return HttpResponse("welcome welcome welcome")

# write this  'happy_homes.rentals.middlewares.MyProcessMiddleware'  inside settings.MIDDLEWARE

"""

"""
# utilizing pre-defifined template_response func

from django.shortcuts import HttpResponse

class MyTemplateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        # in this func u will get the response context from view which can change here
        # also this middleware is implemented when u are utilizing template response in a view
        #alter response then return it
        return response

"""