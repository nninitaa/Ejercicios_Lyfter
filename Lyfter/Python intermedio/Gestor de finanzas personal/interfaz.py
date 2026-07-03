import FreeSimpleGUI as sg
from logic import FinanceManager 
manager = FinanceManager()

FONT_TITLE = ('Georgia', 16, 'italic bold')
FONT_LABEL = ('Georgia', 11)
FONT_BUTTON = ('Georgia', 10, 'bold')
MAIN_PINK = '#E8A7A1'    
BUTTON_PINK = '#D17A71'  
BUTTON_TEXT = '#FFFFFF'

def add_category_window():
    layout = [
        [sg.Text('Add New Category', font=FONT_TITLE, text_color=BUTTON_PINK, pad=(0, 15))],
        [sg.Text('Category Name:', font=FONT_LABEL, size=(13, 1)), 
         sg.Input(key='-IN_CATEGORIA-', size=(22, 1), font=FONT_LABEL)],
        [sg.Text('', pad=(0,7))],
        [sg.Button('Save', key='-BTN_CAT-', button_color=(BUTTON_TEXT, BUTTON_PINK), font=FONT_BUTTON, size=(10, 1)),
         sg.Button('Cancel', key='-CANCEL-', button_color=('#000000', '#E0E0E0'), font=FONT_BUTTON, size=(10, 1))]
    ]

    window = sg.Window('Category Management', layout, finalize=True, modal=True, element_padding=(10, 5))
    created_category = False

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-CANCEL-'):
            break
            
        if event == '-BTN_CAT-':
            success, message = manager.register_category(values['-IN_CATEGORIA-'])
            if success:
                sg.popup_quick_message(message, background_color=MAIN_PINK, text_color='#000000')
                created_category = True
                break  
            else:
                sg.popup_error(message, title='Error', button_color=(BUTTON_TEXT, BUTTON_PINK))
                
    window.close()
    return created_category

def register_transaction_window(type_transaction):
    title_window = 'Register Income' if type_transaction == 'Income' else 'Register Expense'
    
    layout = [
        [sg.Text(title_window, font=FONT_TITLE, text_color=BUTTON_PINK, pad=(0, 15))],
        
        [sg.Text('Title:', font=FONT_LABEL, size=(12, 1)), 
         sg.Input(key='-TITULO-', size=(22, 1), font=FONT_LABEL)],
         
        [sg.Text('Category:', font=FONT_LABEL, size=(12, 1)), 
         sg.Combo(manager.get_categories(), key='-COMBO_CAT-', readonly=True, size=(20, 1), font=FONT_LABEL)],

        [sg.Text('Amount ($):', font=FONT_LABEL, size=(12, 1)), 
         sg.Input(key='-MONTO-', size=(22, 1), font=FONT_LABEL)],
         
        [sg.Text('', pad=(0, 7))],
        [sg.Button('Save', key='-BTN_MOV-', button_color=(BUTTON_TEXT, BUTTON_PINK), font=FONT_BUTTON, size=(10, 1)),
         sg.Button('Cancel', key='-CANCEL-', button_color=('#000000', '#E0E0E0'), font=FONT_BUTTON, size=(10, 1))]
    ]
    
    window = sg.Window(title_window, layout, finalize=True, modal=True, element_padding=(10, 5))
    transaction_made = False

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-CANCEL-'):
            break
            
        if event == '-BTN_MOV-':
            title = values['-TITULO-']
            category = values['-COMBO_CAT-']
            amount = values['-MONTO-']

            success, message = manager.register_transaction(type_transaction, category, amount, title)
            if success:
                sg.popup_quick_message(message, background_color=MAIN_PINK, text_color='#000000')
                transaction_made = True
                break
            else:
                sg.popup_error(message, title='Warning', button_color=(BUTTON_TEXT, BUTTON_PINK))
                
    window.close()
    return transaction_made

def start_interfaz():
    sg.theme('LightGray1') 
    layout = [
        [sg.Text('Personal Finance Manager', font=FONT_TITLE, text_color=BUTTON_PINK, pad=(0, 15))],
        [sg.Button('Add Category', key='-GO_CAT-', button_color=(BUTTON_TEXT, BUTTON_PINK), font=FONT_BUTTON, size=(16, 1), pad=((0, 8), 0)),
         sg.Button('Add Income', key='-GO_INCOME-', button_color=(BUTTON_TEXT, BUTTON_PINK), font=FONT_BUTTON, size=(16, 1), pad=((0, 8), 0)),
         sg.Button('Add Expense', key='-GO_EXPENSE-', button_color=(BUTTON_TEXT, BUTTON_PINK), font=FONT_BUTTON, size=(16, 1))],
        [sg.HSeparator(pad=(0, 25))],
        [sg.Text('Transaction History:', font=FONT_LABEL, text_color=BUTTON_PINK, pad=(0, 5))],
        [sg.Table(values=manager.get_transaction_tables(), 
                  headings=['Title', 'Type', 'Category', 'Amount'],
                  auto_size_columns=True,
                  justification='center', 
                  key='-TABLA-', 
                  num_rows=10,
                  font=FONT_LABEL,
                  header_font=FONT_BUTTON,
                  header_background_color=MAIN_PINK,
                  header_text_color='#000000',
                  expand_x=True)],
                  
        [sg.Button('Exit', size=(10, 1), button_color=('#000000', '#E0E0E0'), font=FONT_BUTTON, pad=(0, 15))]
    ]
    window = sg.Window('My Finances - Dashboard', layout, finalize=True, element_padding=(5, 5))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break          
        if event == '-GO_CAT-':
            if add_category_window():
                pass 
        if event == '-GO_INCOME-':
            if register_transaction_window('Income'):
                window['-TABLA-'].update(values=manager.get_transaction_tables())
        if event == '-GO_EXPENSE-':
            if register_transaction_window('Expense'):
                window['-TABLA-'].update(values=manager.get_transaction_tables())

    window.close()

if __name__ == '__main__':
    start_interfaz()