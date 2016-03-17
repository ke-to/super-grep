# -*- coding: utf-8 -*- 
#URLの重複なしリストを出力する場合

import xml.dom.minidom,os,sys,glob,re,json
import time
from threading import Timer

# 検索する文字列
search_word = raw_input(u"Search word write now! > ")
search_word = r"%s" % search_word

#URLの数だけ検索する
def fild_all_files(csvname,word,directory):
    search_data = {directory:[]}
    print u"ファイルリスト抽出中..."
    cnt = 0
    filename = "%s.txt" % csvname
    output = open(filename, 'w')
    output.writelines("「%s」内で検索した結果\n\n" % str(directory))
    output.write("対象ファイル\t該当箇所\n")
    output.writelines("")
    for root, dirs, files in os.walk(directory):
        for file_ in files:
            cnt += len(files)
            print u"検索したファイル数: %s %s" % (cnt,file_)
            full_path = os.path.join(root, file_)
            # もし対象ファイルがjspがhtmlだったらfull_pathをオープン
            if (str(full_path).find("jsp") >= 0 or str(full_path).find("html") >= 0):
                f = open(full_path)
                data = f.read() # ファイル終端まで全て読んだデータを返す
                # 1つでもヒットしたらfull_pathをjsonに格納
                file_path = full_path.replace(directory,"").replace("\\","/")
                json_data = {file_path:[]}
                # word全検索 
                search_result = re.search(search_word, data)
                if (search_result):
                    json_data[file_path].append(search_result.group())
                f.close()
                # 検索ディレクトリarrに1つの検索文言が入っているファイルのリストを追加
                if(len(json_data[file_path]) >= 1):
                    output.writelines(file_path)
                    #output.writelines('\n')
                    for result in json_data[file_path]:
                        text = "\t%s" % str(result)
                        output.writelines(text)
                    output.writelines('\n')
                    search_data[directory].append(json_data)
    output.close()
    return search_data

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