# Alat Konversi Suhu Temperatur

print("\nPROGRAM KONVERSI SUHU TEMPERATUR\n")

# Celcius
C = float(input("Masukkan temperatur dalam Celcius: "))
print("Suhu sekarang adalah ", C, 'Celcius')

R = (4/5) * C           #Reamur
F = (9/5) * C + 32      #Fahrenheit
K = C + 273             #Kelvin

print("Suhu dalam Reamur menjadi ", R, 'Reamur')
print("Suhu dalam Fahrenheit menjadi ", F, 'Fahrenheit')
print("Suhu dalam Kelvin menjadi ", K, 'Kelvin')

print("\n=============KONVERSI FAHRENHEIT KE KELVIN====================")

F = float(input("Masukkan temperatur dalam Fahrenheit : "))
print("suhu sekarang adalah ", F, 'Fahrenheit')

K = ((5/9) * (F - 32)) + 273

print("Suhu dalam Fahrenheit menjadid ", K, 'Kelvin')



print("\n============KONVERSI KELVIN KE FAHRENHEIT=====================")

K = float(input("Masukkan temperatur dalam Kelvin : "))
print("suhu sekarang adalah ", K, 'Kelvin')

F = ((9/5) * (K - 273)) + 32

print("Suhu dalam Fahrenheit menjadid ", F, 'Fahrenheit')
