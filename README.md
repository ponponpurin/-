# plainWebAPI

このプロジェクトの実行環境構築手順でーす。

ちなみに、まだ動作確認してないので動くか不明です。

APIキーの管理は環境変数を書いたファイルで管理したいと考えております...

anacondaで実行することを想定して手順を解説します。
## インストール

1. git bashでリポジトリをクローンします：
git bashでプロジェクトを配置したいディレクトリに移動して以下のコマンドを入力してください。
例えば、デスクトップにpblっていうフォルダを作ってその中にクローンするなど。
   ```bash
   git clone https://github.com/areldai03/plainWebAPI.git
これで私のリポジトリのファイルがカレントディレクトリに作成されます。

2. 仮想環境の作成と実行
anconda プロンプトを開いてリポジトリをクローンしたディレクトリに移動します。pblというフォルダにクローンしたなら
pbl内のplainWebAPIディレクトリに移動して、

`python -m venv venv` を実行して仮想環境を作成します。

`.\venv\Scripts\activate` で仮想環境を起動します。

起動に成功するとプロンプトの先頭に(venv)と書かれます。
仮想環境を作成する意味は、プロジェクトごとにライブラリやpythonのversionを管理できるからです。
仮想環境を終了する時は`deactivate`を実行してください。

3. 依存関係のインストール
   以下のコードを入力してください。
   ```anaconda
   pip install -r requirements.txt

## 実行

以下のコードを入力して実行してください。

`streamlit run main.py `

## 追加インストール
pip install streamlit

pip install openai

pip install langchain

pip install load_dotenv
