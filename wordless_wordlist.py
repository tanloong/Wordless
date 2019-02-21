#
# Wordless: Wordlist
#
# Copyright (C) 2018-2019  Ye Lei (叶磊))
#
# This source file is licensed under GNU GPLv3.
# For details, see: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#
# All other rights reserved.
#

import collections
import copy

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy

from wordless_checking import *
from wordless_dialogs import *
from wordless_measures import *
from wordless_plot import *
from wordless_text import *
from wordless_utils import *
from wordless_widgets import *

class Wordless_Table_Wordlist(wordless_table.Wordless_Table_Data_Filter_Search):
    def __init__(self, parent):
        super().__init__(parent,
                         headers = [
                             parent.tr('Rank'),
                             parent.tr('Tokens'),
                             parent.tr('Number of\nFiles Found')
                         ],
                         headers_num = [
                             parent.tr('Rank'),
                             parent.tr('Number of\nFiles Found')
                         ],
                         headers_pct = [
                             parent.tr('Number of\nFiles Found')
                         ],
                         sorting_enabled = True)

        dialog_filter_results = wordless_dialog_filter_results.Wordless_Dialog_Filter_Results_Wordlist(
            self.main,
            tab = 'wordlist',
            table = self
        )
        dialog_search_results = wordless_dialog_search_results.Wordless_Dialog_Search_Results(
            self.main,
            tab = 'wordlist',
            table = self
        )

        self.button_filter_results.clicked.connect(dialog_filter_results.load)
        self.button_search_results.clicked.connect(dialog_search_results.load)

        self.button_generate_table = QPushButton(self.tr('Generate Table'), self)
        self.button_generate_plot = QPushButton(self.tr('Generate Plot'), self)

        self.button_generate_table.clicked.connect(lambda: generate_table(self.main, self))
        self.button_generate_plot.clicked.connect(lambda: generate_plot(self.main))

