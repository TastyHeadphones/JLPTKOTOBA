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
        "N1_1001": {"example_sentence": "（（見）み）え（え）を（を）張ら（はら）ないで（为）ください。", "example_reading": "みえわはらないでください。", "example_meaning_cn": "请不要虚张声势（爱面子）。", "example_meaning_en": "Please don't show off / be vain."},
        "N1_1002": {"example_sentence": "（（見）み）え（え）す（す）き（き）た（た）嘘（うそ）を（を）つか（つか）ないで（为）ください。", "example_reading": "みえすいたうそわつかないでください。", "example_meaning_cn": "不要撒一眼就能看穿的谎。", "example_meaning_en": "Don't tell such obvious lies."},
        "N1_1003": {"example_sentence": "（（見）み）か（か）え（え）し（し）を（を）求め（もとめ）ないで（为）ください。", "example_reading": "みかえしわもとめないでください。", "example_meaning_cn": "请不要（为了报复或回报）而做。", "example_meaning_en": "Please don't look for a return / revenge."},
        "N1_1004": {"example_sentence": "（（見）み）か（か）え（え）し（し）を（を）期待（きたい）し（し）ない（ない）で（为）ください。", "example_reading": "みかえしわきたいしないでください。", "example_meaning_cn": "请不要期待回报（或回扣）。", "example_meaning_en": "Please don't expect a reward / return."},
        "N1_1005": {"example_sentence": "（（見）み）え（え）を（を）張る（はる）のは（は）やめ（やめ）ましょう。", "example_reading": "みえわはるのわやめましょう。", "example_meaning_cn": "别再虚张声势（爱面子）了吧。", "example_meaning_en": "Let's stop putting on airs."},
        "N1_1006": {"example_sentence": "（（見）み）か（か）け（け）に（に）よら（よら）ない（ない）人（ひと）です。", "example_reading": "みかけによらないひとです。", "example_meaning_cn": "是个不可貌相的人。", "example_meaning_en": "He is not what he seems to be."},
        "N1_1007": {"example_sentence": "（（見）み）か（か）た（た）を（を）変え（かえ）て（て）見（み）ま（ま）しょ（しょ）う（う）。", "example_reading": "みかたをかえてみましょう。", "example_meaning_cn": "换个看法（角度）看吧。", "example_meaning_en": "Let's look at it from a different perspective."},
        "N1_1008": {"example_sentence": "（（味）み）か（か）た（た）に（に）なっ（なっ）て（て）ください。", "example_reading": "みかたになってください。", "example_meaning_cn": "请成为我这一边（支持者）。", "example_meaning_en": "Please take my side / be my ally."},
        "N1_1009": {"example_sentence": "（（見）み）か（か）な（な）い（以）で（为）ください。", "example_reading": "みかないでください。", "example_meaning_cn": "请不要（看漏或放过）。", "example_meaning_en": "Please don't (omit seeing / let it pass)."},
        "N1_1010": {"example_sentence": "（（見）み）か（か）ら（ら）ないで（为）ください。", "example_reading": "みからないでください。", "example_meaning_cn": "请不到（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1011": {"example_sentence": "（（見）み）き（き）わ（わ）め（め）て（て）ください。", "example_reading": "みきわめてください。", "example_meaning_cn": "请看准（看清）。", "example_meaning_en": "Please see through / discern it."},
        "N1_1012": {"example_sentence": "（（見）み）き（き）わ（わ）め（め）に（に）し（し）ないで（为）ください。", "example_reading": "みきわめにしないでください。", "example_meaning_cn": "请不要作为看清（或放弃）。", "example_meaning_en": "Please don't make it a judgment / abandonment."},
        "N1_1013": {"example_sentence": "（（見）み）き（き）り（り）し（し）ないで（为）ください。", "example_reading": "みきりしないでください。", "example_meaning_cn": "请不要（看清或放弃）。", "example_meaning_en": "Please don't (see through / give up on)."},
        "N1_1014": {"example_sentence": "（（見）み）き（き）り（り）は（は）っ（っ）し（し）ん（ん）し（し）ないで（为）ください。", "example_reading": "みきりはっしんしないでください。", "example_meaning_cn": "请不要仓促行事（未看清就出发）。", "example_meaning_en": "Please don't act before checking / start prematurely."},
        "N1_1015": {"example_sentence": "（（見）み）く（く）び（び）ら（ら）ないで（为）ください。", "example_reading": "みくびらないでください。", "example_meaning_cn": "请不要小看（轻视）。", "example_meaning_en": "Please don't underestimate / slight."},
        "N1_1016": {"example_sentence": "（（三）み）こ（こ）し（し）の（の）事（こと）を（を）考え（かんがえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "みこしのことをかんがえましょう。", "example_meaning_cn": "预想一下未来的事吧。", "example_meaning_en": "Let's think about the future / anticipation."},
        "N1_1017": {"example_sentence": "（（見）み）さ（さ）かい（い）を（を）付け（つけ）て（て）ください。", "example_reading": "みさかいをいれてください。", "example_meaning_cn": "请分清是非（有分寸）。", "example_meaning_en": "Please distinguish / have a sense of proportion."},
        "N1_1018": {"example_sentence": "（（見）み）さ（さ）だ（だ）め（め）て（て）ください。", "example_reading": "みさだめてください。", "example_meaning_cn": "请看清（确定）。", "example_meaning_en": "Please ascertain / see for sure."},
        "N1_1019": {"example_sentence": "（（見）み）し（し）ら（ら）ぬ（ぬ）道（みち）を（を）歩き（あるき）ま（ま）しょ（しょ）う（う）。", "example_reading": "みしらぬみちをあるきましょう。", "example_meaning_cn": "走在陌生的路上吧。", "example_meaning_en": "Let's walk on an unknown path."},
        "N1_1020": {"example_sentence": "（（見）み）し（し）ら（ら）ぬ（ぬ）人（ひと）に（に）は（は）注意（ちゅうい）し（し）て（て）ください。", "example_reading": "みしらぬひとにわちゅういしてください。", "example_meaning_cn": "请注意陌生人。", "example_meaning_en": "Please be careful of strangers."},
        "N1_1021": {"example_sentence": "（（見）み）す（す）え（え）て（て）ください。", "example_reading": "みすえてください。", "example_meaning_cn": "请看准（定睛注视）。", "example_meaning_en": "Please fix your eyes on / stare at it."},
        "N1_1022": {"example_sentence": "（（見）み）す（す）か（か）さ（さ）ないで（为）ください。", "example_reading": "みすかさないでください。", "example_meaning_cn": "请不要看穿（洞察）。", "example_meaning_en": "Please don't see through / look into."},
        "N1_1023": {"example_sentence": "（（見）み）す（す）ご（ご）さ（さ）ないで（为）ください。", "example_reading": "みすごさないでください。", "example_meaning_cn": "请不要看漏（错过）。", "example_meaning_en": "Please don't overlook / let it pass."},
        "N1_1024": {"example_sentence": "（（見）み）す（す）ぼ（ぼ）ら（ら）し（し）い（い）恰好（かっこう）を（を）し（し）ないで（为）ください。", "example_reading": "みすぼらしいかっこうわしないでください。", "example_meaning_cn": "请不要打扮得寒酸（破旧）。", "example_meaning_en": "Please don't look shabby / miserable."},
        "N1_1025": {"example_sentence": "（（見）み）せ（せ）か（か）け（け）の（の）姿（すがた）を（を）信じ（しんじ）ないで（为）ください。", "example_reading": "みせかけのすがたわしんじないでください。", "example_meaning_cn": "不要相信虚假（做样子）的外表。", "example_meaning_en": "Don't believe the outward / deceptive appearance."},
        "N1_1026": {"example_sentence": "（（店）みせ）さ（さ）き（き）を（を）飾っ（かざっ）て（て）ください。", "example_reading": "みせさきをかざってください。", "example_meaning_cn": "请装饰店面。", "example_meaning_en": "Please decorate the storefront."},
        "N1_1027": {"example_sentence": "（（見）み）せ（せ）び（び）ら（ら）か（か）さ（さ）ないで（为）ください。", "example_reading": "みせびらかさないでください。", "example_meaning_cn": "请不要炫耀。", "example_meaning_en": "Please don't show off / flaunt."},
        "N1_1028": {"example_sentence": "（（見）み）せ（せ）もの（性）を（を）高め（たかめ）ましょう。", "example_reading": "みせものせいをたかめましょう。", "example_meaning_cn": "提高观赏性吧。", "example_meaning_en": "Let's increase its value as a show / attraction."},
        "N1_1029": {"example_sentence": "（（見）み）た（た）し（し）て（て）ください。", "example_reading": "みたしてください。", "example_meaning_cn": "请满足（填满）。", "example_meaning_en": "Please satisfy / fill it up."},
        "N1_1030": {"example_sentence": "（（見）み）た（た）て（て）を（を）受け（うけ）て（て）ください。", "example_reading": "みたてをうけてください。", "example_meaning_cn": "请接受诊断（或挑选）。", "example_meaning_en": "Please get a diagnosis / selecion."},
        "N1_1031": {"example_sentence": "（（見）み）だ（だ）し（し）な（な）み（み）を（を）整え（ととなえ）て（て）ください。", "example_reading": "みだしなみをととなえてください。", "example_meaning_cn": "请整理仪表。", "example_meaning_en": "Please groom yourself / tidy your appearance."},
        "N1_1032": {"example_sentence": "（（乱）みだ）ら（ら）な（な）行い（おこない）は（は）し（し）ないで（为）ください。", "example_reading": "みだらなおこないわしないでください。", "example_meaning_cn": "请不要做淫乱（或行为不轨）的事。", "example_meaning_en": "Please don't behave lewdly / indecently."},
        "N1_1033": {"example_sentence": "（（乱）みだ）れ（れ）を（を）直し（なおし）て（て）ください。", "example_reading": "みだれをなおしてください。", "example_meaning_cn": "请整理乱处（纠正秩序）。", "example_meaning_en": "Please fix the disorder / untidiness."},
        "N1_1034": {"example_sentence": "（（道）みち）し（し）る（る）べ（べ）に（に）なり（なり）たい（たい）です。", "example_reading": "みちしるべになりたいです。", "example_meaning_cn": "想成为（引导他人的）指路标。", "example_meaning_en": "I want to be a guidepost / milestone."},
        "N1_1035": {"example_sentence": "（（見）み）つ（つ）か（か）ら（ら）ないで（为）ください。", "example_reading": "みつからないでください。", "example_meaning_cn": "请不要被发现。", "example_meaning_en": "Please don't get caught / found."},
        "N1_1036": {"example_sentence": "（（見）み）つ（つ）め（め）て（て）ください。", "example_reading": "みつめてください。", "example_meaning_cn": "请凝视（注视）。", "example_meaning_en": "Please gaze at / observe closely."},
        "N1_1037": {"example_sentence": "（（密）みつ）に（に）し（し）ないで（为）ください。", "example_reading": "みつにしないでください。", "example_meaning_cn": "请不要使其密集（或偷偷摸摸）。", "example_meaning_en": "Please don't make it crowded / secret."},
        "N1_1038": {"example_sentence": "（（密）みつ）に（に）な（な）ら（ら）ないで（为）ください。", "example_reading": "みつにならないでください。", "example_meaning_cn": "请避开密集（空间）。", "example_meaning_en": "Please avoid crowded places (the '3 Cs')."},
        "N1_1039": {"example_sentence": "（（密）みつ）ど（ど）を（を）高め（たかめ）ま（ま）しょ（しょ）う（う）。", "example_reading": "みつどをたかめましょう。", "example_meaning_cn": "提高密度吧。", "example_meaning_en": "Let's increase the density."},
        "N1_1040": {"example_sentence": "（（見）み）と（と）め（め）て（て）ください。", "example_reading": "みとめてください。", "example_meaning_cn": "请认可（准许）。", "example_meaning_en": "Please admit / acknowledge it."},
        "N1_1041": {"example_sentence": "（（見）み）と（と）ら（ら）ないで（为）ください。", "example_reading": "みとらないでください。", "example_meaning_cn": "请不要（看风景或由于入迷）。", "example_meaning_en": "Please don't (watch / be enchanted)."},
        "N1_1042": {"example_sentence": "（（見）み）と（と）れ（れ）て（て）ください。", "example_reading": "みとれてください。", "example_meaning_cn": "请入迷（看得出神）。", "example_meaning_en": "Please be entranced / captivated."},
        "N1_1043": {"example_sentence": "（（見）み）な（な）ら（ら）わ（わ）ないで（为）ください。", "example_reading": "みならわないでください。", "example_meaning_cn": "请不要效法（或没有看到）。", "example_meaning_en": "Please don't follow that example."},
        "N1_1044": {"example_sentence": "（（見）み）な（な）ら（ら）っ（っ）て（て）ください。", "example_reading": "みならってください。", "example_meaning_cn": "请效法（见习）。", "example_meaning_en": "Please follow that example / learn from it."},
        "N1_1045": {"example_sentence": "（（見）み）ぬ（ぬ）い（以）て（て）ください。", "example_reading": "みぬいてください。", "example_meaning_cn": "请看穿（洞察）。", "example_meaning_en": "Please see through / discern it."},
        "N1_1046": {"example_sentence": "（（見）み）の（の）こ（こ）さ（さ）ないで（为）ください。", "example_reading": "みのこさないでください。", "example_meaning_cn": "请不要看漏。", "example_meaning_en": "Please don't miss anything / overlook."},
        "N1_1047": {"example_sentence": "（（見）み）の（の）が（が）さ（さ）ないで（为）ください。", "example_reading": "みのがさないでください。", "example_meaning_cn": "请不要错过（看漏）。", "example_meaning_en": "Please don't let it slip by / overlook it."},
        "N1_1048": {"example_sentence": "（（身）み）の（の）ま（ま）わ（わ）り（り）を（を）整え（ととなえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "みのまわりをととなえましょう。", "example_meaning_cn": "整理身边的事（或物）吧。", "example_meaning_en": "Let's tidy up our personal surroundings."},
        "N1_1049": {"example_sentence": "（（自）み）ず（ず）か（か）ら（ら）進ん（すすん）で（て）ください。", "example_reading": "みずからすすんでください。", "example_meaning_cn": "请主动前进。", "example_meaning_en": "Please proceed of your own accord."},
        "N1_1050": {"example_sentence": "（（見）み）す（す）ぼ（ぼ）ら（ら）し（し）い（い）恰好（かっこう）を（を）し（し）ないで（为）ください。", "example_reading": "みすぼらしいかっこうわしないでください。", "example_meaning_cn": "请不要打扮得寒酸（破旧）。", "example_meaning_en": "Please don't look shabby / miserable."},
        "N1_1051": {"example_sentence": "（（見）み）は（は）ら（ら）い（以）を（を）し（し）て（て）ください。", "example_reading": "みはらいをしてください。", "example_meaning_cn": "请进行未付（或监视）。", "example_meaning_en": "Please make the payment / observation."},
        "N1_1052": {"example_sentence": "（（見）み）は（は）ら（ら）し（し）の（の）いい（いい）場所（ばしょ）です。", "example_reading": "みはらしのいいばしょです。", "example_meaning_cn": "视野开阔的地方。", "example_meaning_en": "A place with a good view."},
        "N1_1053": {"example_sentence": "（（見）み）は（は）ら（ら）ないで（为）ください。", "example_reading": "みはらないでください。", "example_meaning_cn": "请不要监视（或没有看见）。", "example_meaning_en": "Please don't watch over / keep an eye."},
        "N1_1054": {"example_sentence": "（（見）み）は（は）り（り）を（を）し（し）て（て）ください。", "example_reading": "みはりをしてください。", "example_meaning_cn": "请放哨（监视）。", "example_meaning_en": "Please keep watch / stand guard."},
        "N1_1055": {"example_sentence": "（（見）み）ひ（ひ）ら（ら）か（か）さ（さ）ないで（为）ください。", "example_reading": "みひらかさないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1056": {"example_sentence": "（（見）み）ひ（ひ）ら（ら）か（か）し（し）に（に）し（し）ないで（为）ください。", "example_reading": "みひらかしにしないでください。", "example_meaning_cn": "请不要使其开着（或没有看见）。", "example_meaning_en": "Please don't keep it open / unobserved."},
        "N1_1057": {"example_sentence": "（（見）み）ほ（ほ）れ（れ）る（る）美（うつく）しさ（さ）です。", "example_reading": "みほれるうつくしさです。", "example_meaning_cn": "看得入神的美丽。", "example_meaning_en": "It's a beauty that you could gaze at for hours."},
        "N1_1058": {"example_sentence": "（（見）み）ま（ま）も（も）っ（っ）て（て）ください。", "example_reading": "みまもってください。", "example_meaning_cn": "请守护（照看）。", "example_meaning_en": "Please watch over / keep an eye on it."},
        "N1_1059": {"example_sentence": "（（見）み）み（み）し（し）ないで（为）ください。", "example_reading": "みみしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1060": {"example_sentence": "（（身）み）み（み）し（し）ないで（为）ください。", "example_reading": "みみしないでください。", "example_meaning_cn": "请不要（照顾身体或在身边）。", "example_meaning_en": "Please don't (be beside / take care)."},
        "N1_1061": {"example_sentence": "（（身）み）み（み）だ（だ）れ（れ）を（を）直し（なおし）ま（ま）しょ（しょ）う（う）。", "example_reading": "みみだれをなおしましょう。", "example_meaning_cn": "改正（其行为或秩序）的混乱吧。", "example_meaning_en": "Let's fix our personal disorder / behavior."},
        "N1_1062": {"example_sentence": "（（見）み）や（や）す（す）い（以）よう（よう）に（に）し（し）て（て）ください。", "example_reading": "みやすいようにしてください。", "example_meaning_cn": "请使其易于观看（或阅读）。", "example_meaning_en": "Please make it easy to see / read."},
        "N1_1063": {"example_sentence": "（（見）み）よ（よ）せ（せ）ないで（为）ください。", "example_reading": "みよせないでください。", "example_meaning_cn": "请不要（看漏或放过）。", "example_meaning_en": "Please don't (omit seeing / let it pass)."},
        "N1_1064": {"example_sentence": "（（見）み）や（や）ら（ら）ないで（为）ください。", "example_reading": "みやらないでください。", "example_meaning_cn": "请不要眺望（或没有看见）。", "example_meaning_en": "Please don't look across / observe."},
        "N1_1065": {"example_sentence": "（（見）み）わ（わ）け（け）を（を）付け（つけ）て（て）ください。", "example_reading": "みわけをいれてください。", "example_meaning_cn": "请进行分辨（识别）。", "example_meaning_en": "Please distinguish / identify it."},
        "N1_1066": {"example_sentence": "（（見）み）わ（わ）た（た）し（し）て（て）ください。", "example_reading": "みわたしてください。", "example_meaning_cn": "请远眺（或扫视一圈）。", "example_meaning_en": "Please look across / survey the scene."},
        "N1_1067": {"example_sentence": "（（民）みん）か（か）に（に）泊まり（とまり）ま（ま）しょ（しょ）う（う）。", "example_reading": "みんかにとまりましょう。", "example_meaning_cn": "住在民宅吧。", "example_meaning_en": "Let's stay at a private house."},
        "N1_1068": {"example_sentence": "（（民）みん）き（き）を（を）感じ（かんじ）ます。", "example_reading": "みんきをかんじます。", "example_meaning_cn": "感受到民俗（或民情）。", "example_meaning_en": "I feel the folk spirit / public sentiment."},
        "N1_1069": {"example_sentence": "（（民）みん）し（し）ゅ（ゅ）う（う）を（を）代表（だいひょう）し（し）て（て）ください。", "example_reading": "みんしゅうをだいひょうしてください。", "example_meaning_cn": "请代表民众（大众）。", "example_meaning_en": "Please represent the masses / public."},
        "N1_1070": {"example_sentence": "（（民）みん）せ（せ）い（い）を（を）高め（たかめ）ま（ま）しょ（しょ）う（う）。", "example_reading": "みんせいをたかめましょう。", "example_meaning_cn": "改善民生吧。", "example_meaning_en": "Let's improve the public welfare."},
        "N1_1071": {"example_sentence": "（（無）む）に（に）し（し）ないで（为）ください。", "example_reading": "むにしないでください。", "example_meaning_cn": "请不要归零（或浪费）。", "example_meaning_en": "Please don't make it nothing / waste it."},
        "N1_1072": {"example_sentence": "（（無）む）に（に）なら（なら）ないで（为）ください。", "example_reading": "むにならないでください。", "example_meaning_cn": "请不要白费。", "example_meaning_en": "Please don't let it be in vain."},
        "N1_1073": {"example_sentence": "（（無）む）の（の）境地（きょうち）に（に）なり（なり）たい（たい）です。", "example_reading": "むのきょうちになりたいです。", "example_meaning_cn": "想达到“无”的境界。", "example_meaning_en": "I want to reach the state of 'nothingness'."},
        "N1_1074": {"example_sentence": "（（無）む）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "むばなしをしないでください。", "example_meaning_cn": "请不要说空话（或悄悄话）。", "example_meaning_en": "Please don't speak nonsense / secrets."},
        "N1_1075": {"example_sentence": "（（無）む）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "むふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1076": {"example_sentence": "（（無）む）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "むらんしないでください。", "example_meaning_cn": "请不要（紊乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1077": {"example_sentence": "（（無）む）り（り）し（し）ないで（为）ください。", "example_reading": "むりしないでください。", "example_meaning_cn": "请不要勉强。", "example_meaning_en": "Please don't overdo it."},
        "N1_1078": {"example_sentence": "（（無）む）れ（れ）い（以）し（し）ないで（为）ください。", "example_reading": "むれいしないでください。", "example_meaning_cn": "请不要无理（失礼）。", "example_meaning_en": "Please don't be rude / impolite."},
        "N1_1079": {"example_sentence": "（（無）む）ろ（ろ）し（し）ないで（为）ください。", "example_reading": "むろしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1080": {"example_sentence": "（（無）む）わ（わ）し（し）ないで（为）ください。", "example_reading": "むわしないでください。", "example_meaning_cn": "请不要（和谈或无力）。", "example_meaning_en": "Please don't (be at peace / be powerless)."},
        "N1_1081": {"example_sentence": "（（命）めい）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "めいをまもりましょう。", "example_meaning_cn": "保护生命（或命令）吧。", "example_meaning_en": "Let's protect our life / follow the order."},
        "N1_1082": {"example_sentence": "（（明）めい）に（に）し（し）て（て）ください。", "example_reading": "めいにしてください。", "example_meaning_cn": "请使其明确（或明天）。", "example_meaning_en": "Please make it clear / set it for tomorrow."},
        "N1_1083": {"example_sentence": "（（名）めい）に（に）なら（なら）ないで（为）ください。", "example_reading": "めいにならないでください。", "example_meaning_cn": "请不要（有名或为了名字）。", "example_meaning_en": "Please don't (be famous / use a name)."},
        "N1_1084": {"example_sentence": "（（鳴）めい）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "めいばなしをしないでください。", "example_meaning_cn": "请不要（说谎或说话）。", "example_meaning_en": "Please don't (tell lies / speak)."},
        "N1_1085": {"example_sentence": "（（鳴）めい）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "めいふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1086": {"example_sentence": "（（鳴）めい）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "めいらんしないでください。", "example_meaning_cn": "请不要（混乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1087": {"example_sentence": "（（名）めい）り（り）ょ（ょ）う（う）に（に）し（し）て（て）ください。", "example_reading": "めいりょうにしてください。", "example_meaning_cn": "请使其明了（清晰）。", "example_meaning_en": "Please make it clear / distinct."},
        "N1_1088": {"example_sentence": "（（明）めい）れ（れ）い（い）を（を）受け（うけ）て（て）ください。", "example_reading": "めいれいをうけてください。", "example_meaning_cn": "请接受命令。", "example_meaning_en": "Please receive the command."},
        "N1_1089": {"example_sentence": "（（鳴）めい）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "めいろをとおしてください。", "example_meaning_cn": "请通过迷路（迷宫）。", "example_meaning_en": "Please find your way through the maze."},
        "N1_1090": {"example_sentence": "（（迷）めい）わ（わ）く（く）を（を）かけ（かけ）ないで（为）ください。", "example_reading": "めいわくをかけないでください。", "example_meaning_cn": "请不要给人添麻烦。", "example_meaning_en": "Please don't cause any trouble / inconvenience."},
        "N1_1091": {"example_sentence": "（（面）めん）を（を）伏せ（ふせ）て（て）ください。", "example_reading": "めんをふせてください。", "example_meaning_cn": "请面向下（或低头）。", "example_meaning_en": "Please turn your face down / bow your head."},
        "N1_1092": {"example_sentence": "（（面）めん）に（に）し（し）て（て）ください。", "example_reading": "めにしてください。", "example_meaning_cn": "请面朝（或已经看到）。", "example_meaning_en": "Please face / look at it."},
        "N1_1093": {"example_sentence": "（（綿）めん）に（に）なら（なら）ないで（为）ください。", "example_reading": "めににならないでください。", "example_meaning_cn": "请不要变得绵（软）或为了面子。", "example_meaning_en": "Please don't become soft / for appearances."},
        "N1_1094": {"example_sentence": "（（綿）めん）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "めばなしをしないでください。", "example_meaning_cn": "请不要（随口说或谈话）。", "example_meaning_en": "Please don't (speak casually / talk)."},
        "N1_1095": {"example_sentence": "（（綿）めん）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "めんふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1096": {"example_sentence": "（（綿）めん）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "めんらんしないでください。", "example_meaning_cn": "请不要（混乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_1097": {"example_sentence": "（（面）めん）り（り）し（し）ないで（为）ください。", "example_reading": "めんりしないでください。", "example_meaning_cn": "请不要（改变面貌或为了面子）。", "example_meaning_en": "Please don't (change face / for appearance)."},
        "N1_1098": {"example_sentence": "（（面）めん）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "めんれいしないでください。", "example_meaning_cn": "请不要（效法或同样）。", "example_meaning_en": "Please don't (follow suit / be the same)."},
        "N1_1099": {"example_sentence": "（（面）めん）ろ（ろ）を（を）通し（とおし）て（て）ください。", "example_reading": "めんろをとおしてください。", "example_meaning_cn": "请（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_1100": {"example_sentence": "（（面）めん）わ（わ）し（し）ないで（为）ください。", "example_reading": "めんわしないでください。", "example_meaning_cn": "请不要（和谈或对外）。", "example_meaning_en": "Please don't (be at peace / be outward)."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_1100.")

if __name__ == "__main__":
    main()
