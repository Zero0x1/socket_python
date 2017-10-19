import sys
import socket

def main():
  host = socket.gethostbyname(sys.argv[1])

  try:
    for port in range(1, 65535):
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = sock.connect_ex((host, port))
      if result == 0:
        print "Port {}:    is Open".format(port)
      sock.close()

  except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

  except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

  except socket.error:
    print "Couldn't connect to server"
    sys.exit()

  print 'Scanning Completed'

if __name__ == "__main__":
  main()
