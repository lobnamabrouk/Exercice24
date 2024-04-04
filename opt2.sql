SELECT Combinaisons.ID, COUNT(DISTINCT correspondance_combinaison_regle.RegleID) AS NombreStatuts
FROM Combinaisons
JOIN correspondance_combinaison_regle ON Combinaisons.ID = correspondance_combinaison_regle.CombinaisonID
GROUP BY Combinaisons.ID
HAVING COUNT(DISTINCT correspondance_combinaison_regle.RegleID) > 1;