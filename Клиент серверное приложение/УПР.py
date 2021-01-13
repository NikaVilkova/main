import socket

def Net_in(bufnxt, FR_REC_E, FR_TRAN,REC_R,byte):
    bufend = 0
    if FR_REC_E == 0 and FR_TRAN == 0:
        if REC_R == 0 and byte == 'PRE':
            REC_R = 1
        elif REC_R == 1:
            if byte == 'EOT':
                FR_REC_E = 1
                bufend = bufnxt
                bufnxt = 0
            else:
                bufstx.append(byte)
                bufnxt += 1
    return bufnxt, FR_REC_E, FR_TRAN,bufend,REC_R

def Term_out(bufnxt, bufend, bufstx, FR_TRAN):
    if bufnxt == bufend:
        FR_TRAN = 0
        bufnxt = 0
    else:
        print(chr(int(bufstx[bufnxt])),end='')
        bufnxt += 1
    return bufnxt, bufend, bufstx, FR_TRAN

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostbyname(socket.gethostname())
    print(host)
    port = 6060
    sock.bind((host, port))
    print('Ждем сообщение...')
    while True:
        FR_REC_E = 0
        FR_TRAN = 0
        REC_R = 0
        bufstx = []
        bufnxt = 0
        bufend = 0
        while FR_REC_E == 0:
            byte, addres = sock.recvfrom(1024)
            bufnxt, FR_REC_E, FR_TRAN, bufend, REC_R = Net_in(bufnxt, FR_REC_E, FR_TRAN, REC_R, byte.decode('utf-8'))
        if FR_REC_E == 1:
            FR_REC_E = 0
            FR_TRAN = 1
            while True:
                bufnxt, bufend, bufstx, FR_TRAN = Term_out(bufnxt, bufend, bufstx, FR_TRAN)
                if FR_TRAN != 1:
                    break
