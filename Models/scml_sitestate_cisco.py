from typing import Text
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class ScmlSitestateCisco(base):
    def __init__(self, state, hostname, ip):
        self.state = state
        self.hostname = hostname
        self.ip = ip
        self.equip = None
        self.login_jump_server = None
        self.login_router = None
        self.updated_at = None
        self.bgp_rjogo_output = None
        self.bgp_rjogo = None
        self.bgp_rvideo_output = None
        self.bgp_rvideo = None  
        self.rssi_cellular = None
        self.selected_cellular = None
        self.rsrp_cellular = None
        self.int_gig_0_1_1_state_output = None
        self.int_gig_0_1_1 = None
        self.vlan10_output = None
        self.vlan10 = None
        self.access_list_111 = None
        self.found_duplicate_access_list_111 = None
    
    __tablename__ = "scml_sitestate_cisco"
    state = Column(Integer, nullable=False)
    hostname = Column(String(50),primary_key=True)
    ip = Column(String(50), nullable=True)
    equip = Column(String(50), nullable=True)
    login_jump_server = Column(String(50), nullable=True)
    login_router = Column(String(50), nullable=True)
    updated_at = Column(String(50), nullable=True)
    bgp_rjogo_output = Column(String(255), nullable=True)
    bgp_rjogo = Column(String(50), nullable=True)
    bgp_rvideo_output = Column(String(255), nullable=True)
    bgp_rvideo = Column(String(50), nullable=True)
    rssi_cellular = Column(String(2000), nullable=True)
    selected_cellular = Column(String(255), nullable=True)
    rsrp_cellular = Column(String(255), nullable=True)
    snr_cellular = Column(String(255), nullable=True)
    preference_cellular = Column(String(255), nullable=True)
    int_gig_0_1_1_state_output = Column(String(2000), nullable=True)
    int_gig_0_1_1 = Column(String(255), nullable=True)
    vlan10_output = Column(String(2000), nullable=True)
    vlan10 = Column(String(255), nullable=True)
    access_list_111 = Column(String(2000), nullable=True)
    found_duplicate_access_list_111 = Column(String(50), nullable=True)