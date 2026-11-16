# ATIVIDADE 3 / PYTHON

* **Curso:** Curso Técnico em Informática
* **Turma:** 3º A TEC
* **Disciplina:** Linguagem de Programação
* **Professora:** Kamilla

---

## 01. Plataforma de Rastreamento de Satélites Militares (EXEMPLO RESOLVIDO / MODELO COMPLETO)

**Enunciado (12 Entradas):** Nome do Satélite, Sigla da Agência, Operador Responsável, Cidade da Estação Terrena, Código de Telemetria, Chave Criptográfica, Frequência em MHz, Altitude Orbital, Data do Apogeu (`DD-MM-AAAA`), E-mail da Defesa, Senha de Acesso ao Transponder, Autorização de Órbita (`CONFIRMADO`).[cite: 2]

**Regras:**
* Operador e Cidade devem ser formatados com `.title()` e conter apenas letras (`.isalpha()`).[cite: 2]
* Nome do Satélite e Sigla devem estar em maiúsculas (`.upper()`).[cite: 2]
* Código de Telemetria e Chave devem ser alfanuméricos (`.isalnum()`) e a chave deve iniciar com `"SAT-"` (`.startswith()`).[cite: 2]
* Frequência e Altitude devem ser dígitos (`.isdigit()`).[cite: 2]
* A Data deve ter traços substituídos por barras com `.replace("-", "/")`, conter 2 barras (`.count("/")`) e 10 caracteres (`len()`).[cite: 2]
* E-mail deve terminar com `".defesa.mil.br"` (`.endswith()`).[cite: 2]
* A Senha deve ter no mínimo 8 dígitos com máscara `"*" * len(senha)`.[cite: 2]
* A Autorização deve ser `"CONFIRMADO"` dentro de laço com `range(5)`.[cite: 2]

### Código de Referência em Python (Gabarito Completo com Todas as Funções)

```python
print("--- SISTEMA DE RASTREAMENTO DE SATÉLITES ---")

for tentativa in range(5):
    # 1. ENTRADA E TRATAMENTO DOS DADOS
    satelite = input("Nome do Satélite: ").strip().upper()
    agencia = input("Sigla da Agência: ").strip().upper()
    operador = input("Operador Responsável: ").strip().title()
    cidade = input("Cidade da Estação: ").strip().title()
    telemetria = input("Código de Telemetria: ").strip()
    chave = input("Chave Criptográfica (Ex: SAT-99): ").strip()
    freq = input("Frequência em MHz: ").strip()
    altitude = input("Altitude Orbital: ").strip()
    data = input("Data do Apogeu (DD-MM-AAAA): ").strip()
    email = input("E-mail da Defesa: ").strip().lower()
    senha = input("Senha de Acesso (Mínimo 8 dígitos): ").strip()
    autorizacao = input("Autorização de órbita (CONFIRMADO): ").strip().upper()

    # 2. TRATAMENTO DA DATA COM .replace()
    data_formatada = data.replace("-", "/")

    # 3. VALIDAÇÃO DIRETA COM IF + AND + QUEBRA DE LINHA (\)
    if operador.isalpha() and \
       cidade.isalpha() and \
       telemetria.isalnum() and \
       chave.isalnum() and \
       chave.startswith("SAT-") and \
       freq.isdigit() and \
       altitude.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".defesa.mil.br") and \
       len(senha) >= 8 and \
       autorizacao == "CONFIRMADO":

        # 4. MÁSCARA DE PROTEÇÃO DE SENHA
        senha_oculta = "*" * len(senha)
        print(f"\nSUCESSO: Satélite {satelite} ({agencia}) rastreado por {operador} em {cidade}!")
        print(f"Data Padronizada: {data_formatada} | Senha Protegida: {senha_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas. Notifique o Comando Espacial.")
```

### Legenda Técnica: O que cada função e símbolo faz neste código?

