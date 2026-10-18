class Stand_s:
    def __init__(self, codice_stand, superficie, padiglione, prezzo):
        self.codice_stand = codice_stand
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo

    def __repr__(self):
        return f"{self.codice_stand}, {self.superficie}, {self.padiglione}, {self.prezzo}"