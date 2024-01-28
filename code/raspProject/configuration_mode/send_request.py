import requests


def send_pincode(pincode, backend_url):
    payload = {
        'emp_id': '123',  # Replace with the actual employee ID
        'image': pincode
    }

    try:
        response = requests.post(backend_url, json=payload)

        # Check for a successful response (HTTP status code 2xx)
        if response.status_code // 100 == 2:
            print("Pincode uploaded successfully")
            return True
        else:
            print(f"Error uploading pincode. Status Code: {response.status_code}")
            print(response.text)
            return False

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return False