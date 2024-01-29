import requests

header={
    'Accept':'*/*',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwODU4NywianRpIjoiZGNlOWFlMGItM2Q2OC00Y2EwLTk4NDUtZGMyMDk1M2IyYTIwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDg1ODcsImNzcmYiOiI5ODUxYzBjNi1jZWE4LTQ3MjEtODE3OC1jODY4MWZkMmE2YTkiLCJleHAiOjE3MDY1MDk0ODd9.mS4Bw1tqipHoJQ9dF8d0MsKf0G5HghMVKwe6twZXpag'
}
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)

print("Before Update")
list=response.json()
for i in range(len(list)):
    print(list[i])



headerPut={
    'Accept':'*/*',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwODU4NywianRpIjoiZGNlOWFlMGItM2Q2OC00Y2EwLTk4NDUtZGMyMDk1M2IyYTIwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDg1ODcsImNzcmYiOiI5ODUxYzBjNi1jZWE4LTQ3MjEtODE3OC1jODY4MWZkMmE2YTkiLCJleHAiOjE3MDY1MDk0ODd9.mS4Bw1tqipHoJQ9dF8d0MsKf0G5HghMVKwe6twZXpag'
}

putPayload={
        "address": "Kadri",
        "city": "Mangalore",
        "name": "Manoj",
        "salary": "44000"
}

responsePut= requests.put("http://127.0.0.1:5000/update_employee/6",headers=headerPut,json=putPayload)




print("After Update")
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)
list=response.json()
for i in range(len(list)):
    print(list[i])


assert responsePut.status_code == 200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)