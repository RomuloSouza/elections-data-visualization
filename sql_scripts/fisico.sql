--  ----------------------- eleicoes --------------------------
--                                                                  
--                    SCRIPT DE CRIAÇÃO (DDL)                           
--                                                                  
-- Data Criacao ..........: 24/11/2019                             
-- Autor(es) .............:
--     Rômulo Souza - 15/0147601
--     Vinícius Lima - 15/0151331
-- Banco de Dados ........: MySQL                                   
-- Base de Dados(nome) ...: eleicoes                                                                                      
--                                                                  
-- PROJETO => 1 Base de Dados                                       
--         => 7 Tabelas                                           
--                                                                  
-- -----------------------------------------------------------------


CREATE DATABASE IF NOT EXISTS eleicoes;

USE eleicoes;

CREATE TABLE CANDIDATO (
    cpf VARCHAR(15) NOT NULL,
    nomeUrna VARCHAR(100),
    sexo enum('FEMININO', 'MASCULINO'),
    nomeCandidato VARCHAR(150) NOT NULL,
    dtNascimento DATE,

    CONSTRAINT CANDIDATO_PK PRIMARY KEY (cpf)
)Engine = InnoDB DEFAULT CHARSET = utf8;

CREATE TABLE CARGO (
    idCargo INT NOT NULL AUTO_INCREMENT,
    descricaoCargo VARCHAR(100) NOT NULL,

    CONSTRAINT CARGO_PK PRIMARY KEY (idCargo)
)Engine = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;

CREATE TABLE SITUACAO (
    idSituacao INT NOT NULL AUTO_INCREMENT,
    descricaoSituacao VARCHAR(50) NOT NULL,

    CONSTRAINT SITUACAO_PK PRIMARY KEY (idSituacao)
)Engine = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;

CREATE TABLE PARTIDO (
    sigla VARCHAR(15) NOT NULL,
    nomePartido VARCHAR(50),

    CONSTRAINT PARTIDO_PK PRIMARY KEY (sigla)
)Engine = InnoDB DEFAULT CHARSET = utf8;

CREATE TABLE CANDIDATURA (
    cpf VARCHAR(15) NOT NULL,
    ano INT NOT NULL,
    unidadeEleitoral VARCHAR(100) NOT NULL,
    unidadeFederativa CHAR(2) NOT NULL,
    idCargo INT NOT NULL,
    idSituacao INT NOT NULL,
    sigla VARCHAR(15) NOT NULL,

    CONSTRAINT CANDIDATURA_CANDIDATO_FK FOREIGN KEY (cpf) REFERENCES CANDIDATO (cpf),
    CONSTRAINT CANDIDATURA_PK PRIMARY KEY (ano, cpf),
    CONSTRAINT CANDIDATURA_CARGO_FK FOREIGN KEY (idCargo) REFERENCES CARGO (idCargo),
    CONSTRAINT CANDIDATURA_SITUACAO_FK FOREIGN KEY (idSituacao) REFERENCES SITUACAO (idSituacao),
    CONSTRAINT CANDIDATURA_SIGLA_FK FOREIGN KEY (sigla) REFERENCES PARTIDO (sigla)
)Engine = InnoDB DEFAULT CHARSET = utf8;

CREATE TABLE RESULTADO (
    idResultado INT NOT NULL AUTO_INCREMENT,
    descricaoResultado VARCHAR(50) NOT NULL,

    CONSTRAINT RESULTADO_PK PRIMARY KEY (idResultado)
)Engine = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;

CREATE TABLE ELEICAO (
    idEleicao INT NOT NULL AUTO_INCREMENT,
    turno enum('1', '2') NOT NULL,
    idResultado INT NOT NULL,
    ano INT NOT NULL,
    cpf VARCHAR(15) NOT NULL,

    CONSTRAINT ELEICAO_PK PRIMARY KEY (idEleicao),
    CONSTRAINT ELEICAO_CANDIDATURA_FK FOREIGN KEY (ano, cpf) REFERENCES CANDIDATURA (ano, cpf),
    CONSTRAINT ELEICAO_UK UNIQUE (ano, cpf),
    CONSTRAINT ELEICAO_RESULTADO_FK FOREIGN KEY (idResultado) REFERENCES RESULTADO (idResultado)
)Engine = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;
