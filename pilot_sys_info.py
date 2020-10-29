import psutil

def CPUGetState():
    return str(psutil.cpu_percent())
    
