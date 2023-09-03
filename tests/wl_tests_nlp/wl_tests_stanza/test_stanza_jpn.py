# ----------------------------------------------------------------------
# Wordless: Tests - NLP - Stanza - Japanese
# Copyright (C) 2018-2023  Ye Lei (叶磊)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

from tests.wl_tests_nlp.wl_tests_stanza import test_stanza

def test_stanza_jpn():
    test_stanza.wl_test_stanza(
        lang = 'jpn',
        results_sentence_tokenize = ['日本語（にほんご、にっぽんご[注釈 2]、英語: Japanese language）は、日本国内や、かつての日本領だった国、そして国外移民や移住者を含む日本人同士の間で使用されている言語。', '日本は法令によって公用語を規定していないが、法令その他の公用文は全て日本語で記述され、各種法令[注釈 3]において日本語を用いることが規定され、学校教育においては「国語」の教科として学習を行うなど、事実上日本国内において唯一の公用語となっている。'],
        results_word_tokenize = ['日本', '語（', 'に', 'ほんご', '、', 'にっぽん', 'ご[', '注釈', '2', ']', '、', '英語', ':', 'Japanese', 'language）', 'は', '、', '日本', '国内', 'や', '、', 'かつて', 'の', '日本', '領', 'だっ', 'た', '国', '、', 'そして', '国外', '移民', 'や', '移住', '者', 'を', '含む', '日本', '人', '同士', 'の', '間', 'で', '使用', 'さ', 'れ', 'て', 'いる', '言語', '。'],
        results_pos_tag = [('日本', '名詞-固有名詞-地名-国'), ('語（', '名詞-普通名詞-一般'), ('に', '助詞-格助詞'), ('ほんご', '名詞-普通名詞-一般'), ('、', '補助記号-読点'), ('にっぽん', '名詞-固有名詞-地名-一般'), ('ご[', '名詞-普通名詞-一般'), ('注釈', '名詞-普通名詞-サ変可能'), ('2', '名詞-数詞'), (']', '補助記号-括弧閉'), ('、', '補助記号-読点'), ('英語', '名詞-普通名詞-一般'), (':', '補助記号-一般'), ('Japanese', '名詞-普通名詞-一般'), ('language）', '名詞-普通名詞-一般'), ('は', '助詞-係助詞'), ('、', '補助記号-読点'), ('日本', '名詞-固有名詞-地名-国'), ('国内', '名詞-普通名詞-一般'), ('や', '助詞-副助詞'), ('、', '補助記号-読点'), ('かつて', '副詞'), ('の', '助詞-格助詞'), ('日本', '名詞-固有名詞-地名-国'), ('領', '接尾辞-名詞的-一般'), ('だっ', '助動詞-助動詞-ダ'), ('た', '助動詞-助動詞-タ'), ('国', '名詞-普通名詞-一般'), ('、', '補助記号-読点'), ('そして', '接続詞'), ('国外', '名詞-普通名詞-一般'), ('移民', '名詞-普通名詞-サ変可能'), ('や', '助詞-副助詞'), ('移住', '名詞-普通名詞-サ変可能'), ('者', '接尾辞-名詞的-一般'), ('を', '助詞-格助詞'), ('含む', '動詞-一般-五段-マ行'), ('日本', '名詞-固有名詞-地名-国'), ('人', '接尾辞-名詞的-一般'), ('同士', '接尾辞-名詞的-一般'), ('の', '助詞-格助詞'), ('間', '名詞-普通名詞-副詞可能'), ('で', '助詞-格助詞'), ('使用', '名詞-普通名詞-サ変可能'), ('さ', '動詞-非自立可能-サ行変格'), ('れ', '助動詞-助動詞-レル'), ('て', '助詞-接続助詞'), ('いる', '動詞-非自立可能-上一段-ア行'), ('言語', '名詞-普通名詞-一般'), ('。', '補助記号-句点')],
        results_pos_tag_universal = [('日本', 'PROPN'), ('語（', 'NOUN'), ('に', 'ADP'), ('ほんご', 'NOUN'), ('、', 'PUNCT'), ('にっぽん', 'PROPN'), ('ご[', 'NOUN'), ('注釈', 'NOUN'), ('2', 'NUM'), (']', 'PUNCT'), ('、', 'PUNCT'), ('英語', 'NOUN'), (':', 'SYM'), ('Japanese', 'NOUN'), ('language）', 'NOUN'), ('は', 'ADP'), ('、', 'PUNCT'), ('日本', 'PROPN'), ('国内', 'NOUN'), ('や', 'ADP'), ('、', 'PUNCT'), ('かつて', 'ADV'), ('の', 'ADP'), ('日本', 'PROPN'), ('領', 'NOUN'), ('だっ', 'AUX'), ('た', 'AUX'), ('国', 'NOUN'), ('、', 'PUNCT'), ('そして', 'CCONJ'), ('国外', 'NOUN'), ('移民', 'NOUN'), ('や', 'ADP'), ('移住', 'NOUN'), ('者', 'NOUN'), ('を', 'ADP'), ('含む', 'VERB'), ('日本', 'PROPN'), ('人', 'NOUN'), ('同士', 'NOUN'), ('の', 'ADP'), ('間', 'NOUN'), ('で', 'ADP'), ('使用', 'VERB'), ('さ', 'AUX'), ('れ', 'AUX'), ('て', 'SCONJ'), ('いる', 'VERB'), ('言語', 'NOUN'), ('。', 'PUNCT')],
        results_lemmatize = ['日本', '語（', 'に', 'ほんご', '、', 'にっぽん', 'ご[', '注釈', '2', ']', '、', '英語', ':', 'Japanese', 'language）', 'は', '、', '日本', '国内', 'や', '、', 'かつて', 'の', '日本', '領', 'だ', 'た', '国', '、', 'そして', '国外', '移民', 'や', '移住', '者', 'を', '含む', '日本', '人', '同士', 'の', '間', 'で', '使用', 'する', 'れる', 'て', 'いる', '言語', '。'],
        results_dependency_parse = [('日本', '語（', 'compound', 1), ('語（', '2', 'obl', 7), ('に', '語（', 'case', -1), ('ほんご', '2', 'nmod', 5), ('、', 'ほんご', 'punct', -1), ('にっぽん', '2', 'compound', 3), ('ご[', '2', 'compound', 2), ('注釈', '2', 'compound', 1), ('2', 'language）', 'compound', 6), (']', '2', 'punct', -1), ('、', '2', 'punct', -2), ('英語', 'language）', 'compound', 3), (':', 'language）', 'compound', 2), ('Japanese', 'language）', 'compound', 1), ('language）', '言語', 'nsubj', 34), ('は', 'language）', 'case', -1), ('、', 'language）', 'punct', -2), ('日本', '国内', 'compound', 1), ('国内', '国', 'nmod', 9), ('や', '国内', 'case', -1), ('、', '国内', 'punct', -2), ('かつて', '領', 'advmod', 3), ('の', 'かつて', 'case', -1), ('日本', '領', 'compound', 1), ('領', '国', 'acl', 3), ('だっ', '領', 'cop', -1), ('た', '領', 'aux', -2), ('国', '者', 'nmod', 7), ('、', '国', 'punct', -1), ('そして', '者', 'cc', 5), ('国外', '移民', 'compound', 1), ('移民', '者', 'nmod', 3), ('や', '移民', 'case', -1), ('移住', '者', 'compound', 1), ('者', '含む', 'obj', 2), ('を', '者', 'case', -1), ('含む', '同士', 'acl', 3), ('日本', '同士', 'compound', 2), ('人', '同士', 'compound', 1), ('同士', '間', 'nmod', 2), ('の', '同士', 'case', -1), ('間', '使用', 'obl', 2), ('で', '間', 'case', -1), ('使用', '言語', 'acl', 5), ('さ', '使用', 'aux', -1), ('れ', '使用', 'aux', -2), ('て', '使用', 'mark', -3), ('いる', 'て', 'fixed', -1), ('言語', '言語', 'root', 0), ('。', '言語', 'punct', -1)]
    )

if __name__ == '__main__':
    test_stanza_jpn()
