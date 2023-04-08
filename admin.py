from ggapi import GoldengateRestApiHelper
import argparse
import yaml
import logging.config
import logging

with open("conf/logging.yaml",  "r") as f:
    yaml_config = yaml.safe_load(f.read())
    logging.config.dictConfig(yaml_config)

log = logging.getLogger(__name__) 

def get_deployment_config(deployment_name):
    with open('./conf/config.yml', 'r') as f:
        config = yaml.safe_load(f)
        for deployment in config['deployments']:
            if deployment['deployment'] == deployment_name:
                return deployment
    return None

def main():
    parser = argparse.ArgumentParser(description='GoldenGate API CLI')
    parser.add_argument('-d', '--deployment', type=str, required=True, help='Name of the deployment')
    parser.add_argument('-e', '--extract_name', type=str, help='Name of the extract process')
    parser.add_argument('-r', '--replicat_name', type=str, help='Name of the replicat process')
    parser.add_argument('--Monitor-Deployment', action='store_true', help='Start an extract')
    parser.add_argument('--start-extract', action='store_true', help='Start an extract')
    parser.add_argument('--stop-extract', action='store_true', help='Stop an extract')
    parser.add_argument('--start-replicat', action='store_true', help='Start a replicat')
    parser.add_argument('--stop-replicat', action='store_true', help='Stop a replicat')
    parser.add_argument('--list-extracts', action='store_true', help='List all extracts')
    parser.add_argument('--list-replicats', action='store_true', help='List all replicats')
    parser.add_argument('--extract-status', action='store_true', help='Get status of an extract')
    parser.add_argument('--extract-details', action='store_true', help='Get details of an extract')
    parser.add_argument('--replicat-status', action='store_true', help='Get status of a replicat')
    parser.add_argument('--replicat-details', action='store_true', help='Get details of a replicat')
    parser.add_argument('--view-extract-report', action='store_true', help='View extract report file')
    parser.add_argument('--view-replicat-report', action='store_true', help='View replicat report file')
    args = parser.parse_args()

    deployment_config = get_deployment_config(args.deployment)
    if not deployment_config:
        print(f'Deployment "{args.deployment}" not found in config')
        return

    ggr = GoldengateRestApiHelper(deployment_config['baseURL'], deployment_config['username'],deployment_config['password']) 


    if args.start_extract:
        messages=ggr.start_extract(args.extract_name)
        log.debug(messages)
        for mess in messages['messages']:
            log.info(mess['title'])
    elif args.stop_extract:
        messages=ggr.stop_extract(args.extract_name)
        log.debug(messages)
        for mess in messages['messages']:
            log.info(mess['title'])
    elif args.start_replicat:
        messages=ggr.start_replicat(args.replicat_name)
        log.debug(messages)
        for mess in messages['messages']:
            log.info(mess['title'])
    elif args.stop_replicat:
        messages=ggr.stop_replicat(args.replicat_name)
        log.debug(messages)
        for mess in messages['messages']:
            log.info(mess['title'])
    elif args.list_extracts:
        messages=ggr.list_extracts()
        log.debug(messages)
    elif args.list_replicats:
        messages=ggr.list_replicats()
        log.debug(messages)
    elif args.extract_status:
        messages=ggr.get_extract_status(args.extract_name)
        log.debug(messages)
    elif args.extract_details:
        messages=ggr.get_extract_details(args.extract_name)
        log.debug(messages)
    elif args.replicat_status:
        messages=ggr.get_replicat_status(args.replicat_name)
        log.debug(messages)
    elif args.replicat_details:
        messages=ggr.get_replicat_details(args.replicat_name)
        log.debug(messages)
    elif args.view_extract_report:
        ggr.view_extract_report_file(args.extract_name)
    elif args.view_replicat_report:
        ggr.view_replicat_report_file(args.replicat_name)
    else:
        ggr.monitor_deployment()

if __name__ == '__main__':
    main()