# *****************************
# localizar produto na TERABYTE
# *****************************

def pegar_preco_terabyte(browser, pesquisa):
    context2 = browser.new_context()
    page_two = context2.new_page()

    page_two.goto('https://www.terabyteshop.com.br/busca?str={}'.format(pesquisa))

    # Index para localizar páginas
    index_page_two = page_two.locator('//div[@class="prod-new-price"]')

    nome_do_produto_tera = []
    preco_do_produto_tera = []
    link_do_produto_tera = []
    nome_da_loja_tera = []
    pagina = 0

    print("Pegando preços na Terabyte")

    for i in range(index_page_two.count()):

        print(f"Página Terabyte: {pagina}")

        # Pegando os preços
        try:
            precos = page_two.locator('//div[@class="prod-new-price"]/span').nth(i).inner_text().replace("R$", "").strip().replace(".", "").replace(",", ".")
            preco_do_produto_tera.append(float(precos))
            # print("pegando preço: {}".format(precos))
            print(i)
            print(preco_do_produto_tera)
        except:
            break

        # Pegando os nomes
        produtos = page_two.locator('//div[@class="commerce_columns_item_caption"]').nth(i).inner_text()
        nome_do_produto_tera.append(produtos)
        # print(nome_do_produto_tera)

        # Pegando os links
        href = page_two.locator('//div[@class="commerce_columns_item_inner"]/a').nth(i)
        hrefs = href.get_attribute('href')
        link_do_produto_tera.append(hrefs)

        # Colocando nome da loja em uma lista
        nome_da_loja_tera.append("TERABYTE")

        pagina += 1

    context2.close()


    return nome_da_loja_tera, nome_do_produto_tera, preco_do_produto_tera, link_do_produto_tera








    # Tratamento para filtrar a pesquisa o mais próximo do pesquisado
    # for i in range(len(nome_do_produto)):
    #     if pesquisa.lower() in nome_do_produto[i].lower():
    #         nome_dos_produtos.append(nome_do_produto[i])
    #         preco_dos_produtos.append(preco_do_produto[i])
    #         link_dos_produtos.append(link_do_produto[i])