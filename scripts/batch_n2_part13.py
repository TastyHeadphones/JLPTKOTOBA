import json
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_file = os.path.join(project_root, 'jlpt-web', 'src', 'data', 'vocab.json')

    if not os.path.exists(data_file):
        return

    with open(data_file, 'r', encoding='utf-8') as f:
        vocab = json.load(f)

    enrichment = {
        "N2_1201": {"example_sentence": "（（障）しょう）げ（げ）を（を）取り除き（とりのぞき）ましょう。", "example_reading": "しょうげをとりのぞきましょう。", "example_meaning_cn": "排除障碍吧。", "example_meaning_en": "Let's remove the obstacle."},
        "N2_1202": {"example_sentence": "（（証）しょう）げ（げ）ん（ん）し（し）て（て）ください。", "example_reading": "しょうげんしてください。", "example_meaning_cn": "请作证。", "example_meaning_en": "Please testify."},
        "N2_1203": {"example_sentence": "（（照）しょう）こ（こ）を（を）見（み）て（て）ください。", "example_reading": "しょうこをみてください。", "example_meaning_cn": "请看证据（对照）。", "example_meaning_en": "Please look at the evidence/comparison."},
        "N2_1204": {"example_sentence": "（（详）しょう）さ（さ）い（い）を（を）教えて（おしえて）ください。", "example_reading": "しょうさいをおしえてください。", "example_meaning_cn": "请告诉我详细情况。", "example_meaning_en": "Please tell me the details."},
        "N2_1205": {"example_sentence": "（（省）しょう）さ（さ）つ（つ）し（し）て（て）ください。", "example_reading": "しょうさつしてください。", "example_meaning_cn": "请省察（反思）。", "example_meaning_en": "Please reflect/introspect."},
        "N2_1206": {"example_sentence": "（（商）じょう）し（し）し（し）て（て）ください。", "example_reading": "じょうししてください。", "example_meaning_cn": "请呈报（或上市）。", "example_meaning_en": "Please report it/list it on the market."},
        "N2_1207": {"example_sentence": "（（生）じょう）じ（じ）て（て）い（い）ます。", "example_reading": "じょうじています。", "example_meaning_cn": "已经产生了。", "example_meaning_en": "It has arisen/occurred."},
        "N2_1208": {"example_sentence": "（（照）しょう）じ（じ）ゅ（ゅ）ん（ん）を（を）合わせ（あわせ）て（て）ください。", "example_reading": "しょうじゅんをあわせてください。", "example_meaning_cn": "请对准瞄准镜（瞄准）。", "example_meaning_en": "Please aim/align the sights."},
        "N2_1209": {"example_sentence": "（（象）しょう）じ（じ）ょ（ょ）う（う）を（を）見（み）て（て）ください。", "example_reading": "しょうじょうをみてください。", "example_meaning_cn": "请看症状（或奖状）。", "example_meaning_en": "Please check the symptoms (or certificate)."},
        "N2_1210": {"example_sentence": "（（承）しょう）ち（ち）し（し）まし（し）た。", "example_reading": "しょうちしました。", "example_meaning_cn": "知道了（同意）。", "example_meaning_en": "Understood/I agree."},
        "N2_1211": {"example_sentence": "（（象）しょう）ち（ち）ょ（ょ）う（う）てき（てき）な（な）建物（たてもの）です。", "example_reading": "しょうちょうてきなたてものです。", "example_meaning_cn": "象征性的建筑物。", "example_meaning_en": "It's a symbolic building."},
        "N2_1212": {"example_sentence": "（（勝）しょう）ぶ（ぶ）し（し）ましょう。", "example_reading": "しょうぶしましょう。", "example_meaning_cn": "决一胜负吧。", "example_meaning_en": "Let's have a match."},
        "N2_1213": {"example_sentence": "（（消）しょう）ふ（ふ）し（し）て（て）ください。", "example_reading": "しょうふしてください。", "example_meaning_cn": "请消去（或消解）。", "example_meaning_en": "Please erase/delete it."},
        "N2_1214": {"example_sentence": "（（賞）しょう）ふ（ふ）く（く）し（し）ましょう。", "example_reading": "しょうふくしましょう。", "example_meaning_cn": "佩服（称赞）吧。", "example_meaning_en": "Let's admire/praise them."},
        "N2_1215": {"example_sentence": "（（消）しょう）ぼ（ぼ）う（う）し（し）ゃ（ゃ）が（が）来（き）まし（し）た。", "example_reading": "しょうぼうしゃがきました。", "example_meaning_cn": "消防车来了。", "example_meaning_en": "The fire truck has arrived."},
        "N2_1216": {"example_sentence": "（（详）しょう）み（み）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "しょうみょうしてください。", "example_meaning_cn": "请说明（声明）。", "example_meaning_en": "Please explain/declare it."},
        "N2_1217": {"example_sentence": "（（消）しょう）め（め）つ（つ）し（し）ない（ない）で（で）ください。", "example_reading": "しょうめつしないでください。", "example_meaning_cn": "请不要消灭。", "example_meaning_en": "Please don't perish/disappear."},
        "N2_1218": {"example_sentence": "（（証）しょう）め（め）い（い）し（し）て（て）ください。", "example_reading": "しょうめいしてください。", "example_meaning_cn": "请证明（或照明）。", "example_meaning_en": "Please prove/illuminate it."},
        "N2_1219": {"example_sentence": "（（消）しょう）も（も）う（う）し（し）ないで（で）ください。", "example_reading": "しょうもうしないでください。", "example_meaning_cn": "请不要消耗。", "example_meaning_en": "Please don't consume/exhaust it."},
        "N2_1220": {"example_sentence": "（（奨）しょう）よ（よ）を（を）もらい（もらい）たい（たい）です。", "example_reading": "しょうよをもらいたいです。", "example_meaning_cn": "想领奖金（红利）。", "example_meaning_en": "I want to receive a bonus."},
        "N2_1221": {"example_sentence": "（（勝）しょう）り（り）を（を）つかみ（つかみ）ましょう。", "example_reading": "しょうりをつかみましょう。", "example_meaning_cn": "把握胜利吧。", "example_meaning_en": "Let's seize victory."},
        "N2_1222": {"example_sentence": "（（奨）しょう）れ（れ）い（い）し（し）て（て）ください。", "example_reading": "しょうれいしてください。", "example_meaning_cn": "请奖励（鼓励）。", "example_meaning_en": "Please encourage/incentivize."},
        "N2_1223": {"example_sentence": "（（順）じょ）を（を）守り（まもり）ましょう。", "example_reading": "じょをまもりましょう。", "example_meaning_cn": "按顺序（缘故）吧。", "example_meaning_en": "Let's follow the order."},
        "N2_1224": {"example_sentence": "（（徐）じょ）に（に）慣れ（なれ）ましょう。", "example_reading": "じょになれましょう。", "example_meaning_cn": "慢慢（渐渐）习惯吧。", "example_meaning_en": "Let's get used to it gradually."},
        "N2_1225": {"example_sentence": "（（助）じょ）を（を）呼び（よび）ましょう。", "example_reading": "じょをよびましょう。", "example_meaning_cn": "呼救（或找助手）吧。", "example_meaning_en": "Let's call for help/an assistant."},
        "N2_1226": {"example_sentence": "（（処）しょ）を（を）教えて（おしえて）ください。", "example_reading": "しょをおしえてください。", "example_meaning_cn": "请告诉到处（或处分）。", "example_meaning_en": "Please tell me the place/disposition."},
        "N2_1227": {"example_sentence": "（（書）しょ）を（を）認（したた）め（め）て（て）ください。", "example_reading": "しょをしたためてください。", "example_meaning_cn": "请写书（或书法）。", "example_meaning_en": "Please write the document/calligraphy."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N2_1227. N2 Level Complete.")

if __name__ == "__main__":
    main()
