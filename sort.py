def sort():
  a = [int(x) for x in input("Digite os numeros.Ex: 4 5 2 = ").split()]
  aux = 0
  title = 'Numeros desordenados: '
  tamanho = len (a)
  print (title,a)
  j = 0
  while j < tamanho :
    h = j + 1
    while h < tamanho :
      if a[j] > a[h] :
        aux = a[j]
        a[j] = a[h]
        a[h] = aux
      h += 1
    j += 1
  title = 'Numeros ordenados: '
  print (title,a)