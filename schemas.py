from pydantic import BaseModel
from typing import List, Literal

class Recipe(BaseModel):
    recipe_id: str
    name: str
    place: Literal["petit-dejeuner", "entree", "plat"]
    kcal: float
    proteines: float
    lipides: float

class Constraints(BaseModel):
    kcal: float
    proteines: float
    lipides: float

class MealDetail(BaseModel):
    entree: bool
    plat: bool

class MealsStructure(BaseModel):
    petit_dejeuner: int
    dejeuner: MealDetail
    diner: MealDetail

class RequestMenu(BaseModel):
    recipes: List[Recipe]
    daily_constraints: Constraints
    meals_structure: MealsStructure

