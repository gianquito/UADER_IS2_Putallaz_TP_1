from pythonping import ping

class Ping:
    def execute(self, ip):
        if(ip.split(".")[0] == "192"):
            self.executefree(ip)

    def executefree(self, ip):
        for i in range(10):
            print('Intento de ping n°',i + 1, "a ip", ip)
            print(ping(ip))

class PingProxy:
    def __init__(self) -> None:
        self._klass = Ping()

    def execute(self, ip):
        if(ip == "192.168.0.254"):
            self._klass.executefree("www.google.com")
        else:
            self._klass.execute(ip)

# main
ping_proxy = PingProxy() #creo objeto proxy
ping_proxy.execute("1.1.1.1") # no se ejecuta ya que no empieza con 192.
ping_proxy.execute("192.168.0.1")
ping_proxy.execute("192.168.0.254") #ejecuta ping a google