| Função / Símbolo | Apelido | Função no Código |
| :--- | :--- | :--- |
| `1. .strip()` | **"O FAXINEIRO"** | Remove espaços em branco acidentais antes e depois do texto digitado.[cite: 2] |
| `2. .upper()` | **"O GRITADOR"** | Transforma todo o texto em MAIÚSCULO para padronização e comparações seguras.[cite: 2] |
| `3. .lower()` | **"O COCHICHADOR"** | Transforma todo o texto em minúsculo (ideal para e-mails e domínios).[cite: 2] |
| `4. .title()` | **"O CAPITALIZADOR"** | Coloca a primeira letra de cada palavra em MAIÚSCULA (nomes de pessoas e cidades).[cite: 2] |
| `5. .replace()` | **"O SUBSTITUTO"** | Substitui caracteres no texto (ex: troca traços `'-'` por barras `'/'`).[cite: 2] |
| `6. .startswith()` | **"O VIGIA DO INÍCIO"** | Verifica se o texto começa exatamente com um prefixo obrigatório (ex: `"SAT-"`).[cite: 2] |
| `7. .endswith()` | **"O PORTEIRO"** | Verifica se o final do texto termina com a extensão/domínio exigido (ex: `".gov.br"`).[cite: 2] |
| `8. .count()` | **"O CONTADOR"** | Conta quantas vezes um símbolo aparece no texto (ex: se uma data tem 2 barras).[cite: 2] |
| `9. .isalnum()` | **"O MISTURADOR"** | Garante que o campo contenha somente letras e/ou números (sem símbolos ou espaços).[cite: 2] |
| `10. .isdigit()` | **"O FILTRO NUMÉRICO"** | Garante que o campo contenha estritamente dígitos numéricos (`0` a `9`).[cite: 2] |
| `11. .isalpha()` | **"O FILTRO DE TEXTO"** | Garante que o campo contenha exclusivamente letras do alfabeto.[cite: 2] |
| `12. len()` | **"A RÉGUA"** | Mede e valida a quantidade exata ou mínima de caracteres digitados.[cite: 2] |
| `13. "*" * len(s)` | **"O MASCARADOR"** | Multiplica asteriscos pelo tamanho real da senha para ocultá-la no terminal.[cite: 2] |
| `14. \` (Barra) | **"A PONTE"** | Permite quebrar a instrução `if` em várias linhas mantendo o código limpo.[cite: 2] |
| `15. (t + 1)` | **"O TRADUTOR"** | Ajusta o índice do `range` (`0` a `4`) para a contagem humana de `1` a `5` tentativas.[cite: 2] |

---

## Exercícios Propostos (02 a 20)

### 02. Sistema Central de Compensação Bancária (PIX e TED)
* **Enunciado (12 Entradas):** Nome do Titular, Sobrenome, Cidade de Domicílio, Banco Emissor, Chave PIX Alfanumérica, Código de Transação, Valor Transferido em Centavos, Número da Agência, Data da Compensação (`DD-MM-AAAA`), E-mail do Cliente, Token de Segurança, Parecer Bancário (`LIQUIDADO`).[cite: 3]
* **Regras:** Nome, Sobrenome e Cidade com `.title()` e validação `.isalpha()`. Banco Emissor em maiúsculas (`.upper()`). Chave PIX e Código de Transação devem ser alfanuméricos (`.isalnum()`), com o Código iniciando em `"TX-"` (`.startswith()`). Valor e Agência devem ser estritamente números (`.isdigit()`). Data ajustada com `.replace()` contendo exatamente 2 barras (`.count()`) e 10 caracteres (`len()`). E-mail deve estar em minúsculas (`.lower()`) terminando com `".banco.com.br"` (`.endswith()`). Token mascarado com `"*" * len(token)` e Parecer validado como `"LIQUIDADO"` em 5 tentativas (`range(5)`).[cite: 3]

### 03. Prontuário Eletrônico e Central de Transplantes de Órgãos
* **Enunciado (12 Entradas):** Nome do Paciente Receptor, Tipo do Órgão, Hospital de Origem, Médico Cirurgião, Código do Protocolo, CRM do Médico, Temperatura do Recipiente, Batimentos Cardíacos, Data do Procedimento (`DD-MM-AAAA`), E-mail do SUS, Senha de Abertura do Lacre, Parecer Médico (`COMPATIVEL`).[cite: 3]
* **Regras:** Paciente, Tipo do Órgão e Cirurgião formatados com `.title()` e checados com `.isalpha()`. Hospital em maiúsculas (`.upper()`). Protocolo deve iniciar com `"MED-"` (`.startswith()`) e CRM deve ser alfanumérico (`.isalnum()`) com 6 caracteres (`len()`). Temperatura e Batimentos apenas números (`.isdigit()`). Data tratada com `.replace("-", "/")` e conferida com `.count("/")`. E-mail terminando em `".saude.gov.br"` (`.endswith()`). Senha oculta via máscara `"*" * len(senha)` e Parecer `"COMPATIVEL"` em laço de até 5 tentativas (`range(5)`).[cite: 3]

### 04. Supervisório de Usina Termelétrica e Turbinas a Gás
* **Enunciado (12 Entradas):** Nome do Engenheiro Chefe, Setor Operacional, Nome da Usina, Cidade da Instalação, Código do Reator, Tag da Turbina, Pressão do Vapor, Rotações por Minuto, Data da Verificação (`DD-MM-AAAA`), E-mail da Concessionária, Chave de Bypass, Status da Caldeira (`NORMAL`).[cite: 3]
* **Regras:** Engenheiro, Setor e Cidade com `.title()` e `.isalpha()`. Usina em maiúsculas (`.upper()`). Código do Reator iniciando com `"TURB-"` (`.startswith()`) e Tag alfanumérica (`.isalnum()`). Pressão e RPM exclusivamente numéricos (`.isdigit()`). Data padronizada com `.replace()` e `.count("/") == 2`. E-mail finalizando com `".energia.ind.br"` (`.endswith()`). Chave protegida com `"*" * len(chave)` e Status `"NORMAL"` validado em até 5 tentativas com `range(5)`.[cite: 3]

### 05. Controle de Imigração e Passaportes em Aeroporto Internacional
* **Enunciado (12 Entradas):** Nome do Passageiro, Sobrenome, País de Origem, Cidade de Destino, Número do Passaporte, Código do Voo, Quantidade de Bagagens, Tempo de Estadia em Dias, Data de Entrada (`DD-MM-AAAA`), E-mail da Companhia Aérea, Código de Visto, Entrada no País (`AUTORIZADO`).[cite: 3]
* **Regras:** Passageiro, Sobrenome, País e Cidade formatados com `.title()` e `.isalpha()`. Código do Voo iniciando com `"FLIGHT-"` (`.startswith()`) e Passaporte alfanumérico (`.isalnum()`) com 8 caracteres (`len()`). Bagagens e Dias contendo apenas números (`.isdigit()`). Data ajustada com `.replace()` com 2 barras (`.count("/")`). E-mail institucional terminando com `".air.com"` (`.endswith()`). Visto ocultado no terminal com `"*" * len(visto)` e Entrada `"AUTORIZADO"` checada em laço de 5 tentativas (`range(5)`).[cite: 3]

### 06. Gestão de Cargas e Tráfego Ferroviário de Minérios
* **Enunciado (12 Entradas):** Nome do Maquinista, Terminal de Partida, Terminal de Chegada, Tipo de Minério, Código do Vagão, Número do Trem, Peso em Toneladas, Quilômetros a Percorrer, Data da Viagem (`DD-MM-AAAA`), E-mail da Ferrovia, Chave do Bloqueio de Freio, Sinalização da Linha (`VERDE`).[cite: 3]
* **Regras:** Maquinista, Terminais e Tipo de Minério com `.title()` e `.isalpha()`. Código do Vagão iniciando com `"CARGA-"` (`.startswith()`) e Número do Trem alfanumérico (`.isalnum()`). Peso e Quilômetros compostos por dígitos (`.isdigit()`). Data corrigida com `.replace("-", "/")`, conferindo 2 barras (`.count()`) e 10 caracteres (`len()`). E-mail terminando em `".ferrovia.log.br"` (`.endswith()`). Chave protegida com `"*" * len(chave)` e Sinalização `"VERDE"` validada em até 5 repetições (`range(5)`).[cite: 3]

### 07. Auditoria Forense Digital e Custódia de Evidências (SOC)
* **Enunciado (12 Entradas):** Nome do Perito, Especialidade Forense, Departamento Policial, Cidade da Ocorrência, Código da Evidência, Hash SHA-256 da Imagem, Tamanho em Megabytes, Número do Lacre, Data da Apreensão (`DD-MM-AAAA`), E-mail do Instituto de Perícia, Senha do Cofre Digital, Parecer Forense (`INTEGRO`).[cite: 3]
* **Regras:** Perito, Especialidade e Cidade formatados com `.title()` e `.isalpha()`. Departamento em maiúsculas (`.upper()`). Código da Evidência iniciando com `"EVID-"` (`.startswith()`) e Hash alfanumérico (`.isalnum()`). Tamanho e Lacre contendo estritamente dígitos (`.isdigit()`). Data com `.replace()`, `.count("/") == 2` e 10 caracteres (`len()`). E-mail terminando com `".policia.gov.br"` (`.endswith()`). Senha protegida por máscara `"*" * len(senha)` e Parecer `"INTEGRO"` conferido em laço com `range(5)`.[cite: 3]

### 08. Plataforma de Leilões e Rastreamento de Gado Bovino
* **Enunciado (12 Entradas):** Nome do Pecuarista, Nome da Fazenda, Raça do Animal, Município do Registro, Código do Brinco Eletrônico, Registro Genealógico, Peso em Arrobas, Idade em Meses, Data da Pesagem (`DD-MM-AAAA`), E-mail da Associação Agropecuária, PIN do Produtor, Certificação Sanitária (`APROVADO`).[cite: 3]
* **Regras:** Pecuarista, Fazenda, Raça e Município com `.title()` e `.isalpha()`. Brinco iniciando em `"BOV-"` (`.startswith()`) e Registro Genealógico alfanumérico (`.isalnum()`). Peso e Idade contendo exclusivamente números (`.isdigit()`). Data com `.replace("-", "/")` e verificação de 2 barras com `.count()`. E-mail institucional terminando em `".agro.org.br"` (`.endswith()`). PIN oculto com `"*" * len(pin)` e Certificação validada como `"APROVADO"` em 5 tentativas (`range(5)`).[cite: 3]

### 09. Centro de Comando e Telemetria de Drones de Resgate
* **Enunciado (12 Entradas):** Nome do Piloto Remoto, Região de Busca, Cidade Base, Tipo de Missão, Prefixo do Drone, Canal do Transmissor, Altitude de Voo, Nível da Bateria em Porcentagem, Data da Decolagem (`DD-MM-AAAA`), E-mail do Corpo de Bombeiros, Chave de Arme dos Motores, Status do Link (`CONECTADO`).[cite: 3]
* **Regras:** Piloto, Região, Cidade e Tipo de Missão com `.title()` e `.isalpha()`. Prefixo iniciando com `"DRONE-"` (`.startswith()`) e Canal alfanumérico (`.isalnum()`). Altitude e Bateria com apenas dígitos (`.isdigit()`). Data tratada com `.replace()` contendo 2 barras (`.count()`) e 10 caracteres (`len()`). E-mail com final `".bombeiros.gov.br"` (`.endswith()`). Chave mascarada com `"*" * len(chave)` e Status `"CONECTADO"` em até 5 tentativas com `range(5)`.[cite: 3]

### 10. Plataforma de E-commerce e Despacho de Pedidos Rápidos
* **Enunciado (12 Entradas):** Nome do Comprador, Sobrenome, Cidade de Entrega, Estado Federativo, Código de Rastreamento, SKU do Produto, Quantidade Comprada, Valor Total em Reais, Data da Postagem (`DD-MM-AAAA`), E-mail do Cliente, Código de Validação do Cartão, Status da Entrega (`DESPACHADO`).[cite: 3]
* **Regras:** Comprador, Sobrenome e Cidade com `.title()` e `.isalpha()`. Estado em maiúsculas (`.upper()`). Rastreamento iniciando com `"LOG-"` (`.startswith()`) e SKU alfanumérico (`.isalnum()`). Quantidade e Valor estritamente numéricos (`.isdigit()`). Data ajustada com `.replace("-", "/")` e `.count("/") == 2`. E-mail terminando em `".com.br"` (`.endswith()`). Código de Validação mascarado com `"*" * len(cvv)` e Status `"DESPACHADO"` em 5 tentativas (`range(5)`).[cite: 3]

### 11. Controle de Acesso ao Datacenter de Segurança Nacional
* **Enunciado (12 Entradas):** Nome do Especialista, Área de Atuação, Empresa Contratada, Cidade da Sede, Código do Rack, ID do Gabinete, Temperatura do Corredor Frio, Umidade Relativa do Ar, Data do Acesso (`DD-MM-AAAA`), E-mail Corporativo, Senha Biométrica, Liberação da Porta (`ABERTO`).[cite: 4]
* **Regras:** Especialista, Área e Cidade com `.title()` e `.isalpha()`. Empresa em maiúsculas (`.upper()`). Código do Rack iniciando com `"RACK-"` (`.startswith()`) e ID alfanumérico (`.isalnum()`). Temperatura e Umidade com apenas números (`.isdigit()`). Data padronizada com `.replace()` contendo 2 barras (`.count()`) e 10 dígitos (`len()`). E-mail institucional terminando em `".datacenter.com"` (`.endswith()`). Senha protegida com `"*" * len(senha)` e Liberação `"ABERTO"` conferida em laço de 5 tentativas (`range(5)`).[cite: 4]

### 12. Sistema Municipal de Trânsito e Notificação de Infrações
* **Enunciado (12 Entradas):** Nome do Condutor, Sobrenome, Bairro da Infração, Município do Registro, Placa do Veículo, Código da Infração, Velocidade Aferida, Limite da Via, Data do Auto (`DD-MM-AAAA`), E-mail do DETRAN, Código do Radar, Validação da Notificação (`EMITIDO`).[cite: 4]
* **Regras:** Condutor, Sobrenome, Bairro e Município com `.title()` e `.isalpha()`. Código da Infração iniciando com `"MULTA-"` (`.startswith()`) e Placa alfanumérica (`.isalnum()`) com 7 caracteres (`len()`). Velocidade e Limite com números (`.isdigit()`). Data tratada com `.replace("-", "/")` e `.count("/") == 2`. E-mail terminando em `".detran.gov.br"` (`.endswith()`). Código do Radar protegido por `"*" * len(radar)` e Notificação `"EMITIDO"` validada em até 5 tentativas com `range(5)`.[cite: 4]

### 13. Monitoramento Ambiental e Estação Meteorológica da Amazônia
* **Enunciado (12 Entradas):** Nome do Pesquisador, Reserva Florestal, Bioma Monitorado, Município do Sensor, Código da Estação, Modelo do Pluviômetro, Índice UV Medido, Volume de Chuva em Milímetros, Data da Coleta (`DD-MM-AAAA`), E-mail do INPE, Chave de Calibração, Parecer Climático (`VALIDADO`).[cite: 4]
* **Regras:** Pesquisador, Reserva, Bioma e Município com `.title()` e `.isalpha()`. Estação iniciando com `"MET-"` (`.startswith()`) e Modelo alfanumérico (`.isalnum()`). Índice UV e Chuva exclusivamente dígitos (`.isdigit()`). Data ajustada com `.replace()` contendo 2 barras (`.count()`) e 10 caracteres (`len()`). E-mail oficial terminando com `".inpe.br"` (`.endswith()`). Chave protegida com `"*" * len(chave)` e Parecer `"VALIDADO"` checado em até 5 tentativas (`range(5)`).[cite: 4]

### 14. Controle de Produção e Rastreabilidade em Indústria Farmacêutica
* **Enunciado (12 Entradas):** Nome do Farmacêutico Responsável, Nome do Princípio Ativo, Forma Farmacêutica, Cidade da Fábrica, Número do Lote, Registro ANVISA, Quantidade de Comprimidos, Dosagem em Miligramas, Data da Fabricação (`DD-MM-AAAA`), E-mail do Laboratório, Hash da Fórmula, Liberação do Lote (`APROVADO`).[cite: 4]
* **Regras:** Farmacêutico, Princípio Ativo, Forma e Cidade com `.title()` e `.isalpha()`. Número do Lote iniciando com `"LOTE-"` (`.startswith()`) e Registro ANVISA alfanumérico (`.isalnum()`). Quantidade e Dosagem apenas números (`.isdigit()`). Data com `.replace("-", "/")` e checagem de 2 barras com `.count()`. E-mail finalizado com `".pharma.ind.br"` (`.endswith()`). Hash da Fórmula protegido por máscara `"*" * len(hash)` e Liberação `"APROVADO"` conferida em 5 tentativas (`range(5)`).[cite: 4]

### 15. Supervisório de Plataforma de Extração de Petróleo Offshore
* **Enunciado (12 Entradas):** Nome do Supervisor de Plataforma, Bacia de Extração, Nome do Campo, Cidade Portuária de Apoio, Código do Poço, Tag da Válvula Submarina, Pressão no Cabeçote, Vazão em Barris por Dia, Data do Monitoramento (`DD-MM-AAAA`), E-mail da Operadora, Chave da Válvula de Emergência, Estado do Poço (`ATIVO`).[cite: 4]
* **Regras:** Supervisor, Bacia, Campo e Cidade com `.title()` e `.isalpha()`. Código do Poço iniciando com `"POCO-"` (`.startswith()`) e Tag alfanumérica (`.isalnum()`). Pressão e Vazão contendo apenas dígitos (`.isdigit()`). Data corrigida com `.replace()` contendo 2 barras (`.count()`) e 10 caracteres (`len()`). E-mail terminando em `".oil.com.br"` (`.endswith()`). Chave protegida com `"*" * len(chave)` e Estado `"ATIVO"` validado em laço de até 5 repetições (`range(5)`).[cite: 4]

### 16. Controle de Voos e Operações de Pátio em Aeroporto Militar
* **Enunciado (12 Entradas):** Nome do Oficial Aviador, Posto Militar, Esquadrão Aéreo, Cidade da Base Aérea, Matrícula do Caça, Código da Missão, Combustível Abastecido em Litros, Teto de Voo em Pés, Data da Missão (`DD-MM-AAAA`), E-mail da FAB, Chave do IFF Transponder, Autorização de Decolagem (`AUTORIZADO`).[cite: 4]
* **Regras:** Oficial, Posto, Esquadrão e Cidade formatados com `.title()` e `.isalpha()`. Código da Missão iniciando com `"MISSAO-"` (`.startswith()`) e Matrícula alfanumérica (`.isalnum()`). Combustível e Teto com apenas números (`.isdigit()`). Data padronizada com `.replace("-", "/")` e `.count("/") == 2`. E-mail terminando em `".fab.mil.br"` (`.endswith()`). Chave do Transponder mascarada com `"*" * len(chave)` e Autorização `"AUTORIZADO"` em até 5 tentativas (`range(5)`).[cite: 4]

### 17. Sistema Central de Emissão de Títulos e Registro Acadêmico Superior
* **Enunciado (12 Entradas):** Nome do Diplomado, Sobrenome, Nome do Curso Superior, Cidade do Campus, Código do Diploma, Livro de Registro, Carga Horária Cumprida, Média Geral de Conclusão, Data da Colação de Grau (`DD-MM-AAAA`), E-mail da Reitoria, Código Hash do Certificado Digital, Status do Diploma (`REGISTRADO`).[cite: 4]
* **Regras:** Diplomado, Sobrenome, Curso e Cidade com `.title()` e `.isalpha()`. Código do Diploma iniciando com `"DIP-"` (`.startswith()`) e Livro alfanumérico (`.isalnum()`). Carga Horária e Média com dígitos (`.isdigit()`). Data com `.replace()`, 2 barras (`.count()`) e 10 caracteres (`len()`). E-mail terminando com `".universidade.edu.br"` (`.endswith()`). Hash do Certificado protegido por `"*" * len(hash)` e Status `"REGISTRADO"` validado em laço com `range(5)`.[cite: 4]

### 18. Terminal de Cargas Frigorificadas e Exportação de Carnes
* **Enunciado (12 Entradas):** Nome do Auditor Sanitário, Empresa Frigorífica, Tipo de Corte, Porto de Embarque, Número do Container Reefer, Certificado Internacional, Temperatura de Congelamento, Peso Líquido em Quilos, Data da Inspeção (`DD-MM-AAAA`), E-mail do Ministério da Agricultura, Lacre Eletrônico, Parecer de Exportação (`LIBERADO`).[cite: 4]
* **Regras:** Auditor, Empresa, Corte e Porto com `.title()` e `.isalpha()`. Container iniciando com `"REEFER-"` (`.startswith()`) e Certificado alfanumérico (`.isalnum()`). Temperatura e Peso contendo apenas números (`.isdigit()`). Data tratada com `.replace("-", "/")` e `.count("/") == 2`. E-mail terminando em `".mapa.gov.br"` (`.endswith()`). Lacre protegido com máscara `"*" * len(lacre)` e Parecer `"LIBERADO"` checado em até 5 repetições (`range(5)`).[cite: 4]

### 19. Sistema Central de Custódia e Liquidação de Contratos Futuros
* **Enunciado (12 Entradas):** Nome do Operador de Mesa, Corretora Financeira, Tipo de Commodity, Cidade da Bolsa, Código do Contrato Futuro, ID da Ordem de Compra, Quantidade de Lotes, Margem de Garantia em Reais, Data do Vencimento (`DD-MM-AAAA`), E-mail da B3, Chave Privada da Operação, Validação do Negócio (`EXECUTADO`).[cite: 4]
* **Regras:** Operador, Corretora, Commodity e Cidade com `.title()` e `.isalpha()`. Código do Contrato iniciando com `"B3-"` (`.startswith()`) e ID da Ordem alfanumérico (`.isalnum()`). Lotes e Margem contendo estritamente números (`.isdigit()`). Data ajustada com `.replace()` com 2
