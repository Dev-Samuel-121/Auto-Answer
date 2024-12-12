# Header ◯ <!-- ************************ -->
    div.css-wlaq1z			                                        -> Header (Cabeçalho da página, nome, ra, etc) <br>
    div.css-xz389d			                                        -> Section de cada questão (Div para separar as questões em meio que sections) <br>
    iframe.css-dej042		                                        -> Vídeo (Classe do iframe, para vídeo) <br>

<br>

# Checkbox ▣ <!-- ************************ -->
div.css-xz389d                                                  -> Section da questão
    div.css-1v3caum                                             -> Header da questão (Título, nota, etc)
        div.css-nlzma4                                          -> Conteúdo do Header da questão (Aparece apenas em questões)
            div.css-11tg5ks                                     -> Área nota da questão e valor obtido (Aparece apenas em questões)
                h6.css-h91zzi                                   -> Título "Nota"
                h6.css-1ycllk9                                  -> Valor "Nota"
            div.css-45i6pv                                      -> Área Valor obtido da questão (Aparece apenas em questões)
                h6.css-h91zzi                                   -> Título "Valor"
                h6.css-1ycllk9                                  -> Valor "Valor"
    div.css-odg2wy                                              -> Aréa Alternativas (A, B, C, D, E)
        div.css-t1yck                                           -> Linha da alternativa
            span.MuiCheckbox-root.css-14bgux8                   -> Span para Checkbox (Podemos ver isso pela classe MuiCheckbox-root)
                input.PrivateSwitchBase-input.css-1m9pwf3       -> Inputs (Todo os inputs tem as mesmas classes)
                div.css-kmkory                                  -> Questão (Título da questão [A. O polo pode ser norte ou sul...]. Se repete para todos os títulos de questões, alternativas e sections)
    div.css-5fvs8v                                              -> Área do botão para veririficar questão (Aparece apenas em questões)
        button.css-1vp0eyt                                      -> Botão para veririficar resposta (Aparece apenas em questões)
    div.css-k97gqx                                              -> Área que a resposta da questõa está ERRADA
        div.css-rjvjdk                                          -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                       -> Texto motivacional
            span.css-1dihf0q                                    -> Número de verificações possíveis
    div.css-12jrsk0                                             -> Área que a resposta da questõa está CERTA
        div.css-rjvjdk                                          -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                       -> Texto motivacional
            span.css-1dihf0q                                    -> Número de verificações possíveis
    div.css-nsnxaz                                              -> Área que a resposta da questõa está CERTA
        div.css-rjvjdk                                          -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                       -> Texto de acabou suas tentativas
    span.css-sgwfsg                                             -> Título de "Resolução" da questão
        div.css-1ol0y3d                                         -> Área do texto da resolução da questão
            p.ql-align-justify                                  -> Paragraph para o texto da resolução (A classe .ql-align-justify aparece como TÍTULO DAS QUESTÕES.)

<br>

> ## Note:<br>
> Um ponto bom a se notar é que os inputs do tipo *Checkbox* tem *IDs* igual a um número, creio que isso seja para o servidor receber a alternativo com base no seu *ID*.<br><br>
> Vou dar mais uma verificada em outras atividades que tenham mais de uma *Section* de pergunta do tipo *Checkbox* para ver se esses *IDs* se repetem ou mudam <u>aumentando</u> ou <u>diminuindo</u> seu valor

<br>
<hr>
<br>

