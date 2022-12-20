# Modul raboty s polzovatelem
def viev ():
    import_viev=input('import ili export?=> ')
    if import_viev=='import':
        import_viev=True
    elif import_viev == 'export':
            import_viev=False
    else:
        print('Nekoreknyi vvod')
        viev()
    return import_viev

def viev_export ():
    famely_export=''
    imya_export=''
    list_export=''
    while not famely_export or not imya_export:
        if not famely_export:
            famely_export=input('Vvedite Familiyu=> ')
            list_export+=famely_export
        elif not imya_export:
            imya_export=input('Vvedite Imya=> ')
            list_export+=f' {imya_export}'
    return list_export

def viev_import ():
    familiya=''
    imya=''
    otchestvo=''
    telefon=''
    str_import=''
    while not familiya or not imya or  not otchestvo or not telefon:
        if not familiya:
            familiya=input('Vvedite Familiyu=> ')
            str_import+=familiya
        elif not imya:
            imya=input('Vvedite imya=> ')
            str_import+=f' {imya}'
        elif not otchestvo:
            otchestvo= input('Vvedite otchestvo=> ')
            str_import+=f' {otchestvo}'
        elif not telefon:
            telefon=input('Vvedite telefon=> ')
            str_import+=f' {telefon}'
    return str_import