class Wrapper_Wordlist(wordless_layout.Wordless_Wrapper):
    def __init__(self, main):
        super().__init__(main)

        # Table
        self.table_wordlist = Wordless_Table_Wordlist(self)

        layout_results = QGridLayout()
        layout_results.addWidget(self.table_wordlist.label_number_results, 0, 0)
        layout_results.addWidget(self.table_wordlist.button_filter_results, 0, 2)
        layout_results.addWidget(self.table_wordlist.button_search_results, 0, 3)

        layout_results.setColumnStretch(1, 1)

        self.wrapper_table.layout().addLayout(layout_results, 0, 0, 1, 5)
        self.wrapper_table.layout().addWidget(self.table_wordlist, 1, 0, 1, 5)
        self.wrapper_table.layout().addWidget(self.table_wordlist.button_generate_table, 2, 0)
        self.wrapper_table.layout().addWidget(self.table_wordlist.button_generate_plot, 2, 1)
        self.wrapper_table.layout().addWidget(self.table_wordlist.button_export_selected, 2, 2)
        self.wrapper_table.layout().addWidget(self.table_wordlist.button_export_all, 2, 3)
        self.wrapper_table.layout().addWidget(self.table_wordlist.button_clear, 2, 4)

        # Token Settings
        self.group_box_token_settings = QGroupBox(self.tr('Token Settings'), self)

        (self.checkbox_words,
         self.checkbox_lowercase,
         self.checkbox_uppercase,
         self.checkbox_title_case,
         self.checkbox_nums,
         self.checkbox_puncs,

         self.checkbox_treat_as_lowercase,
         self.checkbox_lemmatize_tokens,
         self.checkbox_filter_stop_words,

         self.stacked_widget_ignore_tags,
         self.stacked_widget_ignore_tags_tags,
         self.label_ignore_tags,
         self.checkbox_use_tags) = wordless_widgets.wordless_widgets_token_settings(self)

        self.checkbox_words.stateChanged.connect(self.token_settings_changed)
        self.checkbox_lowercase.stateChanged.connect(self.token_settings_changed)
        self.checkbox_uppercase.stateChanged.connect(self.token_settings_changed)
        self.checkbox_title_case.stateChanged.connect(self.token_settings_changed)
        self.checkbox_nums.stateChanged.connect(self.token_settings_changed)
        self.checkbox_puncs.stateChanged.connect(self.token_settings_changed)

        self.checkbox_treat_as_lowercase.stateChanged.connect(self.token_settings_changed)
        self.checkbox_lemmatize_tokens.stateChanged.connect(self.token_settings_changed)
        self.checkbox_filter_stop_words.stateChanged.connect(self.token_settings_changed)

        self.stacked_widget_ignore_tags.checkbox_ignore_tags.stateChanged.connect(self.token_settings_changed)
        self.stacked_widget_ignore_tags.checkbox_ignore_tags_tags.stateChanged.connect(self.token_settings_changed)
        self.stacked_widget_ignore_tags_tags.combo_box_ignore_tags.currentTextChanged.connect(self.token_settings_changed)
        self.stacked_widget_ignore_tags_tags.combo_box_ignore_tags_tags.currentTextChanged.connect(self.token_settings_changed)
        self.checkbox_use_tags.stateChanged.connect(self.token_settings_changed)

        layout_ignore_tags = QGridLayout()
        layout_ignore_tags.addWidget(self.stacked_widget_ignore_tags, 0, 0)
        layout_ignore_tags.addWidget(self.stacked_widget_ignore_tags_tags, 0, 1)
        layout_ignore_tags.addWidget(self.label_ignore_tags, 0, 2)

        layout_ignore_tags.setColumnStretch(3, 1)

        self.group_box_token_settings.setLayout(QGridLayout())
        self.group_box_token_settings.layout().addWidget(self.checkbox_words, 0, 0)
        self.group_box_token_settings.layout().addWidget(self.checkbox_lowercase, 0, 1)
        self.group_box_token_settings.layout().addWidget(self.checkbox_uppercase, 1, 0)
        self.group_box_token_settings.layout().addWidget(self.checkbox_title_case, 1, 1)
        self.group_box_token_settings.layout().addWidget(self.checkbox_nums, 2, 0)
        self.group_box_token_settings.layout().addWidget(self.checkbox_puncs, 2, 1)

        self.group_box_token_settings.layout().addWidget(wordless_layout.Wordless_Separator(self), 3, 0, 1, 2)

        self.group_box_token_settings.layout().addWidget(self.checkbox_treat_as_lowercase, 4, 0, 1, 2)
        self.group_box_token_settings.layout().addWidget(self.checkbox_lemmatize_tokens, 5, 0, 1, 2)
        self.group_box_token_settings.layout().addWidget(self.checkbox_filter_stop_words, 6, 0, 1, 2)

        self.group_box_token_settings.layout().addWidget(wordless_layout.Wordless_Separator(self), 7, 0, 1, 2)

        self.group_box_token_settings.layout().addLayout(layout_ignore_tags, 8, 0, 1, 2)
        self.group_box_token_settings.layout().addWidget(self.checkbox_use_tags, 9, 0, 1, 2)

        # Generation Settings
        self.group_box_generation_settings = QGroupBox(self.tr('Generation Settings'))

        (self.label_measure_dispersion,
         self.combo_box_measure_dispersion) = wordless_widgets.wordless_widgets_measure_dispersion(self)
        (self.label_measure_adjusted_freq,
         self.combo_box_measure_adjusted_freq) = wordless_widgets.wordless_widgets_measure_adjusted_freq(self)

        (self.label_settings_measures,
         self.button_settings_measures) = wordless_widgets.wordless_widgets_settings_measures(self,
                                                                                              tab = self.tr('Dispersion'))

        self.combo_box_measure_dispersion.currentTextChanged.connect(self.generation_settings_changed)
        self.combo_box_measure_adjusted_freq.currentTextChanged.connect(self.generation_settings_changed)

        layout_settings_measures = QGridLayout()
        layout_settings_measures.addWidget(self.label_settings_measures, 0, 0)
        layout_settings_measures.addWidget(self.button_settings_measures, 0, 1)

        layout_settings_measures.setColumnStretch(1, 1)

        self.group_box_generation_settings.setLayout(QGridLayout())
        self.group_box_generation_settings.layout().addWidget(self.label_measure_dispersion, 0, 0)
        self.group_box_generation_settings.layout().addWidget(self.combo_box_measure_dispersion, 1, 0)
        self.group_box_generation_settings.layout().addWidget(self.label_measure_adjusted_freq, 2, 0)
        self.group_box_generation_settings.layout().addWidget(self.combo_box_measure_adjusted_freq, 3, 0)

        self.group_box_generation_settings.layout().addWidget(wordless_layout.Wordless_Separator(self), 4, 0)

        self.group_box_generation_settings.layout().addLayout(layout_settings_measures, 5, 0)

        # Table Settings
        self.group_box_table_settings = QGroupBox(self.tr('Table Settings'))

        (self.checkbox_show_pct,
         self.checkbox_show_cumulative,
         self.checkbox_show_breakdown) = wordless_widgets.wordless_widgets_table_settings(self,
                                                                                          table = self.table_wordlist)

        self.checkbox_show_pct.stateChanged.connect(self.table_settings_changed)
        self.checkbox_show_cumulative.stateChanged.connect(self.table_settings_changed)
        self.checkbox_show_breakdown.stateChanged.connect(self.table_settings_changed)

        self.group_box_table_settings.setLayout(QGridLayout())
        self.group_box_table_settings.layout().addWidget(self.checkbox_show_pct, 0, 0)
        self.group_box_table_settings.layout().addWidget(self.checkbox_show_cumulative, 1, 0)
        self.group_box_table_settings.layout().addWidget(self.checkbox_show_breakdown, 2, 0)

        # Plot Settings
        self.group_box_plot_settings = QGroupBox(self.tr('Plot Settings'), self)

        (self.label_plot_type,
         self.combo_box_plot_type,
         self.label_use_file,
         self.combo_box_use_file,
         self.label_use_data,
         self.combo_box_use_data,

         self.checkbox_use_pct,
         self.checkbox_use_cumulative) = wordless_widgets.wordless_widgets_plot_settings(self)

        self.label_rank = QLabel(self.tr('Rank:'), self)
        (self.label_rank_min,
         self.spin_box_rank_min,
         self.checkbox_rank_min_no_limit,
         self.label_rank_max,
         self.spin_box_rank_max,
         self.checkbox_rank_max_no_limit) = wordless_widgets.wordless_widgets_filter(self,
                                                                                     filter_min = 1,
                                                                                     filter_max = 100000)

        self.combo_box_plot_type.currentTextChanged.connect(self.plot_settings_changed)
        self.combo_box_use_file.currentTextChanged.connect(self.plot_settings_changed)
        self.combo_box_use_data.currentTextChanged.connect(self.plot_settings_changed)
        self.checkbox_use_pct.stateChanged.connect(self.plot_settings_changed)
        self.checkbox_use_cumulative.stateChanged.connect(self.plot_settings_changed)

        self.spin_box_rank_min.valueChanged.connect(self.plot_settings_changed)
        self.checkbox_rank_min_no_limit.stateChanged.connect(self.plot_settings_changed)
        self.spin_box_rank_max.valueChanged.connect(self.plot_settings_changed)
        self.checkbox_rank_max_no_limit.stateChanged.connect(self.plot_settings_changed)

        layout_plot_settings_combo_boxes = QGridLayout()
        layout_plot_settings_combo_boxes.addWidget(self.label_plot_type, 0, 0)
        layout_plot_settings_combo_boxes.addWidget(self.combo_box_plot_type, 0, 1)
        layout_plot_settings_combo_boxes.addWidget(self.label_use_file, 1, 0)
        layout_plot_settings_combo_boxes.addWidget(self.combo_box_use_file, 1, 1)
        layout_plot_settings_combo_boxes.addWidget(self.label_use_data, 2, 0)
        layout_plot_settings_combo_boxes.addWidget(self.combo_box_use_data, 2, 1)

        layout_plot_settings_combo_boxes.setColumnStretch(1, 1)

        self.group_box_plot_settings.setLayout(QGridLayout())
        self.group_box_plot_settings.layout().addLayout(layout_plot_settings_combo_boxes, 0, 0, 1, 3)
        self.group_box_plot_settings.layout().addWidget(self.checkbox_use_pct, 1, 0, 1, 3)
        self.group_box_plot_settings.layout().addWidget(self.checkbox_use_cumulative, 2, 0, 1, 3)
        
        self.group_box_plot_settings.layout().addWidget(wordless_layout.Wordless_Separator(self), 3, 0, 1, 3)

        self.group_box_plot_settings.layout().addWidget(self.label_rank, 4, 0, 1, 3)
        self.group_box_plot_settings.layout().addWidget(self.label_rank_min, 5, 0)
        self.group_box_plot_settings.layout().addWidget(self.spin_box_rank_min, 5, 1)
        self.group_box_plot_settings.layout().addWidget(self.checkbox_rank_min_no_limit, 5, 2)
        self.group_box_plot_settings.layout().addWidget(self.label_rank_max, 6, 0)
        self.group_box_plot_settings.layout().addWidget(self.spin_box_rank_max, 6, 1)
        self.group_box_plot_settings.layout().addWidget(self.checkbox_rank_max_no_limit, 6, 2)

        self.group_box_plot_settings.layout().setColumnStretch(1, 1)

        self.wrapper_settings.layout().addWidget(self.group_box_token_settings, 0, 0)
        self.wrapper_settings.layout().addWidget(self.group_box_generation_settings, 1, 0)
        self.wrapper_settings.layout().addWidget(self.group_box_table_settings, 2, 0)
        self.wrapper_settings.layout().addWidget(self.group_box_plot_settings, 3, 0)

        self.wrapper_settings.layout().setRowStretch(4, 1)

        self.load_settings()

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.main.settings_default['wordlist'])
        else:
            settings = copy.deepcopy(self.main.settings_custom['wordlist'])

        # Token Settings
        self.checkbox_words.setChecked(settings['token_settings']['words'])
        self.checkbox_lowercase.setChecked(settings['token_settings']['lowercase'])
        self.checkbox_uppercase.setChecked(settings['token_settings']['uppercase'])
        self.checkbox_title_case.setChecked(settings['token_settings']['title_case'])
        self.checkbox_nums.setChecked(settings['token_settings']['nums'])
        self.checkbox_puncs.setChecked(settings['token_settings']['puncs'])

        self.checkbox_treat_as_lowercase.setChecked(settings['token_settings']['treat_as_lowercase'])
        self.checkbox_lemmatize_tokens.setChecked(settings['token_settings']['lemmatize_tokens'])
        self.checkbox_filter_stop_words.setChecked(settings['token_settings']['filter_stop_words'])

        self.stacked_widget_ignore_tags.checkbox_ignore_tags.setChecked(settings['token_settings']['ignore_tags'])
        self.stacked_widget_ignore_tags.checkbox_ignore_tags_tags.setChecked(settings['token_settings']['ignore_tags_tags'])
        self.stacked_widget_ignore_tags_tags.combo_box_ignore_tags.setCurrentText(settings['token_settings']['ignore_tags_type'])
        self.stacked_widget_ignore_tags_tags.combo_box_ignore_tags_tags.setCurrentText(settings['token_settings']['ignore_tags_type_tags'])
        self.checkbox_use_tags.setChecked(settings['token_settings']['use_tags'])

        # Generation Settings
        self.combo_box_measure_dispersion.setCurrentText(settings['generation_settings']['measure_dispersion'])
        self.combo_box_measure_adjusted_freq.setCurrentText(settings['generation_settings']['measure_adjusted_freq'])

        # Table Settings
        self.checkbox_show_pct.setChecked(settings['table_settings']['show_pct'])
        self.checkbox_show_cumulative.setChecked(settings['table_settings']['show_cumulative'])
        self.checkbox_show_breakdown.setChecked(settings['table_settings']['show_breakdown'])

        # Plot Settings
        self.combo_box_plot_type.setCurrentText(settings['plot_settings']['plot_type'])
        self.combo_box_use_file.setCurrentText(settings['plot_settings']['use_file'])
        self.combo_box_use_data.setCurrentText(settings['plot_settings']['use_data'])
        self.checkbox_use_pct.setChecked(settings['plot_settings']['use_pct'])
        self.checkbox_use_cumulative.setChecked(settings['plot_settings']['use_cumulative'])

        self.spin_box_rank_min.setValue(settings['plot_settings']['rank_min'])
        self.checkbox_rank_min_no_limit.setChecked(settings['plot_settings']['rank_min_no_limit'])
        self.spin_box_rank_max.setValue(settings['plot_settings']['rank_max'])
        self.checkbox_rank_max_no_limit.setChecked(settings['plot_settings']['rank_max_no_limit'])

        self.token_settings_changed()
        self.generation_settings_changed()
        self.table_settings_changed()
        self.plot_settings_changed()

    def token_settings_changed(self):
        settings = self.main.settings_custom['wordlist']['token_settings']

        settings['words'] = self.checkbox_words.isChecked()
        settings['lowercase'] = self.checkbox_lowercase.isChecked()
        settings['uppercase'] = self.checkbox_uppercase.isChecked()
        settings['title_case'] = self.checkbox_title_case.isChecked()
        settings['nums'] = self.checkbox_nums.isChecked()
        settings['puncs'] = self.checkbox_puncs.isChecked()

        settings['treat_as_lowercase'] = self.checkbox_treat_as_lowercase.isChecked()
        settings['lemmatize_tokens'] = self.checkbox_lemmatize_tokens.isChecked()
        settings['filter_stop_words'] = self.checkbox_filter_stop_words.isChecked()

        settings['ignore_tags'] = self.stacked_widget_ignore_tags.checkbox_ignore_tags.isChecked()
        settings['ignore_tags_tags'] = self.stacked_widget_ignore_tags.checkbox_ignore_tags_tags.isChecked()
        settings['ignore_tags_type'] = self.stacked_widget_ignore_tags_tags.combo_box_ignore_tags.currentText()
        settings['ignore_tags_type_tags'] = self.stacked_widget_ignore_tags_tags.combo_box_ignore_tags_tags.currentText()
        settings['use_tags'] = self.checkbox_use_tags.isChecked()

    def generation_settings_changed(self):
        settings = self.main.settings_custom['wordlist']['generation_settings']

        settings['measure_dispersion'] = self.combo_box_measure_dispersion.currentText()
        settings['measure_adjusted_freq'] = self.combo_box_measure_adjusted_freq.currentText()

        # Use Data
        use_data_old = self.combo_box_use_data.currentText()

        text_measure_dispersion = settings['measure_dispersion']
        text_measure_adjusted_freq = settings['measure_adjusted_freq']

        self.combo_box_use_data.clear()

        self.combo_box_use_data.addItem(self.tr('Frequency'))
        self.combo_box_use_data.addItem(self.main.settings_global['measures_dispersion'][text_measure_dispersion]['col'])
        self.combo_box_use_data.addItem(self.main.settings_global['measures_adjusted_freq'][text_measure_adjusted_freq]['col'])

        if self.combo_box_use_data.findText(use_data_old) > -1:
            self.combo_box_use_data.setCurrentText(use_data_old)
        else:
            self.combo_box_use_data.setCurrentText(self.main.settings_default['wordlist']['plot_settings']['use_data'])

    def table_settings_changed(self):
        settings = self.main.settings_custom['wordlist']['table_settings']

        settings['show_pct'] = self.checkbox_show_pct.isChecked()
        settings['show_cumulative'] = self.checkbox_show_cumulative.isChecked()
        settings['show_breakdown'] = self.checkbox_show_breakdown.isChecked()

    def plot_settings_changed(self):
        settings = self.main.settings_custom['wordlist']['plot_settings']

        settings['plot_type'] = self.combo_box_plot_type.currentText()
        settings['use_file'] = self.combo_box_use_file.currentText()
        settings['use_data'] = self.combo_box_use_data.currentText()
        settings['use_pct'] = self.checkbox_use_pct.isChecked()
        settings['use_cumulative'] = self.checkbox_use_cumulative.isChecked()

        settings['rank_min'] = self.spin_box_rank_min.value()
        settings['rank_min_no_limit'] = self.checkbox_rank_min_no_limit.isChecked()
        settings['rank_max'] = self.spin_box_rank_max.value()
        settings['rank_max_no_limit'] = self.checkbox_rank_max_no_limit.isChecked()

