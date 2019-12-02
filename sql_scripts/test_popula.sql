/* popula eleições */

USE eleicoes;

/*
INSERT INTO CANDIDATO
*/
INSERT INTO CANDIDATO (cpf, nomeUrna, sexo, nomeCandidato, dtNascimento)
VALUES ('7857136204', 'PAULINHO', 'MASCULINO', 'PAULO CESAR FERREIRA DE ARAUJO', NULL);

/*
INSERT INTO CARGO
*/
INSERT INTO CARGO (descricaoCargo) VALUES ('PREFEITO');

/*
INSERT INTO SITUACAO
*/
INSERT INTO SITUACAO (descricaoSituacao) VALUES ('DEFERIDO');

/*
INSERT INTO PARTIDO
*/
INSERT INTO PARTIDO (sigla, nomePartido) VALUES ('PFL', 'PARTIDO DA FRENTE LIBERAL');

/*
INSERT INTO CANDIDATURA
*/
INSERT INTO CANDIDATURA (cpf, ano, unidadeEleitoral, unidadeFederativa, idCargo, idSituacao, sigla)
VALUES ('7857136204', 2000, 'ACRELANDIA', 'AC', 1, 1, 'PFL');

INSERT INTO CANDIDATURA (cpf, ano, unidadeEleitoral, unidadeFederativa, idCargo, idSituacao, sigla)
VALUES ('7857136204', 2000, 'ACRELANDIA', 'AC', (select idCargo from CARGO where descricaoCargo = 'PREFEITO'), 1, 'PFL');

/*
INSERT INTO TIPOPATRIMONIO
*/

INSERT INTO TIPOPATRIMONIO (descricaoTipoPatrimonio) VALUES ('APARTAMENTO');

/*
INSERT INTO PATRIMONIO
*/
INSERT INTO PATRIMONIO (valor, detalhe, idTipoPatrimonio, ano, cpf)
VALUES (1000, 'Varios aps', 1, 2000, '7857136204');

/*
INSERT INTO RESULTADO
*/
INSERT INTO RESULTADO (descricaoResultado) VALUES ('ELEITO');

/*
INSERT INTO ELEICAO
*/
INSERT INTO ELEICAO (turno, idResultado, ano, cpf)
VALUES (1, 1, 2000, '7857136204');
INSERT INTO ELEICAO (turno, idResultado, ano, cpf)
VALUES (1, 1, 2000, '9587098234');
INSERT INTO ELEICAO (turno, idResultado, ano, cpf)
VALUES (1, 1, 2000, '9637958215');
