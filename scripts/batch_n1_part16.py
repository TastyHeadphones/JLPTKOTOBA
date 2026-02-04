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
        "N1_1501": {"example_sentence": "（（連）れん）の（の）人（ひと）たち（たち）を（を）待ち（まち）ま（ま）しょ（しょ）う（う）。", "example_reading": "れんのひとたちをまちましょう。", "example_meaning_cn": "等那一伙人吧。", "example_meaning_en": "Let's wait for that group of people."},
        "N1_1502": {"example_sentence": "（（連）れん）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "ればなしをしないでください。", "example_meaning_cn": "请不要（说明或谈话）。", "example_meaning_en": "Please don't (explain / talk)."},
        "N1_1503": {"example_sentence": "（（連）れん）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "れんふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1504": {"example_sentence": "（（連）れん）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "れんらんしないでください。", "example_meaning_cn": "请不要（紊乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1505": {"example_sentence": "（（連）れん）り（り）し（し）ないで（为）ください。", "example_reading": "れんりしないでください。", "example_meaning_cn": "请不要（分离或改变）。", "example_meaning_en": "Please don't (be separated / change)."},
        "N1_1506": {"example_sentence": "（（連）れん）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "れんれいしないでください。", "example_meaning_cn": "请不要（效法或同样）。", "example_meaning_en": "Please don't (follow suit / be the same)."},
        "N1_1507": {"example_sentence": "（（連）れん）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "れんろをとおしてください。", "example_meaning_cn": "请（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1508": {"example_sentence": "（（連）れん）わ（わ）し（し）ないで（为）ください。", "example_reading": "れんわしないでください。", "example_meaning_cn": "请不要（和谈或联结）。", "example_meaning_en": "Please don't (be at peace / connect)."},
        "N1_1509": {"example_sentence": "（（路）ろ）を（を）歩き（あるき）ま（ま）しょ（しょ）う（う）。", "example_reading": "ろをあるきましょう。", "example_meaning_cn": "在路上走吧。", "example_meaning_en": "Let's walk along the road."},
        "N1_1510": {"example_sentence": "（（廊）ろう）か（か）を（を）静か（しずか）に（に）歩き（あるき）ま（ま）しょ（しょ）う（う）。", "example_reading": "ろうかをしずかにあるきましょう。", "example_meaning_cn": "在走廊里安静地走吧。", "example_meaning_en": "Let's walk quietly through the corridor."},
        "N1_1511": {"example_sentence": "（（労）ろう）き（き）を（を）ねぎらい（ねぎらい）ましょう。", "example_reading": "ろうきをねぎらいましょう。", "example_meaning_cn": "慰劳劳苦（或准备）吧。", "example_meaning_en": "Let's reward the labor / effort."},
        "N1_1512": {"example_sentence": "（（労）ろう）ぎ（ぎ）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "ろうぎをまもりましょう。", "example_meaning_cn": "遵守劳诣（或规则）吧。", "example_meaning_en": "Let's observe the labor ethics / rules."},
        "N1_1513": {"example_sentence": "（（労）ろう）し（し）し（し）て（て）ください。", "example_reading": "ろうししてください。", "example_meaning_cn": "请使其劳役（或已经准备）。", "example_meaning_en": "Please make it serve / ready."},
        "N1_1514": {"example_sentence": "（（労）ろう）せ（せ）い（い）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "ろうせいをたのしみましょう。", "example_meaning_cn": "享受劳力（或成功）吧。", "example_meaning_en": "Let's enjoy the labor / achievement."},
        "N1_1515": {"example_sentence": "（（牢）ろう）に（に）入ら（はいら）ないで（为）ください。", "example_reading": "ろうにはいらないでください。", "example_meaning_cn": "请不要进监狱（或固定）。", "example_meaning_en": "Please don't go to jail / be fixed."},
        "N1_1516": {"example_sentence": "（（露）ろ）こ（こ）つ（つ）な（な）物言い（ものいい）を（を）し（し）ないで（为）ください。", "example_reading": "ろこつなものいいをしないでください。", "example_meaning_cn": "不要直言不讳（太露骨）。", "example_meaning_en": "Please don't speak so bluntly / explicitly."},
        "N1_1517": {"example_sentence": "（（論）ろん）じ（じ）て（て）ください。", "example_reading": "ろんじてください。", "example_meaning_cn": "请论述（讨论）。", "example_meaning_en": "Please discuss / argue it."},
        "N1_1518": {"example_sentence": "（（論）ろん）が（が）つ（つ）し（し）ないで（为）ください。", "example_reading": "ろんがつしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1519": {"example_sentence": "（（論）ろん）ご（ご）を（を）読み（よみ）ま（ま）しょ（しょ）う（う）。", "example_reading": "ろんごをよみましょう。", "example_meaning_cn": "读《论语》吧。", "example_meaning_en": "Let's read the Analects."},
        "N1_1520": {"example_sentence": "（（論）ろん）さ（さ）を（を）保っ（たもっ）て（て）ください。", "example_reading": "ろんさをたもってください。", "example_meaning_cn": "请保持论据（或逻辑）。", "example_meaning_en": "Please maintain the argument / logic."},
        "N1_1521": {"example_sentence": "（（論）ろん）し（し）ゅ（ゅ）う（う）し（し）て（て）ください。", "example_reading": "ろんしゅうしてください。", "example_meaning_cn": "请使其成形（或已经收集）。", "example_meaning_en": "Please shape it / collect it."},
        "N1_1522": {"example_sentence": "（（論）ろん）せ（せ）い（い）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "ろんせいをたのしみましょう。", "example_meaning_cn": "享受论说（或真理）吧。", "example_meaning_en": "Let's enjoy the discourse / truth."},
        "N1_1523": {"example_sentence": "（（論）ろん）だ（だ）ん（ん）し（し）ないで（为）ください。", "example_reading": "ろんだんしないでください。", "example_meaning_cn": "请不要妄下结论。", "example_meaning_en": "Please don't jump to conclusions."},
        "N1_1524": {"example_sentence": "（（論）ろん）に（に）なら（なら）ないで（为）ください。", "example_reading": "ろんにならないでください。", "example_meaning_cn": "请不要（不成体统或为了理论）。", "example_meaning_en": "Please don't (be out of the question / for a theory)."},
        "N1_1525": {"example_sentence": "（（論）ろん）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "ろんばなしをしないでください。", "example_meaning_cn": "请不要（说明或谈话）。", "example_meaning_en": "Please don't (explain / talk)."},
        "N1_1526": {"example_sentence": "（（論）ろん）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "ろんふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1527": {"example_sentence": "（（和）わ）を（を）守り（まもり）ま（马）しょ（しょ）う（う）。", "example_reading": "わをまもりましょう。", "example_meaning_cn": "守护和睦（和谐）吧。", "example_meaning_en": "Let's maintain the harmony."},
        "N1_1528": {"example_sentence": "（（和）わ）が（が）つ（つ）し（し）ないで（为）ください。", "example_reading": "わがつしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1529": {"example_sentence": "（（和）わ）き（き）に（に）し（し）ないで（为）ください。", "example_reading": "わきにしないでください。", "example_meaning_cn": "请不要作为侧面（或已经和好）。", "example_meaning_en": "Please don't make it a side / reconciled."},
        "N1_1530": {"example_sentence": "（（和）わ）く（く）を（を）超え（こえ）て（て）ください。", "example_reading": "わくをこえてください。", "example_meaning_cn": "请超越框架（局限）。", "example_meaning_en": "Please cross the framework / limit."},
        "N1_1531": {"example_sentence": "（（和）わ）ざ（ざ）と（と）し（し）ないで（为）ください。", "example_reading": "わざとしないでください。", "example_meaning_cn": "请不要故意。 ", "example_meaning_en": "Please don't do it on purpose."},
        "N1_1532": {"example_sentence": "（（和）わ）ざ（ざ）わ（わ）い（い）を（を）防ぎ（ふせぎ）ま（马）しょ（しょ）う（う）。", "example_reading": "わざわいをふせぎましょう。", "example_meaning_cn": "防止灾祸（不幸）吧。", "example_meaning_en": "Let's prevent the disaster / misfortune."},
        "N1_1533": {"example_sentence": "（（和）わ）し（し）を（を）使い（つかい）ま（马）しょ（しょ）う（う）。", "example_reading": "わしをつかいましょう。", "example_meaning_cn": "使用和纸（或老夫）吧。", "example_meaning_en": "Let's use Japanese paper / an old man."},
        "N1_1534": {"example_sentence": "（（和）わ）す（す）れ（れ）な（な）い（い）で（为）ください。", "example_reading": "わすれないでください。", "example_meaning_cn": "请不要忘记。", "example_meaning_en": "Please don't forget it."},
        "N1_1535": {"example_sentence": "（（綿）わた）を（を）使い（つかい）ま（马）しょ（しょ）う（う）。", "example_reading": "わたをつかいましょう。", "example_meaning_cn": "使用棉花吧。", "example_meaning_en": "Let's use cotton."},
        "N1_1536": {"example_sentence": "（（和）わ）た（た）し（し）に（に）任せ（まかせ）て（て）ください。", "example_reading": "わたしにまかせてください。", "example_meaning_cn": "请交给我（我）。", "example_meaning_en": "Please leave it to me / me."},
        "N1_1537": {"example_sentence": "（（渡）わた）し（し）ぶ（ぶ）ね（ね）に（に）乗り（のり）ま（马）しょ（しょ）う（う）。", "example_reading": "わたしぶねにのりましょう。", "example_meaning_cn": "坐渡船吧。", "example_meaning_en": "Let's take the ferry."},
        "N1_1538": {"example_sentence": "（（和）わ）だ（だ）ん（ん）し（し）て（て）ください。", "example_reading": "わだんしてください。", "example_meaning_cn": "请使其和解（或已经协商）。", "example_meaning_en": "Please make peace / consult."},
        "N1_1539": {"example_sentence": "（（和）わ）な（な）に（に）か（か）かり（かり）ま（ま）し（し）た。", "example_reading": "わなにかかりました。", "example_meaning_cn": "中了陷阱。", "example_meaning_en": "I fell into a trap."},
        "N1_1540": {"example_sentence": "（（和）わ）な（な）ら（ら）ないで（为）ください。", "example_reading": "わならないでください。", "example_meaning_cn": "请不要恢复和睦（或已经准备）。", "example_meaning_en": "Please don't return to harmony / ready."},
        "N1_1541": {"example_sentence": "（（和）わ）に（に）し（し）て（て）ください。", "example_reading": "わにしてください。", "example_meaning_cn": "请定为环状（或已经和好）。", "example_meaning_en": "Please make it a ring / reconciled."},
        "N1_1542": {"example_sentence": "（（和）わ）に（に）なら（なら）ないで（为）ください。", "example_reading": "わにならないでください。", "example_meaning_cn": "请不要（成为环状或为了和睦）。", "example_meaning_en": "Please don't (be in a circle / for harmony)."},
        "N1_1543": {"example_sentence": "（（和）わ）の（の）目（め）を（を）見（み）ま（马）しょ（しょ）う（う）。", "example_reading": "わのめをみましょう。", "example_meaning_cn": "看核心（或中心）吧。", "example_meaning_en": "Let's see the center / core."},
        "N1_1544": {"example_sentence": "（（和）わ）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "わばなしをしないでください。", "example_meaning_cn": "请不要（说明或谈话）。", "example_meaning_en": "Please don't (explain / talk)."},
        "N1_1545": {"example_sentence": "（（和）わ）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "わふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1546": {"example_sentence": "（（和）わ）ま（ま）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "わまわらないでください。", "example_meaning_cn": "请不要（赤裸或绕道）。", "example_meaning_en": "Please don't (be naked / go around)."},
        "N1_1547": {"example_sentence": "（（和）わ）み（み）し（し）ないで（为）ください。", "example_reading": "わみしないでください。", "example_meaning_cn": "请不要（和美或已经说明）。", "example_meaning_en": "Please don't (be harmonious / clarify)."},
        "N1_1548": {"example_sentence": "（（和）わ）め（め）に（に）し（し）ないで（为）ください。", "example_reading": "わめにしないでください。", "example_meaning_cn": "请不要作为核心（或视线）。", "example_meaning_en": "Please don't make it a core / eye."},
        "N1_1549": {"example_sentence": "（（和）わ）ら（ら）い（い）を（を）忘れ（わすれ）ないで（为）ください。", "example_reading": "わらいをわすれないでください。", "example_meaning_cn": "请不要忘记笑容。", "example_meaning_en": "Please don't forget to smile."},
        "N1_1550": {"example_sentence": "（（和）わ）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "わらんしないでください。", "example_meaning_cn": "请不要（紊乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1551": {"example_sentence": "（（和）わ）り（り）し（し）ないで（为）ください。", "example_reading": "わりしないでください。", "example_meaning_cn": "请不要（分离或改变）。", "example_meaning_en": "Please don't (be separated / change)."},
        "N1_1552": {"example_sentence": "（（和）わ）り（り）あ（あ）い（い）を（を）考え（かんがえ）ま（马）しょ（しょ）う（う）。", "example_reading": "わりあいをかんがえましょう。", "example_meaning_cn": "考虑比例吧。", "example_meaning_en": "Let's think about the ratio."},
        "N1_1553": {"example_sentence": "（（和）わ）り（り）こ（こ）ま（ま）ないで（为）ください。", "example_reading": "わりこまないでください。", "example_meaning_cn": "请不要插队（或加塞）。", "example_meaning_en": "Please don't cut in / interrupt."},
        "N1_1554": {"example_sentence": "（（和）わ）り（り）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "わりなしをしないでください。", "example_meaning_cn": "请不要（说预言或闲聊）。", "example_meaning_en": "Please don't speak prophecies / talk."},
        "N1_1555": {"example_sentence": "（（和）わ）り（り）び（び）き（き）に（に）し（し）て（て）ください。", "example_reading": "わりびきにしてください。", "example_meaning_cn": "请打折。", "example_meaning_en": "Please give me a discount."},
        "N1_1556": {"example_sentence": "（（和）わ）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "われいしないでください。", "example_meaning_cn": "请不要（效法或同样）。", "example_meaning_en": "Please don't (follow suit / be the same)."},
        "N1_1557": {"example_sentence": "（（和）わ）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "わろをとおしてください。", "example_meaning_cn": "请（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_1557. Data enrichment complete!")

if __name__ == "__main__":
    main()
