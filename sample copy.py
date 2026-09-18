from client.ChaserClient import ChaserClient


def main():
    client = ChaserClient("192.168.xx.x", 2009, "test")
    client.connect()

    while True:
        # 制御コードとマップ情報を得る
        control_code, map_info = client.receive()
        # 制御コードが'0'の場合ループを抜ける
        if control_code == '0':
            break
        
        client.get_ready()
        client.search_left()
        client.turn_end()

        clientclient.get_ready()
        client.search_left()
        client.turn_end()

    client.close()


if __name__ == "__main__":
    main()
