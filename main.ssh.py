
from concurrent.futures import ThreadPoolExecutor
from configparser import ConfigParser

from datetime import date, datetime
from time import sleep

from Models.scml_sitestate_cisco import ScmlSitestateCisco
from Models.view_cmdb_old import Viewcmdbold
from db import getsites, insertintodatabase
from ssh_login import ssh_connect
from Commands.Commands import GetInfoCommands, Command



config = ConfigParser()
config.read('config.cfg')
jumpserver=config['ssh jump server']['jumpserver']
username=config['ssh jump server']['username']
password= config['ssh jump server']['password']

def get_site_info(site):
    
    siteState = ScmlSitestateCisco(site.active, site.hostname, site.gestao)
    siteState.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Working on site with hostname: {site.hostname}')
    
    session = ssh_connect(username, password, jumpserver)

    if(session == 0 or session == 1):
        print("An error occurred when trying to establish SSH session!")
        siteState.login_jump_server =  'NOK'
        return siteState
        
    if session:
        
        print('[+] SSH session established successfully!')
        
        siteState.login_jump_server =  'OK'
        # Now you can interact with the session
        # Get the get info commands
        commands = GetInfoCommands(session, site, siteState)
        # Authenticate in the router 
        res = commands.loginRouter()
        if res == 0: 
            print(f'There was an error logging in the router: {site.hostname}' )
            # print(siteState)
            return siteState
            
        commands.set_terminal_lenght_zero()
        commands.get_bgp_rjogo_state()
        commands.get_bgp_rvideo_state()
        commands.get_cellular_radio_info()
        commands.get_int_gig_0_1_0_state()
        commands.get_vlan_10_state()
        commands.get_access_list_111_state()
        commands.exit_router()
        session.close()
        print(f'Finished scripts on site with hostname: {site.hostname}')
        return siteState
        
def run(sites): 
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(get_site_info, sites)
  
    sleep(2)
    insertintodatabase(results)
    
    
    
def main():
    
    print("[+] Starting scripts...")
     
    start = datetime.now()
    # siteStateList: ScmlSitestateCisco = getsites()
    sites : Viewcmdbold = getsites()
    # siteStateList = []
    # site = sites.first()
    # print(siteStateList.rowcount)
   


    while(sites.rowcount!= 0):
        run(sites)
        print("######## Finished first query ")
        sites: ScmlSitestateCisco = getsites()
        print(f'######## There are {sites.rowcount} remainining sites')

    # with ThreadPoolExecutor(max_workers=20) as executor:
    #     results = executor.map(get_site_info, sites)

    
    now = datetime.now()
    timePassed = now - start 

    print(f'This execution took: {timePassed} seconds')
    
    
if __name__ == '__main__':
    main()