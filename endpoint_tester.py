import requests

base_url = 'http://localhost:5050'  # Adjust port if finder picked another

# Test subscribe
response = requests.get(f"{base_url}/subscribe/test_user/basic")
print("Subscribe Response:", response.text)

# Test revenue
response = requests.get(f"{base_url}/revenue/subscription")
print("Revenue Response:", response.text)

# Test enhanced
response = requests.get(f"{base_url}/enhanced/api_call/What%20is%20the%20meaning%20of%20life?")
print("Enhanced Response:", response.text)