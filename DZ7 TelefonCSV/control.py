from Viev import *
from export import*
from import_fl import *
reshenie=viev()
def deystvie (reshenie):
    if reshenie == False:
        str_exp = list(viev_export().split())
        export_str(str_exp)
        print (export_str(str_exp))
    if reshenie==True:
        str_imp = list(viev_import().split())
        import_csv(str_imp)
deystvie(reshenie)