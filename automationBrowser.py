import pyautogui

#clica no ícone do navegador
pyautogui.click(35,196,duration=1.5)

#clica na primeira página aberta
pyautogui.click(180,44,duration=1.5)

#clica na barra de url
pyautogui.click(436,94,duration=1.5)

#faz a pesquisa do site desejado
pyautogui.write('youtube.com')
pyautogui.press('enter')

#nesse comando estava apenas brincando.
#pyautogui.confirm(text='Sua senha está expirada', title='Teste', buttons=['OK', 'Cancel'])