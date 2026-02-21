print('Chao mung ban den voi tro choi')
print('------------------------------')
tiengoc = 10000
print('Ban se co 10,000 de lam von \nNeu su dung het ban se thua')


while True:
    try:
        #co che nhap lenh va nhap tien
        lenh = input('\nVui long nhap lenh T/t(tai) hoac X/x(xiu)\nHoac hay nhap mot ki tu bat ki de dung lai: ')
        if lenh not in ['t', 'T', 'X', 'x']:
            break
        tiencuoc = int(input('\nVui long nhap tien cuoc ban mong muon: '))
        tiengoc -= tiencuoc
        if tiengoc < 0:
            tiengoc = 10000
            tiengoc = tiengoc- int(input('\nBan khong du tien dat cuoc\nVui long nhap lai tien cuoc: '))
        
        #co che dem nguoc
        import time #dem nguoc
        n = 10
        while n > 0:
            print(n, end=' ')
            time.sleep(0.3)
            n -= 1
            if n <= 0:
                break
        
        #co che xuc xac may rui
        import random
        xucxac1 = random.randint(1,6)
        xucxac2 = random.randint(1,6)
        xucxac3 = random.randint(1,6)
        ketqua = xucxac1 + xucxac2 + xucxac3
        if ketqua < 11:
            print(ketqua)
            print('\nXiu')
            if lenh in ['t', 'T']:
                print('\nBan da thua')
                print(f'So tien con lai cua ban: {tiengoc}')
                if tiengoc <= 0:
                    print('Ban da het tien')
                    break
            elif lenh in ['x', 'X']:
                    print('\nBan da thang!!')
                    tiengoc = tiengoc + tiencuoc*2
                    print(f'So tien con lai cua ban: {tiengoc}')
        elif ketqua >= 11:
                print('Tai')
                if lenh in ['x', 'X']:
                    print('\nBan da thua')
                    print(f'So tien con lai cua ban: {tiengoc}')
                    if tiengoc <= 0:
                        print('Ban da het tien')
                        break
                elif lenh in ['t', 'T']:
                    print('\nBan da thang!!')
                    tiengoc = tiengoc + tiencuoc*2
                    print(f'So tien con lai cua ban: {tiengoc}')
    except ValueError:
        print('Du lieu ban nhap vao khong hop le')
    except EOFError:
        print('Hay nhap so tien ban muon')