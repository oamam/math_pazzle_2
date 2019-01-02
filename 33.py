def main():
    '''
    義務チョコ: x >= 0
    義理チョコ: y >= 0
    本命チョコ: m - (x + y) >= 0

    チョコの種類に応じて必要になるチョコの数(1)
    x + 2y + 3(m - x - y) = n
    x + 2y + 3m - 3x - 3y = n
    y = -2x - n + 3m

    義理チョコが 0 個のときの義務チョコの数
    x = (3m - n) / 2

    本命チョコが 0 個のときの義理チョコと義務チョコの数(2)
    m - (x + y) = 0
    y = -x + m

    本命チョコが 0 個のときの義務チョコの数(3)
    -2x - n + 3m = -x + m
    x = 2m - n

    義理チョコと本命チョコが 1 個以上のときの義務チョコの数
    (3m - n) / 2 - 2m + n
    '''
    M = 543210
    N = 987654

    # 最後の 1 は本命チョコも義理チョコも 0 個のときのパターン
    print((3 * M - N) // 2 - (2 * M - N) + 1)


if __name__ == '__main__':
    main()
