import pandas as pd

class Lager:
    
    def __init__(self, csv_name: str):
        self.lagerstatus = pd.read_csv(csv_name)
        self.vikt = self.lagerstatus['Vikt'].sum()
        self.förtjänst = self.lagerstatus['Förtjänst'].sum()
        self.dagensförtjänst = 0
        
    def updatera(self, lagerstatus: pd.DataFrame, dagensförtjänst):
        self.lagerstatus = lagerstatus
        self.dagensförtjänst += dagensförtjänst
        if lagerstatus.empty:
            self.vikt = 0
            self.förtjänst = 0
        else:
            self.vikt = self.lagerstatus['Vikt'].sum()
            self.förtjänst = self.lagerstatus['Förtjänst'].sum()
            
    def antal_paket(self):
        return self.lagerstatus.shape[0]
    
    def straff_avgift(self):
        #formel -(x**2) där x är antal dagar efter deadline
        avgift = 0
        straff = self.lagerstatus['Deadline']
        straff = straff[straff < 0]
        for row in straff:
            avgift += (row**2)
        return avgift
    
    