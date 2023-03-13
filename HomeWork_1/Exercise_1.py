side_a = int(input("Side a: "))
side_b = int(input("Side b: "))
side_c = int(input("Side c: "))

if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
    print("there is no such triangle")
elif side_a == side_b and side_b == side_c:
    print("equilateral triangle")
elif side_a == side_b or side_b == side_c or side_a == side_c:
    print("isosceles triangle")
else:
    print("the versatile triangle")