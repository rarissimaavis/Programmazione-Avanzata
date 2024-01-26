"""
Scrivere una classe LaureaT_Student che puo` essere osservata e che ha i seguenti attributi che ne determinano lo stato:
• total_cfu: numero cfu acquisiti
• english_r: booleano settato a False (valore di default) se e solo se lo studente non ha superato la prova di inglese
• grades: dizionario degli esami sostenuti con elementi con chiave uguale al nome dell’esame e valore uguale al voto (exam name, grade)
    • exam e` una tupla del tipo definito in basso
      Exam=collections.namedtuple("Exam", "name cfu")
Gli attributi total_cfu e english_r sono accessibili con il loro nome e modificabili con ‘=‘ mentre grades e` modificabile con il
metodo add_grades che prende in input come primo argomento un oggetto Exam e come secondo argomento un int che rappresenta il voto

Scrivere inoltre i due observer HystoryView e LiveView:
• HistoryView mantiene una lista di triple della forma (dizionario degli esami sostenuti, booleano che indica se inglese
  superato, data cambio stato). Ciascuna tripla e` creata quando l’oggetto LaureaT_Student cambia stato.
• LiveView esegue le seguenti stampe:
    • print("Cambio stato: lo studente ha appena superato la prova di Inglese\n") se il cambio di stato e` dovuto al
      superamento della prova di inglese
    • print("Cambio stato: lo studente ha superato un nuovo esame") print("Cambio stato: il numero di CFU e`: ",
      student.total_cfu,"\n") se il cambio di stato e` dovuto al superamento di un nuovo esame
"""
import collections
import copy
import datetime
import itertools
import sys
import time

Exam = collections.namedtuple("Exam", "name cfu")


def main():
    historyView = HistoryView()
    liveView = LiveView()
    student = LaureaT_Student(0)
    student.observers_add(historyView, liveView)
    print("Lo studente sta per superare analisi matematica")
    student.add_grade(Exam("analisi matematica", 9), 28)
    print("Lo studente sta per superare asistemi operativi")
    student.add_grade(Exam("sistemi operativi", 6), 20)
    print("Lo studente sta per superare la prova di Inglese")
    student.english_r = True

    for grades, flag, timestamp in historyView.data:
        print("Esami: {}, Inglese: {}, Data: {}".format(grades,
                                                        " " if flag is None else "superato" if flag else "non superato",
                                                        datetime.datetime.fromtimestamp(timestamp)), file=sys.stderr)


class Observed:
    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update((self, None))

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self, event):
        for observer in self.__observers:
            observer.update((self, event))


class LaureaT_Student(Observed):
    CFU = "cfu"
    ENG = "eng"

    def __init__(self, total_cfu, english_r=False, grades_dict=None):
        super().__init__()
        self.__total_cfu = None
        self.__english_r = False
        self.total_cfu = total_cfu
        self.english_r = english_r
        if grades_dict is not None:
            self.grades = grades_dict
        else:
            self.grades = {}

    @property
    def total_cfu(self):
        return self.__total_cfu

    @total_cfu.setter
    def total_cfu(self, total_cfu):
        if self.__total_cfu != total_cfu:
            self.__total_cfu = total_cfu
            self.observers_notify(LaureaT_Student.CFU)

    @property
    def english_r(self):
        return self.__english_r

    @english_r.setter
    def english_r(self, english_r):
        if self.__english_r != english_r:
            self.__english_r = english_r
            self.observers_notify(LaureaT_Student.ENG)

    def add_grade(self, exam, grade):
        if self.grades.get(exam.name) is None:
            self.grades[exam.name] = grade
            self.total_cfu += exam.cfu


class HistoryView:
    def __init__(self):
        self.data = []

    def update(self, model):
        student = model[0]
        self.data.append((copy.copy(student.grades), student.english_r, time.time()))


class LiveView:
    def update(self, model):
        student = model[0]
        event = model[1]

        if event is None:
            pass

        elif event == LaureaT_Student.ENG:
            print("Cambio stato: lo studente ha appena superato la prova di Inglese\n")

        elif event == LaureaT_Student.CFU:
            print("Cambio stato: lo studente ha superato un nuovo esame")
            print("Cambio stato: il numero di CFU e`: ", student.total_cfu, "\n")


if __name__ == "__main__":
    main()

"""Il programma stampa:

Lo studente sta per superare analisi matematica
Cambio stato: lo studente ha superato un nuovo esame
Cambio stato: il numero di CFU e`:  9 

Lo studente sta per superare asistemi operativi
Cambio stato: lo studente ha superato un nuovo esame
Cambio stato: il numero di CFU e`:  15 

Lo studente sta per superare la prova di Inglese
Cambio stato: lo studente ha appena superato la prova di Inglese

Esami: {}, Inglese: non superato, Data: 2019-12-10 10:54:41.413786
Esami: {'analisi matematica': 28}, Inglese: non superato, Data: 2019-12-10 10:54:41.474924
Esami: {'analisi matematica': 28}, Inglese: non superato, Data: 2019-12-10 10:54:41.658306
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: non superato, Data: 2019-12-10 10:54:41.707940
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: non superato, Data: 2019-12-10 10:54:41.908861
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: superato, Data: 2019-12-10 10:54:41.959334

"""
