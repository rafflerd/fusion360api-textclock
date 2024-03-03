#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

_app =None
_ui= None
_rowNumber =0
_rowNumber2=0
data={'taille_police':5,
        'taille_horizontal':10,
        'taille_vertical':10,
        'offset_cadre':10,
        'nom_police':"Stencil",
        'text':[
            "ILRESTEUDEUX",
            "QUATRE2TROIS",
            "NEUFUNE3SEPT",
            "HUITNSIXCINQ",
            "MIDIX4MINUIT",
            "ONZE75HEURES",
            "MOINSZLE1DIX",
            "CKFETGOUARTJ",
            "HVINGT-CINQK",
            "LMETNDEMIEST"]
}
matrice={'largeur_max':16,
         'hauteur_max':16,
         'parcour_H':'GDG',
         'parcour_V':'HB',
         'prefix':'uint8_t word_',
         'affectation':'[]=',
         'prefix_liste':'{',
         'separateur_liste':',',
         'sufixe_liste':'};',
         'commentaire_fin_ligne':'//',
         'phrase':["IL EST DEUX HEURES"] 
}  

#Global set of event handlers to keep them referenced for the duration of the command
_handlers = []

header_tab="<style> table,th,td{font:\"Georgia\";border-collapse:collapse;font-size:7px;border:1px solid black;} th,td{align:center;padding:2px;text-align:center}</style>"
foother_tab=""   
def create_html(header,foother,data):
    html_str=header+"<table>"
    for ligne in data:
        html_str=html_str+"<tr>"
        for char in ligne:
            html_str=html_str+"<td>"+char+"</td>"
        html_str=html_str+"</tr>"
    html_str=html_str+"</table>"+foother
    return html_str
def cherche_mots(tableau,txt):
    liste_txt=txt.split()
    liste_mots=[]
    for mots in liste_txt:
        skip=mots.count("/")
        mots=mots.strip("/")
        liste_mots.append([mots,skip,-1,-1,-1])
    print(len(liste_mots))
    for indice in range(len(liste_mots)):
        skip_mots=liste_mots[indice][1]
        mots=liste_mots[indice][0]
        cpt=0
        for ligne in tableau:
            start=ligne.find(mots)
            largeur_mots=len(mots)
            fin_mots=start+largeur_mots-1
            if start>-1:
                skip_mots-=1
                if skip_mots==-1:
                    liste_mots[indice][2]=cpt
                    liste_mots[indice][3]=start
                    liste_mots[indice][4]=fin_mots
                    
            cpt+=1
    liste_mots.sort(key=lambda liste_mots:liste_mots[2]) #trie la liste par ligne       
    return liste_mots
def create_html_color(header,foother,data,compare):
    html_str=header+"<table>"
    liste_text=str(compare).split()
    compteur_ligne=0
    for ligne in data:
        
        html_str=html_str+"<tr>"
        compteur_char=0
        for char in ligne:
            couleur='<td style="color:black;">'
            for data in compare:
                
                
                if (data[2]==compteur_ligne) and (compteur_char>=data[3]) and (compteur_char<=data[4]):
                    couleur='<td style="color:red;">'
                
            compteur_char+=1
            html_str=html_str+couleur+char+"</td>"
        compteur_ligne+=1

        html_str=html_str+"</tr>"
    html_str=html_str+"</table>"+foother
    return html_str

def addRowToTable(tableInput,Contenu):
    global _rowNumber
    # Get the CommandInputs object associated with the parent command.
    cmdInputs = adsk.core.CommandInputs.cast(tableInput.commandInputs)
    row = tableInput.rowCount
    # Create three new command inputs.
    valueInput = cmdInputs.addTextBoxCommandInput('TableInput_string1{}'.format(_rowNumber),'ligne',str(row+1),1,True)
    stringInput =  cmdInputs.addStringValueInput('TableInput_string1{}'.format(_rowNumber), 'String', Contenu)
     
    # Add the inputs to the table.
    
    tableInput.addCommandInput(valueInput, row, 0)
    tableInput.addCommandInput(stringInput, row, 1)
   
    # Increment a counter used to make each row unique.
    _rowNumber = _rowNumber + 1

