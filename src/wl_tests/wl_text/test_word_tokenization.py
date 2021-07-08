# -*- coding: utf-8 -*-

#
# Wordless: Tests - Text - Word Tokenization
#
# Copyright (C) 2018-2021  Ye Lei (叶磊)
#
# This source file is licensed under GNU GPLv3.
# For details, see: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#
# All other rights reserved.
#

import re
import sys

sys.path.append('.')

import pytest

from wl_tests import wl_test_init, wl_test_lang_examples
from wl_text import wl_word_tokenization
from wl_utils import wl_conversion, wl_misc

test_word_tokenizers = []

main = wl_test_init.Wl_Test_Main()

for lang, word_tokenizers in main.settings_global['word_tokenizers'].items():
    for word_tokenizer in word_tokenizers:
        if lang not in ['other']:
            if lang != 'eng':
                if 'NLTK' not in word_tokenizer or 'Tok-tok' in word_tokenizer:
                    test_word_tokenizers.append((lang, word_tokenizer))
            else:
                test_word_tokenizers.append((lang, word_tokenizer))

@pytest.mark.parametrize('lang, word_tokenizer', test_word_tokenizers)
def test_word_tokenize(lang, word_tokenizer, show_results = False):
    lang_text = wl_conversion.to_lang_text(main, lang)

    tokens = wl_word_tokenization.wl_word_tokenize(
        main,
        text = getattr(wl_test_lang_examples, f'SENTENCE_{lang.upper()}'),
        lang = lang,
        word_tokenizer = word_tokenizer
    )
    tokens = list(wl_misc.flatten_list(tokens))

    if show_results:
        print(f'{lang} / {word_tokenizer}:')
        print(tokens)

    if lang == 'afr':
        assert tokens == ['Afrikaans', 'is', 'tipologies', 'beskou', "'", 'n', 'Indo', '-', 'Europese', ',', 'Wes', '-', 'Germaanse', ',', 'Nederfrankiese', 'taal,[2', ']', 'wat', 'aan', 'die', 'suidpunt', 'van', 'Afrika', 'onder', 'invloed', 'van', 'verskeie', 'ander', 'tale', 'en', 'taalgroepe', 'ontstaan', 'het', '.']
    elif lang == 'sqi':
        assert tokens == ['Gjuha', 'shqipe', '(', 'ose', 'thjeshtë', 'shqipja', ')', 'është', 'gjuhë', 'dhe', 'degë', 'e', 'veçantë', 'e', 'familjes', 'indo', '-', 'evropiane', 'të', 'folur', 'nga', 'më', 'shumë', 'se', '6', 'milionë', 'njerëz[4', ']', ',', 'kryesisht', 'në', 'Shqipëri', ',', 'Kosovë', 'dhe', 'Republikën', 'e', 'Maqedonisë', ',', 'por', 'edhe', 'në', 'zona', 'të', 'tjera', 'të', 'Evropës', 'Jugore', 'ku', 'ka', 'një', 'popullsi', 'shqiptare', ',', 'duke', 'përfshirë', 'Malin', 'e', 'Zi', 'dhe', 'Luginën', 'e', 'Preshevës', '.']
    elif lang == 'amh':
        assert tokens == ['አማርኛ[1', ']', '፡', 'የኢትዮጵያ', '፡', 'መደበኛ', '፡', 'ቋንቋ', '፡', 'ነው', '።']
    elif lang == 'ara':
        assert tokens == ['اللُّغَة', 'العَرَبِيّة', 'هي', 'أكثر', 'اللغات', 'السامية', 'تحدثاً', 'وإحدى', 'أكثر', 'اللغات', 'انتشاراً', 'في', 'العالم', '،', 'يتحدثها', 'أكثر', 'من', '467', 'مليون', 'نسمة،(1', ')', 'ويتوزع', 'متحدثوها', 'في', 'الوطن', 'العربي', '،', 'بالإضافة', 'إلى', 'العديد', 'من', 'المناطق', 'الأخرى', 'المجاورة', 'كالأهواز', 'وتركيا', 'وتشاد', 'ومالي', 'والسنغال', 'وإرتيريا', 'وإثيوبيا', 'وجنوب', 'السودان', 'وإيران', '.']
    elif lang == 'hye':
        assert tokens == ['Հայերեն', '(', 'ավանդական՝', 'հայերէն', ')', ',', 'հնդեվրոպական', 'լեզվաընտանիքի', 'առանձին', 'ճյուղ', 'հանդիսացող', 'լեզու։']
    elif lang == 'asm':
        assert tokens == ['অসমীয়া', 'ভাষা', 'হৈছে', 'সকলোতকৈ', 'পূৰ্বীয়', 'ভাৰতীয়-আৰ্য', 'ভাষা', '।']
    elif lang == 'eus':
        assert tokens == ['Euskara', 'Euskal', 'Herriko', 'hizkuntza', 'da.[5', ']']
    elif lang == 'ben':
        if word_tokenizer == 'Sacremoses - Moses Tokenizer':
            assert tokens == ['বাংলা', 'ভাষা', '(', 'বাঙলা', ',', 'বাঙ্গলা', ',', 'তথা', 'বাঙ্গালা', 'নামগুলোতেও', 'পরিচিত', ')', 'একটি', 'ইন্দো-আর্য', 'ভাষা', ',', 'যা', 'দক্ষিণ', 'এশিয়ার', 'বাঙালি', 'জাতির', 'প্রধান', 'কথ্য', 'ও', 'লেখ্য', 'ভাষা', '।']
        elif word_tokenizer == 'spaCy - Bengali Word Tokenizer':
            assert tokens == ['বাংলা', 'ভাষা', '(', 'বাঙলা', ',', 'বাঙ্গলা', ',', 'তথা', 'বাঙ্গালা', 'নামগুলোতেও', 'পরিচিত', ')', 'একটি', 'ইন্দো', '-', 'আর্য', 'ভাষা', ',', 'যা', 'দক্ষিণ', 'এশিয়ার', 'বাঙালি', 'জাতির', 'প্রধান', 'কথ্য', 'ও', 'লেখ্য', 'ভাষা', '।']
    elif lang == 'bul':
        assert tokens == ['Бъ̀лгарският', 'езѝк', 'е', 'индоевропейски', 'език', 'от', 'групата', 'на', 'южнославянските', 'езици', '.']
    elif lang == 'cat':
        if word_tokenizer == 'Sacremoses - Moses Tokenizer':
            assert tokens == ['El', 'català', '(', 'denominació', 'oficial', 'a', 'Catalunya', ',', 'a', 'les', 'Illes', 'Balears', ',', 'a', 'Andorra', ',', 'a', 'la', 'ciutat', 'de', 'l', "'", 'Alguer', 'i', 'tradicional', 'a', 'Catalunya', 'Nord', ')', 'o', 'valencià', '(', 'denominació', 'oficial', 'al', 'País', 'Valencià', 'i', 'tradicional', 'al', 'Carxe', ')', 'és', 'una', 'llengua', 'romànica', 'parlada', 'a', 'Catalunya', ',', 'el', 'País', 'Valencià', '(', 'tret', 'd', "'", 'algunes', 'comarques', 'i', 'localitats', 'de', 'l', "'", 'interior', ')', ',', 'les', 'Illes', 'Balears', ',', 'Andorra', ',', 'la', 'Franja', 'de', 'Ponent', '(', 'a', 'l', "'", 'Aragó', ')', ',', 'la', 'ciutat', 'de', 'l', "'", 'Alguer', '(', 'a', 'l', "'", 'illa', 'de', 'Sardenya', ')', ',', 'la', 'Catalunya', 'del', 'Nord', ',', '[', '8', ']', 'el', 'Carxe', '(', 'un', 'petit', 'territori', 'de', 'Múrcia', 'poblat', 'per', 'immigrats', 'valencians', ')', ',', '[', '9', ']', '[', '10', ']', 'i', 'en', 'petites', 'comunitats', 'arreu', 'del', 'món', '(', 'entre', 'les', 'quals', 'destaca', 'la', 'de', 'l', "'", 'Argentina', ',', 'amb', '195.000', 'parlants', ')', '.', '[', '11', ']']
        elif word_tokenizer == 'spaCy - Catalan Word Tokenizer':
            assert tokens == ['El', 'català', '(', 'denominació', 'oficial', 'a', 'Catalunya', ',', 'a', 'les', 'Illes', 'Balears', ',', 'a', 'Andorra', ',', 'a', 'la', 'ciutat', 'de', "l'", 'Alguer', 'i', 'tradicional', 'a', 'Catalunya', 'Nord', ')', 'o', 'valencià', '(', 'denominació', 'oficial', 'al', 'País', 'Valencià', 'i', 'tradicional', 'al', 'Carxe', ')', 'és', 'una', 'llengua', 'romànica', 'parlada', 'a', 'Catalunya', ',', 'el', 'País', 'Valencià', '(', 'tret', "d'", 'algunes', 'comarques', 'i', 'localitats', 'de', "l'", 'interior', ')', ',', 'les', 'Illes', 'Balears', ',', 'Andorra', ',', 'la', 'Franja', 'de', 'Ponent', '(', 'a', "l'", 'Aragó', ')', ',', 'la', 'ciutat', 'de', "l'", 'Alguer', '(', 'a', "l'", 'illa', 'de', 'Sardenya', ')', ',', 'la', 'Catalunya', 'del', 'Nord,[8', ']', 'el', 'Carxe', '(', 'un', 'petit', 'territori', 'de', 'Múrcia', 'poblat', 'per', 'immigrats', 'valencians),[9][10', ']', 'i', 'en', 'petites', 'comunitats', 'arreu', 'del', 'món', '(', 'entre', 'les', 'quals', 'destaca', 'la', 'de', "l'", 'Argentina', ',', 'amb', '195.000', 'parlants).[11', ']']
    elif lang == 'zho_cn':
        if word_tokenizer == 'jieba - Chinese Word Tokenizer':
            assert tokens == ['汉语', '，', '又称', '汉文', '、', '中文', '、', '中国', '话', '、', '中国', '语', '、', '华语', '、', '华文', '、', '唐话', '[', '2', ']', '，', '或', '被', '视为', '一个', '语族', '，', '或', '被', '视为', '隶属于', '汉藏语系', '汉语', '族', '之', '一种', '语言', '。']
        elif word_tokenizer == 'pkuseg - Chinese Word Tokenizer':
            assert tokens == ['汉语', '，', '又', '称', '汉文', '、', '中文', '、', '中国话', '、', '中国语', '、', '华语', '、', '华文', '、', '唐', '话[', '2', ']', '，', '或', '被', '视为', '一个', '语族', '，', '或', '被', '视为', '隶属于', '汉藏', '语系', '汉语族', '之一', '种', '语言', '。']
        elif word_tokenizer == 'Wordless - Chinese Character Tokenizer':
            assert tokens == ['汉', '语', '，', '又', '称', '汉', '文', '、', '中', '文', '、', '中', '国', '话', '、', '中', '国', '语', '、', '华', '语', '、', '华', '文', '、', '唐', '话', '[', '2', ']', '，', '或', '被', '视', '为', '一', '个', '语', '族', '，', '或', '被', '视', '为', '隶', '属', '于', '汉', '藏', '语', '系', '汉', '语', '族', '之', '一', '种', '语', '言', '。']
    elif lang == 'zho_tw':
        if word_tokenizer == 'jieba - Chinese Word Tokenizer':
            assert tokens == ['漢語', '，', '又', '稱漢文', '、', '中文', '、', '中國話', '、', '中國語', '、', '華語', '、', '華文', '、', '唐話', '[', '2', ']', '，', '或', '被', '視為', '一個', '語族', '，', '或', '被', '視為', '隸屬', '於', '漢藏語', '系漢', '語族', '之一', '種語', '言', '。']
        elif word_tokenizer == 'pkuseg - Chinese Word Tokenizer':
            assert tokens == ['漢語', '，', '又', '稱', '漢文', '、', '中文', '、', '中', '國話', '、', '中國語', '、', '華語', '、', '華文', '、', '唐', '話[', '2', ']', '，', '或', '被', '視為', '一', '個', '語族', '，', '或', '被', '視', '為隸', '屬於', '漢藏', '語系', '漢語族', '之一', '種', '語言', '。']
        elif word_tokenizer == 'Wordless - Chinese Character Tokenizer':
            assert tokens == ['漢', '語', '，', '又', '稱', '漢', '文', '、', '中', '文', '、', '中', '國', '話', '、', '中', '國', '語', '、', '華', '語', '、', '華', '文', '、', '唐', '話', '[', '2', ']', '，', '或', '被', '視', '為', '一', '個', '語', '族', '，', '或', '被', '視', '為', '隸', '屬', '於', '漢', '藏', '語', '系', '漢', '語', '族', '之', '一', '種', '語', '言', '。']
    elif lang == 'hrv':
        assert tokens == ['Hrvatski', 'jezik', '(', 'ISO', '639', '-', '3', ':', 'hrv', ')', 'skupni', 'je', 'naziv', 'za', 'nacionalni', 'standardni', 'jezik', 'Hrvata', ',', 'te', 'za', 'skup', 'narječja', 'i', 'govora', 'kojima', 'govore', 'ili', 'su', 'nekada', 'govorili', 'Hrvati', '.']
    elif lang == 'ces':
        assert tokens == ['Čeština', 'neboli', 'český', 'jazyk', 'je', 'západoslovanský', 'jazyk', ',', 'nejbližší', 'slovenštině', ',', 'poté', 'lužické', 'srbštině', 'a', 'polštině', '.']
    elif lang == 'dan':
        assert tokens == ['Dansk', 'er', 'et', 'nordgermansk', 'sprog', 'af', 'den', 'østnordiske', '(', 'kontinentale', ')', 'gruppe', ',', 'der', 'tales', 'af', 'ca.', 'seks', 'millioner', 'mennesker', '.']
    elif lang == 'nld':
        assert tokens == ['Het', 'Nederlands', 'is', 'een', 'West-Germaanse', 'taal', 'en', 'de', 'officiële', 'taal', 'van', 'Nederland', ',', 'Suriname', 'en', 'een', 'van', 'de', 'drie', 'officiële', 'talen', 'van', 'België', '.']
    elif lang == 'eng':
        if word_tokenizer in ['NLTK - NIST Tokenizer',
                              'NLTK - Twitter Tokenizer',
                              'Sacremoses - Moses Tokenizer']:
            assert tokens == ['English', 'is', 'a', 'West', 'Germanic', 'language', 'originally', 'spoken', 'by', 'the', 'early', 'medieval', 'England', '.', '[', '3', ']', '[', '4', ']', '[', '5', ']']
        elif word_tokenizer in ['NLTK - NLTK Tokenizer',
                                'NLTK - Penn Treebank Tokenizer',
                                'syntok - Word Tokenizer']:
            assert tokens == ['English', 'is', 'a', 'West', 'Germanic', 'language', 'originally', 'spoken', 'by', 'the', 'early', 'medieval', 'England.', '[', '3', ']', '[', '4', ']', '[', '5', ']']
        elif word_tokenizer == 'NLTK - Tok-tok Tokenizer':
            assert tokens == ['English', 'is', 'a', 'West', 'Germanic', 'language', 'originally', 'spoken', 'by', 'the', 'early', 'medieval', 'England.[', '3', ']', '[', '4', ']', '[', '5', ']']
        elif word_tokenizer == 'spaCy - English Word Tokenizer':
            assert tokens == ['English', 'is', 'a', 'West', 'Germanic', 'language', 'originally', 'spoken', 'by', 'the', 'early', 'medieval', 'England.[3][4][5', ']']
    elif lang == 'est':
        assert tokens == ['Eesti', 'keel', '(', 'varasem', 'nimetus', 'maakeel', ')', 'on', 'läänemeresoome', 'lõunarühma', 'kuuluv', 'keel', '.']
    elif lang == 'fin':
        assert tokens == ['Suomen', 'kieli', '(', 'suomi', ')', 'on', 'uralilaisten', 'kielten', 'itämerensuomalaiseen', 'ryhmään', 'kuuluva', 'kieli', '.']
    elif lang == 'fra':
        assert tokens == ['Le', 'français', 'est', 'une', 'langue', 'indo-européenne', 'de', 'la', 'famille', 'des', 'langues', 'romanes', 'dont', 'les', 'locuteurs', 'sont', 'appelés', 'francophones', '.']
    elif lang == 'deu':
        if word_tokenizer == 'NLTK - Tok-tok Tokenizer':
            assert tokens == ['Die', 'deutsche', 'Sprache', 'bzw.', 'das', 'Deutsche', '(', '[', 'dɔɪ̯tʃ', ']', ';', '[', '26', ']', 'abgekürzt', 'dt', '.', 'oder', 'dtsch.', ')', 'ist', 'eine', 'westgermanische', 'Sprache', ',', 'die', 'weltweit', 'etwa', '90', 'bis', '105', 'Millionen', 'Menschen', 'als', 'Muttersprache', 'und', 'weiteren', 'rund', '80', 'Millionen', 'als', 'Zweit-', 'oder', 'Fremdsprache', 'dient', '.']
        elif word_tokenizer == 'Sacremoses - Moses Tokenizer':
            assert tokens == ['Die', 'deutsche', 'Sprache', 'bzw.', 'das', 'Deutsche', '(', '[', 'dɔɪ', '̯', 'tʃ', ']', ';', '[', '26', ']', 'abgekürzt', 'dt', '.', 'oder', 'dtsch', '.', ')', 'ist', 'eine', 'westgermanische', 'Sprache', ',', 'die', 'weltweit', 'etwa', '90', 'bis', '105', 'Millionen', 'Menschen', 'als', 'Muttersprache', 'und', 'weiteren', 'rund', '80', 'Millionen', 'als', 'Zweit-', 'oder', 'Fremdsprache', 'dient', '.']
        elif word_tokenizer == 'spaCy - German Word Tokenizer':
            assert tokens == ['Die', 'deutsche', 'Sprache', 'bzw.', 'das', 'Deutsche', '(', '[', 'dɔɪ̯tʃ];[26', ']', 'abgekürzt', 'dt', '.', 'oder', 'dtsch', '.', ')', 'ist', 'eine', 'westgermanische', 'Sprache', ',', 'die', 'weltweit', 'etwa', '90', 'bis', '105', 'Millionen', 'Menschen', 'als', 'Muttersprache', 'und', 'weiteren', 'rund', '80', 'Millionen', 'als', 'Zweit-', 'oder', 'Fremdsprache', 'dient', '.']
        elif word_tokenizer == 'syntok - Word Tokenizer':
            assert tokens == ['Die', 'deutsche', 'Sprache', 'bzw', '.', 'das', 'Deutsche', '(', '[', 'dɔɪ̯tʃ', ']', ';', '[', '26', ']', 'abgekürzt', 'dt', '.', 'oder', 'dtsch', '.', ')', 'ist', 'eine', 'westgermanische', 'Sprache', ',', 'die', 'weltweit', 'etwa', '90', 'bis', '105', 'Millionen', 'Menschen', 'als', 'Muttersprache', 'und', 'weiteren', 'rund', '80', 'Millionen', 'als', 'Zweit', '-', 'oder', 'Fremdsprache', 'dient', '.']
    elif lang == 'ell':
        if word_tokenizer == 'Sacremoses - Moses Tokenizer':
            assert tokens == ['Η', 'ελληνική', 'γλώσσα', 'ανήκει', 'στην', 'ινδοευρωπαϊκή', 'οικογένεια', '[', '10', ']', 'και', 'αποτελεί', 'το', 'μοναδικό', 'μέλος', 'του', 'ελληνικού', 'κλάδου', ',', 'ενώ', 'είναι', 'η', 'επίσημη', 'γλώσσα', 'της', 'Ελλάδος', 'και', 'της', 'Κύπρου', '.']
        elif word_tokenizer == 'spaCy - Greek (Modern) Word Tokenizer':
            assert tokens == ['Η', 'ελληνική', 'γλώσσα', 'ανήκει', 'στην', 'ινδοευρωπαϊκή', 'οικογένεια[10', ']', 'και', 'αποτελεί', 'το', 'μοναδικό', 'μέλος', 'του', 'ελληνικού', 'κλάδου', ',', 'ενώ', 'είναι', 'η', 'επίσημη', 'γλώσσα', 'της', 'Ελλάδος', 'και', 'της', 'Κύπρου', '.']
    elif lang == 'guj':
        if word_tokenizer == 'Sacremoses - Moses Tokenizer':
            assert tokens == ['ગુજરાતી', '\u200d', '(', '/', 'ɡʊdʒəˈrɑːti', '/', '[', '૭', ']', ',', 'રોમન', 'લિપિમાં', ':', 'Gujarātī', ',', 'ઉચ્ચાર', ':', '[', 'ɡudʒəˈɾɑːtiː', ']', ')', 'ભારત', 'દેશના', 'ગુજરાત', 'રાજ્યની', 'ઇન્ડો-આર્યન', 'ભાષા', 'છે', ',', 'અને', 'મુખ્યત્વે', 'ગુજરાતી', 'લોકો', 'દ્વારા', 'બોલાય', 'છે', '.']
        elif word_tokenizer == 'spaCy - Gujarati Word Tokenizer':
            assert tokens == ['ગુજરાતી', '\u200d(/ɡʊdʒəˈrɑːti/[૭', ']', ',', 'રોમન', 'લિપિમાં', ':', 'Gujarātī', ',', 'ઉચ્ચાર', ':', '[', 'ɡudʒəˈɾɑːtiː', ']', ')', 'ભારત', 'દેશના', 'ગુજરાત', 'રાજ્યની', 'ઇન્ડો-આર્યન', 'ભાષા', 'છે', ',', 'અને', 'મુખ્યત્વે', 'ગુજરાતી', 'લોકો', 'દ્વારા', 'બોલાય', 'છે.']
    elif lang == 'heb':
        assert tokens == ['עִבְרִית', 'היא', 'שפה', 'שמית', ',', 'ממשפחת', 'השפות', 'האפרו', '-', 'אסיאתיות', ',', 'הידועה', 'כשפתם', 'של', 'היהודים', 'ושל', 'השומרונים', ',', 'אשר', 'ניב', 'מודרני', 'שלה', '(', 'עברית', 'ישראלית', ')', 'הוא', 'שפתה', 'הרשמית', 'של', 'מדינת', 'ישראל', ',', 'מעמד', 'שעוגן', 'בשנת', '2018', 'בחוק', 'יסוד', ':', 'ישראל', '–', 'מדינת', 'הלאום', 'של', 'העם', 'היהודי', '.']
    elif lang == 'hin':
        assert tokens == ['हिन्दी', 'विश्व', 'की', 'एक', 'प्रमुख', 'भाषा', 'है', 'एवं', 'भारत', 'की', 'राजभाषा', 'है', '।']
    elif lang == 'hun':
        assert tokens == ['A', 'magyar', 'nyelv', 'az', 'uráli', 'nyelvcsalád', 'tagja', ',', 'a', 'finnugor', 'nyelvek', 'közé', 'tartozó', 'ugor', 'nyelvek', 'egyike', '.']
    elif lang == 'isl':
        if word_tokenizer == 'spaCy - Icelandic Word Tokenizer':
            assert tokens == ['Íslenska', 'er', 'vesturnorrænt', ',', 'germanskt', 'og', 'indóevrópskt', 'tungumál', 'sem', 'er', 'einkum', 'talað', 'og', 'ritað', 'á', 'Íslandi', 'og', 'er', 'móðurmál', 'langflestra', 'Íslendinga.[4', ']']
        elif word_tokenizer == 'Tokenizer - Icelandic Word Tokenizer':
            assert tokens == ['Íslenska', 'er', 'vesturnorrænt', ',', 'germanskt', 'og', 'indóevrópskt', 'tungumál', 'sem', 'er', 'einkum', 'talað', 'og', 'ritað', 'á', 'Íslandi', 'og', 'er', 'móðurmál', 'langflestra', 'Íslendinga', '.', '[', '4', ']']
    elif lang == 'ind':
        assert tokens == ['Bahasa', 'Indonesia', 'adalah', 'bahasa', 'Melayu', 'baku', 'yang', 'dijadikan', 'sebagai', 'bahasa', 'resmi', 'Republik', 'Indonesia[1', ']', 'dan', 'bahasa', 'persatuan', 'bangsa', 'Indonesia.[2', ']']
    elif lang == 'gle':
        assert tokens == ['Is', 'ceann', 'de', 'na', 'teangacha', 'Ceilteacha', 'í', 'an', 'Ghaeilge', '(', 'nó', 'Gaeilge', 'na', 'hÉireann', 'mar', 'a', 'thugtar', 'uirthi', 'corruair', ')', ',', 'agus', 'ceann', 'den', 'dtrí', 'cinn', 'de', 'theangacha', 'Ceilteacha', 'ar', 'a', 'dtugtar', 'na', 'teangacha', 'Gaelacha', '(', '.i.', 'an', 'Ghaeilge', ',', 'Gaeilge', 'na', 'hAlban', 'agus', 'Gaeilge', 'Mhanann', ')', 'go', 'háirithe', '.']
    elif lang == 'ita':
        if word_tokenizer == 'Sacremoses - Moses Tokenizer':
            assert tokens == ["L'", 'italiano', '(', '[', 'itaˈljaːno', ']', '[', 'Nota', '1', ']', 'ascolta', '[', '?', '·', 'info', ']', ')', 'è', 'una', 'lingua', 'romanza', 'parlata', 'principalmente', 'in', 'Italia', '.']
        elif word_tokenizer == 'spaCy - Italian Word Tokenizer':
            assert tokens == ["L'", 'italiano', '(', '[', 'itaˈljaːno][Nota', '1', ']', 'ascolta[?·info', ']', ')', 'è', 'una', 'lingua', 'romanza', 'parlata', 'principalmente', 'in', 'Italia', '.']
    elif lang == 'jpn':
        if word_tokenizer == 'nagisa - Japanese Word Tokenizer':
            assert tokens == ['日本', '語', '(', 'にほんご', '、', 'にっぽん', 'ご', '[', '注', '2', ']', '、', '英', ':', 'Japanese', ')', 'は', '、', '主に', '日本', '国', '内', 'や', '日本', '人', '同士', 'の', '間', 'で', '使用', 'さ', 'れ', 'て', 'いる', '言語', '。']
        elif word_tokenizer == 'Wordless - Japanese Kanji Tokenizer':
            assert tokens == ['日', '本', '語', '（', 'にほんご', '、', 'にっぽん', 'ご', '[', '注', '2', ']', '、', '英', ':', 'Japanese', '）', 'は', '、', '主', 'に', '日', '本', '国', '内', 'や', '日', '本', '人', '同', '士', 'の', '間', 'で', '使', '用', 'さ', 'れ', 'て', 'いる', '言', '語', '。']
    elif lang == 'kan':
        assert tokens == ['ದ್ರಾವಿಡ', 'ಭಾಷೆಗಳಲ್ಲಿ', 'ಪ್ರಾಮುಖ್ಯವುಳ್ಳ', 'ಭಾಷೆಯೂ', 'ಭಾರತದ', 'ಪುರಾತನವಾದ', 'ಭಾಷೆಗಳಲ್ಲಿ', 'ಒಂದೂ', 'ಆಗಿರುವ', 'ಕನ್ನಡ', 'ಭಾಷೆಯನ್ನು', 'ಅದರ', 'ವಿವಿಧ', 'ರೂಪಗಳಲ್ಲಿ', 'ಸುಮಾರು', '೪೫', 'ದಶಲಕ್ಷ', 'ಜನರು', 'ಆಡು', 'ನುಡಿಯಾಗಿ', 'ಬಳಸುತ್ತಲಿದ್ದಾರೆ', '.']
    elif lang == 'kir':
        assert tokens == ['Кыргыз', 'тили', '—', 'Кыргыз', 'Республикасынын', 'мамлекеттик', 'тили', ',', 'түрк', 'тилдеринин', 'курамына', ',', 'анын', 'ичинде', 'кыргыз-кыпчак', 'тобуна', 'кирет', '.']
    elif lang == 'lav':
        if word_tokenizer == 'Sacremoses - Moses Tokenizer':
            assert tokens == ['Latviešu', 'valoda', 'ir', 'dzimtā', 'valoda', 'apmēram', '1,7', 'miljoniem', 'cilvēku', ',', 'galvenokārt', 'Latvijā', ',', 'kur', 'tā', 'ir', 'vienīgā', 'valsts', 'valoda', '.', '[', '3', ']']
        elif word_tokenizer == 'spaCy - Latvian Word Tokenizer':
            assert tokens == ['Latviešu', 'valoda', 'ir', 'dzimtā', 'valoda', 'apmēram', '1,7', 'miljoniem', 'cilvēku', ',', 'galvenokārt', 'Latvijā', ',', 'kur', 'tā', 'ir', 'vienīgā', 'valsts', 'valoda.[3', ']']
    elif lang == 'lij':
        assert tokens == ['O', 'Lìgure', '(', 'in', 'monegasco', ':', 'lenga', 'ligüra', 'e', 'lenga', 'lìgura', ')', 'o', "l'", 'é', "'", 'na', 'lengoa[1', ']', 'do', 'gruppo', 'lengoìstego', 'itàlico', 'oçidentâ', 'parlâ', 'in', 'Italia', '(', 'Liguria', ',', 'Piemonte', ',', 'Emilia', '-', 'Romagna', 'e', 'Sardegna', ')', ',', 'into', 'sud', 'da', 'Fransa', ',', 'in', 'Còrsega', ',', 'e', 'into', 'Prinçipato', 'de', 'Monego', '.']
    elif lang == 'lit':
        assert tokens == ['Lietuvių', 'kalba', '–', 'iš', 'baltų', 'prokalbės', 'kilusi', 'lietuvių', 'tautos', 'kalba', ',', 'kuri', 'Lietuvoje', 'yra', 'valstybinė', ',', 'o', 'Europos', 'Sąjungoje', '–', 'viena', 'iš', 'oficialiųjų', 'kalbų', '.']
    elif lang == 'ltz':
        assert tokens == ["D'", 'Lëtzebuergesch', 'gëtt', 'an', 'der', 'däitscher', 'Dialektologie', 'als', 'ee', 'westgermaneschen', ',', 'mëtteldäitschen', 'Dialekt', 'aklasséiert', ',', 'deen', 'zum', 'Muselfränkesche', 'gehéiert', '.']
    elif lang == 'mkd':
        assert tokens == ['Македонски', 'јазик', '—', 'јужнословенски', 'јазик', ',', 'дел', 'од', 'групата', 'на', 'словенски', 'јазици', 'од', 'јазичното', 'семејство', 'на', 'индоевропски', 'јазици', '.']
    elif lang == 'mal':
        if word_tokenizer == 'Sacremoses - Moses Tokenizer':
            assert tokens == ['ഇന്ത്യയിൽ', 'പ്രധാനമായും', 'കേരള', 'സംസ്ഥാനത്തിലും', 'ലക്ഷദ്വീപിലും', 'പുതുച്ചേരിയുടെ', 'ഭാഗമായ', 'മയ്യഴിയിലും', 'സംസാരിക്കപ്പെടുന്ന', 'ഭാഷയാണ്', 'മലയാളം', '.']
        elif word_tokenizer == 'spaCy - Malayalam Word Tokenizer':
            assert tokens == ['ഇന്ത്യയിൽ', 'പ്രധാനമായും', 'കേരള', 'സംസ്ഥാനത്തിലും', 'ലക്ഷദ്വീപിലും', 'പുതുച്ചേരിയുടെ', 'ഭാഗമായ', 'മയ്യഴിയിലും', 'സംസാരിക്കപ്പെടുന്ന', 'ഭാഷയാണ്', 'മലയാളം.']
    elif lang == 'mar':
        if word_tokenizer == 'Sacremoses - Moses Tokenizer':
            assert tokens == ['मराठीभाषा', 'ही', 'इंडो-युरोपीय', 'भाषाकुलातील', 'एक', 'भाषा', 'आहे', '.']
        elif word_tokenizer == 'spaCy - Marathi Word Tokenizer':
            assert tokens == ['मराठीभाषा', 'ही', 'इंडो', '-', 'युरोपीय', 'भाषाकुलातील', 'एक', 'भाषा', 'आहे', '.']
    elif lang == 'mni':
        assert tokens == ['ꯃꯤꯇꯩꯂꯣꯟ', 'ꯍꯥꯏꯕꯁꯤ', 'ꯏꯟꯗꯤꯌꯥ', 'ꯑꯋꯥꯡ-ꯅꯣꯡꯄꯣꯛꯇ', 'ꯂꯩꯕ', 'ꯃꯅꯤꯄꯨꯔꯗ', 'ꯃꯔꯨꯑꯣꯏꯅ', 'ꯉꯥꯡꯅꯕ', 'ꯇꯤꯕꯦꯇꯣ-ꯕꯔꯃꯟ', 'ꯀꯥꯡꯂꯨꯞꯇ', 'ꯆꯤꯡꯕ', 'ꯂꯣꯟ', 'ꯑꯃꯅꯤ', '꯫', 'ꯚꯥꯔꯠ', 'ꯂꯩꯉꯥꯛꯅꯥ', 'ꯁꯛꯈꯪꯂꯕ', 'ꯂꯣꯟ', '꯲꯲', 'ꯁꯤꯡꯒꯤ', 'ꯃꯅꯨꯡꯗ', 'ꯃꯤꯇꯩꯂꯣꯟꯁꯤꯁꯨ', 'ꯑꯃꯅꯤ', '꯫', 'ꯃꯤꯇꯩꯂꯣꯟ', 'ꯑꯁꯤ', 'ꯏꯟꯗꯤꯌꯥꯒꯤ', 'ꯁ', '꯭', 'ꯇꯦꯠ', 'ꯑꯣꯏꯔꯤꯕ', 'ꯑꯁꯥꯝ', 'ꯑꯃꯁꯨꯡ', 'ꯇ', '꯭', 'ꯔꯤꯄꯨꯔꯥ', 'ꯑꯃꯗꯤ', 'ꯑꯇꯩ', 'ꯂꯩꯕꯥꯛꯁꯤꯡꯗ', 'ꯍꯥꯏꯕꯗꯤ', 'ꯕꯥꯡꯂꯥꯗꯦꯁ', 'ꯑꯃꯁꯨꯡ', 'ꯑꯋꯥꯗꯁꯨ', 'ꯉꯥꯡꯅꯩ', '꯫', 'ꯏꯪ', 'ꯀꯨꯝꯖ', '꯲꯰꯱꯱', 'ꯒꯤ', 'ꯃꯤꯀꯣꯛ', 'ꯊꯤꯕꯗ', 'ꯃꯤꯇꯩꯂꯣꯟꯕꯨ', 'ꯏꯃꯥꯂꯣꯟ', 'ꯑꯣꯢꯅ', 'ꯉꯥꯡꯕꯒꯤ', 'ꯃꯤꯁꯤꯡ', 'ꯂꯤꯆꯥ', '꯱꯸', 'ꯃꯨꯛ', 'ꯁꯨꯢ', '꯫']
    elif lang == 'nep':
        assert tokens == ['नेपाली', 'भाषा', '(', 'अन्तर्राष्ट्रिय', 'ध्वन्यात्मक', 'वर्णमाला', '[', 'neˈpali', 'bʱaʂa', ']', ')', 'नेपालको', 'सम्पर्क', 'भाषा', 'तथा', 'भारत', ',', 'भुटान', 'र', 'म्यानमारको', 'केही', 'भागमा', 'मातृभाषाको', 'रूपमा', 'बोलिने', 'भाषा', 'हो', '।']
    elif lang == 'nob':
        assert tokens == ['Bokmål', 'er', 'en', 'varietet', 'av', 'norsk', 'språk', '.']
    elif lang == 'ori':
        assert tokens == ['ଓଡ଼ିଆ', '(', 'ଇଂରାଜୀ', 'ଭାଷାରେ', 'Odia', '/', 'əˈdiːə', '/', 'or', 'Oriya', '/', 'ɒˈriːə', '/', ',', ')', 'ଏକ', 'ଭାରତୀୟ', 'ଭାଷା', 'ଯାହା', 'ଏକ', 'ଇଣ୍ଡୋ-ଇଉରୋପୀୟ', 'ଭାଷାଗୋଷ୍ଠୀ', 'ଅନ୍ତର୍ଗତ', 'ଇଣ୍ଡୋ-ଆର୍ଯ୍ୟ', 'ଭାଷା', '।']
    elif lang == 'fas':
        if word_tokenizer == 'NLTK - Tok-tok Tokenizer':
            assert tokens == ['فارسی', 'یا', 'پارسی', 'یکی', 'از', 'زبان\u200cهای', 'هندواروپایی', 'در', 'شاخهٔ', 'زبان\u200cهای', 'ایرانی', 'جنوب', 'غربی', 'است', 'که', 'در', 'کشورهای', 'ایران', '،', 'افغانستان', '،', '[', '۳', ']', 'تاجیکستان[', '۴', ']', 'و', 'ازبکستان[', '۵', ']', 'به', 'آن', 'سخن', 'می\u200cگویند', '.']
        elif word_tokenizer == 'spaCy - Persian Word Tokenizer':
            assert tokens == ['فارسی', 'یا', 'پارسی', 'یکی', 'از', 'زبان\u200cهای', 'هندواروپایی', 'در', 'شاخهٔ', 'زبان\u200cهای', 'ایرانی', 'جنوب', 'غربی', 'است', 'که', 'در', 'کشورهای', 'ایران', '،', 'افغانستان،[۳', ']', 'تاجیکستان[۴', ']', 'و', 'ازبکستان[۵', ']', 'به', 'آن', 'سخن', 'می\u200cگویند', '.']
    elif lang == 'pol':
        assert tokens == ['Język', 'polski', ',', 'polszczyzna', '–', 'język', 'lechicki', 'z', 'grupy', 'zachodniosłowiańskiej', '(', 'do', 'której', 'należą', 'również', 'czeski', ',', 'kaszubski', ',', 'słowacki', 'i', 'języki', 'łużyckie', ')', ',', 'stanowiącej', 'część', 'rodziny', 'indoeuropejskiej', '.']
    elif lang == 'por':
        assert tokens == ['A', 'língua', 'portuguesa', ',', 'também', 'designada', 'português', ',', 'é', 'uma', 'língua', 'românica', 'flexiva', 'ocidental', 'originada', 'no', 'galego-português', 'falado', 'no', 'Reino', 'da', 'Galiza', 'e', 'no', 'norte', 'de', 'Portugal', '.']
    elif lang == 'pan':
        assert tokens == ['ਪੰਜਾਬੀ', 'ਭਾਸ਼ਾ', '/', 'pʌnˈdʒɑːbi', '/', '(', 'ਸ਼ਾਹਮੁਖੀ', ':', '\u200e', 'پنجابی', '\u200e', ')', '(', 'ਗੁਰਮੁਖੀ', ':', 'ਪੰਜਾਬੀ', ')', 'ਪੰਜਾਬ', 'ਦੀ', 'ਭਾਸ਼ਾ', ',', 'ਜਿਸ', 'ਨੂੰ', 'ਪੰਜਾਬ', 'ਖੇਤਰ', 'ਦੇ', 'ਵਸਨੀਕ', 'ਜਾਂ', 'ਸੰਬੰਧਿਤ', 'ਲੋਕ', 'ਬੋਲਦੇ', 'ਹਨ', '।', '[', '1', ']']
    elif lang == 'ron':
        assert tokens == ['Limba', 'română', 'este', 'o', 'limbă', 'indo-europeană', ',', 'din', 'grupul', 'italic', 'și', 'din', 'subgrupul', 'oriental', 'al', 'limbilor', 'romanice', '.']
    elif lang == 'rus':
        if word_tokenizer in ['NLTK - Tok-tok Tokenizer',
                              'razdel - Russian Word Tokenizer']:
            assert tokens == ['Ру́сский', 'язы́к', '(', '[', 'ˈruskʲɪi̯', 'jɪˈzɨk', ']', 'Информация', 'о', 'файле', 'слушать', ')', '[', '~', '3', ']', '[', '⇨', ']', '—', 'один', 'из', 'восточнославянских', 'языков', ',', 'национальный', 'язык', 'русского', 'народа', '.']
        elif word_tokenizer == 'Sacremoses - Moses Tokenizer':
            assert tokens == ['Ру', '́', 'сский', 'язы', '́', 'к', '(', '[', 'ˈruskʲɪi', '̯', 'jɪˈzɨk', ']', 'Информация', 'о', 'файле', 'слушать', ')', '[', '~', '3', ']', '[', '⇨', ']', '—', 'один', 'из', 'восточнославянских', 'языков', ',', 'национальный', 'язык', 'русского', 'народа', '.']
        elif word_tokenizer == 'spaCy - Russian Word Tokenizer':
            assert tokens == ['Ру́сский', 'язы́к', '(', '[', 'ˈruskʲɪi̯', 'jɪˈzɨk', ']', 'Информация', 'о', 'файле', 'слушать)[~', '3', ']', '[', '⇨', ']', '—', 'один', 'из', 'восточнославянских', 'языков', ',', 'национальный', 'язык', 'русского', 'народа', '.']
    elif lang == 'san':
        assert tokens == ['संस्कृतम्', '(', 'IPA', ':', '[', 'ˈsɐ̃skr̩tɐm', ']', '(', 'शृणु', ')', ')', 'जगतः', 'एकतमा', 'अतिप्राचीना', 'समृद्धा', 'शास्त्रीया', 'च', 'भाषा', 'वर्तते', '।']
    elif lang == 'srp_cyrl':
        assert tokens == ['Српски', 'језик', 'припада', 'словенској', 'групи', 'језика', 'породице', 'индоевропских', 'језика.[12', ']']
    elif lang == 'srp_latn':
        assert tokens == ['Srpski', 'jezik', 'pripada', 'slovenskoj', 'grupi', 'jezika', 'porodice', 'indoevropskih', 'jezika.[12', ']']
    elif lang == 'sin':
        assert tokens == ['ශ්\u200dරී', 'ලංකාවේ', 'ප්\u200dරධාන', 'ජාතිය', 'වන', 'සිංහල', 'ජනයාගේ', 'මව්', 'බස', 'සිංහල', 'වෙයි', '.']
    elif lang == 'slk':
        assert tokens == ['Slovenčina', 'patrí', 'do', 'skupiny', 'západoslovanských', 'jazykov', '(', 'spolu', 's', 'češtinou', ',', 'poľštinou', ',', 'hornou', 'a', 'dolnou', 'lužickou', 'srbčinou', 'a', 'kašubčinou', ')', '.']
    elif lang == 'slv':
        assert tokens == ['Slovenščina', '[', 'slovénščina', ']', '/', '[', 'sloˈʋenʃtʃina', ']', 'je', 'združeni', 'naziv', 'za', 'uradni', 'knjižni', 'jezik', 'Slovencev', 'in', 'skupno', 'ime', 'za', 'narečja', 'in', 'govore', ',', 'ki', 'jih', 'govorijo', 'ali', 'so', 'jih', 'nekoč', 'govorili', 'Slovenci', '.']
    elif lang == 'spa':
        assert tokens == ['El', 'español', 'o', 'castellano', 'es', 'una', 'lengua', 'romance', 'procedente', 'del', 'latín', 'hablado', '.']
    elif lang == 'swe':
        assert tokens == ['Svenska', '(', 'svenska', '(', 'info', ')', ')', 'är', 'ett', 'östnordiskt', 'språk', 'som', 'talas', 'av', 'ungefär', 'tio', 'miljoner', 'personer', 'främst', 'i', 'Sverige', 'där', 'språket', 'har', 'en', 'dominant', 'ställning', 'som', 'huvudspråk', ',', 'men', 'även', 'som', 'det', 'ena', 'nationalspråket', 'i', 'Finland', 'och', 'som', 'enda', 'officiella', 'språk', 'på', 'Åland', '.']
    elif lang == 'tgl':
        assert tokens == ['Ang', 'Wikang', 'Tagalog[2', ']', '(', 'Baybayin', ':', 'ᜏᜒᜃᜅ᜔', 'ᜆᜄᜎᜓᜄ᜔', ')', ',', 'na', 'kilala', 'rin', 'sa', 'payak', 'na', 'pangalang', 'Tagalog', ',', 'ay', 'isa', 'sa', 'mga', 'pangunahing', 'wika', 'ng', 'Pilipinas', 'at', 'sinasabing', 'ito', 'ang', 'de', 'facto', '(', '"', 'sa', 'katunayan', '"', ')', 'ngunit', 'hindî', 'de', 'jure', '(', '"', 'sa', 'batas', '"', ')', 'na', 'batayan', 'na', 'siyang', 'pambansang', 'Wikang', 'Filipino', '(', 'mula', '1961', 'hanggang', '1987', ':', 'Pilipino).[2', ']']
    elif lang == 'tgk':
        assert tokens == ['Забони', 'тоҷикӣ', '—', 'забоне', ',', 'ки', 'дар', 'Эрон', ':', 'форсӣ', ',', 'ва', 'дар', 'Афғонистон', 'дарӣ', 'номида', 'мешавад', ',', 'забони', 'давлатии', 'кишварҳои', 'Тоҷикистон', ',', 'Эрон', 'ва', 'Афғонистон', 'мебошад', '.']
    elif lang == 'tam':
        assert tokens == ['தமிழ்', 'மொழி', '(', 'Tamil', 'language', ')', 'தமிழர்களினதும்', ',', 'தமிழ்', 'பேசும்', 'பலரதும்', 'தாய்மொழி', 'ஆகும்', '.']
    elif lang == 'tat':
        assert tokens == ['Татар', 'теле', '—', 'татарларның', 'милли', 'теле', ',', 'Татарстанның', 'дәүләт', 'теле', ',', 'таралышы', 'буенча', 'Русиядә', 'икенче', 'тел', '.']
    elif lang == 'tel':
        tokens == ['ఆంధ్ర', 'ప్రదేశ్', ',', 'తెలంగాణ', 'రాష్ట్రాల', 'అధికార', 'భాష', 'తెలుగు', '.']
    elif lang == 'tdt':
        tokens == ['Tetun', '(', 'iha', 'portugés', ':', 'tétum', ';', 'iha', 'inglés', ':', 'Tetum', ')', 'ne', "'", 'e', 'lian', 'nasionál', 'no', 'ko-ofisiál', 'Timór', 'Lorosa', "'", 'e', 'nian', '.']
    elif lang == 'tha':
        if word_tokenizer in ['PyThaiNLP - Longest Matching',
                              'PyThaiNLP - Maximum Matching + TCC',
                              'PyThaiNLP - Maximum Matching + TCC (Safe Mode)',
                              'PyThaiNLP - NERCut']:
            assert tokens == ['ภาษาไทย', 'หรือ', 'ภาษาไทย', 'กลาง', 'เป็น', 'ภาษาราชการ', 'และ', 'ภาษาประจำชาติ', 'ของ', 'ประเทศ', 'ไทย']
        elif word_tokenizer == 'PyThaiNLP - Maximum Matching':
            assert tokens == ['ภาษาไทย', 'หรือ', 'ภาษาไทยกลาง', 'เป็น', 'ภาษาราชการ', 'และ', 'ภาษาประจำชาติ', 'ของ', 'ประเทศ', 'ไทย']
    elif lang == 'bod':
        assert tokens == ['བོད་', 'ཀྱི་', 'སྐད་ཡིག་', 'ནི་', 'བོད་ཡུལ་', 'དང་', 'དེ', 'འི་', 'ཉེ་འཁོར་', 'གྱི་', 'ས་ཁུལ་', 'ཏེ', '།']
    elif lang == 'tir':
        assert tokens ==['ትግርኛ', 'ኣብ', 'ኤርትራን', 'ኣብ', 'ሰሜናዊ', 'ኢትዮጵያን', 'ኣብ', 'ክልል', 'ትግራይ', 'ዝዝረብ', 'ሴማዊ', 'ቋንቋ', 'እዩ', '።']
    elif lang == 'tsn':
        assert tokens == ['Setswana', 'ke', 'teme', 'e', 'e', 'buiwang', 'mo', 'mafatsheng', 'a', 'Aforika', 'Borwa', ',', 'Botswana', ',', 'Namibia', 'le', 'Zimbabwe', '.']
    elif lang == 'tur':
        assert tokens == ['Türkçe', 'ya', 'da', 'Türk', 'dili', ',', 'batıda', 'Balkanlar’dan', 'başlayıp', 'doğuda', 'Hazar', 'Denizi', 'sahasına', 'kadar', 'konuşulan', 'Türkî', 'diller', 'dil', 'ailesine', 'ait', 'sondan', 'eklemeli', 'bir', 'dil.[12', ']']
    elif lang == 'ukr':
        assert tokens == ['Украї́нська', 'мо́ва', '(', 'МФА', ':', '[', 'ukrɑ̽ˈjɪnʲsʲkɑ̽', 'ˈmɔwɑ̽', ']', ',', 'історичні', 'назви', '—', 'ру́ська', ',', 'руси́нська[9][10][11', ']', '[', '*', '2', ']', ')', '—', 'національна', 'мова', 'українців', '.']
    elif lang == 'urd':
        assert tokens == ['اُردُو', 'لشکری', 'زبان[8', ']', '(', 'یا', 'جدید', 'معیاری', 'اردو', ')', 'برصغیر', 'کی', 'معیاری', 'زبانوں', 'میں', 'سے', 'ایک', 'ہے', '۔']
    elif lang == 'vie':
        if word_tokenizer == 'NLTK - Tok-tok Tokenizer':
            assert tokens == ['Tiếng', 'Việt', ',', 'còn', 'gọi', 'tiếng', 'Việt', 'Nam[', '5', ']', ',', 'tiếng', 'Kinh', 'hay', 'Việt', 'ngữ', ',', 'là', 'ngôn', 'ngữ', 'của', 'người', 'Việt', '(', 'dân', 'tộc', 'Kinh', ')', 'và', 'là', 'ngôn', 'ngữ', 'chính', 'thức', 'tại', 'Việt', 'Nam', '.']
        elif word_tokenizer == 'Underthesea - Vietnamese Word Tokenizer':
            assert tokens == ['Tiếng', 'Việt', ',', 'còn', 'gọi', 'tiếng', 'Việt Nam', '[', '5', ']', ',', 'tiếng Kinh', 'hay', 'Việt ngữ', ',', 'là', 'ngôn ngữ', 'của', 'người', 'Việt', '(', 'dân tộc', 'Kinh', ')', 'và', 'là', 'ngôn ngữ', 'chính thức', 'tại', 'Việt Nam', '.']
    elif lang == 'yor':
        assert tokens == ['Èdè', 'Yorùbá', 'Ni', 'èdè', 'tí', 'ó', 'ṣàkójọ', 'pọ̀', 'gbogbo', 'kú', 'oótu', 'o', '-', 'ò', '-', 'jíire', 'bí', ',', 'níapá', 'ìwọ̀', 'Oòrùn', 'ilẹ̀', 'Nàìjíríà', ',', 'tí', 'a', 'bá', 'wo', 'èdè', 'Yorùbá', ',', 'àwọn', 'onímọ̀', 'pín', 'èdè', 'náà', 'sábẹ́', 'ẹ̀yà', 'Kwa', 'nínú', 'ẹbí', 'èdè', 'Niger', '-', 'Congo', '.']
    else:
        raise Exception(f'Warning: language code "{lang}" is absent from the list!')

if __name__ == '__main__':
    for lang, word_tokenizer in test_word_tokenizers:
        test_word_tokenize(lang, word_tokenizer, show_results = True)
