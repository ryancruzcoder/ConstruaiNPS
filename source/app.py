from flask import Flask, render_template, request, redirect, url_for, flash
from time import sleep as pause

list_suges = [["Recomenda-se realizar melhorias na organização e identificação dos produtos para tornar a busca mais fácil e intuitiva.",
               "Sugere-se fazer ajustes na forma como os produtos estão organizados e identificados para melhorar a experiência de busca dos clientes.",
               "Pode ser válido explorar possíveis áreas de melhoria na organização e identificação dos produtos para facilitar a navegação dos clientes.",
               "Parabéns pelo trabalho feito até o momento, mas ainda há espaço para aprimorar a organização e identificação dos produtos.",
               "Ótimo! A organização e identificação dos produtos facilitam a busca dos clientes. Mantenha esse bom trabalho."],
              ["É importante fornecer treinamento adicional aos colaboradores para melhorar a cordialidade e a disponibilidade de ajuda.",
               "É importante fornecer treinamento adicional aos colaboradores para melhorar a cordialidade e a disponibilidade de ajuda.",
               "Pode ser válido realizar uma análise mais aprofundada do atendimento dos colaboradores e identificar oportunidades de melhorias.",
               "Parabéns pelo atendimento cordial e prestativo oferecido pelos colaboradores. Continue incentivando essa abordagem.",
               "Ótimo! Os colaboradores são cordiais, atenciosos e prontos para ajudar, confiantes para uma boa experiência do cliente."],
              ["É fundamental fornecer treinamentos e capacitações aos colaboradores para que adquiram conhecimento sobre os produtos vendidos.",
               "Recomenda-se investir em programas de treinamento contínuo para aprimorar o conhecimento dos colaboradores sobre os produtos.",
               "Pode ser válido avaliar a eficácia dos treinamentos atuais e identificar oportunidades de melhorias para aumentar o conhecimento dos colaboradores.",
               "Parabéns pelo conhecimento demonstrado pelos colaboradores. Continue incentivando o aprendizado contínuo sobre os produtos.",
               "Ótimo! Os colaboradores possuem um conhecimento adequado sobre os produtos, o que contribui para a confiança dos clientes."],
              ["Sugere-se identificar os gargalos que estão causando demora no atendimento e implementar medidas para agilizar o processo.",
               "É importante realizar uma análise mais detalhada do processo de atendimento para identificar áreas de melhoria e garantir maior eficiência.",
               "Pode ser válido realizar uma avaliação mais precisa do tempo de espera e do fluxo de atendimento para identificar oportunidades de otimização.",
               "Parabéns pelos esforços para tornar o atendimento mais ágil e eficiente. Identifique melhorias adicionais possíveis para aprimorar ainda mais o processo.",
               "Ótimo! O tempo de espera é adequado, e o atendimento é ágil e eficiente, proporcionando uma boa experiência para os clientes."],
              ["Sugere-se avaliar a seleção de produtos oferecidos para garantir que estejam satisfeitos com as expectativas dos clientes em termos de qualidade.",
               "É importante buscar fornecedores e produtos da melhor qualidade para atender às expectativas dos clientes.",
               "Pode ser válido obter feedback mais detalhado dos clientes sobre os produtos e realizar ajustes na seleção, se necessário.",
               "Parabéns pela oferta de produtos de qualidade. Busque constantemente ampliar a seleção de produtos de alto padrão.",
	           "Ótimo! Os produtos vendidos são de boa qualidade e atendem às expectativas dos clientes."],
               ["Sugere-se revisar e atualizar as informações fornecidas aos clientes para garantir clareza e precisão.",
                "É importante revisar regularmente as informações fornecidas e mantê-las atualizadas para evitar confusões ou desinformações.",
                "Pode ser válido realizar uma análise mais aprofundada da clareza das informações e identificar áreas de melhoria.",
                "Parabéns pelo esforço em fornecer informações claras e precisas. Continue revisando e atualizando as informações regularmente.",
                "Ótimo! As informações fornecidas são claras, precisas e atualizadas, o que contribui para uma experiência satisfatória para os clientes."],
                ["Sugere-se rever os processos de atendimento pós-venda e garantir que os clientes recebam suporte e assistência adequada.",
                "É importante fortalecer o suporte e o atendimento pós-venda para garantir a satisfação dos clientes.",
                "Pode ser válido coletar mais feedback dos clientes sobre o atendimento pós-venda e identificar áreas específicas que precisam de melhorias.",
                "Parabéns pelo atendimento pós-venda florestal. Procure identificar oportunidades de aprimoramento contínuo para garantir a excelência nessa área.",
                "Ótimo! O atendimento pós-venda é simplificado, fornecendo suporte e assistência capacitada aos clientes."],
                ["Recomenda-se implementar as melhores práticas de gestão de estoque para garantir a disponibilidade dos produtos procurados pelos clientes.",
                "Sugere-se revisar os processos de controle de estoque e melhorar a disponibilidade dos produtos mais procurados.",
                "Pode ser válido realizar uma análise mais detalhada do controle de estoque e identificar possíveis áreas de aprimoramento.",
                "Parabéns por manter uma boa disponibilidade de estoque. Continue monitorando e ajustando conforme necessário.",
                "Ótimo! Os produtos geralmente estão disponíveis em estoque, o que contribui para uma experiência de compra positiva."],
                ["Sugere-se implementar medidas para melhorar a limpeza, organização e agradabilidade do ambiente da loja.",
                "É importante garantir a manutenção regular da limpeza e da organização da loja para criar um ambiente agradável para os clientes.",
                "Pode ser válido realizar uma avaliação mais detalhada do ambiente da loja e identificar oportunidades de melhorias.",
                "Parabéns pelo ambiente agradável, limpo e organizado da loja. Mantenha esse padrão elevado.",
                "Ótimo! O ambiente da loja é agradável, limpo e organizado, proporcionando uma experiência agradável para os clientes."],
                ["Sugere-se incentivar e treinar os colaboradores para serem mais pró-ativos no atendimento ao cliente.",
                "É importante fornecer diretrizes e incentivos para que os colaboradores sejam mais pró-ativos em ajudar os clientes e resolver problemas.",
                "Pode ser válido realizar uma avaliação mais aprofundada do nível de pró-atividade dos colaboradores e identificar oportunidades de melhorias.",
                "Parabéns pelos esforços em incentivar a pró-atividade no atendimento. Continuando encorajando os colaboradores a buscar soluções proativas para os clientes.",
                "Ótimo! Os colegas demonstraram iniciativa em oferecer ajuda e solucionar problemas, proporcionando um atendimento de qualidade."],
                ["Sugere-se trabalhar no engajamento e motivação dos colaboradores para garantir um atendimento mais entusiasmado e comprometido.",
                "É importante fornecer reconhecimento e incentivos para promover o engajamento dos colaboradores no atendimento aos clientes.",
                "Pode ser válido realizar uma análise mais aprofundada do engajamento dos colaboradores e identificar estratégias para aumentar a motivação.",
                "Parabéns pelos colaboradores engajados e comprometidos. Continue incentivando o entusiasmo no atendimento aos clientes.",
                "Ótimo! Os colaboradores demonstram entusiasmo e comprometimento em atender os clientes, o que contribui para uma experiência positiva."],
                ["Sugere-se avaliar a variedade de produtos oferecidos e identificar áreas que precisam ser expandidas para atender melhor às necessidades dos clientes.",
                "É importante buscar fornecedores adicionais ou expandir a seleção de produtos para oferecer uma variedade mais ampla.",
                "Pode ser válido obter feedback mais específico dos clientes sobre a variedade de produtos e realizar ajustes na oferta, se necessário.",
                "Parabéns pela variedade de produtos oferecidos. Identifique áreas específicas que podem ser expandidas para atender ainda mais às necessidades dos clientes.",
                "Ótimo! A loja oferece uma boa variedade de produtos que atendem às necessidades dos clientes."],
                ["Sugere-se realizar uma análise comparativa dos preços com outras lojas e ajustar a política de preços para aumentar a competitividade.",
                "É importante verificar regularmente os preços e garantir que sejam competitivos em relação ao mercado.",
                "Pode ser válido realizar uma pesquisa de mercado para comparar os preços diferenciados e identificar oportunidades de ajustes.",
                "Parabéns pelos preços competitivos. Continue monitorando o mercado para garantir a manutenção dessa competitividade.",
                "Ótimo! Os preços concedidos pela loja são competitivos em comparação com outras lojas."],
                ["Sugere-se melhorar a clareza e a eficácia da comunicação com os clientes, seja por meio de anúncios, promoções ou outras informações relevantes.",
                "É importante revisar os canais de comunicação utilizados e garantir que sejam eficazes e claros para os clientes.",
                "Pode ser válido coletar feedback adicional dos clientes sobre a comunicação da loja e identificar áreas específicas que precisam de melhorias.",
                "Parabéns pelos esforços em comunicação clara e eficaz. Busque sempre aprimorar a comunicação para garantir que as informações cheguem aos clientes de forma adequada.",
                "Ótimo! A loja se comunica de forma clara e eficaz com os clientes, fornecendo informações relevantes de maneira adequada."],
                ["Sugere-se investigar os motivos da insatisfação e tomar medidas corretivas para melhorar a experiência geral dos clientes.",
                "É importante analisar os pontos de insatisfação e tomar medidas para melhorar a experiência dos clientes.",
                "Pode ser válido realizar uma análise mais aprofundada da satisfação dos clientes e identificar áreas específicas que precisam de melhorias.",
                "Parabéns pela satisfação geral dos clientes. Continue buscando oportunidades de aprimoramento para elevar ainda mais a experiência.",
                "Ótimo! Os clientes estão satisfeitos com a loja, o que indica uma experiência positiva e satisfatória."]]             

