# Utilise une image Python légère
FROM python:3.9-slim

# Définit le répertoire de travail dans le container
WORKDIR /app

# Copie le fichier de dépendances dans le container
COPY requirements.txt .

# Installe les dépendances listées dans requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copie le reste du code de l'application dans le container
COPY . .

# Expose le port 8000 (utilisé par Uvicorn)
EXPOSE 8000

# Commande pour démarrer l'application FastAPI avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
