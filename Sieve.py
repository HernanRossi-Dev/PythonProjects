class Sieve:
    def __init__(self, input):
        self.value = input
        self.matrix = [False if x < 2 else True for x in range(0, input + 1)]
        
    def start(self):
        primes = []
        for i in range(2, self.value + 1):
            if self.matrix[i]:
                primes.append(i)
                mult = 1
                multsOfPrime = i * mult
                while multsOfPrime <= self.value:
                    print('Mult: ', multsOfPrime, len(self.matrix))
                    self.matrix[multsOfPrime] = False
                    mult = mult + 1
                    multsOfPrime = i * mult
        return primes

sieve = Sieve(500)
print('List of primes {} {}'.format(500, sieve.start()))
