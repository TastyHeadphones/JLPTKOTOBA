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
        "N2_776": {"example_sentence": "こう（（功）こう）ぜ（ぜ）ん（ん）と（と）し（し）た（た）態度（たいど）です。", "example_reading": "こうぜんとしたたいどです。", "example_meaning_cn": "昂然（或公然）的态度。", "example_meaning_en": "A proud/open attitude."},
        "N2_777": {"example_sentence": "こう（（構）こう）ぞ（ぞ）う（う）を（を）理解（りかい）し（し）て（て）ください。", "example_reading": "こうぞうをりかいしてください。", "example_meaning_cn": "请理解构造。", "example_meaning_en": "Please understand the structure."},
        "N2_778": {"example_sentence": "こう（（後）こう）た（た）い（い）し（し）ないで（で）ください。", "example_reading": "こうたいしないでください。", "example_meaning_cn": "请不要后退。", "example_meaning_en": "Please don't retreat."},
        "N2_779": {"example_sentence": "こう（（光）光）た（た）く（く）を（を）出し（だし）て（て）ください。", "example_reading": "こうたくをだしてください。", "example_meaning_cn": "请发出光泽。", "example_meaning_en": "Please make it glossy/lustrous."},
        "N2_780": {"example_sentence": "（（耕）こう）ち（ち）を（を）広げ（ひろげ）ましょう。", "example_reading": "こうちをひろげましょう。", "example_meaning_cn": "拓宽耕地吧。", "example_meaning_en": "Let's expand the cultivated land."},
        "N2_781": {"example_sentence": "こう（（交）こう）て（て）い（い）し（し）て（て）ください。", "example_reading": "こうていしてください。", "example_meaning_cn": "请肯定。", "example_meaning_en": "Please affirm/approve."},
        "N2_782": {"example_sentence": "こう（（公）こう）て（て）き（き）な（な）仕事（しごと）です。", "example_reading": "こうてきなしごとです。", "example_meaning_cn": "公家的（公用）工作。", "example_meaning_en": "It's official/public business."},
        "N2_783": {"example_sentence": "こう（（航）こう）て（て）い（い）を（を）確認（かくにん）し（し）てください。", "example_reading": "こうていをかくにんしてください。", "example_meaning_cn": "请确认路程（航程）。", "example_meaning_en": "Please check the itinerary/voyage."},
        "N2_784": {"example_sentence": "こう（（高）こう）て（て）い（い）が（が）あり（あり）ます。", "example_reading": "こうていがあります。", "example_meaning_cn": "有高低（起伏）。", "example_meaning_en": "There are highs and lows/fluctuations."},
        "N2_785": {"example_sentence": "こう（（講）こう）と（と）う（う）で（で）話し（はなし）て（て）ください。", "example_reading": "こうとうではなしてください。", "example_meaning_cn": "请口头叙述。", "example_meaning_en": "Please state it orally."},
        "N2_786": {"example_sentence": "こう（（高）こう）と（と）う（う）な（な）技術（ぎじゅつ）です。", "example_reading": "こうとうなぎじゅつです。", "example_meaning_cn": "高等（或尖端）的技术。", "example_meaning_en": "It's advanced/high-level technology."},
        "N2_787": {"example_sentence": "こう（（荒）こう）ど（ど）を（を）考え（かんがえ）て（て）ください。", "example_reading": "こうどをかんがえてください。", "example_meaning_cn": "请考虑荒芜程度（或高度）。", "example_meaning_en": "Please consider the degree of dereliction/altitude."},
        "N2_788": {"example_sentence": "こう（（講）こう）ど（ど）く（く）し（し）て（て）ください。", "example_reading": "こうどくしてください。", "example_meaning_cn": "请订阅（或讲读）。", "example_meaning_en": "Please subscribe/lecture."},
        "N2_789": {"example_sentence": "こう（（公）こう）に（に）ん（ん）し（し）て（て）ください。", "example_reading": "こうにんしてください。", "example_meaning_cn": "请公认。", "example_meaning_en": "Please recognize/authorize it publicly."},
        "N2_790": {"example_sentence": "こう（（後）こう）に（に）ん（ん）を（を）決め（きめ）て（て）ください。", "example_reading": "こうにんをきめてください。", "example_meaning_cn": "请决定继任者。", "example_meaning_en": "Please decide on a successor."},
        "N2_791": {"example_sentence": "こう（（光）こう）は（は）い（い）を（を）見（み）て（て）ください。", "example_reading": "こうはいをみてください。", "example_meaning_cn": "请看光背（或后辈）。", "example_meaning_en": "Please see the halo/junior."},
        "N2_792": {"example_sentence": "こう（（幸）こう）ふ（ふ）く（く）を（を）祈り（いのり）ましょう。", "example_reading": "こうふくをいのりましょう。", "example_meaning_cn": "祈祷幸福吧。", "example_meaning_en": "Let's pray for happiness."},
        "N2_793": {"example_sentence": "こう（（降）こう）ふ（ふ）く（く）し（し）て（て）ください。", "example_reading": "こうふくしてください。", "example_meaning_cn": "请投降（或服从）。", "example_meaning_en": "Please surrender."},
        "N2_794": {"example_sentence": "こう（（興）こう）ふ（ふ）ん（ん）し（し）ないで（で）ください。", "example_reading": "こうふんしないでください。", "example_meaning_cn": "请不要兴奋（激动）。", "example_meaning_en": "Please don't get excited."},
        "N2_795": {"example_sentence": "こう（（公）こう）へ（へ）い（い）に（に）し（し）て（て）ください。", "example_reading": "こうへいにしてください。", "example_meaning_cn": "请做得公平。", "example_meaning_en": "Please be fair/impartial."},
        "N2_796": {"example_sentence": "こう（（候）こう）ほ（ほ）を（を）選ん（えらん）で（て）ください。", "example_reading": "こうほをえらんでください。", "example_meaning_cn": "请选择候选人（或气候）。", "example_meaning_en": "Please choose a candidate/climate."},
        "N2_797": {"example_sentence": "こう（（公）こう）む（む）い（い）ん（ん）になり（なり）たい（たい）です。", "example_reading": "こうむいんになりたいです。", "example_meaning_cn": "想当公务员。", "example_meaning_en": "I want to become a civil servant."},
        "N2_798": {"example_sentence": "こう（（功）こう）り（り）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "こうりょうしてください。", "example_meaning_cn": "请考量（或使用香料）。", "example_meaning_en": "Please consider/use spices."},
        "N2_799": {"example_sentence": "こう（（効）こう）り（り）ょ（ょ）く（く）を（を）考え（かんがえ）て（て）ください。", "example_reading": "こうりょくをかんがえてください。", "example_meaning_cn": "请考虑效力（效果）。", "example_meaning_en": "Please consider the effectiveness."},
        "N2_800": {"example_sentence": "こう（（航）こう）ろ（ろ）を（を）進ん（すすん）で（て）ください。", "example_reading": "こうろをすすんでください。", "example_meaning_cn": "请沿着航线行驶。", "example_meaning_en": "Please proceed along the route/sea path."},
        "N2_801": {"example_sentence": "（（凍）こお）ら（ら）せ（せ）ないで（で）ください。", "example_reading": "こおらせないでください。", "example_meaning_cn": "请不要让它结冰（冻住）。", "example_meaning_en": "Please don't let it freeze."},
        "N2_802": {"example_sentence": "（（小）こ）お（お）ろし（ろし）し（し）て（て）ください。", "example_reading": "こおろししてください。", "example_meaning_cn": "请批发（或零售）。", "example_meaning_en": "Please resell/sell in small lots."},
        "N2_803": {"example_sentence": "こ（こ）が（が）ね（ね）が（が）あり（あり）ます。", "example_reading": "こがねがあります。", "example_meaning_cn": "有金币（黄金）。", "example_meaning_en": "There is small gold/coins."},
        "N2_804": {"example_sentence": "（（漕）こ）い（い）で（て）ください。", "example_reading": "こいでください。", "example_meaning_cn": "请划（船或踏板）。", "example_meaning_en": "Please row/pedal."},
        "N2_805": {"example_sentence": "（（焦）こ）が（が）さ（さ）ないで（で）ください。", "example_reading": "こがさないでください。", "example_meaning_cn": "请不要烧焦。", "example_meaning_en": "Please don't burn/scorch it."},
        "N2_806": {"example_sentence": "（（焦）こ）げ（げ）て（て）います。", "example_reading": "こげています。", "example_meaning_cn": "已经焦了。", "example_meaning_en": "It's burnt/charred."},
        "N2_807": {"example_sentence": "（（個）こ）こ（こ）に（に）話し（はなし）て（て）ください。", "example_reading": "ここににはなしてください。", "example_meaning_cn": "请个别叙述。", "example_meaning_en": "Please speak individually."},
        "N2_808": {"example_sentence": "（（心）こころ）え（え）て（て）ください。", "example_reading": "こころえてください。", "example_meaning_cn": "请领会（心得）。", "example_meaning_en": "Please understand/be aware of it."},
        "N2_809": {"example_sentence": "（（心）こころ）が（が）け（け）て（て）ください。", "example_reading": "こころがけてください。", "example_meaning_cn": "请留心（注意）。", "example_meaning_en": "Please keep in mind/strive for."},
        "N2_810": {"example_sentence": "（（心）こころ）強（づよ）い（い）ですね！ ", "example_reading": "こころづよいですね！", "example_meaning_cn": "真胆大（或令人放心）呢！", "example_meaning_en": "That's encouraging/heartening!"},
        "N2_811": {"example_sentence": "（（心）こころ）細い（ぼそい）です。", "example_reading": "こころぼそいです。", "example_meaning_cn": "心里没底（胆怯）。", "example_meaning_en": "I feel lonely/uneasy."},
        "N2_812": {"example_sentence": "（（試）こころ）み（み）て（て）ください。", "example_reading": "こころみてください。", "example_meaning_cn": "请尝试。", "example_meaning_en": "Please try/attempt it."},
        "N2_813": {"example_sentence": "（（快）こころよ）い（い）風（かぜ）です。", "example_reading": "こころよいかぜです。", "example_meaning_cn": "清爽（快（意））的风。", "example_meaning_en": "A pleasant breeze."},
        "N2_814": {"example_sentence": "（（快）こころよ）く（く）受け（うけ）て（て）ください。", "example_reading": "こころよくうけてください。", "example_meaning_cn": "请欣然接受。", "example_meaning_en": "Please accept it willingly/cheerfully."},
        "N2_815": {"example_sentence": "（（腰）こし）を（を）掛け（かけ）て（て）ください。", "example_reading": "こしをかけてください。", "example_meaning_cn": "请坐下（挂腰）。", "example_meaning_en": "Please sit down."},
        "N2_816": {"example_sentence": "（（箇）こ）じ（じ）ょ（ょ）を（を）数え（かぞえ）て（て）ください。", "example_reading": "こじょをかぞえてください。", "example_meaning_cn": "请数一下条目（个条）。", "example_meaning_en": "Please count the items/articles."},
        "N2_817": {"example_sentence": "（（越）こ）し（し）て（て）ください。", "example_reading": "こしてください。", "example_meaning_cn": "请越过（或搬家）。", "example_meaning_en": "Please cross over/move."},
        "N2_818": {"example_sentence": "（（箇）こ）す（す）う（う）を（を）確認（かくにん）し（し）てください。", "example_reading": "こすうをかくにんしてください。", "example_meaning_cn": "请确认个数。", "example_meaning_en": "Please check the number of items."},
        "N2_819": {"example_sentence": "（（擦）こす）り（り）合わせ（あわせ）て（て）ください。", "example_reading": "こすりあわせてください。", "example_meaning_cn": "请摩擦合拢。", "example_meaning_en": "Please rub them together."},
        "N2_820": {"example_sentence": "（（擦）こす）っ（っ）て（て）ください。", "example_reading": "こすってください。", "example_meaning_cn": "请揉擦。", "example_meaning_en": "Please rub it."},
        "N2_821": {"example_sentence": "（（拘）こだわ）ら（ら）ないで（で）ください。", "example_reading": "こだわらないでください。", "example_meaning_cn": "请不要拘泥（或挑剔）。", "example_meaning_en": "Please don't obsess over it/be picky."},
        "N2_822": {"example_sentence": "（（孤）こ）ど（ど）く（く）を（を）愛し（あいし）て（て）います。", "example_reading": "こどくをあいしています。", "example_meaning_cn": "爱孤独。", "example_meaning_en": "I love solitude."},
        "N2_823": {"example_sentence": "こと（（言）こと）に（に）よれ（よれ）ば（ば）そう（そう）です。", "example_reading": "ことによればそうです。", "example_meaning_cn": "视情况（说起来）是那样的。", "example_meaning_en": "Depending on the circumstances, that's correct."},
        "N2_824": {"example_sentence": "（（殊）こと）に（に）大切（たいせつ）な（な）こと（こと）です。", "example_reading": "ことにたいせつなことです。", "example_meaning_cn": "特别（殊）重要的事情。", "example_meaning_en": "It's an especially important matter."},
        "N2_825": {"example_sentence": "（（事）こと）欠か（かか）ないで（で）ください。", "example_reading": "ことかかないでください。", "example_meaning_cn": "请不要欠缺（事事周全）。", "example_meaning_en": "Please don't lack anything/be resourceful."},
        "N2_826": {"example_sentence": "（（事）こと）がら（ら）を（を）話し（はなし）て（て）ください。", "example_reading": "ことがらをおなしてください。", "example_meaning_cn": "请详述事由。", "example_meaning_en": "Please explain the details/matter."},
        "N2_827": {"example_sentence": "（（事）こと）づ（づ）て（て）に（に）聞き（きき）まし（し）た。", "example_reading": "ことづてにききました。", "example_meaning_cn": "传闻（传话）听说的。", "example_meaning_en": "I heard it by word of mouth."},
        "N2_828": {"example_sentence": "（（異）こと）な（な）る（る）意見（いけん）です。", "example_reading": "ことなるいけんです。", "example_meaning_cn": "不同的见解。", "example_meaning_en": "A differing opinion."},
        "N2_829": {"example_sentence": "（（事）こと）によ（よ）って（て）は（は）中止（ちゅうし）です。", "example_reading": "ことによってはちゅうしです。", "example_meaning_cn": "视情况可能会中止。", "example_meaning_en": "It might be cancelled depending on the situation."},
        "N2_830": {"example_sentence": "（（断）ことわ）っ（っ）て（て）ください。", "example_reading": "ことわってください。", "example_meaning_cn": "请拒绝（或预先说明）。", "example_meaning_en": "Please decline/pre-inform."},
        "N2_831": {"example_sentence": "（（粉）こな）ご（ご）な（な）に（に）し（し）て（て）ください。", "example_reading": "こなごなにしてください。", "example_meaning_cn": "请弄得粉碎。", "example_meaning_en": "Please smash it to pieces."},
        "N2_832": {"example_sentence": "（（好）この）ま（ま）し（し）い（い）結果（けっか）です。", "example_reading": "このましいけっかです。", "example_meaning_cn": "令人满意的结果。", "example_meaning_en": "A desirable result."},
        "N2_833": {"example_sentence": "（（好）この）ん（ん）で（て）やり（やり）ます。", "example_reading": "このんでやります。", "example_meaning_cn": "乐意去（喜好）做。", "example_meaning_en": "I do it by choice/willingly."},
        "N2_834": {"example_sentence": "（（拒）こば）ん（ん）で（て）ください。", "example_reading": "こばんでください。", "example_meaning_cn": "请拒绝（拒不接受）。", "example_meaning_en": "Please refuse/resist."},
        "N2_835": {"example_sentence": "（（零）こぼ）さ（さ）ないで（で）ください。", "example_reading": "こぼさないでください。", "example_meaning_cn": "请不要洒出来。", "example_meaning_en": "Please don't spill it."},
        "N2_836": {"example_sentence": "（（零）こぼ）れ（れ）て（て）います。", "example_reading": "こぼれています。", "example_meaning_cn": "正洒着（或流露）呢。", "example_meaning_en": "It's spilling/overflowing."},
        "N2_837": {"example_sentence": "（（細）こま）か（か）に（に）話し（はなし）て（て）ください。", "example_reading": "こまかにはなしてください。", "example_meaning_cn": "请细说。", "example_meaning_en": "Please talk in detail."},
        "N2_838": {"example_sentence": "（（細）こま）ご（ご）ま（ま）し（し）た（た）用事（ようじ）です。", "example_reading": "こまごましたようじです。", "example_meaning_cn": "琐碎（细碎）的杂事。", "example_meaning_en": "Small/trivial errands."},
        "N2_839": {"example_sentence": "こ（こ）ま（ま）っ（っ）た（た）こと（こと）を（を）し（し）ないで（で）ください。", "example_reading": "こまったことをしないでください。", "example_meaning_cn": "请不要做让人为难的事情。", "example_meaning_en": "Please don't do troublesome things."},
        "N2_840": {"example_sentence": "（（細）こま）やか（か）な（な）配慮（はいりょ）です。", "example_reading": "こまやかなはいりょです。", "example_meaning_cn": "细致（亲切/浓厚）的关怀。", "example_meaning_en": "Fine/tender consideration."},
        "N2_841": {"example_sentence": "（（混）こ）み（み）あっ（あっ）て（て）います。", "example_reading": "こみあっています。", "example_meaning_cn": "正挤（混杂）着呢。", "example_meaning_en": "It's crowded/congested."},
        "N2_842": {"example_sentence": "（（込）こ）め（め）て（て）ください。", "example_reading": "こめてください。", "example_meaning_cn": "请包含（或投入）。", "example_meaning_en": "Please include/put into."},
        "N2_843": {"example_sentence": "（（小）こ）や（や）を（を）建て（たて）ましょう。", "example_reading": "こやをたてましょう。", "example_meaning_cn": "搭个小屋吧。", "example_meaning_en": "Let's build a hut."},
        "N2_844": {"example_sentence": "（（凝）こ）ら（ら）し（し）て（て）ください。", "example_reading": "こらしてください。", "example_meaning_cn": "请凝神（或集中）。", "example_meaning_en": "Please concentrate/strain your eyes."},
        "N2_845": {"example_sentence": "（（凝）こ）り（り）か（か）た（た）まっ（まっ）た（た）考え（かんがえ）です。", "example_reading": "こりかたまったかんがえです。", "example_meaning_cn": "顽固（死板）的想法。", "example_meaning_en": "A rigid/stubborn idea."},
        "N2_846": {"example_sentence": "（（懲）こ）り（り）て（て）ください。", "example_reading": "こりてください。", "example_meaning_cn": "请吸取教训（不再重蹈覆辙）。", "example_meaning_en": "Please learn your lesson/be discouraged."},
        "N2_847": {"example_sentence": "（（凝）こ）る（る）人（ひと）ですね。", "example_reading": "こるひとですね。", "example_meaning_cn": "是个讲究（或入迷）的人呢。", "example_meaning_en": "He's a person who's very picky/absorbed."},
        "N2_848": {"example_sentence": "（（殺）ころ）さ（さ）ないで（で）ください！ ", "example_reading": "ころさないでください！", "example_meaning_cn": "请不要杀生！", "example_meaning_en": "Please don't kill!"},
        "N2_849": {"example_sentence": "（（転）ころ）が（が）し（し）て（て）ください。", "example_reading": "ころがしてください。", "example_meaning_cn": "请滚动。", "example_meaning_en": "Please roll/tumble it."},
        "N2_850": {"example_sentence": "（（転）ころ）が（が）っ（っ）て（て）います。", "example_reading": "ころがっています。", "example_meaning_cn": "正滚（倒）在那儿呢。", "example_meaning_en": "It's rolling/lying around."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N2_850.")

if __name__ == "__main__":
    main()
