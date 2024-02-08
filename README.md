# plainWebAPI
平易化システムプロジェクトの実行環境構築手順です。

### ファイルのダウンロード
ダウンロード後展開を行う。

### コマンドプロンプトの起動

### pythonのダウンロード

### 仮想環境作成と起動
`python -m venv venv` を実行して仮想環境を作成します。
`.\venv\Scripts\activate` で仮想環境を起動します。
起動に成功するとプロンプトの先頭に(venv)と書かれます。
仮想環境を作成する意味は、プロジェクトごとにライブラリやpythonのversionを管理できるからです。
仮想環境を終了する時は`deactivate`を実行してください。

### 依存関係のインストール
以下のコードを入力してください。
```anaconda
   pip install -r requirements.txt

### 実行

以下のコードを入力して実行してください。

`streamlit run main.py `
