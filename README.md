# Trabalho de Resistência de Matereais
Trabalho desenvolvido para a unidade curricular de Resistência de Materias

## Índice

- [Trabalho de Resistência de Matereais](#Trabalho-de-Resistência-de-Matereais)
  - [Índice](#índice)
  - [Objetivo](#objetivo)
  - [Descrição do Projeto](#descrição-do-projeto)
- [Classes Abstratas](#classes-abstratas)
  - [Forma](#forma)
- [Classes Principais](#classes-principais)
  - [Retangulo](#retangulo)
  - [Circulo](#circulo)
  - [Triangulo](#triangulo)
  - [Ponto2D](#ponto2d)
- [Autores](#autores)

## Objetivo
Projeto desenvolvido para determinar momentos e produtos de inérica pra áreas compostas

## Descrição do Projeto

O projeto foi desenvolvido na linguagem de programação python, com orientação a objetos, utilizando também bibliotecas como TkInter para desenvolvimento de interface grafica

# Classes Abstratas

O projeto usa o python orientado a objetos, com isso durante o desenvolvimento vimos a nescessidades de criar classes abstratas.

## Forma
Classe base para as outras formas gemoetricas

### Atributos
- Origem - Origem do objeto no plano cartesiano
- Centroide - Centroide do objeto
- Forma Virutal - Identificação se a forma existe ou é um complemento para facilitar o calculo
- Área - Área do objeto - estre atributo deve ser calculado por metodos da classe derivada.

# Classes Principais
As classes principais represento as formas geometricas de fato como [Retangulo](#Retangulo), [Circulo](#Circulo), [Triangulo](#Triangulo) e [Ponto2D](#Ponto2D)

## Retangulo
A classe Retangulo é usada para armazenar informações sobre a forma retângulo e também implementar alguns metodos como:
- Calculo de área

## Circulo
A classe Circulo é usada para armazenar informações sobre a forma circulo e também implementar alguns metodos como:
- Calculo de área
- Comprimento de Circunferência

## Triangulo
A classe Triangulo é usada para armazenar as informações sobre a forma triangulo e também implementar os seguintes metodos:
- Metodos de identificação do tipo de Triangulo
  - Equilatero
  - Isoceles
  - Escaleno
- Validação do triangulo
  Metodo usado para verificar se o triangulo existe a partir da condição de existencia do triangulo.

## Ponto2D
A classe Ponto2D é usada para armazenar coordenadas no plano cartesiano, seus principais atributos são:
- X
- Y

A classe Também implementa o metodo clone, que instancia e retorna um objeto igual a si.

# Autores
- [Edson Augusto Pereira Ferreira](https://github.com/Edson-2003)
- [Gustavo Oliveira da Silva](https://github.com/LegnD4y)
- [Lucas Robiati Sant'Ana](https://github.com/Lucas-Robiati)
