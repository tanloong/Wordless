# ----------------------------------------------------------------------
# Wordless: Settings - Measures
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

import copy

from PyQt5.QtWidgets import QCheckBox, QGroupBox, QLabel

from wordless.wl_settings import wl_settings
from wordless.wl_widgets import wl_boxes, wl_layouts, wl_widgets

# Measures - Readability
class Wl_Settings_Measures_Readability(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['readability']
        self.settings_custom = self.main.settings_custom['measures']['readability']

        # Al-Heeti's Readability Prediction Formula
        self.group_box_rd = QGroupBox(self.tr("Al-Heeti's Readability Prediction Formula"), self)

        self.label_rd_variant = QLabel(self.tr('Variant:'), self)
        self.combo_box_rd_variant = wl_boxes.Wl_Combo_Box(self)

        self.combo_box_rd_variant.addItems([
            self.tr('Policy one'),
            self.tr('Policy two')
        ])

        self.group_box_rd.setLayout(wl_layouts.Wl_Layout())
        self.group_box_rd.layout().addWidget(self.label_rd_variant, 0, 0)
        self.group_box_rd.layout().addWidget(self.combo_box_rd_variant, 0, 1)

        self.group_box_rd.layout().setColumnStretch(2, 1)

        # Automated Readability Index
        self.group_box_ari = QGroupBox(self.tr('Automated Readability Index'), self)

        self.checkbox_use_navy_variant = QCheckBox(self.tr('Use Navy variant'), self)

        self.group_box_ari.setLayout(wl_layouts.Wl_Layout())
        self.group_box_ari.layout().addWidget(self.checkbox_use_navy_variant, 0, 0)

        # Bormuth's Grade Placement
        self.group_box_bormuths_gp = QGroupBox(self.tr("Bormuth's Grade Placement"), self)

        self.label_cloze_criterion_score = QLabel(self.tr('Cloze criterion score:'), self)
        self.spin_box_cloze_criterion_score = wl_boxes.Wl_Spin_Box(self)

        self.spin_box_cloze_criterion_score.setRange(0, 100)
        self.spin_box_cloze_criterion_score.setSuffix('%')

        self.group_box_bormuths_gp.setLayout(wl_layouts.Wl_Layout())
        self.group_box_bormuths_gp.layout().addWidget(self.label_cloze_criterion_score, 0, 0)
        self.group_box_bormuths_gp.layout().addWidget(self.spin_box_cloze_criterion_score, 0, 1)

        self.group_box_bormuths_gp.layout().setColumnStretch(2, 1)

        # Coleman's Readability Formula
        self.group_box_colemans_readability_formula = QGroupBox(self.tr("Coleman's Readability Formula"), self)

        self.label_colemans_readability_formula_variant = QLabel(self.tr('Variant:'), self)
        self.combo_box_colemans_readability_formula_variant = wl_boxes.Wl_Combo_Box(self)

        self.combo_box_colemans_readability_formula_variant.addItems(['1', '2', '3', '4'])

        self.group_box_colemans_readability_formula.setLayout(wl_layouts.Wl_Layout())
        self.group_box_colemans_readability_formula.layout().addWidget(self.label_colemans_readability_formula_variant, 0, 0)
        self.group_box_colemans_readability_formula.layout().addWidget(self.combo_box_colemans_readability_formula_variant, 0, 1)

        self.group_box_colemans_readability_formula.layout().setColumnStretch(2, 1)

        # Dale-Chall Readability Formula
        self.group_box_x_c50 = QGroupBox(self.tr('Dale-Chall Readability Formula'), self)
        self.label_x_c50_variant = QLabel(self.tr('Variant:'), self)
        self.combo_box_x_c50_variant = wl_boxes.Wl_Combo_Box(self)

        self.combo_box_x_c50_variant.addItems([
            self.tr('Original'),
            'Powers-Sumner-Kearl',
            self.tr('New')
        ])

        self.group_box_x_c50.setLayout(wl_layouts.Wl_Layout())
        self.group_box_x_c50.layout().addWidget(self.label_x_c50_variant, 0, 0)
        self.group_box_x_c50.layout().addWidget(self.combo_box_x_c50_variant, 0, 1)

        self.group_box_x_c50.layout().setColumnStretch(2, 1)

        # Danielson-Bryan's Readability Formula
        self.group_box_danielson_bryans_readability_formula = QGroupBox(self.tr("Danielson-Bryan's Readability Formula"), self)

        self.label_danielson_bryans_readability_formula_variant = QLabel(self.tr('Variant:'), self)
        self.combo_box_danielson_bryans_readability_formula_variant = wl_boxes.Wl_Combo_Box(self)

        self.combo_box_danielson_bryans_readability_formula_variant.addItems(['1', '2'])

        self.group_box_danielson_bryans_readability_formula.setLayout(wl_layouts.Wl_Layout())
        self.group_box_danielson_bryans_readability_formula.layout().addWidget(self.label_danielson_bryans_readability_formula_variant, 0, 0)
        self.group_box_danielson_bryans_readability_formula.layout().addWidget(self.combo_box_danielson_bryans_readability_formula_variant, 0, 1)

        self.group_box_danielson_bryans_readability_formula.layout().setColumnStretch(2, 1)

        # Flesch Reading Ease
        self.group_box_re = QGroupBox(self.tr('Flesch Reading Ease'), self)

        self.checkbox_use_powers_sumner_kearl_variant_for_all_langs = QCheckBox(self.tr('Use Powers-Sumner-Kearl variant for all languages'), self)
        self.label_re_variant_nld = QLabel(self.tr('Dutch variant:'), self)
        self.combo_box_re_variant_nld = wl_boxes.Wl_Combo_Box(self)
        self.label_re_variant_spa = QLabel(self.tr('Spanish variant:'), self)
        self.combo_box_re_variant_spa = wl_boxes.Wl_Combo_Box(self)

        self.combo_box_re_variant_nld.addItems([
            self.tr("Brouwer's Leesindex A"),
            'Douma',
        ])
        self.combo_box_re_variant_spa.addItems([
            'Fernández Huerta',
            'Szigriszt Pazos'
        ])

        self.checkbox_use_powers_sumner_kearl_variant_for_all_langs.stateChanged.connect(self.re_changed)

        self.group_box_re.setLayout(wl_layouts.Wl_Layout())
        self.group_box_re.layout().addWidget(self.checkbox_use_powers_sumner_kearl_variant_for_all_langs, 0, 0, 1, 3)
        self.group_box_re.layout().addWidget(self.label_re_variant_nld, 1, 0)
        self.group_box_re.layout().addWidget(self.combo_box_re_variant_nld, 1, 1)
        self.group_box_re.layout().addWidget(self.label_re_variant_spa, 2, 0)
        self.group_box_re.layout().addWidget(self.combo_box_re_variant_spa, 2, 1)

        self.group_box_re.layout().setColumnStretch(2, 1)

        # Flesch Reading Ease (Farr-Jenkins-Paterson)
        self.group_box_re_farr_jenkins_paterson = QGroupBox(self.tr('Flsch Reading Ease (Farr-Jenkins-Paterson)'), self)

        self.checkbox_use_powers_sumner_kearl_variant = QCheckBox(self.tr('Use Powers-Sumner-Kearl variant'), self)

        self.group_box_re_farr_jenkins_paterson.setLayout(wl_layouts.Wl_Layout())
        self.group_box_re_farr_jenkins_paterson.layout().addWidget(self.checkbox_use_powers_sumner_kearl_variant, 0, 0)

        # Gunning Fog Index
        self.group_box_fog_index = QGroupBox(self.tr('Gunning Fog Index'), self)

        self.label_fog_index_variant_eng = QLabel(self.tr('English variant:'), self)
        self.combo_box_fog_index_variant_eng = wl_boxes.Wl_Combo_Box(self)

        self.combo_box_fog_index_variant_eng.addItems([
            self.tr('Original'),
            'Powers-Sumner-Kearl',
            self.tr('Navy')
        ])

        self.group_box_fog_index.setLayout(wl_layouts.Wl_Layout())
        self.group_box_fog_index.layout().addWidget(self.label_fog_index_variant_eng, 0, 0)
        self.group_box_fog_index.layout().addWidget(self.combo_box_fog_index_variant_eng, 0, 1)

        self.group_box_fog_index.layout().setColumnStretch(2, 1)

        # Lorge Readability Index
        self.group_box_lorge_readability_index = QGroupBox(self.tr('Lorge Readability Index'), self)

        self.checkbox_use_corrected_formula = QCheckBox(self.tr('Use corrected formula'), self)

        self.group_box_lorge_readability_index.setLayout(wl_layouts.Wl_Layout())
        self.group_box_lorge_readability_index.layout().addWidget(self.checkbox_use_corrected_formula, 0, 0)

        # neue Wiener Literaturformeln
        self.group_box_nwl = QGroupBox(self.tr('neue Wiener Literaturformeln'), self)

        self.label_nwl_variant = QLabel(self.tr('Variant:'), self)
        self.combo_box_nwl_variant = wl_boxes.Wl_Combo_Box(self)

        self.combo_box_nwl_variant.addItems(['1', '2', '3'])

        self.group_box_nwl.setLayout(wl_layouts.Wl_Layout())
        self.group_box_nwl.layout().addWidget(self.label_nwl_variant, 0, 0)
        self.group_box_nwl.layout().addWidget(self.combo_box_nwl_variant, 0, 1)

        self.group_box_nwl.layout().setColumnStretch(2, 1)

        # neue Wiener Sachtextformel
        self.group_box_nws = QGroupBox(self.tr('neue Wiener Sachtextformel'), self)

        self.label_nws_variant = QLabel(self.tr('Variant:'), self)
        self.combo_box_nws_variant = wl_boxes.Wl_Combo_Box(self)

        self.combo_box_nws_variant.addItems(['1', '2', '3'])

        self.group_box_nws.setLayout(wl_layouts.Wl_Layout())
        self.group_box_nws.layout().addWidget(self.label_nws_variant, 0, 0)
        self.group_box_nws.layout().addWidget(self.combo_box_nws_variant, 0, 1)

        self.group_box_nws.layout().setColumnStretch(2, 1)

        # Spache Grade Level
        self.group_box_spache_grade_lvl = QGroupBox(self.tr('Spache Grade Level'), self)

        self.checkbox_use_rev_formula = QCheckBox(self.tr('Use revised formula'), self)

        self.group_box_spache_grade_lvl.setLayout(wl_layouts.Wl_Layout())
        self.group_box_spache_grade_lvl.layout().addWidget(self.checkbox_use_rev_formula, 0, 0)

        # Tränkle & Bailer's Readability Formula
        self.group_box_trankle_bailers_readability_formula = QGroupBox(self.tr("Tränkle & Bailer's Readability Formula"), self)

        self.label_trankle_bailers_readability_formula_variant = QLabel(self.tr('Variant:'), self)
        self.combo_box_trankle_bailers_readability_formula_variant = wl_boxes.Wl_Combo_Box(self)

        self.combo_box_trankle_bailers_readability_formula_variant.addItems(['1', '2'])

        self.group_box_trankle_bailers_readability_formula.setLayout(wl_layouts.Wl_Layout())
        self.group_box_trankle_bailers_readability_formula.layout().addWidget(self.label_trankle_bailers_readability_formula_variant, 0, 0)
        self.group_box_trankle_bailers_readability_formula.layout().addWidget(self.combo_box_trankle_bailers_readability_formula_variant, 0, 1)

        self.group_box_trankle_bailers_readability_formula.layout().setColumnStretch(2, 1)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(self.group_box_rd, 0, 0)
        self.layout().addWidget(self.group_box_ari, 1, 0)
        self.layout().addWidget(self.group_box_bormuths_gp, 2, 0)
        self.layout().addWidget(self.group_box_colemans_readability_formula, 3, 0)
        self.layout().addWidget(self.group_box_x_c50, 4, 0)
        self.layout().addWidget(self.group_box_danielson_bryans_readability_formula, 5, 0)
        self.layout().addWidget(self.group_box_re, 6, 0)
        self.layout().addWidget(self.group_box_re_farr_jenkins_paterson, 7, 0)
        self.layout().addWidget(self.group_box_fog_index, 8, 0)
        self.layout().addWidget(self.group_box_lorge_readability_index, 9, 0)
        self.layout().addWidget(self.group_box_nwl, 10, 0)
        self.layout().addWidget(self.group_box_nws, 11, 0)
        self.layout().addWidget(self.group_box_spache_grade_lvl, 12, 0)
        self.layout().addWidget(self.group_box_trankle_bailers_readability_formula, 13, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(14, 1)

    def re_changed(self):
        if self.checkbox_use_powers_sumner_kearl_variant_for_all_langs.isChecked():
            self.combo_box_re_variant_nld.setEnabled(False)
            self.combo_box_re_variant_spa.setEnabled(False)
        else:
            self.combo_box_re_variant_nld.setEnabled(True)
            self.combo_box_re_variant_spa.setEnabled(True)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        # Al-Heeti's Readability Prediction Formula
        self.combo_box_rd_variant.setCurrentText(settings['rd']['variant'])

        # Automated Readability Index
        self.checkbox_use_navy_variant.setChecked(settings['ari']['use_navy_variant'])

        # Bormuth's Grade Placement
        self.spin_box_cloze_criterion_score.setValue(settings['bormuths_gp']['cloze_criterion_score'])

        # Coleman's Readability Formula
        self.combo_box_colemans_readability_formula_variant.setCurrentText(settings['colemans_readability_formula']['variant'])

        # Dale-Chall Readability Formula
        self.combo_box_x_c50_variant.setCurrentText(settings['x_c50']['variant'])

        # Danielson-Bryan's Readability Formula
        self.combo_box_danielson_bryans_readability_formula_variant.setCurrentText(settings['danielson_bryans_readability_formula']['variant'])

        # Flesch Reading Ease
        self.checkbox_use_powers_sumner_kearl_variant_for_all_langs.setChecked(settings['re']['use_powers_sumner_kearl_variant_for_all_langs'])
        self.combo_box_re_variant_nld.setCurrentText(settings['re']['variant_nld'])
        self.combo_box_re_variant_spa.setCurrentText(settings['re']['variant_spa'])

        # Flesch Reading Ease (Farr-Jenkins-Paterson)
        self.checkbox_use_powers_sumner_kearl_variant.setChecked(settings['re_farr_jenkins_paterson']['use_powers_sumner_kearl_variant'])

        # Gunning Fog Index
        self.combo_box_fog_index_variant_eng.setCurrentText(settings['fog_index']['variant_eng'])

        # Lorge Readability Index
        self.checkbox_use_corrected_formula.setChecked(settings['lorge_readability_index']['use_corrected_formula'])

        # neue Wiener Literaturformeln
        self.combo_box_nwl_variant.setCurrentText(settings['nwl']['variant'])

        # neue Wiener Sachtextformel
        self.combo_box_nws_variant.setCurrentText(settings['nws']['variant'])

        # Spache Grade Level
        self.checkbox_use_rev_formula.setChecked(settings['spache_grade_lvl']['use_rev_formula'])

        # Tränkle & Bailer's Readability Formula
        self.combo_box_trankle_bailers_readability_formula_variant.setCurrentText(settings['trankle_bailers_readability_formula']['variant'])

    def apply_settings(self):
        # Al-Heeti's Readability Prediction Formula
        self.settings_custom['rd']['variant'] = self.combo_box_rd_variant.currentText()

        # Automated Readability Index
        self.settings_custom['ari']['use_navy_variant'] = self.checkbox_use_navy_variant.isChecked()

        # Bormuth's Grade Placement
        self.settings_custom['bormuths_gp']['cloze_criterion_score'] = self.spin_box_cloze_criterion_score.value()

        # Coleman's Readability Formula
        self.settings_custom['colemans_readability_formula']['variant'] = self.combo_box_colemans_readability_formula_variant.currentText()

        # Dale-Chall Readability Formula
        self.settings_custom['x_c50']['variant'] = self.combo_box_x_c50_variant.currentText()

        # Danielson-Bryan's Readability Formula
        self.settings_custom['danielson_bryans_readability_formula']['variant'] = self.combo_box_danielson_bryans_readability_formula_variant.currentText()

        # Flesch Reading Ease
        self.settings_custom['re']['use_powers_sumner_kearl_variant_for_all_langs'] = self.checkbox_use_powers_sumner_kearl_variant_for_all_langs.isChecked()
        self.settings_custom['re']['variant_nld'] = self.combo_box_re_variant_nld.currentText()
        self.settings_custom['re']['variant_spa'] = self.combo_box_re_variant_spa.currentText()

        # Flesch Reading Ease (Farr-Jenkins-Paterson)
        self.settings_custom['re_farr_jenkins_paterson']['use_powers_sumner_kearl_variant'] = self.checkbox_use_powers_sumner_kearl_variant.isChecked()

        # Gunning Fog Index
        self.settings_custom['fog_index']['variant_eng'] = self.combo_box_fog_index_variant_eng.currentText()

        # Lorge Readability Index
        self.settings_custom['lorge_readability_index']['use_corrected_formula'] = self.checkbox_use_corrected_formula.isChecked()

        # neue Wiener Literaturformeln
        self.settings_custom['nwl']['variant'] = self.combo_box_nwl_variant.currentText()

        # neue Wiener Sachtextformel
        self.settings_custom['nws']['variant'] = self.combo_box_nws_variant.currentText()

        # Spache Grade Level
        self.settings_custom['spache_grade_lvl']['use_rev_formula'] = self.checkbox_use_rev_formula.isChecked()

        # Tränkle & Bailer's Readability Formula
        self.settings_custom['trankle_bailers_readability_formula']['variant'] = self.combo_box_trankle_bailers_readability_formula_variant.currentText()

        return True

# Measures - Type-token Ratio
class Wl_Settings_Measures_Ttr(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['ttr']
        self.settings_custom = self.main.settings_custom['measures']['ttr']

        # Mean Segmental TTR
        self.group_box_msttr = QGroupBox(self.tr('Mean Segmental TTR'), self)

        self.label_msttr_num_tokens_in_each_seg = QLabel(self.tr('Number of tokens in each segment:'), self)
        self.spin_box_msttr_num_tokens_in_each_seg = wl_boxes.Wl_Spin_Box(self)

        self.spin_box_msttr_num_tokens_in_each_seg.setRange(1, 100000)

        self.group_box_msttr.setLayout(wl_layouts.Wl_Layout())
        self.group_box_msttr.layout().addWidget(self.label_msttr_num_tokens_in_each_seg, 0, 0)
        self.group_box_msttr.layout().addWidget(self.spin_box_msttr_num_tokens_in_each_seg, 0, 1)

        self.group_box_msttr.layout().setColumnStretch(2, 1)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(self.group_box_msttr, 0, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(1, 1)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        # Mean Segmental TTR
        self.spin_box_msttr_num_tokens_in_each_seg.setValue(settings['msttr']['num_tokens_in_each_seg'])

    def apply_settings(self):
        # Mean Segmental TTR
        self.settings_custom['msttr']['num_tokens_in_each_seg'] = self.spin_box_msttr_num_tokens_in_each_seg.value()

        return True

# Measures - Dispersion
class Wl_Settings_Measures_Dispersion(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['dispersion']
        self.settings_custom = self.main.settings_custom['measures']['dispersion']

        # General Settings
        self.group_box_general_settings = QGroupBox(self.tr('General Settings'), self)

        (
            self.label_dispersion_divide_each_file_into,
            self.spin_box_dispersion_num_sub_sections,
            self.label_dispersion_sub_sections
        ) = wl_widgets.wl_widgets_num_sub_sections(self)

        self.group_box_general_settings.setLayout(wl_layouts.Wl_Layout())
        self.group_box_general_settings.layout().addWidget(self.label_dispersion_divide_each_file_into, 0, 0)
        self.group_box_general_settings.layout().addWidget(self.spin_box_dispersion_num_sub_sections, 0, 1)
        self.group_box_general_settings.layout().addWidget(self.label_dispersion_sub_sections, 0, 2)

        self.group_box_general_settings.layout().setColumnStretch(3, 1)

        self.group_box_griess_dp = QGroupBox(self.tr("Gries's DP"), self)

        self.checkbox_griess_dp_apply_normalization = QCheckBox(self.tr('Apply normalization'), self)

        self.group_box_griess_dp.setLayout(wl_layouts.Wl_Layout())
        self.group_box_griess_dp.layout().addWidget(self.checkbox_griess_dp_apply_normalization, 0, 0)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(self.group_box_general_settings, 0, 0)
        self.layout().addWidget(self.group_box_griess_dp, 1, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(2, 1)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        # General Settings
        self.spin_box_dispersion_num_sub_sections.setValue(settings['general_settings']['num_sub_sections'])

        # Gries's DP
        self.checkbox_griess_dp_apply_normalization.setChecked(settings['griess_dp']['apply_normalization'])

    def apply_settings(self):
        # General Settings
        self.settings_custom['general_settings']['num_sub_sections'] = self.spin_box_dispersion_num_sub_sections.value()

        # Gries's DP
        self.settings_custom['griess_dp']['apply_normalization'] = self.checkbox_griess_dp_apply_normalization.isChecked()

        return True

# Measures - Adjusted Frequency
class Wl_Settings_Measures_Adjusted_Freq(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['adjusted_freq']
        self.settings_custom = self.main.settings_custom['measures']['adjusted_freq']

        # General Settings
        self.group_box_general_settings = QGroupBox(self.tr('General Settings'), self)

        (
            self.label_adjusted_freq_divide_each_file_into,
            self.spin_box_adjusted_freq_num_sub_sections,
            self.label_adjusted_freq_sub_sections
        ) = wl_widgets.wl_widgets_num_sub_sections(self)

        self.group_box_general_settings.setLayout(wl_layouts.Wl_Layout())
        self.group_box_general_settings.layout().addWidget(self.label_adjusted_freq_divide_each_file_into, 0, 0)
        self.group_box_general_settings.layout().addWidget(self.spin_box_adjusted_freq_num_sub_sections, 0, 1)
        self.group_box_general_settings.layout().addWidget(self.label_adjusted_freq_sub_sections, 0, 2)

        self.group_box_general_settings.layout().setColumnStretch(3, 1)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(self.group_box_general_settings, 0, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(1, 1)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        # General Settings
        self.spin_box_adjusted_freq_num_sub_sections.setValue(settings['general_settings']['num_sub_sections'])

    def apply_settings(self):
        # General Settings
        self.settings_custom['general_settings']['num_sub_sections'] = self.spin_box_adjusted_freq_num_sub_sections.value()

        return True

# Measures - Statistical Significance
class Wl_Settings_Measures_Statistical_Significance(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['statistical_significance']
        self.settings_custom = self.main.settings_custom['measures']['statistical_significance']

        # Fisher's Exact Test
        self.group_box_fishers_exact_test = QGroupBox(self.tr("Fisher's Exact Test"), self)

        (
            self.label_fishers_exact_test_direction,
            self.combo_box_fishers_exact_test_direction
        ) = wl_widgets.wl_widgets_direction(self)

        self.group_box_fishers_exact_test.setLayout(wl_layouts.Wl_Layout())
        self.group_box_fishers_exact_test.layout().addWidget(self.label_fishers_exact_test_direction, 0, 0)
        self.group_box_fishers_exact_test.layout().addWidget(self.combo_box_fishers_exact_test_direction, 0, 1)

        self.group_box_fishers_exact_test.layout().setColumnStretch(2, 1)

        # Log-likelihood Ratio Test
        self.group_box_log_likelihood_ratio_test = QGroupBox(self.tr('Log-likelihood Ratio Test'), self)

        self.checkbox_log_likelihood_ratio_test_apply_correction = QCheckBox(self.tr("Apply Yates's correction for continuity"))

        self.group_box_log_likelihood_ratio_test.setLayout(wl_layouts.Wl_Layout())
        self.group_box_log_likelihood_ratio_test.layout().addWidget(self.checkbox_log_likelihood_ratio_test_apply_correction, 0, 0)

        # Mann-Whitney U Test
        self.group_box_mann_whitney_u_test = QGroupBox(self.tr('Mann-Whitney U Test'), self)

        (
            self.label_mann_whitney_u_test_divide_each_file_into,
            self.spin_box_mann_whitney_u_test_num_sub_sections,
            self.label_mann_whitney_u_test_sub_sections
        ) = wl_widgets.wl_widgets_num_sub_sections(self)

        (
            self.label_mann_whitney_u_test_use_data,
            self.combo_box_mann_whitney_u_test_use_data
        ) = wl_widgets.wl_widgets_use_data_freq(self)
        (
            self.label_mann_whitney_u_test_direction,
            self.combo_box_mann_whitney_u_test_direction
        ) = wl_widgets.wl_widgets_direction(self)
        self.checkbox_mann_whitney_u_test_apply_correction = QCheckBox(self.tr('Apply continuity correction'), self)

        layout_mann_whitney_u_test_num_sub_sections = wl_layouts.Wl_Layout()
        layout_mann_whitney_u_test_num_sub_sections.addWidget(self.label_mann_whitney_u_test_divide_each_file_into, 0, 0)
        layout_mann_whitney_u_test_num_sub_sections.addWidget(self.spin_box_mann_whitney_u_test_num_sub_sections, 0, 1)
        layout_mann_whitney_u_test_num_sub_sections.addWidget(self.label_mann_whitney_u_test_sub_sections, 0, 2)

        layout_mann_whitney_u_test_num_sub_sections.setColumnStretch(3, 1)

        self.group_box_mann_whitney_u_test.setLayout(wl_layouts.Wl_Layout())
        self.group_box_mann_whitney_u_test.layout().addLayout(layout_mann_whitney_u_test_num_sub_sections, 0, 0, 1, 3)
        self.group_box_mann_whitney_u_test.layout().addWidget(self.label_mann_whitney_u_test_use_data, 1, 0)
        self.group_box_mann_whitney_u_test.layout().addWidget(self.combo_box_mann_whitney_u_test_use_data, 1, 1)
        self.group_box_mann_whitney_u_test.layout().addWidget(self.label_mann_whitney_u_test_direction, 2, 0)
        self.group_box_mann_whitney_u_test.layout().addWidget(self.combo_box_mann_whitney_u_test_direction, 2, 1)
        self.group_box_mann_whitney_u_test.layout().addWidget(self.checkbox_mann_whitney_u_test_apply_correction, 3, 0, 1, 3)

        self.group_box_mann_whitney_u_test.layout().setColumnStretch(3, 1)

        # Pearson's Chi-squared Test
        self.group_box_pearsons_chi_squared_test = QGroupBox(self.tr("Pearson's Chi-squared Test"), self)

        self.checkbox_pearsons_chi_squared_test_apply_correction = QCheckBox(self.tr("Apply Yates's correction for continuity"))

        self.group_box_pearsons_chi_squared_test.setLayout(wl_layouts.Wl_Layout())
        self.group_box_pearsons_chi_squared_test.layout().addWidget(self.checkbox_pearsons_chi_squared_test_apply_correction, 0, 0)

        # Student's t-test (1-sample)
        self.group_box_students_t_test_1_sample = QGroupBox(self.tr("Student's t-test (1-sample)"), self)

        (
            self.label_students_t_test_1_sample_direction,
            self.combo_box_students_t_test_1_sample_direction
        ) = wl_widgets.wl_widgets_direction(self)

        self.group_box_students_t_test_1_sample.setLayout(wl_layouts.Wl_Layout())
        self.group_box_students_t_test_1_sample.layout().addWidget(self.label_students_t_test_1_sample_direction, 0, 0)
        self.group_box_students_t_test_1_sample.layout().addWidget(self.combo_box_students_t_test_1_sample_direction, 0, 1)

        self.group_box_students_t_test_1_sample.layout().setColumnStretch(2, 1)

        # Student's t-test (2-sample)
        self.group_box_students_t_test_2_sample = QGroupBox(self.tr("Student's t-test (2-sample)"), self)

        (
            self.label_students_t_test_2_sample_divide_each_file_into,
            self.spin_box_students_t_test_2_sample_num_sub_sections,
            self.label_students_t_test_2_sample_sub_sections
        ) = wl_widgets.wl_widgets_num_sub_sections(self)
        (
            self.label_students_t_test_2_sample_use_data,
            self.combo_box_students_t_test_2_sample_use_data
        ) = wl_widgets.wl_widgets_use_data_freq(self)
        (
            self.label_students_t_test_2_sample_direction,
            self.combo_box_students_t_test_2_sample_direction
        ) = wl_widgets.wl_widgets_direction(self)

        layout_students_t_test_2_sample_num_sub_sections = wl_layouts.Wl_Layout()
        layout_students_t_test_2_sample_num_sub_sections.addWidget(self.label_students_t_test_2_sample_divide_each_file_into, 0, 0)
        layout_students_t_test_2_sample_num_sub_sections.addWidget(self.spin_box_students_t_test_2_sample_num_sub_sections, 0, 1)
        layout_students_t_test_2_sample_num_sub_sections.addWidget(self.label_students_t_test_2_sample_sub_sections, 0, 2)

        layout_students_t_test_2_sample_num_sub_sections.setColumnStretch(3, 1)

        self.group_box_students_t_test_2_sample.setLayout(wl_layouts.Wl_Layout())
        self.group_box_students_t_test_2_sample.layout().addLayout(layout_students_t_test_2_sample_num_sub_sections, 0, 0, 1, 3)
        self.group_box_students_t_test_2_sample.layout().addWidget(self.label_students_t_test_2_sample_use_data, 1, 0)
        self.group_box_students_t_test_2_sample.layout().addWidget(self.combo_box_students_t_test_2_sample_use_data, 1, 1)
        self.group_box_students_t_test_2_sample.layout().addWidget(self.label_students_t_test_2_sample_direction, 2, 0)
        self.group_box_students_t_test_2_sample.layout().addWidget(self.combo_box_students_t_test_2_sample_direction, 2, 1)

        self.group_box_students_t_test_2_sample.layout().setColumnStretch(2, 1)

        # Welch's t-test
        self.group_box_welchs_t_test = QGroupBox(self.tr("Welch's t-test"), self)

        (
            self.label_welchs_t_test_divide_each_file_into,
            self.spin_box_welchs_t_test_num_sub_sections,
            self.label_welchs_t_test_sub_sections
        ) = wl_widgets.wl_widgets_num_sub_sections(self)
        (
            self.label_welchs_t_test_use_data,
            self.combo_box_welchs_t_test_use_data
        ) = wl_widgets.wl_widgets_use_data_freq(self)
        (
            self.label_welchs_t_test_direction,
            self.combo_box_welchs_t_test_direction
        ) = wl_widgets.wl_widgets_direction(self)

        layout_welchs_t_test_num_sub_sections = wl_layouts.Wl_Layout()
        layout_welchs_t_test_num_sub_sections.addWidget(self.label_welchs_t_test_divide_each_file_into, 0, 0)
        layout_welchs_t_test_num_sub_sections.addWidget(self.spin_box_welchs_t_test_num_sub_sections, 0, 1)
        layout_welchs_t_test_num_sub_sections.addWidget(self.label_welchs_t_test_sub_sections, 0, 2)

        layout_welchs_t_test_num_sub_sections.setColumnStretch(3, 1)

        self.group_box_welchs_t_test.setLayout(wl_layouts.Wl_Layout())
        self.group_box_welchs_t_test.layout().addLayout(layout_welchs_t_test_num_sub_sections, 0, 0, 1, 3)
        self.group_box_welchs_t_test.layout().addWidget(self.label_welchs_t_test_use_data, 1, 0)
        self.group_box_welchs_t_test.layout().addWidget(self.combo_box_welchs_t_test_use_data, 1, 1)
        self.group_box_welchs_t_test.layout().addWidget(self.label_welchs_t_test_direction, 2, 0)
        self.group_box_welchs_t_test.layout().addWidget(self.combo_box_welchs_t_test_direction, 2, 1)

        self.group_box_welchs_t_test.layout().setColumnStretch(2, 1)

        # z-score
        self.group_box_z_score = QGroupBox(self.tr('z-score'), self)

        (
            self.label_z_score_direction,
            self.combo_box_z_score_direction
        ) = wl_widgets.wl_widgets_direction(self)

        self.group_box_z_score.setLayout(wl_layouts.Wl_Layout())
        self.group_box_z_score.layout().addWidget(self.label_z_score_direction, 0, 0)
        self.group_box_z_score.layout().addWidget(self.combo_box_z_score_direction, 0, 1)

        self.group_box_z_score.layout().setColumnStretch(2, 1)

        # z-score (Berry-Rogghe)
        self.group_box_z_score_berry_rogghe = QGroupBox(self.tr('z-score (Berry-Rogghe)'), self)

        (
            self.label_z_score_berry_rogghe_direction,
            self.combo_box_z_score_berry_rogghe_direction
        ) = wl_widgets.wl_widgets_direction(self)

        self.group_box_z_score_berry_rogghe.setLayout(wl_layouts.Wl_Layout())
        self.group_box_z_score_berry_rogghe.layout().addWidget(self.label_z_score_berry_rogghe_direction, 0, 0)
        self.group_box_z_score_berry_rogghe.layout().addWidget(self.combo_box_z_score_berry_rogghe_direction, 0, 1)

        self.group_box_z_score_berry_rogghe.layout().setColumnStretch(2, 1)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(self.group_box_fishers_exact_test, 0, 0)
        self.layout().addWidget(self.group_box_log_likelihood_ratio_test, 1, 0)
        self.layout().addWidget(self.group_box_mann_whitney_u_test, 2, 0)
        self.layout().addWidget(self.group_box_pearsons_chi_squared_test, 3, 0)
        self.layout().addWidget(self.group_box_students_t_test_1_sample, 4, 0)
        self.layout().addWidget(self.group_box_students_t_test_2_sample, 5, 0)
        self.layout().addWidget(self.group_box_welchs_t_test, 6, 0)
        self.layout().addWidget(self.group_box_z_score, 7, 0)
        self.layout().addWidget(self.group_box_z_score_berry_rogghe, 8, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(9, 1)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        # Fisher's Exact Test
        self.combo_box_fishers_exact_test_direction.setCurrentText(settings['fishers_exact_test']['direction'])

        # Log-likelihood Ratio Test
        self.checkbox_log_likelihood_ratio_test_apply_correction.setChecked(settings['log_likelihood_ratio_test']['apply_correction'])

        # Mann-Whitney U Test
        self.spin_box_mann_whitney_u_test_num_sub_sections.setValue(settings['mann_whitney_u_test']['num_sub_sections'])
        self.combo_box_mann_whitney_u_test_use_data.setCurrentText(settings['mann_whitney_u_test']['use_data'])
        self.combo_box_mann_whitney_u_test_direction.setCurrentText(settings['mann_whitney_u_test']['direction'])
        self.checkbox_mann_whitney_u_test_apply_correction.setChecked(settings['mann_whitney_u_test']['apply_correction'])

        # Pearson's Chi-squared Test
        self.checkbox_pearsons_chi_squared_test_apply_correction.setChecked(settings['pearsons_chi_squared_test']['apply_correction'])

        # Student's t-test (1-sample)
        self.combo_box_students_t_test_1_sample_direction.setCurrentText(settings['students_t_test_1_sample']['direction'])

        # Student's t-test (2-sample)
        self.spin_box_students_t_test_2_sample_num_sub_sections.setValue(settings['students_t_test_2_sample']['num_sub_sections'])
        self.combo_box_students_t_test_2_sample_use_data.setCurrentText(settings['students_t_test_2_sample']['use_data'])
        self.combo_box_students_t_test_2_sample_direction.setCurrentText(settings['students_t_test_2_sample']['direction'])

        # Welch's t-test
        self.spin_box_welchs_t_test_num_sub_sections.setValue(settings['welchs_t_test']['num_sub_sections'])
        self.combo_box_welchs_t_test_use_data.setCurrentText(settings['welchs_t_test']['use_data'])
        self.combo_box_welchs_t_test_direction.setCurrentText(settings['welchs_t_test']['direction'])

        # z-score
        self.combo_box_z_score_direction.setCurrentText(settings['z_score']['direction'])

        # z-score (Berry-Rogghe)
        self.combo_box_z_score_berry_rogghe_direction.setCurrentText(settings['z_score_berry_rogghe']['direction'])

    def apply_settings(self):
        # Fisher's Exact Test
        self.settings_custom['fishers_exact_test']['direction'] = self.combo_box_fishers_exact_test_direction.currentText()

        # Log-likelihood Ratio Test
        self.settings_custom['log_likelihood_ratio_test']['apply_correction'] = self.checkbox_log_likelihood_ratio_test_apply_correction.isChecked()

        # Mann-Whitney U Test
        self.settings_custom['mann_whitney_u_test']['num_sub_sections'] = self.spin_box_mann_whitney_u_test_num_sub_sections.value()
        self.settings_custom['mann_whitney_u_test']['use_data'] = self.combo_box_mann_whitney_u_test_use_data.currentText()
        self.settings_custom['mann_whitney_u_test']['direction'] = self.combo_box_mann_whitney_u_test_direction.currentText()
        self.settings_custom['mann_whitney_u_test']['apply_correction'] = self.checkbox_mann_whitney_u_test_apply_correction.isChecked()

        # Pearson's Chi-squared Test
        self.settings_custom['pearsons_chi_squared_test']['apply_correction'] = self.checkbox_pearsons_chi_squared_test_apply_correction.isChecked()

        # Student's t-test (1-sample)
        self.settings_custom['students_t_test_1_sample']['direction'] = self.combo_box_students_t_test_1_sample_direction.currentText()

        # Student's t-test (2-sample)
        self.settings_custom['students_t_test_2_sample']['num_sub_sections'] = self.spin_box_students_t_test_2_sample_num_sub_sections.value()
        self.settings_custom['students_t_test_2_sample']['use_data'] = self.combo_box_students_t_test_2_sample_use_data.currentText()
        self.settings_custom['students_t_test_2_sample']['direction'] = self.combo_box_students_t_test_2_sample_direction.currentText()

        # Welch's t-test
        self.settings_custom['welchs_t_test']['num_sub_sections'] = self.spin_box_welchs_t_test_num_sub_sections.value()
        self.settings_custom['welchs_t_test']['use_data'] = self.combo_box_welchs_t_test_use_data.currentText()
        self.settings_custom['welchs_t_test']['direction'] = self.combo_box_welchs_t_test_direction.currentText()

        # z-score
        self.settings_custom['z_score']['direction'] = self.combo_box_z_score_direction.currentText()

        # z-score (Berry-Rogghe)
        self.settings_custom['z_score_berry_rogghe']['direction'] = self.combo_box_z_score_berry_rogghe_direction.currentText()

        return True

# Measures - Bayes Factor
class Wl_Settings_Measures_Bayes_Factor(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['bayes_factor']
        self.settings_custom = self.main.settings_custom['measures']['bayes_factor']

        # Log-likelihood Ratio Test
        self.group_box_log_likelihood_ratio_test = QGroupBox(self.tr('Log-likelihood Ratio Test'), self)

        self.checkbox_log_likelihood_ratio_test_apply_correction = QCheckBox(self.tr("Apply Yates's correction for continuity"))

        self.group_box_log_likelihood_ratio_test.setLayout(wl_layouts.Wl_Layout())
        self.group_box_log_likelihood_ratio_test.layout().addWidget(self.checkbox_log_likelihood_ratio_test_apply_correction, 0, 0)

        # Student's t-test (2-sample)
        self.group_box_students_t_test_2_sample = QGroupBox(self.tr("Student's t-test (2-sample)"), self)

        (
            self.label_students_t_test_2_sample_divide_each_file_into,
            self.spin_box_students_t_test_2_sample_num_sub_sections,
            self.label_students_t_test_2_sample_sub_sections
        ) = wl_widgets.wl_widgets_num_sub_sections(self)
        (
            self.label_students_t_test_2_sample_use_data,
            self.combo_box_students_t_test_2_sample_use_data
        ) = wl_widgets.wl_widgets_use_data_freq(self)
        (
            self.label_students_t_test_2_sample_direction,
            self.combo_box_students_t_test_2_sample_direction
        ) = wl_widgets.wl_widgets_direction(self)

        layout_students_t_test_2_sample_num_sub_sections = wl_layouts.Wl_Layout()
        layout_students_t_test_2_sample_num_sub_sections.addWidget(self.label_students_t_test_2_sample_divide_each_file_into, 0, 0)
        layout_students_t_test_2_sample_num_sub_sections.addWidget(self.spin_box_students_t_test_2_sample_num_sub_sections, 0, 1)
        layout_students_t_test_2_sample_num_sub_sections.addWidget(self.label_students_t_test_2_sample_sub_sections, 0, 2)

        layout_students_t_test_2_sample_num_sub_sections.setColumnStretch(3, 1)

        self.group_box_students_t_test_2_sample.setLayout(wl_layouts.Wl_Layout())
        self.group_box_students_t_test_2_sample.layout().addLayout(layout_students_t_test_2_sample_num_sub_sections, 0, 0, 1, 3)
        self.group_box_students_t_test_2_sample.layout().addWidget(self.label_students_t_test_2_sample_use_data, 1, 0)
        self.group_box_students_t_test_2_sample.layout().addWidget(self.combo_box_students_t_test_2_sample_use_data, 1, 1)
        self.group_box_students_t_test_2_sample.layout().addWidget(self.label_students_t_test_2_sample_direction, 2, 0)
        self.group_box_students_t_test_2_sample.layout().addWidget(self.combo_box_students_t_test_2_sample_direction, 2, 1)

        self.group_box_students_t_test_2_sample.layout().setColumnStretch(2, 1)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(self.group_box_log_likelihood_ratio_test, 0, 0)
        self.layout().addWidget(self.group_box_students_t_test_2_sample, 1, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(2, 1)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        # Log-likelihood Ratio Test
        self.checkbox_log_likelihood_ratio_test_apply_correction.setChecked(settings['log_likelihood_ratio_test']['apply_correction'])

        # Student's t-test (2-sample)
        self.spin_box_students_t_test_2_sample_num_sub_sections.setValue(settings['students_t_test_2_sample']['num_sub_sections'])
        self.combo_box_students_t_test_2_sample_use_data.setCurrentText(settings['students_t_test_2_sample']['use_data'])
        self.combo_box_students_t_test_2_sample_direction.setCurrentText(settings['students_t_test_2_sample']['direction'])

    def apply_settings(self):
        # Log-likelihood Ratio Test
        self.settings_custom['log_likelihood_ratio_test']['apply_correction'] = self.checkbox_log_likelihood_ratio_test_apply_correction.isChecked()

        # Student's t-test (2-sample)
        self.settings_custom['students_t_test_2_sample']['num_sub_sections'] = self.spin_box_students_t_test_2_sample_num_sub_sections.value()
        self.settings_custom['students_t_test_2_sample']['use_data'] = self.combo_box_students_t_test_2_sample_use_data.currentText()
        self.settings_custom['students_t_test_2_sample']['direction'] = self.combo_box_students_t_test_2_sample_direction.currentText()

        return True

# Measures - Effect Size
class Wl_Settings_Measures_Effect_Size(wl_settings.Wl_Settings_Node):
    def __init__(self, main):
        super().__init__(main)

        self.settings_default = self.main.settings_default['measures']['effect_size']
        self.settings_custom = self.main.settings_custom['measures']['effect_size']

        # Kilgarriff's Ratio
        self.group_box_kilgarriffs_ratio = QGroupBox(self.tr("Kilgarriff's Ratio"), self)

        self.label_kilgarriffs_ratio_smoothing_param = QLabel(self.tr('Smoothing parameter:'), self)
        self.spin_box_kilgarriffs_ratio_smoothing_param = wl_boxes.Wl_Double_Spin_Box(self)

        self.spin_box_kilgarriffs_ratio_smoothing_param.setRange(0.01, 10000)

        self.group_box_kilgarriffs_ratio.setLayout(wl_layouts.Wl_Layout())
        self.group_box_kilgarriffs_ratio.layout().addWidget(self.label_kilgarriffs_ratio_smoothing_param, 0, 0)
        self.group_box_kilgarriffs_ratio.layout().addWidget(self.spin_box_kilgarriffs_ratio_smoothing_param, 0, 1)

        self.group_box_kilgarriffs_ratio.layout().setColumnStretch(2, 1)

        self.setLayout(wl_layouts.Wl_Layout())
        self.layout().addWidget(self.group_box_kilgarriffs_ratio, 0, 0)

        self.layout().setContentsMargins(6, 4, 6, 4)
        self.layout().setRowStretch(1, 1)

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.settings_default)
        else:
            settings = copy.deepcopy(self.settings_custom)

        # Kilgarriff's Ratio
        self.spin_box_kilgarriffs_ratio_smoothing_param.setValue(settings['kilgarriffs_ratio']['smoothing_param'])

    def apply_settings(self):
        # Kilgarriff's Ratio
        self.settings_custom['kilgarriffs_ratio']['smoothing_param'] = self.spin_box_kilgarriffs_ratio_smoothing_param.value()

        return True
