# 🐍 SQLI-Finder v3 (Anti-429 Edition)


      ╔═╗╔═╗ ╦  ╦   ╔═╗╦╔╗╔╔╦╗╔═╗╦═╗
      ╚═╗║═╬╗║  ║───╠╣ ║║║║ ║║║╣ ╠╦╝
      ╚═╝╚═╝╚╩═╝╩   ╚  ╩╝╚╝═╩╝╚═╝╩╚═                          
          Anti-429 Edition by gnu23




## 💣 Sobre

**SQLI-Finder v3** é uma ferramenta para encontrar possíveis pontos vulneráveis a **SQL Injection** usando Google Dorking (ou fallback DuckDuckGo).  
Especialmente criada para fins **educacionais** e **testes autorizados**.  

---

## ⚙️ Features

- ✅ Busca usando Google (ou fallback DuckDuckGo caso bloqueio)
- ✅ Detecta múltiplos erros SQL comuns
- ✅ Multithread (rápido!)
- ✅ User-Agent aleatório (bypass básico)
- ✅ Suporte a proxy (inclui Tor via SOCKS5)
- ✅ Pause configurável para evitar bloqueios (anti-429)
- ✅ Exporta URLs vulneráveis em arquivo `.txt`
- ✅ Barra de progresso

---

## 🚀 Instalação

```bash
git clone https://github.com/gnu23-sys/SQLI-Finder-V3.py
cd SQLI-Finder

Requisitos principais:

Python 3

termcolor

tqdm

googlesearch-python

requests (para fallback DuckDuckGo)

💥 Exemplo de uso

python3 SQLI-Finder.py --dork "php?id=" --ext ".com" --total 20 --page 1

🌍 Usando proxy Tor

python3 SQLI-Finder.py --dork "php?id=" --ext ".br" --total 20 --page 1 --proxy socks5://127.0.0.1:9050


🐢 Aumentar delay para evitar ban


python3 SQLI-Finder.py --dork "php?id=" --ext ".org" --total 15 --page 1 --pause 30



🧊 Usando Tor (no Termux ou Linux)
No Termux ou chroot:

pkg install tor
tor


Mantém o terminal aberto com Tor rodando.
Em outro terminal, roda a ferramenta com --proxy socks5://127.0.0.1:9050.



⚠️ Aviso
❗ Use apenas para fins educacionais ou em testes autorizados.

❗ O uso contra sites sem permissão pode ser crime.

❗ O autor gnu23 não se responsabiliza por usos indevidos.

💚 Autor
gnu23

GitHub: gnu23-sys

LulzSec BlackHat Grupo: https://t.me/lulzsec_blackhat_team



⭐ Contribuições
Pull requests são bem-vindos! Se quiser ajudar a melhorar (ex.: mais payloads, suporte a Bing, etc.), só mandar!
