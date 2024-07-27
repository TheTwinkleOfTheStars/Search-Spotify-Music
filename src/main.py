""" 指定した文字列と完全一致する楽曲からなるSpotifyのプレイリストを作成する。
"""

from config import authentication_dic
from spotipy_utils import make_playlist_by_perfect_matching

# 検索したい楽曲名を代入する
word = "秋"
make_playlist_by_perfect_matching(word, authentication_dic)