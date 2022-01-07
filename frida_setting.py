import frida

class frida_setting:
    def __init__(self):
        self.process = ''
        self.hook_package_name = ''
        self.script = []

    def start(self, hook_package_name: str):
        self.hook_package_name = hook_package_name

        device = frida.get_usb_device(timeout=10)
        pid = device.spawn([self.hook_package_name])
        self.process = device.attach(pid)
        device.resume(pid)
    
    def startScript(self, script: str):
        self.script.append(self.process.create_script(script))
        self.script[len(self.script) - 1].on("message", self.debugMessage)
        self.script[len(self.script) - 1].load()
    
    def debugMessage(self, message, data):
        print("{} -> {}".format(message, data))