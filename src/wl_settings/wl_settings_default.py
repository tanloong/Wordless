#
# Wordless: Settings - Default Settings
#
# Copyright (C) 2018-2021  Ye Lei (叶磊)
#
# This source file is licensed under GNU GPLv3.
# For details, see: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#
# All other rights reserved.
#

from wl_tagsets import (
    wl_tagset_universal,
    wl_tagset_eng_penn_treebank,
    wl_tagset_jpn_unidic,
    wl_tagset_rus_open_corpora,
    wl_tagset_rus_russian_national_corpus,
    wl_tagset_tha_lst20,
    wl_tagset_tha_orchid,
    wl_tagset_bod_botok,
    wl_tagset_vie_underthesea,
    wl_tagset_zho_jieba
)
from wl_utils import wl_misc

def init_settings_default(main):
    main.settings_default = {
        '1st_startup': True,
        'work_area_cur': main.tr('Overview'),

        'layouts': {
            'central_widget': [main.height() - 100 - 210, 210]
        },

        'file_area': {
            'files_open': [],
            'files_closed': [],

            'folder_settings': {
                'subfolders': True
            },

            'auto_detection_settings': {
                'detect_langs': True,
                'detect_encodings': True
            }
        },

        'overview': {
            'token_settings': {
                'words': True,
                'lowercase': True,
                'uppercase': True,
                'title_case': True,
                'nums': True,
                'puncs': False,

                'treat_as_lowercase': True,
                'lemmatize_tokens': False,
                'filter_stop_words': False,

                'ignore_tags': True,
                'use_tags': False
            },

            'generation_settings': {
                'base_sttr': 1000
            },

            'table_settings': {
                'show_pct': True,
                'show_cumulative': False,
                'show_breakdown': True
            }
        },
    
        'concordancer': {
            'parallel_mode': False,
            'token_settings': {
                'puncs': False,

                'ignore_tags': True,
                'use_tags': False
            },
            
            'search_settings': {
                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            },

            'context_settings': {
                'inclusion': {
                    'inclusion': False,

                    'multi_search_mode': False,
                    'search_term': '',
                    'search_terms': [],

                    'ignore_case': True,
                    'match_inflected_forms': True,
                    'match_whole_words': True,
                    'use_regex': False,

                    'ignore_tags': True,
                    'match_tags': False,
                    
                    'context_window_sync': False,
                    'context_window_left': -5,
                    'context_window_right': 5
                },
                
                'exclusion': {
                    'exclusion': False,

                    'multi_search_mode': False,
                    'search_term': '',
                    'search_terms': [],

                    'ignore_case': True,
                    'match_inflected_forms': True,
                    'match_whole_words': True,
                    'use_regex': False,

                    'ignore_tags': True,
                    'match_tags': False,
                    
                    'context_window_sync': False,
                    'context_window_left': -5,
                    'context_window_right': 5
                }
            },
            
            'generation_settings': {
                'width_left_para': 0,
                'width_left_sentence': 0,
                'width_left_token': 5,
                'width_left_char': 50,
                'width_right_para': 0,
                'width_right_sentence': 0,
                'width_right_token': 5,
                'width_right_char': 50,
                'width_unit': main.tr('Token'),

                'sampling_method': main.tr('None'),
                'sample_size_first_n_lines': 100,
                'sample_size_systematic_fixed_interval': 2,
                'sample_size_systematic_fixed_size': 100,
                'sample_size_random': 100
            },

            'table_settings': {
                'show_pct': True
            },

            'fig_settings': {
                'sort_results_by': main.tr('File')
            },

            'zapping_settings': {
                'zapping': False,
                'replace_keywords_with': 15,
                'placeholder': '_',
                'add_line_nums': True,
                'discard_position_info': True,
                'randomize_outputs': True
            },

            'sort_results': {
                'sorting_rules': [
                    [main.tr('Node'), main.tr('Ascending')],
                    [main.tr('File'), main.tr('Ascending')],
                    [main.tr('Token No.'), main.tr('Ascending')]
                ],

                'highlight_colors': [
                    # Red
                    '#F00',
                    # Orange
                    '#C2691D',
                    # Yellow
                    '#CBBE00',
                    # Green
                    '#3F864C',
                    # Blue
                    '#264E8C',
                    # Purple
                    '#491D76'
                ]
            },

            'search_results': {
                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            }
        },

        'concordancer_parallel': {
            'parallel_mode': False,
            'token_settings': {
                'puncs': False,

                'ignore_tags': True,
                'use_tags': False
            },
            
            'search_settings': {
                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            },

            'context_settings': {
                'inclusion': {
                    'inclusion': False,

                    'multi_search_mode': False,
                    'search_term': '',
                    'search_terms': [],

                    'ignore_case': True,
                    'match_inflected_forms': True,
                    'match_whole_words': True,
                    'use_regex': False,

                    'ignore_tags': True,
                    'match_tags': False,
                    
                    'context_window_sync': False,
                    'context_window_left': -5,
                    'context_window_right': 5
                },
                
                'exclusion': {
                    'exclusion': False,

                    'multi_search_mode': False,
                    'search_term': '',
                    'search_terms': [],

                    'ignore_case': True,
                    'match_inflected_forms': True,
                    'match_whole_words': True,
                    'use_regex': False,

                    'ignore_tags': True,
                    'match_tags': False,
                    
                    'context_window_sync': False,
                    'context_window_left': -5,
                    'context_window_right': 5
                }
            },
            
            'generation_settings': {
                'src_file': '',
                'tgt_file': '',

                'sampling_method': main.tr('None'),
                'sample_size_first_n_lines': 100,
                'sample_size_systematic_fixed_interval': 2,
                'sample_size_systematic_fixed_size': 100,
                'sample_size_random': 100
            },

            'table_settings': {
                'show_pct': True
            },

            'sort_results': {
                'sorting_rules': [
                    [main.tr('Node'), main.tr('Ascending')],
                    [main.tr('Segment No.'), main.tr('Ascending')]
                ],

                'highlight_colors': [
                    # Red
                    '#F00',
                    # Orange
                    '#C2691D',
                    # Yellow
                    '#CBBE00',
                    # Green
                    '#3F864C',
                    # Blue
                    '#264E8C',
                    # Purple
                    '#491D76'
                ]
            },

            'search_results': {
                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            }
        },
    
        'wordlist': {
            'token_settings': {
                'words': True,
                'lowercase': True,
                'uppercase': True,
                'title_case': True,
                'nums': True,
                'puncs': False,

                'treat_as_lowercase': True,
                'lemmatize_tokens': False,
                'filter_stop_words': False,

                'ignore_tags': True,
                'use_tags': False
            },

            'generation_settings': {
                'measure_dispersion': main.tr("Juilland's D"),
                'measure_adjusted_freq': main.tr("Juilland's U")
            },

            'table_settings': {
                'show_pct': True,
                'show_cumulative': False,
                'show_breakdown': True
            },

            'fig_settings': {
                'graph_type': main.tr('Line Chart'),
                'use_file': main.tr('Total'),
                'use_data': main.tr('Frequency'),
                'use_pct': False,
                'use_cumulative': False,

                'rank_min': 1,
                'rank_min_no_limit': True,
                'rank_max': 50,
                'rank_max_no_limit': False,
            },

            'filter_results': {
                'file_to_filter': main.tr('Total'),

                'freq_min': 0,
                'freq_min_no_limit': True,
                'freq_max': 1000,
                'freq_max_no_limit': True,

                'dispersion_min': -100,
                'dispersion_min_no_limit': True,
                'dispersion_max': 100,
                'dispersion_max_no_limit': True,

                'adjusted_freq_min': 0,
                'adjusted_freq_min_no_limit': True,
                'adjusted_freq_max': 1000,
                'adjusted_freq_max_no_limit': True,

                'len_token_min': 1,
                'len_token_min_no_limit': True,
                'len_token_max': 20,
                'len_token_max_no_limit': True,

                'num_files_found_min': 1,
                'num_files_found_min_no_limit': True,
                'num_files_found_max': 100,
                'num_files_found_max_no_limit': True
            },

            'search_results': {
                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            }
        },
    
        'ngram': {
            'token_settings': {
                'words': True,
                'lowercase': True,
                'uppercase': True,
                'title_case': True,
                'nums': True,
                'puncs': False,

                'treat_as_lowercase': True,
                'lemmatize_tokens': False,
                'filter_stop_words': False,

                'ignore_tags': True,
                'use_tags': False
            },

            'search_settings': {
                'search_settings': True,

                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False,

                'search_term_position_min': 1,
                'search_term_position_min_no_limit': True,
                'search_term_position_max': 2,
                'search_term_position_max_no_limit': True,
                'allow_skipped_tokens_within_search_terms': True
            },

            'context_settings': {
                'inclusion': {
                    'inclusion': False,

                    'multi_search_mode': False,
                    'search_term': '',
                    'search_terms': [],

                    'ignore_case': True,
                    'match_inflected_forms': True,
                    'match_whole_words': True,
                    'use_regex': False,

                    'ignore_tags': True,
                    'match_tags': False,
                    
                    'context_window_sync': False,
                    'context_window_left': -5,
                    'context_window_right': 5
                },
                
                'exclusion': {
                    'exclusion': False,

                    'multi_search_mode': False,
                    'search_term': '',
                    'search_terms': [],

                    'ignore_case': True,
                    'match_inflected_forms': True,
                    'match_whole_words': True,
                    'use_regex': False,

                    'ignore_tags': True,
                    'match_tags': False,
                    
                    'context_window_sync': False,
                    'context_window_left': -5,
                    'context_window_right': 5
                }
            },
            
            'generation_settings': {
                'ngram_size_sync': False,
                'ngram_size_min': 2,
                'ngram_size_max': 2,
                'allow_skipped_tokens': False,
                'allow_skipped_tokens_num': 1,

                'measure_dispersion': main.tr("Juilland's D"),
                'measure_adjusted_freq': main.tr("Juilland's U")
            },

            'table_settings': {
                'show_pct': True,
                'show_cumulative': False,
                'show_breakdown': True
            },

            'fig_settings': {
                'graph_type': main.tr('Line Chart'),
                'use_file': main.tr('Total'),
                'use_data': main.tr('Frequency'),
                'use_pct': False,
                'use_cumulative': False,

                'rank_min': 1,
                'rank_min_no_limit': True,
                'rank_max': 50,
                'rank_max_no_limit': False,
            },

            'filter_results': {
                'file_to_filter': main.tr('Total'),

                'len_ngram_min': 1,
                'len_ngram_min_no_limit': True,
                'len_ngram_max': 20,
                'len_ngram_max_no_limit': True,

                'freq_min': 0,
                'freq_min_no_limit': True,
                'freq_max': 1000,
                'freq_max_no_limit': True,

                'dispersion_min': -100,
                'dispersion_min_no_limit': True,
                'dispersion_max': 100,
                'dispersion_max_no_limit': True,

                'adjusted_freq_min': 0,
                'adjusted_freq_min_no_limit': True,
                'adjusted_freq_max': 1000,
                'adjusted_freq_max_no_limit': True,

                'num_files_found_min': 1,
                'num_files_found_min_no_limit': True,
                'num_files_found_max': 100,
                'num_files_found_max_no_limit': True
            },

            'search_results': {
                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            }
        },

        'collocation': {
            'token_settings': {
                'words': True,
                'lowercase': True,
                'uppercase': True,
                'title_case': True,
                'nums': True,
                'puncs': False,

                'treat_as_lowercase': True,
                'lemmatize_tokens': False,
                'filter_stop_words': False,

                'ignore_tags': True,
                'use_tags': False
            },
            
            'search_settings': {
                'search_settings': True,

                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            },

            'context_settings': {
                'inclusion': {
                    'inclusion': False,

                    'multi_search_mode': False,
                    'search_term': '',
                    'search_terms': [],

                    'ignore_case': True,
                    'match_inflected_forms': True,
                    'match_whole_words': True,
                    'use_regex': False,

                    'ignore_tags': True,
                    'match_tags': False,
                    
                    'context_window_sync': False,
                    'context_window_left': -5,
                    'context_window_right': 5
                },
                
                'exclusion': {
                    'exclusion': False,

                    'multi_search_mode': False,
                    'search_term': '',
                    'search_terms': [],

                    'ignore_case': True,
                    'match_inflected_forms': True,
                    'match_whole_words': True,
                    'use_regex': False,

                    'ignore_tags': True,
                    'match_tags': False,
                    
                    'context_window_sync': False,
                    'context_window_left': -5,
                    'context_window_right': 5
                }
            },
            
            'generation_settings': {
                'window_sync': False,
                'window_left': -5,
                'window_right': 5,

                'limit_searching': main.tr('None'),

                'test_significance': main.tr("Pearson's Chi-squared Test"),
                'measure_effect_size': main.tr('Pointwise Mutual Information'),
            },

            'table_settings': {
                'show_pct': True,
                'show_cumulative': False,
                'show_breakdown_position': True,
                'show_breakdown_file': True
            },

            'fig_settings': {
                'graph_type': main.tr('Line Chart'),
                'use_file': main.tr('Total'),
                'use_data': main.tr('p-value'),
                'use_pct': False,
                'use_cumulative': False,

                'rank_min': 1,
                'rank_min_no_limit': True,
                'rank_max': 50,
                'rank_max_no_limit': False
            },

            'filter_results': {
                'file_to_filter': main.tr('Total'),

                'len_collocate_min': 1,
                'len_collocate_min_no_limit': True,
                'len_collocate_max': 20,
                'len_collocate_max_no_limit': True,

                'freq_position': main.tr('Total'),
                'freq_min': 0,
                'freq_min_no_limit': True,
                'freq_max': 1000,
                'freq_max_no_limit': True,

                'test_stat_min': -100,
                'test_stat_min_no_limit': True,
                'test_stat_max': 100,
                'test_stat_max_no_limit': True,

                'p_value_min': 0,
                'p_value_min_no_limit': True,
                'p_value_max': 0.05,
                'p_value_max_no_limit': True,

                'bayes_factor_min': -100,
                'bayes_factor_min_no_limit': True,
                'bayes_factor_max': 100,
                'bayes_factor_max_no_limit': True,

                'effect_size_min': -100,
                'effect_size_min_no_limit': True,
                'effect_size_max': 100,
                'effect_size_max_no_limit': True,

                'num_files_found_min': 1,
                'num_files_found_min_no_limit': True,
                'num_files_found_max': 100,
                'num_files_found_max_no_limit': True
            },

            'search_results': {
                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            }
        },

        'colligation': {
            'token_settings': {
                'words': True,
                'lowercase': True,
                'uppercase': True,
                'title_case': True,
                'nums': True,
                'puncs': False,

                'treat_as_lowercase': True,
                'lemmatize_tokens': False,
                'filter_stop_words': False,

                'ignore_tags': True,
                'use_tags': False
            },

            'search_settings': {
                'search_settings': True,

                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            },

            'context_settings': {
                'inclusion': {
                    'inclusion': False,

                    'multi_search_mode': False,
                    'search_term': '',
                    'search_terms': [],

                    'ignore_case': True,
                    'match_inflected_forms': False,
                    'match_whole_words': True,
                    'use_regex': False,

                    'ignore_tags': True,
                    'match_tags': False,
                    
                    'context_window_sync': False,
                    'context_window_left': -5,
                    'context_window_right': 5
                },
                
                'exclusion': {
                    'exclusion': False,

                    'multi_search_mode': False,
                    'search_term': '',
                    'search_terms': [],

                    'ignore_case': True,
                    'match_inflected_forms': False,
                    'match_whole_words': True,
                    'use_regex': False,

                    'ignore_tags': True,
                    'match_tags': False,
                    
                    'context_window_sync': False,
                    'context_window_left': -5,
                    'context_window_right': 5
                }
            },
            
            'generation_settings': {
                'window_sync': False,
                'window_left': -5,
                'window_right': 5,

                'limit_searching': main.tr('None'),

                'test_significance': main.tr("Pearson's Chi-squared Test"),
                'measure_effect_size': main.tr('Pointwise Mutual Information')
            },

            'table_settings': {
                'show_pct': True,
                'show_cumulative': False,
                'show_breakdown_position': True,
                'show_breakdown_file': True
            },

            'fig_settings': {
                'graph_type': main.tr('Line Chart'),
                'use_file': main.tr('Total'),
                'use_data': main.tr('p-value'),
                'use_pct': False,
                'use_cumulative': False,

                'rank_min': 1,
                'rank_min_no_limit': True,
                'rank_max': 50,
                'rank_max_no_limit': False
            },

            'filter_results': {
                'file_to_filter': main.tr('Total'),

                'len_collocate_min': 1,
                'len_collocate_min_no_limit': True,
                'len_collocate_max': 20,
                'len_collocate_max_no_limit': True,

                'freq_position': main.tr('Total'),
                'freq_min': 0,
                'freq_min_no_limit': True,
                'freq_max': 1000,
                'freq_max_no_limit': True,

                'test_stat_min': -100,
                'test_stat_min_no_limit': True,
                'test_stat_max': 100,
                'test_stat_max_no_limit': True,

                'p_value_min': 0,
                'p_value_min_no_limit': True,
                'p_value_max': 0.05,
                'p_value_max_no_limit': True,

                'bayes_factor_min': -100,
                'bayes_factor_min_no_limit': True,
                'bayes_factor_max': 100,
                'bayes_factor_max_no_limit': True,

                'effect_size_min': -100,
                'effect_size_min_no_limit': True,
                'effect_size_max': 100,
                'effect_size_max_no_limit': True,

                'num_files_found_min': 1,
                'num_files_found_min_no_limit': True,
                'num_files_found_max': 100,
                'num_files_found_max_no_limit': True
            },

            'search_results': {
                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            },
        },

        'keyword': {
            'token_settings': {
                'words': True,
                'lowercase': True,
                'uppercase': True,
                'title_case': True,
                'nums': True,
                'puncs': False,

                'treat_as_lowercase': True,
                'lemmatize_tokens': False,
                'filter_stop_words': False,

                'ignore_tags': True,
                'use_tags': False
            },

            'generation_settings': {
                'ref_files': [],
                'test_significance': main.tr('Log-likelihood Ratio Test'),
                'measure_effect_size': main.tr("Kilgarriff's Ratio"),
            },
            
            'table_settings': {
                'show_pct': True,
                'show_cumulative': False,
                'show_breakdown': True
            },

            'fig_settings': {
                'graph_type': main.tr('Line Chart'),
                'use_file': main.tr('Total'),
                'use_data': main.tr('p-value'),
                'use_pct': False,
                'use_cumulative': False,

                'rank_min': 1,
                'rank_min_no_limit': True,
                'rank_max': 50,
                'rank_max_no_limit': False
            },

            'filter_results': {
                'file_to_filter': main.tr('Total'),

                'len_keyword_min': 1,
                'len_keyword_min_no_limit': True,
                'len_keyword_max': 20,
                'len_keyword_max_no_limit': True,

                'freq_min': 0,
                'freq_min_no_limit': True,
                'freq_max': 1000,
                'freq_max_no_limit': True,

                'test_stat_min': -100,
                'test_stat_min_no_limit': True,
                'test_stat_max': 100,
                'test_stat_max_no_limit': True,

                'p_value_min': 0,
                'p_value_min_no_limit': True,
                'p_value_max': 0.05,
                'p_value_max_no_limit': True,

                'bayes_factor_min': -100,
                'bayes_factor_min_no_limit': True,
                'bayes_factor_max': 100,
                'bayes_factor_max_no_limit': True,

                'effect_size_min': -100,
                'effect_size_min_no_limit': True,
                'effect_size_max': 100,
                'effect_size_max_no_limit': True,

                'num_files_found_min': 1,
                'num_files_found_min_no_limit': True,
                'num_files_found_max': 100,
                'num_files_found_max_no_limit': True
            },

            'search_results': {
                'multi_search_mode': False,
                'search_term': '',
                'search_terms': [],

                'ignore_case': True,
                'match_inflected_forms': True,
                'match_whole_words': True,
                'use_regex': False,

                'ignore_tags': True,
                'match_tags': False
            }
        },

        'menu': {
            'prefs': {
                'show_status_bar': True
            },

            'help': {
                'citing': {
                    'citation_sys': main.tr('APA (7th Edition)')
                },

                'acks': {
                    'browse_category': main.tr('General')
                },

                'donating': {
                    'donating_via': main.tr('PayPal')
                }
            }
        },

        'settings': {
            'tab': 'General'
        },

        'general': {
            'font_settings': {
                'font_family': 'Arial',
                'font_size': 14
            },

            'update_settings': {
                'check_updates_on_startup': True
            },

            'misc': {
                'confirm_on_exit': True
            }
        },

        'import': {
            'files': {
                'default_path': wl_misc.get_normalized_path('.')
            },

            'search_terms': {
                'default_path': wl_misc.get_normalized_path('.'),
                'default_encoding': 'utf_8',
                'detect_encodings': True
            },

            'stop_words': {
                'default_path': wl_misc.get_normalized_path('.'),
                'default_encoding': 'utf_8',
                'detect_encodings': True
            },

            'temp_files': {
                'default_path': wl_misc.get_normalized_path('Import/'),
            }
        },

        'export': {
            'tables': {
                'default_path': wl_misc.get_normalized_path('Export/'),
                'default_type': main.tr('Excel Workbook (*.xlsx)'),
                'default_encoding': 'utf_8'
            },

            'search_terms': {
                'default_path': wl_misc.get_normalized_path('Export/'),
                'default_encoding': 'utf_8'
            },

            'stop_words': {
                'default_path': wl_misc.get_normalized_path('Export/'),
                'default_encoding': 'utf_8'
            }
        },

        'files': {
            'default_settings': {
                'lang': 'eng',
                'tokenized': main.tr('No'),
                'tagged': main.tr('No'),
                'encoding': 'utf_8'
            },

            'auto_detection_settings': {
                'number_lines': 100,
                'number_lines_no_limit': False
            },

            'misc': {
                'read_files_in_chunks': 100
            }
        },

        'tags': {
            'tags_header': [
                ['Non-embedded', 'Header', '<teiHeader>', '</teiHeader>'],
                ['Non-embedded', 'Header', '<header>', '</header>']
            ],

            'tags_body': [
                ['Embedded', 'Part of Speech', '_', ''],
                ['Non-embedded', 'Others', '<*>', '</*>']
            ],

            'tags_xml': [
                ['Non-embedded', 'Paragraph', '<p>', '</p>'],
                ['Non-embedded', 'Sentence', '<s>', '</s>'],
                ['Non-embedded', 'Word', '<w>', '</w>']
            ]
        },

        'data': {
            'continue_numbering_after_ties': False,
            
            'precision_decimal': 2,
            'precision_pct': 2,
            'precision_p_value': 5
        },

        'sentence_tokenization': {
            'sentence_tokenizers': {
                'afr': main.tr('spaCy - Sentencizer'),
                'sqi': main.tr('spaCy - Sentencizer'),
                'amh': main.tr('spaCy - Sentencizer'),
                'ara': main.tr('spaCy - Sentencizer'),
                'hye': main.tr('spaCy - Sentencizer'),
                'aze': main.tr('spaCy - Sentencizer'),
                'eus': main.tr('spaCy - Sentencizer'),
                'ben': main.tr('spaCy - Sentencizer'),
                'bul': main.tr('spaCy - Sentencizer'),
                'cat': main.tr('spaCy - Sentencizer'),
                'zho_cn': main.tr('spaCy - Sentence Recognizer'),
                'zho_tw': main.tr('spaCy - Sentence Recognizer'),
                'hrv': main.tr('spaCy - Sentencizer'),
                'ces': main.tr('NLTK - Punkt Sentence Tokenizer'),
                'dan': main.tr('spaCy - Sentence Recognizer'),
                'nld': main.tr('spaCy - Sentence Recognizer'),
                'eng': main.tr('spaCy - Sentence Recognizer'),
                'est': main.tr('NLTK - Punkt Sentence Tokenizer'),
                'fin': main.tr('NLTK - Punkt Sentence Tokenizer'),
                'fra': main.tr('spaCy - Sentence Recognizer'),
                'deu': main.tr('spaCy - Sentence Recognizer'),
                'grc': main.tr('spaCy - Sentencizer'),
                'ell': main.tr('spaCy - Sentence Recognizer'),
                'guj': main.tr('spaCy - Sentencizer'),
                'heb': main.tr('spaCy - Sentencizer'),
                'hin': main.tr('spaCy - Sentencizer'),
                'hun': main.tr('spaCy - Sentencizer'),
                'isl': main.tr('Tokenizer - Icelandic Sentence Tokenizer'),
                'ind': main.tr('spaCy - Sentencizer'),
                'gle': main.tr('spaCy - Sentencizer'),
                'ita': main.tr('spaCy - Sentence Recognizer'),
                'jpn': main.tr('Wordless - Japanese Sentence Tokenizer'),
                'kan': main.tr('spaCy - Sentencizer'),
                'kir': main.tr('spaCy - Sentencizer'),
                'lav': main.tr('spaCy - Sentencizer'),
                'lij': main.tr('spaCy - Sentence Recognizer'),
                'lit': main.tr('spaCy - Sentencizer'),
                'ltz': main.tr('spaCy - Sentencizer'),
                'mkd': main.tr('spaCy - Sentencizer'),
                'mal': main.tr('spaCy - Sentencizer'),
                'mar': main.tr('spaCy - Sentencizer'),
                'nep': main.tr('spaCy - Sentencizer'),
                'nob': main.tr('spaCy - Sentence Recognizer'),
                'nno': main.tr('NLTK - Punkt Sentence Tokenizer'),
                'fas': main.tr('spaCy - Sentencizer'),
                'pol': main.tr('spaCy - Sentence Recognizer'),
                'por': main.tr('spaCy - Sentence Recognizer'),
                'ron': main.tr('spaCy - Sentence Recognizer'),
                'rus': main.tr('spaCy - Sentence Recognizer'),
                'san': main.tr('spaCy - Sentencizer'),
                'srp_cyrl': main.tr('spaCy - Sentencizer'),
                'srp_latn': main.tr('spaCy - Sentencizer'),
                'sin': main.tr('spaCy - Sentencizer'),
                'slk': main.tr('spaCy - Sentencizer'),
                'slv': main.tr('NLTK - Punkt Sentence Tokenizer'),
                'spa': main.tr('spaCy - Sentence Recognizer'),
                'swe': main.tr('NLTK - Punkt Sentence Tokenizer'),
                'tgl': main.tr('spaCy - Sentencizer'),
                'tam': main.tr('spaCy - Sentencizer'),
                'tat': main.tr('spaCy - Sentencizer'),
                'tel': main.tr('spaCy - Sentencizer'),
                'tha': main.tr('PyThaiNLP - CRFCut'),
                'bod': main.tr('botok - Tibetan Sentence Tokenizer'),
                'tir': main.tr('spaCy - Sentencizer'),
                'tsn': main.tr('spaCy - Sentencizer'),
                'tur': main.tr('NLTK - Punkt Sentence Tokenizer'),
                'ukr': main.tr('spaCy - Sentencizer'),
                'urd': main.tr('spaCy - Sentencizer'),
                'vie': main.tr('Underthesea - Vietnamese Sentence Tokenizer'),
                'yor': main.tr('spaCy - Sentencizer'),

                'other': main.tr('spaCy - Sentence Recognizer')
            },

            'preview_lang': 'eng',
            'preview_samples': '',
            'preview_results': ''
        },

        'word_tokenization': {
            'word_tokenizers': {
                'afr': main.tr('spaCy - Afrikaans Word Tokenizer'),
                'sqi': main.tr('spaCy - Albanian Word Tokenizer'),
                'amh': main.tr('spaCy - Amharic Word Tokenizer'),
                'ara': main.tr('spaCy - Arabic Word Tokenizer'),
                'hye': main.tr('spaCy - Armenian Word Tokenizer'),
                'asm': main.tr('Sacremoses - Moses Tokenizer'),
                'aze': main.tr('spaCy - Azerbaijani Word Tokenizer'),
                'eus': main.tr('spaCy - Basque Word Tokenizer'),
                'ben': main.tr('spaCy - Bengali Word Tokenizer'),
                'bul': main.tr('spaCy - Bulgarian Word Tokenizer'),
                'cat': main.tr('spaCy - Catalan Word Tokenizer'),
                'zho_cn': main.tr('spaCy - Chinese Word Tokenizer'),
                'zho_tw': main.tr('spaCy - Chinese Word Tokenizer'),
                'hrv': main.tr('spaCy - Croatian Word Tokenizer'),
                'ces': main.tr('spaCy - Czech Word Tokenizer'),
                'dan': main.tr('spaCy - Danish Word Tokenizer'),
                'nld': main.tr('spaCy - Dutch Word Tokenizer'),
                'eng': main.tr('spaCy - English Word Tokenizer'),
                'est': main.tr('spaCy - Estonian Word Tokenizer'),
                'fin': main.tr('spaCy - Finnish Word Tokenizer'),
                'fra': main.tr('spaCy - French Word Tokenizer'),
                'deu': main.tr('spaCy - German Word Tokenizer'),
                'grc': main.tr('spaCy - Greek (Ancient) Word Tokenizer'),
                'ell': main.tr('spaCy - Greek (Modern) Word Tokenizer'),
                'guj': main.tr('spaCy - Gujarati Word Tokenizer'),
                'heb': main.tr('spaCy - Hebrew Word Tokenizer'),
                'hin': main.tr('spaCy - Hindi Word Tokenizer'),
                'hun': main.tr('spaCy - Hungarian Word Tokenizer'),
                'isl': main.tr('Tokenizer - Icelandic Word Tokenizer'),
                'ind': main.tr('spaCy - Indonesian Word Tokenizer'),
                'gle': main.tr('spaCy - Irish Word Tokenizer'),
                'ita': main.tr('spaCy - Italian Word Tokenizer'),
                'jpn': main.tr('nagisa - Japanese Word Tokenizer'),
                'kan': main.tr('spaCy - Kannada Word Tokenizer'),
                'kir': main.tr('spaCy - Kyrgyz Word Tokenizer'),
                'lav': main.tr('spaCy - Latvian Word Tokenizer'),
                'lij': main.tr('spaCy - Ligurian Word Tokenizer'),
                'lit': main.tr('spaCy - Lithuanian Word Tokenizer'),
                'ltz': main.tr('spaCy - Luxembourgish Word Tokenizer'),
                'mkd': main.tr('spaCy - Macedonian Word Tokenizer'),
                'mal': main.tr('spaCy - Malayalam Word Tokenizer'),
                'mar': main.tr('spaCy - Marathi Word Tokenizer'),
                'mni': main.tr('Sacremoses - Moses Tokenizer'),
                'nep': main.tr('spaCy - Nepali Word Tokenizer'),
                'nob': main.tr('spaCy - Norwegian Bokmål Word Tokenizer'),
                'ori': main.tr('Sacremoses - Moses Tokenizer'),
                'fas': main.tr('spaCy - Persian Word Tokenizer'),
                'pol': main.tr('spaCy - Polish Word Tokenizer'),
                'por': main.tr('spaCy - Portuguese Word Tokenizer'),
                'pan': main.tr('Sacremoses - Moses Tokenizer'),
                'ron': main.tr('spaCy - Romanian Word Tokenizer'),
                'rus': main.tr('razdel - Russian Word Tokenizer'),
                'san': main.tr('spaCy - Sanskrit Word Tokenizer'),
                'srp_cyrl': main.tr('spaCy - Serbian Word Tokenizer'),
                'srp_latn': main.tr('spaCy - Serbian Word Tokenizer'),
                'sin': main.tr('spaCy - Sinhala Word Tokenizer'),
                'slk': main.tr('spaCy - Slovak Word Tokenizer'),
                'slv': main.tr('spaCy - Slovenian Word Tokenizer'),
                'spa': main.tr('spaCy - Spanish Word Tokenizer'),
                'swe': main.tr('spaCy - Swedish Word Tokenizer'),
                'tgl': main.tr('spaCy - Tagalog Word Tokenizer'),
                'tgk': main.tr('NLTK - Tok-tok Tokenizer'),
                'tam': main.tr('spaCy - Tamil Word Tokenizer'),
                'tat': main.tr('spaCy - Tatar Word Tokenizer'),
                'tel': main.tr('spaCy - Telugu Word Tokenizer'),
                'tdt': main.tr('Sacremoses - Moses Tokenizer'),
                'tha': main.tr('PyThaiNLP - Maximum Matching + TCC'),
                'bod': main.tr('botok - Tibetan Word Tokenizer'),
                'tir': main.tr('spaCy - Tigrinya Word Tokenizer'),
                'tsn': main.tr('spaCy - Tswana Word Tokenizer'),
                'tur': main.tr('spaCy - Turkish Word Tokenizer'),
                'ukr': main.tr('spaCy - Ukrainian Word Tokenizer'),
                'urd': main.tr('spaCy - Urdu Word Tokenizer'),
                'vie': main.tr('Underthesea - Vietnamese Word Tokenizer'),
                'yor': main.tr('spaCy - Yoruba Word Tokenizer'),

                'other': main.tr('spaCy - English Word Tokenizer')
            },

            'preview_lang': 'eng',
            'preview_samples': '',
            'preview_results': ''
        },

        'word_detokenization': {
            'word_detokenizers': {
                'asm': main.tr('Sacremoses - Moses Detokenizer'),
                'ben': main.tr('Sacremoses - Moses Detokenizer'),
                'cat': main.tr('Sacremoses - Moses Detokenizer'),
                'zho_cn': main.tr('Wordless - Chinese Word Detokenizer'),
                'zho_tw': main.tr('Wordless - Chinese Word Detokenizer'),
                'ces': main.tr('Sacremoses - Moses Detokenizer'),
                'nld': main.tr('Sacremoses - Moses Detokenizer'),
                'eng': main.tr('Sacremoses - Moses Detokenizer'),
                'est': main.tr('Sacremoses - Moses Detokenizer'),
                'fin': main.tr('Sacremoses - Moses Detokenizer'),
                'fra': main.tr('Sacremoses - Moses Detokenizer'),
                'deu': main.tr('Sacremoses - Moses Detokenizer'),
                'ell': main.tr('Sacremoses - Moses Detokenizer'),
                'guj': main.tr('Sacremoses - Moses Detokenizer'),
                'hin': main.tr('Sacremoses - Moses Detokenizer'),
                'hun': main.tr('Sacremoses - Moses Detokenizer'),
                'isl': main.tr('Sacremoses - Moses Detokenizer'),
                'gle': main.tr('Sacremoses - Moses Detokenizer'),
                'ita': main.tr('Sacremoses - Moses Detokenizer'),
                'jpn': main.tr('Wordless - Japanese Word Detokenizer'),
                'kan': main.tr('Sacremoses - Moses Detokenizer'),
                'lav': main.tr('Sacremoses - Moses Detokenizer'),
                'lit': main.tr('Sacremoses - Moses Detokenizer'),
                'mal': main.tr('Sacremoses - Moses Detokenizer'),
                'mar': main.tr('Sacremoses - Moses Detokenizer'),
                'mni': main.tr('Sacremoses - Moses Detokenizer'),
                'ori': main.tr('Sacremoses - Moses Detokenizer'),
                'pol': main.tr('Sacremoses - Moses Detokenizer'),
                'por': main.tr('Sacremoses - Moses Detokenizer'),
                'pan': main.tr('Sacremoses - Moses Detokenizer'),
                'ron': main.tr('Sacremoses - Moses Detokenizer'),
                'rus': main.tr('Sacremoses - Moses Detokenizer'),
                'slk': main.tr('Sacremoses - Moses Detokenizer'),
                'slv': main.tr('Sacremoses - Moses Detokenizer'),
                'spa': main.tr('Sacremoses - Moses Detokenizer'),
                'swe': main.tr('Sacremoses - Moses Detokenizer'),
                'tam': main.tr('Sacremoses - Moses Detokenizer'),
                'tel': main.tr('Sacremoses - Moses Detokenizer'),
                'tdt': main.tr('Sacremoses - Moses Detokenizer'),
                'tha': main.tr('Wordless - Thai Word Detokenizer'),
                'bod': main.tr('Wordless - Tibetan Word Detokenizer'),

                'other': main.tr('Sacremoses - Moses Detokenizer')
            },

            'preview_lang': 'eng',
            'preview_samples': '',
            'preview_results': ''
        },

        'pos_tagging': {
            'pos_taggers': {
                'cat': main.tr('spaCy - Catalan POS Tagger'),
                'zho_cn': main.tr('spaCy - Chinese POS Tagger'),
                'zho_tw': main.tr('spaCy - Chinese POS Tagger'),
                'dan': main.tr('spaCy - Danish POS Tagger'),
                'nld': main.tr('spaCy - Dutch POS Tagger'),
                'eng': main.tr('spaCy - English POS Tagger'),
                'fra': main.tr('spaCy - French POS Tagger'),
                'deu': main.tr('spaCy - German POS Tagger'),
                'ell': main.tr('spaCy - Greek (Modern) POS Tagger'),
                'ita': main.tr('spaCy - Italian POS Tagger'),
                'jpn': main.tr('nagisa - Japanese POS Tagger'),
                'lit': main.tr('spaCy - Lithuanian POS Tagger'),
                'mkd': main.tr('spaCy - Macedonian POS Tagger'),
                'nob': main.tr('spaCy - Norwegian Bokmål POS Tagger'),
                'pol': main.tr('spaCy - Polish POS Tagger'),
                'por': main.tr('spaCy - Portuguese POS Tagger'),
                'ron': main.tr('spaCy - Romanian POS Tagger'),
                'rus': main.tr('spaCy - Russian POS Tagger'),
                'spa': main.tr('spaCy - Spanish POS Tagger'),
                'tha': main.tr('PyThaiNLP - Perceptron Tagger (PUD)'),
                'bod': main.tr('botok - Tibetan POS Tagger'),
                'ukr': main.tr('pymorphy2 - Morphological Analyzer'),
                'vie': main.tr('Underthesea - Vietnamese POS Tagger')
            },

            'to_universal_pos_tags': False,

            'preview_lang': 'eng',
            'preview_samples': '',
            'preview_results': ''
        },

        'tagsets': {
            'preview_lang': 'eng',

            'preview_pos_tagger': {
                'cat': main.tr('spaCy - Catalan POS Tagger'),
                'zho_cn': main.tr('spaCy - Chinese POS Tagger'),
                'zho_tw': main.tr('spaCy - Chinese POS Tagger'),
                'dan': main.tr('spaCy - Danish POS Tagger'),
                'nld': main.tr('spaCy - Dutch POS Tagger'),
                'eng': main.tr('spaCy - English POS Tagger'),
                'fra': main.tr('spaCy - French POS Tagger'),
                'deu': main.tr('spaCy - German POS Tagger'),
                'ell': main.tr('spaCy - Greek (Modern) POS Tagger'),
                'ita': main.tr('spaCy - Italian POS Tagger'),
                'jpn': main.tr('nagisa - Japanese POS Tagger'),
                'lit': main.tr('spaCy - Lithuanian POS Tagger'),
                'mkd': main.tr('spaCy - Macedonian POS Tagger'),
                'nob': main.tr('spaCy - Norwegian Bokmål POS Tagger'),
                'pol': main.tr('spaCy - Polish POS Tagger'),
                'por': main.tr('spaCy - Portuguese POS Tagger'),
                'ron': main.tr('spaCy - Romanian POS Tagger'),
                'rus': main.tr('spaCy - Russian POS Tagger'),
                'spa': main.tr('spaCy - Spanish POS Tagger'),
                'tha': main.tr('PyThaiNLP - Perceptron Tagger (PUD)'),
                'bod': main.tr('botok - Tibetan POS Tagger'),
                'ukr': main.tr('pymorphy2 - Morphological Analyzer'),
                'vie': main.tr('Underthesea - Vietnamese POS Tagger')
            },

            'mappings': {
                'zho_cn': {
                    main.tr('jieba - Chinese POS Tagger'): wl_tagset_zho_jieba.MAPPINGS
                },

                'zho_tw': {
                    main.tr('jieba - Chinese POS Tagger'): wl_tagset_zho_jieba.MAPPINGS
                },

                'eng': {
                    main.tr('NLTK - Perceptron POS Tagger'): wl_tagset_eng_penn_treebank.MAPPINGS,
                },

                'jpn': {
                    main.tr('nagisa - Japanese POS Tagger'): wl_tagset_jpn_unidic.MAPPINGS
                },

                'rus': {
                    main.tr('NLTK - Perceptron POS Tagger'): wl_tagset_rus_russian_national_corpus.MAPPINGS,
                    main.tr('pymorphy2 - Morphological Analyzer'): wl_tagset_rus_open_corpora.MAPPINGS
                },

                'tha': {
                    main.tr('PyThaiNLP - Perceptron Tagger (LST20)'): wl_tagset_tha_lst20.MAPPINGS,
                    main.tr('PyThaiNLP - Perceptron Tagger (ORCHID)'): wl_tagset_tha_orchid.MAPPINGS,
                    main.tr('PyThaiNLP - Perceptron Tagger (PUD)'): wl_tagset_universal.MAPPINGS
                },

                'bod': {
                    main.tr('botok - Tibetan POS Tagger'): wl_tagset_bod_botok.MAPPINGS
                },

                'ukr': {
                    main.tr('pymorphy2 - Morphological Analyzer'): wl_tagset_rus_open_corpora.MAPPINGS
                },

                'vie': {
                    main.tr('Underthesea - Vietnamese POS Tagger'): wl_tagset_vie_underthesea.MAPPINGS
                }
            }
        },

        'lemmatization': {
            'lemmatizers': {
                'ast': main.tr('Lemmatization Lists - Asturian Lemma List'),
                'ben': main.tr('spaCy - Bengali Lemmatizer'),
                'bul': main.tr('Lemmatization Lists - Bulgarian Lemma List'),
                'cat': main.tr('spaCy - Catalan Lemmatizer'),
                'hrv': main.tr('spaCy - Croatian Lemmatizer'),
                'ces': main.tr('spaCy - Czech Lemmatizer'),
                'dan': main.tr('spaCy - Danish Lemmatizer'),
                'nld': main.tr('spaCy - Dutch Lemmatizer'),
                'eng': main.tr('spaCy - English Lemmatizer'),
                'est': main.tr('Lemmatization Lists - Estonian Lemma List'),
                'fra': main.tr('spaCy - French Lemmatizer'),
                'glg': main.tr('Lemmatization Lists - Galician Lemma List'),
                'deu': main.tr('spaCy - German Lemmatizer'),
                'grc': main.tr('lemmalist-greek - Greek (Ancient) Lemma List'),
                'ell': main.tr('spaCy - Greek (Modern) Lemmatizer'),
                'hun': main.tr('spaCy - Hungarian Lemmatizer'),
                'ind': main.tr('spaCy - Indonesian Lemmatizer'),
                'gle': main.tr('Lemmatization Lists - Irish Lemma List'),
                'ita': main.tr('spaCy - Italian Lemmatizer'),
                'lit': main.tr('spaCy - Lithuanian Lemmatizer'),
                'ltz': main.tr('spaCy - Luxembourgish Lemmatizer'),
                'mkd': main.tr('spaCy - Macedonian Lemmatizer'),
                'glv': main.tr('Lemmatization Lists - Manx Lemma List'),
                'nob': main.tr('spaCy - Norwegian Bokmål Lemmatizer'),
                'fas': main.tr('spaCy - Persian Lemmatizer'),
                'pol': main.tr('spaCy - Polish Lemmatizer'),
                'por': main.tr('spaCy - Portuguese Lemmatizer'),
                'ron': main.tr('spaCy - Romanian Lemmatizer'),
                'rus': main.tr('spaCy - Russian Lemmatizer'),
                'gla': main.tr('Lemmatization Lists - Scottish Gaelic Lemma List'),
                'srp_cyrl': main.tr('spaCy - Serbian (Cyrillic) Lemmatizer'),
                'slk': main.tr('Lemmatization Lists - Slovak Lemma List'),
                'slv': main.tr('Lemmatization Lists - Slovenian Lemma List'),
                'spa': main.tr('spaCy - Spanish Lemmatizer'),
                'swe': main.tr('spaCy - Swedish Lemmatizer'),
                'tgl': main.tr('spaCy - Tagalog Lemmatizer'),
                'bod': main.tr('botok - Tibetan Lemmatizer'),
                'tur': main.tr('spaCy - Turkish Lemmatizer'),
                'ukr': main.tr('pymorphy2 - Morphological Analyzer'),
                'urd': main.tr('spaCy - Urdu Lemmatizer'),
                'cym': main.tr('Lemmatization Lists - Welsh Lemma List')
            },

            'preview_lang': 'eng',
            'preview_samples': '',
            'preview_results': ''

        },

        'stop_word_lists': {
            'stop_word_lists': {
                'afr': main.tr('spaCy - Afrikaans Stop Word List'),
                'akk': main.tr('CLTK - Akkadian Stop Word List'),
                'sqi': main.tr('spaCy - Albanian Stop Word List'),
                'amh': main.tr('spaCy - Amharic Stop Word List'),
                'ara': main.tr('spaCy - Arabic Stop Word List'),
                'arb': main.tr('CLTK - Arabic (Standard) Stop Word List'),
                'hye': main.tr('spaCy - Armenian Stop Word List'),
                'aze': main.tr('NLTK - Azerbaijani Stop Word List'),
                'eus': main.tr('spaCy - Basque Stop Word List'),
                'bel': main.tr('extra-stopwords - Belarusian Stop Word List'),
                'ben': main.tr('spaCy - Bengali Stop Word List'),
                'bre': main.tr('Stopwords ISO - Breton Stop Word List'),
                'bul': main.tr('spaCy - Bulgarian Stop Word List'),
                'cat': main.tr('spaCy - Catalan Stop Word List'),
                'zho_cn': main.tr('spaCy - Chinese (Simplified) Stop Word List'),
                'zho_tw': main.tr('spaCy - Chinese (Traditional) Stop Word List'),
                'cop': main.tr('CLTK - Coptic Stop Word List'),
                'hrv': main.tr('spaCy - Croatian Stop Word List'),
                'ces': main.tr('spaCy - Czech Stop Word List'),
                'dan': main.tr('spaCy - Danish Stop Word List'),
                'nld': main.tr('spaCy - Dutch Stop Word List'),
                'eng': main.tr('spaCy - English Stop Word List'),
                'enm': main.tr('CLTK - English (Middle) Stop Word List'),
                'ang': main.tr('CLTK - English (Old) Stop Word List'),
                'epo': main.tr('Stopwords ISO - Esperanto Stop Word List'),
                'est': main.tr('spaCy - Estonian Stop Word List'),
                'fin': main.tr('spaCy - Finnish Stop Word List'),
                'fra': main.tr('spaCy - French Stop Word List'),
                'fro': main.tr('CLTK - French (Old) Stop Word List'),
                'glg': main.tr('Stopwords ISO - Galician Stop Word List'),
                'deu': main.tr('spaCy - German Stop Word List'),
                'gmh': main.tr('CLTK - German (Middle High) Stop Word List'),
                'grc': main.tr('spaCy - Greek (Ancient) Stop Word List'),
                'ell': main.tr('spaCy - Greek (Modern) Stop Word List'),
                'guj': main.tr('spaCy - Gujarati Stop Word List'),
                'hau': main.tr('Stopwords ISO - Hausa Stop Word List'),
                'heb': main.tr('spaCy - Hebrew Stop Word List'),
                'hin': main.tr('CLTK - Hindi Stop Word List'),
                'hun': main.tr('spaCy - Hungarian Stop Word List'),
                'isl': main.tr('spaCy - Icelandic Stop Word List'),
                'ind': main.tr('spaCy - Indonesian Stop Word List'),
                'gle': main.tr('spaCy - Irish Stop Word List'),
                'ita': main.tr('spaCy - Italian Stop Word List'),
                'jpn': main.tr('spaCy - Japanese Stop Word List'),
                'kan': main.tr('spaCy - Kannada Stop Word List'),
                'kaz': main.tr('NLTK - Kazakh Stop Word List'),
                'kor': main.tr('spaCy - Japanese Stop Word List'),
                'kur': main.tr('Stopwords ISO - Kurdish Stop Word List'),
                'kir': main.tr('spaCy - Kyrgyz Stop Word List'),
                'lat': main.tr('CLTK - Latin Stop Word List'),
                'lav': main.tr('spaCy - Latvian Stop Word List'),
                'lij': main.tr('spaCy - Ligurian Stop Word List'),
                'lit': main.tr('spaCy - Lithuanian Stop Word List'),
                'ltz': main.tr('spaCy - Luxembourgish Stop Word List'),
                'mkd': main.tr('spaCy - Macedonian Stop Word List'),
                'msa': main.tr('Stopwords ISO - Malay Stop Word List'),
                'mal': main.tr('spaCy - Malayalam Stop Word List'),
                'mar': main.tr('spaCy - Marathi Stop Word List'),
                'omr': main.tr('CLTK - Marathi (Old) Stop Word List'),
                'mon': main.tr('extra-stopwords - Mongolian Stop Word List'),
                'nep': main.tr('spaCy - Nepali Stop Word List'),
                'non': main.tr('CLTK - Norse (Old) Stop Word List'),
                'nob': main.tr('spaCy - Norwegian Bokmål Stop Word List'),
                'nno': main.tr('NLTK - Norwegian Nynorsk Stop Word List'),
                'fas': main.tr('spaCy - Persian Stop Word List'),
                'pol': main.tr('spaCy - Polish Stop Word List'),
                'por': main.tr('spaCy - Portuguese Stop Word List'),
                'pan': main.tr('CLTK - Punjabi Stop Word List'),
                'ron': main.tr('spaCy - Romanian Stop Word List'),
                'rus': main.tr('spaCy - Russian Stop Word List'),
                'san': main.tr('CLTK - Sanskrit Stop Word List'),
                'srp_cyrl': main.tr('spaCy - Serbian (Cyrillic) Stop Word List'),
                'srp_latn': main.tr('spaCy - Serbian (Latin) Stop Word List'),
                'sin': main.tr('spaCy - Sinhala Stop Word List'),
                'slk': main.tr('spaCy - Slovak Stop Word List'),
                'slv': main.tr('spaCy - Slovenian Stop Word List'),
                'som': main.tr('Stopwords ISO - Somali Stop Word List'),
                'sot': main.tr('Stopwords ISO - Sotho (Southern) Stop Word List'),
                'spa': main.tr('spaCy - Spanish Stop Word List'),
                'swa': main.tr('Stopwords ISO - Swahili Stop Word List'),
                'swe': main.tr('spaCy - Swedish Stop Word List'),
                'tgl': main.tr('spaCy - Tagalog Stop Word List'),
                'tgk': main.tr('NLTK - Tajik Stop Word List'),
                'tam': main.tr('spaCy - Tamil Stop Word List'),
                'tat': main.tr('spaCy - Tatar Stop Word List'),
                'tel': main.tr('spaCy - Telugu Stop Word List'),
                'tha': main.tr('PyThaiNLP - Thai Stop Word List'),
                'tir': main.tr('spaCy - Tigrinya Stop Word List'),
                'tsn': main.tr('spaCy - Tswana Stop Word List'),
                'tur': main.tr('spaCy - Turkish Stop Word List'),
                'ukr': main.tr('spaCy - Ukrainian Stop Word List'),
                'urd': main.tr('spaCy - Urdu Stop Word List'),
                'vie': main.tr('spaCy - Vietnamese Stop Word List'),
                'yor': main.tr('spaCy - Yoruba Stop Word List'),
                'zul': main.tr('Stopwords ISO - Zulu Stop Word List'),

                'other': main.tr('Custom List')
            },

            'custom_lists': {
                'afr': [],
                'akk': [],
                'sqi': [],
                'amh': [],
                'ara': [],
                'arb': [],
                'hye': [],
                'aze': [],
                'eus': [],
                'bel': [],
                'ben': [],
                'bre': [],
                'bul': [],
                'cat': [],
                'zho_cn': [],
                'zho_tw': [],
                'cop': [],
                'hrv': [],
                'ces': [],
                'dan': [],
                'nld': [],
                'eng': [],
                'enm': [],
                'ang': [],
                'epo': [],
                'est': [],
                'fin': [],
                'fra': [],
                'fro': [],
                'glg': [],
                'deu': [],
                'gmh': [],
                'grc': [],
                'ell': [],
                'guj': [],
                'hau': [],
                'heb': [],
                'hin': [],
                'hun': [],
                'isl': [],
                'ind': [],
                'gle': [],
                'ita': [],
                'jpn': [],
                'kan': [],
                'kaz': [],
                'kor': [],
                'kur': [],
                'kir': [],
                'lat': [],
                'lav': [],
                'lij': [],
                'lit': [],
                'ltz': [],
                'mkd': [],
                'msa': [],
                'mal': [],
                'mar': [],
                'omr': [],
                'mon': [],
                'nep': [],
                'non': [],
                'nob': [],
                'nno': [],
                'fas': [],
                'pol': [],
                'por': [],
                'pan': [],
                'ron': [],
                'rus': [],
                'san': [],
                'srp_cyrl': [],
                'srp_latn': [],
                'sin': [],
                'slk': [],
                'slv': [],
                'som': [],
                'sot': [],
                'spa': [],
                'swa': [],
                'swe': [],
                'tgl': [],
                'tgk': [],
                'tam': [],
                'tat': [],
                'tel': [],
                'tha': [],
                'tir': [],
                'tsn': [],
                'tur': [],
                'ukr': [],
                'urd': [],
                'vie': [],
                'yor': [],
                'zul': [],
                
                'other': []
            },

            'preview_lang': 'eng',
        },

        'measures': {
            'dispersion': {
                'general': {
                    'number_sections': 5
                }
            },

            'adjusted_freq': {
                'general': {
                    'number_sections': 5,
                    'use_same_settings_dispersion': True
                }
            },

            'statistical_significance': {
                'z_score': {
                    'direction': 'Two-tailed'
                },

                'students_t_test_2_sample': {
                    'number_sections': 5,
                    'use_data': main.tr('Relative Frequency'),
                    'variances': main.tr('Equal'),
                },

                'pearsons_chi_squared_test': {
                    'apply_correction': True
                },

                'fishers_exact_test': {
                    'direction': main.tr('Two-tailed')
                },

                'mann_whitney_u_test': {
                    'number_sections': 5,
                    'use_data': main.tr('Relative Frequency'),
                    'direction': main.tr('Two-tailed'),
                    'apply_correction': True
                }
            },

            'effect_size': {
                'kilgarriffs_ratio': {
                    'smoothing_param': 1.00
                }
            }
        },

        'figs': {
            'line_chart': {
                'font': 'Arial'
            },

            'word_cloud': {
                'font': 'Code2000',
                'bg_color': '#FFFFFF'
            },

            'network_graph': {
                'layout': 'Spring',
                'node_font': 'Arial',
                'node_font_size': 10,
                'edge_font': 'Arial',
                'edge_font_size': 8,
                'edge_color': '#5C88C5'
            }
        }
    }
