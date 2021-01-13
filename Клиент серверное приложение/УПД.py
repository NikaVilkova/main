import socket

def Term_in(bufnxt, FR_REC_E, FR_TRAN):
    bufend = 0
    while True:
        str = input('Введите строку(не больше 80 символов): ')+'`'
        if len(str) <= 80:
            break
    for byte in str:
        if byte == '`':
            bufstx.append(ord('\r'))
            bufnxt += 1
            bufstx.append(ord('\n'))
            bufnxt += 1
            bufstx.append('EOT')
            bufend = bufnxt + 1
            bufnxt = 0
            FR_REC_E = 1
        elif FR_REC_E == 0 and FR_TRAN == 0:
            bufstx.append(ord(byte))
            bufnxt += 1
    return bufnxt, FR_REC_E, FR_TRAN, bufend

def Net_out(bufnxt, bufend, bufstx, FR_TRAN):
    if bufnxt == bufend:
        FR_TRAN = 0
        bufnxt = 1
    else:
        s.sendto(str(bufstx[bufnxt]).encode('utf-8'), server)
        bufnxt += 1
    return bufnxt, bufend, bufstx, FR_TRAN

if __name__ == '__main__':
    port = 0
    host = input('Введите Ip адрес приемника: ')
    server = (host, 6060)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', port))
    s.setblocking(1)
    while True:
        FR_REC_E = 0
        FR_TRAN = 0
        bufstx = ['PRE']
        bufnxt = 1
        bufnxt, FR_REC_E, FR_TRAN, bufend = Term_in(bufnxt, FR_REC_E, FR_TRAN)
        if FR_REC_E == 1:
            FR_TRAN = 1
            FR_REC_E = 0
            while True:
                bufnxt, bufend, bufstx, FR_TRAN = Net_out(bufnxt, bufend, bufstx, FR_TRAN)
                if FR_TRAN != 1:
                    break
