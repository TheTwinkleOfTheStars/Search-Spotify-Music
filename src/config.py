""" .envファイルによる環境変数の設定
"""

import os
from dotenv import load_dotenv

load_dotenv("../.env")

authentication_dic = {
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
    "username": os.getenv("USERNAME"),
    "redirect_uri": os.getenv("REDIRECT_URL"),
    "scope": os.getenv("SCOPE")
}