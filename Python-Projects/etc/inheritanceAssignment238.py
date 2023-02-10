class computer:
    cpu = "Intel"   # Processor maker
    gpu = "AMD"     # Card maker
    ram = 8         # In GB
    case = True     # Has a case
    

class windows(computer): # Denotes that windows is a child class of computer and will add the following attributes
    os = 'Windows10'  # New attribute
    canModify = True  # New windows-specific attribute
    canInstall = True # New windows-specific attribute
    
	
class nintendoGC(computer): # nintendoGC is a child class of computer
    os = 'Nintendo GameCube' # New attribute
    cd_drive = True          # New nintendoGC-specific attribute
    controller_input = True  # New nintendoGC-specific attribute