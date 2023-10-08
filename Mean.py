class School:

    def __init__(self, note_total):
        self._note_total = note_total

    @property
    def code_notes(self):
        return self._note_total
    
    @code_notes.setter
    def note_total(self,value):
        if value >= 7:
            print("Parabéns, passou de ano")
        elif value <= 6.9 and value >= 5:
            print("Recuperação")
        else:
            print('Até ano que vem')

notas = School(10)
print(notas.code_notes)