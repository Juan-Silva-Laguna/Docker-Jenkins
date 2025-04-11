FROM jenkins/jenkins:lts

USER root

# Instalar Python y pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Crear carpeta de trabajo y copiar archivos
WORKDIR /app
COPY funcion/ ./funcion/

# Instalar pytest
RUN pip3 install --break-system-packages pytest

# Exponer Jenkins
EXPOSE 8080

# Volver al usuario Jenkins (por seguridad)
USER jenkins
