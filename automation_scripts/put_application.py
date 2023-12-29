import requests

header={
    'Accept':'*/*',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMzgyNTEzMiwianRpIjoiMDI0MjVlNTctNzE5Yy00YzRiLWE2ZmEtZmQ1MDZjM2Q0YzNhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDM4MjUxMzIsImNzcmYiOiI2MmM2MWMzNy1mZTdlLTQxODQtODI3Zi1kMDM4ODU4ZGE1NmUiLCJleHAiOjE3MDM4MjYwMzJ9.Tvlid_PJEQjaHXIBnhX1XKDBukUTaNFZ537SRPTErfg'
}
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)

print("Before Update")
list=response.json()
for i in range(len(list)):
    print(list[i])



headerPut={
    'Accept':'*/*',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMzgyNTEzMiwianRpIjoiMDI0MjVlNTctNzE5Yy00YzRiLWE2ZmEtZmQ1MDZjM2Q0YzNhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ik1pY2hhZWwiLCJuYmYiOjE3MDM4MjUxMzIsImNzcmYiOiI2MmM2MWMzNy1mZTdlLTQxODQtODI3Zi1kMDM4ODU4ZGE1NmUiLCJleHAiOjE3MDM4MjYwMzJ9.Tvlid_PJEQjaHXIBnhX1XKDBukUTaNFZ537SRPTErfg'
}

putPayload={
        "address": "Kadri",
        "city": "Mangalore",
        "name": "Manoj",
        "salary": "92000"
}

responsePut= requests.put("http://127.0.0.1:5000/update_employee/6",headers=headerPut,json=putPayload)




print("After Update")
response= requests.get("http://127.0.0.1:5000/list_employees", headers=header)
list=response.json()
for i in range(len(list)):
    print(list[i])


assert responsePut.status_code == 200 , f"expected response to have status code 200 but got {response.status_code}"

print("The program has run successfully and the Status Code is",response.status_code)