#authotication mechanish
import jwt
#shared secret is confidential dont disclose it any where
shared_secret = "One_Bloodline"

#working for athurization using jwt token
key_data = shared_secret
payload_data = {
    "email": "samiksha@gmail.com",
    "name": "samiksha",
    "Id": 1
}
access_token = jwt.encode(payload=payload_data, key=key_data)

print("access token:")
print(access_token)
