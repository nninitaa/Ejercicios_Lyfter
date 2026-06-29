import FreeSimpleGUI as sg
import logic

def iniciar_interfaz():
    sg.theme('LightGray1') 

    FONT_TITLE = ('Georgia', 16, 'italic bold')
    FONT_LABEL = ('Georgia', 11)
    FONT_BUTTON = ('Georgia', 10, 'bold')
    MAIN_PINK = '#E8A7A1'    
    BUTTON_PINK = '#D17A71'  
    BUTTON_TEXT = '#FFFFFF'  

    layout = [
        [sg.Text('Personal Finance Manager', font=FONT_TITLE, text_color=BUTTON_PINK, pad=(0, 15))],
        
        [sg.Frame('Category Management', [
            [sg.Text('New Category:', font=FONT_LABEL), 
             sg.Input(key='-IN_CATEGORIA-', size=(20, 1), font=FONT_LABEL), 
             sg.Button('Add Category', key='-BTN_CAT-', button_color=(BUTTON_TEXT, BUTTON_PINK), font=FONT_BUTTON)]
        ], title_color=BUTTON_PINK, font=FONT_LABEL, pad=(0, 10))],
        
        [sg.Frame('Register Income / Expense', [
            [sg.Text('Type:', font=FONT_LABEL), 
             sg.Combo(['Income', 'Expense'], default_value='Expense', key='-TIPO-', readonly=True, size=(10, 1), font=FONT_LABEL),
             sg.Text('Category:', font=FONT_LABEL), 
             sg.Combo(logic.get_categories(), key='-COMBO_CAT-', readonly=True, size=(15, 1), font=FONT_LABEL),
             sg.Text('Amount:', font=FONT_LABEL), 
             sg.Input(key='-MONTO-', size=(10, 1), font=FONT_LABEL),
             sg.Button('Add', key='-BTN_MOV-', button_color=(BUTTON_TEXT, BUTTON_PINK), font=FONT_BUTTON)]
        ], title_color=BUTTON_PINK, font=FONT_LABEL, pad=(0, 10))],

        [sg.Text('Transaction History:', font=FONT_LABEL, text_color=BUTTON_PINK)],
        [sg.Table(values=logic.get_transaction_tables(), 
                  headings=['Type', 'Category', 'Amount'], 
                  auto_size_columns=True,
                  justification='center', 
                  key='-TABLA-', 
                  num_rows=8,
                  font=FONT_LABEL,
                  header_font=FONT_BUTTON,
                  header_background_color=MAIN_PINK,
                  header_text_color='#000000',
                  expand_x=True)],
                  
        [sg.Button('Exit', size=(10, 1), button_color=('#000000', '#E0E0E0'), font=FONT_BUTTON, pad=(0, 15))]
    ]

    window = sg.Window('My Finances', layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == '-BTN_CAT-':
            success, message = logic.register_category(values['-IN_CATEGORIA-'])
            if success:
                sg.popup_quick_message(message, background_color=MAIN_PINK, text_color='#000000')
                window['-COMBO_CAT-'].update(values=logic.get_categories())
                window['-IN_CATEGORIA-'].update('')
            else:
                sg.popup_error(message, title='Error', button_color=(BUTTON_TEXT, BUTTON_PINK))
        if event == '-BTN_MOV-':
            t_type = values['-TIPO-']
            category = values['-COMBO_CAT-']
            amount = values['-MONTO-']
            success, message = logic.register_transaction(t_type, category, amount)
            if success:
                sg.popup_quick_message(message, background_color=MAIN_PINK, text_color='#000000')
                window['-TABLA-'].update(values=logic.get_transaction_tables())
                window['-MONTO-'].update('')
            else:
                sg.popup_error(message, title='Warning', button_color=(BUTTON_TEXT, BUTTON_PINK))

    window.close()
if __name__ == '__main__':
    iniciar_interfaz()