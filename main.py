
from flask import Flask, jsonify, request
from virtualbox import library
import virtualbox
import time
import vboxapi 
app = Flask(__name__)

@app.route('/RuningVMS', methods=['GET'])
def Runingvms():
        vbox = virtualbox.VirtualBox()
        session = virtualbox.Session()
        return jsonify({"ON/Off:" : [session.state >= 1 for m in vbox.machines],
        "machines":[m.name for m in vbox.machines]})

@app.route('/AllVMachines', methods=['GET'])
def index():
        vbox = virtualbox.VirtualBox()
        return jsonify({"Tout les machines virtuels:" : [m.name for m in vbox.machines]})

@app.route('/TurningOnMachine', methods=['POST'])
def index2():
        vbox = virtualbox.VirtualBox()
        session = virtualbox.Session()
        machine = vbox.find_machine("ubuntu_server")
        progress = machine.launch_vm_process(session, "gui", [])
        progress.wait_for_completion()

@app.route('/TurningOffMachine', methods=['POST'])
def index3():
        vbox = virtualbox.VirtualBox()
        vm = vbox.find_machine('ubuntu_server')
        s = virtualbox.Session()
        p = vm.launch_vm_process(s, "gui", [])
        p.wait_for_completion(1000)
        s.console.power_down() 
        s.unlock_machine()

@app.route('/IpAdress', methods=['POST'])
def index4(self):
       vbox = virtualbox.VirtualBox()
       vm = vbox.find_machine('ubuntu_server')
       session = vm.create_session()
       guest = self.session.console.guest.create_session("bilel", "2904",timeout_ms=60*2000)
       e = guest.execute("", "ip addr show")  # ""-> car on peut executer "ip addr show" peut importe l'emplacement

@app.route('/InstallMysql', methods=['POST'])
def index5(self):
       vbox = virtualbox.VirtualBox()
       vm = vbox.find_machine('ubuntu_server')
       session = vm.create_session()
       guest = self.session.console.guest.create_session("bilel", "2904",timeout_ms=60*2000) 
       e = guest.execute("", "sudo apt update")  #on fait l'update puis on install mysql server
       e.wait_for_completion(5000)
       e = guest.execute("", "sudo apt install mysql-server")
        
if __name__ == "__main__":
    app.run(debug=True) #Pour commencer notre serveur