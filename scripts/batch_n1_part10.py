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
        "N1_901": {"example_sentence": "（（片）かた）み（み）に（に）なり（なり）たい（たい）です。", "example_reading": "かたみになりたいです。", "example_meaning_cn": "想拥有（或作为）纪念品。", "example_meaning_en": "I want to have / be a memento."},
        "N1_902": {"example_sentence": "（（片）かた）み（み）に（に）思い（おもい）出（だ）し（し）て（て）ください。", "example_reading": "かたみにおもいだしてください。", "example_meaning_cn": "请偶尔（互换地或纪念性）想起我。", "example_meaning_en": "Please remember me mutually / as a memento."},
        "N1_903": {"example_sentence": "（（片）かた）め（め）に（に）し（し）ないで（为）ください。", "example_reading": "かためしないでください。", "example_meaning_cn": "请不要（偏心或只看一眼）。", "example_meaning_en": "Please don't be partial / look with one eye."},
        "N1_904": {"example_sentence": "（（固）かた）め（め）て（て）ください。", "example_reading": "かためてください。", "example_meaning_cn": "请使其固化（或变硬）。", "example_meaning_en": "Please solidify / harden it."},
        "N1_905": {"example_sentence": "（（固）かた）ま（ま）っ（っ）て（て）います。", "example_reading": "かたまっています。", "example_meaning_cn": "已经凝固（或变硬）了。", "example_meaning_en": "It has solidified / hardened."},
        "N1_906": {"example_sentence": "（（片）かた）も（も）ち（ち）を（を）し（し）ないで（为）ください。", "example_reading": "かたもちをしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_907": {"example_sentence": "（（片）かた）も（も）の（の）に（に）なり（なり）たい（たい）です。", "example_reading": "かたものになりたいです。", "example_meaning_cn": "想成为（或制作）固定的某样东西。", "example_meaning_en": "I want to be / make something fixed."},
        "N1_908": {"example_sentence": "（（片）かた）よ（よ）ら（ら）ないで（为）ください。", "example_reading": "かたよらないでください。", "example_meaning_cn": "请不要偏颇（或不偏不倚）。", "example_meaning_en": "Please don't be biased."},
        "N1_909": {"example_sentence": "（（片）かた）ら（ら）な（な）い（い）で（为）ください。", "example_reading": "かたらないでください。", "example_meaning_cn": "请不要谈论（或缺少）。", "example_meaning_en": "Please don't speak / doesn't lack."},
        "N1_910": {"example_sentence": "（（片）かた）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "かたわらないでください。", "example_meaning_cn": "请不要（在身边或改变）。", "example_meaning_en": "Please don't (be beside / change)."},
        "N1_911": {"example_sentence": "（（片）かた）わ（わ）ら（ら）の（の）人（ひと）を（を）助け（たすけ）ま（ま）しょ（しょ）う（う）。", "example_reading": "かたわらのひとをたすけましょう。", "example_meaning_cn": "帮助身边的人吧。", "example_meaning_en": "Let's help those beside us."},
        "N1_912": {"example_sentence": "（（片）かた）わ（わ）を（を）防ぎ（ふせぎ）ましょう。", "example_reading": "かたわをふせぎましょう。", "example_meaning_cn": "预防变形（或残疾）吧。", "example_meaning_en": "Let's prevent the deformity / being crippled."},
        "N1_913": {"example_sentence": "（（活）かっ）き（き）を（を）取り戻し（とりもどし）ま（ま）しょ（しょ）う（う）。", "example_reading": "かっきをとりもどしましょう。", "example_meaning_cn": "找回活力吧。", "example_meaning_en": "Let's regain our vitality / vigor."},
        "N1_914": {"example_sentence": "（（活）かっ）き（き）に（に）し（し）ないで（为）ください。", "example_reading": "かっきしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_915": {"example_sentence": "（（画）かっ）き（き）て（て）き（き）な（な）発見（はっけん）です。", "example_reading": "かっきてきなはっけんです。", "example_meaning_cn": "划时代的发现。", "example_meaning_en": "It's an epoch-making discovery."},
        "N1_916": {"example_sentence": "（（活）かっ）き（き）を（を）呈し（ていし）て（て）い（い）ます。", "example_reading": "かっきをていしています。", "example_meaning_cn": "呈现出活力。", "example_meaning_en": "It's showing signs of activity / vigor."},
        "N1_917": {"example_sentence": "（（活）かっ）き（き）つ（つ）し（し）ないで（为）ください。", "example_reading": "かっきつしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_918": {"example_sentence": "（（学）がっ）き（き）を（を）鳴らし（ならし）ま（ま）しょ（しょ）う（う）。", "example_reading": "がっきをならしましょう。", "example_meaning_cn": "奏响乐器吧。", "example_meaning_en": "Let's play the musical instruments."},
        "N1_919": {"example_sentence": "（（学）がっ）き（き）を（を）終え（おえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "がっきをおえましょう。", "example_meaning_cn": "结束学期吧。", "example_meaning_en": "Let's finish the academic term."},
        "N1_920": {"example_sentence": "（（括）かっ）こ（こ）を（を）付け（つけ）て（て）ください。", "example_reading": "かっこをいれてください。", "example_meaning_cn": "请加上括号。", "example_meaning_en": "Please add parentheses."},
        "N1_921": {"example_sentence": "（（格）かっ）こ（こ）う（う）な（な）値段（ねだん）です。", "example_reading": "かっこうなねだんです。", "example_meaning_cn": "合适的价格。", "example_meaning_en": "It's an appropriate price."},
        "N1_922": {"example_sentence": "（（格）かっ）こ（こ）よ（よ）く（く）なり（なり）たい（たい）です。", "example_reading": "かっこよくなりたいです。", "example_meaning_cn": "想变得帅气。", "example_meaning_en": "I want to become cool / stylish."},
        "N1_923": {"example_sentence": "（（活）かっ）さ（さ）し（し）ないで（为）ください。", "example_reading": "かっさしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_924": {"example_sentence": "（（活）かっ）さ（さ）い（い）を（を）送り（おくり）ま（ま）しょ（しょ）う（う）。", "example_reading": "かっさいをおくりましょう。", "example_meaning_cn": "送上喝彩吧。", "example_meaning_en": "Let's give them a round of applause / cheers."},
        "N1_925": {"example_sentence": "（（渇）かっ）さ（さ）い（い）し（し）ないで（为）ください。", "example_reading": "かっさいしないでください。", "example_meaning_cn": "请不要（口渴或喝彩）。", "example_meaning_en": "Please don't (be thirsty / cheer)."},
        "N1_926": {"example_sentence": "（（合）がっ）さ（さ）い（い）し（し）て（て）ください。", "example_reading": "がっさいしてください。", "example_meaning_cn": "请（全部）放在一起。", "example_meaning_en": "Please put everything together."},
        "N1_927": {"example_sentence": "（（渇）かっ）し（し）ないで（为）ください。", "example_reading": "かっしないでください。", "example_meaning_cn": "请不要（口渴或干燥）。", "example_meaning_en": "Please don't (be thirsty / withered)."},
        "N1_928": {"example_sentence": "（（活）かっ）し（し）ゅ（ゅ）う（う）し（し）ないで（为）ください。", "example_reading": "かっしゅうしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_929": {"example_sentence": "（（合）がっ）し（し）ょ（ょ）う（う）を（を）聞き（きき）ま（ま）しょ（しょ）う（う）。", "example_reading": "がっしょうをききましょう。", "example_meaning_cn": "听合唱吧。", "example_meaning_en": "Let's listen to the chorus."},
        "N1_930": {"example_sentence": "（（活）かっ）せ（せ）い（い）し（し）て（て）ください。", "example_reading": "かっせいしてください。", "example_meaning_cn": "请激活（使产生活力）。", "example_meaning_en": "Please activate / stimulate it."},
        "N1_931": {"example_sentence": "（（活）かっ）せ（せ）つ（つ）し（し）ないで（为）ください。", "example_reading": "かっせつしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_932": {"example_sentence": "（（活）かっ）せ（せ）ん（ん）し（し）ないで（为）ください。", "example_reading": "かっせんしないでください。", "example_meaning_cn": "请不要（开战或打斗）。", "example_meaning_en": "Please don't (start a battle / fight)."},
        "N1_933": {"example_sentence": "（（合）がっ）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "がっぜんとしています。", "example_meaning_cn": "骤然（突然）间。", "example_meaning_en": "Suddenly / all of a sudden."},
        "N1_934": {"example_sentence": "（（活）かっ）そ（そ）う（う）し（し）て（て）ください。", "example_reading": "かっそうしてください。", "example_meaning_cn": "请滑行。", "example_meaning_en": "Please glide / taxi."},
        "N1_935": {"example_sentence": "（（活）かっ）そ（そ）く（く）し（し）ないで（为）ください。", "example_reading": "かっそくしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_936": {"example_sentence": "（（活）かっ）た（た）い（い）し（し）ないで（为）ください。", "example_reading": "かったいしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_937": {"example_sentence": "（（合）がっ）た（た）い（い）し（し）て（て）ください。", "example_reading": "がったいしてください。", "example_meaning_cn": "请合并（合体）。", "example_meaning_en": "Please combine / merge it."},
        "N1_938": {"example_sentence": "（（活）かっ）だ（だ）ん（ん）を（を）避け（さけ）て（て）ください。", "example_reading": "かっだんをさけてください。", "example_meaning_cn": "请避免做出断定（或突然）。", "example_meaning_en": "Please avoid making a definitive conclusion."},
        "N1_939": {"example_sentence": "（（活）かっ）ち（ち）を（を）守り（まもり）ま（ま）しょ（しょ）う（う）。", "example_reading": "かっちをまもりましょう。", "example_meaning_cn": "遵守约定（或胜利）吧。", "example_meaning_en": "Let's follow the rule / victory."},
        "N1_940": {"example_sentence": "（（活）かっ）ち（ち）ょ（ょ）う（う）し（し）ないで（为）ください。", "example_reading": "かっちょうしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_941": {"example_sentence": "（（活）かっ）つ（つ）し（し）ないで（为）ください。", "example_reading": "かっつしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_942": {"example_sentence": "（（活）かっ）て（て）に（に）し（し）ないで（为）ください。", "example_reading": "かってにしないでください。", "example_meaning_cn": "请不要随意（自作主张）。", "example_meaning_en": "Please don't do as you please / be selfish."},
        "N1_943": {"example_sentence": "（（活）かっ）と（と）う（う）を（を）乗り越え（のりこえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "かっとうをのりこえましょう。", "example_meaning_cn": "克服纠葛（折磨）吧。", "example_meaning_en": "Let's overcome the conflict / complications."},
        "N1_944": {"example_sentence": "（（活）かっ）と（と）く（く）し（し）ないで（为）ください。", "example_reading": "かっとくしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_945": {"example_sentence": "（（活）かっ）な（な）い（い）で（为）ください。", "example_reading": "かっないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_946": {"example_sentence": "（（活）かっ）ぱ（ぱ）つ（つ）な（な）活動（かつどう）です。", "example_reading": "かっぱつなかつどうです。", "example_meaning_cn": "活泼的活动。", "example_meaning_en": "It's a vigorous / active activity."},
        "N1_947": {"example_sentence": "（（活）かっ）ひ（ひ）し（し）ないで（为）ください。", "example_reading": "かっひしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_948": {"example_sentence": "（（活）かっ）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "かっふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_949": {"example_sentence": "（（活）かっ）ほ（ほ）う（う）し（し）て（て）ください。", "example_reading": "かっほうしてください。", "example_meaning_cn": "请大步走（或活着）。", "example_meaning_en": "Please stride along / be active."},
        "N1_950": {"example_sentence": "（（活）かっ）ま（ま）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "かっまわらないでください。", "example_meaning_cn": "请不要（绕道或改变）。", "example_meaning_en": "Please don't (go around / change)."},
        "N1_951": {"example_sentence": "（（活）かっ）み（み）し（し）ないで（为）ください。", "example_reading": "かっみしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_952": {"example_sentence": "（（活）かっ）め（め）い（い）を（を）受け（うけ）て（て）ください。", "example_reading": "かっめいをうけてください。", "example_meaning_cn": "请接受生命（或活力）。", "example_meaning_en": "Please receive the life / vitality."},
        "N1_953": {"example_sentence": "（（活）かっ）も（も）う（う）し（し）て（て）ください。", "example_reading": "かっもうしてください。", "example_meaning_cn": "请拭目以待（刮目相看）。", "example_meaning_en": "Please watch it with intense interest / expect."},
        "N1_954": {"example_sentence": "（（火）か）つ（つ）よ（よ）う（う）し（し）て（て）ください。", "example_reading": "かつようしてください。", "example_meaning_cn": "请活用（利用）。", "example_meaning_en": "Please utilize / make use of it."},
        "N1_955": {"example_sentence": "（（活）かっ）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "かっらんしないでください。", "example_meaning_cn": "请不要（紊乱或突然）。", "example_meaning_en": "Please don't (disturb / be sudden)."},
        "N1_956": {"example_sentence": "（（活）かっ）り（り）し（し）ないで（为）ください。", "example_reading": "かっりしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_957": {"example_sentence": "（（活）かっ）り（り）ょ（ょ）く（く）に（に）溢れ（あふれ）て（て）い（い）ます。", "example_reading": "かっりょくにあふれています。", "example_meaning_cn": "充满活力。", "example_meaning_en": "Full of vitality / energy."},
        "N1_958": {"example_sentence": "（（活）かっ）る（る）のを（を）手伝っ（てつだっ）て（て）ください。", "example_reading": "かっるのをてつだってください。", "example_meaning_cn": "请帮我旋转（或回去）。", "example_meaning_en": "Please help me rotate / return."},
        "N1_959": {"example_sentence": "（（活）かっ）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "かっれいしないでください。", "example_meaning_cn": "请不要（效法或同样）。", "example_meaning_en": "Please don't (follow suit / be the same)."},
        "N1_960": {"example_sentence": "（（活）かっ）ろ（ろ）を（を）見出し（みいだし）ま（ま）しょ（しょ）う（う）。", "example_reading": "かっろをみいだしましょう。", "example_meaning_cn": "寻找生路吧。", "example_meaning_en": "Let's find a way out / means of survival."},
        "N1_961": {"example_sentence": "（（活）かっ）わ（わ）し（し）ないで（为）ください。", "example_reading": "かっわしないでください。", "example_meaning_cn": "请不要（和谈或对外）。", "example_meaning_en": "Please don't (be at peace / be outward)."},
        "N1_962": {"example_sentence": "（（活）かっ）を（を）入れ（いれ）て（て）ください。", "example_reading": "かつをいれてください。", "example_meaning_cn": "请注入活力（大喝一声）。", "example_meaning_en": "Please put some life into it / stimulate it."},
        "N1_963": {"example_sentence": "（（仮）か）て（て）い（い）を（を）立て（たて）ま（ま）しょ（しょ）う（う）。", "example_reading": "かていをたてましょう。", "example_meaning_cn": "建立假设吧。", "example_meaning_en": "Let's make an assumption / hypothesis."},
        "N1_964": {"example_sentence": "（（仮）か）に（に）し（し）ないで（为）ください。", "example_reading": "かにしないでください。", "example_meaning_cn": "请不要作为假定（临时）。", "example_meaning_en": "Please don't make it provisional."},
        "N1_965": {"example_sentence": "（（仮）か）の（の）人（ひと）を（を）信じ（しんじ）ないで（为）ください。", "example_reading": "かのひとをしんじないでください。", "example_meaning_cn": "不要相信那个人（虚幻的）。", "example_meaning_en": "Don't believe that person / fictional person."},
        "N1_966": {"example_sentence": "（（仮）か）ば（ば）な（な）し（し）を（を）し（し）ないで（为）ください。", "example_reading": "かばなしをしないでください。", "example_meaning_cn": "请不要说假话。", "example_meaning_en": "Please don't tell a lie / fiction."},
        "N1_967": {"example_sentence": "（（仮）か）ふ（ふ）し（し）ないで（为）ください。", "example_reading": "かふしないでください。", "example_meaning_cn": "请不要（说漏或放过）。", "example_meaning_en": "Please don't (omit saying / let it pass)."},
        "N1_968": {"example_sentence": "（（仮）か）ら（ら）ん（ん）し（し）ないで（为）ください。", "example_reading": "からんしないでください。", "example_meaning_cn": "请不要（缠绕或纠缠）。", "example_meaning_en": "Please don't (get entangled / pester)."},
        "N1_969": {"example_sentence": "（（仮）か）り（り）し（し）ないで（为）ください。", "example_reading": "かりしないでください。", "example_meaning_cn": "请不要（借用或假定）。", "example_meaning_en": "Please don't (borrow / assume)."},
        "N1_970": {"example_sentence": "（（仮）か）れ（れ）い（い）し（し）ないで（为）ください。", "example_reading": "かれいしないでください。", "example_meaning_cn": "请不要（凋谢或同样）。", "example_meaning_en": "Please don't (wither / follow same path)."},
        "N1_971": {"example_sentence": "（（仮）か）わ（わ）し（し）ないで（为）ください。", "example_reading": "かわしないでください。", "example_meaning_cn": "请不要（交换或回避）。", "example_meaning_en": "Please don't (exchange / avoid)."},
        "N1_972": {"example_sentence": "（（仮）か）を（を）尽くし（つくし）て（て）ください。", "example_reading": "かをつくしてください。", "example_meaning_cn": "请极尽（临时或虚幻）。", "example_meaning_en": "Please do your utmost in this provisional way."},
        "N1_973": {"example_sentence": "（（仮）か）わ（わ）ず（ず）に（に）い（い）て（て）ください。", "example_reading": "かわらずにいてください。", "example_meaning_cn": "请保持不变。", "example_meaning_en": "Please stay the same."},
        "N1_974": {"example_sentence": "（（仮）か）わ（わ）ら（ら）ないで（为）ください。", "example_reading": "かわらないでください。", "example_meaning_cn": "请不要改变（或不替代）。", "example_meaning_en": "Please don't change."},
        "N1_975": {"example_sentence": "（（仮）か）わ（わ）り（り）に（に）し（し）て（て）ください。", "example_reading": "かわりにしてください。", "example_meaning_cn": "请作为替代。", "example_meaning_en": "Please make it a substitute."},
        "N1_976": {"example_sentence": "（（仮）か）わ（わ）る（る）のを（を）手伝っ（てつだっ）て（て）ください。", "example_reading": "かわるのをてつだってください。", "example_meaning_cn": "请帮我更换（或改变）。", "example_meaning_en": "Please help me change / replace it."},
        "N1_977": {"example_sentence": "（（仮）か）ん（ん）し（し）ないで（为）ください。", "example_reading": "かんしないでください。", "example_meaning_cn": "请不要（看管或忽视）。", "example_meaning_en": "Please don't (oversee / ignore)."},
        "N1_978": {"example_sentence": "（（仮）か）ん（ん）を（を）深め（ふかめ）ま（ま）しょ（しょ）う（う）。", "example_reading": "かんをふかめましょう。", "example_meaning_cn": "深化（直觉或理解）吧。", "example_meaning_en": "Let's deepen our intuition / feeling."},
        "N1_979": {"example_sentence": "（（仮）か）を（を）向け（むけ）て（て）ください。", "example_reading": "かをむけてください。", "example_meaning_cn": "请面向（或引导）。", "example_meaning_en": "Please face it / direct it."},
        "N1_980": {"example_sentence": "（（仮）か）を（を）向け（むけ）ないで（为）ください。", "example_reading": "かをむけないでください。", "example_meaning_cn": "请不要面向（或忽视）。", "example_meaning_en": "Please don't face it / ignore it."},
        "N1_981": {"example_sentence": "（（仮）か）ん（ん）を（を）磨き（みがき）ま（ま）しょ（しょ）う（う）。", "example_reading": "かんをみがきましょう。", "example_meaning_cn": "磨练直觉（灵感）吧。", "example_meaning_en": "Let's polish our intuition."},
        "N1_982": {"example_sentence": "（（関）かん）し（し）ん（ん）が（が）あり（あり）ますか。", "example_reading": "かんしんがありますか。", "example_meaning_cn": "感兴趣吗？", "example_meaning_en": "Are you interested?"},
        "N1_983": {"example_sentence": "（（感）かん）し（し）ん（ん）な（な）行い（おこない）です。", "example_reading": "かんしんなおこないです。", "example_meaning_cn": "钦佩的（值得赞扬的）行为。", "example_meaning_en": "It's an admirable act."},
        "N1_984": {"example_sentence": "（（感）かん）し（し）ん（ん）し（し）て（て）ください。", "example_reading": "かんしんしてください。", "example_meaning_cn": "请佩服（赞赏）。", "example_meaning_en": "Please be impressed / admire it."},
        "N1_985": {"example_sentence": "（（寒）かん）し（し）ん（ん）に（に）耐え（たえ）ま（ま）しょ（しょ）う（う）。", "example_reading": "かんしんにたえましょう。", "example_meaning_cn": "忍耐寒冷的环境吧。", "example_meaning_en": "Let's endure the cold heart / environment."},
        "N1_986": {"example_sentence": "（（関）かん）し（し）ょ（ょ）う（う）し（し）ないで（为）ください。", "example_reading": "かんしょうしないでください。", "example_meaning_cn": "请不要干涉。", "example_meaning_en": "Please don't interfere / intervene."},
        "N1_987": {"example_sentence": "（（鑑）かん）し（し）ょ（ょ）う（う）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "かんしょうをたのしみましょう。", "example_meaning_cn": "享受鉴赏吧。", "example_meaning_en": "Let's enjoy the appreciation / viewing."},
        "N1_988": {"example_sentence": "（（感）かん）し（し）ょ（ょ）う（う）に（に）浸り（ひたり）ま（ま）しょ（しょ）う（う）。", "example_reading": "かんしょうにひたりましょう。", "example_meaning_cn": "沉浸在感伤中吧。", "example_meaning_en": "Let's indulge in sentimentality."},
        "N1_989": {"example_sentence": "（（観）かん）し（し）ょ（ょ）う（う）し（し）て（て）ください。", "example_reading": "かんしょうしてください。", "example_meaning_cn": "请观赏。", "example_meaning_en": "Please watch / observe."},
        "N1_990": {"example_sentence": "（（汗）かん）す（す）う（う）を（を）整え（ととなえ）て（て）ください。", "example_reading": "かんすうをととなえてください。", "example_meaning_cn": "请整理函数（或数值）。", "example_meaning_en": "Please adjust the function / values."},
        "N1_991": {"example_sentence": "（（関）かん）ぜ（ぜ）ん（ん）と（と）し（し）て（て）い（い）ます。", "example_reading": "かんぜんとしています。", "example_meaning_cn": "完全（恬静）着。", "example_meaning_en": "It's complete / quiet."},
        "N1_992": {"example_sentence": "（（関）かん）せ（せ）い（い）を（を）上げ（あげ）ま（ま）しょ（しょ）う（う）。", "example_reading": "かんせいをあげましょう。", "example_meaning_cn": "欢呼吧。", "example_meaning_en": "Let's give a shout for joy / cheer."},
        "N1_993": {"example_sentence": "（（完）かん）せ（せ）い（い）し（し）て（て）ください。", "example_reading": "かんせいしてください。", "example_meaning_cn": "请完成。", "example_meaning_en": "Please complete it."},
        "N1_994": {"example_sentence": "（（感）かん）せ（せ）い（い）を（を）磨き（みがき）ま（ま）しょ（しょ）う（う）。", "example_reading": "かんせいをみがきましょう。", "example_meaning_cn": "磨练感性吧。", "example_meaning_en": "Let's polish our sensitivity / aesthetic sense."},
        "N1_995": {"example_sentence": "（（官）かん）せ（せ）い（い）の（の）仕事（しごと）です。", "example_reading": "かんせいのしごとです。", "example_meaning_cn": "政府（官办）的工作。", "example_meaning_en": "It's a government / official job."},
        "N1_996": {"example_sentence": "（（陥）かん）せ（せ）つ（つ）し（し）ないで（为）ください。", "example_reading": "かんせつしないでください。", "example_meaning_cn": "请不要（塌陷或关节）。", "example_meaning_en": "Please don't (collapse / be indirect)."},
        "N1_997": {"example_sentence": "（（関）かん）せ（せ）つ（つ）的（てき）な（な）影響（えいきょう）です。", "example_reading": "かんせつてきなえいきょうです。", "example_meaning_cn": "间接的影响。", "example_meaning_en": "It's an indirect influence."},
        "N1_998": {"example_sentence": "（（関）かん）せ（せ）ん（ん）を（を）楽しみ（たのしみ）ましょう。", "example_reading": "かんせんをたのしみましょう。", "example_meaning_cn": "享受观战吧。", "example_meaning_en": "Let's enjoy watching the game."},
        "N1_999": {"example_sentence": "（（感）かん）せ（せ）ん（ん）を（を）防ぎ（ふせぎ）ましょう。", "example_reading": "かんせんをふせぎましょう。", "example_meaning_cn": "预防感染吧。", "example_meaning_en": "Let's prevent the infection."},
        "N1_1000": {"example_sentence": "（（完）かん）ぞ（ぞ）う（う）を（を）大切（たいせつ）に（に）し（し）ましょう。", "example_reading": "かんぞうをたいせつにしましょう。", "example_meaning_cn": "珍惜肝脏（或完全拥有）吧。", "example_meaning_en": "Let's take care of our liver / possess completely."}
    }

    for item in vocab:
        if item['id'] in enrichment:
            item.update(enrichment[item['id']])

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print(f"Updated items up to N1_1000.")

if __name__ == "__main__":
    main()
