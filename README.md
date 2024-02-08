# plainWebAPI
平易化システムプロジェクトの実行環境構築手順です。


### ファイルのダウンロード
---
![code](https://github.com/ponponpurin/-/assets/125785005/41c6f9fb-5b43-44c4-aab7-040bbb3656c1)
緑色のCodeボタンをクリックして、Download zipを行い、必要なファイルをダウンロードします。  
ダウンロードしたzipファイルを**展開**します。  
ここでは、分かりやすいようにデスクトップにzipファイルを移動して展開を行うことにします。
### コマンドプロンプトの起動
---
main.pyや

### pythonのダウンロード
---
コマンドプロンプトもしくはターミナルでpython3と打つとpythonのインストールを促されるので、インストールします。  
されない場合は、Microsoft storeやブラウザでpythonをダウンロードしてください。
<https://www.python.org/>

### 仮想環境作成と起動
---
`python -m venv venv` を実行して仮想環境を作成します。  
`.\venv\Scripts\activate` で仮想環境を起動します。(windows用)  
`source env/bin/activate` で仮想環境を起動します。(Mac用)  
起動に成功するとプロンプトの先頭に(venv)と書かれます。  
仮想環境を作成する意味は、プロジェクトごとにライブラリやpythonのversionを管理できるからです。
仮想環境を終了する時は`deactivate`を実行してください。  
くわしくは[こちら](https://qiita.com/shun_sakamoto/items/7944d0ac4d30edf91fde)

### APIキーの設定
---
.envというファイルを作成し、その中にAPIキーを記入します。
```
API_KEY=
```
に続く形でキーを入力する必要があります。

### 依存関係のインストール
---
以下のコードを入力してください。
```anaconda
 pip install -r requirements.txt
```

### 実行
---
以下のコードを入力して実行してください。

`streamlit run main.py `
