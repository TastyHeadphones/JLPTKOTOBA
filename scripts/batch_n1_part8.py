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
        "N1_701": {"example_sentence": "（（外）がい）し（し）し（し）て（て）ください。", "example_reading": "がいししてください。", "example_meaning_cn": "请（排除或在）外。进行投资。", "example_meaning_en": "Please (exclude / be) outside. / Invest in foreign capital."},
        "N1_702": {"example_sentence": "（（階）かい）し（し）て（て）ください。", "example_reading": "かいしてください。", "example_meaning_cn": "请定为等级（或楼层）。", "example_meaning_en": "Please rank it / set the level."},
        "N1_703": {"example_sentence": "（（怪）かい）し（し）ないで（で）ください。", "example_reading": "かいしないでください。", "example_meaning_cn": "请不要（惊怪或怀疑）。", "example_meaning_en": "Please don't (be surprised / doubt)."},
        "N1_704": {"example_sentence": "（（快）かい）し（し）ゃ（ゃ）く（く）し（し）て（て）ください。", "example_reading": "かいしゃくしてください。", "example_meaning_cn": "请进行快嚼（爽快吃）或解释。", "example_meaning_en": "Please interpret it / enjoy it thoroughly."},
        "N1_705": {"example_sentence": "（（改）かい）し（し）ゅ（ゅ）う（う）し（し）て（て）ください。", "example_reading": "かいしゅうしてください。", "example_meaning_cn": "请进行改修（修复）。", "example_meaning_en": "Please repair / renovate it."},
        "N1_706": {"example_sentence": "（（回収）かいしゅう）し（し）て（て）ください。", "example_reading": "かいしゅうしてください。", "example_meaning_cn": "请回收。", "example_meaning_en": "Please collect / recover it."},
        "N1_707": {"example_sentence": "（（改）かい）し（し）ん（ん）し（し）て（て）ください。", "example_reading": "かいしんしてください。", "example_meaning_cn": "请改过自新。", "example_meaning_en": "Please repent / mend your ways."},
        "N1_708": {"example_sentence": "（（快）かい）し（し）ん（ん）の（の）出来（でき）ばえ（ばえ）です。", "example_reading": "かいしんのできばえです。", "example_meaning_cn": "那是令人满意的佳作。", "example_meaning_en": "It's a most satisfying / brilliant piece of work."},
        "N1_709": {"example_sentence": "（（階）かい）す（す）う（う）を（を）数え（かぞえ）ましょう。", "example_reading": "かいすうをかぞえましょう。", "example_meaning_cn": "数数层数（或次数）吧。", "example_meaning_en": "Let's count the number of floors / times."},
        "N1_710": {"example_sentence": "（（快）かい）せ（せ）い（い）の（の）空（そら）です。", "example_reading": "かいせいのそらです。", "example_meaning_cn": "万里无云的晴空。", "example_meaning_en": "It's a clear / cloudless sky."},
        "N1_711": {"example_sentence": "（（海）かい）せ（せ）い（い）し（し）ないで（で）ください。", "example_reading": "かいせいしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_712": {"example_sentence": "（（改）かい）せ（せ）つ（つ）し（し）て（て）ください。", "example_reading": "かいせつしてください。", "example_meaning_cn": "请改设（或设立）。", "example_meaning_en": "Please re-establish / set up."},
        "N1_713": {"example_sentence": "（（解）かい）せ（せ）つ（つ）を（を）聞い（きい）て（て）ください。", "example_reading": "かいせつをきいてください。", "example_meaning_cn": "请听讲解。", "example_meaning_en": "Please listen to the explanation."},
        "N1_714": {"example_sentence": "（（快）かい）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "かいぜんとしています。", "example_meaning_cn": "快然（舒畅）着。", "example_meaning_en": "It feels pleasant / comfortable."},
        "N1_715": {"example_sentence": "（（改）かい）ぜ（ぜ）ん（ん）し（し）て（て）ください。", "example_reading": "かいぜんしてください。", "example_meaning_cn": "请改善。", "example_meaning_en": "Please improve it."},
        "N1_716": {"example_sentence": "（（海）かい）せ（せ）ん（ん）を（を）防ぎ（ふせぎ）ましょう。", "example_reading": "かいせんをふせぎましょう。", "example_meaning_cn": "防御海战（或开战）吧。", "example_meaning_en": "Let's prevent the naval battle / start of war."},
        "N1_717": {"example_sentence": "（（階）かい）そ（そ）に（に）なり（なり）たい（たい）です。", "example_reading": "かいそになりたいです。", "example_meaning_cn": "想成为（某个领域的）鼻祖。", "example_meaning_en": "I want to be the founder / patriarch."},
        "N1_718": {"example_sentence": "（（改）かい）そ（そ）う（う）し（し）て（て）ください。", "example_reading": "かいそうしてください。", "example_meaning_cn": "请改换包装（或装修）。", "example_meaning_en": "Please repackage / renovate it."},
        "N1_719": {"example_sentence": "（（回）かい）そ（そ）う（う）し（し）て（て）ください。", "example_reading": "かいそうしてください。", "example_meaning_cn": "请回送（或回想）。", "example_meaning_en": "Please send it back / recall it."},
        "N1_720": {"example_sentence": "（（階）かい）そ（そ）う（う）を（を）意識（いしき）し（し）て（て）ください。", "example_reading": "かいそうをいしきしてください。", "example_meaning_cn": "请意识到阶层。", "example_meaning_en": "Please be aware of the social class / layer."},
        "N1_721": {"example_sentence": "（（海）かい）そ（そ）う（う）を（を）見（み）ま（ま）しょ（しょ）う（う）。", "example_reading": "かいそうをみましょう。", "example_meaning_cn": "看海藻吧。", "example_meaning_en": "Let's see the seaweed."},
        "N1_722": {"example_sentence": "（（解）かい）そ（そ）く（く）し（し）ないで（で）ください。", "example_reading": "かいそくしないでください。", "example_meaning_cn": "请不要（解锁或快速）。", "example_meaning_en": "Please don't (unlock / be high-speed)."},
        "N1_723": {"example_sentence": "（（外）かい）だ（だ）ん（ん）し（し）ないで（で）ください。", "example_reading": "かいだんしないでください。", "example_meaning_cn": "请不要（下楼或谈话）。", "example_meaning_en": "Please don't (go down the stairs / talk)."},
        "N1_724": {"example_sentence": "（（会）かい）た（た）い（い）し（し）て（て）ください。", "example_reading": "かいたいしてください。", "example_meaning_cn": "请解体（或拆卸）。", "example_meaning_en": "Please dismantle / disassemble it."},
        "N1_725": {"example_sentence": "（（改）かい）た（た）く（く）し（し）て（て）ください。", "example_reading": "かいたくしてください。", "example_meaning_cn": "请开拓。", "example_meaning_en": "Please pioneer / cultivate it."},
        "N1_726": {"example_sentence": "（（快）かい）だ（だ）く（く）し（し）て（て）ください。", "example_reading": "かいだくしてください。", "example_meaning_cn": "请欣然允诺。", "example_meaning_en": "Please give your ready consent."},
        "N1_727": {"example_sentence": "（（海）かい）ち（ち）く（く）し（し）て（て）ください。", "example_reading": "かいちくしてください。", "example_meaning_cn": "请改筑（改建）。", "example_meaning_en": "Please rebuild / reconstruct it."},
        "N1_728": {"example_sentence": "（（改）かい）ち（ち）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "かいちょうしてください。", "example_meaning_cn": "请改订（修正）。", "example_meaning_en": "Please revise it."},
        "N1_729": {"example_sentence": "（（快）かい）ち（ち）ょ（ょ）う（う）な（な）走（はし）り（り）です。", "example_reading": "かいちょうなはしりです。", "example_meaning_cn": "轻快的跑（状态良好）。", "example_meaning_en": "It's a smooth / good run."},
        "N1_730": {"example_sentence": "（（海）かい）て（て）い（い）に（に）降り（おり）ましょう。", "example_reading": "かいていにおりましょう。", "example_meaning_cn": "潜入海底吧。", "example_meaning_en": "Let's go down to the seabed."},
        "N1_731": {"example_sentence": "（（改）かい）て（て）い（い）を（を）し（し）て（て）ください。", "example_reading": "かいていをしてください。", "example_meaning_cn": "请进行修订。", "example_meaning_en": "Please revise / amend it."},
        "N1_732": {"example_sentence": "（（街）がい）て（て）き（き）に（に）なり（なり）たい（たい）です。", "example_reading": "がいてきになりたいです。", "example_meaning_cn": "想成为外界的（或外部的）。", "example_meaning_en": "I want to be external / outward."},
        "N1_733": {"example_sentence": "（（快）かい）て（て）き（き）な（な）暮らし（くらし）です。", "example_reading": "かいてきなくらしです。", "example_meaning_cn": "舒适的生活。", "example_meaning_en": "It's a comfortable life."},
        "N1_734": {"example_sentence": "（（回）かい）て（て）ん（ん）し（し）て（て）ください。", "example_reading": "かいてんしてください。", "example_meaning_cn": "请旋转（或开店）。", "example_meaning_en": "Please rotate / open the store."},
        "N1_735": {"example_sentence": "（（海）かい）ど（ど）お（お）くな（な）事（こと）を（を）し（し）ないで（で）ください。", "example_reading": "かいどおくなことをしないでください。", "example_meaning_cn": "请不要做（海事或延误）的事。", "example_meaning_en": "Please don't do anything that (relates to the sea / delays)."},
        "N1_736": {"example_sentence": "（（解）かい）ど（ど）く（く）し（し）て（て）ください。", "example_reading": "かいどくしてください。", "example_meaning_cn": "请解读（或购读）。", "example_meaning_en": "Please decipher / read it."},
        "N1_737": {"example_sentence": "（（街）がい）に（に）行き（いき）ましょう。", "example_reading": "がいにいきましょう。", "example_meaning_cn": "去街上吧。", "example_meaning_en": "Let's go to the town / street."},
        "N1_738": {"example_sentence": "（（飼）かい）に（に）し（し）ないで（で）ください。", "example_reading": "かいにしないでください。", "example_meaning_cn": "请不要作为饲养（或购买）。", "example_meaning_en": "Please don't keep it as a pet / buy it."},
        "N1_739": {"example_sentence": "（（快）かい）に（に）し（し）て（て）ください。", "example_reading": "かいにしてください。", "example_meaning_cn": "请使其愉快（或已经康复）。", "example_meaning_en": "Please keep it pleasant / recovery."},
        "N1_740": {"example_sentence": "（（外）がい）に（に）し（し）てください。", "example_reading": "がいにしてください。", "example_meaning_cn": "请放在外面。", "example_meaning_en": "Please put it outside."},
        "N1_741": {"example_sentence": "（（改）かい）に（に）し（し）て（て）ください。", "example_reading": "かいにしてください。", "example_meaning_cn": "请定为更改（或已经修改）。", "example_meaning_en": "Please mark it as revised."},
        "N1_742": {"example_sentence": "（（海）かい）に（に）行っ（いっ）て（て）ください。", "example_reading": "かいにいってください。", "example_meaning_cn": "请去海边。", "example_meaning_en": "Please go to the sea / ocean."},
        "N1_743": {"example_sentence": "（（皆）かい）に（に）な（な）ら（ら）わ（わ）ないで（为）ください。", "example_reading": "かいにならわないでください。", "example_meaning_cn": "请不要效仿大家。", "example_meaning_en": "Please don't follow everyone else."},
        "N1_744": {"example_sentence": "（（快）かい）ね（ね）ん（ん）し（し）て（得）ください。", "example_reading": "かいねんしてください。", "example_meaning_cn": "请获得（快感或获得）。", "example_meaning_en": "Please get (pleasure / obtain)."},
        "N1_745": {"example_sentence": "（（概）がい）ね（ね）ん（ん）を（を）理解（りかい）し（し）ましょう。", "example_reading": "がいねんをりかいしましょう。", "example_meaning_cn": "理解概念吧。", "example_meaning_en": "Let's understand the concept."},
        "N1_746": {"example_sentence": "（（改）かい）ね（ね）ん（ん）し（し）ないで（で）ください。", "example_reading": "かいねんしないでください。", "example_meaning_cn": "请不要（改变或已经修改）。", "example_meaning_en": "Please don't (alter / change)."},
        "N1_747": {"example_sentence": "（（外）がい）は（は）あり（あり）ません。", "example_reading": "がいわありません。", "example_meaning_cn": "没有危害（或外面）。", "example_meaning_en": "There is no harm / nothing outside."},
        "N1_748": {"example_sentence": "（（改）かい）ば（ば）な（な）し（し）を（を）し（し）て（て）ください。", "example_reading": "かいばなしをしてください。", "example_meaning_cn": "请进行谈话（或解释）。", "example_meaning_en": "Please speak / explain."},
        "N1_749": {"example_sentence": "（（開）かい）ぱ（ぱ）ん（ん）し（し）て（て）ください。", "example_reading": "かいぱんしてください。", "example_meaning_cn": "请开启（或开盘）。", "example_meaning_en": "Please open / start the market."},
        "N1_750": {"example_sentence": "（（海）かい）は（は）ら（ら）わ（わ）ないで（で）ください。", "example_reading": "かいはらわないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_751": {"example_sentence": "（（開）かい）は（は）つ（つ）し（し）て（て）ください。", "example_reading": "かいはつしてください。", "example_meaning_cn": "请开发。", "example_meaning_en": "Please develop it."},
        "N1_752": {"example_sentence": "（（海）かい）ば（ば）つ（つ）を（を）測り（はかり）ましょう。", "example_reading": "かいばつをはかりましょう。", "example_meaning_cn": "测量海拔吧。", "example_meaning_en": "Let's measure the altitude (above sea level)."},
        "N1_753": {"example_sentence": "（（快）かい）び（び）ん（ん）し（し）て（て）ください。", "example_reading": "かいびんしてください。", "example_meaning_cn": "请派快船（或快报）。", "example_meaning_en": "Please send it by fast boat / express mail."},
        "N1_754": {"example_sentence": "（（開）かい）ふ（ふ）う（う）し（し）て（て）ください。", "example_reading": "かいふうしてください。", "example_meaning_cn": "请拆封（开封）。", "example_meaning_en": "Please unseal / open the envelope."},
        "N1_755": {"example_sentence": "（（改）かい）ふ（ふ）く（く）し（し）て（て）ください。", "example_reading": "かいふくしてください。", "example_meaning_cn": "请进行修复（或康复）。", "example_meaning_en": "Please recover / restore it."},
        "N1_756": {"example_sentence": "（（快）かい）ふ（ふ）く（く）を（を）祈り（いのり）ましょう。", "example_reading": "かいふくをいのりましょう。", "example_meaning_cn": "祈祷早日康复吧。", "example_meaning_en": "Let's pray for a speedy recovery."},
        "N1_757": {"example_sentence": "（（外）がい）ぶ（ぶ）の（の）意見（いけん）を（を）聞き（きき）ましょう。", "example_reading": "がいぶのいけんをききましょう。", "example_meaning_cn": "听听外部的意见吧。", "example_meaning_en": "Let's listen to external opinions."},
        "N1_758": {"example_sentence": "（（快）かい）ほ（ほう）し（し）ないで（で）ください。", "example_reading": "かいほうしないでください。", "example_meaning_cn": "请不要（快步或释放）。", "example_meaning_en": "Please don't (walk fast / release)."},
        "N1_759": {"example_sentence": "（（開）かい）ほ（ほう）し（し）て（て）ください。", "example_reading": "かいほうしてください。", "example_meaning_cn": "请开放。", "example_meaning_en": "Please open / make it public."},
        "N1_760": {"example_sentence": "（（解）かい）ほ（ほう）し（し）て（て）ください。", "example_reading": "かいほうしてください。", "example_meaning_cn": "请解开（释放）。", "example_meaning_en": "Please release / set free."},
        "N1_761": {"example_sentence": "（（介）かい）ほ（ほう）し（し）て（て）ください。", "example_reading": "かいほうしてください。", "example_meaning_cn": "请进行护理（或介抱）。", "example_meaning_en": "Please care for / look after him."},
        "N1_762": {"example_sentence": "（（外）がい）ほ（ほう）し（し）ないで（为）ください。", "example_reading": "がいほうしないでください。", "example_meaning_cn": "请不要在外面。", "example_meaning_en": "Please don't be outside."},
        "N1_763": {"example_sentence": "（（改）かい）ま（ま）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "かいまわらないでください。", "example_meaning_cn": "请不要（绕道或改变）。", "example_meaning_en": "Please don't (go around / change)."},
        "N1_764": {"example_sentence": "（（解）かい）め（め）い（い）し（し）て（て）ください。", "example_reading": "かいめいしてください。", "example_meaning_cn": "请解明（阐明）。", "example_meaning_en": "Please elucidate / clarify it."},
        "N1_765": {"example_sentence": "（（快）かい）め（め）い（い）を（を）感じ（かんじ）ます。", "example_reading": "かいめいをかんじます。", "example_meaning_cn": "感受到快鸣（或愉悦）。", "example_meaning_en": "I feel the pleasant sound / joy."},
        "N1_766": {"example_sentence": "（（改）かい）め（め）い（い）し（し）て（て）ください。", "example_reading": "かいめいしてください。", "example_meaning_cn": "请改名。", "example_meaning_en": "Please change the name."},
        "N1_767": {"example_sentence": "（（海）かい）め（め）ん（ん）が（が）上昇（じょうしょう）し（し）て（て）います。", "example_reading": "かいめんがじょうしょうしています。", "example_meaning_cn": "海平面正在上升。", "example_meaning_en": "The sea level is rising."},
        "N1_768": {"example_sentence": "（（改）かい）も（も）の（の）に（に）なり（なり）たい（たい）です。", "example_reading": "かいものになりたいです。", "example_meaning_cn": "想成为（改过的）人。", "example_meaning_en": "I want to be a reformed person."},
        "N1_769": {"example_sentence": "（（改）かい）ら（ら）ん（ん）し（し）ないで（で）ください。", "example_reading": "かいらんしないでください。", "example_meaning_cn": "请不要（修改或传阅）。", "example_meaning_en": "Please don't (alter / circulate)."},
        "N1_770": {"example_sentence": "（（改）かい）り（り）し（し）ないで（为）ください。", "example_reading": "かいりしないでください。", "example_meaning_cn": "请不要（乖离或改变）。", "example_meaning_en": "Please don't (be estranged / change)."},
        "N1_771": {"example_sentence": "（（解）かい）り（り）し（し）て（て）ください。", "example_reading": "かいりしてください。", "example_meaning_cn": "请定为理解（或处理）。", "example_meaning_en": "Please understand / deal with it."},
        "N1_772": {"example_sentence": "（（快）かい）り（り）ょ（ょ）く（く）を（を）見せ（みせ）て（て）ください。", "example_reading": "かいりょくをみせてください。", "example_meaning_cn": "请大显神威（怪力）。", "example_meaning_en": "Please show me your superhuman strength."},
        "N1_773": {"example_sentence": "（（海）かい）り（り）ゅう（ゅう）を（を）調べ（しらべ）ましょう。", "example_reading": "かいりゅうをしらべましょう。", "example_meaning_cn": "调查洋流吧。", "example_meaning_en": "Let's investigate the ocean current."},
        "N1_774": {"example_sentence": "（（改）かい）り（り）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "かいりょうしてください。", "example_meaning_cn": "请改良（改进）。", "example_meaning_en": "Please improve / upgrade it."},
        "N1_775": {"example_sentence": "（（回）かい）り（り）ゅう（ゅう）し（し）ないで（为）ください。", "example_reading": "かいりゅうしないでください。", "example_meaning_cn": "请不要（回流或循环）。", "example_meaning_en": "Please don't (backflow / circulate)."},
        "N1_776": {"example_sentence": "（（回）かい）る（る）のを（を）手伝っ（てつだっ）て（て）ください。", "example_reading": "かいるのわてつだってください。", "example_meaning_cn": "请帮我旋转（或回去）。", "example_meaning_en": "Please help me rotate / return."},
        "N1_777": {"example_sentence": "（（外）がい）れ（れ）い（い）を（を）受け（うけ）て（て）ください。", "example_reading": "がいれいをうけてください。", "example_meaning_cn": "请接收例外的待遇（或外例）。", "example_meaning_en": "Please receive extra-legal / exceptional treatment."},
        "N1_778": {"example_sentence": "（（皆）かい）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "かいれいしないでください。", "example_meaning_cn": "请不要效法大家。", "example_meaning_en": "Please don't follow everyone else."},
        "N1_779": {"example_sentence": "（（改）かい）ろ（ろ）し（し）ないで（为）ください。", "example_reading": "かいろしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_780": {"example_sentence": "（（回）かい）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "かいろをとおしてください。", "example_meaning_cn": "请接通电路（或回路）。", "example_meaning_en": "Please complete the circuit / path."},
        "N1_781": {"example_sentence": "（（外）がい）わ（わ）し（し）ないで（和）ください。", "example_reading": "がいわしないでください。", "example_meaning_cn": "请不要（和谈或对外）。", "example_meaning_en": "Please don't (be at peace / be outward)."},
        "N1_782": {"example_sentence": "（（皆）かい）わ（わ）し（し）ないで（和）ください。", "example_reading": "かいわしないでください。", "example_meaning_cn": "请不要（效仿或一致）。", "example_meaning_en": "Please don't (be the same / follow)."},
        "N1_783": {"example_sentence": "（（会）かい）わ（わ）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "かいわをたのしみましょう。", "example_meaning_cn": "享受会话（聊天）吧。", "example_meaning_en": "Let's enjoy a conversation."},
        "N1_784": {"example_sentence": "（（改）かい）わ（わ）を（を）し（し）て（て）ください。", "example_reading": "かいわをしてください。", "example_meaning_cn": "请进行修改（或对话）。", "example_meaning_en": "Please revise / speak."},
        "N1_785": {"example_sentence": "（（海）かい）わ（わ）ん（ん）を（を）見（み）ま（ま）しょ（しょ）う（う）。", "example_reading": "かいわんをみましょう。", "example_meaning_cn": "看海湾吧。", "example_meaning_en": "Let's see the bay."},
        "N1_786": {"example_sentence": "（（飼）か）い（い）を（を）し（し）て（て）ください。", "example_reading": "かいをしてください。", "example_meaning_cn": "请进行饲养（或购买）。", "example_meaning_en": "Please keep / buy it."},
        "N1_787": {"example_sentence": "（（皆）かい）を（を）尽くし（つくし）て（て）ください。", "example_reading": "かいをつくしてください。", "example_meaning_cn": "请极尽所能。", "example_meaning_en": "Please do your utmost."},
        "N1_788": {"example_sentence": "（（壊）かい）を（を）防ぎ（ふせぎ）ましょう。", "example_reading": "かいをふせぎましょう。", "example_meaning_cn": "预防破坏（或溃散）吧。", "example_meaning_en": "Let's prevent the collapse / destruction."},
        "N1_789": {"example_sentence": "（（馨）かお）り（り）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "かおりをたのしみましょう。", "example_meaning_cn": "享受香气吧。", "example_meaning_en": "Let's enjoy the fragrance."},
        "N1_790": {"example_sentence": "（（顔）かお）つ（つ）き（き）が（が）いい（いい）ですね。", "example_reading": "かおつきがいいですね。", "example_meaning_cn": "神情（长相）不错呢。", "example_meaning_en": "They have a good expression / features."},
        "N1_791": {"example_sentence": "（（抱）かか）え（え）込ん（こん）で（て）ください。", "example_reading": "かかえこんでください。", "example_meaning_cn": "请承担起来（或抱在怀里）。", "example_meaning_en": "Please take it on / hold it in your arms."},
        "N1_792": {"example_sentence": "（（掲）かか）げ（げ）て（て）ください。", "example_reading": "かかげてください。", "example_meaning_cn": "请高举（或刊登）。", "example_meaning_en": "Please hold high / publish it."},
        "N1_793": {"example_sentence": "（（踵）かかと）を（を）鳴らし（ならし）て（て）歩き（あるき）ましょう。", "example_reading": "かかとをならしてあるきましょう。", "example_meaning_cn": "蹬着后跟走吧。", "example_meaning_en": "Let's walk by clicking our heels."},
        "N1_794": {"example_sentence": "（（係）かか）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "かかわらないでください。", "example_meaning_cn": "请不要牵连（或不管）。", "example_meaning_en": "Please don't get involved."},
        "N1_795": {"example_sentence": "（（係）かか）わ（わ）っ（っ）て（て）ください。", "example_reading": "かかわってください。", "example_meaning_cn": "请参与进去（牵涉）。", "example_meaning_en": "Please be involved / concerned."},
        "N1_796": {"example_sentence": "（（利）き）き（き）を（を）感じ（かんじ）ます。", "example_reading": "ききをかんじます。", "example_meaning_cn": "感到利息（或奏效）。", "example_meaning_en": "I feel the effect / interest."},
        "N1_797": {"example_sentence": "（（限）かぎ）り（り）な（な）い（い）愛（あい）を（を）捧げ（ささげ）ます。", "example_reading": "かぎりないあいをささげます。", "example_meaning_cn": "奉献无限的爱。", "example_meaning_en": "I offer boundless love."},
        "N1_798": {"example_sentence": "（（限）かぎ）る（る）のを（を）やめ（やめ）ましょう。", "example_reading": "かぎるのをやめましょう。", "example_meaning_cn": "别再局限（或最好）了吧。", "example_meaning_en": "Let's stop limiting ourselves."},
        "N1_799": {"example_sentence": "（（描）か）き（き）お（お）し（し）ないで（为）ください。", "example_reading": "かきおしないでください。", "example_meaning_cn": "请不要（画错或改正）。", "example_meaning_en": "Please don't (misdraw / correct)."},
        "N1_800": {"example_sentence": "（（描）か）き（き）き（き）る（る）のを（を）手伝っ（てつだっ）て（て）ください。", "example_reading": "かききるのをてつだってください。", "example_meaning_cn": "请帮我画完（或写完）。", "example_meaning_en": "Please help me finish drawing / writing."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_800.")

if __name__ == "__main__":
    main()
