import requests

if __name__ == "__main__":
    response = requests.post("http://127.0.0.1:8000/", json={
        "opening_hours": "24hrs"
    })
    print(response.text)