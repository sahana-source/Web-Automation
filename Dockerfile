FROM python:3.12-slim

# System deps + Chrome runtime libraries
RUN apt-get update && apt-get install -y \
    wget gnupg unzip ca-certificates curl \
    # fonts + X11/GTK/DRM/GBM/NSPR/NSS etc. required by chrome
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libexpat1 \
    libfontconfig1 \
    libgbm1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libu2f-udev \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxkbcommon0 \
    libxshmfence1 \
    xdg-utils \
 && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -qO - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg \
 && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list \
 && apt-get update && apt-get install -y google-chrome-stable \
 && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/google-chrome

WORKDIR /app
COPY requirements.txt .
# (optional but helpful)
ENV PIP_DEFAULT_TIMEOUT=60
RUN pip install --no-cache-dir -r requirements.txt
# running yaml file github actions

COPY . .

ENV HEADLESS=1
ENV REPORT_PATH=/reports/report.html

RUN mkdir -p /reports

CMD ["pytest", "-v", "--html=/reports/report.html", "--self-contained-html"]
