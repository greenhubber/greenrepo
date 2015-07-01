import socket
import paramiko
import threading
import sys
 
host_key = paramiko.RSAKey("this_is_a_bad_rsa_key")
 
class Server (paramiko.ServerInterface):
   def _init_(self):
       self.event = threading.Event()
   def check_channel_request(self, kind, chanid):
       if kind == 'session':
           return paramiko.OPEN_SUCCEEDED
       return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
   def check_auth_password(self, username, password):
       if (username == 'root') and (password == 'yeah_i_am_in'):
           return paramiko.AUTH_SUCCESSFUL
       return paramiko.AUTH_FAILED
 
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('10.0.2.15', 22))
    sock.listen(100)
    print '[+] Listening for connection ...'
    client, addr = sock.accept()
except Exception, e:
    print '[-] Listen/bind/accept failed: ' + str(e)
    sys.exit(1)
print '[+] Got a connection!'
 
try:
    t = paramiko.Transport(client)
    try:
        t.load_server_moduli()
    except:
        print '[-] (Failed to load moduli -- gex will be unsupported.)'
        raise
    t.add_server_key(host_key)
    server = Server()
    try:
        t.start_server(server=server)
    except paramiko.SSHException, x:
        print '[-] SSH negotiation failed.'
 
    chan = t.accept(20)
    print '[+] Authenticated!'
    print chan.recv(1024)
    chan.send('Yeah i can see this')
 
except Exception, e:
    print '[-] Caught exception: ' + str(e. class ) + ': ' + str(e)
    try:
        t.close()
    except:
        pass
    sys.exit(1)
