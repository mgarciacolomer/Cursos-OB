import time as t

def main():
    horaSalida = 19
    structTime = t.localtime(t.time())

    if structTime.tm_hour >= horaSalida:
        print('Hora de ir a casa')
    else:
        remainingSec = 60 - structTime.tm_sec
        remainingMin = 60 - structTime.tm_min - 1            # REMINDER
        remainingHour = horaSalida - structTime.tm_hour - 1  # REMINDER

        print('Todavía quedan', remainingHour, 'horas', remainingMin, 'minutos y', remainingSec, 'segundos')


if __name__ == '__main__':
    main()