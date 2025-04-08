USE tax;
SET @Prov = 'BC'; -- Configure this before running --
SET @Amount = '50'; -- Configure this before running --
SET @calcrate = (SELECT rate FROM rates WHERE Province = @Prov);
SET @Amount = @calcrate * @Amount + @Amount;
INSERT INTO Data VALUES (@Amount, @calcrate);
SELECT * FROM Data;