def generate_wordlists(main, files):
    texts = []
    tokens_freq_files = []
    tokens_stats_files = []

    settings = main.settings_custom['wordlist']

    # Frequency
    for file in files:
        text = wordless_text.Wordless_Text(main, file)

        tokens = wordless_token_processing.wordless_process_tokens_wordlist(text,
                                                                            token_settings = settings['token_settings'])

        texts.append(text)
        tokens_freq_files.append(collections.Counter(tokens))

    # Total
    if len(files) > 1:
        text_total = wordless_text.Wordless_Text_Blank()
        text_total.tokens = [token for text in texts for token in text.tokens]

        texts.append(text_total)
        tokens_freq_files.append(sum(tokens_freq_files, collections.Counter()))

    # Dispersion & Adjusted Frequency
    text_measure_dispersion = settings['generation_settings']['measure_dispersion']
    text_measure_adjusted_freq = settings['generation_settings']['measure_adjusted_freq']

    measure_dispersion = main.settings_global['measures_dispersion'][text_measure_dispersion]['func']
    measure_adjusted_freq = main.settings_global['measures_adjusted_freq'][text_measure_adjusted_freq]['func']

    tokens_total = tokens_freq_files[-1].keys()

    for text in texts:
        tokens_stats_file = {}

        # Dispersion
        number_sections = main.settings_custom['measures']['dispersion']['general']['number_sections']

        sections_freq = [collections.Counter(section)
                         for section in wordless_text_utils.to_sections(text.tokens, number_sections)]

        for token in tokens_total:
            counts = [section_freq[token] for section_freq in sections_freq]

            tokens_stats_file[token] = [measure_dispersion(counts)]

        # Adjusted Frequency
        if not main.settings_custom['measures']['adjusted_freq']['general']['use_same_settings_dispersion']:
            number_sections = main.settings_custom['measures']['adjusted_freq']['general']['number_sections']

            sections_freq = [collections.Counter(section)
                             for section in wordless_text_utils.to_sections(text.tokens, number_sections)]

        for token in tokens_total:
            counts = [section_freq[token] for section_freq in sections_freq]

            tokens_stats_file[token].append(measure_adjusted_freq(counts))

        tokens_stats_files.append(tokens_stats_file)

    if len(files) == 1:
        tokens_freq_files *= 2
        tokens_stats_files *= 2

    return (wordless_misc.merge_dicts(tokens_freq_files),
            wordless_misc.merge_dicts(tokens_stats_files))