def addRowToTable2(tableInput,Contenu):
    global _rowNumber2
    # Get the CommandInputs object associated with the parent command.
    cmdInputs = adsk.core.CommandInputs.cast(tableInput.commandInputs)
    row = tableInput.rowCount
    # Create three new command inputs.
    valueInput = cmdInputs.addTextBoxCommandInput('TableInput_string2{}'.format(_rowNumber2),'ligne',str(row+1),1,True)
    stringInput =  cmdInputs.addStringValueInput('TableInput_string2{}'.format(_rowNumber2), 'String', Contenu)
     
    # Add the inputs to the table.
    
    tableInput.addCommandInput(valueInput, row, 0)
    tableInput.addCommandInput(stringInput, row, 1)
   
    # Increment a counter used to make each row unique.
    _rowNumber2 = _rowNumber2 + 1

def removeRowToTable(tableInput,Contenu):
    global _rowNumber
    # Get the CommandInputs object associated with the parent command.
    cmdInputs = adsk.core.CommandInputs.cast(tableInput.commandInputs)
    row = tableInput.rowCount
    # Create three new command inputs.
    valueInput = cmdInputs.addTextBoxCommandInput('TableInput_string1{}'.format(_rowNumber),'ligne',str(row),1,True)
    stringInput =  cmdInputs.addStringValueInput('TableInput_string1{}'.format(_rowNumber), 'String', Contenu)
     
    # Add the inputs to the table.
    
    tableInput.addCommandInput(valueInput, row, 0)
    tableInput.addCommandInput(stringInput, row, 1)
   
    # Increment a counter used to make each row unique.
    _rowNumber = _rowNumber + 1

def removeRowToTable2(tableInput,Contenu):
    global _rowNumber2
    # Get the CommandInputs object associated with the parent command.
    cmdInputs = adsk.core.CommandInputs.cast(tableInput.commandInputs)
    row = tableInput.rowCount
    # Create three new command inputs.
    valueInput = cmdInputs.addTextBoxCommandInput('TableInput_string2{}'.format(_rowNumber2),'ligne',str(row),1,True)
    stringInput =  cmdInputs.addStringValueInput('TableInput_string2{}'.format(_rowNumber2), 'String', Contenu)
     
    # Add the inputs to the table.
    
    tableInput.addCommandInput(valueInput, row, 0)
    tableInput.addCommandInput(stringInput, row, 1)
   
    # Increment a counter used to make each row unique.
    _rowNumber2 = _rowNumber2 + 1

class MyCommandInputChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            eventArgs = adsk.core.InputChangedEventArgs.cast(args)
            inputs = eventArgs.inputs
            cmdInput = eventArgs.input
            # onInputChange for slider controller
            tableInput = inputs.itemById('table')
            tableInput2= inputs.itemById('table2')
            htmlInput=inputs.itemById('fullWidth_textBox')
            htmlInputColor=inputs.itemById('fullWidth_textBox2')
#            adsk.core.Application.log(str(cmdInput.name)+"-->"+str(tableInput.selectedRow))
            if  'TableInput_string1' in cmdInput.id:
                indice=int(cmdInput.id[18:])
                if indice==tableInput.selectedRow:
                    data['text'][indice]=tableInput.getInputAtPosition(indice,1).value
#                    adsk.core.Application.log(str(create_html(header_tab,"",data['text'])))
                htmlInput.formattedText=create_html(header_tab,"",data['text'])
            elif "TableInput_string2" in cmdInput.id:
                indice=int(cmdInput.id[18:])
                if indice==tableInput2.selectedRow:
                    matrice['phrase'][indice]=tableInput2.getInputAtPosition(indice,1).value
