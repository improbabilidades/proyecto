#!/bin/bash

# Clonar el repositorio original
git clone https://github.com/mpss-eie/proyecto.git
cd proyecto || exit

# Crear un nuevo repositorio para grupos 01 a 17
for i in $(seq -w 1 17); do
    # Cambiar el nombre del repositorio remoto
    git remote set-url origin https://github.com/mpss-eie/proyecto-2025-1-$i.git
    
    # Actualizar el repositorio remoto
    git branch -M main
    git push -u origin main
done