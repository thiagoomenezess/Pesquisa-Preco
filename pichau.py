# **************************
# localizar produto na PICHAU
# **************************

def pegar_preco_pichau(browser, pesquisa):
    context5 = browser.new_context()
    page_one = context5.new_page()

    page_one.goto(f"https://www.pichau.com.br/search?q={pesquisa}")

    # Index para localizar páginas
    index = page_one.locator('//div[contains(text(), "R$")]')

    nome_do_produto = []
    preco_do_produto_errado = []
    preco_do_produto = []
    link_do_produto = []
    nome_da_loja = []
    pagina = 0

    while True:

        print("Pegando preços na pichau")
        print(f"Página pichau: {pagina}")

        for i in range(index.count()):
            print(index.count())
            print (i)


            # Pegando os preços
            if i % 2 == 0:
                # precos_geral = page_one.locator('//*[contains (@class, "MuiCardContent-root")]/div/div/div/div[2]').nth(i).inner_text()

                precos = page_one.locator('//div[contains(text(), "R$")]').nth(i).inner_text()
                # if not "sem juros no cartão" in precos_geral:
                precos = precos.replace("R$", "").strip().replace(".", "").replace(",", ".")
                preco_do_produto.append(float(precos))
                print(f"pegando preço: {precos}")


            if i < (index.count() // 2):

                # Pegando os nomes
                produtos = page_one.locator('//*[contains (@class, "MuiTypography-h6")]').nth(i).inner_text()
                nome_do_produto.append(produtos)
                print(f"pegando o nome: {produtos}")

                # Pegando os links
                link = page_one.locator('//div[contains (@class, "MuiGrid-root")]/div[contains (@class, "MuiGrid-root")]/div[contains (@class, "MuiGrid-root")]/div[contains (@class, "MuiGrid-root MuiGrid-item")]/a').nth(i).get_attribute('href')
                link_do_produto.append(f"https://www.pichau.com.br{link}")
                print(f"Pegando os links: {link}")

                # Guardando nome da Loja
                nome_da_loja.append("PICHAU")

            pagina += 1


        # Condição para sair do loop infinito
        if page_one.is_enabled('//button[@aria-label="Go to next page"]') and not page_one.is_visible('//p[contains(text(), "Esgotado")]'):
            page_one.locator('//button[@aria-label="Go to next page"]').click()
        # print("estou dentro do IF")

        else:
            break







    # for i, numero in enumerate(preco_do_produto_errado):
    #     if (i % 2) == 0:
    #         preco_do_produto.append(numero)
    #         print("Estou dentro do IF 2")


    return nome_da_loja, nome_do_produto, preco_do_produto, link_do_produto
