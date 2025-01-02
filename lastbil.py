import pandas as pd
from lager import Lager
from genetic import find_goat
class Lastbil:
    
    kapacitet = float(800)
    DAGAR_TILL_DEADLINE = -100
    
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
                p = round((row['Förtjänst'] / row['Vikt']), 1)
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
            if self.vikt + round(paket['Vikt'], 1) < self.kapacitet:
                self.vikt += round(paket['Vikt'], 1)
                self.förtjänst += int(paket['Förtjänst'])
                self.last.append(paket['Paket_id'])
    
    def lasta_bil(self, lager: pd.DataFrame):
        första_prio, resterande_paket = self.lasta_bil_prioritering(lager)
    
        if första_prio:
            self.lasta_bil_helper(första_prio, lager)
        
        self.lasta_bil_helper(resterande_paket, lager)

        for x in self.last:
            lager.drop(lager[lager['Paket_id'] == x].index, inplace = True)
        lager.reset_index(drop=True, inplace=True)
        return lager, self.förtjänst
    
    def lasta_bil_genetic(self, lager:Lager):
        last_order = find_goat(lager)
        paket_no = 0
        for x in last_order:
            if x == 1:
                paket = lager.lagerstatus.iloc[paket_no]
                self.vikt += round(paket['Vikt'], 1)
                self.förtjänst += int(paket['Förtjänst'])
                self.last.append(paket['Paket_id'])
            paket_no += 1
        for x in self.last:
            lager.lagerstatus.drop(lager.lagerstatus[lager.lagerstatus['Paket_id'] == x].index, inplace = True)
        lager.lagerstatus.reset_index(drop=True, inplace=True)
        return lager.lagerstatus, self.förtjänst
        
