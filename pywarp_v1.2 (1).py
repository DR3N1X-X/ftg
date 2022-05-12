import random
import httpx

headers = {
    "CF-Client-Version": "a-6.11-2223",
    "Host": "api.cloudflareclient.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.1",
}

with httpx.Client(
    base_url="https://api.cloudflareclient.com/v0a2223", headers=headers, timeout=10.0
) as client:

    r = client.post("/reg")
    id = r.json()["id"]
    license = r.json()["account"]["license"]
    token = r.json()["token"]

    r = client.post("/reg")
    id2 = r.json()["id"]
    token2 = r.json()["token"]

    headers_get = {"Authorization": f"Bearer {token}"}
    headers_get2 = {"Authorization": f"Bearer {token2}"}
    headers_post = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": f"Bearer {token}",
    }

    json = {"referrer": f"{id2}"}
    client.patch(f"/reg/{id}", headers=headers_post, json=json)

    client.delete(f"/reg/{id2}", headers=headers_get2)

    keys = [
        "47d58Hqv-ueR37x50-db3l70n2",
        "bwK01o62-c15C78MH-Z2g5Ji74",
        "c3Dd52l4-K28SzY14-0wKO47c8",
        "Vq765xO8-TR392VI5-z4j6Xp28",
        "3C651Aqt-3PHl50V7-3751AOCb",
        "WE38q17B-25DP3um4-9A7xg48Z",
        "x0yZ894a-3Sh2b90q-718Wrw4A",
        "3z1tW5s7-03L78SFw-6w2T9F4c",
        "bkp5301R-VDB6234t-x954U8Jb",
        "ofQ759g4-9628GDiy-6i58VGa2",
    ]
    key = random.choice(keys)

    json = {"license": f"{key}"}
    client.put(f"/reg/{id}/account", headers=headers_post, json=json)

    json = {"license": f"{license}"}
    client.put(f"/reg/{id}/account", headers=headers_post, json=json)

    r = client.get(f"/reg/{id}/account", headers=headers_get)
    account_type = r.json()["account_type"]
    referral_count = r.json()["referral_count"]
    license = r.json()["license"]

    client.delete(f"/reg/{id}", headers=headers_get)

    print(f"Тип аккаунта: {account_type}")
    print(f"Данных выделено: {referral_count} Гбайт")
    print(f"Лицензия: {license}")
