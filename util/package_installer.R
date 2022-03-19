#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

install.packages('tictoc')
library(tictoc)

if(length(args) == 0){
  stop("No se suministro argumentos")
}else{
  package_list <- read.csv("paquetes.csv", header= T)[,toupper(args[1])]
}
missin_packages <- package_list[!(package_list %in% installed.packages()[,"Package"])]
print(paste('Numero de paquetes a instalar:', length(missin_packages)))
print(missin_packages)
tic('Tiempo de instalacion de paquetes:')
if(length(missin_packages)) install.packages(missin_packages)
toc()