# Radios ◉ <!-- ************************ -->
div.css-xz389d                                                          -> Section da questão
    div.css-1v3caum                                                     -> Header da questão (Título, nota, etc)
        div.css-nlzma4                                                  -> Conteúdo do Header da questão (Aparece apenas em questões)
            div.css-11tg5ks                                             -> Área nota da questão e valor obtido (Aparece apenas em questões)
                h6.css-h91zzi                                           -> Título "Nota"
                h6.css-1ycllk9                                          -> Valor "Nota"
            div.css-45i6pv                                              -> Área Valor obtido da questão (Aparece apenas em questões)
                h6.css-h91zzi                                           -> Título "Valor"
                h6.css-1ycllk9                                          -> Valor "Valor"
    div.css-odg2wy                                                      -> Aréa Alternativas (A, B, C, D, E)
        div.css-1h7anqn                                                 -> Div de agrupamentoda as alternativas
            div.css-t1yck                                               -> Linha da alternativa
                label.MuiFormControlLabel-root.css-1jaw3da              -> Label para o Radio
                    span.MuiRadio-root.css-1sgsc5r                      -> span para Radio (Podemos ver isso pela classe MuiRadio-root)
                        input.PrivateSwitchBase-input.css-1m9pwf3       -> Inputs (Todo os inputs tem as mesmas classes)
                        div.css-kmkory                                  -> Questão (Título da questão [A. O polo pode ser norte ou sul...]. Se repete para todos os títulos de questões, alternativas e sections)
    div.css-5fvs8v                                                      -> Área do botão para veririficar questão (Aparece apenas em questões)
        button.css-1vp0eyt                                              -> Botão para veririficar resposta (Aparece apenas em questões)
    div.css-k97gqx                                                      -> Área que a resposta da questõa está ERRADA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto motivacional
            span.css-1dihf0q                                            -> Número de verificações possíveis
    div.css-12jrsk0                                                     -> Área que a resposta da questõa está CERTA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto motivacional
            span.css-1dihf0q                                            -> Número de verificações possíveis
    div.css-nsnxaz                                                      -> Área que a resposta da questõa está CERTA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto de acabou suas tentativas
    span.css-sgwfsg                                                     -> Título de "Resolução" da questão
        div.css-1ol0y3d                                                 -> Área do texto da resolução da questão
            p.ql-align-justify                                          -> Paragraph para o texto da resolução (A classe .ql-align-justify aparece como TÍTULO DAS QUESTÕES.)

<br>

> ## Note:<br>
> Um ponto bom a se notar é que os inputs do tipo *Radio* recebem *Values* igual a um número, creio que isso seja para o servidor receber a alternativo com base no seu *Value*.<br><br>
> Vou dar mais uma verificada em outras atividades que tenham mais de uma *Section* de pergunta do tipo *Radio* para ver se esses *Values* se repetem ou mudam <u>aumentando</u> ou <u>diminuindo</u> seu valor

<br>
<hr>
<br>

# Radios - Right Wrong ◉ ◎ <!-- ************************ -->
div.css-xz389d                                                                                              -> Section da questão
    div.css-1v3caum                                                                                         -> Header da questão (Título, nota, etc)
        div.css-nlzma4                                                                                      -> Conteúdo do Header da questão (Aparece apenas em questões)
            div.css-11tg5ks                                                                                 -> Área nota da questão e valor obtido (Aparece apenas em questões)
                h6.css-h91zzi                                                                               -> Título "Nota"
                h6.css-1ycllk9                                                                              -> Valor "Nota"
            div.css-45i6pv                                                                                  -> Área Valor obtido da questão (Aparece apenas em questões)
                h6.css-h91zzi                                                                               -> Título "Valor"
                h6.css-1ycllk9                                                                              -> Valor "Valor"
    div.css-odg2wy                                                                                          -> Aréa Alternativas (A, B, C, D, E)
        div.css-j7qwjs                                                                                      -> Div de agrupamentoda da questão e botões
            p                                                                                               -> Paragraph com o texto da alternativa
        div.MuiRadioGroup-row.css-1sv5mar                                                                   -> Div de agrupamento dos botões
            label.MuiFormControlLabel-labelPlacementEnd.css-1jaw3da                                         -> Label para separar Btn do Texto
                span.MuiRadio-root.css-1dgpfwv                                                              -> Span para Input
                    input.PrivateSwitchBase-input.css-1m9pwf3(value="true")                                 -> Input do botão com value igual a True
                    span.css-hyxlzm                                                                         -> Span para SVG
                        svg.MuiSvgIcon-fontSizeSmall.css-cpa9t9(data-testid="RadioButtonUncheckedIcon")     -> Svg para botão não precionado
                        svg.MuiSvgIcon-fontSizeSmall.css-1exsolk(data-testid="RadioButtonCheckedIcon")      -> Svg para botão com icon check
                    span.MuiFormControlLabel-label.css-1tnm47n                                              -> Span para texto do botão (Certo)
            label.MuiFormControlLabel-labelPlacementEnd.css-1jaw3da                                         -> Label para separar Btn do Texto
                span.MuiRadio-root.css-1dgpfwv                                                              -> Span para Input
                    input.PrivateSwitchBase-input.css-1m9pwf3(value="false")                                -> Input do botão com value igual a False
                    span.css-hyxlzm                                                                         -> Span para SVG
                        svg.MuiSvgIcon-fontSizeSmall.css-cpa9t9(data-testid="RadioButtonUncheckedIcon")     -> Svg para botão não precionado
                        svg.MuiSvgIcon-fontSizeSmall.css-1exsolk(data-testid="RadioButtonCheckedIcon")      -> Svg para botão com icon check
                    span.MuiFormControlLabel-label css-1tnm47n                                              -> Span para texto do botão (Certo)
    div.css-5fvs8v                                                                                          -> Área do botão para veririficar questão (Aparece apenas em questões)
        button.css-1vp0eyt                                                                                  -> Botão para veririficar resposta (Aparece apenas em questões)
    div.css-k97gqx                                                                                          -> Área que a resposta da questõa está ERRADA
        div.css-rjvjdk                                                                                      -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                                                                   -> Texto motivacional
            span.css-1dihf0q                                                                                -> Número de verificações possíveis
    div.css-12jrsk0                                                                                         -> Área que a resposta da questõa está CERTA
        div.css-rjvjdk                                                                                      -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                                                                   -> Texto motivacional
            span.css-1dihf0q                                                                                -> Número de verificações possíveis
    <!-- * COLOCAR PARTE ONDE ACABOU SUAS TENTATIVAS -->
    <!-- * div.css-12jrsk0                                                                                  -> Área que a resposta da questõa está CERTA -->
    <!-- *     div.css-rjvjdk                                                                               -> Áre para o texto de motivamação e Número de verificações disponiveis -->
    <!-- *         p.css-1dihf0q                                                                            -> Texto motivacional -->
    <!-- *         span.css-1dihf0q                                                                         -> Número de verificações possíveis -->
    span.css-sgwfsg                                                                                         -> Título de "Resolução" da questão
        div.css-1ol0y3d                                                                                     -> Área do texto da resolução da questão
            p.ql-align-justify                                                                              -> Paragraph para o texto da resolução (A classe .ql-align-justify aparece como TÍTULO DAS QUESTÕES.)

