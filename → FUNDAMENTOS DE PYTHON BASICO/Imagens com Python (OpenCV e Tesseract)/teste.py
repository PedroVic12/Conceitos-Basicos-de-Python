from PIL import Image
import pytesseract
import cv2
import os

os.system('cls')
""" 
! links úteis:

! corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

! instalar outra língua: https://github.com/tesseract-ocr/tessdata

! pegar linguas: print(pytesseract.get_languages())
"""

# Passo 1: Ler a imagem
imagem = cv2.imread('teste2.png')

# Definindo o caminho onde esta instalado o tesseract
caminho = r"C:\Users\pedro\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = caminho 

# Passo 2: Pedir pro tesseract extrair o texto da imagem

texto = pytesseract.image_to_string(imagem, lang = 'por')

print(texto.split())

