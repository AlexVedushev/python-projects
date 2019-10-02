import requests

baseAPI = 'http://localhost:1337/v1/'

class AuthRequest(object):
    def register(self, number=1):
        data = self.gerUserDict(1)
        print(baseAPI + 'auth/register')
        try:
            response = requests.post(baseAPI + 'auth/register', data=data)
        except Exception as err:
            print(err)
            return
        return response

    def gerUserDict(self, number=1):
        return {"firstName" : 'firstName1', 
                "lastName" : 'lastName1', 
                "email" : 'email1@mail.ru', 
                "password": 'password1'
                }

authRequest = AuthRequest()
response = authRequest.register(1)
print(response.json())