<br>

> ## Note:<br>
> Um ponto bom a se notar é que os inputs do tipo *Radio* recebem *Values* igual a um número, creio que isso seja para o servidor receber a alternativo com base no seu *Value*.<br><br>
> Vou dar mais uma verificada em outras atividades que tenham mais de uma *Section* de pergunta do tipo *Radio* para ver se esses *Values* se repetem ou mudam <u>aumentando</u> ou <u>diminuindo</u> seu valor

<br>
<hr>
<br>

# Order ▥ <!-- !!!!!!!!!!!!!!!!!!!!!!!! -->
div.css-xz389d                                                          -> Section da questão
    div.css-1v3caum                                                     -> Header da questão (Título, nota, etc)
        div.css-nlzma4                                                  -> Conteúdo do Header da questão (Aparece apenas em questões)
            div.css-11tg5ks                                             -> Área nota da questão e valor obtido (Aparece apenas em questões)
                h6.css-h91zzi                                           -> Título "Nota"
                h6.css-1ycllk9                                          -> Valor "Nota"
            div.css-45i6pv                                              -> Área Valor obtido da questão (Aparece apenas em questões)
                h6.css-h91zzi                                           -> Título "Valor"
                h6.css-1ycllk9                                          -> Valor "Valor"
    div.css-odg2wy                                                      -> Aréa Alternativas (A, B, C, D, E)
        div.css-1h7anqn                                                 -> Div de agrupamentoda as alternativas
            div.css-t1yck                                               -> Linha da alternativa
                label.MuiFormControlLabel-root.css-1jaw3da              -> Label para o Radio
                    span.MuiRadio-root.css-1sgsc5r                      -> span para Radio (Podemos ver isso pela classe MuiRadio-root)
                        input.PrivateSwitchBase-input.css-1m9pwf3       -> Inputs (Todo os inputs tem as mesmas classes)
                        div.css-kmkory                                  -> Questão (Título da questão [A. O polo pode ser norte ou sul...]. Se repete para todos os títulos de questões, alternativas e sections)
    div.css-5fvs8v                                                      -> Área do botão para veririficar questão (Aparece apenas em questões)
        button.css-1vp0eyt                                              -> Botão para veririficar resposta (Aparece apenas em questões)
    div.css-k97gqx                                                      -> Área que a resposta da questõa está ERRADA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto motivacional
            span.css-1dihf0q                                            -> Número de verificações possíveis
    div.css-12jrsk0                                                     -> Área que a resposta da questõa está CERTA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto motivacional
            span.css-1dihf0q                                            -> Número de verificações possíveis
    <!-- * COLOCAR PARTE ONDE ACABOU SUAS TENTATIVAS -->
    <!-- * div.css-12jrsk0                                              -> Área que a resposta da questõa está CERTA -->
    <!-- *     div.css-rjvjdk                                           -> Áre para o texto de motivamação e Número de verificações disponiveis -->
    <!-- *         p.css-1dihf0q                                        -> Texto motivacional -->
    <!-- *         span.css-1dihf0q                                     -> Número de verificações possíveis -->
    span.css-sgwfsg                                                     -> Título de "Resolução" da questão
        div.css-1ol0y3d                                                 -> Área do texto da resolução da questão
            p.ql-align-justify                                          -> Paragraph para o texto da resolução (A classe .ql-align-justify aparece como TÍTULO DAS QUESTÕES.)

