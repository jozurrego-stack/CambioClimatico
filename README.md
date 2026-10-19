# BotClimatico 🌱
Bot de Discord para aprender sobre cambio climático y promover hábitos sostenibles.

## Instalación
1. Instala Python 3.10 o superior.
2. En la terminal de esta carpeta ejecuta `pip install -r requirements.txt`.
3. Pon el token del bot en `.env` como `DISCORD_TOKEN=tu_token`.
4. En Discord Developer Portal activa **Message Content Intent**.
5. Ejecuta `python bot.py`.

## Comandos
`!hola`, `!ayuda`, `!dato`, `!consejo`, `!reto`, `!completar`, `!puntos`,
`!ranking`, `!quiz`, `!respuesta A`, `!noticia`, `!clima`,
`!huella km_bus km_carro kwh_mes`, `!colombia`.

## Copernicus
`!clima` requiere una cuenta en https://cds.climate.copernicus.eu/ y aceptar
los términos del conjunto ERA5. Configura las credenciales según las instrucciones
actuales de Copernicus, mediante `.env` o `~/.cdsapirc`. La descarga no es una
medición instantánea de tu ubicación.

Nunca compartas tu token de Discord ni subas `.env` a GitHub.
