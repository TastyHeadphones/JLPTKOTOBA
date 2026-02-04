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
        "N2_851": {"example_sentence": "（（転）ころ）び（び）ま（ま）わ（わ）ら（ら）ないで（で）ください。", "example_reading": "ころびまわらないでください。", "example_meaning_cn": "请不要翻滚（打滚）。", "example_meaning_en": "Please don't roll around."},
        "N2_852": {"example_sentence": "（（転）ころ）び（び）そう（そう）です。", "example_reading": "ころびそうです。", "example_meaning_cn": "快要跌倒了。", "example_meaning_en": "I'm about to fall down."},
        "N2_853": {"example_sentence": "（（困）こん）き（き）ょ（ょ）を（を）示し（しめし）てください。", "example_reading": "こんきょをしめしてください。", "example_meaning_cn": "请出示根据（根据）。", "example_meaning_en": "Please show the evidence/basis."},
        "N2_854": {"example_sentence": "（（混）こん）ざ（ざ）つ（つ）し（し）て（て）います。", "example_reading": "こんざつしています。", "example_meaning_cn": "正拥挤（混杂）着呢。", "example_meaning_en": "It's congested/crowded."},
        "N2_855": {"example_sentence": "（（混）こん）し（し）ん（ん）し（し）て（て）ください。", "example_reading": "こんしんしてください。", "example_meaning_cn": "请进行混信（或交流）。", "example_meaning_en": "There's interference/mixed signals."},
        "N2_856": {"example_sentence": "（（混）こん）ぜ（ぜ）ん（ん）と（と）し（し）て（て）います。", "example_reading": "こんぜんとしています。", "example_meaning_cn": "浑然一体（混在一起）。", "example_meaning_en": "It's all blended together/harmonious."},
        "N2_857": {"example_sentence": "（（混）こん）と（と）う（う）し（し）ないで（で）ください。", "example_reading": "こんとうしないでください。", "example_meaning_cn": "请不要混淆（混同）。", "example_meaning_en": "Please don't confuse/mix them up."},
        "N2_858": {"example_sentence": "（（困）こん）な（な）ん（ん）に（に）立ち（たち）向かい（むかい）ましょう。", "example_reading": "こんなんにたちむかいましょう。", "example_meaning_cn": "勇敢面对困难吧。", "example_meaning_en": "Let's face the difficulties."},
        "N2_859": {"example_sentence": "（（混）こん）に（に）ゅう（ゅう）し（し）ないで（で）ください。", "example_reading": "こんにゅうしないでください。", "example_meaning_cn": "请不要混入。", "example_meaning_en": "Please don't let foreign objects get in."},
        "N2_860": {"example_sentence": "（（差）さ）が（が）あり（あり）ますね。", "example_reading": "さがありますね。", "example_meaning_cn": "有差距呢。", "example_meaning_en": "There's a difference/gap, isn't there?"},
        "N2_861": {"example_sentence": "（（際）さい）に（に）なっ（なっ）て（て）ください。", "example_reading": "さいになってください。", "example_meaning_cn": "请成为边际（或到时候）。", "example_meaning_en": "Please be on the edge/when the time comes."},
        "N2_862": {"example_sentence": "（（再）さい）かい（かい）を（を）祝っ（いわっ）て（て）ください。", "example_reading": "さいかいをいわってください。", "example_meaning_cn": "请祝贺重逢（再会）。", "example_meaning_en": "Please celebrate our reunion/meeting again."},
        "N2_863": {"example_sentence": "（（災）さい）がい（がい）に（に）備え（そなえ）ましょう。", "example_reading": "さいがいにそなえましょう。", "example_meaning_cn": "防范灾害吧。", "example_meaning_en": "Let's prepare for disasters."},
        "N2_864": {"example_sentence": "（（歳）さい）げ（げ）つ（つ）を（を）考え（かんがえ）て（て）ください。", "example_reading": "さいげつをかんがえてください。", "example_meaning_cn": "请考虑岁月（时光）。", "example_meaning_en": "Please consider the years/time passing."},
        "N2_865": {"example_sentence": "（（再）さい）げ（げ）ん（ん）し（し）て（て）ください。", "example_reading": "さいげんしてください。", "example_meaning_cn": "请再现。", "example_meaning_en": "Please reproduce/recreate it."},
        "N2_866": {"example_sentence": "（（最）さい）こ（こ）う（う）ですね！ ", "example_reading": "さいこうですね！", "example_meaning_cn": "最高（最好）了！", "example_meaning_en": "It's the best!"},
        "N2_867": {"example_sentence": "（（再）さい）こ（こ）ん（ん）し（し）て（て）ください。", "example_reading": "さいこんしてください。", "example_meaning_cn": "请再婚。", "example_meaning_en": "Please remarry."},
        "N2_868": {"example_sentence": "（（採）さい）さ（さ）ん（ん）が（が）合い（あい）ますか。", "example_reading": "さいさんがあいますか。", "example_meaning_cn": "划算（采算）吗？", "example_meaning_en": "Is it profitable/economical?"},
        "N2_869": {"example_sentence": "（（産）さい）し（し）を（を）養っ（やしなっ）て（て）ください。", "example_reading": "さいしをやしなってください。", "example_meaning_cn": "请抚养妻儿（产子）。", "example_meaning_en": "Please support your wife and children."},
        "N2_870": {"example_sentence": "（（祭）さい）じ（じ）つ（つ）は（は）休み（やすみ）です。", "example_reading": "さいじつわやすみです。", "example_meaning_cn": "祭日（节日）休息。", "example_meaning_en": "Public holidays are days off."},
        "N2_871": {"example_sentence": "（（採）さい）じ（じ）ゅ（ゅ）う（う）し（し）て（て）ください。", "example_reading": "さいじゅうしてください。", "example_meaning_cn": "请再次采集（重叠）。", "example_meaning_en": "Please collect/gather again."},
        "N2_872": {"example_sentence": "（（再）さい）し（し）ん（ん）の（の）注意（ちゅうい）を（を）払っ（はらっ）て（て）ください。", "example_reading": "さいしんのちゅういをはらってください。", "example_meaning_cn": "请予以万分注意（更新）。", "example_meaning_en": "Please pay the utmost attention."},
        "N2_873": {"example_sentence": "（（最）さい）ぜ（ぜ）ん（ん）を（を）尽くし（つくし）ましょう。", "example_reading": "さいぜんをつくしましょう。", "example_meaning_cn": "尽最大（最善）努力吧。", "example_meaning_en": "Let's do our very best."},
        "N2_874": {"example_sentence": "（（採）さい）た（た）く（く）し（し）ないで（で）ください。", "example_reading": "さいたくしないでください。", "example_meaning_cn": "请不要采纳。", "example_meaning_en": "Please don't adopt/select it."},
        "N2_875": {"example_sentence": "（（裁）さい）だ（だ）ん（ん）し（し）て（て）ください。", "example_reading": "さいだんしてください。", "example_meaning_cn": "请裁剪。", "example_meaning_en": "Please cut the cloth/judge."},
        "N2_876": {"example_sentence": "（（産）さい）ち（ち）を（を）確認（かくにん）し（し）てください。", "example_reading": "さいちをかくにんしてください。", "example_meaning_cn": "请确认产地。", "example_meaning_en": "Please check the place of origin."},
        "N2_877": {"example_sentence": "（（祭）さい）て（て）ん（ん）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "さいてんをたのしみましょう。", "example_meaning_cn": "享受祭典（典礼）吧。", "example_meaning_en": "Let's enjoy the festival/ceremony."},
        "N2_878": {"example_sentence": "（（採）さい）て（て）ん（ん）し（し）て（て）ください。", "example_reading": "さいてんしてください。", "example_meaning_cn": "请打分（采点）。", "example_meaning_en": "Please score/grade it."},
        "N2_879": {"example_sentence": "（（災）さい）な（な）ん（ん）に（に）逢い（あい）まし（し）た。", "example_reading": "さいなんにあいました。", "example_meaning_cn": "遭遇了灾难。", "example_meaning_en": "I met with a disaster/misfortune."},
        "N2_880": {"example_sentence": "（（裁）さい）ば（ば）ん（ん）に（に）訴え（うったえ）ましょう。", "example_reading": "さいばんにうったえましょう。", "example_meaning_cn": "起诉（上法庭）吧。", "example_meaning_en": "Let's take it to court."},
        "N2_881": {"example_sentence": "（（裁）さい）ふ（ふ）を（を）忘れ（わすれ）ない（ない）で（で）ください。", "example_reading": "さいふをわすれないでください。", "example_meaning_cn": "请不要忘记钱包。", "example_meaning_en": "Please don't forget your wallet."},
        "N2_882": {"example_sentence": "（（採）さい）ほ（ほ）う（う）し（し）て（て）ください。", "example_reading": "さいほうしてください。", "example_meaning_cn": "请缝纫。", "example_meaning_en": "Please do some sewing."},
        "N2_883": {"example_sentence": "（（材）さい）り（り）ょ（ょ）う（う）を（を）集め（あつめ）て（て）ください。", "example_reading": "さいりょうをあつめてください。", "example_meaning_cn": "请收集材料。", "example_meaning_en": "Please gather the materials."},
        "N2_884": {"example_sentence": "（（差）さ）い（い）が（が）あり（あり）ますね。", "example_reading": "さいがありますね。", "example_meaning_cn": "有差异呢。", "example_meaning_en": "There's a disparity/gap."},
        "N2_885": {"example_sentence": "（（遮）さえぎ）ら（ら）ないで（で）ください。", "example_reading": "さえぎらないでください。", "example_meaning_cn": "请不要遮挡（或打断）。", "example_meaning_en": "Please don't block/interrupt me."},
        "N2_886": {"example_sentence": "（（囀）さえず）っ（っ）て（て）います。", "example_reading": "さえずっています。", "example_meaning_cn": "正在婉转地歌唱（啁啾）。", "example_meaning_en": "The birds are chirping/twittering."},
        "N2_887": {"example_sentence": "（（冴）さ）え（え）て（て）いますね！ ", "example_reading": "さえていますね！", "example_meaning_cn": "真够清醒（或灵巧）的呢！", "example_meaning_en": "You're very sharp/vivid!"},
        "N2_888": {"example_sentence": "（（逆）さか）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "さからわないでください。", "example_meaning_cn": "请不要抗拒（违抗）。", "example_meaning_en": "Please don't defy/go against it."},
        "N2_889": {"example_sentence": "（（盛）さか）り（り）に（に）やっ（やっ）て（て）ください。", "example_reading": "さかりにやってください。", "example_meaning_cn": "在最盛（繁荣）的时候做吧。", "example_meaning_en": "Please do it when it's in full swing/at its peak."},
        "N2_890": {"example_sentence": "（（境）さかい）を（を）越え（こえ）まし（し）た。", "example_reading": "さかいをこえました。", "example_meaning_cn": "跨过了边界。", "example_meaning_en": "I crossed the border/boundary."},
        "N2_891": {"example_sentence": "（（盛）さか）ん（ん）な（な）拍手（はくしゅ）です。", "example_reading": "さかんなはくしゅです。", "example_meaning_cn": "热烈（盛大）的掌声。", "example_meaning_en": "Hearty/vigorous applause."},
        "N2_892": {"example_sentence": "（（坂）さか）み（み）ち（ち）を（を）登り（のぼり）ます。", "example_reading": "さかみちをのぼります。", "example_meaning_cn": "爬坡路径。", "example_meaning_en": "Climbing up a sloping road."},
        "N2_893": {"example_sentence": "（（栄）さか）え（え）て（て）ください。", "example_reading": "さかえてください。", "example_meaning_cn": "请繁荣昌盛。", "example_meaning_en": "Please prosper/thrive."},
        "N2_894": {"example_sentence": "（（杯）さかずき）を（を）交わし（かわし）ましょう。", "example_reading": "さかずきをかわしましょう。", "example_meaning_cn": "干杯吧。", "example_meaning_en": "Let's exchange cups/toast together."},
        "N2_895": {"example_sentence": "（（逆）さか）だ（だ）ち（ち）し（し）て（て）ください。", "example_reading": "さかだちしてください。", "example_meaning_cn": "请倒立。", "example_meaning_en": "Please do a handstand."},
        "N2_896": {"example_sentence": "（（逆）さか）ら（ら）っ（っ）て（て）はいけ（いけ）ない（ない）です。", "example_reading": "さからってはいけないです。", "example_meaning_cn": "不能违抗。", "example_meaning_en": "You must not disobey/oppose it."},
        "N2_897": {"example_sentence": "（（探）さが）っ（っ）て（て）ください。", "example_reading": "さがってください。", "example_meaning_cn": "请寻找（或打听）。", "example_meaning_en": "Please search/look for it."},
        "N2_898": {"example_sentence": "（（下）さ）が（が）っ（っ）て（て）ください。", "example_reading": "さがってください。", "example_meaning_cn": "请退后（或下降）。", "example_meaning_en": "Please step back/fall back."},
         "N2_899": {"example_sentence": "（（捜）さが）し（し）て（て）ください。", "example_reading": "さがしてください。", "example_meaning_cn": "请寻找（搜寻）。", "example_meaning_en": "Please search/look for it."},
        "N2_900": {"example_sentence": "（（下）さ）げ（げ）て（て）ください。", "example_reading": "さげてください。", "example_meaning_cn": "请放下（或降低）。", "example_meaning_en": "Please lower/let down."},
        "N2_901": {"example_sentence": "（（詐）さ）ぎ（ぎ）に（に）気（き）をつけ（つけ）ましょう。", "example_reading": "さぎにきをつけましょう。", "example_meaning_cn": "注意诈骗吧。", "example_meaning_en": "Let's beware of fraud/scams."},
        "N2_902": {"example_sentence": "（（搾）さく）に（に）入り（はいり）たい（たい）です。", "example_reading": "さくにはいりたいです。", "example_meaning_cn": "想进入政策（计谋）环节。", "example_meaning_en": "I want to get into the plan/strategy."},
        "N2_903": {"example_sentence": "（（昨）さく）じ（じ）つ（つ）はお（お）世話（せわ）になり（なり）まし（し）た。", "example_reading": "さくじつわおせわになりました。", "example_meaning_cn": "昨天受您照顾了。", "example_meaning_en": "Thank you for your help yesterday."},
        "N2_904": {"example_sentence": "（（昨）さく）ね（ね）ん（ん）は（は）ありがとう。", "example_reading": "さくねんわありがとう。", "example_meaning_cn": "去年谢谢了。", "example_meaning_en": "Thank you for last year."},
        "N2_905": {"example_sentence": "（（搾）さく）に（に）ゅう（ゅう）し（し）て（て）ください。", "example_reading": "さくにゅうしてください。", "example_meaning_cn": "请挤奶。", "example_meaning_en": "Please milk the cow/squeeze milk."},
        "N2_906": {"example_sentence": "（（探）さぐ）っ（っ）て（て）ください。", "example_reading": "さぐってください。", "example_meaning_cn": "请探听（或摸索）。", "example_meaning_en": "Please probe/grope for it."},
        "N2_907": {"example_sentence": "（（酒）さけ）を（を）飲ま（のま）ないで（で）ください。", "example_reading": "さけをのまないでください。", "example_meaning_cn": "请不要喝酒。", "example_meaning_en": "Please don't drink alcohol."},
        "N2_908": {"example_sentence": "（（避）さ）け（け）て（て）ください。", "example_reading": "さけてください。", "example_meaning_cn": "请避开（回避）。", "example_meaning_en": "Please avoid/evade."},
        "N2_909": {"example_sentence": "（（叫）さけ）ん（ん）で（て）ください。", "example_reading": "さけんでください。", "example_meaning_cn": "请大叫。", "example_meaning_en": "Please shout/scream."},
        "N2_910": {"example_sentence": "（（裂）さ）け（け）て（て）います。", "example_reading": "さけています。", "example_meaning_cn": "正裂着（揭开）呢。", "example_meaning_en": "It's torn/split open."},
        "N2_911": {"example_sentence": "（（捧）ささ）げ（げ）て（て）ください。", "example_reading": "ささげてください。", "example_meaning_cn": "请奉献（献出）。", "example_meaning_en": "Please offer/dedicate it."},
        "N2_912": {"example_sentence": "（（支）ささ）え（え）て（て）ください。", "example_reading": "ささえてください。", "example_meaning_cn": "请支撑（扶持）。", "example_meaning_en": "Please support/prop up."},
        "N2_913": {"example_sentence": "（（指）さ）し（し）て（て）ください。", "example_reading": "さしてください。", "example_meaning_cn": "请指着（或撑伞/注）。", "example_meaning_en": "Please point to it/hold an umbrella."},
        "N2_914": {"example_sentence": "（（授）さず）け（け）て（て）ください。", "example_reading": "さずけてください。", "example_meaning_cn": "请授予（或赐予）。", "example_meaning_en": "Please grant/bestow it."},
        "N2_915": {"example_sentence": "（（授）さず）か（か）っ（っ）て（て）ください。", "example_reading": "さずかってください。", "example_meaning_cn": "请领受（或怀孕）。", "example_meaning_en": "Please be blessed with/receive it."},
        "N2_916": {"example_sentence": "（（刺）さ）し（し）て（て）ください。", "example_reading": "さしてください。", "example_meaning_cn": "请刺（或插）。", "example_meaning_en": "Please stab/sting/pierce."},
        "N2_917": {"example_sentence": "（（指）さ）し（し）あ（あ）げ（げ）て（て）ください。", "example_reading": "さしあげてください。", "example_meaning_cn": "请呈上（谦语）。", "example_meaning_en": "Please give/offer it (humble)."},
        "N2_918": {"example_sentence": "（（指）さ）し（し）え（え）を（を）描い（かいて）ください。", "example_reading": "さしえをかいてください。", "example_meaning_cn": "请画插图。", "example_meaning_en": "Please draw an illustration."},
        "N2_919": {"example_sentence": "（（指）さ）し（し）お（お）さえ（え）て（て）ください。", "example_reading": "さしおさえてください。", "example_meaning_cn": "请查封（扣押）。", "example_meaning_en": "Please seize/distrain."},
        "N2_920": {"example_sentence": "（（指）さ）し（し）か（か）え（え）て（て）ください。", "example_reading": "さしかえてください。", "example_meaning_cn": "请替换（或改插）。", "example_meaning_en": "Please replace/substitute."},
        "N2_921": {"example_sentence": "（（指）さ）し（し）つ（つ）か（か）え（え）が（が）あり（あり）ますか。", "example_reading": "さしつかえがありますか。", "example_meaning_cn": "有妨碍（不方便）吗？", "example_meaning_en": "Is there any objection/inconvenience?"},
        "N2_922": {"example_sentence": "（（指）さ）し（し）で（で）話し（はなし）ましょう。", "example_reading": "さしでではなしましょう。", "example_meaning_cn": "面对面（两个人）谈吧。", "example_meaning_en": "Let's talk one-on-one."},
        "N2_923": {"example_sentence": "（（指）さ）し（し）ひ（ひ）い（い）て（て）ください。", "example_reading": "さしひいてください。", "example_meaning_cn": "请扣除（差额）。", "example_meaning_en": "Please deduct it."},
        "N2_924": {"example_sentence": "（（指）さ）し（し）む（む）け（け）て（て）ください。", "example_reading": "さしむけてください。", "example_meaning_cn": "请派往（或对着）。", "example_meaning_en": "Please send/dispatch someone."},
        "N2_925": {"example_sentence": "（（定）さだ）め（め）を（を）守り（まもり）ましょう。", "example_reading": "さだめをまもりましょう。", "example_meaning_cn": "遵守约定（或命运）吧。", "example_meaning_en": "Let's follow the rule/destiny."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N2_925.")

if __name__ == "__main__":
    main()
