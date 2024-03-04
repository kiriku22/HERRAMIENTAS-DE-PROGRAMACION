class Asignatura:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos
        self.notas = {}

    def agregar_nota(self, nombre_nota, valor, porcentaje):
        if nombre_nota in self.notas:
            print(f"Ya existe una nota con el nombre '{nombre_nota}'. Se actualizará el valor y porcentaje.")
        self.notas[nombre_nota] = {'valor': valor, 'porcentaje': porcentaje}
        print(f"Nota '{nombre_nota}' agregada correctamente a '{self.nombre}'.")

    def calcular_promedio_acumulado(self):
        if not self.notas:
            print("No hay notas registradas para esta asignatura.")
            return 0, 0, {}

        total_puntos = sum(nota['valor'] * nota['porcentaje'] / 100 for nota in self.notas.values())
        porcentaje_total = sum(nota['porcentaje'] for nota in self.notas.values())
        notas_faltantes = {}
        if porcentaje_total < 100:
            porcentaje_faltante = 100 - porcentaje_total
            notas_faltantes = {nombre: porcentaje['porcentaje'] for nombre, porcentaje in self.notas.items() if porcentaje['porcentaje'] < porcentaje_faltante}
        else:
            porcentaje_faltante = 0
        return total_puntos, porcentaje_faltante, notas_faltantes

    def calcular_promedio_minimo(self, nota_deseada):
        if not self.notas:
            print("No hay notas registradas para esta asignatura.")
            return 0

        total_puntos = self.calcular_promedio_acumulado()[0]
        puntos_faltantes = nota_deseada - total_puntos
        porcentaje_restante = 100 - sum(nota['porcentaje'] for nota in self.notas.values())
        if porcentaje_restante == 0:
            print("Error: No se puede calcular el promedio mínimo, el porcentaje total de las notas ya es 100%.")
            return

        promedio_minimo = puntos_faltantes / (porcentaje_restante / 100)
        return promedio_minimo