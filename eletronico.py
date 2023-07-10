from log import LogFileMixin

class Eletronico:
    def __init__(self, name):
        self._name = name
        self._on = False


    def on(self):
        if not self._on:
            self._on = True

    
    def off(self):
        if self._on:
            self._on = False


class Smartphone(Eletronico, LogFileMixin):
    def on(self):
        super().on()

        if self._on:
            msg = f'{self._name} is on'
            self.log_sucess(msg)

    def off(self):
        super().off()
        
        if not self._on:
            msg = f'{self._name} is off'
            self.log_error(msg)