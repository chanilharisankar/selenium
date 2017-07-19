import  requests
import pytest

class Test_ApiTest():

    def test_Api_T1(self):
        print("api tests")
        r = requests.get('https://reqres.in/api/users?page=2')
        print(r.json())
        print("\n")
        print(r.status_code)
        # print(r.text)
        # print(r.content)
        # print(r.raw)

