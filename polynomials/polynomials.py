from numbers import Number, Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented
        
    def __radd__(self, other):
        return self + other

    """
    def __sub__(self, other):
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients, other.coefficients[:common1])]
            for i in range(common1, common2 + 1):
                if len(self.coefficients) >= len(other.coefficients):
                    coefs1.append(self.coefficients[i]) 
                
                else: 
                    coefs1.append(other.coefficients[i])
            
            return Polynomial(coefs1)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __rsub__(self, other):
        return other - self
    
    def __mul__(self, other):
        if isinstance(other, Polynomial):
            # create new list 
            result_coeffs = [0] * (self.degree() + other.degree() + 1) 
            for i in range(self.degree()):
                for j in range(other.degree()):
                    result_coeffs[i+j] += self.coefficients[i] * other.coefficients[j]

            return Polynomial(result_coeffs)
        
        elif isinstance(other, Number):
            return Polynomial( other * self.coefficients[i] for i in self.degree())   
        
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        return other * self
    
    def __pow__(self, other):
        if isinstance(other, Number) and other == 1:
            return self
        
        elif isinstance(other, Number) and other > 1 :
            
            res_coeffs = [0] * ((self.degree() * other) + 1)

           # polynomial 같은 걸 곱하는 걸 n-1번 
            for i in range(other-1):
                 # 같은 polynomial 두 번 곱한 거임 
                for i in range(self.degree()):
                    for j in range(self.degree()):
                        res_coeffs[i+j] += self.coefficients[i] * self.coefficients[j]     

        else: 
            return NotImplemented
    
    def __call__(self):
        if isinstance(x, Number):
            return sum([a * x**n for a, n in zip(self.coefficients,
                                                 range(self.degree() + 1))])
        else:
            return NotImplemented
    
    def dx(self):
        if isinstance(self, Polynomial):
            # multiplying coefficients with its degree
            derivative_list = [ index * coeff for index , coeff in enumerate(self.coefficients[1:], start = 1)]
            # moving the degree 1 lower 
            return Polynomial(derivative_list)
        
        elif isinstance(self, Number):
            return Polynomial(0)
    """
    
    def __neg__(self):
        return Polynomial(tuple(-x for x in self.coefficients))


    def __sub__(self, other):
        if isinstance(other, Polynomial):
            return self.__add__(other.__neg__())
        elif isinstance(other, Number):
            return self.__add__(- other)  # where - other is well defined
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Polynomial) or isinstance(other, Number):
            return -self + other
            # "self.__neg__().__add__(other)"

    def __mul__(self, other):
        # Polynomial multiplication
        if isinstance(other, Polynomial):
            boo = (self.degree() < other.degree())
            p, q = (self, other) if boo else (other, self)
            # p is the polynomial with smaller degree
            a, m = p.coefficients, p.degree()
            b, n = q.coefficients, q.degree()

            coef1 = [sum([a[i] * b[k - i] for i in range(k + 1)]) for k in range(m)]
            coef2 = [sum([a[i] * b[k - i] for i in range(m + 1)]) for k in range(m, n + 1)]
            coef3 = [sum([a[m - i] * b[k + i - m] for i in range(n + m - k + 1)]) for k in range(n + 1, m + n + 1)]
            
            return Polynomial(tuple(coef1 + coef2 + coef3))
 
        elif isinstance(other, Number):
            coefs = tuple(other * a for a in self.coefficients)
            return Polynomial(coefs)

        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, number):
        p0 = self
        p = p0
        if isinstance(number, Integral):
            for n in range(number - 1):
                p0 = p0 * p
            return p0
        else:
            return NotImplemented

    def __call__(self, x): 
        if isinstance(x, Number):
            return sum([a * x**n for a, n in zip(self.coefficients,
                                                 range(self.degree() + 1))])
        else:
            return NotImplemented

    
    def dx(self):
        new_coefficients = []
        if len(self.coefficients) > 1:
            for i in range(1, Polynomial.degree(self)+1):
                new_coefficients.append(self.coefficients[i]*(i))
            newcoefs = tuple(new_coefficients)
            return Polynomial(newcoefs)
        
        else:
            return Polynomial((0,))

def derivative(polynomial):
    return polynomial.dx()
