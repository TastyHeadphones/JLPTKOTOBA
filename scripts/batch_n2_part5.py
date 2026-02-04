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
        "N2_551": {"example_sentence": "きょく（（極）きょく）たんば（な）考（かんが）え（え）は（は）避け（さけ）ましょう。", "example_reading": "きょくたんなかんがえわさけましょう。", "example_meaning_cn": "避开极端的想法吧。", "example_meaning_en": "Let's avoid extreme thinking."},
        "N2_552": {"example_sentence": "（（居）きょ）じ（じ）ゅう（ゅう）し（し）て（て）ください。", "example_reading": "きょじゅうしてください。", "example_meaning_cn": "请居住。", "example_meaning_en": "Please reside/dwell there."},
        "N2_553": {"example_sentence": "（（巨）きょ）だ（だ）い（い）な（な）岩（いわ）があり（あり）ます。", "example_reading": "きょだいな岩があります。", "example_meaning_cn": "有一块巨大的岩石。", "example_meaning_en": "There is a huge rock."},
        "N2_554": {"example_sentence": "（（拒）きょ）ふ（ふ）し（し）ないで（で）ください。", "example_reading": "きょふしないでください。", "example_meaning_cn": "请不要拒绝。", "example_meaning_en": "Please don't refuse."},
        "N2_555": {"example_sentence": "（（許）きょ）よう（よう）はん（ん）い（い）です。", "example_reading": "きょようはんいです。", "example_meaning_cn": "在许可（容许）范围内。", "example_meaning_en": "It's within the allowable range."},
        "N2_556": {"example_sentence": "（（距）きょ）り（り）を（を）置い（おい）て（て）ください。", "example_reading": "きょりをおいてください。", "example_meaning_cn": "请保持距离。", "example_meaning_en": "Please keep your distance."},
        "N2_557": {"example_sentence": "（（魚）ぎょ）る（る）い（い）を（を）食べ（たべ）ましょう。", "example_reading": "ぎょるいをたべましょう。", "example_meaning_cn": "吃点鱼类吧。", "example_meaning_en": "Let's eat some fish."},
        "N2_558": {"example_sentence": "（（嫌）きら）わ（わ）ないで（で）ください。", "example_reading": "きらわないでください。", "example_meaning_cn": "请不要讨厌。", "example_meaning_en": "Please don't hate/dislike it."},
        "N2_559": {"example_sentence": "（（切）き）り（り）か（か）え（え）て（て）ください。", "example_reading": "きりかえてください。", "example_meaning_cn": "请切换（或改变心情）。", "example_meaning_en": "Please switch over/change your mindset."},
        "N2_560": {"example_sentence": "（（切）き）り（り）さ（さ）げ（げ）て（て）ください。", "example_reading": "きりさげてください。", "example_meaning_cn": "请削减（或降低）。", "example_meaning_en": "Please cut back/lower it."},
        "N2_561": {"example_sentence": "（（切）き）り（り）は（は）な（な）し（し）て（て）ください。", "example_reading": "きりはなしてください。", "example_meaning_cn": "请切断（或拆开）。", "example_meaning_en": "Please disconnect/separate it."},
        "N2_562": {"example_sentence": "（（切）き）り（り）び（び）な（な）お（お）し（し）て（て）ください。", "example_reading": "きりびなおしてください。", "example_meaning_cn": "请重新开始（剪开）。", "example_meaning_en": "Please cut it again/start over."},
        "N2_563": {"example_sentence": "き（（際）ぎ）わ（わ）ど（ど）い（い）質問（しつもん）です。", "example_reading": "きわどいしつもんです。", "example_meaning_cn": "微妙（或危险）的问题。", "example_meaning_en": "A risky/delicate question."},
        "N2_564": {"example_sentence": "（（極）きわ）め（め）て（て）ください。", "example_reading": "きわめてください。", "example_meaning_cn": "请达到极点（或极其）。", "example_meaning_en": "Please master it/it's extremely..."},
        "N2_565": {"example_sentence": "（（菌）きん）が（が）増え（ふえ）て（て）います。", "example_reading": "きんがふえています。", "example_meaning_cn": "细菌增加了。", "example_meaning_en": "Bacteria are increasing."},
        "N2_566": {"example_sentence": "きん（（金）きん）が（が）欲しい（ほしい）です。", "example_reading": "きんがほしいです。", "example_meaning_cn": "想要金子。", "example_meaning_en": "I want gold."},
        "N2_567": {"example_sentence": "きん（（銀）ぎん）の（の）メダル（めたる）です。", "example_reading": "ぎんのめたるです。", "example_meaning_cn": "银牌。", "example_meaning_en": "It's a silver medal."},
        "N2_568": {"example_sentence": "きん（（禁）きん）え（え）ん（ん）し（し）て（て）ください。", "example_reading": "きんえんしてください。", "example_meaning_cn": "请戒烟。", "example_meaning_en": "Please stop smoking."},
        "N2_569": {"example_sentence": "きん（（金）きん）が（が）く（く）を（を）教えて（おしえて）ください。", "example_reading": "きんがくをおしえてください。", "example_meaning_cn": "请告诉我金额。", "example_meaning_en": "Please tell me the amount."},
        "N2_570": {"example_sentence": "きん（（緊）きん）き（き）ゅう（ゅう）事態（じたい）です！ ", "example_reading": "きんきゅうじたいです！", "example_meaning_cn": "紧急情况！", "example_meaning_en": "It's an emergency!"},
        "N2_571": {"example_sentence": "きん（（近）きん）じょ（じょ）の（の）人（ひと）です。", "example_reading": "きんじょのひとです。", "example_meaning_cn": "邻居。", "example_meaning_en": "It's a neighbor."},
        "N2_572": {"example_sentence": "きん（（近）きん）し（し）ん（ん）な（な）態度（たいど）です。", "example_reading": "きんしんなたいどです。", "example_meaning_cn": "谨严（或闭门思过）的态度。", "example_meaning_en": "A discrete/humble attitude."},
        "N2_573": {"example_sentence": "（（筋）きん）じょ（じょ）を（を）鍛え（きたえ）ましょう。", "example_reading": "きんじょをきたえましょう。", "example_meaning_cn": "锻炼肌肉（筋骨）吧。", "example_meaning_en": "Let's train our muscles."},
        "N2_574": {"example_sentence": "きん（（近）きん）だい（だい）てき（てき）な（な）建物（たてもの）です。", "example_reading": "きんだいてきなたてものです。", "example_meaning_cn": "近代的建筑。", "example_meaning_en": "It's a modern building."},
        "N2_575": {"example_sentence": "きん（（緊）きん）ちょう（ちょう）し（し）ないで（で）ください。", "example_reading": "きんちょうしないでください。", "example_meaning_cn": "请不要紧张。", "example_meaning_en": "Please don't be nervous."},
        "N2_576": {"example_sentence": "きん（（近）きん）に（に）ゅ（ゅ）う（う）し（し）て（て）ください。", "example_reading": "きんにゅうしてください。", "example_meaning_cn": "请侵入（或记入）。", "example_meaning_en": "Please enter/intrude."},
        "N2_577": {"example_sentence": "きん（（勤）きん）む（む）し（し）て（て）います。", "example_reading": "きんむしています。", "example_meaning_cn": "正在上班（任职）。", "example_meaning_en": "I'm on duty/working."},
        "N2_578": {"example_sentence": "きん（（金）きん）り（り）を（を）計算（けいさん）し（し）てください。", "example_reading": "きんりをけいさんしてください。", "example_meaning_cn": "请计算利息。", "example_meaning_en": "Please calculate the interest rate."},
        "N2_579": {"example_sentence": "（（句）く）を（を）詠ん（よん）で（て）ください。", "example_reading": "くをよんでください。", "example_meaning_cn": "请作（咏）句。", "example_meaning_en": "Please compose a haiku/phrase."},
        "N2_580": {"example_sentence": "（（苦）く）を（を）共に（ともに）し（し）ましょう。", "example_reading": "くをともにしましょう。", "example_meaning_cn": "同甘共苦吧。", "example_meaning_en": "Let's share our hardships."},
        "N2_581": {"example_sentence": "（（食）く）い（い）ち（ち）が（が）って（て）います。", "example_reading": "くいちがっています。", "example_meaning_cn": "分歧（或说走嘴）了。", "example_meaning_en": "There's a discrepancy/clash."},
        "N2_582": {"example_sentence": "（（空）くう）き（き）を（を）入れ（いれ）て（て）ください。", "example_reading": "くうきをいれてください。", "example_meaning_cn": "请打气（或换气）。", "example_meaning_en": "Please pump in air/ventilate."},
        "N2_583": {"example_sentence": "（（空）くう）ぐ（ぐ）ん（ん）に（に）入り（はいり）たい（たい）です。", "example_reading": "くうぐんにはいりたいです。", "example_meaning_cn": "想加入空军。", "example_meaning_en": "I want to join the Air Force."},
        "N2_584": {"example_sentence": "（（空）くう）こ（こ）う（う）に（に）行き（いき）ましょう。", "example_reading": "くうこうにいきましょう。", "example_meaning_cn": "去机场吧。", "example_meaning_en": "Let's go to the airport."},
        "N2_585": {"example_sentence": "（（空）くう）ち（ち）ゅう（ゅう）を（を）飛び（とび）たい（たい）です。", "example_reading": "くうちゅうをとびたいです。", "example_meaning_cn": "想在空中飞。", "example_meaning_en": "I want to fly in the air."},
        "N2_586": {"example_sentence": "（（茎）くき）を（を）切ら（きら）ないで（で）ください。", "example_reading": "くきをきらないでください。", "example_meaning_cn": "请不要割断茎。", "example_meaning_en": "Please don't cut the stem."},
        "N2_587": {"example_sentence": "（（区）く）ぎ（ぎ）り（り）を（を）つけ（つけ）て（て）ください。", "example_reading": "くぎりをつけいてください。", "example_meaning_cn": "请做个交代（或划分）。", "example_meaning_en": "Please make a clear division/break."},
        "N2_588": {"example_sentence": "（（潜）くぐ）っ（っ）て（て）ください。", "example_reading": "くぐってください。", "example_meaning_cn": "请钻过去（或潜过）。", "example_meaning_en": "Please pass under/dive through."},
        "N2_589": {"example_sentence": "（（草）くさ）を（を）取っ（とっ）て（て）ください。", "example_reading": "くさをとってください。", "example_meaning_cn": "请拔草。", "example_meaning_en": "Please pull the weeds."},
        "N2_590": {"example_sentence": "（（鎖）くさり）を（を）外し（はずし）て（て）ください。", "example_reading": "くさりをはずしてください。", "example_meaning_cn": "请解开锁链。", "example_meaning_en": "Please unchain it."},
        "N2_591": {"example_sentence": "（（腐）くさ）っ（っ）て（て）いますか。", "example_reading": "くさっていますか。", "example_meaning_cn": "腐烂（或变质）了吗？", "example_meaning_en": "Is it rotten/spoiled?"},
        "N2_592": {"example_sentence": "（（癖）くせ）に（に）なり（なり）ますね。", "example_reading": "くせになりますね。", "example_meaning_cn": "真会上瘾（成习惯）呢。", "example_meaning_en": "It becomes a habit, doesn't it?"},
        "N2_593": {"example_sentence": "（（口）くち）ず（ず）さ（さ）んで（て）ください。", "example_reading": "くちずさんでください。", "example_meaning_cn": "请哼唱（或吟诵）。", "example_meaning_en": "Please hum/chant it."},
        "N2_594": {"example_sentence": "（（唇）くちびる）を（を）噛ま（かま）ないで（で）ください。", "example_reading": "くちびるをかまないでください。", "example_meaning_cn": "请不要咬嘴唇。", "example_meaning_en": "Please don't bite your lip."},
        "N2_595": {"example_sentence": "（（口）くち）べ（べ）に（に）を（を）塗っ（ぬっ）て（て）ください。", "example_reading": "くちべにをぬってください。", "example_meaning_cn": "请涂口红。", "example_meaning_en": "Please put on lipstick."},
        "N2_596": {"example_sentence": "（（苦）く）つ（つ）う（う）を（を）和らげ（やわらげ）て（て）ください。", "example_reading": "くつうをやわらげてください。", "example_meaning_cn": "请减轻痛苦。", "example_meaning_en": "Please alleviate the pain."},
        "N2_597": {"example_sentence": "（（苦）く）っ（っ）せ（せ）つ（つ）し（し）ないで（で）ください。", "example_reading": "くっせつしないでください。", "example_meaning_cn": "请不要屈折（或折射）。", "example_meaning_en": "Please don't be refracted/curved."},
        "N2_598": {"example_sentence": "（（配）くば）っ（っ）て（て）ください。", "example_reading": "くばってください。", "example_meaning_cn": "请分发。", "example_meaning_en": "Please distribute them."},
        "N2_599": {"example_sentence": "（（首）くび）を（を）振ら（ふら）ないで（で）ください。", "example_reading": "くびをふらないでください。", "example_meaning_cn": "请不要摇头。", "example_meaning_en": "Please don't shake your head."},
        "N2_600": {"example_sentence": "（（足）く）び（び）き（き）を（を）外し（はずし）て（て）ください。", "example_reading": "くびきをはずしてください。", "example_meaning_cn": "请解开枷锁（轭）。", "example_meaning_en": "Please unyoke/free it."},
        "N2_601": {"example_sentence": "（（工夫）くふう）し（し）て（て）ください。", "example_reading": "くふうしてください。", "example_meaning_cn": "请开动脑筋（下工夫）。", "example_meaning_en": "Please devise a way/innovate."},
        "N2_602": {"example_sentence": "（（区分）くぶん）し（し）て（て）ください。", "example_reading": "くぶんしてください。", "example_meaning_cn": "请划分（区分）。", "example_meaning_en": "Please classify/divide it."},
        "N2_603": {"example_sentence": "（（組合）くみあい）に（に）入り（はいり）ましょう。", "example_reading": "くみあいにはいりましょう。", "example_meaning_cn": "加入工会（组合）吧。", "example_meaning_en": "Let's join the union."},
        "N2_604": {"example_sentence": "（（組み）くみ）合わせ（あわせ）を（を）考え（かんがえ）て（て）ください。", "example_reading": "くみあわせをかんがえてください。", "example_meaning_cn": "请考虑组合。", "example_meaning_en": "Please think about the combination."},
        "N2_605": {"example_sentence": "（（組み）くみ）立て（たて）て（て）ください。", "example_reading": "くみたててください。", "example_meaning_cn": "请组装。", "example_meaning_en": "Please assemble it."},
        "N2_606": {"example_sentence": "（（配）くば）る（る）声（こえ）に（に）気（き）をつけ（つけ）ましょう。", "example_reading": "くばるこえにきをつけましょう。", "example_meaning_cn": "注意分配的声音（语气）吧。", "example_meaning_en": "Mind your tone of distribution."},
        "N2_607": {"example_sentence": "（（悔）くや）しい（しい）ですね！ ", "example_reading": "くやしいですね！", "example_meaning_cn": "真令人气愤（或不甘心）呢！", "example_meaning_en": "How frustrating!"},
        "N2_608": {"example_sentence": "（（悔）くや）んで（て）ください。", "example_reading": "くやんでください。", "example_meaning_cn": "请哀悼（或后悔）。", "example_meaning_en": "Please mourn/regret it."},
        "N2_609": {"example_sentence": "く（くら）い（い）ですね。 ", "example_reading": "くらいですね。", "example_meaning_cn": "真够暗（或阴沉）的呢。", "example_meaning_en": "It's dark/gloomy, isn't it?"},
        "N2_610": {"example_sentence": "（（暮）く）らし（し）を（を）整え（ととのえ）ましょう。", "example_reading": "くらしをととのえましょう。", "example_meaning_cn": "打理生活吧。", "example_meaning_en": "Let's organize our lives."},
        "N2_611": {"example_sentence": "（（暮）く）ら（ら）し（し）て（て）ください。", "example_reading": "くらしてください。", "example_meaning_cn": "请生活。", "example_meaning_en": "Please live/reside."},
        "N2_612": {"example_sentence": "（（比）くら）べ（べ）て（て）ください。", "example_reading": "くらべてください。", "example_meaning_cn": "请比较。", "example_meaning_en": "Please compare."},
        "N2_613": {"example_sentence": "（（狂）くる）わせ（せ）ないで（で）ください。", "example_reading": "くるわせないでください。", "example_meaning_cn": "请不要（把计划等）打乱。", "example_meaning_en": "Please don't mess it up/disturb it."},
        "N2_614": {"example_sentence": "（（苦）くる）し（し）ま（ま）ないで（で）ください。", "example_reading": "くるしまないでください。", "example_meaning_cn": "请不要痛苦。", "example_meaning_en": "Please don't suffer."},
        "N2_615": {"example_sentence": "（（苦）くる）しい（しい）です。", "example_reading": "くるしいです。", "example_meaning_cn": "好痛苦（或艰难）。", "example_meaning_en": "I'm in pain/suffering."},
        "N2_616": {"example_sentence": "（（狂）くる）っ（っ）て（て）います。", "example_reading": "くるっています。", "example_meaning_cn": "正发狂（或出故障）呢。", "example_meaning_en": "It's crazy/out of order."},
        "N2_617": {"example_sentence": "（（包）くる）んで（て）ください。", "example_reading": "くるんでください。", "example_meaning_cn": "请包裹起来。", "example_meaning_en": "Please wrap it up."},
        "N2_618": {"example_sentence": "く（（車）くるま）椅（い）子（し）を（を）押し（おし）ます。", "example_reading": "くるまいすをおします。", "example_meaning_cn": "推轮椅。", "example_meaning_en": "Pushing a wheelchair."},
        "N2_619": {"example_sentence": "（（暮）く）れ（れ）ないで（で）ください。", "example_reading": "くれないでください。", "example_meaning_cn": "天请不要黑（或请不要给）。", "example_meaning_en": "Please don't get dark/don't give."},
        "N2_620": {"example_sentence": "（（苦）く）ろ（ろ）う（う）し（し）まし（し）た。", "example_reading": "くろうしました。", "example_meaning_cn": "辛苦了（受累了）。", "example_meaning_en": "I've had a hard time/worked hard."},
        "N2_621": {"example_sentence": "（（加）くわ）え（え）て（て）ください。", "example_reading": "くわえてください。", "example_meaning_cn": "请加上（或叼着）。", "example_meaning_en": "Please add it/hold it in your mouth."},
         "N2_622": {"example_sentence": "（（加）くわ）わ（わ）っ（っ）て（て）ください。", "example_reading": "くわわってください。", "example_meaning_cn": "请加入（参加）。", "example_meaning_en": "Please join in."},
        "N2_623": {"example_sentence": "（（詳）くわ）しい（しい）ですね！ ", "example_reading": "くわしいですね！", "example_meaning_cn": "真够详细（或了解）的呢！", "example_meaning_en": "You're very knowledgeable/detailed!"},
        "N2_624": {"example_sentence": "（（企）くわだ）て（て）を（を）話し（はなし）て（て）ください。", "example_reading": "くわだてをななしてください。", "example_meaning_cn": "请说一下企划（打算）。", "example_meaning_en": "Please tell me the plan."},
        "N2_625": {"example_sentence": "（（軍）ぐん）に（に）入り（はいり）たい（たい）です。", "example_reading": "ぐんにはいりたいです。", "example_meaning_cn": "想参军。", "example_meaning_en": "I want to join the military."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N2_625.")

if __name__ == "__main__":
    main()
