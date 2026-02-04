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
        "N1_1301": {"example_sentence": "（（良）よ）く（く）考え（かんがえ）て（て）ください。", "example_reading": "よくかんがえてください。", "example_meaning_cn": "请仔细考虑。", "example_meaning_en": "Please think it over carefully."},
        "N1_1302": {"example_sentence": "（（欲）よく）を（を）出さ（ださ）ないで（为）ください。", "example_reading": "よくをださないでください。", "example_meaning_cn": "不要起贪欲。", "example_meaning_en": "Please don't be greedy."},
        "N1_1303": {"example_sentence": "（（抑制）よくせい）し（し）て（て）ください。", "example_reading": "よくせいしてください。", "example_meaning_cn": "请抑制一下。", "example_meaning_en": "Please suppress / restrain it."},
        "N1_1304": {"example_sentence": "（（浴）よく）び（び）る（る）のを（を）楽しみ（たのしみ）ま（ま）しょ（しょ）う（う）。", "example_reading": "よくびるのをたのしみましょう。", "example_meaning_cn": "享受淋浴（或沐浴）吧。", "example_meaning_en": "Let's enjoy taking a bath / shower."},
        "N1_1305": {"example_sentence": "（（予）よ）く（く）に（に）し（し）て（て）ください。", "example_reading": "よくにしてください。", "example_meaning_cn": "请定为预备（或世界）。", "example_meaning_en": "Please make it preparation / world."},
        "N1_1306": {"example_sentence": "（（抑）よく）あ（あ）つ（つ）し（し）ないで（为）ください。", "example_reading": "よくあつしないでください。", "example_meaning_cn": "请不要压制（压迫）。", "example_meaning_en": "Please don't oppress / suppress."},
        "N1_1307": {"example_sentence": "（（翌）よく）じ（じ）つ（つ）を（を）待ち（まち）ま（ま）しょ（しょ）う（う）。", "example_reading": "よくじつを待ちましょう。", "example_meaning_cn": "等第二天吧。", "example_meaning_en": "Let's wait for the next day."},
        "N1_1308": {"example_sentence": "（（抑）よく）せ（せ）い（い）し（し）て（て）ください。", "example_reading": "よくせいしてください。", "example_meaning_cn": "请抑制。", "example_meaning_en": "Please restrain / curb it."},
        "N1_1309": {"example_sentence": "（（浴）よく）そ（そ）う（う）を（を）洗い（あらい）ま（ま）しょ（しょ）う（う）。", "example_reading": "よくそうをあらいましょう。", "example_meaning_cn": "洗浴缸吧。", "example_meaning_en": "Let's wash the bathtub."},
        "N1_1310": {"example_sentence": "（（欲）よく）た（た）い（い）に（に）し（し）ないで（为）ください。", "example_reading": "よくたいにしないでください。", "example_meaning_cn": "请不要作为欲（或已经满足）。", "example_meaning_en": "Please don't make it a desire / satisfied."},
        "N1_1311": {"example_sentence": "（（欲）よく）ば（ば）っ（っ）た（た）考（かんが）え（え）です。", "example_reading": "よくばったかんがえです。", "example_meaning_cn": "贪婪的想法。", "example_meaning_en": "It's a greedy idea."},
        "N1_1312": {"example_sentence": "（（浴）よく）び（び）る（る）のを（を）手伝っ（てつだっ）て（て）ください。", "example_reading": "よくびるのをてつだってください。", "example_meaning_cn": "请帮我旋转（或沐浴）。", "example_meaning_en": "Please help me rotate / take a bath."},
        "N1_1313": {"example_sentence": "（（欲）よく）ぼ（ぼ）う（う）を（を）抑え（おさえ）て（て）ください。", "example_reading": "よくぼうをおさえてください。", "example_meaning_cn": "请克制欲望。", "example_meaning_en": "Please control your desires."},
        "N1_1314": {"example_sentence": "（（予）よ）け（け）な（な）事（こと）を（を）し（し）ないで（为）ください。", "example_reading": "よけなことをしないでください。", "example_meaning_cn": "请不要做多余的事。", "example_meaning_en": "Please don't do anything unnecessary."},
        "N1_1315": {"example_sentence": "（（予）よ）けい（けい）な（な）心配（しんぱい）を（を）し（し）ないで（为）ください。", "example_reading": "よけいなしんぱいをしないでください。", "example_meaning_cn": "请不要多虑。", "example_meaning_en": "Please don't worry unnecessarily."},
        "N1_1316": {"example_sentence": "（（汚）よご）れ（れ）を（を）落とし（おとし）て（て）ください。", "example_reading": "よごれをおとしてください。", "example_meaning_cn": "请去除污垢。", "example_meaning_en": "Please remove the dirt / stain."},
        "N1_1317": {"example_sentence": "（（予）よ）こ（こ）せ（せ）て（て）ください。", "example_reading": "よこせてください。", "example_meaning_cn": "请给我（或交给我）。", "example_meaning_en": "Please give it to me / hand it over."},
        "N1_1318": {"example_sentence": "（（予）よ）こ（こ）た（た）わ（わ）る（る）のを（を）やめ（やめ）ましょう。", "example_reading": "よこたわるのをやめましょう。", "example_meaning_cn": "别再横躺着了。", "example_meaning_en": "Let's stop lying down."},
        "N1_1319": {"example_sentence": "（（予）よ）こ（こ）づ（づ）け（け）し（し）て（て）ください。", "example_reading": "よこづけしてください。", "example_meaning_cn": "请靠边停车（或横放）。", "example_meaning_en": "Please pull over to the side / place it alongside."},
        "N1_1320": {"example_sentence": "（（予）よ）こ（こ）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "よこなしをしないでください。", "example_meaning_cn": "请不要（说预言或闲聊）。", "example_meaning_en": "Please don't speak prophecies / talk."},
        "N1_1321": {"example_sentence": "（（予）よ）こ（こ）ば（ば）し（し）て（て）ください。", "example_reading": "よこばしてください。", "example_meaning_cn": "请使其横过（或已经横置）。", "example_meaning_en": "Please make it go across / place it horizontally."},
        "N1_1322": {"example_sentence": "（（予）よ）こ（こ）ひ（ひ）し（し）て（て）ください。", "example_reading": "よこひしてください。", "example_meaning_cn": "请使其横向（或已经横过）。", "example_meaning_en": "Please make it sideways / crosswise."},
        "N1_1323": {"example_sentence": "（（余）よ）さ（さ）を（を）感じ（かんじ）ます。", "example_reading": "よさをかんじます。", "example_meaning_cn": "感到余味（或优点）。", "example_meaning_en": "I feel the lingering charm / goodness."},
        "N1_1324": {"example_sentence": "（（予）よ）し（し）し（し）て（て）ください。", "example_reading": "よししてください。", "example_meaning_cn": "请准备（预习）。", "example_meaning_en": "Please prepare for the lesson."},
        "N1_1325": {"example_sentence": "（（予）よ）し（し）に（に）し（し）ないで（为）ください。", "example_reading": "よしにしないでください。", "example_meaning_cn": "请不要作为好（或适当）。", "example_meaning_en": "Please don't make it a 'good' / 'that's enough'."},
        "N1_1326": {"example_sentence": "（（予）よ）し（し）な（な）い（い）で（为）ください。", "example_reading": "よしないでください。", "example_meaning_cn": "请别做那种事（或无果）。", "example_meaning_en": "Please don't do that / it's pointless."},
        "N1_1327": {"example_sentence": "（（芳）よし）に（に）し（し）て（て）ください。", "example_reading": "よしにしてください。", "example_meaning_cn": "请定为芳（或已经芳香）。", "example_meaning_en": "Please make it fragrant / good."},
        "N1_1328": {"example_sentence": "（（予）よ）し（し）ゅ（ゅ）う（う）を（を）し（し）ましょう。", "example_reading": "よしゅうをしましょう。", "example_meaning_cn": "预习吧。", "example_meaning_en": "Let's do the preview / preparation for the lesson."},
        "N1_1329": {"example_sentence": "（（余）よ）し（し）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "よししょうしてください。", "example_meaning_cn": "请使其成形（或已经余震）。", "example_meaning_en": "Please shape it / have aftershocks."},
        "N1_1330": {"example_sentence": "（（予）よ）し（し）ん（ん）に（に）気（き）を（を）つけ（つけ）ま（ま）しょ（しょ）う（う）。", "example_reading": "よしんにきをつけましょう。", "example_meaning_cn": "注意余震吧。", "example_meaning_en": "Let's watch out for aftershocks."},
        "N1_1331": {"example_sentence": "（（予）よ）せ（せ）に（に）行き（いき）ま（ま）しょ（しょ）う（う）。", "example_reading": "よせいにいきましょう。", "example_meaning_cn": "去曲艺场（或聚集地）吧。", "example_meaning_en": "Let's go to the variety theater / gathering place."},
        "N1_1332": {"example_sentence": "（（予）よ）そ（そ）う（う）し（し）て（て）ください。", "example_reading": "よそうしてください。", "example_meaning_cn": "请预测。", "example_meaning_en": "Please predict / forecast it."},
        "N1_1333": {"example_sentence": "（（余）よ）そ（そ）う（う）し（し）て（て）ください。", "example_reading": "よそうしてください。", "example_meaning_cn": "请使其有余（或已经装好）。", "example_meaning_en": "Please make it surplus / serve it up."},
        "N1_1334": {"example_sentence": "（（予）よ）そ（そ）く（く）し（し）て（て）ください。", "example_reading": "よそくしてください。", "example_meaning_cn": "请预测。", "example_meaning_en": "Please predict / estimate it."},
        "N1_1335": {"example_sentence": "（（余）よ）だ（だ）ん（ん）を（を）許さ（ゆるさ）ない（ない）状況（じょうきょう）です。", "example_reading": "よだんをゆるさないじょうきょうです。", "example_meaning_cn": "不容预测（疏忽）的状况。", "example_meaning_en": "It's a situation that allows no prediction / negligence."},
        "N1_1336": {"example_sentence": "（（淀）よど）み（み）を（を）直し（なおし）て（て）ください。", "example_reading": "よどみをなおしてください。", "example_meaning_cn": "请修正淤积（或迟缓）处。", "example_meaning_en": "Please fix the stagnation / hesitation."},
        "N1_1337": {"example_sentence": "（（与）よ）に（に）し（し）て（て）ください。", "example_reading": "よにしてください。", "example_meaning_cn": "请定为给予（或世界）。", "example_meaning_en": "Please make it a gift / world."},
        "N1_1338": {"example_sentence": "（（予）よ）ば（ば）い（い）し（し）ないで（为）ください。", "example_reading": "よばいしないでください。", "example_meaning_cn": "请不要（求婚或诱拐）。", "example_meaning_en": "Please don't (propose / abduct)."},
        "N1_1339": {"example_sentence": "（（予）よ）ひ（ひ）し（し）て（て）ください。", "example_reading": "よひしてください。", "example_meaning_cn": "请使其备用（或已经准备）。", "example_meaning_en": "Please make it spare / ready."},
        "N1_1340": {"example_sentence": "（（予）よ）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "よふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1341": {"example_sentence": "（（予）よ）め（め）に（に）し（し）ないで（为）ください。", "example_reading": "よめにしないでください。", "example_meaning_cn": "请不要作为预言（或余晖）。", "example_meaning_en": "Please don't make it a prophecy / afterglow."},
        "N1_1342": {"example_sentence": "（（予）よ）め（め）い（い）を（を）全う（まっとう）し（し）ま（ま）しょ（しょ）う（う）。", "example_reading": "よめいをまっとうしましょう。", "example_meaning_cn": "度过余生吧。", "example_meaning_en": "Let's live our remaining years to the fullest."},
        "N1_1343": {"example_sentence": "（（余）よ）め（め）ん（ん）し（し）ないで（为）ください。", "example_reading": "よめんしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1344": {"example_sentence": "（（予）よ）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "よらんしないでください。", "example_meaning_cn": "请不要（紊乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1345": {"example_sentence": "（（予）よ）り（り）し（し）ないで（为）ください。", "example_reading": "よりしないでください。", "example_meaning_cn": "请不要（借用或假定）。", "example_meaning_en": "Please don't (borrow / assume)."},
        "N1_1346": {"example_sentence": "（（依）よ）り（り）か（か）かっ（かっ）て（て）ください。", "example_reading": "よりかかってください。", "example_meaning_cn": "请依靠（或依赖）。", "example_meaning_en": "Please lean on it / rely on it."},
        "N1_1347": {"example_sentence": "（（依）よ）り（り）どころ（ところ）を（を）見つけ（みつけ）ま（ま）しょ（しょ）う（う）。", "example_reading": "よりどころをみつけましょう。", "example_meaning_cn": "找个依靠处（根据）吧。", "example_meaning_en": "Let's find a place to rely on / basis."},
        "N1_1348": {"example_sentence": "（（選）よ）り（り）どり（どり）え（え）ら（ら）べ（べ）ま（ま）す（す）。", "example_reading": "よりどりえらべます。", "example_meaning_cn": "可以随心所欲地挑选。", "example_meaning_en": "You can pick as many as you like."},
        "N1_1349": {"example_sentence": "（（選）よ）り（り）わ（わ）け（け）て（て）ください。", "example_reading": "よりわけてください。", "example_meaning_cn": "请分选出来。", "example_meaning_en": "Please sort them out."},
        "N1_1350": {"example_sentence": "（（予）よ）る（る）べ（べ）な（な）い（い）身（み）です。", "example_reading": "よるべないみです。", "example_meaning_cn": "举目无亲（无依无靠）的身世。", "example_meaning_en": "It's a state of having no one to rely on."},
        "N1_1351": {"example_sentence": "（（予）よ）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "よれいしないでください。", "example_meaning_cn": "请不要（效法或同样）。", "example_meaning_en": "Please don't (follow suit / be the same)."},
        "N1_1352": {"example_sentence": "（（予）よ）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "よろをとおしてください。", "example_meaning_cn": "请（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1353": {"example_sentence": "（（万）よろ）ず（ず）の（の）神（かみ）を（を）信じ（しんじ）ま（ま）す（す）か。", "example_reading": "よろずのかみをしんじますか。", "example_meaning_cn": "相信万物（八百万）神灵吗？", "example_meaning_en": "Do you believe in the myriad of gods?"},
        "N1_1354": {"example_sentence": "（（喜）よろこ）ば（ば）せ（せ）て（て）ください。", "example_reading": "よろこばせてください。", "example_meaning_cn": "请让我高兴（或取悦）。", "example_meaning_en": "Please make me happy / please me."},
        "N1_1355": {"example_sentence": "（（宜）よろ）し（し）く（く）願い（ねがい）ま（ま）す（す）。", "example_reading": "よろしくねがいます。", "example_meaning_cn": "请多指教。", "example_meaning_en": "Pleasure to meet you / please be kind to me."},
        "N1_1356": {"example_sentence": "（（弱）よわ）み（み）を（を）見せ（みせ）ないで（为）ください。", "example_reading": "よわみをみせないでください。", "example_meaning_cn": "请不要示弱。", "example_meaning_en": "Please don't show any weakness."},
        "N1_1357": {"example_sentence": "（（弱）よわ）る（る）のを（を）やめ（やめ）ましょう。", "example_reading": "よわるのをやめましょう。", "example_meaning_cn": "别再衰弱下去了。", "example_meaning_en": "Let's stop getting weak / depressed."},
        "N1_1358": {"example_sentence": "（（予）よ）わ（わ）し（し）ないで（为）ください。", "example_reading": "よわしないでください。", "example_meaning_cn": "请不要（和谈或预备）。", "example_meaning_en": "Please don't (be at peace / prepare)."},
        "N1_1359": {"example_sentence": "（（来）らい）い（い）し（し）て（て）ください。", "example_reading": "らいいしてください。", "example_meaning_cn": "请使其到来（或已经准备）。", "example_meaning_en": "Please make it come / ready."},
        "N1_1360": {"example_sentence": "（（来）らい）き（き）ゃ（ゃ）く（く）を（を）迎え（むかえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "らいきゃくをむかえましょう。", "example_meaning_cn": "迎接来客吧。", "example_meaning_en": "Let's welcome the guests."},
        "N1_1361": {"example_sentence": "（（来）らい）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "らいしんしないでください。", "example_meaning_cn": "请不要（来信或来访）。", "example_meaning_en": "Please don't (send a letter / visit)."},
        "N1_1362": {"example_sentence": "（（来）らい）じ（じ）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "らいじょうしてください。", "example_meaning_cn": "请光临（来场）。", "example_meaning_en": "Please come to the venue / visit."},
        "N1_1363": {"example_sentence": "（（来）らい）せ（せ）い（い）を（を）信じ（しんじ）ま（ま）す（す）か。", "example_reading": "らいせいをしんじますか。", "example_meaning_cn": "相信来世（下辈子）吗？", "example_meaning_en": "Do you believe in the afterlife?"},
        "N1_1364": {"example_sentence": "（（落）らく）え（え）ん（ん）を（を）探し（さがし）ま（ま）しょ（しょ）う（う）。", "example_reading": "らくえんをさがしましょう。", "example_meaning_cn": "寻找乐园（天堂）吧。", "example_meaning_en": "Let's search for paradise."},
        "N1_1365": {"example_sentence": "（（落）らく）が（が）き（き）を（を）し（し）ないで（为）ください。", "example_reading": "らくがきをしないでください。", "example_meaning_cn": "请不要乱涂乱画。", "example_meaning_en": "Please don't scribble / graffiti."},
        "N1_1366": {"example_sentence": "（（落）らく）さ（さ）つ（つ）し（し）て（て）ください。", "example_reading": "らくさつしてください。", "example_meaning_cn": "请使其（或已经中标）。", "example_meaning_en": "Please win the bid / successful auction."},
        "N1_1367": {"example_sentence": "（（落）らく）じ（じ）つ（つ）し（し）ないで（为）ください。", "example_reading": "らくじつしないでください。", "example_meaning_cn": "请不要（落日或失败）。", "example_meaning_en": "Please don't (be sunset / fail)."},
        "N1_1368": {"example_sentence": "（（落）らく）た（た）ん（ん）し（し）ないで（为）ください。", "example_reading": "らくたんしないでください。", "example_meaning_cn": "请不要灰心丧气。", "example_meaning_en": "Please don't be discouraged / lose heart."},
        "N1_1369": {"example_sentence": "（（落）らく）ち（ち）ょ（ょ）く（く）し（し）ないで（为）ください。", "example_reading": "らくちょくしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1370": {"example_sentence": "（（裸）ら）た（た）い（い）に（に）なら（なら）ないで（为）ください。", "example_reading": "らたいにならないでください。", "example_meaning_cn": "请不要裸体。", "example_meaning_en": "Please don't be naked."},
        "N1_1371": {"example_sentence": "（（拉）ら）し（し）し（し）ないで（为）ください。", "example_reading": "らししないでください。", "example_meaning_cn": "请不要（拉致或拉索）。", "example_meaning_en": "Please don't (abduct / drag)."},
        "N1_1372": {"example_sentence": "（（裸）ら）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "らしんしないでください。", "example_meaning_cn": "请不要（裸体或裸露）。", "example_meaning_en": "Please don't (be naked / expose)."},
        "N1_1373": {"example_sentence": "（（裸）ら）せ（せ）つ（つ）し（し）ないで（为）ください。", "example_reading": "らせつしないでください。", "example_meaning_cn": "请不要（裸体或罗刹）。", "example_meaning_en": "Please don't (be naked / demon)."},
        "N1_1374": {"example_sentence": "（（裸）ら）だ（だ）ん（ん）し（し）ないで（为）ください。", "example_reading": "らだんしないでください。", "example_meaning_cn": "请不要（裸体或论断）。", "example_meaning_en": "Please don't (be naked / judge)."},
        "N1_1375": {"example_sentence": "（（裸）ら）に（に）なら（なら）ないで（为）ください。", "example_reading": "らにならないでください。", "example_meaning_cn": "请不要裸体。", "example_meaning_en": "Please don't be naked."},
        "N1_1376": {"example_sentence": "（（裸）ら）ま（ま）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "らまわらないでください。", "example_meaning_cn": "请不要（赤裸或绕道）。", "example_meaning_en": "Please don't (be naked / go around)."},
        "N1_1377": {"example_sentence": "（（乱）らん）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "らんしんしないでください。", "example_meaning_cn": "请不要精神错乱。", "example_meaning_en": "Please don't go out of your mind / be insane."},
        "N1_1378": {"example_sentence": "（（乱）らん）せ（せ）つ（つ）し（し）ないで（为）ください。", "example_reading": "らんせつしないでください。", "example_meaning_cn": "请不要（乱设或紊乱）。", "example_meaning_en": "Please don't (install randomly / disturb)."},
        "N1_1379": {"example_sentence": "（（乱）らん）だ（だ）ん（ん）し（し）ないで（为）ください。", "example_reading": "らんだんしないでください。", "example_meaning_cn": "请不要（乱谈或紊乱）。", "example_meaning_en": "Please don't (talk randomly / disturb)."},
        "N1_1380": {"example_sentence": "（（乱）らん）に（に）なら（なら）ないで（为）ください。", "example_reading": "らんにならないでください。", "example_meaning_cn": "请不要乱糟糟的。", "example_meaning_en": "Please don't be in disorder / chaotic."},
        "N1_1381": {"example_sentence": "（（乱）らん）ぼ（ぼ）う（う）な（な）口（くち）を（を）きか（きか）ないで（为）ください。", "example_reading": "らんぼうなくちをきかないでください。", "example_meaning_cn": "别出言不逊。", "example_meaning_en": "Please don't speak rudely / violently."},
        "N1_1382": {"example_sentence": "（（裸）ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "らんしないでください。", "example_meaning_cn": "请不要（赤裸或乱来）。", "example_meaning_en": "Please don't (be naked / act wildly)."},
        "N1_1383": {"example_sentence": "（（利）り）あ（あ）い（い）を（を）楽しみ（たのしみ）ま（ま）しょ（しょ）う（う）。", "example_reading": "りあいをたのしみましょう。", "example_meaning_cn": "享受利益（或利息）吧。", "example_meaning_en": "Let's enjoy the profit / interest."},
        "N1_1384": {"example_sentence": "（（理）り）う（う）を（を）考え（かんがえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "りうをかんがえましょう。", "example_meaning_cn": "考虑理由（或理应）吧。", "example_meaning_en": "Let's think about the reason / principle."},
        "N1_1385": {"example_sentence": "（（利）り）え（え）き（き）を（を）上げ（あげ）ま（ま）しょ（しょ）う（う）。", "example_reading": "りえきをあげましょう。", "example_meaning_cn": "提高利润（利益）吧。", "example_meaning_en": "Let's increase the profit / benefit."},
        "N1_1386": {"example_sentence": "（（理）り）か（か）い（い）を（を）深め（ふかめ）ま（ま）しょ（しょ）う（う）。", "example_reading": "りかいをふかめましょう。", "example_meaning_cn": "加深理解吧。", "example_meaning_en": "Let's deepen our understanding."},
        "N1_1387": {"example_sentence": "（（理）り）が（が）し（し）ないで（为）ください。", "example_reading": "りがしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1388": {"example_sentence": "（（理）り）き（き）に（に）なら（なら）ないで（为）ください。", "example_reading": "りきにならないでください。", "example_meaning_cn": "请不要作为理（或已经解释）。", "example_meaning_en": "Please don't be (logical / interpreted)."},
        "N1_1389": {"example_sentence": "（（陸）りく）を（を）歩き（あるき）ま（ま）しょ（しょ）う（う）。", "example_reading": "りくをあるきましょう。", "example_meaning_cn": "在陆地上走吧。", "example_meaning_en": "Let's walk on land."},
        "N1_1390": {"example_sentence": "（（利）り）こ（こ）て（て）き（き）に（に）なら（なら）ないで（为）ください。", "example_reading": "りこてきにならないでください。", "example_meaning_cn": "不要利己主义（自私）。", "example_meaning_en": "Please don't be selfish / egoistic."},
        "N1_1391": {"example_sentence": "（（理）り）さ（さ）を（を）保っ（たもっ）て（て）ください。", "example_reading": "りさをたもってください。", "example_meaning_cn": "请保持理智（或离散）。", "example_meaning_en": "Please maintain reason / separation."},
        "N1_1392": {"example_sentence": "（（利）り）さ（さ）い（い）し（し）ないで（为）ください。", "example_reading": "りさいしないでください。", "example_meaning_cn": "请不要受灾（或已经遭受）。", "example_meaning_en": "Please don't suffer a disaster."},
        "N1_1393": {"example_sentence": "（（利）り）し（し）を（を）払い（はらい）ま（ま）しょ（しょ）う（う）。", "example_reading": "りしをはらいましょう。", "example_meaning_cn": "付利息吧。", "example_meaning_en": "Let's pay the interest."},
        "N1_1394": {"example_sentence": "（（理）り）し（し）ゅ（ゅ）う（う）を（を）済ませ（すませ）ま（ま）しょ（しょ）う（う）。", "example_reading": "りしゅうをすませましょう。", "example_meaning_cn": "完成修业（课程学习）吧。", "example_meaning_en": "Let's complete the course / study."},
        "N1_1395": {"example_sentence": "（（理）り）せ（せ）い（い）を（を）保っ（たもっ）て（て）ください。", "example_reading": "りせいをたもってください。", "example_meaning_cn": "请保持理性。", "example_meaning_en": "Please maintain your reason / rationality."},
        "N1_1396": {"example_sentence": "（（離）り）そ（そ）う（う）を（を）追い（おい）ま（ま）しょ（しょ）う（う）。", "example_reading": "りそうを追いましょう。", "example_meaning_cn": "追求理想吧。", "example_meaning_en": "Let's pursue our ideals."},
        "N1_1397": {"example_sentence": "（（利）り）そ（そ）く（く）を（を）計算（けいさん）し（し）ま（ま）しょ（しょ）う（う）。", "example_reading": "りそくをけいさんしましょう。", "example_meaning_cn": "计算利息吧。", "example_meaning_en": "Let's calculate the interest."},
        "N1_1398": {"example_sentence": "（（理）り）た（た）い（い）し（し）て（て）ください。", "example_reading": "りたいしてください。", "example_meaning_cn": "请使其成形（或已经离队）。", "example_meaning_en": "Please make it shape / withdraw."},
        "N1_1399": {"example_sentence": "（（立）りっ）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "りっしんしないでください。", "example_meaning_cn": "请不要立身（出人头地）。", "example_meaning_en": "Please don't (succeed in life / be promoted)."},
        "N1_1400": {"example_sentence": "（（立）りっ）し（し）ゅ（ゅ）う（う）の（の）日（ひ）です。", "example_reading": "りっしゅうのひです。", "example_meaning_cn": "是立秋之日。", "example_meaning_en": "It's the day of the beginning of autumn."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_1400.")

if __name__ == "__main__":
    main()
