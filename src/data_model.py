from pydantic import BaseModel

class water(BaseModel):
    ph : float
    Hardness : float
    Solids : float
    Chloramines : float
    Sulfate : float
    Conductivity : float
    Organic_carbon : float
    Trihalomethanses : float
    Turbidity : float