from mxproxy import mx
import requests

class Headers:
	teacher={'x-auth-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibXVrZXNoIGdpbHVrYSIsImVtYWlsIjoiZ2lsdWthZ2lsdWthQGdtYWlsLmNvbSIsIl9pZCI6IjVmZTNiYTg2NWVmM2ZmMDAxMjEwMWNjMyIsInR5cGUiOiJUIiwiaWF0IjoxNjEwMDUxMDYzfQ.w-53QUWgqAMW_QUyj3mC_uNCE3ljWr79OCVnfM07K3U'}
	student={'x-auth-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibmlraGlsIHN3YW1pIiwiZW1haWwiOiJuaWtoaWxzd2FtaTFAZ21haWwuY29tIiwiX2lkIjoiNjA0MzE2OTdmZDFjMTEwMDEzZjkwY2FhIiwidHlwZSI6IlMiLCJpYXQiOjE2MTUyMjQ4MzN9.IZaCIAh6QpQpgaGMKipueE-RqBqOSsN0kpOH0XsleiA'}

def get_quiz_as_json(quizurl,pprint=0):
	response=requests.get(quizurl,headers=Headers.student).json()
	if pprint: print(mx.jdumps(response))
	return response

if __name__=='__main__':
	quizurl='https://teachomatrix.tk/api/quiz/6085a0cd0e4abe0013586e0f'
	data=get_quiz_as_json(quizurl,pprint=1)
	print(data)