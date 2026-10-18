class Espositore:
    def __init__(self, codice_espositore, nome, cognome):
        self.codice_espositore = codice_espositore
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"{self.codice_espositore}{self.nome}{self.cognome}"