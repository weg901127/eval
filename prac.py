import os, subprocess

if __name__ == '__main__':
     user = dict()
     for j in range(100):
        for i in os.listdir('.'):
            if os.path.isdir('./'+i):
                k = os.system('bash prac.sh ' + i + ' > /dev/null 2>&1')
                if k == 512:
                    print(i, ':', False)
                else:
                    subprocess.check_output(['cc', 'main.c', '-I./' + i, '-L./' + i,'-lft'])
                    k = subprocess.check_output(['./a.out'])
                    try:
                        user[i] = float(user[i]) + float(k.decode('utf8'))
                    except:
                        user[i] = float(k.decode('utf8')
                        )
     print(user)