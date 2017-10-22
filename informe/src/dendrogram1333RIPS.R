
library(readr)
xaa_clean <- read_csv("~/Documents/RIP2013/scripts/xaa_clean1333.csv", 
                      col_types = cols(AmbitosProcedimientoCD = col_factor(c(0,1,2)), 
                                       Codigo = col_factor(c(41, 42, 37, 43,  3, 39, 28, 21, 31, 25, 24, 27, 15, 34, 40, 26,  1,
                                                             12,  6, 11, 33, 19)), 
                                       CodigoProcedimiento = col_skip(), 
                                       CostoConsulta = col_skip(), 
                                       CostoProcedimiento = col_double(), 
                                       DxEgreso = col_skip(), 
                                       DxPrincipal = col_factor(c(  0,  608, 1745,  696,  817,  620,  634, 1419,  438,  737,  526,
                                                                    706,  740,  705,  557, 1870, 1417,  703,  674, 1717,  761, 1491,
                                                                    1002, 1591,  677, 1465,  691,  816,  744,  882,  679,  625,  120,
                                                                    1729, 1436,  600,  734)), 
                                       EstadoSalidaDesc = col_skip(), 
                                       FinalidadConsultaCD = col_skip(), 
                                       FinalidadProcedimientosCD = col_factor(c(2, 1, 3, 4)), 
                                       MunicipioCD = col_skip(), 
                                       NetoAPagarConsulta = col_skip(), 
                                       NumeroDiasEstancia = col_skip(), 
                                       PersonaID = col_skip(), 
                                       Prestador = col_skip(), 
                                       RegimenAdministradoraDesc = col_factor(c(0,3,2)), 
                                       SexoDesc =col_factor(c(0,1,2)),
                                       TipoEventoRIPSDesc = col_skip(), 
                                       TipoUsuarioCD = col_factor(c(2, 3, 1, 5, 8)), 
                                       fechaid = col_skip()))
xaa<-na.omit(xaa_clean)
xaa<-data.frame(xaa$SexoDesc)
set.seed(1) 

hc=hclust(dist(xaa))
plot(hc)