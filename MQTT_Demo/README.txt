Copiare i seguenti file in /etc/mosquitto (Linux):

-pwd: file contenente gli utenti autorizzati a connettersi al broker, ad ognuno è associato uno username e una pwd da fornire al fine di autenticarsi

-custom.conf: configura il broker, le opzioni definite sono alla fine del file (copiare questo file in /etc/mosquitto/conf.d). Sostituire al secondo parametro dell'opzione listener l'IP del broker. Per come è configurato non sono possibili connessioni senza autenticazione.