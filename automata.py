from enum import Enum
#1302204034
class TiketBusStatus(Enum):
    LogIn = 0
    Dashboard = 1
    Tambah_Bus = 2
    Cari_Bus = 3

class Trigger(Enum):
    Gagal_Login = 0
    Home = 1
    Tambah_Bis = 2
    Cari_Bis = 3

class transition():
    prevState : TiketBusStatus
    nextState : TiketBusStatus
    trigger : Trigger

    def __init__(self,prevState:TiketBusStatus, nextState:TiketBusStatus, trigger:Trigger):
        self.prevState = prevState
        self.nextState = nextState
        self.trigger = trigger

p : transition = [transition(TiketBusStatus.LogIn, TiketBusStatus.Dashboard, Trigger.Home),
                    transition(TiketBusStatus.LogIn, TiketBusStatus.Tambah_Bus, Trigger.Tambah_Bis),
                    transition(TiketBusStatus.LogIn, TiketBusStatus.Cari_Bus, Trigger.Cari_Bis),
                    transition(TiketBusStatus.LogIn, TiketBusStatus.LogIn, Trigger.Gagal_Login),
                ]

currentState : TiketBusStatus = "LogIn"
def getNextState(prevState:TiketBusStatus, trigger:Trigger):
    nextState : TiketBusStatus = prevState
    i = 0
    for i in range(len(p)):
        if p[i].prevState.name == prevState and p[i].trigger.name == trigger:
            nextState = p[i].nextState
    return nextState

def activeTrigger(trigger:Trigger):
    global currentState
    nextState:TiketBusStatus = getNextState(currentState, Trigger[trigger].name)
    currentState = nextState

print("Program Booking Tiket Bus Shantika")
print("Halaman",currentState)
y =  input("Mau ke halaman (Home, Cari_Bis, Tambah_Bis): ")
activeTrigger(y)
print("Halaman",currentState.name)