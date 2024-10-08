
from pydantic import BaseModel
from datetime import datetime

class JournalActivitesBase(BaseModel):
    utilisateur_id: int
    date_activite: datetime
    type_activite: str
    description: str

class JournalActivitesCreate(JournalActivitesBase):
    pass

class JournalActivites(JournalActivitesBase):
    id: int

    class Config:
        orm_mode = True
