# plainWebAPI

このプロジェクトの実行環境構築手順でーす。

anacondaで実行することを想定して手順を解説します。
## インストール
1. git bashなどでリポジトリをクローンします：
git bashでプロジェクトを配置したいディレクトリに移動して以下のコマンドを入力してください。
例えば、デスクトップにpblっていうフォルダを作ってその中にクローンするなど。
   ```bash
   git clone https://github.com/ponponpurin/-.git
これで私のリポジトリのファイルがカレントディレクトリに作成されます。

2. 仮想環境の作成と実行
anconda プロンプトを開いてリポジトリをクローンしたディレクトリに移動します。pblというフォルダにクローンしたなら
pbl内の-というディレクトリに移動して、

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
