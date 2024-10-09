from fastapi import FastAPI
from app.routes import (
    facturation, utilisateur, journal_activites, patient, mutuelle, medicament,
    tva_marges, produit, stock, sessions_utilisateur, ordonnance, patient_mutuelle
)

app = FastAPI()

# Inclusion des routes
app.include_router(facturation.router)
app.include_router(utilisateur.router)
app.include_router(journal_activites.router)
app.include_router(patient.router)
app.include_router(mutuelle.router)
app.include_router(medicament.router)
app.include_router(tva_marges.router)
app.include_router(produit.router)
app.include_router(stock.router)
app.include_router(sessions_utilisateur.router)
app.include_router(ordonnance.router)
app.include_router(patient_mutuelle.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API de gestion officinale"}

@app.get("/status")
def status():
    return {"status": "API is running correctly"}