@ wordless_misc.log_timing
def generate_table(main, table):
    settings = main.settings_custom['wordlist']

    files = main.wordless_files.get_selected_files()

    if wordless_checking_file.check_files_on_loading(main, files):
        tokens_freq_files, tokens_stats_files = generate_wordlists(main, files)

        if tokens_freq_files:
            table.clear_table()

            table.settings = copy.deepcopy(main.settings_custom)

            text_measure_dispersion = settings['generation_settings']['measure_dispersion']
            text_measure_adjusted_freq = settings['generation_settings']['measure_adjusted_freq']

            text_dispersion = main.settings_global['measures_dispersion'][text_measure_dispersion]['col']
            text_adjusted_freq = main.settings_global['measures_adjusted_freq'][text_measure_adjusted_freq]['col']

            table.blockSignals(True)
            table.setSortingEnabled(False)
            table.setUpdatesEnabled(False)

            if settings['token_settings']['use_tags']:
                table.setHorizontalHeaderLabels([
                    main.tr('Rank'),
                    main.tr('Tags'),
                    main.tr('Number of\nFiles Found')
                ])

            # Insert Columns (Files)
            for file in files:
                table.insert_col(table.columnCount() - 1,
                                 main.tr(f'[{file["name"]}]\nFrequency'),
                                 num = True, pct = True, cumulative = True, breakdown = True)

                table.insert_col(table.columnCount() - 1,
                                 main.tr(f'[{file["name"]}]\n{text_dispersion}'),
                                 num = True, breakdown = True)

                table.insert_col(table.columnCount() - 1,
                                 main.tr(f'[{file["name"]}]\n{text_adjusted_freq}'),
                                 num = True, breakdown = True)

            # Insert Columns (Total)
            table.insert_col(table.columnCount() - 1,
                             main.tr('Total\nFrequency'),
                             num = True, pct = True, cumulative = True)

            table.insert_col(table.columnCount() - 1,
                             main.tr(f'Total\n{text_dispersion}'),
                             num = True)

            table.insert_col(table.columnCount() - 1,
                             main.tr(f'Total\n{text_adjusted_freq}'),
                             num = True)

            # Sort by frequency of the first file
            table.sortByColumn(table.find_col(main.tr(f'[{files[0]["name"]}]\nFrequency')), Qt.DescendingOrder)

            cols_freq = table.find_cols(main.tr('\nFrequency'))
            cols_dispersion = table.find_cols(main.tr(f'\n{text_dispersion}'))
            cols_adjusted_freq = table.find_cols(main.tr(f'\n{text_adjusted_freq}'))
            col_files_found = table.find_col(main.tr('Number of\nFiles Found'))

            len_files = len(files)

            table.setRowCount(len(tokens_freq_files))

            for i, (token, freq_files) in enumerate(wordless_sorting.sorted_tokens_freq_files(tokens_freq_files)):
                stats_files = tokens_stats_files[token]

                # Rank
                table.set_item_num_int(i, 0, -1)

                # Tokens
                table.setItem(i, 1, wordless_table.Wordless_Table_Item(token))

                # Frequency
                for j, freq in enumerate(freq_files):
                    table.set_item_num_cumulative(i, cols_freq[j], freq)

                for j, (dispersion, adjusted_freq) in enumerate(stats_files):
                    # Dispersion
                    table.set_item_num_float(i, cols_dispersion[j], dispersion)

                    # Adjusted Frequency
                    table.set_item_num_float(i, cols_adjusted_freq[j], adjusted_freq)

                # Number of Files Found
                table.set_item_num_pct(i, col_files_found,
                                       len([freq for freq in freq_files[:-1] if freq]),
                                       len_files)

            table.blockSignals(False)
            table.setSortingEnabled(True)
            table.setUpdatesEnabled(True)

            table.toggle_pct()
            table.toggle_cumulative()
            table.toggle_breakdown()
            table.update_ranks()

            table.update_items_width()

            table.itemChanged.emit(table.item(0, 0))

            wordless_message.wordless_message_generate_table_success(main)
        else:
            wordless_message_box.wordless_message_box_no_results_table(main)

            wordless_message.wordless_message_generate_table_error(main)
    else:
        wordless_message.wordless_message_generate_table_error(main)

