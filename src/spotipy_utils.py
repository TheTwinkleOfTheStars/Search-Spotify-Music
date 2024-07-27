"""spotify APIを用いた楽曲情報の取得関数、プレイリスト作成関数を記載。
"""

from typing import Optional

import spotipy
import spotipy.util as util

def get_track_info(word:str, sp:spotipy.Spotify)->Optional[list]:
    """指定されたキーワードを使用してSpotifyのトラックを検索し、トラック情報を取得する。

    Args:
        word (str): 検索する楽曲名。
        sp (spotipy.Spotify): 検索を実行するために使用するSpotipyクライアントインスタンス。

    Returns:
        Optional[dict]: 成功した場合はトラック情報の辞書のリスト、失敗した場合はNoneを返します。

    Notes: 
        - Spotipyで一度にリクエストできる曲の上限が50曲であるため、オフセットを利用して50曲ずつ検索結果を取得する。
    """
    tracks = []
    for offset_n in range(0, 1_000, 50):
        try:
            # market="JP": 日本市場で利用可能なコンテンツに限定。
            response = sp.search(q=f'track:{word}', type='track', limit=50, market="JP", offset=offset_n)
            tracks += response["tracks"]["items"]
        except Exception as e:
            print(f"offset:{offset_n} {e}")
    return tracks

def get_id_by_perfect_matching(word: str, tracks: dict) -> list:
    """指定された単語と完全一致するトラックIDのリストを取得する。

    Args:
        word (str): 検索する楽曲名。
        tracks (dict): トラック情報。get_track_info()により出力された辞書を想定。

    Returns:
        list: wordと完全一致する楽曲のIDのリスト。

    """
    ids = []
    for track in tracks:
        if track.get("name") == word:
            ids.append(track.get("id"))
    return ids

def make_playlist(sp: spotipy.Spotify, username: str, playlist_name: str, ids: list) -> None:
    """指定したユーザ上に、IDリストの楽曲から成るプレイリストを作成する。

    Args:
        sp (spotipy.Spotify): Spotipyクライアントインスタンス。
        username (str): プレイリストを作成するユーザー名。
        playlist_name (str): 新しいプレイリストの名前。
        ids (list): プレイリストに追加するトラックのIDリスト。

    """
    try:
        # 空のプレイリストを作成。
        playlists = sp.user_playlist_create(username, playlist_name)

        # プレイリストに曲を追加。
        # 100曲超のトラックを一度にプレイリストに追加しようとするとエラーが発生するため、
        # チャンクに分割してプレイリストに追加。
        chunk_size = 100
        for i in range(0, len(ids), chunk_size):
            ids_chunk = ids[i:i+chunk_size]
            sp.user_playlist_add_tracks(username, playlists['id'], ids_chunk)
    except Exception as e:
        print(e)

def make_playlist_by_perfect_matching(word:dict, authentication_dic:dict):
    """指定したキーワードと完全一致する楽曲名のプレイリストを作成する。

        APIを利用し、引数wordに関連する楽曲最大1,000曲の情報を取得。
        得られた楽曲のうち曲名がwordと完全一致する曲のみからなるプレイリストを作成する。

    Args:
        word (dict): キーワード(楽曲名)。
        authentication_dic (dict): 下記のSpotify認証情報を含む辞書。
            - 'client_id' (str): SpotifyのクライアントID。
            - 'client_secret' (str): Spotifyのクライアントシークレット。
            - 'username' (str): Spotifyのユーザ名。
            - 'redirect_url' (str): SpotifyのリダイレクトURL。
            - 'scope' (str): スコープ。

    Notes:
        - 引数wordの関連楽曲が1,000曲以上存在する場合、検索結果の上位1,000曲のみ
          が抽出対象となる。
    """
    token = util.prompt_for_user_token(**authentication_dic)
    sp = spotipy.Spotify(auth=token)
    # APIを叩き、条件を満たすトラックのIDリストを取得
    tracks = get_track_info(word, sp=sp)
    ids = get_id_by_perfect_matching(word, tracks)
    make_playlist(sp=sp, username=authentication_dic["username"], playlist_name=word, ids=ids)