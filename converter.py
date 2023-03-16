import OpenSSL

# carrega o arquivo PFX

def converter(arquivo, senha, status):
    nome = arquivo
    pfx_file = open(nome, 'rb').read()
    pfx_password = senha
    status.value = "Convertendo arquivo"
    status.update()
    try:
    # decodifica o arquivo PFX
        pfx = OpenSSL.crypto.load_pkcs12(pfx_file, pfx_password)

        # obtém a chave privada e o certificado
        private_key = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, pfx.get_privatekey())
        certificate = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, pfx.get_certificate())

        # salva a chave privada e o certificado em arquivos PEM
        if '.pfx' in arquivo:
            novo_nome = nome.replace(".pfx", '.pem')
        elif '.p12' in arquivo:
            novo_nome = nome.replace(".p12", '.pem')
        #novo_nome = nome.replace(".pfx", '.pem')
        open(novo_nome, 'wb').write(private_key)
        open(novo_nome, 'wb').write(certificate)
        status.value = "Arquivo convertido, salvo no mesmo local!"
        status.update()
    except:
        status.value = "Não foi possivel converter, senha ou arquivo invalido!"
        status.update()