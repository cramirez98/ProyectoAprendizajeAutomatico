#!/usr/bin/env Rscript

install.packages('tictoc')
library(tictoc)

package_list <- read.csv("paquetes.csv", header= T)$PAQUETES
missin_packages <- package_list[!(package_list %in% installed.packages()[,"Package"])]
print('Paquetes a instalar:')
print(missin_packages)
tic('Tiempo de instalacion de paquetes:')
if(length(missin_packages)) install.packages(missin_packages)
toc()
m<-lapply(package_list, require, character.only = TRUE)
print('Paquetes cargados correctamente')