"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'filter_1' block
    filter_1(container=container)

    return

def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('filter_1() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.name", "==", "Email Artifact"],
        ],
        name="filter_1:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        custom_function_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def custom_function_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('custom_function_1() called')
    filtered_artifacts_data_1 = phantom.collect2(container=container, datapath=['filtered-data:filter_1:condition_1:artifact:*.cef.bodyHtml'])
    filtered_artifacts_item_1_0 = [item[0] for item in filtered_artifacts_data_1]

    custom_function_1__text_from_body_html = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(filtered_artifacts_item_1_0[0])
    custom_function_1__text_from_body_html = soup.get_text()
    phantom.debug(custom_function_1__text_from_body_html)

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key='custom_function_1:text_from_body_html', value=json.dumps(custom_function_1__text_from_body_html))

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return