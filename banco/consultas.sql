-- Consulta básica para validação da carga
SELECT * FROM SENSORES;

-- Contagem de registros
SELECT COUNT(*) AS TOTAL_REGISTROS FROM SENSORES;

-- Média de umidade
SELECT AVG(UMID) AS MEDIA_UMIDADE FROM SENSORES;

-- Registros onde a irrigação foi ligada
SELECT * FROM SENSORES
WHERE BOMBA = 'True';

-- Registros com chuva
SELECT * FROM SENSORES
WHERE CHUVA = 'True';