from stand_s import Stand_s
class Stand_e(Stand_s):
    def __init__(self, codice, superficie, padiglione, prezzo, prese):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.prese = prese

    def __str__(self):
        return f"{super().__init__()}{self.prese}"