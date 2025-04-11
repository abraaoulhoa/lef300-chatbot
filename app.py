from flask import Flask, request, jsonify

app = Flask(__name__)

knowledge_base = {
    "erro 912": "⚠️ Erro 912: Tampa aberta durante operação. Verifique se a tampa frontal está completamente fechada.",
    "erro 201": "🔄 Erro 201: Problema no cartucho de tinta. Verifique se está bem encaixado ou substitua.",
    "limpeza do bocal": "🧼 Vá ao Menu > Manutenção > Limpeza da cabeça. Siga as instruções no visor. Use luvas e material recomendado.",
    "substituir cabeça de impressão": "🔧 Desligue a máquina. Use ferramentas apropriadas como TORQUE DRIVER N6. Entre em modo de serviço pressionando [←][↑][→] ao ligar o sub power.",
    "modo de serviço": "🛠️ Para entrar no modo de serviço, pressione [←][↑][→] ao ligar o sub power.",
    "ajuste da altura da mesa": "📏 Ajuste em SERVICE MENU > MOTOR MENU > AXIS MOVE > HEIGHT. Valor recomendado: 102.0 mm.",
    "wiper": "🧽 Substituição: Menu > Sub Menu > Manutenção > Replace Wiper. Siga as etapas no visor e use pinça para encaixe correto.",
    "cap top": "💧 Para trocar os Cap Tops, entre no menu de serviço, mova o eixo Y para 2.8mm, siga desmontagem com proteção UV.",
    "circulação de tinta": "🔁 Sistema de circulação ativa em linhas CMYKWh e Gloss. Melhora estabilidade e reduz entupimentos.",
    "impressão com verniz": "✨ LEF-300 permite impressão com Gloss ou Matte em processo simplificado de 2 etapas com movimento do UV Lamp.",
    "velocidade de impressão": "🚀 Print Speed depende do modo. Ex: Alta qualidade (CMYK, 12 passadas): ~10 min para 508x330mm (~1 m²/h).",
    "ajuste do sensor de altura": "📐 Ajuste feito com precisão de 0.1mm. Sensor não é mais afetado por objetos magnéticos (LEF-300).",
    "instalação da impressora": "🛠️ Posicione em superfície plana. Todos os 4 pés de borracha devem estar em contato para evitar vibração.",
    "versaworks": "🖥️ A LEF-300 é compatível com Roland VersaWorks Dual para controle de fila, perfis ICC e configurações de impressão.",
    "manutenção programada": "📅 Use a checklist do Capítulo 5 do manual de serviço para garantir manutenção periódica e preventiva.",
}

@app.route("/")
def index():
    return "LEF-300 Chatbot ativo! Endpoint de mensagens: /chatbot"

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    user_message = data.get("message", {}).get("text", "").lower()

    if "bot" in user_message:
        return jsonify({})

    for key in knowledge_base:
        if key in user_message:
            return jsonify({"text": knowledge_base[key]})

    return jsonify({
        "text": "❓ Desculpe, não encontrei informações sobre isso no manual. Tente usar palavras como: 'limpeza', 'erro 912', 'modo de serviço', etc."
    })

if __name__ == "__main__":
    app.run(port=8080)
