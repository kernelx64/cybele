# ⚠️ PROJECT STATUS / AVISO IMPORTANTE

> ### "The Ungrateful Reality / A Realidade Ingrata"
> 
> I did my part: I found the data, organized it, and tried to give it a voice. 
> Current infrastructures make it almost impossible for an ordinary citizen to maintain 
> an open data flow...
>
> **[Read the full manifesto below]**

## English Version
The Ungrateful Reality
I am right when I say that this is no longer my problem. I did my part: I found the data, organized it, and tried to give it a voice. Current infrastructures (the "modern" databases) make it almost impossible for an ordinary citizen to maintain an open data flow without having to take a cybersecurity course.

It is deeply ironic that these systems grant full administrative privileges by default upon creation—a massive security oversight—yet they treat a simple, read-only API as a threat if shared. It’s like buying a gun that comes pre-loaded with ammunition by default, yet being told it's a security risk just to show someone an empty holster. The blame lies with the evolution of technology itself, which has closed in on itself.

Not forgetting that this entire process saves any end user from the scientific component of extracting and converting values from an .nc file into pure data, accessible today even to a 15-year-old.

One Last Thought (No Pressure)
I don’t feel bad about "leaving it as it is." In computer science, as in science, tools are sometimes not yet up to the author's vision. Google Sheets is easy, but it is static — which is why Cybele lost this module. As for SQLite/Baserow, they are dynamic, but they are "paranoid" and contradictory: a read-only API should not have to face these kinds of barriers. Furthermore, the fact that APIs have full privileges by default is, in itself, a contradiction to that very "paranoia." But these are different ways of looking at things, and I guess I’m just a dinosaur in this field.

For me, this isn't just about fatigue; it’s a matter of principle. Seeing knowledge blocked by "technical semantics" is an insult to the intelligence of those who simply want to document the reality of our planet. Did you know that more than 90% of the population doesn't even know what the AMOC is or what it’s for?

This clearly explains why Cybele has been pushed to a corner. The only viable option I found—one that is free and without "walls"—was to use a simple spreadsheet to share the values.


# Versão Portuguesa
A Realidade Ingrata
Tenho razão quando digo que isto já não é um problema meu. Fiz a minha parte: encontrei os dados, organizei-os e tentei dar-lhes voz. As infraestruturas atuais (as bases de dados "modernas") tornam quase impossível para um cidadão comum manter um fluxo de dados aberto sem ter de tirar um curso de cibersegurança.

É profundamente irónico que estes sistemas concedam privilégios administrativos totais por defeito na sua criação — uma falha de segurança massiva — mas tratem uma simples API de leitura como uma ameaça se for partilhada. É como comprar uma arma que já vem carregada por defeito, mas ser-te dito que é um risco de segurança apenas mostrares o coldre vazio a alguém. A culpa é da própria evolução da tecnologia, que se fechou sobre si mesma.

Sem esquecer que todo este processo poupa a qualquer utilizador final a componente científica de extrair e converter valores de um ficheiro .nc em dados puros, acessíveis hoje até a um jovem de 15 anos.
Um último pensamento
Não me sinto mal por "deixar como está". Na informática, como na ciência, às vezes as ferramentas ainda não estão à altura da visão do autor. O Google Sheets é fácil, mas é estático, e por isso a Cybele perdeu este módulo. Já o SQLite e o Baserow são dinâmicos, mas "paranoicos" e contraditórios: uma API só de leitura não deveria passar por este tipo de entraves. Além disso, as APIs por defeito não deveriam ter privilégios totais — o que, por si só, é uma contradição à própria "paranoia" de segurança. Mas são formas de olhar para as coisas, e eu se calhar já sou um dinossauro.

Para mim, isto não é apenas cansaço; é uma questão de princípios. Ver o conhecimento ficar bloqueado por "semânticas" é um insulto à inteligência de quem quer apenas documentar a realidade — no meu caso, a do nosso planeta. Sabiam que mais de 90% da população nem sequer sabe o que é a AMOC ou para que serve?

Fica aqui bem explícito o porquê de a Cybele ter ficado encostada a um canto. A única hipótese mais viável que encontrei, gratuita e sem "muros", foi uma simples folha de cálculo para partilhar os valores.


# 🤖 Cybele Bot

> *"The code is open, but the conscience is not."* > *"Remember: Many charge monthly for a mountain I built for free."*

Cybele is an ever-evolving Python-based chatbot—think of it as a digital attic of knowledge and a curated cheat sheet for the themes mentioned below. It reached a stable beta release in August 2024. Built upon core components of my previous Zorie framework and serving as a cornerstone of the Elysia extension, Cybele employs diverse programming techniques and two distinct chatbot algorithms without using NLP or NLTK modules.

While you can certainly leverage other AI platforms to build your own chatbot, Cybele offers a unique, handcrafted experience.

---

## 🚀 How to Run

You don't need to worry about complex installations. Cybele manages its own facilities! 

### On Windows:
1. Locate the `run.bat` file in the main folder.
2. Double-click it.
3. If any libraries are missing, Cybele will ask for permission to install them. Simply type `y` and you're good to go!

### On Linux:
1. Open the terminal in the project folder.
2. Grant execution permission: `chmod +x run.sh`
3. Run it with: `./run.sh`

---

## 📁 Project Structure

* **`/src`**: Contains the core logic (`cybele.py`).
* **`/assets`**: Icons, retro-inspired graphics, and visual resources.
* **`run.bat` / `run.sh`**: Quick-launch scripts for ease of use.

---

## 🧠 Features & Design

Sporting a **retro-inspired design** reminiscent of classic consoles and terminals, Cybele functions as a comprehensive knowledge repository.

* **Knowledge Domains**: Insights ranging from "Make a Difference Daily" life advice to celestial exploration (planetary dynamics, astronomical glossary, lunar phases, and constellations).
* **Data Curation**: Meticulously curated geographical, environmental, and technological data.
* **Scientific Precision**: Incorporates the **Haversine formula** for distance calculations and sophisticated algorithms for determining sunrise, sunset, and seasonal variations.
* **Education**: Fundamental periodic table and interactive games (capitals, constellations, and elements).
* **Portability**: Designed to work **offline** and capable of running on Android or iOS devices via a Python interpreter (version 3.10+).

---

## ⚠️ Disclaimer & Info
**Expect bugs and breaking changes.** This is a labor of love and a work in progress.

ⓘ **Note**: You can find the main documentation, including installation guides, at [adelinosaldanha.site/cybele](https://www.adelinosaldanha.site/cybele)

docs: finalize Cybele v1.1.1 and legacy notes.
```markdown
# 🏺 Cybele v1.1.1

### 📅 Project Status: End of Life (EOL)
**Date:** 26.03.2026  
**Cycle:** Final Maintenance  

This repository is now in its final form. No further updates or support will be provided.

---

### ✨ Special Thanks
A huge shoutout to **[Maya]** for illuminating this code. Without that spark, the logic wouldn't shine half as bright. 💡

---
*Developed with a focus on freedom and functionality.*
ⓘ Note:
You can find the main documentation, including installation guides, at https://www.adelinosaldanha.site/cybele

## 🚀 How to Run

You don't need to worry about complex installations. Cybele manages its own facilities!
