a=float(input("Введите положение точки А на оси: "))
b=float(input("Введите положение точки B на оси: "))
c=float(input("Введите положение точки C на оси: "))
dlac=abs(a-c)
dlbc=abs(b-c)
print("Длинна отрезка AC равна ", dlac, "\n"
      "Длинна отрезка AB равна ", dlbc, "\n"
      "Их сумма равна", dlac+dlbc)
