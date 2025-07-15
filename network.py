class Packet:
  def __init__(self, src, dst, data):
    self.src = src
    self.dst = dst
    self.data = data
  
class Computer:
    def __init__(self, name, router):
        self.name = name 
        self.router = router

    def send(self, dst, data):
        packet = Packet(self.name, dst, data)
        self.router.route(packet)

    def receive(self, packet):
        print(f"[{self.name}] Получено сообщение от '{packet.src}': {packet.data}")

class Router:
    def __init__(self):
        self.devices = {}

    def connect(self, device):
        self.devices[device.name] = device

    def route(self, packet):
        if packet.dst in self.devices:
            self.devices[packet.dst].receive(packet)
        else:
            print(f"[ROUTER] Ошибка: получатель '{packet.dst}' не найден!")

router = Router()
PC1 = Computer("PC1", router)
PC2 = Computer("PC2", router)
PC3 = Computer("PC3", router)
PC4 = Computer("PC4", router)
router.connect(PC1)
router.connect(PC2)
router.connect(PC3)
router.connect(PC4)
PC1.send("PC3", "Привет от PC1!")
PC3.send("PC1", "Ответ от PC3!")
PC4.send("PC2","PC2 здесь")
PC2.send("PC4","Принято!")
pavel = Computer("Pavel", router)
bogdan = Computer("Bogdan", router)
router.connect(pavel)
router.connect(bogdan)
pavel.send("Pavel", "Привет, Богдан!")
bogdan.send("Bogdan", "Здравствуйте, Павел! Скоро будет восстание машин.")

pavel.send("Eve", "Ты меня слышишь?")
