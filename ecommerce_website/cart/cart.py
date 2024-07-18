class Cart():
    def __init__(self,request):
        self.session =request.session

        #get session key if exist 
        cart = self.session.get('session_key')

        #if no session key then create one
        if 'session_key' not in request.session:
            cart = self.session['session_key']={}

        #make cart session available in all app by making kindof template next in context_processor.py
        
        self.cart = cart