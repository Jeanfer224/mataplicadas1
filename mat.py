
precio_petr = [75.08, 75.18, 75.38, 77.65, 77.88, 78.31, 78.74]

#precio/L
precio_coca_litro = 1.12

precio_barril_coca = precio_coca_litro * 159 

relacion = [precio_barril_coca / precio for precio in precio_petr]

print("Relación de precio entre barril de Coca-Cola y barril de petróleo:", relacion)