import sys, os
import SimpleHTTPServer, SocketServer

os.chdir("htdocs")

try:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
except:
    HOST = "localhost"
    PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
try:
    httpd = SocketServer.TCPServer((HOST, PORT), Handler)
except:
    PORT += 1
    httpd = SocketServer.TCPServer((HOST, PORT), Handler)

print "Servidor funcionando en", HOST + ":" + str(PORT)
print "Para detener el servidor usa la combinacion de teclas 'CTRL + C'"

try:    
    httpd.serve_forever()
except:    
    httpd.server_close()