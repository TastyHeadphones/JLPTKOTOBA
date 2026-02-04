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
        "N1_501": {"example_sentence": "（（往）おう）よ（よ）う（う）に（に）話し（はなし）て（て）ください。", "example_reading": "おうようにおなしてください。", "example_meaning_cn": "请详细地谈话。", "example_meaning_en": "Please speak in detail."},
        "N1_502": {"example_sentence": "（（王）おう）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "おうらわないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_503": {"example_sentence": "（（産）う）ん（ん）で（て）ください。", "example_reading": "うんでください。", "example_meaning_cn": "请生产（或分娩）。", "example_meaning_en": "Please give birth / produce it."},
        "N1_504": {"example_sentence": "（（起き）おき）あ（あ）が（が）っ（っ）て（て）ください。", "example_reading": "おきあがってください。", "example_meaning_cn": "请起来（起床）。", "example_meaning_en": "Please get up / stand up."},
        "N1_505": {"example_sentence": "（（置）お）き（き）か（か）え（え）て（て）ください。", "example_reading": "おきかえてください。", "example_meaning_cn": "请更换（替换）。", "example_meaning_en": "Please replace / substitute it."},
        "N1_506": {"example_sentence": "（（沖）おき）な（な）い（い）で（で）ください。", "example_reading": "おきないでください。", "example_meaning_cn": "请不要在海面上（或起来）。", "example_meaning_en": "Please don't be offshore / don't get up."},
        "N1_507": {"example_sentence": "（（置）お）き（き）な（な）ま（ま）せ（せ）て（て）ください。", "example_reading": "おきなませてください。", "example_meaning_cn": "请搁置（或在座）。", "example_meaning_en": "Please leave it as is / be present."},
        "N1_508": {"example_sentence": "（（奥）おく）ぎ（ぎ）を（を）極め（きわめ）ましょう。", "example_reading": "おくぎをきわめましょう。", "example_meaning_cn": "钻研奥义（秘诀）吧。", "example_meaning_en": "Let's master the inner secrets / deep mysteries."},
        "N1_509": {"example_sentence": "（（臆）おく）き（き）ょ（ょ）う（う）に（に）なら（なら）ないで（で）ください。", "example_reading": "おくきょうにならないでください。", "example_meaning_cn": "不要胆怯（胆小）。", "example_meaning_en": "Please don't be a coward."},
        "N1_510": {"example_sentence": "（（贈）おく）り（り）もの（もの）を（を）し（し）ましょう。", "example_reading": "おくりものをしましょう。", "example_meaning_cn": "送礼（赠物）吧。", "example_meaning_en": "Let's give a gift."},
        "N1_511": {"example_sentence": "（（後）おく）れ（れ）げ（げ）を（を）直し（なおし）て（て）ください。", "example_reading": "おくれげをなおしてください。", "example_meaning_cn": "请理弄一下后脑勺的碎发。", "example_meaning_en": "Please fix your stray hair at the back."},
        "N1_512": {"example_sentence": "（（後）おく）れ（れ）さ（さ）せ（せ）ないで（で）ください。", "example_reading": "おくれさせないでください。", "example_meaning_cn": "请不要让我迟到（延误）。", "example_meaning_en": "Please don't make me late."},
        "N1_513": {"example_sentence": "（（起）お）こ（こ）せ（せ）ないで（で）ください。", "example_reading": "おこせないでください。", "example_meaning_cn": "请不要叫醒我。", "example_meaning_en": "Please don't wake me up."},
        "N1_514": {"example_sentence": "（（行）おこな）い（い）を（を）慎み（つつしみ）ましょう。", "example_reading": "おこないをつつしみましょう。", "example_meaning_cn": "谨言慎行（慎重行为）吧。", "example_meaning_en": "Let's behave prudently."},
        "N1_515": {"example_sentence": "（（起）お）こ（こ）り（り）を（を）絶っ（たっ）て（て）ください。", "example_reading": "おこりをたってください。", "example_meaning_cn": "请断绝起源（或病根）。", "example_meaning_en": "Please cut off the source / origin."},
        "N1_516": {"example_sentence": "（（怠）おこた）ら（ら）ない（ない）で（で）ください。", "example_reading": "おこたらないでください。", "example_meaning_cn": "请不要怠慢（疏忽）。", "example_meaning_en": "Please don't neglect it / be diligent."},
        "N1_517": {"example_sentence": "（（怒）おこ）ら（ら）せ（せ）ないで（で）ください。", "example_reading": "おこらせないでください。", "example_meaning_cn": "请不要让我生气。", "example_meaning_en": "Please don't make me angry."},
        "N1_518": {"example_sentence": "（（起）お）こ（こ）る（る）のを（を）手伝っ（てつだっ）て（て）ください。", "example_reading": "おこるのわてつだってください。", "example_meaning_cn": "请帮我引起（或发生）。", "example_meaning_en": "Please help me make it happen / occur."},
        "N1_519": {"example_sentence": "（（奢）おご）ら（ら）ないで（で）ください。", "example_reading": "おごらないでください。", "example_meaning_cn": "请不要奢侈（自满）。", "example_meaning_en": "Please don't be extravagant / haughty."},
        "N1_520": {"example_sentence": "（（奢）おご）り（り）は（は）あり（あり）ません。", "example_reading": "おごりわありません。", "example_meaning_cn": "没有奢侈（傲慢）。", "example_meaning_en": "There is no luxury / pride."},
        "N1_521": {"example_sentence": "（（厳）おごそ）か（か）な（な）儀式（ぎしき）です。", "example_reading": "おごそかなぎしきです。", "example_meaning_cn": "庄严的仪式。", "example_meaning_en": "It's a solemn ceremony."},
        "N1_522": {"example_sentence": "（（教）おし）え（え）を（を）乞い（こい）ましょう。", "example_reading": "おしえをこいましょう。", "example_meaning_cn": "请教（请乞教诲）吧。", "example_meaning_en": "Let's ask for guidance / instruction."},
        "N1_523": {"example_sentence": "（（愛）お）し（し）い（い）結果（けっか）でした。", "example_reading": "おしいけっかでした。", "example_meaning_cn": "是令人惋惜的结果。", "example_meaning_en": "It was a regrettable / close result."},
        "N1_524": {"example_sentence": "（（押）お）し（し）あ（あ）き（き）ないで（で）ください。", "example_reading": "おしあきないでください。", "example_meaning_cn": "请不要（强制推销或厌烦）。", "example_meaning_en": "Please don't (be pushy / get tired of it)."},
        "N1_525": {"example_sentence": "（（押）お）し（し）あ（あ）て（て）て（て）ください。", "example_reading": "おしあててください。", "example_meaning_cn": "请按住（贴紧）。", "example_meaning_en": "Please press / hold it against something."},
        "N1_526": {"example_sentence": "（（押）お）し（し）か（か）え（え）さ（さ）ないで（で）ください。", "example_reading": "おしかえさないでください。", "example_meaning_cn": "请不要推回。", "example_meaning_en": "Please don't push back."},
        "N1_527": {"example_sentence": "（（押）お）し（し）か（か）け（け）ないで（で）ください。", "example_reading": "おしかけないでください。", "example_meaning_cn": "请不要闯入（硬要去）。", "example_meaning_en": "Please don't barge in / visit uninvited."},
        "N1_528": {"example_sentence": "（（押）お）し（し）か（か）さ（さ）ないで（で）ください。", "example_reading": "おしかさないでください。", "example_meaning_cn": "请不要（重叠或压碎）。", "example_meaning_en": "Please don't (overlap / crush)."},
        "N1_529": {"example_sentence": "（（押）お）し（し）き（き）っ（っ）て（て）ください。", "example_reading": "おしきってください。", "example_meaning_cn": "请坚持到底（排斥反对）。", "example_meaning_en": "Please push it through / overcome opposition."},
        "N1_530": {"example_sentence": "（（惜）お）し（し）げ（げ）な（な）い（い）努力（どりょく）です。", "example_reading": "おしげないどりょくです。", "example_meaning_cn": "毫不吝啬（无憾）的努力。", "example_meaning_en": "It's a generous / unsparing effort."},
        "N1_531": {"example_sentence": "（（押）お）し（し）こ（こ）ま（ま）ないで（で）ください。", "example_reading": "おしこまないでください。", "example_meaning_cn": "请不要塞进去。", "example_meaning_en": "Please don't crowd in / push in."},
        "N1_532": {"example_sentence": "（（押）お）し（し）な（な）が（が）さ（さ）ないで（で）ください。", "example_reading": "おしながさないでください。", "example_meaning_cn": "请不要冲走（或推开）。", "example_meaning_en": "Please don't wash away / push aside."},
        "N1_533": {"example_sentence": "（（押）お）し（し）の（の）け（け）ない（ない）で（で）ください。", "example_reading": "おしのけないでください。", "example_meaning_cn": "请不要推开（排挤）。", "example_meaning_en": "Please don't push aside / elbow aside."},
        "N1_534": {"example_sentence": "（（押）お）し（し）は（は）か（か）っ（っ）て（て）ください。", "example_reading": "おしはかってください。", "example_meaning_cn": "请推测（推量）。", "example_meaning_en": "Please surmise / conjecture."},
        "N1_535": {"example_sentence": "（（押）お）し（し）ま（ま）く（く）っ（っ）て（て）ください。", "example_reading": "おしまくってください。", "example_meaning_cn": "请猛推（猛攻）。", "example_meaning_en": "Please keep pushing hard / attack forcefully."},
        "N1_536": {"example_sentence": "（（惜）お）し（し）む（む）のを（を）やめ（やめ）ましょう。", "example_reading": "おしむのをやめましょう。", "example_meaning_cn": "别再可惜（或吝啬）了吧。", "example_meaning_en": "Let's stop feeling regret / being stingy."},
        "N1_537": {"example_sentence": "（（押）お）し（し）よ（よ）せ（せ）ないで（で）ください。", "example_reading": "おしよせないでください。", "example_meaning_cn": "请不要蜂拥而至。", "example_meaning_en": "Please don't surge / crowd forward."},
        "N1_538": {"example_sentence": "（（愛）お）し（し）み（み）な（な）が（が）ら（ら）帰り（かえり）まし（し）た。", "example_reading": "おしみながらかえりました。", "example_meaning_cn": "恋恋不舍（惜别）地回去了。", "example_meaning_en": "I went home reluctantly (with regret)."},
        "N1_539": {"example_sentence": "（（教）おし）え（え）ご（ご）に（に）会い（あい）まし（し）た。", "example_reading": "おしえごにあいました。", "example_meaning_cn": "见到了学生（弟子）。", "example_meaning_en": "I met my pupil / student."},
        "N1_540": {"example_sentence": "（（雄）お）す（す）だ（だ）け（け）集め（あつめ）て（て）ください。", "example_reading": "おすだけあつめてください。", "example_meaning_cn": "请只收集雄性。", "example_meaning_en": "Please collect only the males."},
        "N1_541": {"example_sentence": "（（汚）お）せ（せ）ん（ん）さ（さ）せ（せ）ないで（で）ください。", "example_reading": "おせんさせないでください。", "example_meaning_cn": "请不要造成污染。", "example_meaning_en": "Please don't allow it to be polluted."},
        "N1_542": {"example_sentence": "（（襲）おそ）わ（わ）れ（れ）ないで（で）ください。", "example_reading": "おそわれないでください。", "example_meaning_cn": "请不要被袭击。", "example_meaning_en": "Please don't be attacked."},
        "N1_543": {"example_sentence": "（（遅）おそ）き（き）に（に）失し（しっし）て（て）い（い）ます。", "example_reading": "おそきにしっしています。", "example_meaning_cn": "为时已晚（迟了）。", "example_meaning_en": "It's too late / missed the timing."},
        "N1_544": {"example_sentence": "（（遅）おそ）く（く）と（と）も（も）明日（あした）まで（まで）に（に）。", "example_reading": "おそくともあしたまでに。", "example_meaning_cn": "最迟到明天为止。", "example_meaning_en": "By tomorrow at the latest."},
        "N1_545": {"example_sentence": "（（恐）おそ）ら（ら）く（く）来る（くる）で（で）しょう。", "example_reading": "おそらくくるでしょう。", "example_meaning_cn": "恐怕（大概）会来吧。", "example_meaning_en": "He will probably come."},
        "N1_546": {"example_sentence": "（（恐れ）おそれ）お（お）お（お）い（い）事（こと）です。", "example_reading": "おそれおおいことです。", "example_meaning_cn": "惶恐（真是不敢当）的事。", "example_meaning_en": "It's a most gracious / awe-inspiring thing."},
        "N1_547": {"example_sentence": "（（恐れ）おそれ）入り（はいり）ます。", "example_reading": "おそれいります。", "example_meaning_cn": "非常抱歉（或不敢当）。", "example_meaning_en": "I'm much obliged / I beg your pardon."},
        "N1_548": {"example_sentence": "（（恐れ）おそれ）な（な）がら（ながら）申し上げ（もうしあげ）ます。", "example_reading": "おそれながらもうしあげます。", "example_meaning_cn": "冒昧（惶恐）启奏。", "example_meaning_en": "I venture to state (with all due respect)."},
        "N1_549": {"example_sentence": "（（恐）おそ）ろ（ろ）し（し）い（い）夢（ゆめ）を（を）見（み）まし（し）た。", "example_reading": "おそろしいゆめをみました。", "example_meaning_cn": "做了个可怕的梦。", "example_meaning_en": "I had a terrifying dream."},
        "N1_550": {"example_sentence": "（（教）おさ）わ（わ）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "おさわらわないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_551": {"example_sentence": "（（穏）おだ）や（や）か（か）な（な）海（うみ）です。", "example_reading": "おだやかなうみです。", "example_meaning_cn": "平稳的海。", "example_meaning_en": "A calm / peaceful sea."},
        "N1_552": {"example_sentence": "（（煽）おだ）て（て）ないで（で）ください。", "example_reading": "おだてないでください。", "example_meaning_cn": "请不要奉承（戴高帽）。", "example_meaning_en": "Please don't flatter / butter me up."},
        "N1_553": {"example_sentence": "（（落）お）ち（ち）あ（あ）い（い）ましょう。", "example_reading": "おちあいましょう。", "example_meaning_cn": "汇合（相见）吧。", "example_meaning_en": "Let's meet / join up."},
        "N1_554": {"example_sentence": "（（落）お）ち（ち）い（い）ら（ら）ないで（で）ください。", "example_reading": "おちいらないでください。", "example_meaning_cn": "请不要陷入（或中计）。", "example_meaning_en": "Please don't fall into / get trapped."},
        "N1_555": {"example_sentence": "（（落）お）ち（ち）つ（つ）い（い）て（て）ください。", "example_reading": "おちついてください。", "example_meaning_cn": "请冷静下来。", "example_meaning_en": "Please calm down / settle down."},
        "N1_556": {"example_sentence": "（（落）お）ち（ち）な（な）ら（ら）さ（さ）ないで（で）ください。", "example_reading": "おちならさないでください。", "example_meaning_cn": "请不要（跌落或平静）。", "example_meaning_en": "Please don't (fall down / be quiet)."},
        "N1_557": {"example_sentence": "（（乙）おつ）な（な）味（あじ）ですね。", "example_reading": "おつなあじですね。", "example_meaning_cn": "别致的（有韵味的）味道呢。", "example_meaning_en": "It's a chic / unique flavor."},
        "N1_558": {"example_sentence": "（（夫）おっ）と（と）を（を）支え（ささえ）ます。", "example_reading": "おっとをささえます。", "example_meaning_cn": "支持丈夫。", "example_meaning_en": "I support my husband."},
        "N1_559": {"example_sentence": "（（仰）おっ）しゃ（しゃ）る（る）通り（とおり）です。", "example_reading": "おっしゃるとおりです。", "example_meaning_cn": "正如您所说。", "example_meaning_en": "It's exactly as you say (honorific)."},
        "N1_560": {"example_sentence": "（（威）お）ど（ど）か（か）さ（さ）ないで（で）ください。", "example_reading": "おどかさないでください。", "example_meaning_cn": "请不要吓唬（威胁）我。", "example_meaning_en": "Please don't threaten / scare me."},
        "N1_561": {"example_sentence": "（（威）お）ど（ど）さ（さ）ないで（で）ください。", "example_reading": "おどさないでください。", "example_meaning_cn": "请不要威吓。", "example_meaning_en": "Please don't intimidate me."},
        "N1_562": {"example_sentence": "（（威）お）ど（ど）し（し）を（を）かけ（かけ）ない（ない）で（で）ください。", "example_reading": "おどしをかけないでください。", "example_meaning_cn": "请不要威胁。", "example_meaning_en": "Please don't use threats."},
        "N1_563": {"example_sentence": "（（訪）おとず）れ（れ）て（て）ください。", "example_reading": "おとずれてください。", "example_meaning_cn": "请访问（到来）。", "example_meaning_en": "Please visit / come."},
        "N1_564": {"example_sentence": "（（衰）おとろ）え（え）さ（さ）せ（せ）ないで（で）ください。", "example_reading": "おとろえさせないでください。", "example_meaning_cn": "请不要使其衰退。", "example_meaning_en": "Please don't let it decay / weaken."},
        "N1_565": {"example_sentence": "（（恐）おど）お（お）ど（ど）し（し）ないで（で）ください。", "example_reading": "おどおどしないでください。", "example_meaning_cn": "请不要提心吊胆（战战兢兢）。", "example_meaning_en": "Please don't be nervous / timid."},
        "N1_566": {"example_sentence": "（（驚）おどろ）か（か）さ（さ）ないで（で）ください。", "example_reading": "おどろかさないでください。", "example_meaning_cn": "请不要吓我。", "example_meaning_en": "Please don't surprise me."},
        "N1_567": {"example_sentence": "（（落）おと）し（し）あ（あ）な（な）に（に）気（き）をつけ（つけ）ましょう。", "example_reading": "おとしあなにきをつけましょう。", "example_meaning_cn": "小心陷阱吧。", "example_meaning_en": "Let's be careful of pitfalls."},
        "N1_568": {"example_sentence": "（（落）おと）し（し）こ（こ）ま（ま）ないで（で）ください。", "example_reading": "おとしこまないでください。", "example_meaning_cn": "请不要陷害（或落选）。", "example_meaning_en": "Please don't entrap / fail it."},
        "N1_569": {"example_sentence": "（（落）おと）し（し）だ（だ）ま（ま）を（を）あげ（あげ）ましょう。", "example_reading": "おとしだまをあげましょう。", "example_meaning_cn": "给压岁钱吧。", "example_meaning_en": "Let's give New Year's money gifts."},
        "N1_570": {"example_sentence": "（（落）おと）し（し）も（も）の（の）を（を）届け（とどけ）まし（し）た。", "example_reading": "おとしものをとどけました。", "example_meaning_cn": "送还（上交）了失物。", "example_meaning_en": "I turned in the lost item."},
        "N1_571": {"example_sentence": "（（劣）おと）ら（ら）せ（せ）ないで（で）ください。", "example_reading": "おとらせないでください。", "example_meaning_cn": "请不要（让其劣于或变差）。", "example_meaning_en": "Please don't make it inferior / worse."},
        "N1_572": {"example_sentence": "（（同）おな）じ（じ）く（く）し（し）てください。", "example_reading": "おなじくしてください。", "example_meaning_cn": "请同样做。", "example_meaning_en": "Please do the same."},
        "N1_573": {"example_sentence": "（（同）おな）じ（じ）よ（よ）う（う）に（に）並べ（ならべ）て（て）ください。", "example_reading": "おなじようにならべてください。", "example_meaning_cn": "请同样地排列。", "example_meaning_en": "Please arrange them the same way."},
        "N1_574": {"example_sentence": "（（鬼）おに）に（に）なら（なら）ないで（で）ください。", "example_reading": "おににならないでください。", "example_meaning_cn": "请不要变成魔鬼（或拼命）。", "example_meaning_en": "Please don't be a demon / work too hard."},
        "N1_575": {"example_sentence": "（（自）おの）ず（ず）と（と）明らか（あきらか）に（に）なり（なり）ます。", "example_reading": "おのずとあきらかになります。", "example_meaning_cn": "自然而然（不言而喻）会明白的。", "example_meaning_en": "It will become clear on its own."},
        "N1_576": {"example_sentence": "（（各）おの）お（お）の（の）頑張り（がんばり）ましょう。", "example_reading": "おのおのがんばりましょう。", "example_meaning_cn": "各自努力吧。", "example_meaning_en": "Let's each do our best."},
        "N1_577": {"example_sentence": "（（帯）お）び（び）を（を）締め（しめ）て（て）ください。", "example_reading": "おびをしめてください。", "example_meaning_cn": "请系好带子（和服腰带）。", "example_meaning_en": "Please tighten the belt / sash."},
        "N1_578": {"example_sentence": "（（帯）お）び（び）き（き）だ（だ）さ（さ）ないで（で）ください。", "example_reading": "おびきださないでください。", "example_meaning_cn": "请不要引诱出来。", "example_meaning_en": "Please don't lure them out."},
        "N1_579": {"example_sentence": "（（怯）おび）え（え）さ（さ）せ（せ）ないで（で）ください。", "example_reading": "おびえさせないでください。", "example_meaning_cn": "请不要吓唬我（使其胆怯）。", "example_meaning_en": "Please don't terrify / frighten me."},
        "N1_580": {"example_sentence": "（（脅）おびや）か（か）さ（さ）ないで（で）ください。", "example_reading": "おびやかさないでください。", "example_meaning_cn": "请不要威胁（危及）。", "example_meaning_en": "Please don't threaten / endanger."},
        "N1_581": {"example_sentence": "（（夥）おびただ）し（し）い（い）数（かず）です。", "example_reading": "おびたただしいかずです。", "example_meaning_cn": "大量的（无数的）数目。", "example_meaning_en": "It's an immense / huge number."},
        "N1_582": {"example_sentence": "（（覚）おぼ）え（え）て（て）ください。", "example_reading": "おぼえてください。", "example_meaning_cn": "请记住。", "example_meaning_en": "Please remember it."},
        "N1_583": {"example_sentence": "（（溺）おぼ）れ（れ）さ（さ）せ（せ）ないで（で）ください。", "example_reading": "おぼれさせないでください。", "example_meaning_cn": "请不要让其溺水（或沉溺）。", "example_meaning_en": "Please don't let them drown / indulge."},
        "N1_584": {"example_sentence": "（（覚）おぼ）つ（つ）か（か）ない（ない）足取り（あしどり）です。", "example_reading": "おぼつかないあしどりです。", "example_meaning_cn": "踉跄（不稳）的脚步。", "example_meaning_en": "Uncertain / unsteady steps."},
        "N1_585": {"example_sentence": "（（覚）おぼ）ろ（ろ）げ（げ）な（な）記憶（きおく）です。", "example_reading": "おぼろげなきおくです。", "example_meaning_cn": "模糊（朦胧）的记忆。", "example_meaning_en": "A faint / hazy memory."},
        "N1_586": {"example_sentence": "（（向）お）も（も）む（む）き（き）を（を）感じ（かんじ）ます。", "example_reading": "おもむきをかんじます。", "example_meaning_cn": "感到情趣（风格）。", "example_meaning_en": "I feel the charm / atmosphere."},
        "N1_587": {"example_sentence": "（（思）おも）い（い）あ（あ）げ（げ）ないで（で）ください。", "example_reading": "おもいあげないでください。", "example_meaning_cn": "请不要（死心或上当）。", "example_meaning_en": "Please don't (give up hope / be deceived)."},
        "N1_588": {"example_sentence": "（（思）おも）い（い）あ（あ）た（た）り（り）ますか。", "example_reading": "おもいあたりましたか。", "example_meaning_cn": "想到了吗？（或由于记忆）。", "example_meaning_en": "Does it occur to you? / Do you recall it?"},
        "N1_589": {"example_sentence": "（（思）お内）い（い）あ（あ）ま（ま）せ（せ）て（て）ください。", "example_reading": "おもいあませてください。", "example_meaning_cn": "请深思（或内在）。", "example_meaning_en": "Please think deeply / keep it within."},
        "N1_590": {"example_sentence": "（（思）おも）い（い）あ（あ）わ（わ）せ（せ）て（て）ください。", "example_reading": "おもいあわせてください。", "example_meaning_cn": "请（结合情况）考虑。", "example_meaning_en": "Please consider it in context."},
        "N1_591": {"example_sentence": "（（思）おも）い（い）う（う）か（か）べ（べ）て（て）ください。", "example_reading": "おもいうかべてください。", "example_meaning_cn": "请回想（或使其漂浮）。", "example_meaning_en": "Please recall / call to mind."},
        "N1_592": {"example_sentence": "（（思）おも）い（い）き（き）っ（っ）て（て）やり（やり）ましょう。", "example_reading": "おもいきってやりましょう。", "example_meaning_cn": "下定决心（痛快地）做吧。", "example_meaning_en": "Let's do it with determination / boldly."},
        "N1_593": {"example_sentence": "（（思）おも）い（い）き（き）ら（ら）せ（せ）ないで（で）ください。", "example_reading": "おもいきらせないでください。", "example_meaning_cn": "请不要让我死心。", "example_meaning_en": "Please don't make me give up hope."},
        "N1_594": {"example_sentence": "（（思）おも）い（い）こ（こ）ま（ま）ないで（で）ください。", "example_reading": "おもいこまないでください。", "example_meaning_cn": "请不要（深思或执着）。", "example_meaning_en": "Please don't (brood / be obsessed)."},
        "N1_595": {"example_sentence": "（（思）おも）い（い）込ん（こん）で（て）ください。", "example_reading": "おもいこんでください。", "example_meaning_cn": "请深信（或执着）。", "example_meaning_en": "Please be convinced / think hard."},
        "N1_596": {"example_sentence": "（（思）おも）い（い）さ（さ）だ（だ）め（め）て（て）ください。", "example_reading": "おもいさだめてください。", "example_meaning_cn": "请确信（或下决心）。", "example_meaning_en": "Please make up your mind for certain."},
        "N1_597": {"example_sentence": "（（思）おも）い（い）し（し）ら（ら）せ（せ）て（て）ください。", "example_reading": "おもいしらせてください。", "example_meaning_cn": "请（给个教训）使其领悟。", "example_meaning_en": "Please teach me a lesson / make me realize."},
        "N1_598": {"example_sentence": "（（思）おも）い（い）だ（だ）し（し）て（て）ください。", "example_reading": "おもいだしてください。", "example_meaning_cn": "请想起来。", "example_meaning_en": "Please remember / recall it."},
        "N1_599": {"example_sentence": "（（立）おも）い（い）た（た）っ（っ）た（た）が（が）吉日（きちじつ）です。", "example_reading": "おもいたったがきちじつです。", "example_meaning_cn": "择日不如撞日（立即行动）。", "example_meaning_en": "Better today than tomorrow / Start immediately."},
        "N1_600": {"example_sentence": "（（思）おも）い（い）な（な）さ（さ）ないで（で）ください。", "example_reading": "おもいなさないでください。", "example_meaning_cn": "请不要（误认为或不在）。", "example_meaning_en": "Please don't (misunderstand / ignore)."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_600.")

if __name__ == "__main__":
    main()
