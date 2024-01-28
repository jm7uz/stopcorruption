import aiohttp

async def loginOnePage(username, password):
    url = "https://my3.gov.uz/api/account/auth/sign-in-via-login-passwd/index?lang=uz"
    headers = {
        "accept": "application/json",
        "host": "my3.gov.uz",
        "user-agent": "Dart/3.1 (dart:io)",
        "qjr7z489gvvj5tqhmnrufxtl0lgk6k6k4jkq4e0jm" : "I7Ej8c6BMe0HQzt88PQjGTQOfNzzTfr1RmYBgDT2q" 
    }
    data = {
        "username": username,
        "password": password
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            return await response.json()


async def UserData(token):
    url = "https://my3.gov.uz/api/account/user/info?lang=uz"
    headers = {
        "accept": "application/json",
        "host": "my3.gov.uz",
        "user-agent": "Dart/3.1 (dart:io)",
        "qjr7z489gvvj5tqhmnrufxtl0lgk6k6k4jkq4e0jm" : "I7Ej8c6BMe0HQzt88PQjGTQOfNzzTfr1RmYBgDT2q",
        "pevaoun6hphkumxxigradhmazavl3uqflkmmfkb2g" : token
    }
    data = {

    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            print(f"Status: {response.status}")
            return await response.json()

