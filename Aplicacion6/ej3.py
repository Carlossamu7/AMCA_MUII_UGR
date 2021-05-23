""" Realiza el algoritmo Haar Wavelet de manera. Devuelve una lista con los coeficientes.
- list: lista a la que hacer el split de haar.
- p: normalizado en Lp. Si p=0 entonces los coeficientes son sin normalizar.
"""
def haar_transform(list, p):
    if(p==0):
        val=2
    else:
        val = 2**((p-1)/p)

    # Función recursiva con las particiones
    haar = haar_split(list, [], val)

    # Normalizado uniforme
    if(p!=0):
        for i in range(len(haar)):
            haar[i] = haar[i] / (len(haar)**(1/p))

    return haar

""" Realiza el algoritmo Haar Wavelet de manera recursiva realizando las particiones
adecuadas y calculando sus medias y diferencias. Devuelve una lista con los coeficientes.
- list: lista a la que hacer el split de haar.
- offset: parte fija del split.
"""
def haar_split(list, offset, value):
    if(len(list) >= 2):
        avgs = []
        difs = []
        for i in range(0, len(list), 2):
            avgs.append((list[i] + list[i+1]) / value)
            difs.append((list[i] - list[i+1]) / value)
        return haar_split(avgs, difs + offset, value)

    else:
        return list + offset

print("Compresión de Haar sin normalización:\n{}\n".format(haar_transform([1, 3, 7, 9, 8, 8, 6, 2], 0)))

print("Compresión de Haar normalizado en L2:\n{}\n".format(haar_transform([1, 3, 7, 9, 8, 8, 6, 2], 2)))