<br>

> ## Note:<br>
> Um ponto bom a se notar é que os inputs do tipo *Radio* recebem *Values* igual a um número, creio que isso seja para o servidor receber a alternativo com base no seu *Value*.<br><br>
> Vou dar mais uma verificada em outras atividades que tenham mais de uma *Section* de pergunta do tipo *Radio* para ver se esses *Values* se repetem ou mudam <u>aumentando</u> ou <u>diminuindo</u> seu valor

<br>
<hr>
<br>


# Select ▤ <!-- !!!!!!!!!!!!!!!!!!!!!!!! -->
div.css-xz389d                                                          -> Section da questão
    div.css-1v3caum                                                     -> Header da questão (Título, nota, etc)
        div.css-nlzma4                                                  -> Conteúdo do Header da questão (Aparece apenas em questões)
            div.css-11tg5ks                                             -> Área nota da questão e valor obtido (Aparece apenas em questões)
                h6.css-h91zzi                                           -> Título "Nota"
                h6.css-1ycllk9                                          -> Valor "Nota"
            div.css-45i6pv                                              -> Área Valor obtido da questão (Aparece apenas em questões)
                h6.css-h91zzi                                           -> Título "Valor"
                h6.css-1ycllk9                                          -> Valor "Valor"
    div.css-odg2wy                                                      -> Aréa Alternativas (A, B, C, D, E)
        div.css-1h7anqn                                                 -> Div de agrupamentoda as alternativas
            div.css-t1yck                                               -> Linha da alternativa
                label.MuiFormControlLabel-root.css-1jaw3da              -> Label para o Radio
                    span.MuiRadio-root.css-1sgsc5r                      -> span para Radio (Podemos ver isso pela classe MuiRadio-root)
                        input.PrivateSwitchBase-input.css-1m9pwf3       -> Inputs (Todo os inputs tem as mesmas classes)
                        div.css-kmkory                                  -> Questão (Título da questão [A. O polo pode ser norte ou sul...]. Se repete para todos os títulos de questões, alternativas e sections)
    div.css-5fvs8v                                                      -> Área do botão para veririficar questão (Aparece apenas em questões)
        button.css-1vp0eyt                                              -> Botão para veririficar resposta (Aparece apenas em questões)
    div.css-k97gqx                                                      -> Área que a resposta da questõa está ERRADA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto motivacional
            span.css-1dihf0q                                            -> Número de verificações possíveis
    div.css-12jrsk0                                                     -> Área que a resposta da questõa está CERTA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto motivacional
            span.css-1dihf0q                                            -> Número de verificações possíveis
    <!-- * COLOCAR PARTE ONDE ACABOU SUAS TENTATIVAS -->
    <!-- * div.css-12jrsk0                                              -> Área que a resposta da questõa está CERTA -->
    <!-- *     div.css-rjvjdk                                           -> Áre para o texto de motivamação e Número de verificações disponiveis -->
    <!-- *         p.css-1dihf0q                                        -> Texto motivacional -->
    <!-- *         span.css-1dihf0q                                     -> Número de verificações possíveis -->
    span.css-sgwfsg                                                     -> Título de "Resolução" da questão
        div.css-1ol0y3d                                                 -> Área do texto da resolução da questão
            p.ql-align-justify                                          -> Paragraph para o texto da resolução (A classe .ql-align-justify aparece como TÍTULO DAS QUESTÕES.)

<br>

