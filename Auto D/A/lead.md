"""
    STEPS
    | STEPS                                                                                        | Biblioteca              | Por que                                                                                               |
    | -------------------------------------------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------- |
    | 1. Ver código HTML (F12)                                                                     | Selenium                | Permite inspecionar o HTML diretamente no navegador, identificando elementos e atributos específicos. |
    | 2. Identificar o que é e o que não é questão                                                 | Selenium                | Usando `find_elements`, é possível localizar elementos pelo tipo (ex.: `input`, `textarea`, etc.).    |
    | 3. Categorizar as questões (CHECKBOX, RADIOS, DRAG-DROP...)                                  | Selenium                | Identifica o tipo de elemento pelos atributos, como `type="radio"` ou `type="checkbox"`.              |
    | 4. Extrair texto                                                                             | Selenium, BeautifulSoup | Selenium captura o texto diretamente do DOM; BeautifulSoup pode ajudar em análises mais detalhadas.   |
    | 5. Procurar resposta (Chatgpt - Copiar as perguntas e passar para a Janela onde está o chat) | OpenAI API              | A API permite enviar perguntas ao modelo GPT-3.5-Turbo para obter respostas automatizadas.            |
    | 6. Responder (Simular click do mouse na alternativa)                                         | Selenium                | Simula cliques humanos nos elementos de resposta, como botões ou checkboxes.                          |
    
"""


