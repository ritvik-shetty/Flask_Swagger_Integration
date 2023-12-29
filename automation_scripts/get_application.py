import requests

header={
    'Accept':'*/*',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMzgyNzA1OCwianRpIjoiYjQzYjc5NTAtZmIxNi00OTU5LWI1ZTQtNTdmZGYwYzdlNWEyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDM4MjcwNTgsImNzcmYiOiJiYjQ1MTU5Mi04YTg0LTRlMDgtYmFjNC03NTJmMzRiNmRhOGUiLCJleHAiOjE3MDM4Mjc5NTh9.LUM-1qjUhdDdbsRTrbs-K6ORfsLt5b4mLuxbd9B15eU'
}
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)

assert response.status_code==200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)

list=response.json()
for i in range(len(list)):
    print(list[i])
