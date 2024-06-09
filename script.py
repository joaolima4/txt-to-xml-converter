import os

def convert_to_xml(input_file, output_file):
    with open(input_file, 'r') as f:
        questions_data = f.read().strip().split('\n\n')  # Separa as perguntas

    xml_output = '<?xml version="1.0" encoding="UTF-8"?>\n<quiz>\n'

    for idx, question_data in enumerate(questions_data):
        lines = question_data.strip().split('\n')
        question_type = lines[0].split(';')[0]  # Tipo da pergunta (escolha multipla ou verdadeiro/falso)
        question_text = lines[0].split(';')[1]  # Texto da pergunta
        answers = lines[1:]  # Respostas
        
        xml_output += f'<question type="{question_type}">\n<name>\n<text>Pergunta {idx+1}</text>\n</name>\n'
        xml_output += '<questiontext format="html">\n<text>\n' + question_text + '\n</text>\n</questiontext>\n'
        
        if question_type == 'multichoice':  # Se for uma pergunta de escolha múltipla
            xml_output += '<shuffleanswers>true</shuffleanswers>\n'
            for answer_data in answers:
                parts = answer_data.split(';')
                answer_text = parts[1]
                fraction = parts[2]
                xml_output += f'<answer fraction="{fraction}">\n<text>{answer_text}</text>\n</answer>\n'
        elif question_type == 'truefalse':  # Se for uma pergunta de verdadeiro/falso
            for answer_data in answers:
                parts = answer_data.split(';')
                answer_text = parts[0]  # A resposta verdadeira/falsa
                fraction = '100' if answer_text.lower() == 'true' else '-25'  # A pontuação é 100 para verdadeiro e -25 para falso
                xml_output += f'<answer fraction="{fraction}">\n<text>{answer_text}</text>\n</answer>\n'
        
        xml_output += '</question>\n'

    xml_output += '</quiz>\n'

    with open(output_file, 'w') as f:
        f.write(xml_output)


while True:
    # Solicitar nome do arquivo de entrada
    input_file = input("Digite o nome do arquivo de texto de entrada (ex: perguntas.txt): ")
    if not input_file.endswith('.txt'): # Aqui caso ele nao ponha a sua extensao ele automaticamente mete a extensao(txt)
        input_file += '.txt'

    # Verificar se o arquivo de entrada existe
    if os.path.exists(input_file):
        print(f'Arquivo de entrada "{input_file}" encontrado com sucesso.')
        break  # Se o arquivo existir, sair do loop
    else:
        print("Arquivo de entrada não encontrado. Por favor, tente novamente.")

while True:
    # Solicitar nome do arquivo de saída
    output_file = input("Digite o nome do arquivo XML de saída (ex: perguntas.xml): ")
    if not output_file.endswith('.xml'): # Aqui caso ele nao ponha a sua extensao ele automaticamente mete a extensao(txt)
        output_file += '.xml'

    # Converter para XML
    convert_to_xml(input_file, output_file)
    print(f'Arquivo XML gerado com sucesso: {output_file}')
    break  # Saia do loop após a conversão bem-sucedida

