import argparse
import os

lang = 'russian'

if(lang=='english'):
  msg ='Hello World'
elif(lang == 'german'):
    msg = 'Hola'
else:
  msg='Привет'
print(msg)
