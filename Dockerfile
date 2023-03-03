FROM python:3.9-slim-buster

# Instala dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    wget \
    libnss3 \
    gnupg

RUN wget -q -O- https://dl.google.com/linux/linux_signing_key.pub | apt-key add -  && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google.list

RUN apt-get update && apt-get install -y \
    google-chrome-stable

# Descarga y guarda Chromedriver en /usr/bin
RUN CD_LAST_RELEASE=$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -qO tmp.zip http://chromedriver.storage.googleapis.com/$CD_LAST_RELEASE/chromedriver_linux64.zip && \
    unzip -j tmp.zip chromedriver -d /usr/local/bin  && rm tmp.zip && \
    chown root:root /usr/local/bin/chromedriver  && \
    chmod 0777 /usr/local/bin/chromedriver

# Copia el código fuente en la imagen de Docker
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py /app/main.py

# Configura el entorno
ENV DISPLAY=:99

# Ejecuta el script de automatización al iniciar el contenedor
CMD xvfb-run --server-args="-screen 0 1024x768x24" python main.py

# Desactiva el CMD line 37 y con Entrypoint entras a la consola del docker corrienddo
#ENTRYPOINT ["sh"]