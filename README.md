## Capturas de la pantalla de `http://localhost:8888` y del health
<img width="1918" height="1012" alt="Captura de pantalla 2025-10-30 200058" src="https://github.com/user-attachments/assets/80a72ec0-1660-4cd3-b2d4-7dc6179331e2" />
<img width="1918" height="996" alt="Captura de pantalla 2025-10-30 200120" src="https://github.com/user-attachments/assets/3b7c771a-056e-4b3d-9a86-f638e19d5d87" />

## Breve explicación del `-e DICE_SIDES=...`
Cuando ejecutas el contenedor docker con `-e DICE_SIDES=...` lo que hace es definir el valor que le pongamos, por ejemplo '-e DICE_SIDES=20' pone
que el dado sea por defecto 20 caras.



## Entrega

- Carpeta con `app.py`, `templates/index.html`, `requirements.txt`, `Dockerfile`.
- **README.md** con:
  - Comandos de build y ejecucion (con y sin `DICE_SIDES`).
  - Captura de pantalla de `http://localhost:8888`.
  - Breve explicacion (2-3 lineas) de que cambia al usar `-e DICE_SIDES=...`.

## Rubrica (10 pt)

- **App funcional** (4 pt): `/` muestra la tirada; `/health` responde ok; lectura correcta de `DICE_SIDES` (valor por defecto + validacion).
- **Dockerizacion** (4 pt): build sin errores; puerto 5000 expuesto; contenedor operativo al publicar `8888:5000`.
- **Documentacion** (2 pt): README con comandos y captura.
