from subprocess import check_call


for counter in range(10):
    chrome_cmd = 'export BROWSER=chrome && python3 test.py'
    firefox_cmd = 'export BROWSER=firefox && python3 test.py'
    check_call(chrome_cmd, shell=True)
    check_call(firefox_cmd, shell=True)