#ABSTRAÇÃO
from pathlib import Path 

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Log not implemented')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_ready = f'{msg} ({self.__class__.__name__})'
        print('SALVANDO NO LOG...', msg_ready)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_ready)
            arquivo.write('\r\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')



if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_sucess('Sucesso')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa dnv')
    lf.log_sucess('Sucesso denovo')
    print(LOG_FILE)