> ## Note:<br>
> Um ponto bom a se notar é que os inputs do tipo *Radio* recebem *Values* igual a um número, creio que isso seja para o servidor receber a alternativo com base no seu *Value*.<br><br>
> Vou dar mais uma verificada em outras atividades que tenham mais de uma *Section* de pergunta do tipo *Radio* para ver se esses *Values* se repetem ou mudam <u>aumentando</u> ou <u>diminuindo</u> seu valor

<br>
<hr>
<br>

# Textarea ʈ <!-- !!!!!!!!!!!!!!!!!!!!!!!! -->
div.css-xz389d                                                          -> Section da questão
    div.css-1v3caum                                                     -> Header da questão (Título, nota, etc)
        div.css-nlzma4                                                  -> Conteúdo do Header da questão (Aparece apenas em questões)
            div.css-11tg5ks                                             -> Área nota da questão e valor obtido (Aparece apenas em questões)
                h6.css-h91zzi                                           -> Título "Nota"
                h6.css-1ycllk9                                          -> Valor "Nota"
            div.css-45i6pv                                              -> Área Valor obtido da questão (Aparece apenas em questões)
                h6.css-h91zzi                                           -> Título "Valor"
                h6.css-1ycllk9                                          -> Valor "Valor"
    div.css-odg2wy                                                      -> Aréa Alternativas (A, B, C, D, E)
        div.css-1h7anqn                                                 -> Div de agrupamentoda as alternativas
            div.css-t1yck                                               -> Linha da alternativa
                label.MuiFormControlLabel-root.css-1jaw3da              -> Label para o Radio
                    span.MuiRadio-root.css-1sgsc5r                      -> span para Radio (Podemos ver isso pela classe MuiRadio-root)
                        input.PrivateSwitchBase-input.css-1m9pwf3       -> Inputs (Todo os inputs tem as mesmas classes)
                        div.css-kmkory                                  -> Questão (Título da questão [A. O polo pode ser norte ou sul...]. Se repete para todos os títulos de questões, alternativas e sections)
    div.css-5fvs8v                                                      -> Área do botão para veririficar questão (Aparece apenas em questões)
        button.css-1vp0eyt                                              -> Botão para veririficar resposta (Aparece apenas em questões)
    div.css-k97gqx                                                      -> Área que a resposta da questõa está ERRADA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto motivacional
            span.css-1dihf0q                                            -> Número de verificações possíveis
    div.css-12jrsk0                                                     -> Área que a resposta da questõa está CERTA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto motivacional
            span.css-1dihf0q                                            -> Número de verificações possíveis
    <!-- * COLOCAR PARTE ONDE ACABOU SUAS TENTATIVAS -->
    <!-- * div.css-12jrsk0                                              -> Área que a resposta da questõa está CERTA -->
    <!-- *     div.css-rjvjdk                                           -> Áre para o texto de motivamação e Número de verificações disponiveis -->
    <!-- *         p.css-1dihf0q                                        -> Texto motivacional -->
    <!-- *         span.css-1dihf0q                                     -> Número de verificações possíveis -->
    span.css-sgwfsg                                                     -> Título de "Resolução" da questão
        div.css-1ol0y3d                                                 -> Área do texto da resolução da questão
            p.ql-align-justify                                          -> Paragraph para o texto da resolução (A classe .ql-align-justify aparece como TÍTULO DAS QUESTÕES.)

<br>

> ## Note:<br>
> Um ponto bom a se notar é que os inputs do tipo *Radio* recebem *Values* igual a um número, creio que isso seja para o servidor receber a alternativo com base no seu *Value*.<br><br>
> Vou dar mais uma verificada em outras atividades que tenham mais de uma *Section* de pergunta do tipo *Radio* para ver se esses *Values* se repetem ou mudam <u>aumentando</u> ou <u>diminuindo</u> seu valor

<br>
<hr>
<br>