#                    adsk.core.Application.log(str(create_html(header_tab,"",data['text'])))
                    mots_trouve=cherche_mots(data['text'],matrice['phrase'][indice])
                    message = create_html_color(header_tab,foother_tab,data['text'],mots_trouve)
                    
                    htmlInputColor.formattedText=message
            elif cmdInput.id == 'tableAdd':
                addRowToTable(tableInput,'Vide')
                data['text'].append('Vide')
                htmlInput.formattedText=create_html(header_tab,"",data['text'])
            elif cmdInput.id == 'tableAdd2':
                addRowToTable2(tableInput2,'IL')
                matrice['phrase'].append('IL')
                mots_trouve=cherche_mots(data['text'],'IL')
                message = create_html_color(header_tab,foother_tab,data['text'],mots_trouve)
                htmlInputColor.formattedText=message
            elif cmdInput.id == 'tableDelete':
                if tableInput.selectedRow == -1:
                    _ui.messageBox('Select one row to delete.')
                else:
                    row_deleted=tableInput.selectedRow
                    tableInput.deleteRow(row_deleted)
                    data['text'].pop(row_deleted)
                    for row in range(tableInput.rowCount):
                        indice=tableInput.getInputAtPosition(row, 0)
                        indice.text=str(row)
                    htmlInput.formattedText=create_html(header_tab,"",data['text'])
            elif cmdInput.id == 'tableDelete2':
                if tableInput2.selectedRow == -1:
                    _ui.messageBox('Select one row to delete.')
                else:
                    row_deleted=tableInput2.selectedRow
                    tableInput2.deleteRow(row_deleted)
                    matrice['phrase'].pop(row_deleted)
                    for row in range(tableInput2.rowCount):
                        indice=tableInput2.getInputAtPosition(row, 0)
                        indice.text=str(row)
                        htmlInput.formattedText=create_html(header_tab,"",data['text'])
                    pass
                    
        except:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Event handler that reacts to when the command is destroyed. This terminates the script.            
class MyCommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # When the command is done, terminate the script
            # This will release all globals which will remove all event handlers
            adsk.terminate()
        except:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Event handler that reacts when the command definitio is executed which
# results in the command being created and this event being fired.
class MyCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # Get the command that was created.
            cmd = adsk.core.Command.cast(args.command)

            # Connect to the command destroyed event.
            onDestroy = MyCommandDestroyHandler()
            cmd.destroy.add(onDestroy)
            _handlers.append(onDestroy)

            # Connect to the input changed event.           
            onInputChanged = MyCommandInputChangedHandler()
            cmd.inputChanged.add(onInputChanged)
            _handlers.append(onInputChanged)    

            # Get the CommandInputs collection associated with the command.
            inputs = cmd.commandInputs



            # Create a tab input.
            tabCmdInput1 = inputs.addTabCommandInput('tab_1', 'Parametre esquisse')
            tab1ChildInputs = tabCmdInput1.children
            
            tab1ChildInputs.addImageCommandInput('image', 'Image', "resources/Param1.png")
               
            # Create distance value input 1.
            distanceValueInput = tab1ChildInputs.addDistanceValueCommandInput('distanceValueH', 'Largeur', adsk.core.ValueInput.createByReal(data['taille_horizontal']/10))
            distanceValueInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0))
            distanceValueInput.minimumValue = 0
            distanceValueInput.isMinimumValueInclusive = True
            distanceValueInput.maximumValue = 10
            distanceValueInput.isMaximumValueInclusive = True

            # Create distance value input 1.
            distanceValueInput = tab1ChildInputs.addDistanceValueCommandInput('distanceValueV', 'Hauteur', adsk.core.ValueInput.createByReal(data['taille_vertical']/10))
            distanceValueInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0))
            distanceValueInput.minimumValue = 0
            distanceValueInput.isMinimumValueInclusive = True
            distanceValueInput.maximumValue = 10
            distanceValueInput.isMaximumValueInclusive = True

            # Create distance value input 1.
            distanceValueInput = tab1ChildInputs.addDistanceValueCommandInput('TailleP', 'Taille de la police', adsk.core.ValueInput.createByReal(data['taille_police']/10))
            distanceValueInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0))
            distanceValueInput.minimumValue = 0
            distanceValueInput.isMinimumValueInclusive = True
            distanceValueInput.maximumValue = 10
            distanceValueInput.isMaximumValueInclusive = True

