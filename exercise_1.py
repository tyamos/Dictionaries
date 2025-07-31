
response = {
     # Key Values pair 
     "success": True, 
     "message": "Login successful!", 
     "data": ["tyamos@gmail.com","tyamos"]
}

print(response)
print(response["success"]) 
print(response["message"])
print(response["data"])
print(response.get("success"))
print(response.get("message"))
print(response.get("data"))
print(len(response))