# Draggable ⇅ <!-- ************************ -->
div.css-xz389d                                                                                                          -> Section da questão
    div.css-1v3caum                                                                                                     -> Header da questão (Título, nota, etc)
        div.css-nlzma4                                                                                                  -> Conteúdo do Header da questão (Aparece apenas em questões)
            div.css-11tg5ks                                                                                             -> Área nota da questão e valor obtido (Aparece apenas em questões)
                h6.css-h91zzi                                                                                           -> Título "Nota"
                h6.css-1ycllk9                                                                                          -> Valor "Nota"
            div.css-45i6pv                                                                                              -> Área Valor obtido da questão (Aparece apenas em questões)
                h6.css-h91zzi                                                                                           -> Título "Valor"
                h6.css-1ycllk9                                                                                          -> Valor "Valor"
    div.css-odg2wy                                                                                                      -> Aréa Alternativas (A, B, C, D, E)
        div.MuiGrid-root.css-2csr8t                                                                                     -> Div de agrupamentoda do Draggable
            div.MuiGrid-item.css-1ouk5di                                                                                -> Div item do Draggable
                h6.MuiTypography-subtitle1.css-rsavpr                                                                   -> Subtítulo da questão "Ordene as frases abaixo"
                div#2BkaUihp.css-4rmlxi                                                                                 -> Div de agrupamento das alternativas a serem movidas ()
                    div.css-z0sbrd(data-content="{index:0,id:xxmpuVdv,areaId:2BkaUihp,type:draggable}")                 -> Item draggable, div.css-z0sbrd é a div do item onde tem o botão e o conteúdo
                        div.MuiCard-root.css-mt2pr9                                                                     -> Card do conteúdo
                            div.MuiBox-root.css-16izr03                                                                 -> Conteúdo propriamente dito
                                svg.MuiSvgIcon-root.MuiSvgIcon-fontSizeMedium.css-taiaz                                 -> Incone de puxar para alterar sua ordem
                                h6.MuiTypography-subtitle1.css-rckqyx                                                   -> Texto do card
                                div.MuiBox-root.css-1u57xu6                                                             -> Div de agrupamento dos botões para subir ou descer o item
                                    span.MuiIconButton-sizeMedium.css-2wyiu                                             -> Span para guardar o SVG
                                        svg.MuiSvgIcon-fontSizeMedium.css-1in44b7(data-testid="ArrowCircleUpIcon")      -> svg.MuiSvgIcon-fontSizeMedium.css-1in44b7 é o Svg do botão. O que define se ele é de ir para cima ou para baixo é o seu data-testid="ArrowCircleDIREÇÃOIcon"
                                        svg.MuiSvgIcon-fontSizeMedium.css-1in44b7(data-testid="ArrowCircleDownIcon")    -> svg.MuiSvgIcon-fontSizeMedium.css-1in44b7 é o Svg do botão. O que define se ele é de ir para cima ou para baixo é o seu data-testid="ArrowCircleDIREÇÃOIcon"
    div.css-5fvs8v                                                      -> Área do botão para veririficar questão (Aparece apenas em questões)
        button.css-1vp0eyt                                              -> Botão para veririficar resposta (Aparece apenas em questões)
    div.css-k97gqx                                                      -> Área que a resposta da questõa está ERRADA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto motivacional
            span.css-1dihf0q                                            -> Número de verificações possíveis
    div.css-12jrsk0                                                     -> Área que a resposta da questõa está CERTA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto motivacional
            span.css-1dihf0q                                            -> Número de verificações possíveis
    div.css-nsnxaz                                                      -> Área que a resposta da questõa está CERTA
        div.css-rjvjdk                                                  -> Áre para o texto de motivamação e Número de verificações disponiveis
            p.css-1dihf0q                                               -> Texto de acabou suas tentativas
    span.css-sgwfsg                                                     -> Título de "Resolução" da questão
        div.css-1ol0y3d                                                 -> Área do texto da resolução da questão
            p.ql-align-justify                                          -> Paragraph para o texto da resolução (A classe .ql-align-justify aparece como TÍTULO DAS QUESTÕES.)

<br>

> ## Note:<br>
> Um ponto bom a se notar é que os inputs do tipo *Radio* recebem *Values* igual a um número, creio que isso seja para o servidor receber a alternativo com base no seu *Value*.<br><br>
> Vou dar mais uma verificada em outras atividades que tenham mais de uma *Section* de pergunta do tipo *Radio* para ver se esses *Values* se repetem ou mudam <u>aumentando</u> ou <u>diminuindo</u> seu valor
> Referenciação ao ID

<br>
<hr>
<br>


# Mensage <!-- ???????????????????????? -->

<!-- 

    Lógica de Andamento
    1. Drag Drop

    Identificar Inputs
    2. Identificar a qeustão correta é peagar a classe que se repete em todos os inputs e calcular, supondo que tem 20 input.classe_input e cada questão é de A a E e estamos na questão 2 então o nosso raio de questões será apartir do  6 ao 10.
    3. Identificar o :nth-match('Lógica para ser mais especifico possível sobre qual elemento estamos falando', $Número dele com base na sua especificidade)


 -->