"""

    ## Always
    * TODO - Getting in CMSP                  ✔ ✖
    * TODO - Type creedentials                ✔ ✖
    * TODO - Getting in Provas Atividades     ✔ ✖
    * TODO - Getting in Todas as atividades   ✔ ✖

    # A fazer
    Se (dentro do da tabela[0] o tbody for vazio/Null) {
        ## Verificar se há atividade para fazer
        ## SENÃO
        ## Verificar se há atividades Expirada

        Vá para Expiradas

            Se (dentro do da tabela[2] o tbody for vazio/Null) {
                Passar para próxima lição
            } Senao {
                TODO - Iterar sobre btn.css-k9aczr ✔ ✖
                * Faça {
                *   SE ( 
                *       dentro do btn.css-k9aczr tiver span.css-1l6c7y9 
                *       OU
                *       O conteúdo do btn.css-1hmr1hq for ! de "Realizar") {
                *       pass
                *   } SE NÃO {
                *       Subtraia -1 nas ativadades
                *       Click no btn.css-1hmr1hq
                *   }
                * Enquanto (Atividades > 0)
            }
    } senao {
        ## Saber quantas atividades tem para fazer, para isso
        ## Itere em quantos bnt.css-k9aczr tem e com base nisso
        ## Faça _____ equanto atividades for > 0

        TODO - Iterar sobre btn.css-k9aczr ✔ ✖
        * Faça {
        *   SE ( 
        *       dentro do btn.css-1hmr1hq tiver span.css-1l6c7y9 
        *       OU
        *       O conteúdo do btn.css-1hmr1hq for ! de "Realizar") {
        *       pass
        *   } SE NÃO {
        *       Subtraia -1 nas ativadades
        *       Click no btn.css-1hmr1hq
        *   }
        * Enquanto (Atividades > 0)
    }

    ## Inside teste

    Header -> .css-vwhf6n
    Vídeo -> .css-xz389d 
        h6 > .css-qpwa0j
        div iframe > .css-6u0h3m
    Sec_Quest CHECKBOX -> .css-xz389d
        Header -> .css-1v3caum
        Header Points -> .css-nlzma4
        Header Title -> .ql-editor .css-kmkory
        
        Body -> .css-odg2wy
            Alter A Input -> .PrivateSwitchBase-input .css-1m9pwf3 #0
            Alter A Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="0" type="checkbox" data-indeterminate="false">

            Alter B Input -> .PrivateSwitchBase-input .css-1m9pwf3 #1
            Alter B Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="1" type="checkbox" data-indeterminate="false">

            Alter C Input -> .PrivateSwitchBase-input .css-1m9pwf3 #2
            Alter C Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="2" type="checkbox" data-indeterminate="false">

            Alter D Input -> .PrivateSwitchBase-input .css-1m9pwf3 #3
            Alter D Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="3" type="checkbox" data-indeterminate="false">

            Alter E Input -> .PrivateSwitchBase-input .css-1m9pwf3 #4
            Alter E Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="4" type="checkbox" data-indeterminate="false">
        
        Sec_Quest RADIO 1 -> .css-xz389d
        Header -> .css-1v3caum
        Header Points -> .css-nlzma4
        Header Title -> .ql-editor .css-kmkory
        Body -> .css-odg2wy
            Alter A Input -> .PrivateSwitchBase-input .css-1m9pwf3
            Alter A Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="0" type="checkbox" data-indeterminate="false">
            
            Alter B Input -> .PrivateSwitchBase-input .css-1m9pwf3
            Alter B Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="1" type="checkbox" data-indeterminate="false">
            
            Alter C Input -> .PrivateSwitchBase-input .css-1m9pwf3
            Alter C Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="2" type="checkbox" data-indeterminate="false">
            
            Alter D Input -> .PrivateSwitchBase-input .css-1m9pwf3
            Alter D Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="3" type="checkbox" data-indeterminate="false">
            
            Alter E Input -> .PrivateSwitchBase-input .css-1m9pwf3
            Alter E Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="4" type="checkbox" data-indeterminate="false">
        
        Sec_Quest RADIO 2 -> .css-xz389d
        Header -> .css-1v3caum
        Header Points -> .css-nlzma4
        Header Title -> .ql-editor .css-kmkory
        Body -> .css-odg2wy
            Alter A Input -> .PrivateSwitchBase-input .css-1m9pwf3
            Alter A Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="0" type="checkbox" data-indeterminate="false">
            
            Alter B Input -> .PrivateSwitchBase-input .css-1m9pwf3
            Alter B Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="1" type="checkbox" data-indeterminate="false">
            
            Alter C Input -> .PrivateSwitchBase-input .css-1m9pwf3
            Alter C Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="2" type="checkbox" data-indeterminate="false">
            
            Alter D Input -> .PrivateSwitchBase-input .css-1m9pwf3
            Alter D Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="3" type="checkbox" data-indeterminate="false">
            
            Alter E Input -> .PrivateSwitchBase-input .css-1m9pwf3
            Alter E Text -> .ql-editor .MuiBox-root .css-kmkory
            <input class="PrivateSwitchBase-input css-1m9pwf3" id="4" type="checkbox" data-indeterminate="false">

        Sec_Quest TEXTAREA -> .css-xz389d
        Header -> .css-1v3caum
        Header Points -> .css-nlzma4
        Header Title -> .ql-editor .css-kmkory
        Body -> .css-odg2wy
            <form action="" method="post" spellcheck="false" autocorrect="off" autocomplete="off" autocapitalize="none"
                class="css-0" data-gtm-form-interact-id="0"><input type="text" name="hidden" autocorrect="off" spellcheck="false"
                    autocomplete="false" autocapitalize="none" class="css-0" style="display: none;">
                <div class="MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-feqhe6"><label
                        class="MuiFormLabel-root MuiInputLabel-root MuiInputLabel-formControl MuiInputLabel-animated MuiInputLabel-sizeMedium MuiInputLabel-standard MuiFormLabel-colorPrimary MuiInputLabel-root MuiInputLabel-formControl MuiInputLabel-animated MuiInputLabel-sizeMedium MuiInputLabel-standard css-1h1avmt"
                        data-shrink="false" for=":rd:" id=":rd:-label">Resposta</label>
                    <div
                        class="MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-multiline css-1104ogz">
                        <textarea aria-invalid="false" id=":rd:"
                            class="MuiInputBase-input MuiInput-input MuiInputBase-inputMultiline css-13pivat"
                            style="height: 23px; overflow: hidden;" data-lt-tmp-id="lt-888352" spellcheck="false" data-gramm="false"
                            data-gtm-form-interact-field-id="0"></textarea><textarea aria-hidden="true"
                            class="MuiInputBase-input MuiInput-input MuiInputBase-inputMultiline css-13pivat" readonly=""
                            tabindex="-1"
                            style="visibility: hidden; position: absolute; overflow: hidden; height: 0px; top: 0px; left: 0px; transform: translateZ(0px); padding-top: 0px; padding-bottom: 0px; width: 472.094px;"></textarea>
                    </div>
                </div>
            </form>


        ===================== Compare Inputs Type

        <input class="PrivateSwitchBase-input css-1m9pwf3" name=":rl:" type="radio" value="0">
        <input class="PrivateSwitchBase-input css-1m9pwf3" name=":rl:" type="radio" value="4">

        <input class="PrivateSwitchBase-input css-1m9pwf3" id="0" type="checkbox" data-indeterminate="false">
        <input class="PrivateSwitchBase-input css-1m9pwf3" id="4" type="checkbox" data-indeterminate="false">

        ==================== Compare "Nota: 1, Valor: 1"

        <div class="css-nlzma4"><p class="MuiTypography-root MuiTypography-body1 css-1gxf8zg">Obrigatória</p><p class="MuiTypography-root MuiTypography-body1 css-1oxu2ga">Sem resposta</p><div class="MuiBox-root css-1902l77"><div class="css-1eiafge"><h6 class="MuiTypography-root MuiTypography-subtitle2 css-h91zzi">Nota:</h6><h6 class="MuiTypography-root MuiTypography-subtitle2 css-1ycllk9">1</h6></div><div class="css-45i6pv"><h6 class="MuiTypography-root MuiTypography-subtitle2 css-h91zzi">Valor:</h6><h6 class="MuiTypography-root MuiTypography-subtitle2 css-1ycllk9">1</h6></div></div></div>
        <div class="css-nlzma4"><p class="MuiTypography-root MuiTypography-body1 css-1gxf8zg">Obrigatória</p><p class="MuiTypography-root MuiTypography-body1 css-1oxu2ga">Sem resposta</p><div class="MuiBox-root css-1902l77"><div class="css-1eiafge"><h6 class="MuiTypography-root MuiTypography-subtitle2 css-h91zzi">Nota:</h6><h6 class="MuiTypography-root MuiTypography-subtitle2 css-1ycllk9">1</h6></div><div class="css-45i6pv"><h6 class="MuiTypography-root MuiTypography-subtitle2 css-h91zzi">Valor:</h6><h6 class="MuiTypography-root MuiTypography-subtitle2 css-1ycllk9">1</h6></div></div></div>
         
        ==================== Compare "Botão Voltar"
        <button class="MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedInherit MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorInherit MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedInherit MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorInherit css-1n6n6mo" tabindex="0" type="button" id=":rl:"><span class="MuiButton-icon MuiButton-startIcon MuiButton-iconSizeMedium css-1l6c7y9"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-1xpyc8b" focusable="false" aria-hidden="true" viewBox="0 0 24 24" data-testid="ArrowBackIcon"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"></path></svg></span>Voltar<span class="MuiTouchRipple-root css-w0pj6f"></span></button>
        <button class="MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedInherit MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorInherit MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedInherit MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorInherit css-1n6n6mo" tabindex="0" type="button" id=":rl:"><span class="MuiButton-icon MuiButton-startIcon MuiButton-iconSizeMedium css-1l6c7y9"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-1xpyc8b" focusable="false" aria-hidden="true" viewBox="0 0 24 24" data-testid="ArrowBackIcon"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"></path></svg></span>Voltar<span class="MuiTouchRipple-root css-w0pj6f"></span></button>

        ==================== View Table Todo
        <table class="MuiTable-root css-1rb4ifj">
            <thead class="MuiTableHead-root css-1wbz3t9"><tr class="MuiTableRow-root MuiTableRow-head css-wygh5w">
            <tbody class="MuiTableBody-root css-1xnox0e">
                <tr class="MuiTableRow-root css-wygh5w">
                    <td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-1apkbt2">
                        <button class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall css-k9aczr" tabindex="0" type="button"></button>
                    </td>
                </tr>
            </tbody>
        </table>

"""
