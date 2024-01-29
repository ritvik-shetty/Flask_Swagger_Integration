import requests

header={
    'Accept':'*/*',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjUwODU4NywianRpIjoiZGNlOWFlMGItM2Q2OC00Y2EwLTk4NDUtZGMyMDk1M2IyYTIwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDY1MDg1ODcsImNzcmYiOiI5ODUxYzBjNi1jZWE4LTQ3MjEtODE3OC1jODY4MWZkMmE2YTkiLCJleHAiOjE3MDY1MDk0ODd9.mS4Bw1tqipHoJQ9dF8d0MsKf0G5HghMVKwe6twZXpag'

}

request_payload={
        "name": "Karthik",
        "address": "kundapura-street",
        "city": "udupi",
        "salary": "97765"
    }

response= requests.post('http://127.0.0.1:5000/create_employee',headers=header,json=request_payload)

print(response.json())


assert response.status_code == 201 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)

response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)

list=response.json()
for i in range(len(list)):
    print(list[i])
