from executar import pesquisar

import time
import schedule

schedule.every(15).minutes.do(pesquisar)

while True:
    schedule.run_pending()
    time.sleep(1)