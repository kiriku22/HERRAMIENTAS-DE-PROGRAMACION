from asignatura import Asignatura

class CalculadoraNotas:
    asignaturas = []

    @classmethod
    def agregar_asignatura(cls, asignatura):
        cls.asignaturas.append(asignatura)

    @classmethod
    def mostrar_catalogo_asignaturas(cls):
        print("Catálogo de Asignaturas:")
        for i, asignatura in enumerate(cls.asignaturas, start=1):
            print(f"{i}. {asignatura.nombre}")

    @classmethod
    def obtener_asignatura_por_indice(cls, indice):
        if 1 <= indice <= len(cls.asignaturas):
            return cls.asignaturas[indice - 1]
        else:
            return None

    @staticmethod
    def ejecutar():
        while True:
            print("\n--- Calculadora de Notas ---")
            print("1. Agregar nueva asignatura")
            print("2. Seleccionar una asignatura del catálogo")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
                creditos_asignatura = int(input("Ingrese el número de créditos de la asignatura: "))
                asignatura = Asignatura(nombre_asignatura, creditos_asignatura)
                CalculadoraNotas.agregar_asignatura(asignatura)
                print(f"Asignatura '{nombre_asignatura}' agregada correctamente.")

            elif opcion == "2":
                if not CalculadoraNotas.asignaturas:
                    print("No hay asignaturas registradas.")
                    continue
                
                CalculadoraNotas.mostrar_catalogo_asignaturas()
                indice_seleccionado = int(input("Seleccione una asignatura del catálogo (ingrese el número correspondiente): "))
                asignatura_seleccionada = CalculadoraNotas.obtener_asignatura_por_indice(indice_seleccionado)
                
                if asignatura_seleccionada:
                    CalculadoraNotas.menu_asignatura(asignatura_seleccionada)
                else:
                    print("¡Opción inválida!")

            elif opcion == "3":
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    @staticmethod
    def menu_asignatura(asignatura):
        while True:
            print(f"\n--- Asignatura: {asignatura.nombre} ---")
            print("1. Agregar nota")
            print("2. Calcular promedio acumulado")
            print("3. Calcular promedio mínimo necesario para una nota deseada")
            print("4. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre_nota = input("Ingrese el nombre de la nota: ")
                valor_nota = float(input("Ingrese el valor de la nota: "))
                porcentaje_nota = float(input("Ingrese el porcentaje de la nota con respecto al total: "))
                asignatura.agregar_nota(nombre_nota, valor_nota, porcentaje_nota)

            elif opcion == "2":
                promedio_acumulado, porcentaje_faltante, notas_faltantes = asignatura.calcular_promedio_acumulado()
                print(f"El promedio acumulado de '{asignatura.nombre}' es: {promedio_acumulado:.2f}")
                if porcentaje_faltante > 0:
                    print("Faltan notas o porcentaje para totalizar el 100%:")
                    for nombre, porcentaje in notas_faltantes.items():
                        print(f" - {nombre}: {porcentaje}%")

            elif opcion == "3":
                nota_deseada = float(input("Ingrese la nota deseada: "))
                promedio_minimo = asignatura.calcular_promedio_minimo(nota_deseada)
                if promedio_minimo:
                    print(f"El promedio mínimo necesario para obtener {nota_deseada} en '{asignatura.nombre}' es: {promedio_minimo:.2f}")

            elif opcion == "4":
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    CalculadoraNotas.ejecutar()