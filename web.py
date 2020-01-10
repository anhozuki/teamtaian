import requests
# 存在する URL
get_url_info = requests.get('https://www6.jwu.ac.jp/up/faces/login/Com00504A.jsp')
status_code = get_url_info.status_code
print(status_code) # => 200 
get_url_info = requests.post('https://www6.jwu.ac.jp/up/faces/login/Com00504A.jsp')
# コンテンツタイプの取得
print(get_url_info.headers['content-type']) #=>text/html
# エンコーディング情報
print(get_url_info.encoding) #=>ISO-8859-1
# web ページの中身
print(get_url_info.text) #=> <!DOCTYPE html>...</html>
