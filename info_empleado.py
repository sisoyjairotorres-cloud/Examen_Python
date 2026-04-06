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