@ wordless_misc.log_timing
def generate_plot(main):
    settings = main.settings_custom['wordlist']

    files = main.wordless_files.get_selected_files()

    if wordless_checking_file.check_files_on_loading(main, files):
        tokens_freq_files, tokens_stats_files = generate_wordlists(main, files)

        if tokens_freq_files:
            measure_dispersion = settings['generation_settings']['measure_dispersion']
            measure_adjusted_freq = settings['generation_settings']['measure_adjusted_freq']

            col_dispersion = main.settings_global['measures_dispersion'][measure_dispersion]['col']
            col_adjusted_freq = main.settings_global['measures_adjusted_freq'][measure_adjusted_freq]['col']
            
            if settings['plot_settings']['use_data'] == main.tr('Frequency'):
                wordless_plot_freq.wordless_plot_freq(main, tokens_freq_files,
                                                      settings = settings['plot_settings'],
                                                      label_x = main.tr('Tokens'))
            else:
                if settings['plot_settings']['use_data'] == col_dispersion:
                    tokens_stat_files = {token: numpy.array(stats_files)[:, 0]
                                         for token, stats_files in tokens_stats_files.items()}

                    label_y = col_dispersion
                elif settings['plot_settings']['use_data'] == col_adjusted_freq:
                    tokens_stat_files = {token: numpy.array(stats_files)[:, 1]
                                         for token, stats_files in tokens_stats_files.items()}

                    label_y = col_adjusted_freq

                wordless_plot_stat.wordless_plot_stat(main, tokens_stat_files,
                                                      settings = settings['plot_settings'],
                                                      label_x = main.tr('Tokens'),
                                                      label_y = label_y)

            wordless_message.wordless_message_generate_plot_success(main)
        else:
            wordless_message_box.wordless_message_box_no_results_plot(main)

            wordless_message.wordless_message_generate_plot_error(main)
    else:
        wordless_message.wordless_message_generate_plot_error(main)
