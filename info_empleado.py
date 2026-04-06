nombre = input("Introduce tu nombre: ")
cargo = input("Introduce tu cargo: ")
añosexp = int(input("Introduce tus años de experiencia: "))

def datos_empleado(mi_nombre,mi_cargo,mi_añosexp):
            print("El empleado " 
                + str(mi_nombre) + " trabaja como " + str(mi_cargo) + " y tiene "
                + str(mi_añosexp) + " años de experiencia")
            if mi_añosexp>5:
                print("Empleado con experiencia senior")
            return
datos_empleado(nombre,cargo,añosexp)

#ejemplos
datos_empleado("mauricio","programador ",4)
datos_empleado("paul","Dev",7)

class NetworkDevice:
    def __init__(self, name,ip_address,device_type):
        self.name = name
        self.ip_address = ip_address
        self.device_type = device_type

    def showinfo(self):
            mi_name = self.name
            mi_ip_address = self.ip_address
            mi_device_type = self.device_type

            print("Diospositivo: <" 
                + str(mi_name) + "> | IP: <" + mi_ip_address + "> | Tipo: <"
                + str(mi_device_type) + ">")

    def pingTest(self):
        print("Realizando ping al dispositivo <" + self.name + ">...")
dev1= NetworkDevice("Router1","10.0.0.1","Router")
dev2= NetworkDevice("Switch","10.0.0.2","Switch")
dev3= NetworkDevice("Firewall","10.0.0.3","Firewall")

dev1.showinfo()
dev2.showinfo()
dev3.showinfo()

