from client.ChaserClient import ChaserClient

direction = "right"
 ｃｖｓｄｗｘ
def main():
    client = ChaserClient("192.168.xx.x", 2009, "test")
    client.connect()

    while True:
        # 制御コードとマップ情報を得る
        control_code, map_info = client.receive()
        # 制御コードが'0'の場合ループを抜ける
        if control_code == '0':
            break

        break
    # 今の方向をsearchする
    client.get_ready()
    if direction == "right":
        control_code, map_info = client.search_right()
    elif direction == "up":
        control_code, map_info = client.search_up()
    # left, down も同様に用意する
    client.turn_end()

    if 進める(map_info):
        client.get_ready()
        if direction == "right":
            client.walk_right()
        elif direction == "up":
            client.walk_up()
        client.turn_end()
    else:
        direction = 次の方向(direction) # 右回りに切り替える
    client.close()


if __name__ == "__main__":
    main()
