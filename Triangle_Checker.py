class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        sides = sorted([self.a, self.b, self.c])

        for side in sides:
            if type(side) not in (int, float):
                return 1

        for side in sides:
            if side < 1:
                return 1

        if sides[0] + sides[1] < sides[2]:
            return 2

        else:
            return 3


a, b, c = input().split()  # эту строчку не менять
# здесь создайте экземпляр tr класса Triд  с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
print(tr.is_triangle('3', 4, 5))
