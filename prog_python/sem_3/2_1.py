def main():
  mass_1 = list(map(int, input().split()))
  mass_2 = list(map(int, input().split()))

  new_mass = []
  last_mass_2_elem = 0
  for elem in mass_1:
    while len(mass_2) > last_mass_2_elem and  elem > mass_2[last_mass_2_elem]:
      new_mass.append(mass_2[last_mass_2_elem])
      last_mass_2_elem += 1
    new_mass.append(elem)
  while len(mass_2) > last_mass_2_elem:
     new_mass.append(mass_2[last_mass_2_elem])
     last_mass_2_elem += 1
  print(new_mass)




if __name__ == "__main__":
	main()
