from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Viewcmdbold(base):
    __tablename__ = "viewcmdbold"
    active = Column(Integer, nullable=True)
    hostname = Column(String(50),primary_key=True)
    numFirma = Column(Integer, nullable=True)
    numEstabelecimento = Column(Integer, nullable=True)
    numEquipamento = Column(Integer, nullable=True)
    nomefirma = Column(String(50), nullable=True)
    nomeEstabelecimento = Column(String(50), nullable=True)
    atividade = Column(String(50), nullable=True)
    zona = Column(String(50), nullable=True)
    morada = Column(String(50), nullable=True)
    cPostal = Column(String(50), nullable=True)
    locPostal = Column(String(50), nullable=True)
    telEstabelecimento = Column(String(50), nullable=True)
    numTelefonePT = Column(String(50), nullable=True)
    freguesia = Column(String(50), nullable=True)
    concelho = Column(String(50), nullable=True)
    distrito = Column(String(50), nullable=True)
    nomeGerente = Column(String(50), nullable=True)
    contactoGerente = Column(Integer, nullable=True)
    GECA = Column(String(50), nullable=True)
    NNA = Column(String(50), nullable=True)
    maq = Column(String(50), nullable=True)
    numTerminais = Column(Integer, nullable=True)
    numTvs = Column(Integer, nullable=True)
    horario = Column(String(50), nullable=True)
    sDeskString = Column(String(50), nullable=True)
    diasAbertura = Column(String(50), nullable=True)
    aberturaManha = Column(Integer, nullable=True)
    fechoManha = Column(Integer, nullable=True)
    aberturaTarde = Column(Integer, nullable=True)
    fechoTarde = Column(Integer, nullable=True)
    obs = Column(String(50), nullable=True)
    acessoPrincipal = Column(String(50), nullable=True)
    acessoBackup = Column(String(50), nullable=True)
    linkPrincipalWAN = Column(String(50), nullable=True)
    linkBackupWAN = Column(String(50), nullable=True)
    linkPhaseOut = Column(String(50), nullable=True)
    LAN = Column(String(50), nullable=True)
    XOT = Column(String(50), nullable=True)
    gestao = Column(String(50), nullable=True)
    IpRJogo = Column(String(50), nullable=True)
    IpRJogoNextHop = Column(String(50), nullable=True)
    IpRVideo = Column(String(50), nullable=True)
    IpRVideoNextHop = Column(String(50), nullable=True)
    ipBackupVideo = Column(String(50), nullable=True)
    ipFortigate = Column(String(50), nullable=True)
    ipTunel100 = Column(String(50), nullable=True)
    ipxDSL = Column(String(50), nullable=True)
    ipxBackupDSL = Column(String(50), nullable=True)
    ipRJogoDSL = Column(String(50), nullable=True)
    ipRVideoDSL = Column(String(50), nullable=True)
    IpRJogoBackupETH = Column(String(50), nullable=True)
    IpRVideoBackupETH = Column(String(50), nullable=True)
    AC = Column(String(50), nullable=True)
    circuitoPriCRM = Column(String(50), nullable=True)
    PCLNEWGPON = Column(String(50), nullable=True)
    IXSNEWGPON = Column(String(50), nullable=True)
    reqNEWGPON = Column(String(50), nullable=True)
    IXSRJOGO = Column(String(50), nullable=True)
    IDRJOGO = Column(String(50), nullable=True)
    IXSRVIDEO = Column(String(50), nullable=True)
    IDRVIDEO = Column(String(50), nullable=True)
    PCLxDSL = Column(String(50), nullable=True)
    IXSxDSL = Column(String(50), nullable=True)
    circuito150 = Column(Integer, nullable=True)
    reqxDSL = Column(String(50), nullable=True)
    bitstream = Column(String(50), nullable=True)
    dslMode = Column(String(50), nullable=True)
    PCLGPON = Column(String(50), nullable=True)
    IXSGPON = Column(String(50), nullable=True)
    circuito170 = Column(Integer, nullable=True)
    vlanGPON = Column(String(50), nullable=True)
    circuitoBckCRM = Column(String(50), nullable=True)
    PCL3G = Column(String(50), nullable=True)
    IXS3G = Column(String(50), nullable=True)
    SIMcard = Column(String(50), nullable=True)
    NumTMN = Column(Integer, nullable=True)
    PIN = Column(String(50), nullable=True)
    PUK = Column(String(50), nullable=True)
    user3G = Column(String(50), nullable=True)
    password3G = Column(String(50), nullable=True)
    IXS3GVideo = Column(String(50), nullable=True)
    user3GVideo = Column(String(50), nullable=True)
    password3GVideo = Column(String(50), nullable=True)
    linkCellular = Column(String(50), nullable=True)
    PCLRDIS = Column(String(50), nullable=True)
    IXSRDIS = Column(String(50), nullable=True)
    sftRDIS = Column(Integer, nullable=True)
    RDIStipoCentral = Column(String(50), nullable=True)
    ReqRDIS = Column(String(50), nullable=True)
    userRDIS = Column(String(50), nullable=True)
    passwordRDIS = Column(String(50), nullable=True)
    phaseout_circuitoDslCRM = Column(String(50), nullable=True)
    phaseout_PCLxDSL = Column(String(50), nullable=True)
    phaseout_IXSxDSL = Column(String(50), nullable=True)
    phaseout_circuito150 = Column(Integer, nullable=True)
    phaseout_reqxDSL = Column(String(50), nullable=True)
    phaseout_bitstream = Column(String(50), nullable=True)
    phaseout_dslMode = Column(String(50), nullable=True)
    phaseout_IXSxDSLRVideo = Column(String(50), nullable=True)
    phaseout_IXCxDSLRJogo = Column(String(50), nullable=True)
    phaseout_IXCxDSLRVideo = Column(String(50), nullable=True)
    IXS_Acesso_circuitoBackup = Column(String(50), nullable=True)
    circuitoBackup = Column(String(50), nullable=True)
    IXS_RJogoBackupETH = Column(String(50), nullable=True)
    IDRJogoBackupETH = Column(String(50), nullable=True)
    IXS_RVideoBackupETH = Column(String(50), nullable=True)
    IDRVideoBackupETH = Column(String(50), nullable=True)
    routing = Column(String(50), nullable=True)
    classeComercial = Column(String(50), nullable=True)
    site = Column(String(50), nullable=True)
    QoS = Column(String(50), nullable=True)
    ModeloCPE = Column(String(50), nullable=True)
    codSAP = Column(Integer, nullable=True)
    pnSITE = Column(String(50), nullable=True)
    PCLCPE = Column(String(50), nullable=True)
    IXPCPE = Column(String(50), nullable=True)
    EWM = Column(String(50), nullable=True)
    snCPE = Column(String(50), nullable=True)
    AtividadeGECA = Column(String(50), nullable=True)
    RSSI = Column(String(50), nullable=True)
    Upload = Column(String(50), nullable=True)
    Download = Column(String(50), nullable=True)
    multiSite = Column(String(50), nullable=True)
    antena3G = Column(String(50), nullable=True)
    org_name = Column(String(50), nullable=True)
    org_spect = Column(String(50), nullable=True)
    ci = Column(String(50), nullable=True)
    termIP = Column(Integer, nullable=True)
    fortigate = Column(Integer, nullable=True)
    tipologia = Column(String(50), nullable=True)
    vodafone = Column(Integer, nullable=True)
