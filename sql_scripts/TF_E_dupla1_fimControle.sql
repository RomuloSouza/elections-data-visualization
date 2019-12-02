--  ----------------------- eleicoes --------------------------
--                                                                  
--                    SCRIPT DE CONTROLE (DDL)                           
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

CREATE USER 'admin'@'localhost' IDENTIFIED BY '@d2019';
GRANT ALL PRIVILEGES ON eleicoes.* TO 'admin'@'localhost';

CREATE USER 'user'@'localhost' IDENTIFIED BY 'uso2019';
GRANT SELECT ON eleicoes.* TO 'user'@'localhost';