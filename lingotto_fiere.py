from importlib.metadata import pass_none


from stand_s import Stand_s
from stand_e import Stand_e
from stand_p import Stand_p
from espositore import Espositore


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.codici_stands = []
        self.codici_espositori = []
        self.stand_assegnare = None
        self.diz = {}
        self.lista_diz = []


    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, "r") as file:
                for riga in file:
                    riga = riga.strip()
                    campi = riga.split(",")
                    if len(campi) == 3:
                        codice = campi[0]
                        nome = campi[1]
                        cognome = campi[2]
                    elif len(campi) == 4:
                        codice = campi[0]
                        superficie = campi[1]
                        padiglione = campi[2]
                        prezzo = campi[3]
                    elif len(campi) == 5:
                        codice = campi[0]
                        superficie = campi[1]
                        padiglione = campi[2]
                        prezzo = campi[3]
                        special = campi[4]
                    else:
                        return None



                    if riga.startswith("S") and len(campi) == 4:
                        stand_s = Stand_s(codice, superficie, padiglione, prezzo)
                        self.codici_stands.append(stand_s.codice_stand)
                    if riga.startswith("S") and len(campi) == 5:
                        if isinstance(special, int):
                            prese = special
                            stand_e = Stand_e(codice, superficie, padiglione, prezzo, prese)
                            self.codici_stands.append(stand_e.codice_stand)
                        else:
                            premium = special
                            stand_p = Stand_p(codice, superficie, padiglione, prezzo, premium)
                            self.codici_stands.append(stand_p.codice_stand)
                    if riga.startswith("E"):
                        espositore = Espositore(codice, nome, cognome)
                        self.codici_espositori.append(codice)



            file.close()



        except FileNotFoundError:
            print("Errore nell'apertura del file")
            return None





    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.codici_stands:
            raise ValueError(f"Errore: Lo stand {codice_stand} non esiste.")
        if codice_espositore not in self.codici_espositori:
            raise ValueError(f"Errore: L'espositore {codice_espositore} non esiste.")

        if codice_stand in self.diz.values():
            raise ValueError(f"Errore: Lo stand {codice_stand} è già stato assegnato a un altro espositore.")
        if codice_espositore in self.diz:
            raise ValueError(f"Errore: L'espositore {codice_espositore} ha già uno stand assegnato.")

        self.diz[codice_espositore] = codice_stand









    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        if not self.codici_espositori:
            print("Nessun espositore presente a sistema.")
            return

        for cod_esp in self.codici_espositori:
            stand_assegnato = self.diz.get(cod_esp)
            if stand_assegnato:
                print(f"Espositore: {cod_esp} -> Stand assegnato: {stand_assegnato}")
            else:
                print(f"Espositore: {cod_esp} -> Nessuno stand assegnato")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        prezzi_stand = []

        try:
            with open("dati_lingotto.csv", "r") as file:
                for riga in file:
                    campi = riga.strip().split(",")
                    if riga.startswith("S") and len(campi) >= 4:
                        codice = campi[0]
                        prezzo_base = float(campi[3])


                        if len(campi) == 4:
                            prezzo_finale = prezzo_base
                        elif len(campi) == 5:
                            special = campi[4]
                            if special.isdigit():
                                prezzo_finale = prezzo_base * (1 + 0.07 * int(special))
                            else:
                                prezzo_finale = prezzo_base * 1.30


                        prezzi_stand.append({"codice": codice, "prezzo": prezzo_finale})
        except FileNotFoundError:
            print("Impossibile recuperare i prezzi: file non trovato.")
            return []

        stand_ordinati = sorted(prezzi_stand, key=lambda s: s["prezzo"])

        risultato = []
        for s in stand_ordinati:
            risultato.append(f"Stand: {s['codice']} - Prezzo: {s['prezzo']:.2f}€")

        return risultato
