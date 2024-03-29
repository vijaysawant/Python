# coding=utf-16BE
from langdetect import detect
# import cld3
import json

def dump_translation_statistics(stat_dictionary, file_name = None):
    if file_name is None:
        file_name = "translations_stats.txt"
    file_descriptor = open(file_name, "w+")
    json.dump(stat_dictionary, file_descriptor, ensure_ascii=False)
    print("[Info] Dump dictionary into file '{}'".format(file_name))
    # print("[Info] : Dict data - {}\n".format(stat_dictionary))
    file_descriptor.close()

def load_translation_statisics(stat_dictionary = None, file_name = None):
    if file_name is None:
        file_name = "translations_stats.txt"
    file_descriptor = open(file_name, "r")
    stat_dictionary = json.load(file_descriptor)
    file_descriptor.close()
    print("[Info] Load dictionary from file '{}'".format(file_name))
    return stat_dictionary

statistics = {"Non-translated":{}, "Translated":{}}

def check_page_translation(Input_data = None):
    global statistics
    locale_value = "ja-JP"
    target_lang = None
    translated = 0
    not_translated = 0
    data = []
    foo = open("translations.txt", "a")
    if type(Input_data) == str:
        # import pdb;pdb.set_trace()
        data = Input_data.split("\n")
    else:
        data = Input_data
    for line in data:
        if line in ('/', '×') or line.isdigit() or line.isnumeric(): continue
        foo.write(str(line))
        text = line.strip()
        target_lang = detect(text)
        # target_lang1 = cld3.get_language(text)
        print("Locale1: {0}\tString: {1}".format(target_lang, text))
        if target_lang in locale_value:
            statistics["Translated"][text] = target_lang
            translated += 1
        else:
            statistics["Non-translated"][text] = target_lang
            not_translated += 1

    foo.close()
    dump_translation_statistics(stat_dictionary=statistics)
    print("Translated: {}\tNon-translated {}".format(
        len(statistics["Translated"]),
        len(statistics["Non-translated"]))
        )
    statistics = load_translation_statisics()
    # print("statistics: ",statistics)

def check_string_translations():
    global statistics, locale_value, target_lang
    translated = 0
    not_translated = 0
    foo = open("translations.txt", "a+")
    for line in mix_data:
        foo.write(str(line))
        text = line.strip()
        target_lang = detect(text)
        print("Locale: {0}\tString: {1}".format(target_lang, text))
        if target_lang in locale_value:
            statistics["Translated"][text] = locale_value
            translated += 1
        else:
            statistics["Non-translated"][text] = locale_value
            not_translated += 1

    foo.close()
    dump_translation_statistics(stat_dictionary=statistics)
    print("Translated: {}\tNon-translated {}".format(
            len(statistics["Translated"]),
            len(statistics["Non-translated"])))
    statistics = load_translation_statisics()
    print("statistics: ",statistics)