questions = ['', 
             'Os produtos são organizados e identificados de forma clara e facilitam a busca?', 
             'Os colaboradores são cordiais, atenciosos e estão prontos para ajudar?', 
             'Os colaboradores possuem conhecimento adequado sobre os produtos vendidos?', 
             'O tempo de espera para ser atendido é adequado, e o atendimento é ágil e eficiente?', 
             'Os produtos vendidos são de boa qualidade e atendem às minhas expectativas?',
             'As informações fornecidas sobre os produtos e serviços são claras, precisas e atualizadas?',
             'O atendimento pós-venda é forte, com suporte e assistência adequada?',
             'Os produtos que eu procuro geralmente estão disponíveis em estoque?',
             'O ambiente da loja é agradável, limpo e organizado?',
             'Os colaboradores demonstraram iniciativa em oferecer ajuda e solucionar problemas?',
             'Os colaboradores demonstraram entusiasmo e comprometimento em atender os clientes?',
             'A loja oferece uma boa variedade de produtos que atendem às minhas necessidades?',
             'Os preços dos produtos da loja são competitivos em comparação com outras lojas?',
             'A loja se comunica de forma clara e eficaz com os clientes, seja por meio de anúncios, promoções ou outras informações relevantes?',
             'Considerando sua experiência geral, você está satisfeito(a) com a loja?']

