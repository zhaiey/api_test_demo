import  requests
# get_token()
url = 'http://192.168.5.47:32000'
header1 = {
    'Terrace': 'HOSPITAL-CALL',
    'Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7InRlcnJhY2UiOiJIT1NQSVRBTC1DQUxMIiwidXNlcklkIjoiTlRjeU5UWT0iLCJpcCI6Ik1Ua3lMakUyT0M0MExqRTBOdz09IiwidXNlcm5hbWUiOiJsaWd1In0sInN1YiI6ImxpZ3UiLCJpc3MiOiJTU08iLCJpYXQiOjE3MTQyNjM5MTMsImF1ZCI6IkhPU1BJVEFMLUNBTEwiLCJleHAiOjI3MTIyNjM4NTMsIm5iZiI6MTcxNDI2Mzg1M30.zrBxq9nfX3MLKI1EQxO35g__YbhInyLUkAJQ3z0HDq0'
}
response = requests.post(url='{}/ym-auth-server/u/api/v1/auth/init'.format(url), json={"serverCode":"HOSPITAL-CALL"},headers=header1)

print(response.json())
print(response.request.url)
print(response.request.headers)
print(response.request.body)

