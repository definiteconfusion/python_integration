import subprocess

class Binary:
    def __init__(self, name='binary', *args):
        self.name = name
        self.args = args
        
    def get(self, *args):
        base_schema = [
                self.name,
            ]
        if len(args) == 0:
            for value in self.args:
                base_schema.append(str(value))
        else:
            for value in args:
                base_schema.append(str(value))
        out = str(subprocess.run(
            base_schema,
            capture_output=True,
            text=True
        ).stdout).split('\n')[:-1]
        if len(out) == 1:
            return out[0]
        elif len(out) == 0:
            return None
        else:
            print(out)
            return tuple(out)
        
def Run(name, *args):
    TempApp = Binary(name, *args).get()
    return TempApp