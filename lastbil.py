import pandas as pd

class Lastbil:
    
    kapacitet = 800
    DAGAR_TILL_DEADLINE = 1
    
    def __init__(self):
        self.last = []
        self.vikt = 0
        self.förtjänst = 0
        
    def lasta_bil_prioritering(self, lager: pd.DataFrame):
        första_prio = []
        resterande_paket = []
        for index, row in lager.iterrows():
            if row['Deadline'] < self.DAGAR_TILL_DEADLINE:
                första_prio.append((index, row['Deadline']))
            else:
                p = row['Förtjänst'] / row['Vikt']
                resterande_paket.append((index, p))
                
        första_prio = sorted(
            första_prio,
            key=lambda x: x[1]
        )
        resterande_paket = sorted(
            resterande_paket, 
            key=lambda x: x[1],
            reverse=True
        )
        return första_prio, resterande_paket    
    
    def lasta_bil_helper(self, list, lager: pd.DataFrame):
        for x in list:
            paket = lager.iloc[x[0]]
            if self.vikt + paket['Vikt'] < self.kapacitet:
                self.vikt += paket['Vikt']
                self.förtjänst += paket['Förtjänst']
                self.last.append(paket['Paket_id'])
    
    def lasta_bil(self, lager: pd.DataFrame) -> pd.DataFrame:
        första_prio, resterande_paket = self.lasta_bil_prioritering(lager)
    
        if första_prio:
            self.lasta_bil_helper(första_prio, lager)
        
        self.lasta_bil_helper(resterande_paket, lager)

        for x in self.last:
            lager.drop(lager[lager['Paket_id'] == x].index, inplace = True)
        lager.reset_index(drop=True, inplace=True)
        return lager, self.förtjänst
