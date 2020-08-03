class Polynomial:
    def __init__(self, *coeff):
        self.coeff = [c for c in coeff]
        print(self.coeff)

    def __str__(self):
        st = []
        for i in range(len(self.coeff)):
            st.append(f"{self.coeff[i]}*x^{len(self.coeff)-i-1}")
        return " + ".join(st)

    def __call__(self, x):
        res = 0
        for i in range(len(self.coeff)):
            res += self.coeff[i] * x ** (len(self.coeff)-i-1)
        return res


p = Polynomial(5,1,2)
print(str(p))
print(p(2))

p2 = Polynomial(4,5,4,1,2,3)
print(p2)