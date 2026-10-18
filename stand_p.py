from stand_s import Stand_s
class Stand_p(Stand_s):
    def __init__(self, codice, superficie, padiglione, prezzo, premium):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.premium = premium

    def __str__(self):
        return f"{super().__init__()}{self.premium}"