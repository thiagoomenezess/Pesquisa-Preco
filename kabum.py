# **************************
# localizar produto na KABUM
# **************************

def pegar_preco_kabum(browser, pesquisa):
    context1 = browser.new_context()
    page_one = context1.new_page()

    page_one.goto(f"https://www.kabum.com.br/busca?query={pesquisa}")

    # Index para localizar páginas
    # index = page_one.locator('//*[contains (@class, "priceCard")]')
    index = page_one.locator('//span[contains(text(), "À vista no PIX")]')
    print(index.count())

    nome_do_produto = []
    preco_do_produto = []
    link_do_produto = []
    nome_da_loja = []
    pagina = 0

    # while page_one.is_visible('//*[@class="nextLink"]') or page_one.is_enabled('//*[@class="sc-dwLEzm bXwgF priceCard"]'):
    while True:

        print("Pegando preços na Kabum")
        print(f"Página Kabum: {pagina}")

        for i in range(index.count()):


            # Pegando os preços
            try:
                precos = page_one.locator('//*[contains (@class, "priceCard")]').nth(i).inner_text().replace("R$", "").strip().replace(".", "").replace(",", ".")
                preco_do_produto.append(float(precos))

            except:
                break

            # Pegando os nomes
            produtos = page_one.locator('//*[contains (@class, "nameCard")]').nth(i).inner_text()
            nome_do_produto.append(produtos)

            # Pegando os links
            link_do_produto.append("https://www.kabum.com.br{}".format(page_one.locator('//*[contains (@class, "productCard")]/a').nth(i).get_attribute('href')))

            # Guardando nome da Loja
            nome_da_loja.append("KABUM")

        pagina += 1

        # Condição para sair do loop infinito
        if page_one.is_enabled('//*[@class="nextLink"]') and not page_one.is_visible('//*[@class="IconCloseFill"]') and not page_one.is_visible('//*[@class="IconOpenboxFlag"]'):
            page_one.locator('//*[@class="nextLink"]').click()

        # if page_one.is_visible('//*[@class="IconCloseFill"]'):
        #     break

        else:
            break

    context1.close()
    # Tratamento para filtrar a pesquisa o mais próximo do pesquisado
    # for i in range(len(nome_do_produto)):
    #     if pesquisa.lower() in nome_do_produto[i].lower():
    #         nome_dos_produtos.append(nome_do_produto[i])
    #         preco_dos_produtos.append(preco_do_produto[i])
    #         link_dos_produtos.append(link_do_produto[i])
    #         # Colocando nome da loja em uma lista


    return nome_da_loja, nome_do_produto, preco_do_produto, link_do_produto
