# Spotify APIを用いた楽曲名の完全一致検索とプレイリスト作成

## 目次
- 概要
- ディレクトリ構成
- 準備
- 実行方法
- トラブルシューティング
- 必要なPythonパッケージとライセンス情報

## 概要
Spotify APIを用いて、下記の自動化を行いました。
- Spotifyの楽曲で、指定したキーワードと**完全一致**する楽曲情報を取得する
- 取得した楽曲から成るプレイリストを作成する

Using the Spotify API, I automated the following tasks:
- Retrieve track information from Spotify that **exactly matches** the specified keyword
- Create a playlist from the retrieved tracks

## ディレクトリ構成
<pre>
.
├── .env.sample
├── .gitignore
├── README.md
├── poetry.lock
├── pyproject.toml
└── src
    ├── config.py
    ├── main.py
    └── spotipy_utils.py
</pre>

## 準備
`main.py`を実行するために、3項目の準備をする。
- Spotify周りの準備
- `.env`ファイルの作成
- PoetryによるPythonの環境構築

### Spotify周りの準備
- Spotify Developers ユーザーアカウントの作成
    - [Spotify Developers](https://developer.spotify.com/)へアクセスし、アカウントを作成する。
    - 作成したアカウントでログインする。
- Dashboard画面からappを作成する。
    - [Dashboard](https://developer.spotify.com/dashboard)画面右上「create app」からappを作成する。
- クライアントID、クライアントシークレット、ユーザー名の確認
    - appを作成後、クライアントIDとクライアントシークレットを控えておく。
    - Spotifyのアカウント画面からユーザー名を控えておく。([参考: ユーザー名の確認方法](https://support.spotify.com/jp/article/username-and-display-name/))

### `.env`ファイルの作成
- `.env`ファイルを作成し、Spotify情報(クライアントID、クライアントシークレット、ユーザー名)を記載する。
    - `.env.sample`ファイルを`.env`ファイルに置き換え、`USERNAME`にユーザー名、`CLIENT_ID`にクライアントID、`CLIENT_SECRET`にクライアントシークレットを記載すれば良い。

### PoetryによるPythonの環境構築
Poetryを使用してPythonのパッケージを行う。

#### 前提条件
- Python 3.12がインストールされていること。

#### Poetryのインストール
- Poetryをインストールする。
```
    curl -sSL https://install.python-poetry.org | python3 -
```
以下のように表示されたら、表示にしたがってコマンドを入力する。
```
To get started you need Poetry's bin directory (/Users/beginning/.local/bin) in your `PATH`
environment variable.

Add `export PATH="/Users/[Username]/.local/bin:$PATH"` to your shell configuration file.
```
- `poetry --version`と入力し、Pooetryのバージョンが表示されればインストール完了。

#### 仮想環境の作成
- プロジェクトのディレクトリに移動する。
- `pyproject.toml`と`poetry.lock`を基に必要なパッケージをインストールし、仮想環境を設定する。
```
    poetry install
```

#### 仮想環境のアクティベート、ライブラリのインストール
- 仮想環境をアクティベートする。
```
    poetry shell
```
- 必要なライブラリをインストールする。
```
    poetry install --no-dev
```

## 実行方法
- ターミナルを起動し、プロジェクトのディレクトリに移動する。
- 仮想環境をアクティベートする。
```
    poetry shell
```
- `main.py`を実行する。
```
    python src/main.py
```
- `main.py`の実行が完了すると、`word`に代入される文字列と完全一致する曲のプレイリストが自動で作成される。
- `main.py`の実行がうまくいかない場合は**トラブルシューティング**を参照。

## トラブルシューティング
`main.py`の実行がうまくいかない場合の対処方法を記載する。

- 下記が表示された場合、`.env`を正しく読み込めていない可能性がある。
    - `config.py`の`load_dotenv("../.env")`を`load_dotenv(".env")`に修正して`.env`を正しく読み込めるようにするか、実行するディレクトリを変更する。
```
    You need to set your Spotify API credentials.
    You can do this by setting environment variables like so:

    export SPOTIPY_CLIENT_ID='your-spotify-client-id'
    export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
    export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

    Get your credentials at
        https://developer.spotify.com/my-applications
```

## 必要なPythonパッケージとライセンス情報
| Name               | Version     | License                              |
|--------------------|-------------|--------------------------------------|
| certifi            | 2024.7.4    | Mozilla Public License 2.0 (MPL 2.0) |
| charset-normalizer | 3.3.2       | MIT License                          |
| idna               | 3.7         | BSD License                          |
| python-dotenv      | 1.0.1       | BSD License                          |
| redis              | 5.0.7       | MIT License                          |
| requests           | 2.32.3      | Apache Software License              |
| spotipy            | 2.24.0      | MIT                                  |
| urllib3            | 2.2.2       | MIT License                          |