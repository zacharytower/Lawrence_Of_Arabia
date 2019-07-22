class PlayerModPacket:
    
    def __init__(self, mod_dict):
        self.change_dict = mod_dict
        
    def __iter__(self):
        for item in self.change_dict.keys():
            yield (item, self.change_dict[item])
            
    