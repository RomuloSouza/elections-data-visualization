--  ----------------------- eleicoes --------------------------
--                                                                  
--                    SCRIPT DE CONSULTA (DML)                           
--                                                                  
-- Data Criacao ..........: 02/12/2019                             
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

USE eleicoes;

/*
Consulta responsável por mostrar o número total de candidatos que se
candidataram por partido
*/
SELECT p.sigla, count(c.sigla) AS TotalCandidatos
FROM PARTIDO p, CANDIDATURA c 
WHERE p.sigla = c.sigla
GROUP BY c.sigla ORDER BY TotalCandidatos DESC;


/*
Essa view é responsável por mostrar o número total de candidatos que foram
eleitos por partido. Assim, pode-se fazer análises dos do resultado de cada
partido nas eleições
*/
CREATE VIEW ELEITOS_V AS
SELECT c.sigla, count(e.cpf) AS eleitos
FROM PARTIDO p, CANDIDATURA c, ELEICAO e, RESULTADO r
WHERE p.sigla = c.sigla AND c.cpf = e.cpf AND c.ano = e.ano AND
    e.idResultado = r.idResultado AND r.descricaoResultado = 'ELEITO'
GROUP BY c.sigla ORDER BY eleitos;

/*
Consulta responsável por mostrar o número de candidatos correspondente
a cada uma das situações de candidatura
*/
SELECT s.descricaoSituacao, count(c.cpf) AS TotalCandidatos
FROM SITUACAO s, CANDIDATURA c
WHERE s.idSituacao = c.idSituacao
GROUP BY s.descricaoSituacao ORDER BY TotalCandidatos DESC;
