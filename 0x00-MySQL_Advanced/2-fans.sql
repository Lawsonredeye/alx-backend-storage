-- script that ranks the country and its fans
-- it can be used on any db

SELECT DISTINCT `origin`, SUM(`fans`) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans
