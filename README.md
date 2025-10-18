TDE 2 - MAPEAMENTO MEMÓRIA CACHE

Disciplina: Performance em Sistemas Ciberfísicos  
Aluna: Milena Ferraz, Leonardo Pereira, Eduardo Erthal, Diego Nunes
Linguagem: Python  

---

Vídeo Explicativo

https://youtu.be/nVCCjDkqpnk?si=mzS0cY4gs-BWZ_NL

---

Descrição do Trabalho

O objetivo deste trabalho é implementar e comparar três algoritmos de substituição de páginas:  
- FIFO (First-In, First-Out)  
- LRU (Least Recently Used)  
- MRU (Most Recently Used)

Esses algoritmos são utilizados em memória cache** para decidir qual página será removida** quando a memória estiver cheia.

---

Algoritmos Implementados

FIFO (First-In, First-Out)
- Remove a página que entrou há mais tempo na memória.
- É simples, mas pode causar mais faltas de página, pois **não considera o uso recente.

 LRU (Least Recently Used)
- Remove a página que não é usada há mais tempo.
- Simula melhor o comportamento real de programas, pois **páginas usadas recentemente têm mais chance de serem reutilizadas.

 MRU (Most Recently Used)
- Remove a página que foi **usada mais recentemente.
- Pode ser vantajoso em certos padrões de acesso (quando uma página usada recentemente **não será usada novamente tão cedo).

---

 Execução

Comando para executar o programa:

codigo sem comentarios: python3 mapeamento.py
codigo comentado: python3 mapeamento_comentado.py
