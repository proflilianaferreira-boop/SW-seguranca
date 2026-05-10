import bcrypt
password = 'Seg_2028!'
bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
hash = bcrypt.hashpw(bytes, salt)
userPassword =  input('Indique a password:')
userBytes = userPassword.encode('utf-8')
result = bcrypt.checkpw(userBytes, hash)
if result: print ("Palavra Passe Correta.") 
else: print ("Palavra Passe Errada.")