if __name__ == "__main__":
    statistics = {"Non-translated": {}, "Translated": {}}
    data = ['ようこそ\n', 'バージョン 6.11.0 Beta\n', 'アカウントにログイン\n', 'ログイン']
    # data1 = ["Then\n", "verify\n", "Satellite\n", "ログイン\n"]
    mix_data = ['ようこそ\n', 'バージョン 6.11.0 Beta\n', "Satellite\n", "login screen\n"]
    # data2 = 'ようこそ\nバージョン 6.11.0 Beta\nアカウントにログイン\nログイン'
    data1 = ["_Satellite_\n", "_1_ログイン_1_\n"]
    data2 = '_2_ようこそ_2_\n_3_バージョン_3_\n'
    data3 = ['_2_ようこそ_2_\n', '_1_ログイン_1_\n']
    live_data = '概要\n0 selections\n/\n  生成日: Jul 14, 5:20 PM\n管理\nドキュメント\n×\nAll のホスト設定のステータス\n  エラーなしで変更を実行したホスト\n0\n  エラー状態のホスト\n0\n  れのあるホスト\n0\n  レポートのないホスト\n0\n  警告が無効にされているホスト\n0\nホストの合計数: 0 台\n×\nAll のホスト設定チャート\n利用可能なデータはありません\n×\nAnsib分 間に報告された良好なホスト\n0\n  保留中の変更があるホスト\n0\n  同期にずれのあるホスト\n0\n  レポートのないホスト\n0\n  警告が無効にされているホスト\n0\nホストの合計数\n  エラーなしで変更を実行したホスト\n0\n  エラー状態のホスト\n0\n  直近 30分 間に報告された良好なホスト\n0\n  保留中の変更があるホスト\n0\n  同期にずれのあるホスト\n0\n ト設定チャート\n利用可能なデータはありません\n×\nPuppet の実行分布の表\n分前\n30\n27\n24\n21\n18\n15\n12\n9\n6\n3\nクライアント数\n×\nAnsible の実行分布の表\n分前\n30\n27ベント\n関連するレポートを過去一週間受信していません\n×\n新規ホスト\n利用可能なホストがありません\n×\nビルドモードのホストまたはビルドエラーのあるホスト\nビルドモードのホ hours ago\nscheduled pending 28 N/A\nstopped error 471 12 hours ago\n×\n最新の警告/エラータスク\n名前 状態 結果 開始済み\nInsights scheduled sync stopped error 12 hours ed sync stopped error 12 hours ago\nInsights scheduled sync stopped error 12 hours ago\nInsights scheduled sync stopped error 12 hours ago\nInsights scheduled sync stopped error 12 hours ago\n×\n0 Discovered Host\n検出されたホストがありません\n×\n最新コンプライアンスレポート\nレポートがありません\n×\nコンプライアンスレポートの内訳\n利用可who 設定ステータス\n設定ステータス 数量\nレポートがありません 0\nNo Change 0\nOK 0\n合計の設定 0\nLatest Configurations Without Change\n設定が見つかりません\n×\nLatest Ernコンテンツビュー\nコンテンビューの履歴イベントが見つかりません。\n×\n同期の概要\nNo recently synced products\n×\nHost Subscription Status\n数量\n Invalid 0\n Partial 0\n Unknown or Unregistered 0\nTotal Content Hosts\n0\n×\nSubscription Status\nSubscription Status 数量\nActive Subscriptions 1\nSubscriptions Expiring in 120 Days 0\nRecent Expired Subscriptions 0\n×\nホストコレクション\nホストコレクションが見つかりません'
    live_data2 = ['概要', '0 s14, 11:34 PM', '×', '0', '  エラー状態のホスト', '0', '  直近 30分 間に報告さト', '0', '  レポートのないホスト', '0', '  警告が無効にされているホスト', '0', 'ホストの合計数: 0 台', '×', 'All のホスト設定チャート', '利用可能なデータはありません', ' エラー状態のホスト', '0', '  直近 30分 間に報告された良好なホスト', '0', '  保留中の変更があるホスト', '0', '  同期にずれのあるホスト', '0', '  レポートのないホスト', '0のホスト設定チャート', '利用可能なデータはありません', '×', 'Puppet のホスト設定のステータス', '  エラーなしで変更を実行したホスト', '0', '  エラー状態のホスト', '0', '  るホスト', '0', '  レポートのないホスト', '0', '  警告が無効にされているホスト', '0', 'ホストの合計数: 0 台', '×', 'Puppet のホスト設定チャート', '利用可能なデータはありま', '18', '15', '12', '9', '6', '3', 'クライアント数', '×', 'Ansible の実行分布の表', '分前', '30', '27', '24', '21', '18', '15', '12', '9', '6', '3', 'クライアント数', '×','一週間受信していません', '×', '新規ホスト', '利用可能なホストがありません', '×', 'ビルドモードのホストまたはビルドエラーのあるホスト', 'ビルドモードのホストも、ビルドエラ6 18 hours ago', 'scheduled pending 28 N/A', 'stopped error 471 18 hours ago', '×', '最新の警告/エラータスク', '名前 状態 結果 開始済み', 'Insights scheduled sync stopped ','Insights scheduled sync stopped error 18 hours ago', 'Insights scheduled sync stopped error 18 hours ago', 'Insights scheduled sync stopped error 18 hours ago', 'Insights scheduled sync stopped error 18 hours ago', '×', '0 Discovered Host', '検出されたホストがありません', '×', '最新コンプライアンスレポート', 'レポートがありません', '×','×', 'Latest Jobs', 'No jobs available', '×', 'Virt-who 設定ステータス', '設定ステータス 数量', 'レポートがありません 0', 'No Change 0', 'OK 0', '合計の設定 0', 'Latest C','設定が見つかりません', '×', 'Latest Errata', '登録済みコンテンツホストへの適用が必要なエラータはありません。', '×', 'コンテンツビュー', 'コンテンビューの履歴イベントが見', 'Host Subscription Status', '数量', ' Invalid 0', ' Partial 0', ' Valid 0', ' Unsubscribed Hypervisor 0', ' Unknown or Unregistered 0', 'Total Content Hosts', '0', '×','Subscription Status', 'Subscription Status 数量', 'Active Subscriptions 1', 'Subscriptions Expiring in 120 Days 0', 'Recently Expired Subscriptions 0', '×', 'ホストコレクホストコレクションが見つかりません']

    import pdb;pdb.set_trace()
    print("Data 1 ----------\n", data1)
    check_page_translation(Input_data=live_data)
    # import pdb; pdb.set_trace()

    # print("Data 2 ----------\n",data2)
    # check_page_translation(Input_data=data2)
