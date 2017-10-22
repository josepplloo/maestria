import numpy as np
import pandas as pd
from sklearn import preprocessing
infile ="/Users/josepplloo/Documents/scripts/xaa.csv"
infile2 ="/Users/josepplloo/Documents/scripts/xab.csv"
dictfile ="/Users/josepplloo/Documents/scripts/dictresult.csv"
df = pd.read_csv(infile, header = 0)
df2 = pd.read_csv(infile2, header = 0)
a=[]
frames = [df, df2]
result = pd.concat(frames)
#cargo el archivo de datos
l1 = preprocessing.LabelEncoder()
l2 = preprocessing.LabelEncoder()
l3 = preprocessing.LabelEncoder()
l4 = preprocessing.LabelEncoder()
l5 = preprocessing.LabelEncoder()
l6 = preprocessing.LabelEncoder()


#Guardo los encabezados de la tabla y los transformo
a.append("PersonaID: id de la persona")
a.append(result.PersonaID.unique())
result=result.drop('PersonaID',1)

a.append("TipoEventoRIPSDesc: Evento en la Factura")
a.append(result.TipoEventoRIPSDesc.unique())
result=result.drop('TipoEventoRIPSDesc',1)

a.append("Codigo: id de la eps")
a.append(result.Codigo.unique())
result=result.drop('Codigo',1)


a.append("RegimenAdministradoraDesc: id del regimen: Contributivo-Subsidiado-Vinculado-Particular-Otro-Desplazado")
a.append(result.RegimenAdministradoraDesc.unique())
l2.fit(result.RegimenAdministradoraDesc.unique())
a.append(l2.transform(result.RegimenAdministradoraDesc.unique()))
result.RegimenAdministradoraDesc=l2.transform(result.RegimenAdministradoraDesc)


a.append("DxPrincipal: diagnostico principal")
a.append(result.DxPrincipal.unique())
l3.fit(result.DxPrincipal.unique())
a.append(l3.transform(result.DxPrincipal.unique()))
result.DxPrincipal=l3.transform(result.DxPrincipal)
a.append("tome el diagnostico G800 ")
a.append(l3.transform(["G800"]))


a.append("DxEgreso: diagnostico de salida")
a.append(result.DxEgreso.unique())
result=result.drop('DxEgreso',1)

a.append("FinalidadProcedimientosCD: si la finalidad es diagnostica-terapeutica")
a.append(result.FinalidadProcedimientosCD.unique())

a.append("FinalidadConsultaCD: la consulta que se realiza")
a.append(result.FinalidadConsultaCD.unique())
result=result.drop('FinalidadConsultaCD',1)

a.append("TipoUsuarioCD: si el usuario es Contributivo-Subsidiado-Vinculado-Particular-Otro-Desplazado")
a.append(result.TipoUsuarioCD.unique())

a.append("CausaExternaCD:si es victima de matrato o violencia")
a.append(result.CausaExternaCD.unique())
result=result.drop('CausaExternaCD',1)

a.append("Prestador: ISP")
a.append(result.Prestador.unique())
result=result.drop('Prestador',1)

a.append("AmbitosProcedimientoCD: si es ambulatorio-hospitalario-urgencias")
a.append(result.AmbitosProcedimientoCD.unique())
l4.fit(result.AmbitosProcedimientoCD.unique())
a.append(l4.transform(result.AmbitosProcedimientoCD.unique()))
result.AmbitosProcedimientoCD=l4.transform(result.AmbitosProcedimientoCD)

a.append("CodigoProcedimiento: procedimiento medico")
a.append(result.CodigoProcedimiento.unique())
l5.fit(result.CodigoProcedimiento.unique())
a.append(l5.transform(result.CodigoProcedimiento.unique()))
result.CodigoProcedimiento=l5.transform(result.CodigoProcedimiento)

a.append("MunicipioCD: id municipo")
a.append(result.MunicipioCD.unique())
result=result.drop('MunicipioCD',1)

a.append("EstadoSalidaDesc: si sale vivo o muerto")
a.append(result.EstadoSalidaDesc.unique())
result=result.drop('EstadoSalidaDesc',1)

a.append("CostoConsulta: el costo de la consulta")
a.append(result.CostoConsulta.unique())
result=result.drop('CostoConsulta',1)

a.append("CostoProcedimiento: costo del procedimiento")
a.append(result.CostoProcedimiento.unique())
result=result.drop('CostoProcedimiento',1)

a.append("NetoAPagarConsulta: total a pagar")
a.append(result.NetoAPagarConsulta.unique())
result=result.drop('NetoAPagarConsulta',1)

a.append("NumeroDiasEstancia: numero de dias en el servicio")
a.append(result.NumeroDiasEstancia.unique())
result=result.drop('NumeroDiasEstancia',1)

a.append("fechaid: fecha")
a.append(result.fechaid.unique())
result=result.drop('fechaid',1)

a.append("Edad: edad")
a.append(result.Edad.unique())

a.append("SexoDesc: genero del usuario")
a.append(result.SexoDesc.unique())
l6.fit(result.SexoDesc.unique())
a.append(l6.transform(result.SexoDesc.unique()))
result.SexoDesc=l6.transform(result.SexoDesc)

#ahora a volcar el df en un csv y en un diccionario
np.savetxt(dictfile, a, delimiter=",",fmt='%s')

df = result[:len(result)/2]
df2 = result[len(result)/2:]
df.to_csv("/Users/josepplloo/Documents/scripts/xaa_clean.csv",index=False)
df2.to_csv("/Users/josepplloo/Documents/scripts/xab_clean.csv",index=False)


"""
PersonaID: id de la persona
TipoEventoRIPSDesc: Evento en la Factura
Codigo: id de la eps
RegimenAdministradoraDesc: id del regimen: Contributivo-Subsidiado-Vinculado-Particular-Otro-Desplazado
DxPrincipal: diagnostico principal
DxEgreso: diagnostico de salida
FinalidadProcedimientosCD: si la finalidad es diagnostica-terapeutica
FinalidadConsultaCD: la consulta que se realiza
TipoUsuarioCD: si el usuario es Contributivo-Subsidiado-Vinculado-Particular-Otro-Desplazado
CausaExternaCD:si es victima de matrato o violencia
Prestador: ISP
AmbitosProcedimientoCD: si es ambulatorio-hospitalario-urgencias
CodigoProcedimiento: procedimiento medico
MunicipioCD: id municipo
EstadoSalidaDesc: si sale vivo o muerto
CostoConsulta: el costo de la consulta
CostoProcedimiento: costo del procedimiento
NetoAPagarConsulta: total a pagar
NumeroDiasEstancia: numero de dias en el servicio
fechaid: fecha
Edad: edad
SexoDesc: genero del usuario
"""
