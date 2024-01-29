import tkinter as tk
import deepl
import os
API_KEY=os.environ['API_KEY_DEEPL']
source_lang1 = 'JA'
target_lang1 = 'EN-US'
target_lang2 = 'EN-GB'
target_lang3 = 'ZH'
target_lang4 = 'KO'

# 初期化
translator = deepl.Translator(API_KEY)

def btn_click():
    str_JA=entry.get()
    result_1 = translator.translate_text(str_JA, source_lang=source_lang1, 
    target_lang=target_lang1)
    m3["text"] = result_1
    m3.update()
    result_2 = translator.translate_text(str_JA, source_lang=source_lang1, 
    target_lang=target_lang2)
    m4["text"] = result_2
    m4.update()
    result_3 = translator.translate_text(str_JA, source_lang=source_lang1, 
    target_lang=target_lang3)
    m5["text"] = result_3
    m5.update()
    result_4 = translator.translate_text(str_JA, source_lang=source_lang1, 
    target_lang=target_lang4)
    m6["text"] = result_4
    m6.update()


    
    
############################################################
if __name__ == "__main__":
    root=tk.Tk()
    #画面構成
    root.title("同時多言語翻訳ソフト")#タイトル
    root.geometry("600x500")#画面サイズ設定
    root.resizable(False,False)#リサイズ不可

    # == 見出し == #
    m1=tk.Label(root,text="同時言語翻訳ソフト",relief="solid",font=("メイリオ",32))
    m1.pack(pady=10)

    # == 文字入力 ==#
    entry = tk.Entry(width=40)
    entry.pack(ipady=8)

    # == ボタン　== #
    button = tk.Button(root,text="翻訳",font=("メイリオ",10),
    command=btn_click)
    button.pack(pady=10)
    # == 結果 == #
    m2 = tk.Label(root,text="-結果-アメリカ英語,イギリス英語,中国語,韓国語",font=("メイリオ",15))
    m2.pack(pady=10)
    # == English-US ==#
    m3 = tk.Label(root,text="English-American",font=("メイリオ",10))
    m3.pack(pady=10)
    # == English-GB ==#
    m4 = tk.Label(root,text="English-British",font=("メイリオ",10))
    m4.pack(pady=10)
    # == Chinise == #
    m5 = tk.Label(root,text="Chinise",font=("メイリオ",10))
    m5.pack(pady=10)
    # == Korean == #
    m6 = tk.Label(root,text="Korean",font=("メイリオ",10))
    m6.pack(pady=10)

    root.tk.mainloop()#イベントループの開始
############################################################