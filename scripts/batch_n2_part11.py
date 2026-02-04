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
        "N2_1001": {"example_sentence": "（（資）し）げ（げ）ん（ん）を（を）大切（たいせつ）に（に）し（し）ましょう。", "example_reading": "しげんをたいせつにしましょう。", "example_meaning_cn": "珍惜资源（资源）吧。", "example_meaning_en": "Let's value our resources."},
        "N2_1002": {"example_sentence": "（（事）じ）こ（こ）に（に）気（き）をつけ（つけ）て（て）ください。", "example_reading": "じこにきをつけてください。", "example_meaning_cn": "请注意事故。", "example_meaning_en": "Please be careful to avoid accidents."},
        "N2_1003": {"example_sentence": "（（事）じ）こ（こ）く（く）の（の）文化（ぶんか）を（を）守り（まもり）ましょう。", "example_reading": "じこくのぶんかをまもりましょう。", "example_meaning_cn": "守护本国（自国）文化吧。", "example_meaning_en": "Let's protect our own country's culture."},
        "N2_1004": {"example_sentence": "（（仕）し）こ（こ）み（み）を（を）始め（はじめ）て（て）ください。", "example_reading": "しこみをはじめてください。", "example_meaning_cn": "请开始准备（或酿造/采购）。", "example_meaning_en": "Please start the preparation/stocking up."},
        "N2_1005": {"example_sentence": "（（仕）し）さ（さ）く（く）し（し）て（て）ください。", "example_reading": "しさくしてください。", "example_meaning_cn": "请试作（试行）。", "example_meaning_en": "Please make a prototype/trial."},
        "N2_1006": {"example_sentence": "（（視）し）さ（さ）つ（つ）し（し）て（て）ください。", "example_reading": "しさつしてください。", "example_meaning_cn": "请视察。", "example_meaning_en": "Please inspect/observe."},
        "N2_1007": {"example_sentence": "（（資）し）さ（さ）ん（ん）を（を）運用（うんよう）し（し）て（て）ください。", "example_reading": "しさんをうんようしてください。", "example_meaning_cn": "请运用资产。", "example_meaning_en": "Please manage your assets."},
        "N2_1008": {"example_sentence": "（（死）し）し（し）を（を）乗り越え（のりこえ）て（て）ください。", "example_reading": "ししをのりこえてください。", "example_meaning_cn": "请克服死（生死/四肢）。", "example_meaning_en": "Please overcome death/limbs."},
        "N2_1009": {"example_sentence": "（（自）じ）し（し）ん（ん）を（を）持っ（もっ）て（て）ください。", "example_reading": "じしんをもってください。", "example_meaning_cn": "请持有自信（或这就是地震）。", "example_meaning_en": "Please have confidence (or it's an earthquake)."},
        "N2_1010": {"example_sentence": "（（静）しず）まり（まり）かえっ（かえっ）て（て）います。", "example_reading": "しずまりかえっています。", "example_meaning_cn": "鸦雀无声（静悄悄）。", "example_meaning_en": "It's completely silent."},
        "N2_1011": {"example_sentence": "（（沈）しず）め（め）て（て）ください。", "example_reading": "しずめてください。", "example_meaning_cn": "请使其沉没（或镇定）。", "example_meaning_en": "Please sink it/calm it down."},
        "N2_1012": {"example_sentence": "（（静）しず）ま（ま）っ（っ）て（て）ください。", "example_reading": "しずまってください。", "example_meaning_cn": "请安静下来。", "example_meaning_en": "Please quiet down/become calm."},
        "N2_1013": {"example_sentence": "（（沈）しず）ん（ん）で（て）います。", "example_reading": "しずんでいます。", "example_meaning_cn": "正在沉没（或消沉）。", "example_meaning_en": "It's sinking/depressed."},
        "N2_1014": {"example_sentence": "（（姿）しがた）を（を）見せ（みせ）て（て）ください。", "example_reading": "しがたをみせてください。", "example_meaning_cn": "请现身（姿态）。", "example_meaning_en": "Please show yourself/your figure."},
        "N2_1015": {"example_sentence": "（（仕）し）た（た）い（い）こと（こと）を（を）し（し）て（て）ください。", "example_reading": "したいことをしてください。", "example_meaning_cn": "请做想做的事情（或尸体）。", "example_meaning_en": "Please do what you want (or corpse)."},
        "N2_1016": {"example_sentence": "（（辞）じ）たい（たい）し（し）ないで（で）ください。", "example_reading": "じたいしないでください。", "example_meaning_cn": "请不要辞退。", "example_meaning_en": "Please don't decline/withdraw."},
        "N2_1017": {"example_sentence": "（（事）じ）たい（たい）を（を）重く（おもく）見（み）て（て）ください。", "example_reading": "じたいをおもくみてください。", "example_meaning_cn": "请慎重对待事态（局面）。", "example_meaning_en": "Please take the situation seriously."},
        "N2_1018": {"example_sentence": "（（下）した）が（が）き（き）を（を）し（し）て（て）ください。", "example_reading": "したがきをしてください。", "example_meaning_cn": "请写草稿（底稿）。", "example_meaning_en": "Please make a draft/sketch."},
        "N2_1019": {"example_sentence": "（（下）した）ご（ご）し（し）ら（ら）え（え）を（を）し（し）て（て）ください。", "example_reading": "したごしらえをしてください。", "example_meaning_cn": "请做初步准备。", "example_meaning_en": "Please do the preliminary preparations."},
        "N2_1020": {"example_sentence": "（（親）した）し（し）い（い）人（ひと）です。", "example_reading": "したしいひとです。", "example_meaning_cn": "亲近的人。", "example_meaning_en": "It's a close friend."},
        "N2_1021": {"example_sentence": "（（親）した）し（し）ま（ま）れ（れ）て（て）います。", "example_reading": "したしまれています。", "example_meaning_cn": "深受喜爱（亲近）。", "example_meaning_en": "It is widely loved/familiar."},
        "N2_1022": {"example_sentence": "（（親）した）し（し）み（み）を（を）持っ（もっ）て（て）ください。", "example_reading": "したしみをもってください。", "example_meaning_cn": "请持有亲近感。", "example_meaning_en": "Please have a sense of familiarity."},
        "N2_1023": {"example_sentence": "（（仕）し）た（た）て（て）て（て）ください。", "example_reading": "したててください。", "example_meaning_cn": "请缝纫（或培养）。", "example_meaning_en": "Please tailor/sew it."},
        "N2_1024": {"example_sentence": "（（下）した）び（び）に（に）なり（なり）まし（し）た。", "example_reading": "したびになりました。", "example_meaning_cn": "火势减弱（或热潮减退）了。", "example_meaning_en": "The fire has died down/lost momentum."},
        "N2_1025": {"example_sentence": "（（下）した）まち（まち）を（を）歩き（あるき）ましょう。", "example_reading": "したまちをあるきましょう。", "example_meaning_cn": "在旧市区（下町）走走吧。", "example_meaning_en": "Let's walk through the old downtown."},
        "N2_1026": {"example_sentence": "（（下）した）ま（ま）わ（わ）り（り）し（し）て（て）ください。", "example_reading": "したまわりしてください。", "example_meaning_cn": "请做下游（或视察）。", "example_meaning_en": "Please do a preliminary inspection."},
        "N2_1027": {"example_sentence": "（（下）した）む（む）き（き）に（に）なっ（なっ）て（て）います。", "example_reading": "したむきになっています。", "example_meaning_cn": "正趋于下降（或低头）。", "example_meaning_en": "It's on a downward trend/looking down."},
        "N2_1028": {"example_sentence": "（（仕）し）た（た）め（め）て（て）ください。", "example_reading": "しためてください。", "example_meaning_cn": "请写信（或吃完）。", "example_meaning_en": "Please write a letter/eat it up."},
        "N2_1029": {"example_sentence": "（（親）した）や（や）か（か）な（な）態度（たいど）です。", "example_reading": "したやかなたいどです。", "example_meaning_cn": "亲切（亲热）的态度。", "example_meaning_en": "A friendly/cordial attitude."},
        "N2_1030": {"example_sentence": "（（仕）し）た（た）より（より）を（を）待っ（まっ）て（て）ください。", "example_reading": "したよりをまってください。", "example_meaning_cn": "请等候预报（或回音）。", "example_meaning_en": "Please wait for the preliminary news."},
        "N2_1031": {"example_sentence": "（（質）しつ）を（を）高め（たかめ）ましょう。", "example_reading": "しつをたかめましょう。", "example_meaning_cn": "提高质量（品质）吧。", "example_meaning_en": "Let's improve the quality."},
        "N2_1032": {"example_sentence": "（（実）じつ）に（に）面白い（おもしろい）です。", "example_reading": "じつにおもしろいです。", "example_meaning_cn": "确实（实在）很有趣。", "example_meaning_en": "It's truly interesting."},
        "N2_1033": {"example_sentence": "（（実）じつ）え（え）ん（ん）し（し）て（て）ください。", "example_reading": "じつえんしてください。", "example_meaning_cn": "请演练（实演）。", "example_meaning_en": "Please demonstrate/perform."},
        "N2_1034": {"example_sentence": "（（実）じつ）か（か）を（を）話し（はなし）て（て）ください。", "example_reading": "じつかをおなしてください。", "example_meaning_cn": "请说出真话（或娘家）。", "example_meaning_en": "Please tell the truth/real story."},
        "N2_1035": {"example_sentence": "（（実）じつ）げ（げ）ん（ん）し（し）て（て）ください。", "example_reading": "じつげんしてください。", "example_meaning_cn": "请实现。", "example_meaning_en": "Please realize/fulfill it."},
        "N2_1036": {"example_sentence": "（（実）じつ）じ（じ）に（に）基づき（もとづき）ます。", "example_reading": "じつじにもとづきます。", "example_meaning_cn": "基于事实（实事）。", "example_meaning_en": "It's based on actual facts."},
        "N2_1037": {"example_sentence": "（（実）じつ）し（し）し（し）て（て）ください。", "example_reading": "じつししてください。", "example_meaning_cn": "请实施。", "example_meaning_en": "Please implement/carry out."},
        "N2_1038": {"example_sentence": "（（実）じつ）じ（じ）ょ（ょ）う（う）を（を）話し（はなし）て（て）ください。", "example_reading": "じつじょうをおなしてください。", "example_meaning_cn": "请说明实况（实情）。", "example_meaning_en": "Please explain the actual situation."},
        "N2_1039": {"example_sentence": "（（失）しつ）じ（じ）ょ（ょ）う（う）し（し）ないで（で）ください。", "example_reading": "しつじょうしないでください。", "example_meaning_cn": "请不要失常（或失当）。", "example_meaning_en": "Please don't lose your composure."},
        "N2_1040": {"example_sentence": "（（質）しつ）そ（そ）な（な）暮らし（くらし）です。", "example_reading": "しつそなくらしです。", "example_meaning_cn": "简朴（质素）的生活。", "example_meaning_en": "A simple/frugal life."},
        "N2_1041": {"example_sentence": "（（実）じつ）た（た）い（い）を（を）調査（ちょうさ）し（し）てください。", "example_reading": "じったいをちょうさしてください。", "example_meaning_cn": "请调查实际状态。", "example_meaning_en": "Please investigate the actual state."},
         "N2_1042": {"example_sentence": "（（湿）しっ）ち（ち）を（を）埋め立て（うめたて）ましょう。", "example_reading": "しっちをうめたてましょう。", "example_meaning_cn": "填平湿地吧。", "example_meaning_en": "Let's reclaim the wetland."},
        "N2_1043": {"example_sentence": "（（執）しつ）ぴ（ぴ）つ（つ）し（し）て（て）ください。", "example_reading": "しっぴつしてください。", "example_meaning_cn": "请执笔（写作）。", "example_meaning_en": "Please write/author it."},
        "N2_1044": {"example_sentence": "（（尻）しっ）ぽ（ぽ）を（を）振ら（ふら）ないで（で）ください。", "example_reading": "しっぽをふらないでください。", "example_meaning_cn": "请不要摇尾巴。", "example_meaning_en": "Please don't wag your tail."},
        "N2_1045": {"example_sentence": "（（実）じつ）ぶ（ぶ）つ（つ）を（を）見（み）て（て）ください。", "example_reading": "じつぶつをみてください。", "example_meaning_cn": "请看实物。", "example_meaning_en": "Please look at the real thing."},
        "N2_1046": {"example_sentence": "（（失）しつ）ぼ（ぼ）う（う）し（し）ないで（で）ください。", "example_reading": "しつぼうしないでください。", "example_meaning_cn": "请不要失望。", "example_meaning_en": "Please don't be disappointed."},
        "N2_1047": {"example_sentence": "（（失）しつ）め（め）い（い）し（し）ないで（で）ください。", "example_reading": "しつめいしないでください。", "example_meaning_cn": "请不要失明。", "example_meaning_en": "Please don't lose your sight."},
        "N2_1048": {"example_sentence": "（（実）じつ）よ（よ）う（う）てき（てき）な（な）品（しな）です。", "example_reading": "じつようてきなしなです。", "example_meaning_cn": "实用的物品。", "example_meaning_en": "It's a practical item."},
        "N2_1049": {"example_sentence": "（（実）じつ）り（り）を（を）得（え）て（て）ください。", "example_reading": "じつりをえてください。", "example_meaning_cn": "请获得实利（成果）。", "example_meaning_en": "Please get practical benefits."},
        "N2_1050": {"example_sentence": "（（実）じつ）れ（れ）い（い）を（を）出し（だし）て（て）ください。", "example_reading": "じつれいをだしてください。", "example_meaning_cn": "请举出实例。", "example_meaning_en": "Please give an actual example."},
        "N2_1051": {"example_sentence": "（（仕）し）て（て）あげ（あげ）て（て）ください。", "example_reading": "してあげてください。", "example_meaning_cn": "请为他（她）做。", "example_meaning_en": "Please do it for them."},
        "N2_1052": {"example_sentence": "（（指）し）て（て）い（い）を（を）受け（うけ）て（て）ください。", "example_reading": "していをうけてください。", "example_meaning_cn": "请按指定（通过指定）。", "example_meaning_en": "Please be designated/receive instructions."},
        "N2_1053": {"example_sentence": "（（私）し）て（て）き（き）な（な）用事（ようじ）です。", "example_reading": "してきなようじです。", "example_meaning_cn": "私人的事。", "example_meaning_en": "It's a private matter."},
        "N2_1054": {"example_sentence": "（（視）し）て（て）ん（ん）を（を）変え（かえ）て（て）ください。", "example_reading": "してんをかえてください。", "example_meaning_cn": "请改变视点（视角）。", "example_meaning_en": "Please change your perspective."},
        "N2_1055": {"example_sentence": "（（支）し）て（て）ん（ん）に（に）行き（いき）ます。", "example_reading": "してんにいきます。", "example_meaning_cn": "去分店（支店）。", "example_meaning_en": "I'm going to the branch office."},
        "N2_1056": {"example_sentence": "（（地）じ）ど（ど）り（り）を（を）食べ（たべ）ましょう。", "example_reading": "じどりをたべましょう。", "example_meaning_cn": "吃地鸡（本地鸡）吧。", "example_meaning_en": "Let's eat local chicken."},
        "N2_1057": {"example_sentence": "（（品）しな）び（び）な（な）態度（たいど）です。", "example_reading": "しなびなたいどです。", "example_meaning_cn": "品格高（上品）的态度。", "example_meaning_en": "A refined/elegant attitude."},
        "N2_1058": {"example_sentence": "（（品）しな）び（び）る（る）まで（まで）待っ（まっ）て（て）ください。", "example_reading": "しなびるまでまってください。", "example_meaning_cn": "请等到枯萎（或凋落）。", "example_meaning_en": "Please wait until it withers."},
        "N2_1059": {"example_sentence": "（（死）し）ぬ（ぬ）まで（まで）頑張り（がんばり）ます。", "example_reading": "しぬまでがんばります。", "example_meaning_cn": "努力到死。", "example_meaning_en": "I'll work hard until I die."},
        "N2_1060": {"example_sentence": "（（芝）しぱ）ふ（ふ）を（を）刈っ（かっ）て（て）ください。", "example_reading": "しぱふをかってください。", "example_meaning_cn": "请修剪草坪。", "example_meaning_en": "Please mow the lawn."},
        "N2_1061": {"example_sentence": "（（支）し）は（は）ら（ら）い（い）を（を）済ませ（すませ）て（て）ください。", "example_reading": "しはらいをすませてください。", "example_meaning_cn": "请结账（支付）。", "example_meaning_en": "Please finish the payment."},
        "N2_1062": {"example_sentence": "（（芝）し）ば（ば）い（い）を（を）見（み）に（に）行き（いき）ましょう。", "example_reading": "しぱいをみにいきましょう。", "example_meaning_cn": "去看戏吧。", "example_meaning_en": "Let's go see a play."},
        "N2_1063": {"example_sentence": "（（磁）じ）ば（ば）を（を）測っ（はかっ）て（て）ください。", "example_reading": "じばをはかってください。", "example_meaning_cn": "请测量磁场。", "example_meaning_en": "Please measure the magnetic field."},
        "N2_1064": {"example_sentence": "（（始）し）ま（ま）る（る）前（まえ）に（に）来（き）て（て）ください。", "example_reading": "しまるまえにきてください。", "example_meaning_cn": "请在开始（或关门）前来。", "example_meaning_en": "Please come before it starts/closes."},
        "N2_1065": {"example_sentence": "（（耳）じ）び（び）か（か）に（に）行き（いき）ます。", "example_reading": "じびかにいきます。", "example_meaning_cn": "去耳鼻科。", "example_meaning_en": "I'm going to the ENT clinic."},
        "N2_1066": {"example_sentence": "（（絞）しぼ）っ（っ）て（て）ください。", "example_reading": "しぼってください。", "example_meaning_cn": "请绞（或勒碎）。", "example_meaning_en": "Please wring/squeeze it."},
        "N2_1067": {"example_sentence": "（（搾）しぼ）っ（っ）て（て）ください。", "example_reading": "しぼってください。", "example_meaning_cn": "请榨（或挤）。", "example_meaning_en": "Please squeeze/press out."},
        "N2_1068": {"example_sentence": "（（縞）しま）の（の）服（ふく）です。", "example_reading": "しまのふくです。", "example_meaning_cn": "条纹衣服。", "example_meaning_en": "It's striped clothing."},
        "N2_1069": {"example_sentence": "（（締）し）め（め）き（き）っ（っ）て（て）ください。", "example_reading": "しめきってください。", "example_meaning_cn": "请紧闭（或截止）。", "example_meaning_en": "Please close it tightly/shutter it."},
        "N2_1070": {"example_sentence": "（（湿）しめ）っ（っ）て（て）いますね。", "example_reading": "しめっていますね。", "example_meaning_cn": "真潮湿呢。", "example_meaning_en": "It's damp, isn't it?"},
        "N2_1071": {"example_sentence": "（（締）し）め（め）る（る）のを（を）忘れ（わすれ）ない（ない）で（で）ください。", "example_reading": "しめるのわわすれないでください。", "example_meaning_cn": "请不要忘记系上（或关上）。", "example_meaning_en": "Please don't forget to fasten/close it."},
        "N2_1072": {"example_sentence": "（（占）し）め（め）る（る）割合（わりあい）を（を）教えて（おしえて）ください。", "example_reading": "しめるわりあいをおしえてください。", "example_meaning_cn": "请告诉我所占的比例。", "example_meaning_en": "Please tell me the percentage it occupies."},
        "N2_1073": {"example_sentence": "（（湿）しめ）す（す）のを（を）待っ（まっ）て（て）ください。", "example_reading": "しめすのわまってください。", "example_meaning_cn": "请等它变湿（或显示）。", "example_meaning_en": "Please wait for it to get damp/show it."},
        "N2_1074": {"example_sentence": "（（霜）しも）が（が）降り（ふり）まし（し）た。", "example_reading": "しもがふりまいた。", "example_meaning_cn": "下霜了。", "example_meaning_en": "Frost has fallen."},
        "N2_1075": {"example_sentence": "（（視野）しや）を（を）広げ（ひろげ）ましょう。", "example_reading": "しやをひろげましょう。", "example_meaning_cn": "开阔视野吧。", "example_meaning_en": "Let's broaden our horizons."},
        "N2_1076": {"example_sentence": "（（社）し）や（や）く（く）に（に）なり（なり）たい（たい）です。", "example_reading": "しやくになりたいです。", "example_meaning_cn": "想成为公司的重臣（或主角）。", "example_meaning_en": "I want to take on the role (or main person) of the company."},
        "N2_1077": {"example_sentence": "（（写）しゃ）し（し）ん（ん）を（を）撮り（とり）ましょう。", "example_reading": "しゃしんをとりましょう。", "example_meaning_cn": "拍照片吧。", "example_meaning_en": "Let's take a photo."},
        "N2_1078": {"example_sentence": "（（車）しゃ）こ（こ）に（に）入れ（いれ）て（て）ください。", "example_reading": "しゃこにいれてください。", "example_meaning_cn": "请进车库。", "example_meaning_en": "Please put it in the garage."},
        "N2_1079": {"example_sentence": "（（借）しゃ）く（く）し（し）に（に）なり（なり）たい（たい）です。", "example_reading": "しゃくしになりたいです。", "example_meaning_cn": "想成为借主（借款人/杓子）。", "example_meaning_en": "I want to become a borrower (or ladle)."},
        "N2_1080": {"example_sentence": "（（尺）しゃく）ど（ど）を（を）測っ（はかっ）て（て）ください。", "example_reading": "しゃくどをはかってください。", "example_meaning_cn": "请测量尺度。", "example_meaning_en": "Please measure the scale/standard."},
        "N2_1081": {"example_sentence": "（（社）しゃ）せ（せ）つ（つ）を（を）読み（よみ）ましょう。", "example_reading": "しゃせつをよみましょう。", "example_meaning_cn": "读社论吧。", "example_meaning_en": "Let's read the editorial."},
        "N2_1082": {"example_sentence": "（（車）しゃ）せ（せ）ん（ん）を（を）守り（まもり）ましょう。", "example_reading": "しゃせんをまもりましょう。", "example_meaning_cn": "遵守车道吧。", "example_meaning_en": "Let's stick to our lane."},
        "N2_1083": {"example_sentence": "（（謝）しゃ）ぜ（ぜ）つ（つ）し（し）ないで（で）ください。", "example_reading": "しゃぜつしないでください。", "example_meaning_cn": "请不要谢绝。", "example_meaning_en": "Please don't refuse/decline."},
        "N2_1084": {"example_sentence": "（（喋）しゃべ）り（り）すぎ（すぎ）ないで（で）ください。", "example_reading": "しゃべりすぎないでください。", "example_meaning_cn": "请不要说太多。", "example_meaning_en": "Please don't talk too much."},
        "N2_1085": {"example_sentence": "（（斜）しゃ）め（め）に（に）なら（なら）ないで（で）ください。", "example_reading": "しゃめにならないでください。", "example_meaning_cn": "请不要倾斜（歪斜）。", "example_meaning_en": "Please don't be slanted."},
        "N2_1086": {"example_sentence": "（（酒）しゅ）を（を）酌み（くみ）交わし（かわし）ましょう。", "example_reading": "しゅをくみかわしましょう。", "example_meaning_cn": "对酒当歌（饮酒）吧。", "example_meaning_en": "Let's share a drink together."},
        "N2_1087": {"example_sentence": "（（周）しゅう）を（を）一周（いっしゅう）し（し）ましょう。", "example_reading": "しゅうをいっしゅうしましょう。", "example_meaning_cn": "绕一周吧。", "example_meaning_en": "Let's go around once."},
        "N2_1088": {"example_sentence": "（（主）しゅ）を（を）大切（たいせつ）に（に）し（し）ましょう。", "example_reading": "しゅをたいせつにしましょう。", "example_meaning_cn": "珍惜主人（君主/主）吧。", "example_meaning_en": "Let's value the master/lord."},
        "N2_1089": {"example_sentence": "（（州）しゅう）に（に）行き（いき）ましょう。", "example_reading": "しゅうにいきましょう。", "example_meaning_cn": "去那个州吧。", "example_meaning_en": "Let's go to that state."},
        "N2_1090": {"example_sentence": "（（衆）しゅう）に（に）示し（しめし）てください。", "example_reading": "しゅうにしめしてください。", "example_meaning_cn": "请示众。", "example_meaning_en": "Please show the public."},
        "N2_1091": {"example_sentence": "（（収）しゅう）い（い）し（し）て（て）ください。", "example_reading": "しゅういしてください。", "example_meaning_cn": "请收受（或周围）。", "example_meaning_en": "Please accept/around."},
        "N2_1092": {"example_sentence": "（（収）しゅう）か（か）く（く）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "しゅうかくをたのしみましょう。", "example_meaning_cn": "享受收获吧。", "example_meaning_en": "Let's enjoy the harvest."},
        "N2_1093": {"example_sentence": "（（週）しゅう）か（か）ん（ん）し（し）を（を）読み（よみ）ます。", "example_reading": "しゅうかんしをよみます。", "example_meaning_cn": "读周刊。", "example_meaning_en": "Reading a weekly magazine."},
        "N2_1094": {"example_sentence": "（（収）しゅう）き（き）を（を）上げ（あげ）ましょう。", "example_reading": "しゅうきをあげましょう。", "example_meaning_cn": "提高收益（周期）吧。", "example_meaning_en": "Let's increase the profit/cycle."},
        "N2_1095": {"example_sentence": "（（集）しゅう）き（き）ょ（ょ）く（く）し（し）て（て）ください。", "example_reading": "しゅうきょくしてください。", "example_meaning_cn": "请终局（结尾）。", "example_meaning_en": "Please bring it to a close/finale."},
        "N2_1096": {"example_sentence": "（（祝）しゅう）ぎ（ぎ）を（を）包ん（つつん）で（て）ください。", "example_reading": "しゅうぎをつつんでください。", "example_meaning_cn": "请封礼金（喜钱）。", "example_meaning_en": "Please wrap the gift money."},
        "N2_1097": {"example_sentence": "（（集）しゅう）け（け）い（い）し（し）て（て）ください。", "example_reading": "しゅうけいしてください。", "example_meaning_cn": "请合计（汇总）。", "example_meaning_en": "Please aggregate/tally it up."},
        "N2_1098": {"example_sentence": "（（襲）しゅう）げ（げ）き（き）し（し）ないで（で）ください！ ", "example_reading": "しゅうげきしないでください！", "example_meaning_cn": "请不要袭击！", "example_meaning_en": "Please don't attack/raid!"},
        "N2_1099": {"example_sentence": "（（収）しゅう）し（し）を（を）合わせ（あわせ）て（て）ください。", "example_reading": "しゅうしをあわせてください。", "example_meaning_cn": "请做到收支平衡。", "example_meaning_en": "Please balance the income and expenditure."},
        "N2_1100": {"example_sentence": "（（終）しゅう）し（し）見守（みまも）り（り）まし（し）た。", "example_reading": "しゅうしみまもりました。", "example_meaning_cn": "始终守护着。", "example_meaning_en": "I watched over them from beginning to end."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N2_1100.")

if __name__ == "__main__":
    main()
