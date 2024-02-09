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
![1707412221314](https://github.com/ponponpurin/-/assets/125785005/88c055c3-bb37-482f-8428-bdac15f7af8a)
展開したフォルダ内に入り、赤枠の部分でcmdと入力し、コマンドプロンプトを起動します。  
macの場合は展開したフォルダに右クリックし、「フォルダに新規ターミナル」もしくは「フォルダに新規ターミナルタブ」をクリックで起動してください。  
くはしくは、[こちら](https://aadojo.alterbooth.com/entry/2023/01/17/110000)


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
以下の＝につながる形でコマンドプロンプトでAPIキーを入力して実行してください
set OPENAI_API_KEY=

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

## 評価指標について
**BLUE**
janomeをトークナイザーに用い、nltkのsentence_blueを用いて実装した。

**SARI**
janomeをトークナイザーを使い、fuggingfaceのevaluateライブラリで実装した。
