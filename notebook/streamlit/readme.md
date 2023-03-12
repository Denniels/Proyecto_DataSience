#crear entorno virtual
python -m venv <nombre_entorno_virtual>
python -m venv automotoraenv

permiso exepcion de politicas en consola powershell
ejecutar comando: Set-ExecutionPolicy Unrestricted
a la pregunta escribir s

#entrar a entorno virtual
automotoraenv/Scripts/activate

ayuda:
https://www.youtube.com/watch?v=JyCE-yxeGl0

comando streamlit:
streamlit run notebook\streamlit\automotora_web.py

instalar psycopg2
python -m pip install psycopg2
