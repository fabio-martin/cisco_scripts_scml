import pexpect
import re
from configparser import ConfigParser

from Models.scml_sitestate_cisco import ScmlSitestateCisco
from Models.view_cmdb_old import Viewcmdbold

config = ConfigParser()
config.read('config.cfg')
routeruserssh=config['router login ssh']['username'] 
routerpasswordssh = config['router login ssh']['password']
routerusertelnet=config['router login telnet']['username'] 
routerpasswordtelnet = config['router login telnet']['password']

class Command():
    def __init__(self, toSend, prompt, name ):
        self.toSend = toSend
        self.prompt = prompt
        self.name = name

class GetInfoCommands():

    def __init__(self, ssh, site, siteState):
        self.ssh = ssh
        self.site : Viewcmdbold = site 
        self.siteState : ScmlSitestateCisco = siteState
    
    def send_command(self, commands):
        ssh = self.ssh
        results = []
        for command in commands:
            pattern = command.prompt
            ssh.sendline(command.toSend)
            match = ssh.expect([pattern, pexpect.TIMEOUT, pexpect.EOF], timeout=20)
            if match == 1:
                # print(f'TIMEOUT - [{command.name}]')
                return None
            elif match == 2:
                # print(f'EOF - [{command.name}]')
                return None
            
            output  = ssh.before.decode()
            results.append(output)
            # print(output)
            
        return results
        
    def loginRouter(self):
        commandName = 'Login Router'
        site = self.site
        siteState = self.siteState
        maxRetries = 3
        retries = 1
        
        commands = [
            Command( f'ssh {routeruserssh}@{site.gestao}', '[P|p]assword:', commandName),
            Command( routerpasswordssh, re.compile(r'.*#$'), commandName)
        ]
        
        while(retries <= maxRetries):
            results = self.send_command(commands)
    
            if results: 
                # print(f'Success - [{commandName}]')
                siteState.login_router = 'OK'
                return 1

            # print(f'ERROR - [{commandName}] - Retry number: {retries}')
            retries +=1
            
        siteState.login_router = 'NOK'
        # print(f'ERROR - [{commandName}]')
        return 0   
    
    def loginRouterTelnet(self):
        commandName = 'Login Router'
        site = self.site
        siteState = self.siteState
        maxRetries = 3
        retries = 1
        
        commands = [
            Command( f'telnet {site.XOT}', 'Username:', commandName),
            Command(  routerusertelnet, '[P|p]assword:', commandName),
            Command( routerpasswordtelnet, re.compile(r'.*#$'), commandName),
            Command( f'terminal length 0', re.compile(r'.*#$'), commandName),            
        ]
        
        while(retries <= maxRetries):
            results = self.send_command(commands)
    
            if results: 
                # print(f'Success - [{commandName}]')
                siteState.login_router = 'OK'
                return 1

            print(f'ERROR - [{commandName}] - Retry number: {retries}')
            retries +=1
            
        siteState.login_router = 'NOK'
        # print(f'ERROR - [{commandName}]')
        return 0       
    

        
    def set_terminal_lenght_zero(self):
        commandName= 'Set Terminal Lenght to Zero'
        commandPrompt = re.compile(r'.*#$')
        toSend = "terminal length 0"
        commands = [Command(toSend, commandPrompt, commandName)]
        results = self.send_command(commands)
        # if not results:
        #     print(f'ERROR - [{commandName}]')
        # else:
        #     print(f'Success - [{commandName}]')
            
        # print(''.join(results))
        
        
    def get_bgp_rjogo_state(self):
        commandName= 'Show ip bgp sum | i 15525'
        commandPrompt= re.compile(r'.*#$')
        toSend = 'show ip bgp sum | i 1552'
        commands = [Command(toSend, commandPrompt, commandName)]
        results= self.send_command(commands)
                
        if not results:
            self.siteState.bgp_rjogo = 'NOK'
            # print(f'ERROR - [{commandName}]')
        else:
            output = results.pop(0).splitlines().pop()
            self.siteState.bgp_rjogo_output = output
            notConnected = ['never', 'Active', 'Idle', 'OpenSent']
            for line in notConnected:
                if(line in output):
                    self.siteState.bgp_rjogo = 'NOK'
                    return 

            self.siteState.bgp_rjogo = 'OK'
            # print(f'Success - [{commandName}]')
            return 
    
    def get_bgp_rvideo_state(self):
        commandName= 'Show ip bgp all sum | begin 172.21'
        commandPrompt= re.compile(r'.*#$')
        toSend = 'sh ip bgp all sum | begin 172.21'
        commands = [Command(toSend, commandPrompt, commandName)]
        results= self.send_command(commands)
                
        if not results:
            self.siteState.bgp_rvideo = 'NOK'
            # print(f'ERROR - [{commandName}]')
        else:
            output = results.pop(0).splitlines().pop()
            self.siteState.bgp_rvideo_output= output
            notConnected = ['never', 'Active', 'Idle', 'OpenSent']
            for line in notConnected:
                if(line in output):
                    self.siteState.bgp_rvideo = 'NOK'
                    return 

            self.siteState.bgp_rvideo = 'OK'
            # print(f'Success - [{commandName}]')
            return  
    
    def get_cellular_radio_info(self):
        commandName= 'Show cellular 0/2/0 radio | i RSSI | Selected | RSRP | SNR | Preference'
        commandPrompt= re.compile(r'.*#$')
        toSend = 'show cellular 0/2/0 radio | i RSSI | Selected | RSRP | SNR | Preference'
        commands = [Command(toSend, commandPrompt, commandName)]
        results= self.send_command(commands)
        sitestate = self.siteState        
        
        if not results:
            print(f'ERROR - [{commandName}]')
        else:
            output = results.pop().split('\n')[1:]
            for line in output:
                if('RSSI' in line):
                    # print(f'RSSI:{line}')
                    sitestate.rssi_cellular = line
                elif ('Selected' in line):
                    # print(f'Selected:{line}')
                    sitestate.selected_cellular = line
                elif ('RSRP' in line):
                    # print(f'RSRP: {line}')
                    sitestate.rsrp_cellular = line
                elif ('SNR' in line):
                    # print(f'SNR: {line}')
                    sitestate.snr_cellular = line 
                elif ('Preference' in line):
                    # print(f'Preference: {line}')
                    sitestate.preference_cellular = line
                    
            # print(f'Success - [{commandName}]')
            return  sitestate
            
    
    def show_ip_int_brief(self):
        commandName = 'Show ip int brief'
        commandPrompt = re.compile(r'.*#$')
        toSend = "sh ip int brief"
        commands = [Command(toSend, commandPrompt, commandName)]
        results= self.send_command(commands)
        
        # if not results:
        #     print(f'ERROR - [{commandName}]')
        # else:
        #     print(f'Success - [{commandName}]')
            
        print(''.join(results))
        
    
    def get_int_gig_0_1_0_state(self):
        commandName = 'Show ip int brief | i GigabitEthernet0/1/0'
        commandPrompt = re.compile(r'.*#$')
        toSend = "sh ip int brief | i GigabitEthernet0/1/0"
        commands = [Command(toSend, commandPrompt, commandName)]
        results= self.send_command(commands)
        
        if not results:
            print(f'ERROR - [{commandName}]')
        else:
            output = results.pop()
            self.siteState.int_gig_0_1_1_state_output = ''.join(output.split('\n')[1:])
            if(output.count("up") == 0): 
                self.siteState.int_gig_0_1_1 = 'NOK'
            else: 
                self.siteState.int_gig_0_1_1 = 'OK'
                
            # print(f'Success - [{commandName}]')

        
    def get_vlan_10_state(self):
        commandName = 'Show ip int brief | i Vlan10'
        commandPrompt = re.compile(r'.*#$')
        toSend = "sh ip int brief | i Vlan10"
        commands = [Command(toSend, commandPrompt, commandName)]
        results= self.send_command(commands)
        
        if not results:
            print(f'ERROR - [{commandName}]')
        else:
            output = results.pop()
            self.siteState.vlan10_output = ''.join(output.split('\n')[1:])
            # print(output)
            if(output.count("up") == 0): 
                self.siteState.vlan10 = 'NOK'
            else: 
                self.siteState.vlan10 = 'OK'
                
            # print(f'Success - [{commandName}]')
            
    def get_access_list_111_state(self):
        commandName = 'Show ip access-lists 111'
        commandPrompt = re.compile(r'.*#$')
        toSend = "sh ip access-lists 111"
        commands = [Command(toSend, commandPrompt, commandName)]
        results= self.send_command(commands)
       
        # print(''.join(results))
        
        self.siteState.access_list_111 = ''.join(results)
        
        if not results:
            print(f'ERROR - [{commandName}]')
        else:
            output = results.pop().split('\n')
        
            for line in output: 
                if('10.130.246.128' in line):
                    # print(f'Found the line:{line}')
                    self.siteState.found_duplicate_access_list_111 = 'OK'
                    
                elif ('10.252.2.246' in line):
                    # print(f'Found the line:{line}')
                    self.siteState.found_duplicate_access_list_111 = 'OK'
             
                    
            # print(f'Success - [{commandName}]')
                
    def exit_router(self):
        commandName = 'Exit'
        commandPrompt = re.compile(r'.*#$')
        toSend = "exit"
        commands = [Command(toSend, commandPrompt, commandName)]

        
 
       

        