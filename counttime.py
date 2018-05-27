import random
import time


def Count(timeInit, timeEnd):

    tempo = str(timeEnd - timeInit)  # Minha contribuição ao código

    if (float(tempo)) >= 60:
        return "Tempo de Execução: %s min" % str((float(tempo)/60))
    elif tempo[len(tempo) - 3] == '-':
        return "Tempo de Execução: %s ms" % (tempo)
    else:
        return "Tempo de Execução: %s sec" % (tempo)