#           message = '<div align="center"><p style="color:blue;font-family:\"Georgia\""> Boites de caratères</div>'

#            tab1ChildInputs.addTextBoxCommandInput('fullWidth_textBox', '', message, 10, True) 

            MaPolice = tab1ChildInputs.addStringValueInput('Police', 'Police de caracrère', data['nom_police'])
            # Create a tab input.
            tabCmdInput2 = inputs.addTabCommandInput('tab_2', 'Tableau caractère')
            tab2ChildInputs = tabCmdInput2.children

            message = create_html(header_tab,"",data['text'])
            tab2ChildInputs.addTextBoxCommandInput('fullWidth_textBox', '', message, 10, True) 
            


           # Create table input
            tableInput = tab2ChildInputs.addTableCommandInput('table', 'Table', 2, '1:4')
            for ligne in data['text']:
                addRowToTable(tableInput,ligne)

 
            addButtonInput = tab2ChildInputs.addBoolValueInput('tableAdd', 'Add', False, '', True)
            tableInput.addToolbarCommandInput(addButtonInput)
            deleteButtonInput = tab2ChildInputs.addBoolValueInput('tableDelete', 'Delete', False, '', True)
            tableInput.addToolbarCommandInput(deleteButtonInput)

            tabCmdInput3 = inputs.addTabCommandInput('tab_3', 'Controle Text')
            tab3ChildInputs = tabCmdInput3.children
            mots_trouve=cherche_mots(data['text'],"IL EST DEUX HEURES")
            message = create_html_color(header_tab,foother_tab,data['text'],mots_trouve)
            tab3ChildInputs.addTextBoxCommandInput('fullWidth_textBox2', '', message, 10, True) 

                       # Create table input
            tableInput2 = tab3ChildInputs.addTableCommandInput('table2', 'Table', 2, '1:4')
            for ligne in matrice['phrase']:
                addRowToTable2(tableInput2,ligne)

 
            addButtonInput2 = tab3ChildInputs.addBoolValueInput('tableAdd2', 'Add', False, '', True)
            tableInput2.addToolbarCommandInput(addButtonInput2)
            deleteButtonInput2 = tab3ChildInputs.addBoolValueInput('tableDelete2', 'Delete', False, '', True)
            tableInput2.addToolbarCommandInput(deleteButtonInput2)

        #    # Create a selection input.
        #     selectionInput = tab1ChildInputs.addSelectionInput('selection', 'Select', 'Basic select command input')
        #     selectionInput.setSelectionLimits(0)


        #     # Create value input.
        #     tab1ChildInputs.addValueInput('value', 'Value', 'cm', adsk.core.ValueInput.createByReal(0.0))

        #     # Create bool value input with checkbox style.
        #     tab1ChildInputs.addBoolValueInput('checkbox', 'Checkbox', True, '', False)


        #     # Create bool value input with button style that can be clicked.
        #     tab1ChildInputs.addBoolValueInput('buttonClick', 'Click Button', False, 'resources/button', True)

        #     # Create bool value input with button style that has a state.
        #     tab1ChildInputs.addBoolValueInput('buttonState', 'State Button', True, 'resources/button', True)

        #     # Create float slider input with two sliders.
        #     tab1ChildInputs.addFloatSliderCommandInput('floatSlider', 'Float Slider', 'cm', 0, 10.0, True)

        #     # Create float slider input with two sliders and a value list.
        #     floatValueList = [1.0, 3.0, 4.0, 7.0]
        #     tab1ChildInputs.addFloatSliderListCommandInput('floatSlider2', 'Float Slider 2', 'cm', floatValueList)

        #     # Create float slider input with two sliders and visible texts.
        #     floatSlider3 = tab1ChildInputs.addFloatSliderCommandInput('floatSlider3', 'Float Slider 3', '', 0, 50.0, False)
        #     floatSlider3.setText('Min', 'Max')

        #     # Create integer slider input with one slider.
        #     tab1ChildInputs.addIntegerSliderCommandInput('intSlider', 'Integer Slider', 0, 10);
        #     valueList = [1, 3, 4, 7, 11]

        #     # Create integer slider input with two sliders and a value list.
        #     tab1ChildInputs.addIntegerSliderListCommandInput('intSlider2', 'Integer Slider 2', valueList)

        #     # Create float spinner input.
        #     tab1ChildInputs.addFloatSpinnerCommandInput('spinnerFloat', 'Float Spinner', 'cm', 0.2 , 9.0 , 2.2, 1)

        #     # Create integer spinner input.
        #     tab1ChildInputs.addIntegerSpinnerCommandInput('spinnerInt', 'Integer Spinner', 2 , 9 , 2, 3)

        #     # Create dropdown input with checkbox style.
        #     dropdownInput = tab1ChildInputs.addDropDownCommandInput('dropdown', 'Dropdown 1', adsk.core.DropDownStyles.CheckBoxDropDownStyle)
        #     dropdownItems = dropdownInput.listItems
        #     dropdownItems.add('Item 1', False, 'resources/One')
        #     dropdownItems.add('Item 2', False, 'resources/Two')

        #     # Create dropdown input with icon style.
        #     dropdownInput2 = tab1ChildInputs.addDropDownCommandInput('dropdown2', 'Dropdown 2', adsk.core.DropDownStyles.LabeledIconDropDownStyle);
        #     dropdown2Items = dropdownInput2.listItems
        #     dropdown2Items.add('Item 1', True, 'resources/One')
        #     dropdown2Items.add('Item 2', False, 'resources/Two')

        #     # Create dropdown input with radio style.
        #     dropdownInput3 = tab1ChildInputs.addDropDownCommandInput('dropdown3', 'Dropdown 3', adsk.core.DropDownStyles.LabeledIconDropDownStyle);
        #     dropdown3Items = dropdownInput3.listItems
        #     dropdown3Items.add('Item 1', True, '')
        #     dropdown3Items.add('Item 2', False, '')

        #     # Create dropdown input with test list style.
        #     dropdownInput4 = tab1ChildInputs.addDropDownCommandInput('dropdown4', 'Dropdown 4', adsk.core.DropDownStyles.TextListDropDownStyle);
        #     dropdown4Items = dropdownInput4.listItems
        #     dropdown4Items.add('Item 1', True, '')
        #     dropdown4Items.add('Item 2', False, '')

        #     # Create single selectable button row input.
        #     buttonRowInput = tab1ChildInputs.addButtonRowCommandInput('buttonRow', 'Single Select Buttons', False)
        #     buttonRowInput.listItems.add('Item 1', False, 'resources/One')
        #     buttonRowInput.listItems.add('Item 2', False, 'resources/Two')

        #     # Create multi selectable button row input.
        #     buttonRowInput2 = tab1ChildInputs.addButtonRowCommandInput('buttonRow2', 'Multi-select Buttons', True)
        #     buttonRowInput2.listItems.add('Item 1', False, 'resources/One')
        #     buttonRowInput2.listItems.add('Item 2', False, 'resources/Two')

        #     # Create tab input 2
        #     tabCmdInput2 = inputs.addTabCommandInput('tab_2', 'Tab 2')
        #     tab2ChildInputs = tabCmdInput2.children

        #     # Create group input.
        #     groupCmdInput = tab2ChildInputs.addGroupCommandInput('group', 'Group')
        #     groupCmdInput.isExpanded = True
        #     groupCmdInput.isEnabledCheckBoxDisplayed = True
        #     groupChildInputs = groupCmdInput.children
            
        #     # Create radio button group input.
        #     radioButtonGroup = groupChildInputs.addRadioButtonGroupCommandInput('radioButtonGroup', 'Radio button group')
        #     radioButtonItems = radioButtonGroup.listItems
        #     radioButtonItems.add("Item 1", False)
        #     radioButtonItems.add("Item 2", False)
        #     radioButtonItems.add("Item 3", False)
            
        #     # Create image input.
        #     groupChildInputs.addImageCommandInput('image', 'Image', "resources/image.png")
            
        #     # Create direction input 1.
        #     directionCmdInput = tab2ChildInputs.addDirectionCommandInput('direction', 'Direction1')
        #     directionCmdInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0))
            
        #     # Create direction input 2.
        #     directionCmdInput2 = tab2ChildInputs.addDirectionCommandInput('direction2', 'Direction 2', 'resources/One')
        #     directionCmdInput2.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(0, 1, 0)) 
        #     directionCmdInput2.isDirectionFlipped = True
            
        #     # Create distance value input 1.
        #     distanceValueInput = tab2ChildInputs.addDistanceValueCommandInput('distanceValue', 'DistanceValue', adsk.core.ValueInput.createByReal(2))
        #     distanceValueInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0))
        #     distanceValueInput.minimumValue = 0
        #     distanceValueInput.isMinimumValueInclusive = True
        #     distanceValueInput.maximumValue = 10
        #     distanceValueInput.isMaximumValueInclusive = True
            
        #     # Create distance value input 2.
        #     distanceValueInput2 = tab2ChildInputs.addDistanceValueCommandInput('distanceValue2', 'DistanceValue 2', adsk.core.ValueInput.createByReal(1))
        #     distanceValueInput2.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(0, 1, 0))
        #     distanceValueInput2.expression = '1 in'
        #     distanceValueInput2.hasMinimumValue = False
        #     distanceValueInput2.hasMaximumValue = False
            
        #     # Add inputs into the table.            

            
        #     # Create angle value input.
        #     angleValueInput = tab2ChildInputs.addAngleValueCommandInput('angleValue', 'AngleValue', adsk.core.ValueInput.createByString('30 degree'))
        #     angleValueInput.setManipulator(adsk.core.Point3D.create(0, 0, 0), adsk.core.Vector3D.create(1, 0, 0), adsk.core.Vector3D.create(0, 0, 1))
        #     angleValueInput.hasMinimumValue = False
        #     angleValueInput.hasMaximumValue = False

        #     # Create tab input 3
        #     tabCmdInput3 = inputs.addTabCommandInput('tab_3', 'Tab 3')
        #     tab3ChildInputs = tabCmdInput3.children
        #     # Create group
        #     sliderGroup = tab3ChildInputs.addGroupCommandInput("slider_configuration", "Configuration")
        #     sliderInputs = sliderGroup.children


        except:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))




def run(context):
    try:
        global _app, _ui
        _app = adsk.core.Application.get()
        _ui = _app.userInterface

        # Get the existing command definition or create it if it doesn't already exist.
        cmdDef = _ui.commandDefinitions.itemById('cmdInputsSample')
        if not cmdDef:
            cmdDef = _ui.commandDefinitions.addButtonDefinition('cmdInputsSample', 'Text Clock', 'Générateur de matrice de texte')
        cmdDef.name="Text Clock"
        # Connect to the command created event.
        onCommandCreated = MyCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        _handlers.append(onCommandCreated)

        # Execute the command definition.
        cmdDef.execute()

        # Prevent this module from being terminated when the script returns, because we are waiting for event handlers to fire.
        adsk.autoTerminate(False)
    except:
        if _ui:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))