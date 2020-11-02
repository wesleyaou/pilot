import requests
import git

pilot_ver = 'https://raw.githubusercontent.com/wesleyaou/pilot/main/version'
ver_file = 'version'

def check_conn(url='http://172.217.165.142', timeout=3):
    try:
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        return False

def ver_check(ver_url, ver_file):
    try:
        curr_ver = float(requests.get(ver_url).text)
        local_ver = float(open(ver_file, 'r').read())
        if curr_ver == local_ver:
            update_needed = 0
        elif curr_ver > local_ver:
            update_needed = 1
        elif curr_ver < local_ver:
            update_needed = 2
    except:
        update_stat = 3
    return update_needed

def pilot_update():
    try:
        if check_conn() == True:
            if ver_check(pilot_ver, ver_file) == 0:
                update_status = 'up to date'
            elif ver_check(pilot_ver, ver_file) == 1:
                pilot_repo = git.Git()
                pilot_repo.pull('origin', 'main')
                update_status = 'success'
            elif ver_check(pilot_ver, ver_file) == 2:
                update_status = 'local ahead'
            elif ver_check(pilot_ver, ver_file) == 3:
                update_status = 'failed, ver error'
            return update_status
        else:
            update_status = 'failed, error'
    except:
        update_status = 'failed, update error'
        return update_status
                
            
    
        

