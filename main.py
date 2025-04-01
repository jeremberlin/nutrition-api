
from fastapi import FastAPI
from schemas import RequestMenu

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenue sur mon API nutrition!"}

@app.post("/api/generate_menu")
async def generate_menu(data: RequestMenu):
    return {
        "status": "success",
        "weekly_menu": {
            "lundi": {
                "petit_dejeuner": {
                    "recipe_id": data.recipes[0].recipe_id,
                    "factor": "+0%"
                },
                "dejeuner": {
                    "entree": {
                        "recipe_id": data.recipes[1].recipe_id,
                        "factor": "+0%"
                    } if data.meals_structure.dejeuner.entree else None,
                    "plat": {
                        "recipe_id": data.recipes[2].recipe_id,
                        "factor": "+0%"
                    }
                },
                "diner": {
                    "entree": {
                        "recipe_id": data.recipes[3].recipe_id,
                        "factor": "+0%"
                    } if data.meals_structure.diner.entree else None,
                    "plat": {
                        "recipe_id": data.recipes[4].recipe_id,
                        "factor": "+0%"
                    }
                }
            }
        }
    }
