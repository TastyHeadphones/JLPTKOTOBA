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
        "N2_626": {"example_sentence": "（（軍）ぐん）えい（えい）し（し）て（て）ください。", "example_reading": "ぐんえいしてください。", "example_meaning_cn": "请进行军营（营地）建设（经营）。", "example_meaning_en": "Please manage/operate the military camp."},
        "N2_627": {"example_sentence": "（（軍）ぐん）じ（じ）き（き）ょう（ょう）だ（だ）い（い）です。", "example_reading": "ぐんじきょうだいです。", "example_meaning_cn": "军事强大。", "example_meaning_en": "Military strength is great."},
        "N2_628": {"example_sentence": "（（軍）ぐん）た（た）い（い）に（に）入り（はいり）ます。", "example_reading": "ぐんたいにはいります。", "example_meaning_cn": "入伍（加入军队）。", "example_meaning_en": "I'm joining the army."},
        "N2_629": {"example_sentence": "（（訓練）くんれん）し（し）て（て）ください。", "example_reading": "くんれんしてください。", "example_meaning_cn": "请训练。", "example_meaning_en": "Please train/drill."},
        "N2_630": {"example_sentence": "（（下）げ）が（が）あり（あり）ますか。", "example_reading": "げがありますか。", "example_meaning_cn": "有下方（或卑贱）的吗？", "example_meaning_en": "Is there a lower/inferior part?"},
        "N2_631": {"example_sentence": "（（家）け）い（い）あ（あ）い（い）し（し）て（て）ください。", "example_reading": "けいあいしてください。", "example_meaning_cn": "请敬爱（敬佩）。", "example_meaning_en": "Please respect and love them."},
        "N2_632": {"example_sentence": "（（刑）け）い（い）き（き）を（を）終え（おえ）まし（し）た。", "example_reading": "けいきをおえました。", "example_meaning_cn": "服完刑了。", "example_meaning_en": "I've served my sentence."},
        "N2_633": {"example_sentence": "（（景）け）い（い）き（き）が（が）いい（いい）ですね。", "example_reading": "けいきがいいですね。", "example_meaning_cn": "生意兴隆（景气好）呢。", "example_meaning_en": "The economy/business is good, isn't it?"},
        "N2_634": {"example_sentence": "（（経）け）い（い）け（け）い（い）な（な）態度（たいど）です。", "example_reading": "けいけいなたいどです。", "example_meaning_cn": "轻率（或草率）的态度。", "example_meaning_en": "A light/careless attitude."},
        "N2_635": {"example_sentence": "（（経）け）い（い）け（け）ん（ん）が（が）あり（あり）ますか。", "example_reading": "けいけんがありますか。", "example_meaning_cn": "有经验吗？", "example_meaning_en": "Do you have experience?"},
        "N2_636": {"example_sentence": "（（慶）け）い（い）こ（こ）う（う）を（を）祝っ（いわっ）て（て）ください。", "example_reading": "けいこうをいわってください。", "example_meaning_cn": "请祝贺喜庆的事。", "example_meaning_en": "Please celebrate the happy occasion."},
        "N2_637": {"example_sentence": "（（継）け）い（い）ぞ（ぞ）く（く）し（し）て（て）ください。", "example_reading": "けいぞくしてください。", "example_meaning_cn": "请继续（持续）。", "example_meaning_en": "Please continue/persist."},
        "N2_638": {"example_sentence": "（（形）け）い（い）たい（たい）を（を）持ち（もち）ます。", "example_reading": "けいたいをもちます。", "example_meaning_cn": "携带（手机）。", "example_meaning_en": "I carry a mobile phone."},
        "N2_639": {"example_sentence": "（（警）け）い（い）ちょう（ちょう）し（し）て（て）ください。", "example_reading": "けいちょうしてください。", "example_meaning_cn": "请倾听（警听）。", "example_meaning_en": "Please listen carefully."},
        "N2_640": {"example_sentence": "（（景）け）い（い）ど（ど）を（を）測っ（はかっ）て（て）ください。", "example_reading": "けいどをはかってください。", "example_meaning_cn": "请测量经度。", "example_meaning_en": "Please measure the longitude."},
        "N2_641": {"example_sentence": "（（系）け）い（い）と（と）う（う）だ（だ）て（て）て（て）ください。", "example_reading": "けいとうだててください。", "example_meaning_cn": "请系统化。", "example_meaning_en": "Please systematize it."},
        "N2_642": {"example_sentence": "（（経）け）い（い）ど（ど）を（を）守り（まもり）ましょう。", "example_reading": "けいどをまもりましょう。", "example_meaning_cn": "遵守经度（或规则）吧。", "example_meaning_en": "Let's respect the rules/norms."},
        "N2_643": {"example_sentence": "（（軽）け）い（い）べ（べ）つ（つ）し（し）ないで（で）ください。", "example_reading": "けいべつしないでください。", "example_meaning_cn": "请不要轻视（蔑视）。", "example_meaning_en": "Please don't despise/scorn them."},
        "N2_644": {"example_sentence": "（（刑）け）い（い）む（む）し（し）ょ（ょ）に（に）行き（いき）ます。", "example_reading": "けいむしょにいきます。", "example_meaning_cn": "去监狱。", "example_meaning_en": "I'm going to prison."},
        "N2_645": {"example_sentence": "（（契）け）い（い）やく（やく）し（し）て（て）ください。", "example_reading": "けいやくしてください。", "example_meaning_cn": "请签约。", "example_meaning_en": "Please sign the contract."},
        "N2_646": {"example_sentence": "（（経）け）い（い）ゆ（ゆ）し（し）て（て）ください。", "example_reading": "けいゆしてください。", "example_meaning_cn": "请经由（或中转）。", "example_meaning_en": "Please go via/through."},
        "N2_647": {"example_sentence": "（（敬）け）い（い）よ（よ）を（を）払い（はらい）ましょう。", "example_reading": "けいよをはらいましょう。", "example_meaning_cn": "表示敬意吧。", "example_meaning_en": "Let's pay our respects."},
        "N2_648": {"example_sentence": "（（経）け）い（い）り（り）を（を）任せ（まかせ）ます。", "example_reading": "けいりをまかせます。", "example_meaning_cn": "交由会计处理。", "example_meaning_en": "I'll leave the accounting to you."},
        "N2_649": {"example_sentence": "（（軽）け）い（い）り（り）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "けいりょうしてください。", "example_meaning_cn": "请测量（称重）。", "example_meaning_en": "Please measure/weigh it."},
        "N2_650": {"example_sentence": "（（汚）けが）さないで（で）ください。", "example_reading": "けがさないでください。", "example_meaning_cn": "请不要弄脏。", "example_meaning_en": "Please don't defile/stain it."},
        "N2_651": {"example_sentence": "（（外科）げか）しゅじゅつ（しゅじゅつ）を（を）し（し）ます。", "example_reading": "げかしゅじゅつをします。", "example_meaning_cn": "做外科手术。", "example_meaning_en": "Performing surgery."},
        "N2_652": {"example_sentence": "（（劇）げき）を（を）見（み）て（て）ください。", "example_reading": "げきをみてください。", "example_meaning_cn": "请看戏（剧）。", "example_meaning_en": "Please watch the play/drama."},
        "N2_653": {"example_sentence": "（（激）げき）し（し）ん（ん）が（が）走り（はしり）まし（し）た。", "example_reading": "げきしんがはしりました。", "example_meaning_cn": "感受到了剧烈的震动。", "example_meaning_en": "A severe earthquake struck."},
        "N2_654": {"example_sentence": "（（劇）げき）てき（てき）な（な）出会い（であい）です。", "example_reading": "げきてきなであいです。", "example_meaning_cn": "剧性的相遇。", "example_meaning_en": "It's a dramatic encounter."},
        "N2_655": {"example_sentence": "（（激）げき）ど（ど）う（う）の（の）時代（じだい）です。", "example_reading": "げきどうのじだいです。", "example_meaning_cn": "激荡的时代。", "example_meaning_en": "An era of upheaval."},
        "N2_656": {"example_sentence": "（（劇）げき）れ（れ）つ（つ）な（な）戦い（たたかい）です。", "example_reading": "げきれつなたたかいです。", "example_meaning_cn": "剧烈的战斗。", "example_meaning_en": "A fierce battle."},
        "N2_657": {"example_sentence": "（（月）げ）っ（っ）か（か）ん（ん）誌（し）を（を）読み（よみ）ます。", "example_reading": "げっかんしをよみます。", "example_meaning_cn": "看月刊杂志。", "example_meaning_en": "Reading a monthly magazine."},
        "N2_658": {"example_sentence": "（（月）げ）っ（っ）き（き）ゅう（ゅう）を（を）もらい（もらい）ます。", "example_reading": "げっきゅうをもらいます。", "example_meaning_cn": "领月薪。", "example_meaning_en": "Receiving a monthly salary."},
        "N2_659": {"example_sentence": "（（月）げ）っ（っ）し（し）ゃ（ゃ）を（を）払い（はらい）ます。", "example_reading": "げっしゃをはらいます。", "example_meaning_cn": "交月费。", "example_meaning_en": "Paying a monthly tuition fee."},
        "N2_660": {"example_sentence": "（（削）けず）っ（っ）て（て）ください。", "example_reading": "けずってください。", "example_meaning_cn": "请削减（或刨平）。", "example_meaning_en": "Please shave/reduce it."},
        "N2_661": {"example_sentence": "（（桁）けた）が（が）違い（ちがい）ますね。", "example_reading": "けたがちがいますね。", "example_meaning_cn": "相差悬殊（差几个数位）呢。", "example_meaning_en": "It's on a completely different scale."},
        "N2_662": {"example_sentence": "（（血）け）っ（っ）あ（あ）つ（つ）を（を）測っ（はかっ）て（て）ください。", "example_reading": "けつあつをはかってください。", "example_meaning_cn": "请测量血压。", "example_meaning_en": "Please measure the blood pressure."},
        "N2_663": {"example_sentence": "（（血）け）っ（っ）き（き）さ（さ）かん（かん）ですね。", "example_reading": "けっきさかんですね。", "example_meaning_cn": "血气方刚（精力充沛）呢。", "example_meaning_en": "They are full of vigor/hot-blooded."},
        "N2_664": {"example_sentence": "（（結）け）っ（っ）き（き）ょ（ょ）く（く）どう（どう）なり（なり）まし（し）たか。", "example_reading": "けっきょくどうなりましたか。", "example_meaning_cn": "结局（结果）怎么样了？", "example_meaning_en": "What happened in the end?"},
        "N2_665": {"example_sentence": "（（決）け）っ（っ）さ（さ）ん（ん）し（し）て（て）ください。", "example_reading": "けっさんしてください。", "example_meaning_cn": "请结算。", "example_meaning_en": "Please settle the accounts."},
        "N2_666": {"example_sentence": "（（決）け）っ（っ）し（し）て（て）忘れ（わすれ）ない（ない）で（で）ください。", "example_reading": "けっしてわすれないでください。", "example_meaning_cn": "决不要忘记。", "example_meaning_en": "Never forget it."},
        "N2_667": {"example_sentence": "（（結）け）っ（っ）し（し）ん（ん）し（し）て（て）ください。", "example_reading": "けっしんしてください。", "example_meaning_cn": "请下决心。", "example_meaning_en": "Please make up your mind."},
        "N2_668": {"example_sentence": "（（欠）け）っ（っ）せ（せ）き（き）し（し）ないで（で）ください。", "example_reading": "けっせきしないでください。", "example_meaning_cn": "请不要缺席。", "example_meaning_en": "Please don't be absent."},
        "N2_669": {"example_sentence": "（（決）け）っ（っ）ぜ（ぜ）ん（ん）と（と）し（し）た（た）態度（たいど）です。", "example_reading": "けっぜんとしたたいどです。", "example_meaning_cn": "决然（坚决）的态度。", "example_meaning_en": "A resolute attitude."},
        "N2_670": {"example_sentence": "（（決）け）っ（っ）た（た）い（い）し（し）て（て）ください。", "example_reading": "けったいしてください。", "example_meaning_cn": "请结队（或奇怪）。", "example_meaning_en": "Please form a group/how strange."},
        "N2_671": {"example_sentence": "（（決）け）っ（っ）て（て）い（い）し（し）て（て）ください。", "example_reading": "けっていしてください。", "example_meaning_cn": "请决定。", "example_meaning_en": "Please decide."},
        "N2_672": {"example_sentence": "（（欠）け）っ（っ）て（て）ん（ん）を（を）直し（なおし）て（て）ください。", "example_reading": "けってんをなおしてください。", "example_meaning_cn": "请改正缺点。", "example_meaning_en": "Please fix the defect/shortcoming."},
        "N2_673": {"example_sentence": "（（決）け）っ（っ）と（と）う（う）を（を）し（し）ましょう。", "example_reading": "けっとうをしましょう。", "example_meaning_cn": "决斗吧。", "example_meaning_en": "Let's have a duel."},
        "N2_674": {"example_sentence": "（（結）け）っ（っ）ぱ（ぱ）く（く）を（を）証明（しょうめい）し（し）てください。", "example_reading": "けっぱくをしょうめいしてください。", "example_meaning_cn": "请证明清白。", "example_meaning_en": "Please prove your innocence."},
        "N2_675": {"example_sentence": "（（結）け）っ（っ）び（び）ん（ん）し（し）て（て）います。", "example_reading": "けっびんしています。", "example_meaning_cn": "停航（欠航）中。", "example_meaning_en": "The flight is cancelled."},
        "N2_676": {"example_sentence": "（（結）け）っ（っ）ま（ま）つ（つ）を（を）見（み）て（て）ください。", "example_reading": "けっまつをみてください。", "example_meaning_cn": "请看结局（结末）。", "example_meaning_en": "Please see the conclusion/outcome."},
         "N2_677": {"example_sentence": "（（決）け）っ（っ）よ（よ）う（う）し（し）て（て）ください。", "example_reading": "けっようしてください。", "example_meaning_cn": "请决断（或使用）。", "example_meaning_en": "Please make a decision."},
        "N2_678": {"example_sentence": "（（結）け）っ（っ）ろ（ろ）ん（ん）を（を）出し（だし）て（て）ください。", "example_reading": "けっろんをだしてください。", "example_meaning_cn": "请得出结论。", "example_meaning_en": "Please reach a conclusion."},
        "N2_679": {"example_sentence": "（（気配）けはい）を（を）感じ（かんじ）ます。", "example_reading": "けはいをかんじます。", "example_meaning_cn": "感觉到动静（情形）。", "example_meaning_en": "I feel a presence/sign."},
        "N2_680": {"example_sentence": "（（下）げ）び（び）な（な）こと（こと）を（を）言い（いい）ない（ない）で（で）ください。", "example_reading": "げびなことをいいないでください。", "example_meaning_cn": "请不要说卑鄙（或下流）的话。", "example_meaning_en": "Please don't say vulgar things."},
        "N2_681": {"example_sentence": "（（憲）けん）ほ（ほ）う（う）を（を）守り（まもり）ましょう。", "example_reading": "けんぽうをまもりましょう。", "example_meaning_cn": "遵守宪法吧。", "example_meaning_en": "Let's uphold the constitution."},
        "N2_682": {"example_sentence": "（（見）けん）を（を）持ち（もち）ます。", "example_reading": "けんをもちます。", "example_meaning_cn": "持有见解。", "example_meaning_en": "I have an opinion/view."},
        "N2_683": {"example_sentence": "（（圏）けん）に（に）入り（はいり）ます。", "example_reading": "けんにはいります。", "example_meaning_cn": "进入范围（圈）内。", "example_meaning_en": "Coming within the range/sphere."},
        "N2_684": {"example_sentence": "（（権）けん）り（り）を（を）主張（しゅちょう）し（し）て（て）ください。", "example_reading": "けんりをしゅちょうしてください。", "example_meaning_cn": "请主张权利。", "example_meaning_en": "Please assert your rights."},
        "N2_685": {"example_sentence": "（（券）けん）を（を）買っ（かっ）て（て）ください。", "example_reading": "けんをかってください。", "example_meaning_cn": "请买票。", "example_meaning_en": "Please buy a ticket."},
        "N2_686": {"example_sentence": "（（県）けん）へ（へ）行き（いき）ます。", "example_reading": "けんへいきます。", "example_meaning_cn": "去县里（省）。", "example_meaning_en": "I'm going to the prefecture."},
        "N2_687": {"example_sentence": "（（険）けん）あ（あ）く（く）な（な）空気（くうき）です。", "example_reading": "けんあくなくうきです。", "example_meaning_cn": "险恶（或紧张）的气氛。", "example_meaning_en": "A dangerous/strained atmosphere."},
        "N2_688": {"example_sentence": "（（見）けん）あ（あ）つ（つ）し（し）て（て）ください。", "example_reading": "けんあつしてください。", "example_meaning_cn": "请视察（或见习）。", "example_meaning_en": "Please inspect/observe."},
        "N2_689": {"example_sentence": "（（芸）げい）の（の）う（う）じ（じ）ん（ん）になり（なり）たい（たい）です。", "example_reading": "げいのうじんになりたいです。", "example_meaning_cn": "想成为艺人。", "example_meaning_en": "I want to become an entertainer."},
        "N2_690": {"example_sentence": "（（芸）げい）き（き）ょう（ょう）し（し）て（て）ください。", "example_reading": "げいきょうしてください。", "example_meaning_cn": "请进行演艺活动。", "example_meaning_en": "Please perform/entertain."},
        "N2_691": {"example_sentence": "（（原）げん）あ（あ）つ（つ）を（を）下げ（さげ）て（て）ください。", "example_reading": "げんあつをさげてください。", "example_meaning_cn": "请降压。", "example_meaning_en": "Please reduce the pressure."},
        "N2_692": {"example_sentence": "（（検）けん）い（い）が（が）あり（あり）ますね。", "example_reading": "けんいがありますね。", "example_meaning_cn": "真有权威呢。", "example_meaning_en": "They have authority, don't they?"},
        "N2_693": {"example_sentence": "（（原）げん）い（い）ん（ん）を（を）調べ（しらべ）て（て）ください。", "example_reading": "げんいんをしらべてください。", "example_meaning_cn": "请调查原因。", "example_meaning_en": "Please investigate the cause."},
        "N2_694": {"example_sentence": "（（検）けん）え（え）き（き）し（し）て（て）ください。", "example_reading": "けんえきしてください。", "example_meaning_cn": "请检疫。", "example_meaning_en": "Please quarantine it."},
        "N2_695": {"example_sentence": "（（見）けん）え（え）ん（ん）し（し）て（て）ください。", "example_reading": "けんえんしてください。", "example_meaning_cn": "请避而远之。", "example_meaning_en": "Please keep your distance/avoid."},
        "N2_696": {"example_sentence": "（（現）げん）か（か）を（を）下げ（さげ）て（て）ください。", "example_reading": "げんかをさげてください。", "example_meaning_cn": "请降低原价（成本）。", "example_meaning_en": "Please lower the cost price."},
        "N2_697": {"example_sentence": "（（限）げん）か（か）い（い）に（に）挑み（いどみ）ましょう。", "example_reading": "げんかいにいどみましょう。", "example_meaning_cn": "挑战极限吧。", "example_meaning_en": "Let's challenge the limit."},
        "N2_698": {"example_sentence": "（（見）けん）か（か）く（く）を（を）は（は）っきり（り）し（し）て（て）ください。", "example_reading": "けんかくをはっきりしてください。", "example_meaning_cn": "请明确见解。", "example_meaning_en": "Please clarify your view."},
        "N2_699": {"example_sentence": "（（健）けん）た（た）い（い）で（で）い（い）て（て）ください。", "example_reading": "けんたいでいてください。", "example_meaning_cn": "请保持健泰（健康）。", "example_meaning_en": "Please stay healthy."},
        "N2_700": {"example_sentence": "（（厳）げん）かく（かく）に（に）守っ（まもっ）て（て）ください。", "example_reading": "げんかくにまもってください。", "example_meaning_cn": "请严格遵守。", "example_meaning_en": "Please follow strictly."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N2_700.")

if __name__ == "__main__":
    main()
