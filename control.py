from random import randint
import time


class Processo:

    def __init__(self, idf):
        self.idf = idf
        self.texec = randint(1, 100)

    def __str__(self):
        return f'Processo {self.idf} - tempo restante para executar: {self.texec}'


class ListaProcessos:

    def __init__(self, procs=None):
        if procs is None:
            procs = list()
        self.procs = procs

    def add_proc(self, proc):
        self.procs.append(proc)

    def del_proc(self, proc):
        tipo = type(proc)
        if tipo is int:
            index = -1
            for p in range(len(self.procs)):
                if self.procs[p].idf == proc:
                    index = p
                    break
            if index > -1:
                return self.procs.pop(index)
            else:
                return None

        elif tipo is Processo:
            return self.procs.pop(self.procs.index(proc))
        else:
            return None

    def ordena_processos(self):
        self.procs.sort(key=lambda x: x.texec)

    def fila2str(self):
        strg = '|- '

        for p in self.procs:
            strg += f'Pr{p.idf}({p.texec}) -> '
        strg += '-|'
        return strg

    def copy(self):
        return ListaProcessos(list(self.procs))

    def executar_ucp(self, func_result, func_fila, func_msg=None):
        self.ordena_processos()
        func_fila(self.fila2str())
        if len(self.procs):
            proc_e = self.procs.pop(0)
            if func_msg:
                while proc_e.texec > 0:
                    proc_e.texec -= 1
                    time.sleep(1)
                    func_msg(str(proc_e))

            if func_result:
                func_result(f'Processo {proc_e.idf} executado completamente')
                return proc_e
            else:
                return None

        else:
            func_result('Fila vazia')
            return None
