logs_acessos = [
    {"ip": "192.168.1.15", "usuario": "admin", "status": "FALHA", "valor": 0},
    {"ip": "192.168.1.15", "usuario": "admin", "status": "FALHA", "valor": 0},
    {"ip": "192.168.1.15", "usuario": "admin", "status": "FALHA", "valor": 0},
    {"ip": "192.168.1.15", "usuario": "admin", "status": "FALHA", "valor": 0},
    {"ip": "192.168.1.15", "usuario": "admin", "status": "FALHA", "valor": 0},
    {"ip": "10.0.0.8", "usuario": "carlos", "status": "SUCESSO", "valor": 4900.00},
    {"ip": "10.0.0.8", "usuario": "carlos", "status": "SUCESSO", "valor": 4950.00},
    {"ip": "172.16.0.4", "usuario": "maria", "status": "SUCESSO", "valor": 150.00},
    {"ip": "172.16.0.4", "usuario": "manu", "status": "FALHA", "valor": 0},
    {"ip": "172.16.0.4", "usuario": "manu", "status": "FALHA", "valor": 0},
    {"ip": "172.16.0.4", "usuario": "manu", "status": "SUCESSO", "valor": 200.00},
    {"ip": "172.16.0.4", "usuario": "manu", "status": "SUCESSO", "valor": 3000.00},
    
    # [DESAFIO 1]: Adicione aqui pelo menos mais 4 linhas de registros de log criados pelo grupo
] 
tentativas_ip = {}
transacoes_suspeitas = []
valor_total_fraudado = 0.0

for log in logs_acessos: 
    # 1. Contagem de Falhas por IP 
    if log["STATUS"] == "FALHA": 
        ip = log["ip"]
        tentativas_ip[ip] = tentativas_ip.get(ip, 0) + 1 

    # 2. Detecção de Fracionamento (Valores suspeitos entre R$ 4.500 e R$ 4.999)
    if log["status"] == "SUCESSO" and 4500.00 <= log["valor"] < 5000.00: 
        transacoes_suspeitas.append(log)
        # [DESAFIO 2]: Escreva a linha que acumula a soma dos valores em 'valor_total_fraudado'
        # COMPLETE: valor_total_fraudado +=...

print("=== PAINEL DE AUDITORIA DE SEGURANÇA E FRAUDES ===")

print("[ALERTA 1: TENTATIVAS DE FORÇA BRUTA (BLOQUEIO)]")
for ip, qtd in tentativas_ip.items():
    # [DESAFIO 3]: Complete a condição para bloquear somente IPs com 5 ou mais falhas 
    if qtd >= 5:
        print(f"IP BLOQUEADO: {ip} detectado com {qtd} tentativas consecutivas de falha.")

print("[ALERTA 2: TRANSAÇÕES SUSPEITAS (SMUFING)]")
for item in transacoes_suspeitas: 
    print(f"usuário: {item['usuario']} | Valor: R$ {item['valor']:.2f} | IP: {item['ip']}")

print(f"VALOR TOTAL IDENTIFICADO EM TRASAÇÕES SUSPEITAS: R$ {valor_total_fraudado:.2f}")