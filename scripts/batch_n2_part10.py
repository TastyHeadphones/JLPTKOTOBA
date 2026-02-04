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
        "N2_926": {"example_sentence": "（（定）さだ）まっ（まっ）て（て）います。", "example_reading": "さだまっています。", "example_meaning_cn": "已经定（确定）了。", "example_meaning_en": "It has been decided/fixed."},
        "N2_927": {"example_sentence": "（（定）さだ）める（める）方法（ほうほう）を（を）教えて（おしえて）ください。", "example_reading": "さだめるほうほうをおしえてください。", "example_meaning_cn": "请告诉我制定的方法。", "example_meaning_en": "Please tell me the way to establish/determine it."},
        "N2_928": {"example_sentence": "（（察）さ）っ（っ）て（て）ください。", "example_reading": "さっしてください。", "example_meaning_cn": "请体谅（或察觉）。", "example_meaning_en": "Please sympathize with/sense it."},
        "N2_929": {"example_sentence": "（（雑）ざっ）し（し）を（を）読み（よみ）ます。", "example_reading": "ざっしをよみます。", "example_meaning_cn": "读杂志。", "example_meaning_en": "Reading a magazine."},
        "N2_930": {"example_sentence": "（（察）さ）っ（っ）ぱ（ぱ）り（り）し（し）て（て）ください。", "example_reading": "さっぱりしてください。", "example_meaning_cn": "请做得清爽（或乾脆）。", "example_meaning_en": "Please feel refreshed/be frank."},
        "N2_931": {"example_sentence": "（（里）さ）と（と）を（を）離れ（はなれ）まし（し）た。", "example_reading": "さとをはなれました。", "example_meaning_cn": "离开了故乡（里）。", "example_meaning_en": "I left my hometown."},
        "N2_932": {"example_sentence": "（（悟）さと）り（り）を（を）開い（ひらい）て（て）ください。", "example_reading": "さとりをひらいてください。", "example_meaning_cn": "请开悟（觉悟）。", "example_meaning_en": "Please attain enlightenment."},
        "N2_933": {"example_sentence": "（（悟）さと）っ（っ）て（て）ください。", "example_reading": "さとってください。", "example_meaning_cn": "请领悟（或察觉）。", "example_meaning_en": "Please realize/perceive it."},
        "N2_934": {"example_sentence": "（（真）さ）に（に）その（その）通り（とおり）です。", "example_reading": "さにそのとおりです。", "example_meaning_cn": "正如其言（的确）。", "example_meaning_en": "Indeed, that's correct."},
        "N2_935": {"example_sentence": "（（砂）さ）ば（ば）く（く）に（に）行き（いき）たい（たい）です。", "example_reading": "さばくにいきたいです。", "example_meaning_cn": "想去沙漠。", "example_meaning_en": "I want to go to the desert."},
        "N2_936": {"example_sentence": "（（裁）さば）い（い）て（て）ください。", "example_reading": "さばいてください。", "example_meaning_cn": "请审判（或处理）。", "example_meaning_en": "Please judge/dispose of it."},
        "N2_937": {"example_sentence": "（（寂）さび）し（し）が（が）ら（ら）ないで（で）ください。", "example_reading": "さびしがらないでください。", "example_meaning_cn": "请不要感到寂寞。", "example_meaning_en": "Please don't feel lonely."},
        "N2_938": {"example_sentence": "（（寂）さび）しい（しい）ですね。 ", "example_reading": "さびしいですね。", "example_meaning_cn": "真寂寞呢。", "example_meaning_en": "It's lonely/quiet, isn't it?"},
        "N2_939": {"example_sentence": "（（錆）さび）び（び）さ（さ）せ（せ）ないで（で）ください。", "example_reading": "さびびさせないでください。", "example_meaning_cn": "请不要让它生锈。", "example_meaning_en": "Please don't let it rust."},
        "N2_940": {"example_sentence": "（（錆）さび）び（び）て（て）います。", "example_reading": "さびびています。", "example_meaning_cn": "已经生锈了。", "example_meaning_en": "It's rusted."},
        "N2_941": {"example_sentence": "（（座）さ）ぶ（ぶ）と（と）ん（ん）を（を）当て（あて）て（て）ください。", "example_reading": "ざぶとんをあててください。", "example_meaning_cn": "请垫上坐垫。", "example_meaning_en": "Please use a cushion."},
        "N2_942": {"example_sentence": "（（作）さ）ま（ま）あ（あ）い（い）を見（み）て（て）ください。", "example_reading": "さまあいをみてください。", "example_meaning_cn": "请看情况（作相）。", "example_meaning_en": "Please look at the state/appearance."},
        "N2_943": {"example_sentence": "（（冷）さ）め（め）ない（ない）うち（うち）に（に）食べ（たべ）てください。", "example_reading": "さめないうちにたべてください。", "example_meaning_cn": "趁热（还没凉（冷））吃吧。", "example_meaning_en": "Please eat it while it's hot."},
        "N2_944": {"example_sentence": "（（覚）さ）め（め）て（て）ください。", "example_reading": "さめてください。", "example_meaning_cn": "请醒过来（或冷静下来）。", "example_meaning_en": "Please wake up/sober up."},
        "N2_945": {"example_sentence": "（（妨）さまた）げ（げ）ないで（で）ください。", "example_reading": "さまたげないでください。", "example_meaning_cn": "请不要妨碍。", "example_meaning_en": "Please don't hinder/obstruct it."},
        "N2_946": {"example_sentence": "（（様）さま）ざ（ざ）ま（ま）な（な）意見（いけん）があり（あり）ます。", "example_reading": "さまざまないけんがあります。", "example_meaning_cn": "有各种各样的意见。", "example_meaning_en": "There are various opinions."},
        "N2_947": {"example_sentence": "（（冷）さ）まし（し）て（て）ください。", "example_reading": "さましてください。", "example_meaning_cn": "请弄凉（冷）。", "example_meaning_en": "Please cool it down."},
        "N2_948": {"example_sentence": "（（覚）さ）まし（し）て（て）ください。", "example_reading": "さましてください。", "example_meaning_cn": "请叫醒（或弄醒）。", "example_meaning_en": "Please wake someone up."},
         "N2_949": {"example_sentence": "（（彷）さまよ）わ（わ）ないで（で）ください。", "example_reading": "さまよわないでください。", "example_meaning_cn": "请不要彷徨（徘徊）。", "example_meaning_en": "Please don't wander/loiter."},
        "N2_950": {"example_sentence": "（（覚）さ）め（め）な（な）い（い）で（で）ください。", "example_reading": "さめないでください。", "example_meaning_cn": "请不要醒来（或变凉）。", "example_meaning_en": "Please don't wake up/don't cool down."},
        "N2_951": {"example_sentence": "（（左）さ）よ（よ）う（う）で（で）ござい（ござい）ます。", "example_reading": "さようでございます。", "example_meaning_cn": "正是那样（如此）。", "example_meaning_en": "That is so (polite)."},
        "N2_952": {"example_sentence": "（（更）さら）に（に）頑張り（がんばり）ましょう。", "example_reading": "さらにがんばりましょう。", "example_meaning_cn": "更加地努力吧。", "example_meaning_en": "Let's work even harder."},
        "N2_953": {"example_sentence": "（（去）さ）ら（ら）な（な）い（い）で（で）ください。", "example_reading": "さらないでください。", "example_meaning_cn": "请不要离开。", "example_meaning_en": "Please don't leave."},
        "N2_954": {"example_sentence": "（（騒）さわ）が（が）せ（せ）て（て）すみません。", "example_reading": "さわがせてすみません。", "example_meaning_cn": "打扰了（吵闹了）真抱歉。", "example_meaning_en": "Sorry for causing a disturbance."},
        "N2_955": {"example_sentence": "（（騒）さわ）が（が）し（し）い（い）ですね。", "example_reading": "さわがしいですね。", "example_meaning_cn": "真够嘈杂（吵死人）的呢。", "example_meaning_en": "It's noisy, isn't it?"},
        "N2_956": {"example_sentence": "（（騒）さわ）い（い）で（て）ください。", "example_reading": "さわいでください。", "example_meaning_cn": "请欢呼（吵闹）。", "example_meaning_en": "Please make noise/clamor."},
        "N2_957": {"example_sentence": "（（触）さわ）ら（ら）ないで（で）ください。", "example_reading": "さわらないでください。", "example_meaning_cn": "请不要触摸。", "example_meaning_en": "Please don't touch."},
        "N2_958": {"example_sentence": "（（触）さわ）り（り）を（を）話し（はなし）て（て）ください。", "example_reading": "さわりをおなしてください。", "example_meaning_cn": "请说一下触及点（感触/开头）。", "example_meaning_en": "Please tell me the gist/touch of it."},
        "N2_959": {"example_sentence": "（（障）さわ）ら（ら）ないで（で）ください。", "example_reading": "さわらないでください。", "example_meaning_cn": "请不要碍事（或有害）。", "example_meaning_en": "Please don't interfere/harm."},
        "N2_960": {"example_sentence": "（（三）さん）か（か）し（し）て（て）ください。", "example_reading": "さんかしてください。", "example_meaning_cn": "请参加。", "example_meaning_en": "Please participate."},
        "N2_961": {"example_sentence": "（（参）さん）げ（げ）し（し）て（て）ください。", "example_reading": "さんげしてください。", "example_meaning_cn": "请忏悔。", "example_meaning_en": "Please repent/confess."},
        "N2_962": {"example_sentence": "（（参）さん）こ（こ）う（う）に（に）し（し）てください。", "example_reading": "さんこうにしてください。", "example_meaning_cn": "请作为参考。", "example_meaning_en": "Please use it as a reference."},
        "N2_963": {"example_sentence": "（（参）さん）さ（さ）く（く）し（し）ましょう。", "example_reading": "さんさくしましょう。", "example_meaning_cn": "去散步吧。", "example_meaning_en": "Let's take a stroll."},
        "N2_964": {"example_sentence": "（（賛）さん）せ（せ）い（い）し（し）ます。", "example_reading": "さんせいします。", "example_meaning_cn": "赞成。", "example_meaning_en": "I agree/approve."},
        "N2_965": {"example_sentence": "（（参）さん）そ（そ）う（う）を（を）吸っ（すっ）て（て）ください。", "example_reading": "さんそうをすってください。", "example_meaning_cn": "请吸氧（含氧量）。", "example_meaning_en": "Please inhale oxygen."},
        "N2_966": {"example_sentence": "（（賛）さん）た（た）い（い）を（を）歌い（うたい）ましょう。", "example_reading": "さんたいをうたいましょう。", "example_meaning_cn": "唱赞歌（赞美诗）吧。", "example_meaning_en": "Let's sing a hymn of praise."},
        "N2_967": {"example_sentence": "（（産）さん）ち（ち）を（を）確認（かくにん）し（し）てください。", "example_reading": "さんちをかくにんしてください。", "example_meaning_cn": "请确认产地。", "example_meaning_en": "Please check the location of production."},
        "N2_968": {"example_sentence": "（（散）さん）ふ（ふ）し（し）て（て）ください。", "example_reading": "さんふしてください。", "example_meaning_cn": "请散布（喷洒）。", "example_meaning_en": "Please scatter/spray it."},
        "N2_969": {"example_sentence": "（（散）さん）ほ（ほ）し（し）ましょう。", "example_reading": "さんほしましょう。", "example_meaning_cn": "去散步吧。", "example_meaning_en": "Let's go for a walk."},
        "N2_970": {"example_sentence": "（（仕）し）あ（あ）げ（げ）て（て）ください。", "example_reading": "しあげてください。", "example_meaning_cn": "请完成（做收尾）。", "example_meaning_en": "Please finish it up."},
        "N2_971": {"example_sentence": "（（仕）し）あ（あ）が（が）っ（っ）て（て）います。", "example_reading": "しあがっています。", "example_meaning_cn": "已经做好了。", "example_meaning_en": "It's finished/ready."},
        "N2_972": {"example_sentence": "（（仕）し）あ（あ）さ（さ）っ（っ）て（て）に（に）会い（あい）ましょう。", "example_reading": "しあさってに会いましょう。", "example_meaning_cn": "大后天见面吧。", "example_meaning_en": "Let's meet three days from now."},
        "N2_973": {"example_sentence": "（（強）し）い（い）ないで（で）ください。", "example_reading": "しいないでください。", "example_meaning_cn": "请不要强迫。", "example_meaning_en": "Please don't force me."},
        "N2_974": {"example_sentence": "（（詩）し）を（を）作っ（つくっ）て（て）ください。", "example_reading": "しをつくってください。", "example_meaning_cn": "请写诗。", "example_meaning_en": "Please write a poem."},
        "N2_975": {"example_sentence": "（（字）じ）を（を）丁寧（ていねい）に（に）書い（かい）て（て）ください。", "example_reading": "じをていねいにかいてください。", "example_meaning_cn": "请认真写字。", "example_meaning_en": "Please write the characters neatly."},
        "N2_976": {"example_sentence": "（（児）じ）を（を）可愛がっ（かわいがっ）て（て）ください。", "example_reading": "じをかわいがってください。", "example_meaning_cn": "请爱护孩子（小儿）。", "example_meaning_en": "Please be kind to the child."},
        "N2_977": {"example_sentence": "（（雌）し）の（の）動物（どうぶつ）です。", "example_reading": "しのどうぶつです。", "example_meaning_cn": "雌性动物。", "example_meaning_en": "It's a female animal."},
        "N2_978": {"example_sentence": "（（地）じ）を（を）固め（かため）ましょう。", "example_reading": "じをかためましょう。", "example_meaning_cn": "打好基础（或地基）吧。", "example_meaning_en": "Let's solidify the foundation."},
        "N2_979": {"example_sentence": "（（仕）し）あ（あ）わ（わ）せ（せ）を（を）祈り（いのり）ます。", "example_reading": "しあわせをいのります。", "example_meaning_cn": "祈祷幸福。", "example_meaning_en": "I pray for happiness."},
        "N2_980": {"example_sentence": "（（飼）し）い（い）なら（ら）し（し）て（て）ください。", "example_reading": "しいならしてください。", "example_meaning_cn": "请驯养。", "example_meaning_en": "Please tame it."},
        "N2_981": {"example_sentence": "（（強）し）い（い）る（る）ことは（は）し（し）ないで（で）ください。", "example_reading": "しいることわしないでください。", "example_meaning_cn": "请不要做强人所难的事。", "example_meaning_en": "Please don't compel/force anyone."},
        "N2_982": {"example_sentence": "（（仕）し）入れ（いれ）て（て）ください。", "example_reading": "しいれてください。", "example_meaning_cn": "请进货。", "example_meaning_en": "Please stock up/lay in goods."},
        "N2_983": {"example_sentence": "（（強）し）い（い）る（る）意見（いけん）です。", "example_reading": "しいるいけんです。", "example_meaning_cn": "强加的见解。", "example_meaning_en": "It's a forced opinion."},
        "N2_984": {"example_sentence": "（（自）じ）え（え）い（い）し（し）て（て）ください。", "example_reading": "じえいしてください。", "example_meaning_cn": "请自卫。", "example_meaning_en": "Please defend yourself."},
        "N2_985": {"example_sentence": "（（塩）しお）を（を）足し（たし）て（て）ください。", "example_reading": "しおをたしてください。", "example_meaning_cn": "请加点盐。", "example_meaning_en": "Please add some salt."},
        "N2_986": {"example_sentence": "（（潮）しお）が（が）満ち（みち）て（て）き（き）まし（し）た。", "example_reading": "しおがみちてきました。", "example_meaning_cn": "潮水涨上来了。", "example_meaning_en": "The tide is coming in."},
        "N2_987": {"example_sentence": "（（仕）し）か（か）え（え）し（し）し（し）ないで（で）ください。", "example_reading": "しかえししないでください。", "example_meaning_cn": "请不要报复（或重做）。", "example_meaning_en": "Please don't retaliate/do it again."},
        "N2_988": {"example_sentence": "（（仕）し）か（か）け（け）て（て）ください。", "example_reading": "しかけてください。", "example_meaning_cn": "请设置（或开始做）。", "example_meaning_en": "Please set it up/start doing it."},
        "N2_989": {"example_sentence": "（（強）し）か（か）た（た）が（が）あり（あり）ませんね。", "example_reading": "しかたがありませんね。", "example_meaning_cn": "没办法呢。", "example_meaning_en": "It can't be helped, can it?"},
        "N2_990": {"example_sentence": "（（仕）し）か（か）た（た）を（を）教えて（おしえて）ください。", "example_reading": "しかたをおしえてください。", "example_meaning_cn": "请教我做法。", "example_meaning_en": "Please tell me how to do it."},
        "N2_991": {"example_sentence": "（（死）し）か（か）つ（つ）問題（もんだい）です。", "example_reading": "しかつもんだいです。", "example_meaning_cn": "性命交关（生死）的问题。", "example_meaning_en": "It's a matter of life and death."},
        "N2_992": {"example_sentence": "（（仕）し）か（か）ね（ね）ないで（で）ください。", "example_reading": "しかねないでください。", "example_meaning_cn": "请不要（做出可能的事）。", "example_meaning_en": "Please don't (be capable of/prone to)."},
        "N2_993": {"example_sentence": "（（辞）じ）き（き）を（を）申し（もし）伝え（つたえ）て（て）ください。", "example_reading": "じきをもしつたえてください。", "example_meaning_cn": "请转告辞意（或到时候）。", "example_meaning_en": "Please convey my resignation/the timing."},
        "N2_994": {"example_sentence": "（（直）じ）き（き）に（に）行き（いき）ます。", "example_reading": "じきにいきます。", "example_meaning_cn": "马上（直接）去。", "example_meaning_en": "I'll go soon/directly."},
        "N2_995": {"example_sentence": "（（磁）じ）き（き）を（を）帯び（おび）て（て）います。", "example_reading": "じきをおびています。", "example_meaning_cn": "带有磁性。", "example_meaning_en": "It's magnetized."},
        "N2_996": {"example_sentence": "（（時）じ）き（き）を（を）待ち（まち）ましょう。", "example_reading": "じきをまちましょう。", "example_meaning_cn": "等待时机吧。", "example_meaning_en": "Let's wait for the right time."},
        "N2_997": {"example_sentence": "（（仕）し）き（き）り（り）に（に）話し（はなし）て（て）ください。", "example_reading": "しきりにはなしてください。", "example_meaning_cn": "请不停地（频繁地）说。", "example_meaning_en": "Please talk incessantly."},
        "N2_998": {"example_sentence": "（（頻）し）き（き）り（り）に（に）雨（あめ）が（が）降り（ふり）ます。", "example_reading": "しきりにあめがふります。", "example_meaning_cn": "雨下个不停（频繁）。", "example_meaning_en": "It's raining frequently/incessantly."},
        "N2_999": {"example_sentence": "（（仕）し）き（き）る（る）人（ひと）がい（い）ますか。", "example_reading": "しきるひとがいますか。", "example_meaning_cn": "有主持（隔开）的人吗？", "example_meaning_en": "Is there someone in charge/directing?"},
        "N2_1000": {"example_sentence": "（（至）し）き（き）ゅう（ゅう）来（き）て（て）ください！ ", "example_reading": "しきゅうきてください！", "example_meaning_cn": "请火速赶来！", "example_meaning_en": "Please come immediately!"}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N2_1000.")

if __name__ == "__main__":
    main()
