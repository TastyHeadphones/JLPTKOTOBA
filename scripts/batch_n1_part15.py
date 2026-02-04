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
        "N1_1401": {"example_sentence": "（（立）りっ）し（し）ゅ（ゅ）ん（ん）が（が）過ぎ（すぎ）ま（ま）し（し）た。", "example_reading": "りっしゅんがすぎました。", "example_meaning_cn": "立春已经过了。", "example_meaning_en": "Beginning of spring has passed."},
        "N1_1402": {"example_sentence": "（（立）りっ）し（し）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "りっしょうしてください。", "example_meaning_cn": "请立证（证明）。", "example_meaning_en": "Please prove / establish the fact."},
        "N1_1403": {"example_sentence": "（（立）りっ）そ（そ）く（く）し（し）ないで（为）ください。", "example_reading": "りっそくしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1404": {"example_sentence": "（（立）りっ）た（た）い（い）て（て）き（き）な（な）パ（ぱ）ル（る）を（を）作り（つくり）ま（ま）しょ（しょ）う（う）。", "example_reading": "りったいてきなぱるをつくりましょう。", "example_meaning_cn": "制作立体的拼图吧。", "example_meaning_en": "Let's make a three-dimensional puzzle."},
        "N1_1405": {"example_sentence": "（（立）りっ）ちゃ（ちゃ）く（く）し（し）ないで（为）ください。", "example_reading": "りっちゃくしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1406": {"example_sentence": "（（立）りっ）て（て）き（き）に（に）なら（なら）ないで（为）ください。", "example_reading": "りってきにならないでください。", "example_meaning_cn": "请不要（变成由于立点或立脚）。", "example_meaning_en": "Please don't (be on the point / standing)."},
        "N1_1407": {"example_sentence": "（（立）りっ）ぽ（ぽ）し（し）ないで（为）ください。", "example_reading": "りっぽしないでください。", "example_meaning_cn": "请不要（立脚或已经准备）。", "example_meaning_en": "Please don't (be standing / ready)."},
        "N1_1408": {"example_sentence": "（（立）りっ）ぽ（ぽ）う（う）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "りっぽうをたのしみましょう。", "example_meaning_cn": "享受立法吧。", "example_meaning_en": "Let's enjoy the legislation."},
        "N1_1409": {"example_sentence": "（（利）り）づ（づ）め（め）し（し）ないで（为）ください。", "example_reading": "りづめしないでください。", "example_meaning_cn": "请不要（利己或利用）。", "example_meaning_en": "Please don't (be selfish / use it)."},
        "N1_1410": {"example_sentence": "（（理）り）な（な）ら（ら）ないで（为）ください。", "example_reading": "りならないでください。", "example_meaning_cn": "请不要恢复理智（或已经解释）。", "example_meaning_en": "Please don't return to reason / be explained."},
        "N1_1411": {"example_sentence": "（（利）り）に（に）し（し）て（て）ください。", "example_reading": "りにしてください。", "example_meaning_cn": "请使其有用（或已经准备）。", "example_meaning_en": "Please make it useful / ready."},
        "N1_1412": {"example_sentence": "（（理）り）に（に）なら（なら）ないで（为）ください。", "example_reading": "りにならないでください。", "example_meaning_cn": "请不要（变得有名或为了理由）。", "example_meaning_en": "Please don't (be famous / for a reason)."},
        "N1_1413": {"example_sentence": "（（利）り）の（の）目（め）を（を）見（み）ま（ま）しょ（しょ）う（う）。", "example_reading": "りのめをみましょう。", "example_meaning_cn": "看利益的趋势吧。", "example_meaning_en": "Let's see the trend of profits."},
        "N1_1414": {"example_sentence": "（（様）りゃく）し（し）て（て）ください。", "example_reading": "りゃくしてください。", "example_meaning_cn": "请省略（简称）。", "example_meaning_en": "Please abbreviate / omit it."},
        "N1_1415": {"example_sentence": "（（略）りゃく）が（が）つ（つ）し（し）ないで（为）ください。", "example_reading": "りゃくがつしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1416": {"example_sentence": "（（略）りゃく）ご（ご）を（を）使い（つかい）ま（ま）しょ（しょ）う（う）。", "example_reading": "りゃくごをつかいましょう。", "example_meaning_cn": "使用略语吧。", "example_meaning_en": "Let's use abbreviations."},
        "N1_1417": {"example_sentence": "（（略）りゃく）さ（さ）を（を）保っ（たもっ）て（て）ください。", "example_reading": "りゃくさをたもってください。", "example_meaning_cn": "请保持简略（或策略）。", "example_meaning_en": "Please maintain the brevity / strategy."},
        "N1_1418": {"example_sentence": "（（略）りゃく）し（し）ゅ（ゅ）う（う）し（し）て（て）ください。", "example_reading": "りゃくしゅうしてください。", "example_meaning_cn": "请使其成形（或已经收集）。", "example_meaning_en": "Please shape it / collect it."},
        "N1_1419": {"example_sentence": "（（略）りゃく）じ（じ）を（を）書き（かき）ま（ま）しょ（しょ）う（う）。", "example_reading": "りゃくじをかきましょう。", "example_meaning_cn": "写略字吧。", "example_meaning_en": "Let's write a simplified character."},
        "N1_1420": {"example_sentence": "（（流）りゅう）い（い）し（し）て（て）ください。", "example_reading": "りゅういしてください。", "example_meaning_cn": "请注意（留意）。", "example_meaning_en": "Please pay attention / be careful."},
        "N1_1421": {"example_sentence": "（（粒）りゅう）が（が）し（し）ないで（为）ください。", "example_reading": "りゅうがしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1422": {"example_sentence": "（（流）りゅう）か（か）し（し）て（て）ください。", "example_reading": "りゅうかしてください。", "example_meaning_cn": "请使其流动（或已经硫化）。", "example_meaning_en": "Please make it flow / sulfidize."},
        "N1_1423": {"example_sentence": "（（流）りゅう）き（き）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "りゅうきをまもりましょう。", "example_meaning_cn": "遵守流仪（或规则）吧。", "example_meaning_en": "Let's keep the style / school traditions."},
        "N1_1424": {"example_sentence": "（（流）りゅう）げ（げ）ん（ん）ひ（ひ）ご（ご）に（に）惑わ（まどわ）さ（さ）れ（れ）ないで（为）ください。", "example_reading": "りゅうげんひごにまどわされないでください。", "example_meaning_cn": "不要被流言蜚语所迷惑。", "example_meaning_en": "Don't be misled by wild rumors."},
        "N1_1425": {"example_sentence": "（（竜）りゅう）こ（こ）つ（つ）し（し）ないで（为）ください。", "example_reading": "りゅうこつしないでください。", "example_meaning_cn": "请不要（龙骨或已经结实）。", "example_meaning_en": "Please don't (be a keel / solid)."},
        "N1_1426": {"example_sentence": "（（流）りゅう）さ（さ）を（を）保っ（たもっ）て（て）ください。", "example_reading": "りゅうさをたもってください。", "example_meaning_cn": "请保持流动性（或已经流散）。", "example_meaning_en": "Please maintain the flow / dispersion."},
        "N1_1427": {"example_sentence": "（（柳）りゅう）さ（さ）ん（ん）が（が）舞っ（まっ）て（て）い（い）ます。", "example_reading": "りゅうさんがまっています。", "example_meaning_cn": "硫酸（或柳絮）正在飞舞。", "example_meaning_en": "Sulfuric acid / willow catkins are dancing in the air."},
        "N1_1428": {"example_sentence": "（（流）りゅう）し（し）ゅ（ゅ）つ（つ）を（を）防ぎ（ふせぎ）ま（ま）しょ（しょ）う（う）。", "example_reading": "りゅうしゅつをふせぎましょう。", "example_meaning_cn": "防止流出（或泄露）吧。", "example_meaning_en": "Let's prevent the outflow / leak."},
        "N1_1429": {"example_sentence": "（（粒）りゅう）し（し）を（を）調べ（しらべ）ま（ま）しょ（しょ）う（う）。", "example_reading": "りゅうしをしらべましょう。", "example_meaning_cn": "调查粒子吧。", "example_meaning_en": "Let's investigate the particles."},
        "N1_1430": {"example_sentence": "（（流）りゅう）せ（せ）い（い）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "りゅうせいをたのしみましょう。", "example_meaning_cn": "享受流星（或辉煌）吧。", "example_meaning_en": "Let's enjoy the meteors / prosperity."},
        "N1_1431": {"example_sentence": "（（流）りゅう）つ（つ）う（う）を（を）支え（ささえ）ま（马）しょ（しょ）う（う）。", "example_reading": "りゅうつうをささえましょう。", "example_meaning_cn": "支撑流通吧。", "example_meaning_en": "Let's support the distribution / circulation."},
        "N1_1432": {"example_sentence": "（（硫）りゅう）ど（ど）く（く）に（に）気（き）を（を）つけ（つけ）ま（ま）しょ（しょ）う（う）。", "example_reading": "りゅうどくにきをつけましょう。", "example_meaning_cn": "注意硫磺毒（或流动）吧。", "example_meaning_en": "Let's watch out for sulfur poison / flow."},
        "N1_1433": {"example_sentence": "（（流）りゅう）に（に）し（し）て（て）ください。", "example_reading": "りゅうにしてください。", "example_meaning_cn": "请使其流动（或已经流失）。", "example_meaning_en": "Please make it flow / missing."},
        "N1_1434": {"example_sentence": "（（流）りゅう）に（に）なら（なら）ないで（为）ください。", "example_reading": "りゅうにならないでください。", "example_meaning_cn": "请不要（流失或为了规则）。", "example_meaning_en": "Please don't (lost / for a rule)."},
        "N1_1435": {"example_sentence": "（（留）りゅう）は（は）あり（あり）ません。", "example_reading": "りゅうわありません。", "example_meaning_cn": "没有留守（或停止）。", "example_meaning_en": "There is no staying / stopping."},
        "N1_1436": {"example_sentence": "（（流）りゅう）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "りゅうふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1437": {"example_sentence": "（（隆）りゅう）り（り）ゅ（ゅ）う（う）し（し）て（て）います。", "example_reading": "りゅうりゅうしています。", "example_meaning_cn": "隆隆（兴旺）着。", "example_meaning_en": "It's prosperous / thriving."},
        "N1_1438": {"example_sentence": "（（流）りゅう）り（り）ょ（ょ）う（う）を（を）量り（はかり）ま（ま）しょ（しょ）う（う）。", "example_reading": "りゅうりょうをはかりましょう。", "example_meaning_cn": "测量流量吧。", "example_meaning_en": "Let's measure the flow rate."},
        "N1_1439": {"example_sentence": "（（流）りゅう）る（る）のを（を）手伝っ（てつだっ）て（て）ください。", "example_reading": "りゅうるのをてつだってください。", "example_meaning_cn": "请帮我旋转（或流动）。", "example_meaning_en": "Please help me rotate / flow."},
        "N1_1440": {"example_sentence": "（（流）りゅう）わ（わ）し（し）ないで（为）ください。", "example_reading": "りゅうわしないでください。", "example_meaning_cn": "请不要（和谈或流动）。", "example_meaning_en": "Please don't (be at peace / flow)."},
        "N1_1441": {"example_sentence": "（（利）り）ょ（ょ）う（う）が（が）え（え）し（し）て（て）ください。", "example_reading": "りょうがえしてください。", "example_meaning_cn": "请兑换（钱）。", "example_meaning_en": "Please exchange money."},
        "N1_1442": {"example_sentence": "（（領）りょう）か（か）い（い）し（し）ま（ま）し（し）た。", "example_reading": "りょうかいしました。", "example_meaning_cn": "了解（明白了）。", "example_meaning_en": "Understood / Roger that."},
        "N1_1443": {"example_sentence": "（（料）りょう）き（き）ん（ん）を（を）払い（はらい）ま（马）しょ（しょ）う（う）。", "example_reading": "りょうきんをはらいましょう。", "example_meaning_cn": "付费用吧。", "example_meaning_en": "Let's pay the fee / charge."},
        "N1_1444": {"example_sentence": "（（領）りょう）く（く）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "りょうくをまもりましょう。", "example_meaning_cn": "守护领空（领土）吧。", "example_meaning_en": "Let's defend the airspace / territory."},
        "N1_1445": {"example_sentence": "（（漁）りょう）し（し）が（が）海（うみ）に（に）出（で）ま（ま）す（す）。", "example_reading": "りょうしがうみにでます。", "example_meaning_cn": "渔夫出海了。", "example_meaning_en": "The fisherman goes out to sea."},
        "N1_1446": {"example_sentence": "（（領）りょう）し（し）ゅ（ゅ）う（う）し（し）て（て）ください。", "example_reading": "りょうしゅうしてください。", "example_meaning_cn": "请签收（领收）。", "example_meaning_en": "Please receive / receipt it."},
        "N1_1447": {"example_sentence": "（（量）りょう）し（し）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "りょうしょうしてください。", "example_meaning_cn": "请谅解。", "example_meaning_en": "Please acknowledge / consent."},
        "N1_1448": {"example_sentence": "（（料）りょう）し（し）ん（ん）が（が）痛み（いたみ）ま（ま）す（す）。", "example_reading": "りょうしんがいたみます。", "example_meaning_cn": "良心（或双亲）在痛。", "example_meaning_en": "My conscience / parents are in pain."},
        "N1_1449": {"example_sentence": "（（領）りょう）ち（ち）を（を）広げ（ひろげ）ま（马）しょ（しょ）う（う）。", "example_reading": "りょうちをひろげましょう。", "example_meaning_cn": "扩充领地吧。", "example_meaning_en": "Let's expand the territory."},
        "N1_1450": {"example_sentence": "（（領）りょう）ど（ど）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "りょうどをまもりましょう。", "example_meaning_cn": "守护领土吧。", "example_meaning_en": "Let's defend the territory."},
        "N1_1451": {"example_sentence": "（（料）りょう）り（り）し（し）て（て）ください。", "example_reading": "りょうりしてください。", "example_meaning_cn": "请做菜（料理）。", "example_meaning_en": "Please cook / prepare the meal."},
        "N1_1452": {"example_sentence": "（（量）りょう）を（を）量り（はかり）ま（马）しょ（しょ）う（う）。", "example_reading": "りょうをはかりましょう。", "example_meaning_cn": "量一下分量吧。", "example_meaning_en": "Let's measure the quantity."},
        "N1_1453": {"example_sentence": "（（良）りょ）く（く）し（し）ないで（为）ください。", "example_reading": "りょくしないでください。", "example_meaning_cn": "请不要（立脚或已经准备）。", "example_meaning_en": "Please don't (be standing / ready)."},
        "N1_1454": {"example_sentence": "（（旅）りょ）け（け）つ（つ）し（し）ないで（为）ください。", "example_reading": "りょけつしないでください。", "example_meaning_cn": "请不要（旅行或已经解决）。", "example_meaning_en": "Please don't (travel / be resolved)."},
        "N1_1455": {"example_sentence": "（（旅）りょ）こ（こ）う（う）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "りょこうをたのしみましょう。", "example_meaning_cn": "享受旅行吧。", "example_meaning_en": "Let's enjoy the trip."},
        "N1_1456": {"example_sentence": "（（力）りょく）さ（さ）を（を）感じ（かんじ）ます。", "example_reading": "りょくさをかんじます。", "example_meaning_cn": "感到力量（或差距）。", "example_meaning_en": "I feel the force / gap."},
        "N1_1457": {"example_sentence": "（（緑）りょく）ち（ち）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "りょくちをまもりましょう。", "example_meaning_cn": "守护绿地吧。", "example_meaning_en": "Let's protect the green space."},
        "N1_1458": {"example_sentence": "（（力）りょく）に（に）し（し）て（て）ください。", "example_reading": "りょくにしてください。", "example_meaning_cn": "请使其有用（或已经准备）。", "example_meaning_en": "Please make it useful / ready."},
        "N1_1459": {"example_sentence": "（（倫）りん）り（り）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "りんりをまもりましょう。", "example_meaning_cn": "遵守伦理吧。", "example_meaning_en": "Let's observe the ethics."},
        "N1_1460": {"example_sentence": "（（理）り）を（を）尽くし（つくし）て（て）ください。", "example_reading": "りをつくしてください。", "example_meaning_cn": "请极尽所有（或道理）。", "example_meaning_en": "Please do your utmost with everything / logic."},
        "N1_1461": {"example_sentence": "（（瑠）る）い（い）し（し）て（て）ください。", "example_reading": "るいしてください。", "example_meaning_cn": "请使其成类（或已经类似）。", "example_meaning_en": "Please classify / make it similar."},
        "N1_1462": {"example_sentence": "（（累）るい）き（き）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "るいきをまもりましょう。", "example_meaning_cn": "遵守累积（或规则）吧。", "example_meaning_en": "Let's keep the cumulative / rules."},
        "N1_1463": {"example_sentence": "（（類）るい）じ（じ）し（し）て（て）います。", "example_reading": "るいじしています。", "example_meaning_cn": "类似（相似）着。", "example_meaning_en": "It's similar / analogous."},
        "N1_1464": {"example_sentence": "（（累）るい）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "るいしんしないでください。", "example_meaning_cn": "请不要累进。", "example_meaning_en": "Please don't progress / be progressive."},
        "N1_1465": {"example_sentence": "（（類）るい）べ（べ）つ（つ）し（し）て（て）ください。", "example_reading": "るいべつしてください。", "example_meaning_cn": "请分类。", "example_meaning_en": "Please classify / categorize it."},
        "N1_1466": {"example_sentence": "（（留）る）守（す）中（ちゅう）に（に）荷物（にもつ）が（が）届き（とどき）ま（ま）し（し）た。", "example_reading": "るすちゅうにもつがとどきました。", "example_meaning_cn": "不在家的时候快递到了。", "example_meaning_en": "The package arrived while I was out."},
        "N1_1467": {"example_sentence": "（（礼）れい）あ（あ）い（い）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "れいあいをたのしみましょう。", "example_meaning_cn": "享受恋爱（或礼遇）吧。", "example_meaning_en": "Let's enjoy love / courtesy."},
        "N1_1468": {"example_sentence": "（（例）れい）う（う）を（を）考え（かんがえ）ま（马）しょ（しょ）う（う）。", "example_reading": "れいうをかんがえましょう。", "example_meaning_cn": "考虑例子（或礼节）吧。", "example_meaning_en": "Let's think about the example / courtesy."},
        "N1_1469": {"example_sentence": "（（例）れい）がい（がい）を（を）認め（みとめ）ま（马）しょ（しょ）う（う）。", "example_reading": "れいがいをみとめましょう。", "example_meaning_cn": "承认例外吧。", "example_meaning_en": "Let's allow for exceptions."},
        "N1_1470": {"example_sentence": "（（冷）れい）きゃ（きゃ）く（く）し（し）て（て）ください。", "example_reading": "れいきゃくしてください。", "example_meaning_cn": "请冷却。", "example_meaning_en": "Please cool it down."},
        "N1_1471": {"example_sentence": "（（礼）れい）ぎ（ぎ）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "れいぎをまもりましょう。", "example_meaning_cn": "遵守礼仪吧。", "example_meaning_en": "Let's observe the etiquette / manners."},
        "N1_1472": {"example_sentence": "（（励）れい）こ（こ）し（し）て（て）ください。", "example_reading": "れいこしてください。", "example_meaning_cn": "请勉励（或已经履行）。", "example_meaning_en": "Please encourage / fulfill it."},
        "N1_1473": {"example_sentence": "（（令）れい）じ（じ）ょ（ょ）う（う）を（を）受け取り（うけとり）ま（ま）し（し）た。", "example_reading": "れいじょうをうけとりました。", "example_meaning_cn": "收到了召集令（或礼状）。", "example_meaning_en": "I received the warrant / thank-you note."},
        "N1_1474": {"example_sentence": "（（冷）れい）せ（せ）い（い）に（に）なり（なり）ま（ま）しょ（しょ）う（う）。", "example_reading": "れいせいになりましょう。", "example_meaning_cn": "冷静下来吧。", "example_meaning_en": "Let's be calm / composed."},
        "N1_1475": {"example_sentence": "（（冷）れい）た（た）い（い）し（し）ないで（为）ください。", "example_reading": "れいたいしないでください。", "example_meaning_cn": "请不要（冷淡或已经冷却）。", "example_meaning_en": "Please don't (be cold / cool down)."},
        "N1_1476": {"example_sentence": "（（冷）れい）だ（だ）ん（ん）し（し）ないで（为）ください。", "example_reading": "れいだんしないでください。", "example_meaning_cn": "请不要（冷谈或论断）。", "example_meaning_en": "Please don't (be cold / judge)."},
        "N1_1477": {"example_sentence": "（（冷）れい）と（と）う（う）し（し）て（て）ください。", "example_reading": "れいとうしてください。", "example_meaning_cn": "请冷冻。", "example_meaning_en": "Please freeze it."},
        "N1_1478": {"example_sentence": "（（冷）れい）に（に）し（し）て（て）ください。", "example_reading": "れいにしてください。", "example_meaning_cn": "请使其冷静（或已经说明）。", "example_meaning_en": "Please make it calm / stated."},
        "N1_1479": {"example_sentence": "（（令）れい）に（に）なら（なら）ないで（为）ください。", "example_reading": "れいにならないでください。", "example_meaning_cn": "请不要（变得有名或为了命令）。", "example_meaning_en": "Please don't (be famous / for an order)."},
        "N1_1480": {"example_sentence": "（（冷）れい）は（は）あり（あり）ません。", "example_reading": "れいわありません。", "example_meaning_cn": "没有例子（或冷静）。", "example_meaning_en": "There is no example / calmness."},
        "N1_1481": {"example_sentence": "（（冷）れい）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "ればなしをしないでください。", "example_meaning_cn": "请不要说冷笑话（或在这种地方）。", "example_meaning_en": "Please don't tell cold jokes / talk here."},
        "N1_1482": {"example_sentence": "（（冷）れい）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "れいふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1483": {"example_sentence": "（（冷）れい）ま（ま）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "れいまわらないでください。", "example_meaning_cn": "请不要（赤裸或绕道）。", "example_meaning_en": "Please don't (be naked / go around)."},
        "N1_1484": {"example_sentence": "（（冷）れい）め（め）い（い）を（を）待ち（まち）ま（ま）しょ（しょ）う（う）。", "example_reading": "れいめいをまちましょう。", "example_meaning_cn": "等待黎明（或觉醒）吧。", "example_meaning_en": "Let's wait for the dawn / awakening."},
        "N1_1485": {"example_sentence": "（（冷）れい）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "れいらんしないでください。", "example_meaning_cn": "请不要（紊乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1486": {"example_sentence": "（（冷）れい）り（り）し（し）ないで（为）ください。", "example_reading": "れいりしないでください。", "example_meaning_cn": "请不要（离散或改变）。", "example_meaning_en": "Please don't (be dispersed / change)."},
        "N1_1487": {"example_sentence": "（（歴）れき）さ（さ）を（を）感じ（かんじ）ます。", "example_reading": "れきさをかんじます。", "example_meaning_cn": "感到历史（或差距）。", "example_meaning_en": "I feel the history / gap."},
        "N1_1488": {"example_sentence": "（（歴）れき）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "れきぜんとしています。", "example_meaning_cn": "历然（明显）着。", "example_meaning_en": "It's obvious / distinct."},
        "N1_1489": {"example_sentence": "（（列）れつ）に（に）並ん（ならん）で（で）ください。", "example_reading": "れつにならんでください。", "example_meaning_cn": "请排队。", "example_meaning_en": "Please stand in line."},
        "N1_1490": {"example_sentence": "（（列）れつ）に（に）なら（なら）ないで（为）ください。", "example_reading": "れつにならないでください。", "example_meaning_cn": "请不要（列队或由于分裂）。", "example_meaning_en": "Please don't (be in line / divided)."},
        "N1_1491": {"example_sentence": "（（練）れん）あ（あ）い（い）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "れんあいをたのしみましょう。", "example_meaning_cn": "享受恋爱吧。", "example_meaning_en": "Let's enjoy the romance."},
        "N1_1492": {"example_sentence": "（（連）れん）が（が）つ（つ）し（し）ないで（为）ください。", "example_reading": "れんがつしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1493": {"example_sentence": "（（連）れん）き（き）ゅ（ゅ）う（う）を（を）楽しみ（たのしみ）ま（马）しょ（しょ）う（う）。", "example_reading": "れんきゅうをたのしみましょう。", "example_meaning_cn": "享受长假吧。", "example_meaning_en": "Let's enjoy the long holiday."},
        "N1_1494": {"example_sentence": "（（連）れん）け（け）い（い）を（を）取り（とり）ま（马）しょ（しょ）う（う）。", "example_reading": "れんけいをとりましょう。", "example_meaning_cn": "协作（配合）吧。", "example_meaning_en": "Let's cooperate / coordinate."},
        "N1_1495": {"example_sentence": "（（連）れん）こ（こ）し（し）て（て）ください。", "example_reading": "れんこしてください。", "example_meaning_cn": "请使其联结（或已经练习）。", "example_meaning_en": "Please connect / practice it."},
        "N1_1496": {"example_sentence": "（（連）れん）ざ（ざ）い（い）し（し）ないで（为）ください。", "example_reading": "れんざいしないでください。", "example_meaning_cn": "请不要坐连（或已经遭受）。", "example_meaning_en": "Please don't be involved / suffer."},
        "N1_1497": {"example_sentence": "（（連）れん）し（し）ゅ（ゅ）う（う）を（を）し（し）ま（马）しょ（しょ）う（う）。", "example_reading": "れんしゅうをしましょう。", "example_meaning_cn": "练习吧。", "example_meaning_en": "Let's practice."},
        "N1_1498": {"example_sentence": "（（廉）れん）じ（じ）ょ（ょ）う（う）し（し）ないで（为）ください。", "example_reading": "れんじょうしないでください。", "example_meaning_cn": "请不要（廉让或已经准备）。", "example_meaning_en": "Please don't (be moderate / ready)."},
        "N1_1499": {"example_sentence": "（（連）れん）ず（ず）な（な）話題（わだい）を（を）出し（だし）ま（马）しょ（しょ）う（う）。", "example_reading": "れんずなわだいをだしましょう。", "example_meaning_cn": "提出连续的话题（或透镜）吧。", "example_meaning_en": "Let's bring up consistent topics / lenses."},
        "N1_1500": {"example_sentence": "（（連）れん）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "れんぜんとしています。", "example_meaning_cn": "连然（明显）着。", "example_meaning_en": "It's obvious / distinct."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_1500.")

if __name__ == "__main__":
    main()
