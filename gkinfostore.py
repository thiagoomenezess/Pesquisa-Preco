# *********************************
# localizar produto na GkInfoStore
# *********************************

def pegar_preco_gkinfo(browser, pesquisa):
    context4 = browser.new_context()
    page_4 = context4.new_page()

    page_4.goto(f"https://www.gkinfostore.com.br/produtos?q={pesquisa}")

    # Index para pegar a quantidade de produtos por página
    index = page_4.locator('//div[@class="product-price-final"]/span[@class="price total"]').count()
    i = (index // 2)


    nome_do_produto = []
    preco_do_produto = []
    link_do_produto = []
    nome_da_loja = []

    print("Pegando preços na GkInfoStore")

    for i in range(i):

        # Pegando os preços
        try:
            precos = page_4.locator('//div[@class="product-price-final"]/span[@class="price total"]').nth(i).inner_text().replace("R$", "").strip().replace(".", "").replace(",", ".")
            preco_do_produto.append(float(precos))
            # print(precos)

        except:
            break

        # Pegando os nomes
        produtos = page_4.locator('//div[@class="product-title text-center mb-4"]').nth(i).inner_text()
        nome_do_produto.append(produtos)

        # Pegando os links
        link_do_produto.append(page_4.locator('//div[contains (@data-product-url, "https://www.gkinfostore.com.br/")]/a[contains (@class, "product-link")]').nth(i).get_attribute('href'))

        # Guardando nome da Loja
        nome_da_loja.append("GkInfoStore")


    # # Condição para sair do loop infinito
    # if page_3.is_visible('//button[@aria-label="Go to next page"]') and not page_3.is_visible('//p[contains(text(), "Esgotado")]'):
    #     page_3.locator('//button[@aria-label="Go to next page"]').click()
    #
    # else:
    #     break


    context4.close()

    return nome_da_loja, nome_do_produto, preco_do_produto, link_do_produto