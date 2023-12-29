import requests

header={
    'Accept':'*/*',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMzgyMzk2NywianRpIjoiYTFjNDFiMGEtM2FjMi00MzdkLWIxYWMtZWI0MWNmMmIxZTMwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDM4MjM5NjcsImNzcmYiOiJhZTA5NmRjYy0wY2YxLTQxYTQtYjVmMy1hMjM1NzkyNWU1MjYiLCJleHAiOjE3MDM4MjQ4Njd9.KtzhgxbN99y52Dqmro8NAH0gBJjYLqKPrPIIts-3kIM'

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
