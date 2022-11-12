import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060")

# print(res.text)
# res ステータスコードを表示
# .text データの中身を表示
 
# print(res.text["status"]) # エラー
# print(type(res.text))  # 文字型のデータ
# print(res.json()) # json形式に変更 > 辞書がたのdデータが返ってくる
# print(res.json()["status"])

# print(len(res.json()["results"]))

# print(res.json()["results"][0]["address1"])
# print(res.json()["results"][0]["address2"])
# print(res.json()["results"][0]["address3"])
# print(res.json()["results"][0]["prefcode"])

# よく使うものは変数にしてみる
json = res.json()
print(json["results"][0]["address1"])
print(json["results"][0]["address2"])
print(json["results"][0]["address3"])
print(json["results"][0]["prefcode"])

