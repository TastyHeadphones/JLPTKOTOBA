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
        "N1_801": {"example_sentence": "（（描）か）き（き）け（け）さ（さ）ないで（为）ください。", "example_reading": "かきけさないでください。", "example_meaning_cn": "请不要涂改（或抹去）。", "example_meaning_en": "Please don't erase / cross it out."},
        "N1_802": {"example_sentence": "（（描）か）き（き）こ（こ）ま（ま）ないで（为）ください。", "example_reading": "かきこまないでください。", "example_meaning_cn": "请不要（写进去或细节描写）。", "example_meaning_en": "Please don't (write in / describe in detail)."},
        "N1_803": {"example_sentence": "（（描）か）き（き）だ（だ）し（し）て（て）ください。", "example_reading": "かきだしてください。", "example_meaning_cn": "请勾勒出来（或开始写）。", "example_meaning_en": "Please sketch it out / start writing."},
        "N1_804": {"example_sentence": "（（描）か）き（き）な（な）ぐ（ぐ）ら（ら）ないで（为）ください。", "example_reading": "かきなぐらないでください。", "example_meaning_cn": "请不要潦草书写（涂鸦）。", "example_meaning_en": "Please don't scribble / scrawl."},
        "N1_805": {"example_sentence": "（（描）か）き（き）の（の）こ（こ）さ（さ）ないで（为）ください。", "example_reading": "かきのこさないでください。", "example_meaning_cn": "请不要漏画（或留下笔迹）。", "example_meaning_en": "Please don't omit any part / leave a note."},
        "N1_806": {"example_sentence": "（（描）か）き（き）わ（わ）け（け）て（て）ください。", "example_reading": "かきわけてください。", "example_meaning_cn": "请（分别描绘）区分开画。", "example_meaning_en": "Please draw them distinctly / separately."},
        "N1_807": {"example_sentence": "（（描）か）き（き）そ（そ）え（え）て（て）ください。", "example_reading": "かきそえてください。", "example_meaning_cn": "请（在画中或文中）补写。", "example_meaning_en": "Please add a postscript / additional drawing."},
        "N1_808": {"example_sentence": "（（描）か）き（き）た（た）て（て）て（て）ください。", "example_reading": "かきたててください。", "example_meaning_cn": "请煽动（或唤起）。", "example_meaning_en": "Please stir up / arouse / incite."},
        "N1_809": {"example_sentence": "（（描）か）き（き）ち（ち）ら（ら）さ（さ）ないで（为）ください。", "example_reading": "かきちらさないでください。", "example_meaning_cn": "请不要乱写（胡乱涂抹）。", "example_meaning_en": "Please don't scribble around / waste paper."},
        "N1_810": {"example_sentence": "（（描）か）き（き）つ（つ）ら（ら）ね（ね）て（て）ください。", "example_reading": "かきつらねてください。", "example_meaning_cn": "请（一一列举）写下来。", "example_meaning_en": "Please list them in writing / enumerate."},
        "N1_811": {"example_sentence": "（（描）か）き（き）と（と）め（め）て（て）ください。", "example_reading": "かきとめてください。", "example_meaning_cn": "请记录（摘录）下来。", "example_meaning_en": "Please jot it down / take a note."},
        "N1_812": {"example_sentence": "（（描）か）き（き）なお（なお）し（し）て（て）ください。", "example_reading": "かきなおしてください。", "example_meaning_cn": "请重画（重写）。", "example_meaning_en": "Please redraw / rewrite it."},
        "N1_813": {"example_sentence": "（（描）か）き（き）な（な）が（が）さ（さ）ないで（为）ください。", "example_reading": "かきながさないでください。", "example_meaning_cn": "请不要（流走或随手画）。", "example_meaning_en": "Please don't (wash away / dash off a drawing)."},
        "N1_814": {"example_sentence": "（（描）か）き（き）な（な）ら（ら）さ（さ）ないで（为）ください。", "example_reading": "かきならさないでください。", "example_meaning_cn": "请不要（弄平或书写）。", "example_meaning_en": "Please don't (level / write)."},
        "N1_815": {"example_sentence": "（（描）か）き（き）ぬ（ぬ）き（き）を（を）し（し）て（て）ください。", "example_reading": "かきぬきをしてください。", "example_meaning_cn": "请摘录（精选文字）。", "example_meaning_en": "Please extract / select from writing."},
        "N1_816": {"example_sentence": "（（描）か）き（き）ね（ね）に（に）し（し）ないで（为）ください。", "example_reading": "かきねにしないでください。", "example_meaning_cn": "请不要作为篱笆（墙）。", "example_meaning_en": "Please don't use it as a fence / boundary."},
        "N1_817": {"example_sentence": "（（描）か）き（き）も（も）ら（ら）さ（さ）ないで（为）ください。", "example_reading": "かきもらさないでください。", "example_meaning_cn": "请不要漏写。", "example_meaning_en": "Please don't omit anything while writing."},
        "N1_818": {"example_sentence": "（（描）か）き（き）よ（よ）せ（せ）て（て）ください。", "example_reading": "かきよせてください。", "example_meaning_cn": "请搜集（并写下来）。", "example_meaning_en": "Please collect (and write down)."},
        "N1_819": {"example_sentence": "（（核）かく）を（を）持ち（もち）ましょ（しょ）う（う）。", "example_reading": "かくをもちましょう。", "example_meaning_cn": "拥有核心（或核能）吧。", "example_meaning_en": "Let's have a core / nuclear power."},
        "N1_820": {"example_sentence": "（（覚）かく）ご（ご）を（を）決め（きめ）て（て）ください。", "example_reading": "かくごをきめてください。", "example_meaning_cn": "请做好心理准备（下决心）。", "example_meaning_en": "Please make up your mind / be prepared."},
        "N1_821": {"example_sentence": "（（学）がく）さ（さ）を（を）感じ（かんじ）ます。", "example_reading": "がくをかんじます。", "example_meaning_cn": "感到（学问或才华）的差距。", "example_meaning_en": "I feel the gap in scholarship / talent."},
        "N1_822": {"example_sentence": "（（学）がく）し（し）を（を）深め（ふかめ）ましょう。", "example_reading": "がくをしをふかめましょう。", "example_meaning_cn": "深化学识吧。", "example_meaning_en": "Let's deepen our knowledge / learning."},
        "N1_823": {"example_sentence": "（（格）かく）さ（さ）を（を）是正（ぜせい）し（し）ましょう。", "example_reading": "かくさをぜせいしましょう。", "example_meaning_cn": "矫正差距吧。", "example_meaning_en": "Let's correct the disparity / gap."},
        "N1_824": {"example_sentence": "（（確）かく）し（し）ん（ん）し（し）て（て）ください。", "example_reading": "かくしんしてください。", "example_meaning_cn": "请确信（深信不疑）。", "example_meaning_en": "Please be certain / convinced."},
        "N1_825": {"example_sentence": "（（革）かく）し（し）ん（ん）を（を）進め（すすめ）て（て）ください。", "example_reading": "かくしんをすすめてください。", "example_meaning_cn": "请推进革新。", "example_meaning_en": "Please proceed with the innovation / reform."},
        "N1_826": {"example_sentence": "（（確）かく）し（し）ん（ん）を（を）突い（つい）て（て）ください。", "example_reading": "かくしんをついてください。", "example_meaning_cn": "请击中核心（要害）。", "example_meaning_en": "Please hit the core / the point."},
        "N1_827": {"example_sentence": "（（確）かく）し（し）ょ（ょ）う（う）が（が）あり（あり）ますか。", "example_reading": "かくしょうがありますか。", "example_meaning_cn": "有确凿的证据吗？", "example_meaning_en": "Do you have positive proof?"},
        "N1_828": {"example_sentence": "（（隔）かく）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "かくぜんとしています。", "example_meaning_cn": "隔绝（相差很远）着。", "example_meaning_en": "There's a marked difference / separation."},
        "N1_829": {"example_sentence": "（（額）がく）を（を）飾っ（かざっ）て（て）ください。", "example_reading": "がくをかざってください。", "example_meaning_cn": "请在额头（或相框）上装饰。", "example_meaning_en": "Please decorate the forehead / frame."},
        "N1_830": {"example_sentence": "（（確）かく）だ（だ）ん（ん）を（を）避け（さけ）て（て）ください。", "example_reading": "かくだんをさけてください。", "example_meaning_cn": "请避免做出断定（确诊）。", "example_meaning_en": "Please avoid making a definitive conclusion."},
        "N1_831": {"example_sentence": "（（格）かく）だ（だ）ん（ん）の（の）差（さ）があり（あり）ます。", "example_reading": "かくだんのさがあります。", "example_meaning_cn": "有明显的差距。", "example_meaning_en": "There is a significant / marked difference."},
        "N1_832": {"example_sentence": "（（格）かく）ち（ち）を（を）保っ（たもっ）て（て）ください。", "example_reading": "かくちをたもってください。", "example_meaning_cn": "请保持格调（或各地）。", "example_meaning_en": "Please maintain the style / status."},
        "N1_833": {"example_sentence": "（（確）かく）ち（ち）を（を）得（え）て（て）ください。", "example_reading": "かくちをえてください。", "example_meaning_cn": "请获得确知（确信）。", "example_meaning_en": "Please gain certain knowledge / conviction."},
        "N1_834": {"example_sentence": "（（拡）かく）ち（ち）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "かくちょうしてください。", "example_meaning_cn": "请扩张（扩充）。", "example_meaning_en": "Please expand / extend it."},
        "N1_835": {"example_sentence": "（（角）かく）ど（ど）を（を）変え（かえ）て（て）見（み）ま（ま）しょ（しょ）う（う）。", "example_reading": "かくどをかえてみましょう。", "example_meaning_cn": "换个角度看吧。", "example_meaning_en": "Let's look at it from a different angle."},
        "N1_836": {"example_sentence": "（（確）かく）に（に）し（し）て（て）ください。", "example_reading": "かくにしてください。", "example_meaning_cn": "请定为确定（或正确）。", "example_meaning_en": "Please make it certain / correct."},
        "N1_837": {"example_sentence": "（（確）かく）に（に）ん（ん）し（し）て（て）ください。", "example_reading": "かくにんしてください。", "example_meaning_cn": "请确认。", "example_meaning_en": "Please confirm it."},
        "N1_838": {"example_sentence": "（（学）がく）ね（ね）ん（ん）を（を）終え（おえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "がくねんをおえましょう。", "example_meaning_cn": "结束学年吧。", "example_meaning_en": "Let's finish the school year."},
        "N1_839": {"example_sentence": "（（確）かく）は（は）あり（あり）ません。", "example_reading": "かくわありません。", "example_meaning_cn": "没有确定（或核）。", "example_meaning_en": "There is no certainty / core."},
        "N1_840": {"example_sentence": "（（確）かく）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "かくばなしをしないでください。", "example_meaning_cn": "请不要（确切说或谈话）。", "example_meaning_en": "Please don't (speak certainly / talk)."},
        "N1_841": {"example_sentence": "（（確）かく）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "かくふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_842": {"example_sentence": "（（確）かく）ぽ（ぽ）し（し）てください。", "example_reading": "かくぽしてください。", "example_meaning_cn": "请确信（或保证）。", "example_meaning_en": "Please be sure / guarantee it."},
        "N1_843": {"example_sentence": "（（学）がく）も（も）ん（ん）を（を）志し（こころざし）ましょう。", "example_reading": "がくもんをこころざしましょう。", "example_meaning_cn": "志向学问吧。", "example_meaning_en": "Let's strive for scholarship / learning."},
        "N1_844": {"example_sentence": "（（格）かく）や（や）す（す）な（な）料金（りょうきん）です。", "example_reading": "かくやすなりょうきんです。", "example_meaning_cn": "特别便宜的费用。", "example_meaning_en": "It's an exceptionally cheap rate."},
        "N1_845": {"example_sentence": "（（確）かく）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "かくらんしないでください。", "example_meaning_cn": "请不要（混乱或骚扰）。", "example_meaning_en": "Please don't (disturb / confuse)."},
        "N1_846": {"example_sentence": "（（確）かく）り（り）し（し）て（て）ください。", "example_reading": "かくりしてください。", "example_meaning_cn": "请定为确立（或隔离）。", "example_meaning_en": "Please establish / isolate it."},
        "N1_847": {"example_sentence": "（（学）がく）り（り）ょ（ょ）く（く）を（を）伸ばし（のばし）ま（ま）しょ（しょ）う（う）。", "example_reading": "がくりょくをのばしましょう。", "example_meaning_cn": "提高学力（成绩）吧。", "example_meaning_en": "Let's improve our academic ability."},
        "N1_848": {"example_sentence": "（（格）かく）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "かくれいしないでください。", "example_meaning_cn": "请不要（客气或同样）。", "example_meaning_en": "Please don't (be polite / fall in line)."},
        "N1_849": {"example_sentence": "（（格）かく）ろ（ろ）し（し）ないで（为）ください。", "example_reading": "かくろしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_850": {"example_sentence": "（（確）かく）わ（わ）し（し）ないで（和）ください。", "example_reading": "かくわしないでください。", "example_meaning_cn": "请不要（和谈或确定）。", "example_meaning_en": "Please don't (be at peace / be certain)."},
        "N1_851": {"example_sentence": "（（陰）かげ）に（に）隠れ（かくれ）て（て）ください。", "example_reading": "かげにかくれたりてください。", "example_meaning_cn": "请躲在影子（阴影）里。", "example_meaning_en": "Please hide in the shadow / shade."},
        "N1_852": {"example_sentence": "（（駆）か）け（け）あ（あ）お（お）ず（ず）し（し）ないで（为）ください。", "example_reading": "かけあおずしないでください。", "example_meaning_cn": "请不要（催促或纠缠）。", "example_meaning_en": "Please don't (urge / pester)."},
        "N1_853": {"example_sentence": "（（駆）か）け（け）あ（あ）し（し）で（で）行き（いき）ましょう。", "example_reading": "かけあしでいきましょう。", "example_meaning_cn": "跑步去吧。", "example_meaning_en": "Let's go at a double-quick pace / run."},
        "N1_854": {"example_sentence": "（（懸）か）け（け）が（が）え（え）の（の）ない（ない）存在（そんざい）です。", "example_reading": "かけがえのないそんざいです。", "example_meaning_cn": "是不可替代的存在。", "example_meaning_en": "You are an irreplaceable presence."},
        "N1_855": {"example_sentence": "（（賭）か）け（け）ご（ご）と（と）は（は）避け（さけ）ましょう。", "example_reading": "かけごとわさけましょう。", "example_meaning_cn": "戒赌（避开赌博）吧。", "example_meaning_en": "Let's avoid gambling."},
        "N1_856": {"example_sentence": "（（駆）か）け（け）な（な）い（い）で（为）ください。", "example_reading": "かけないでください。", "example_meaning_cn": "请不要跑（或挂着）。", "example_meaning_en": "Please don't run / don't hang it."},
        "N1_857": {"example_sentence": "（（駆）か）け（け）は（は）し（し）に（に）なり（なり）たい（たい）です。", "example_reading": "かけはしになりたいです。", "example_meaning_cn": "想成为（沟通的）桥梁。", "example_meaning_en": "I want to be a bridge / mediator."},
        "N1_858": {"example_sentence": "（（欠）か）け（け）ら（ら）を（を）拾い（ひろい）ましょう。", "example_reading": "かけらをひろいましょう。", "example_meaning_cn": "捡起碎片吧。", "example_meaning_en": "Let's pick up the fragments / splinters."},
        "N1_859": {"example_sentence": "（（駆）か）け（け）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "かけわらないでください。", "example_meaning_cn": "请不要（乱跑或分开）。", "example_meaning_en": "Please don't (run around / divide)."},
        "N1_860": {"example_sentence": "（（刺）か）ご（ご）に（に）入れ（いれ）て（て）ください。", "example_reading": "かごにいれてください。", "example_meaning_cn": "请放入篮子里。", "example_meaning_en": "Please put it in the basket."},
        "N1_861": {"example_sentence": "（（過）か）ご（ご）を（を）犯さ（おかさ）ないで（为）ください。", "example_reading": "かごをおかさないでください。", "example_meaning_cn": "请不要犯过失（错误）。", "example_meaning_en": "Please don't commit an error / fault."},
        "N1_862": {"example_sentence": "（（火）か）こ（こ）う（う）し（し）て（て）ください。", "example_reading": "かこうしてください。", "example_meaning_cn": "请进行加工（或包围）。", "example_meaning_en": "Please process / surround it."},
        "N1_863": {"example_sentence": "（（箇）か）こ（こ）く（く）な（な）状況（じょうきょう）です。", "example_reading": "かこくなじょうきょうです。", "example_meaning_cn": "严酷（苛酷）的情况。", "example_meaning_en": "It's a harsh / severe situation."},
        "N1_864": {"example_sentence": "（（貸）か）さ（さ）ないで（为）ください。", "example_reading": "かさないでください。", "example_meaning_cn": "请不要借出（或重叠）。", "example_meaning_en": "Please don't lend it / don't overlap it."},
        "N1_865": {"example_sentence": "（（重）かさ）な（な）ら（ら）ないで（为）ください。", "example_reading": "かさならないでください。", "example_meaning_cn": "请不要重叠。", "example_meaning_en": "Please don't overlap / pile up."},
        "N1_866": {"example_sentence": "（（笠）かさ）を（を）さし（さし）て（て）ください。", "example_reading": "かさをさしてください。", "example_meaning_cn": "请撑伞（或戴笠）。", "example_meaning_en": "Please put on the bamboo hat / hold the umbrella."},
        "N1_867": {"example_sentence": "（（傘）かさ）を（を）貸し（かし）て（て）ください。", "example_reading": "かさをかしてください。", "example_meaning_cn": "请借给我雨伞。", "example_meaning_en": "Please lend me your umbrella."},
        "N1_868": {"example_sentence": "（（風）かぜ）を（を）防ぎ（ふせぎ）ましょう。", "example_reading": "かぜをふせぎましょう。", "example_meaning_cn": "御寒（防风）吧。", "example_meaning_en": "Let's block the wind / keep out the cold."},
        "N1_869": {"example_sentence": "（（火）か）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "かぜんとしています。", "example_meaning_cn": "果断（果然）着。", "example_meaning_en": "It's resolute / decisive."},
        "N1_870": {"example_sentence": "（（火）か）ぜ（ぜ）ん（ん）し（し）て（て）ください。", "example_reading": "かぜんしてください。", "example_meaning_cn": "请使其变红（或火红）。", "example_meaning_en": "Please turn it red / glow like fire."},
        "N1_871": {"example_sentence": "（（火）か）そ（そ）に（に）なら（なら）ないで（为）ください。", "example_reading": "かそにならないでください。", "example_meaning_cn": "请不要变得稀少（或过疏）。", "example_meaning_en": "Please don't become depopulated."},
        "N1_872": {"example_sentence": "（（火）か）そ（そ）う（う）し（し）て（て）ください。", "example_reading": "かそうしてください。", "example_meaning_cn": "请进行火葬（或假装）。", "example_meaning_en": "Please perform cremation / pretend it."},
        "N1_873": {"example_sentence": "（（火）か）そ（そ）く（く）し（し）て（て）ください。", "example_reading": "かそくしてください。", "example_meaning_cn": "请加速。", "example_meaning_en": "Please accelerate."},
        "N1_874": {"example_sentence": "（（肩）かた）を（を）貸し（かし）て（て）ください。", "example_reading": "かたをかしてください。", "example_meaning_cn": "请借肩膀给我（扶一下）。", "example_meaning_en": "Please lend me your shoulder."},
        "N1_875": {"example_sentence": "（（方）かた）を（を）選ん（えらん）で（て）ください。", "example_reading": "かたをえらんでください。", "example_meaning_cn": "请选择方法（或某位人士）。", "example_meaning_en": "Please choose the way / person."},
        "N1_876": {"example_sentence": "（（型）かた）に（に）はめ（はめ）ないで（为）ください。", "example_reading": "かたにはめないでください。", "example_meaning_cn": "请不要墨守成规（套模子）。", "example_meaning_en": "Please don't pigeonhole / mold it."},
        "N1_877": {"example_sentence": "（（形）かた）を（を）整え（ととなえ）て（て）ください。", "example_reading": "かたをととなえてください。", "example_meaning_cn": "请整理形状。", "example_meaning_en": "Please adjust the shape."},
        "N1_878": {"example_sentence": "（（難）かた）い（い）事（こと）を（を）言わ（いわ）ないで（为）ください。", "example_reading": "かたいことをいわないでください。", "example_meaning_cn": "请不要说为难（或死板）的话。", "example_meaning_en": "Please don't be so stiff / difficult."},
        "N1_879": {"example_sentence": "（（片）かた）い（い）を（を）し（し）ないで（为）ください。", "example_reading": "かたいをしないでください。", "example_meaning_cn": "请不要单一方面（或片理）。", "example_meaning_en": "Please don't be one-sided."},
        "N1_880": {"example_sentence": "（（片）かた）い（い）を（を）合わせ（あわせ）て（て）ください。", "example_reading": "かたいをあわせてください。", "example_meaning_cn": "请配合（或对准）一方面。", "example_meaning_en": "Please match up / fit together."},
        "N1_881": {"example_sentence": "（（固）かた）え（え）に（に）なら（なら）ないで（为）ください。", "example_reading": "かたえにならないでください。", "example_meaning_cn": "请不要变得顽固（或在座）。", "example_meaning_en": "Please don't be stubborn / be present."},
        "N1_882": {"example_sentence": "（（片）かた）お（お）し（し）ないで（为）ください。", "example_reading": "かたおしないでください。", "example_meaning_cn": "请不要偏袒（或单推）。", "example_meaning_en": "Please don't be biased / push one side."},
        "N1_883": {"example_sentence": "（（堅）かた）ぎ（ぎ）な（な）生き方（いきかた）を（を）し（し）ましょう。", "example_reading": "かたぎないきかたをしましょう。", "example_meaning_cn": "过着正经（安分）的生活吧。", "example_meaning_en": "Let's live an honest / steady life."},
        "N1_884": {"example_sentence": "（（気）かた）ぎ（ぎ）を（を）感じ（かんじ）ます。", "example_reading": "かたぎをかんじます。", "example_meaning_cn": "感受到其禀性（或风气）。", "example_meaning_en": "I feel their spirit / character."},
        "N1_885": {"example_sentence": "（（片）かた）く（く）ち（ち）を（を）聞き（きき）たい（たい）です。", "example_reading": "かたくちをききたいです。", "example_meaning_cn": "想听单方面的话（或片语）。", "example_meaning_en": "I want to hear one side of the story."},
        "N1_886": {"example_sentence": "（（固）かた）く（く）な（な）態度（たいど）を（を）崩さ（くずさ）ないで（为）ください。", "example_reading": "かたくなたいどをくずさないでください。", "example_meaning_cn": "请不要改变顽固的态度。", "example_meaning_en": "Please don't keep that stubborn attitude."},
        "N1_887": {"example_sentence": "（（片）かた）こ（こ）と（と）を（を）し（し）ないで（为）ください。", "example_reading": "かたことしないでください。", "example_meaning_cn": "请不要说半咸不淡（不流利）的话。", "example_meaning_en": "Please don't speak in broken language."},
        "N1_888": {"example_sentence": "（（片）かた）こ（こ）な（な）事（こと）を（を）し（し）ないで（为）ください。", "example_reading": "かたこなことをしないでください。", "example_meaning_cn": "请不要做顽固（或片面）的事。", "example_meaning_en": "Please don't do anything stubborn / one-sided."},
        "N1_889": {"example_sentence": "（（片）かた）さ（さ）を（を）感じ（かんじ）ます。", "example_reading": "かたさをかんじます。", "example_meaning_cn": "感受到硬度（或死板）。", "example_meaning_en": "I feel the stiffness / hardness."},
        "N1_890": {"example_sentence": "（（片）かた）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "かたしをしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_891": {"example_sentence": "（（片）かた）し（し）ゅ（ゅ）う（う）し（し）ないで（为）ください。", "example_reading": "かたしゅうしないでください。", "example_meaning_cn": "请不要（偏心或收集）。", "example_meaning_en": "Please don't (be partial / collect)."},
        "N1_892": {"example_sentence": "（（形）かた）ど（ど）っ（っ）て（て）ください。", "example_reading": "かたどってください。", "example_meaning_cn": "请仿造（造型）。", "example_meaning_en": "Please model / shape it after something."},
        "N1_893": {"example_sentence": "（（片）かた）な（な）し（し）に（に）し（し）ないで（为）ください。", "example_reading": "かたなしにしないでください。", "example_meaning_cn": "请不要使其一败涂地（或名誉扫地）。", "example_meaning_en": "Please don't ruin it / bring disgrace."},
        "N1_894": {"example_sentence": "（（刀）かた）な（な）を（を）抜か（ぬか）ないで（为）ください。", "example_reading": "かたなをぬかないでください。", "example_meaning_cn": "请不要拔刀。", "example_meaning_en": "Please don't draw your sword."},
        "N1_895": {"example_sentence": "（（片）かた）ね（ね）に（に）し（し）ないで（为）ください。", "example_reading": "かたねにしないでください。", "example_meaning_cn": "请不要（由于偏爱或在座）。", "example_meaning_en": "Please don't (favor / be present)."},
        "N1_896": {"example_sentence": "（（片）かた）の（の）し（し）ないで（为）ください。", "example_reading": "かたのしないでください。", "example_meaning_cn": "请不要（偏移或放在肩膀上）。", "example_meaning_en": "Please don't (lean / shoulder it)."},
        "N1_897": {"example_sentence": "（（片）かた）は（は）し（し）を（を）歩き（あるき）ましょう。", "example_reading": "かたはしをあるきましょう。", "example_meaning_cn": "走在边上（一端）吧。", "example_meaning_en": "Let's walk along the edge / end."},
        "N1_898": {"example_sentence": "（（片）かた）ひ（ひ）し（し）ないで（为）ください。", "example_reading": "かたひしないでください。", "example_meaning_cn": "请不要（偏袒或比试）。", "example_meaning_en": "Please don't (favor / contest)."},
        "N1_899": {"example_sentence": "（（片）かた）ほ（ほ）う（う）を（を）捨て（すて）ないで（为）ください。", "example_reading": "かたほうをすてないでください。", "example_meaning_cn": "请不要丢掉另一半（单方面）。", "example_meaning_en": "Please don't throw away the other half."},
        "N1_900": {"example_sentence": "（（片）かた）ま（ま）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "かたまわらないでください。", "example_meaning_cn": "请不要（绕到一侧或改变）。", "example_meaning_en": "Please don't (go to one side / change)."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_900.")

if __name__ == "__main__":
    main()
