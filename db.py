from datetime import date, datetime
from configparser import ConfigParser
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from Models import scml_sitestate_cisco
from Models.view_cmdb_old import Viewcmdbold
from Models.scml_sitestate_cisco import ScmlSitestateCisco

config = ConfigParser()
config.read('config.cfg')
username=config['database']['username']
password=config['database']['password']
database_host=config['database']['database_host']
database= config['database']['database']
port= config['database']['port']

engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{database_host}:{port}/{database}")
base = declarative_base()
factory = sessionmaker(bind=engine)
session = factory()

# scml_sitestate_cisco_table = ScmlSitestateCisco.metadata.tables["scml_sitestate_cisco"]
# for instance in session.execute(scml_sitestate_cisco_table.select().where(scml_sitestate_cisco_table.c.hostname == "RJACS032000")):
#     print("Hostname: ", instance.acessoPrincipal)
#     print("---------")

def getsitesTelnet():
    # viewcmdbold_table = Viewcmdbold.metadata.tables["viewcmdbold"]
    # # scml_sitestate_cisco_telnet_table = scml_sitestate_cisco_telnet_table.metadata.tables["scml_sitestate_cisco"]
    sites = session.execute(text("SELECT" +
                                 " V.*"  +
                                 " FROM portal.viewcmdbold as V"  +
                                 " LEFT JOIN portal.scml_sitestate_cisco_telnet as S ON V.hostname = S.hostname" +
                                 " WHERE"  +
                                 " V.active = 1"  +
                                 " AND" +
                                 " V.ModeloCPE LIKE 'CISCO%'" +
                                 " AND" +
                                 " (S.updated_at  < CURRENT_DATE() OR S.updated_at is null) "
                                )
                            )
    
    return sites


def getsites():
    # viewcmdbold_table = Viewcmdbold.metadata.tables["viewcmdbold"]
    # scml_sitestate_cisco_table = ScmlSitestateCisco.metadata.tables["scml_sitestate_cisco"]

    sites = session.execute(text("SELECT" +
                                 " V.*"  +
                                 " FROM portal.viewcmdbold as V"  +
                                 " LEFT JOIN portal.scml_sitestate_cisco as S ON V.hostname = S.hostname" +
                                 " WHERE"  +
                                 " V.active = 1"  +
                                 " AND" +
                                 " V.ModeloCPE LIKE 'CISCO%'" +
                                 " AND" +
                                 " (S.updated_at  < CURRENT_DATE() OR S.updated_at is null)" 
                                )
                            )

    
    # sites = session.execute(text("SELECT" +
    #                              " V.*"  +
    #                              " FROM portal.viewcmdbold as V"  +
    #                              " LEFT JOIN portal.scml_sitestate_cisco as S ON V.hostname = S.hostname" +
    #                              " WHERE"  +
    #                              " V.active = 1"  +
    #                              " AND" +
    #                              " V.ModeloCPE LIKE 'CISCO%'" +
    #                              " AND" +
    #                              " S.updated_at IS NULL"
    #                             )
    #                         )
        
    # sites = session.execute(query)
    
    return sites

def getSitesNotUpdatedToday():
    viewcmdbold_table = Viewcmdbold.metadata.tables["viewcmdbold"]
    scml_sitestate_cisco_table = ScmlSitestateCisco.metadata.tables["scml_sitestate_cisco"]
    sites = session.execute(text("SELECT * FROM portal.viewcmdbold as V WHERE V.active = 1 AND V.ModeloCPE LIKE 'TELDAT%'"))
    
    

def insertintodatabase(siteStateList):
    for siteState in siteStateList:
        # print(f'Inserting {siteState.hostname}')
        if(siteState):
            session.merge(siteState)

    session.commit()
    session.close()



