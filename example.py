import ggapi as gg
'''
This example will get a list ofextracts and replicats and ppost the stat and current stats to console
'''
for extract in gg.list_extracts()['response']['items']:
    extract_name = extract['name']
    e_status=gg.get_extract_status(extract_name)['response']
    e_statistics=gg.get_extract_Stats(extract_name)['response']

    print(f"\tExtract: {extract_name} \tstatus: {e_status['status']} \tInserts: {e_statistics['mappedTotalInserts']} \tUpdates: {e_statistics['mappedTotalUpdates']}\tDeletes: {e_statistics['mappedTotalUpdates']} \tLast Started: {e_status['lastStarted']}")

for replicat in gg.list_replicats()['response']['items']:
    replicat_name = replicat['name']
    r_status=gg.get_replicat_status(replicat_name)['response']
    r_statistics=gg.get_replicat_Stats(replicat_name)['response']

    print(f"\tReplicat: {replicat_name} \tstatus: {r_status['status']} \tInserts: {r_statistics['mappedTotalInserts']} \tUpdates: {r_statistics['mappedTotalUpdates']}\tDeletes: {r_statistics['mappedTotalUpdates']} \tLast Started: {r_status['lastStarted']}")


