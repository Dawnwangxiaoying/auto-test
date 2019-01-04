#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: UTF-8 -*-
import os

apk = {'alpha': 'com.icourt.alpha',
       'note': 'com.icourt.alphanote',
        'echo': 'com.icourt.alphanews'}
while True:

    test_apk = input('which apk do you want to test?\n(\'alpha\' or \'note\' or \'echo\'):')

    try:
        apk_name = apk[test_apk]
    except KeyError:
        print('Please enter \'alpha\' or \'note\' or \'echo\'!')
    else:
        break
while True:
    event_num = input('How many pseudo random events do you want?\nenter int num(>0):')
    if event_num.isdigit() and int(event_num) > 0:
        print('OK, your events are ' + event_num)
        break
    else:
        print('Please enter a number and the number > 0')

while True:
    for_time = input('How many time series seed value do you want?\ntimes(>1):')
    if for_time.isdigit() and int(for_time) > 1:
        print('OK, you want to loop ' + for_time + 'time series seed')
        break
    else:
        print('Please enter a number and the number > 1')



# the log path
log_path = './monkey.txt'

# monkey shell script
monkey_shell = 'adb shell monkey -p ' + apk_name + ' -s ' + for_time + ' --ignore-crashes --ignore-timeouts --monitor-native-crashes -v -v -v ' + event_num + ' > ' + log_path


def monkeytest():
    print('now let\'s check your phone')
    phonedevice = os.popen('adb devices').read()
    if phonedevice.strip().endswith('device'):
        print('OK, your phone get ready,let\'s start moneky test!')
        os.system(monkey_shell)
        print('OK, moneky test all complete! The log is in root directory named monkey.txt')
    else:
        print('please check your phone has linked your computer well')


# find 'adb' command at your os
sysPath = os.environ.get('PATH')
if not sysPath.find('platform-tools'):
    print('''please install the android-sdk and put the 'platform-tools' dir in your system PATH''')

else:
    monkeytest()

