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
        "N2_701": {"example_sentence": "（（建）けん）せ（せ）つ（つ）し（し）て（て）ください。", "example_reading": "けんせつしてください。", "example_meaning_cn": "请建设。", "example_meaning_en": "Please construct/build it."},
        "N2_702": {"example_sentence": "（（見）けん）せ（せ）つ（つ）てき（てき）な（な）意見（いけん）を（を）出し（だし）て（て）ください。", "example_reading": "けんせつてきないけんをだしてください。", "example_meaning_cn": "请提出建设性的意见。", "example_meaning_en": "Please give constructive feedback."},
        "N2_703": {"example_sentence": "（（健）けん）ぜ（ぜ）ん（ん）な（な）遊び（あそび）をし（し）ましょう。", "example_reading": "けんぜんなあそびをしましょう。", "example_meaning_cn": "玩点健康的（健全）游戏吧。", "example_meaning_en": "Let's play wholesome games."},
        "N2_704": {"example_sentence": "（（謙）けん）そ（そ）ん（ん）し（し）ないで（で）ください。", "example_reading": "けんそんしないでください。", "example_meaning_cn": "请不要客气（谦逊）。", "example_meaning_en": "Please don't be so humble."},
        "N2_705": {"example_sentence": "（（検）けん）た（た）い（い）し（し）て（て）ください。", "example_reading": "けんたいしてください。", "example_meaning_cn": "请进行检体（化验）。", "example_meaning_en": "Please perform a specimen test."},
        "N2_706": {"example_sentence": "（（見）けん）ち（ち）を（を）広げ（ひろげ）ましょう。", "example_reading": "けんちをひろげましょう。", "example_meaning_cn": "开阔见识吧。", "example_meaning_en": "Let's broaden our views."},
        "N2_707": {"example_sentence": "（（見）けん）て（て）い（い）し（し）て（て）ください。", "example_reading": "けんていしてください。", "example_meaning_cn": "请通过检定（考试）。", "example_meaning_en": "Please take the certification test."},
        "N2_708": {"example_sentence": "（（現）げん）て（て）い（い）し（し）て（て）ください。", "example_reading": "げんていしてください。", "example_meaning_cn": "请限定（或限量）。", "example_meaning_en": "Please limit/restrict it."},
        "N2_709": {"example_sentence": "（（見）けん）と（と）う（う）を（を）つけ（つけ）て（て）ください。", "example_reading": "けんとうをつけてください。", "example_meaning_cn": "请估计（或想出办法）。", "example_meaning_en": "Please estimate/figure it out."},
        "N2_710": {"example_sentence": "（（検）けん）と（と）う（う）し（し）て（て）ください。", "example_reading": "けんとうしてください。", "example_meaning_cn": "请讨论（或研究（检讨））。", "example_meaning_en": "Please consider/examine it."},
        "N2_711": {"example_sentence": "（（現）げん）ど（ど）を（を）守り（まもり）ましょう。", "example_reading": "げんどをまもりましょう。", "example_meaning_cn": "遵守限度吧。", "example_meaning_en": "Let's stay within the limits."},
        "N2_712": {"example_sentence": "（（顕）けん）び（び）き（き）ょ（ょ）う（う）で（で）見（み）て（て）ください。", "example_reading": "けんびきょうでみてください。", "example_meaning_cn": "请用显微镜看。", "example_meaning_en": "Please look through the microscope."},
        "N2_713": {"example_sentence": "（（見）けん）ふ（ふ）つ（つ）し（し）て（て）ください。", "example_reading": "けんぶつしてください。", "example_meaning_cn": "请参观（游览）。", "example_meaning_en": "Please go sightseeing/visit."},
        "N2_714": {"example_sentence": "（（現）げん）ぶ（ぶ）つ（つ）を（を）見（み）せ（せ）て（て）ください。", "example_reading": "げんぶつをみせてください。", "example_meaning_cn": "请让我看现物（实物）。", "example_meaning_en": "Please show me the actual item."},
        "N2_715": {"example_sentence": "（（憲）けん）ほ（ほ）う（う）を（を）改正（かいせい）し（し）ます。", "example_reading": "けんぽうをかいせいします。", "example_meaning_cn": "修改宪法。", "example_meaning_en": "Amending the constitution."},
        "N2_716": {"example_sentence": "（（懸）けん）め（め）い（い）に（に）やっ（やっ）て（て）ください。", "example_reading": "けんめいにやってください。", "example_meaning_cn": "请拼命（努力）地做。", "example_meaning_en": "Please do it with all your might."},
        "N2_717": {"example_sentence": "（（賢）けん）め（め）い（い）な（な）判断（はんだん）です。", "example_reading": "けんめいなはんだんです。", "example_meaning_cn": "贤明（英明）的判断。", "example_meaning_en": "A wise/clever decision."},
        "N2_718": {"example_sentence": "（（現）げん）め（め）つ（つ）し（し）ないで（で）ください。", "example_reading": "げんめつしないでください。", "example_meaning_cn": "请不要幻灭（大失所望）。", "example_meaning_en": "Please don't be disillusioned."},
        "N2_719": {"example_sentence": "（（謙）けん）よ（よ）な（な）態度（たいど）です。", "example_reading": "けんよなたいどです。", "example_meaning_cn": "谦虚（谦虚）的态度。", "example_meaning_en": "A humble/modest attitude."},
        "N2_720": {"example_sentence": "（（現）げん）ら（ら）い（い）の（の）方法（ほうほう）を（を）続け（つづけ）ます。", "example_reading": "げんらいのほうほうをつづけます。", "example_meaning_cn": "继续（由来已久）的方法。", "example_meaning_en": "We'll continue with the existing method."},
        "N2_721": {"example_sentence": "（（限）げん）り（り）を（を）尽くし（つくし）ましょう。", "example_reading": "げんりをつくしましょう。", "example_meaning_cn": "尽力（限度）而为吧。", "example_meaning_en": "Let's do our best within the limits."},
        "N2_722": {"example_sentence": "（（原）げん）り（り）を（を）理解（りかい）し（し）て（て）ください。", "example_reading": "げんりをりかいしてください。", "example_meaning_cn": "请理解原理（原理）。", "example_meaning_en": "Please understand the principle."},
        "N2_723": {"example_sentence": "（（原）げん）り（り）ょ（ょ）う（う）を（を）調達（ちょうたつ）し（し）て（て）ください。", "example_reading": "げんりょうをちょうたつしてください。", "example_meaning_cn": "请筹措原料。", "example_meaning_en": "Please procure the raw materials."},
        "N2_724": {"example_sentence": "（（減）げん）り（り）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "げんりょうしてください。", "example_meaning_cn": "请减量（或减肥）。", "example_meaning_en": "Please reduce weight/amount."},
        "N2_725": {"example_sentence": "（（権）けん）り（り）ょ（ょ）く（く）を（を）持っ（もっ）て（て）います。", "example_reading": "けんりょくをもっています。", "example_meaning_cn": "持有权力（权力）。", "example_meaning_en": "I hold power/authority."},
        "N2_726": {"example_sentence": "（（限）げん）ろ（ろ）を（を）話し（はなし）て（て）ください。", "example_reading": "げんろをおなしてください。", "example_meaning_cn": "请说出原委（源委）。", "example_meaning_en": "Please explain the origin/circumstances."},
        "N2_727": {"example_sentence": "（（個）こ）を（を）大切（たいせつ）に（に）し（し）ましょう。", "example_reading": "こをたいせつにしましょう。", "example_meaning_cn": "珍惜个性（个人）吧。", "example_meaning_en": "Let's value the individual."},
        "N2_728": {"example_sentence": "（（恋）こい）し（し）て（て）います。", "example_reading": "こいしています。", "example_meaning_cn": "正在恋爱（或想念）。", "example_meaning_en": "I'm in love."},
        "N2_729": {"example_sentence": "（（恋）こい）しい（しい）ですね。 ", "example_reading": "こいしいですね。", "example_meaning_cn": "真怀念（想见）呢。", "example_meaning_en": "I miss it/long for it, don't I?"},
        "N2_730": {"example_sentence": "こう（（公）こう）に（に）しましょう。", "example_reading": "こうにしましょう。", "example_meaning_cn": "公开吧。", "example_meaning_en": "Let's make it public."},
        "N2_731": {"example_sentence": "こう（（工）こう）を（を）急ぎ（いそぎ）ましょう。", "example_reading": "こうをいそぎましょう。", "example_meaning_cn": "赶工（工程）吧。", "example_meaning_en": "Let's speed up the construction/work."},
        "N2_732": {"example_sentence": "（（乞）こ）う（う）ご（ご）期待（きたい）！ ", "example_reading": "こうごきたい！", "example_meaning_cn": "敬请期待（乞期待）！", "example_meaning_en": "Please look forward to it!"},
        "N2_733": {"example_sentence": "（（孝）こう）こ（こ）う（う）し（し）て（て）ください。", "example_reading": "こうこうしてください。", "example_meaning_cn": "请尽孝心（孝行）。", "example_meaning_en": "Please be filial."},
        "N2_734": {"example_sentence": "こう（（好）こう）を（を）見（み）て（て）ください。", "example_reading": "こうをみててください。", "example_meaning_cn": "请看好事情（项）。", "example_meaning_en": "Please look at the item/point."},
        "N2_735": {"example_sentence": "こう（（厚）こう）を（を）受け（うけ）て（て）います。", "example_reading": "こうをうけています。", "example_meaning_cn": "受到了厚待（恩惠）。", "example_meaning_en": "I'm receiving your kindness/favor."},
        "N2_736": {"example_sentence": "こう（（香）こう）を（を）焚い（たい）て（て）ください。", "example_reading": "こうをたいてください。", "example_meaning_cn": "请焚香。", "example_meaning_en": "Please burn incense."},
        "N2_737": {"example_sentence": "（（高）こう）か（か）な（な）品（しな）です。", "example_reading": "こうかなしなです。", "example_meaning_cn": "高价（贵重）的物品。", "example_meaning_en": "It's an expensive/valuable item."},
        "N2_738": {"example_sentence": "こう（（降）こう）か（か）し（し）て（て）ください。", "example_reading": "こうかしてください。", "example_meaning_cn": "请降下。", "example_meaning_en": "Please descend."},
        "N2_739": {"example_sentence": "こう（（広）こう）か（か）く（く）で（で）撮っ（とっ）て（て）ください。", "example_reading": "こうかくでとってください。", "example_meaning_cn": "请用广角拍摄。", "example_meaning_en": "Please take a photo with a wide angle."},
        "N2_740": {"example_sentence": "こう（（後）こう）か（か）い（い）し（し）ないで（で）ください。", "example_reading": "こうかいしないでください。", "example_meaning_cn": "请不要后悔。", "example_meaning_en": "Please don't regret it."},
        "N2_741": {"example_sentence": "こう（（公）こう）か（か）い（い）し（し）て（て）ください。", "example_reading": "こうかいしてください。", "example_meaning_cn": "请公开。", "example_meaning_en": "Please make it public."},
        "N2_742": {"example_sentence": "こう（（航）こう）か（か）い（い）に（に）出（で）ます。", "example_reading": "こうかいにでます。", "example_meaning_cn": "出航（航海）。", "example_meaning_en": "Setting sail/going on a voyage."},
        "N2_743": {"example_sentence": "こう（（工）こう）か（か）を（を）見（み）て（て）ください。", "example_reading": "こうかをみてください。", "example_meaning_cn": "请看工科（或效果）。", "example_meaning_en": "Please see the effect/result."},
        "N2_744": {"example_sentence": "こう（（交）こう）か（か）ん（ん）し（し）て（て）ください。", "example_reading": "こうかんしてください。", "example_meaning_cn": "请交换。", "example_meaning_en": "Please exchange/swap it."},
        "N2_745": {"example_sentence": "こう（（講）こう）ぎ（ぎ）を（を）聴い（きい）て（て）ください。", "example_reading": "こうぎをきいてください。", "example_meaning_cn": "请听讲义。", "example_meaning_en": "Please listen to the lecture."},
        "N2_746": {"example_sentence": "こう（（抗）こう）ぎ（ぎ）し（し）て（て）ください。", "example_reading": "こうぎしてください。", "example_meaning_cn": "请抗议。", "example_meaning_en": "Please protest."},
        "N2_747": {"example_sentence": "こう（（好）こう）き（き）を（を）逃さ（のがさ）ないで（で）ください。", "example_reading": "こうきをのがさないでください。", "example_meaning_cn": "请不要错失好机。", "example_meaning_en": "Please don't miss the good opportunity."},
        "N2_748": {"example_sentence": "こう（（高）こう）き（き）な（な）身分（みぶん）です。", "example_reading": "こうきなみぶんです。", "example_meaning_cn": "高贵的身份。", "example_meaning_en": "A noble status."},
        "N2_749": {"example_sentence": "こう（（工）こう）ぎ（ぎ）ょ（ょ）う（う）を（を）振興（しんこう）し（し）ましょう。", "example_reading": "こうぎょうをしんこうしましょう。", "example_meaning_cn": "振兴工业吧。", "example_meaning_en": "Let's promote industry."},
        "N2_750": {"example_sentence": "こう（（興）こう）ぎ（ぎ）ょ（ょ）う（う）を（を）見（み）に（に）行き（いき）ましょう。", "example_reading": "こうぎょうをみにいきましょう。", "example_meaning_cn": "去看演出（兴行）吧。", "example_meaning_en": "Let's go watch the performance."},
        "N2_751": {"example_sentence": "こう（（航）こう）く（く）う（う）き（き）に（に）乗り（のり）ます。", "example_reading": "こうくうきにのります。", "example_meaning_cn": "乘飞机（航空机）。", "example_meaning_en": "I'm boarding the aircraft."},
        "N2_752": {"example_sentence": "こう（（光）光）け（け）い（い）を（を）見（み）て（て）ください。", "example_reading": "こうけいをみてください。", "example_meaning_cn": "请看这幅光景（景象）。", "example_meaning_en": "Please look at this scene."},
        "N2_753": {"example_sentence": "こう（（合）こう）け（け）い（い）し（し）て（て）ください。", "example_reading": "こうけいしてください。", "example_meaning_cn": "请合计。", "example_meaning_en": "Please sum it up."},
        "N2_754": {"example_sentence": "こう（（後）こう）け（け）い（い）し（し）て（て）ください。", "example_reading": "こうけいしてください。", "example_meaning_cn": "请继任（后继）。", "example_meaning_en": "Please succeed/follow up."},
        "N2_755": {"example_sentence": "こう（（巧）こう）げ（げ）な（な）仕事（しごと）です。", "example_reading": "こうげなしごとです。", "example_meaning_cn": "精巧（巧妙）的工作。", "example_meaning_en": "A skillful/clever job."},
        "N2_756": {"example_sentence": "こう（（工）こう）げ（げ）い（い）し（し）て（て）ください。", "example_reading": "こうげいしてください。", "example_meaning_cn": "请展现工艺。", "example_meaning_en": "Please show your craft/art."},
        "N2_757": {"example_sentence": "こう（（攻）こう）げ（げ）き（き）し（し）ないで（で）ください！ ", "example_reading": "こうげきしないでください！", "example_meaning_cn": "请不要攻击！", "example_meaning_en": "Please don't attack!"},
        "N2_758": {"example_sentence": "こう（（格子）こうし）の（の）向こう（むこう）です。", "example_reading": "こうしのむこうです。", "example_meaning_cn": "格子窗（或栅栏）的对面。", "example_meaning_en": "Beyond the lattice/bars."},
        "N2_759": {"example_sentence": "こう（（公）こう）し（し）を（を）分（わ）け（け）て（て）ください。", "example_reading": "こうしをわけてください。", "example_meaning_cn": "请公私分明。", "example_meaning_en": "Please separate public and private matters."},
        "N2_760": {"example_sentence": "こう（（講）こう）し（し）になり（なり）たい（たい）です。", "example_reading": "こうしになりたいです。", "example_meaning_cn": "想当讲师。", "example_meaning_en": "I want to become a lecturer."},
        "N2_761": {"example_sentence": "こう（（厚）こう）し（し）な（な）人（ひと）です。", "example_reading": "こうしなひとです。", "example_meaning_cn": "厚道（厚志）的人。", "example_meaning_en": "A kind/generous person."},
        "N2_762": {"example_sentence": "こう（（行）こう）し（し）て（て）ください。", "example_reading": "こうしてください。", "example_meaning_cn": "请行使（权力等）。", "example_meaning_en": "Please exercise/wield it."},
        "N2_763": {"example_sentence": "こう（（後）こう）し（し）ゃ（ゃ）を（を）選ん（えらん）で（て）ください。", "example_reading": "こうしゃをえらんでください。", "example_meaning_cn": "请选择后者。", "example_meaning_en": "Please choose the latter."},
        "N2_764": {"example_sentence": "こう（（校）こう）し（し）ゃ（ゃ）を（を）見（み）て（て）ください。", "example_reading": "こうしゃをみてください。", "example_meaning_cn": "请看校舍。", "example_meaning_en": "Please look at the school building."},
        "N2_765": {"example_sentence": "こう（（公）こう）し（し）ゅう（ゅう）で（で）話し（はなし）ましょう。", "example_reading": "こうしゅうではなしましょう。", "example_meaning_cn": "在公众（大众）场合说吧。", "example_meaning_en": "Let's talk in public."},
        "N2_766": {"example_sentence": "こう（（講）こう）し（し）ゅう（ゅう）を（を）受け（うけ）て（て）ください。", "example_reading": "こうしゅうをうけてください。", "example_meaning_cn": "请接受讲习。", "example_meaning_en": "Please receive the training."},
        "N2_767": {"example_sentence": "こう（（功）こう）し（し）ょ（ょ）う（う）を（を）称え（たたえ）ましょう。", "example_reading": "こうしょうをたたえましょう。", "example_meaning_cn": "称赞功勋（或高尚）吧。", "example_meaning_en": "Let's laud the high merit/achievement."},
        "N2_768": {"example_sentence": "こう（（公）こう）し（し）ょう（ょう）し（し）て（て）ください。", "example_reading": "こうしょうしてください。", "example_meaning_cn": "请交涉。", "example_meaning_en": "Please negotiate."},
        "N2_769": {"example_sentence": "こう（（向）こう）じ（じ）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "こうじょうしてください。", "example_meaning_cn": "请向上（提高）。", "example_meaning_en": "Please improve/make progress."},
        "N2_770": {"example_sentence": "こう（（工）こう）じ（じ）ょう（ょう）に（に）行き（いき）ます。", "example_reading": "こうじょうにいきます。", "example_meaning_cn": "去工厂。", "example_meaning_en": "I'm going to the factory."},
        "N2_771": {"example_sentence": "こう（（公）こう）せい（せい）に（に）判断（はんだん）し（し）てください。", "example_reading": "こうせいにはんだんしてください。", "example_meaning_cn": "请公正地判断。", "example_meaning_en": "Please judge fairly."},
        "N2_772": {"example_sentence": "こう（（後）こう）せい（せい）に（に）残し（のこし）ましょう。", "example_reading": "こうせいにのこしましょう。", "example_meaning_cn": "留给后世（后生）吧。", "example_meaning_en": "Let's leave it for future generations."},
        "N2_773": {"example_sentence": "こう（（功）こう）せ（せ）き（き）を（を）認め（みとめ）てください。", "example_reading": "こうせきをみとめてください。", "example_meaning_cn": "请承认功绩。", "example_meaning_en": "Please acknowledge the achievement/merit."},
        "N2_774": {"example_sentence": "こう（（光）こう）せ（せ）ん（ん）を（を）放っ（はなっ）て（て）ください。", "example_reading": "こうせんをはなってください。", "example_meaning_cn": "请发射光线。", "example_meaning_en": "Please emit a beam of light."},
        "N2_775": {"example_sentence": "こう（（交）こう）せ（せ）ん（ん）し（し）て（て）ください。", "example_reading": "こうせんしてください。", "example_meaning_cn": "请作战（交战）。", "example_meaning_en": "Please engage in battle."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N2_775.")

if __name__ == "__main__":
    main()
