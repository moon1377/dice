import os
import random
from flask import Flask, render_template

app = Flask(__name__)


def get_sides():
    """Return how many sides the die should have based on the DICE_SIDES env var."""
    # TODO: leer DICE_SIDES desde la variable de entorno (usa os.getenv como base)
    dice_env = os.getenv("DICE_SIDES", "6")
    # TODO: convertirlo a int, validar que sea >= 2 y devolverlo
    try:
        sides = int(dice_env)
        if sides < 2:
    # TODO: si la variable no existe o es invalida, devolver 6
            raise ValueError("DICE_SIDES debe ser >= 2")
    except ValueError:
        sides = 6

    # TODO: si la variable no existe o es invalida, devolver 6
    return 6  # 


@app.route("/")
def index():
    sides = get_sides()
    # TODO: generar un numero aleatorio entre 1 y `sides`
    result = random.randint(1, sides)
    return render_template("index.html", result=result, sides=sides)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)
