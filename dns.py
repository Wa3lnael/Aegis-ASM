import socket
def run(target):
    try:
        return socket.gethostbyname_ex(target)
    except:
        return None