counter = 0
total = 0
nome = ''
file_way = ''

def write_in(counter, resp):
    global total
    global list_suges
    global questions
    global file_way
    total = total + int(resp)
    resp_number = int(resp)
    if resp == '1':
        resp = 'Discordo totalmente'
    elif resp == '2':
        resp = 'Discordo parcialmente'
    elif resp == '3':
        resp = 'Neutro'
    elif resp == '4':
        resp = 'Concordo parcialmente'
    else:
        resp = 'Concordo totalmente'
    try:
        file = open(file_way, "a", newline="", encoding='utf-8')
        file.write(f'\n\n\n{counter}.  {questions[counter]}\n\nResposta: {resp}\n\nSugestão: {list_suges[counter - 1][resp_number - 1]}')
        file.close()
    except IndexError:
        pass


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'construai@2515'

url = "http://localhost:8080"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/questions/', methods=['POST', 'GET'])
def questions_pag():
    global total
    global counter
    global questions
    global file_way
    if request.method == 'POST':
        resp = request.form.get('radios')
        write_in(counter=counter, resp=resp)
        counter = counter + 1
        print(f'\nPergunta {counter}: {resp}\n')
        try:
            return render_template('questions.html', pergunta = questions[counter], counter = counter)
        except IndexError:
            file = open(file_way, "a", newline="", encoding='utf-8')
            file.write(f'\n\n\nTotal de Maturidade: {total}')
            file.close()
            return render_template('end.html')
    else:
        counter = 0
        counter = counter + 1
        return render_template('questions.html', pergunta = questions[counter], counter = counter)
        
@app.route('/verification/', methods=['POST'])
def verification():
    global nome
    global file_way
    nome = request.form.get("nome")
    cargo = request.form.get("cargo")
    loja = request.form.get("loja")
    cidade = request.form.get("cidade")
    if nome and cargo and loja and cidade:
        pause(5)
        nome_filter = nome[0:7] + '-' + cargo
        nome_filter = nome_filter.replace(' ', '')
        file_way = f"{nome_filter}.txt"
        file = open(file_way, "w", newline="", encoding='utf-8')
        file.truncate(0)
        file.write(f'Informações:\n\nNome: {nome} \nCargo: {cargo} \nLoja: {loja} \nCidade: {cidade} \n')
        file.close()
        return redirect(url_for('questions_pag'))
    else:
        pause(5)
        return render_template('index.html', alert=flash('Informações inválidas!')) 


@app.route('/finalized/', methods=['GET'])
def finalized():
    return render_template('end.html')



if __name__ == '__main__':
    app.run(debug=True, port=8080, host='localhost')

