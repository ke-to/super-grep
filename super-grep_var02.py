# -*- coding: utf-8 -*- 
#色々な条件で色々なものに置換する

import xml.dom.minidom,os,sys,glob,re,json
import time
from threading import Timer

# 検索する文字列
search_word = ["xxx","xxx"]

#URLの数だけ検索する
def fild_all_files(csvname,word,directory):
    search_arr = []
    for i in search_word:
        search_arr.append([i,[]])
    search_data = {directory:[]}
    print u"ファイルリスト抽出中..."
    cnt = 0
    filename = "%s.txt" % csvname
    output = open(filename, 'w')
    output.writelines("「%s」内で検索した結果\n\n" % str(directory))
    output.write("検索したURL\t該当ファイル\n")
    output.writelines("")
    for root, dirs, files in os.walk(directory):
        for file_ in files:
            cnt += len(files)
            print u"検索したファイル数: %s" % cnt
            full_path = os.path.join(root, file_)
            # もし対象ファイルがjspがhtmlだったらfull_pathをオープン
            if (str(full_path).find("jsp") >= 0 or str(full_path).find("html") >= 0):
                f = open(full_path)
                data = f.read() # ファイル終端まで全て読んだデータを返す
                # 1つでもヒットしたらfull_pathをjsonに格納
                file_path = full_path.replace(directory,"").replace("\\","/")
                json_data = {file_path:[]}
                # word全検索
                for i,d in enumerate(word):
                    if (data.find(d) >= 0):
                        search_arr[i][1].append(str(file_path))
                f.close()
    for i in search_arr: # [i,["","",""],[i,["","",""],
        output.writelines(i[0])
        output.writelines("\t")
        for j in i[1]: # [],[],[]
            output.writelines(j)
            output.writelines("\t")
        output.writelines("\n")
    output.close()

path01 = u"C:/Users/xxx"
data1 = fild_all_files(u"sumple_01",search_word,path01)
path02 = u"C:/xxx"
data2 = fild_all_files(u"sumple_02",search_word,path02)


print('''-------------------------------------
|           ALL COMPLATE!           |
-------------------------------------''')

def hello():
    print("closing...")

t = Timer(3.0, hello)
t.start()