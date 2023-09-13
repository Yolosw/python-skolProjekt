
# Skapar en varible som kallas för i sedan skriver den ut den 10 gångr
for i in range(10):
    print("Kördes\n", i)

# Skapar en variable som kallas för c sedan lägger vi på 1 varje gång den körs tills den har uppnått 10
c = 0
# Om c är mindre än 10 så körs den
while c < 10:
    # Läggs på 1 varje gång den körs.
    c += 1
    print("Denna kördes\n",c)