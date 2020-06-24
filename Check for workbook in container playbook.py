"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'FB_REST_Get_WorkFlow_Name' block
    FB_REST_Get_WorkFlow_Name(container=container)

    return

"""
Format data to get workflow_name
"""
def FB_REST_Get_WorkFlow_Name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('FB_REST_Get_WorkFlow_Name() called')
    
    template = """/container?_filter_id={0}&_filter_workflow_name=\"\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="FB_REST_Get_WorkFlow_Name")

    REST_GET_Get_WorkFlow_Name(container=container)

    return

"""
Get workflow_name
"""
def REST_GET_Get_WorkFlow_Name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('REST_GET_Get_WorkFlow_Name() called')

    # collect data for 'REST_GET_Get_WorkFlow_Name' call
    formatted_data_1 = phantom.get_format_data(name='FB_REST_Get_WorkFlow_Name')

    parameters = []
    
    # build parameters list for 'REST_GET_Get_WorkFlow_Name' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act("get data", parameters=parameters, assets=['http01'], callback=DB_Container_Has_Workbook, name="REST_GET_Get_WorkFlow_Name")

    return

"""
Check if container already have workbook
"""
def DB_Container_Has_Workbook(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('DB_Container_Has_Workbook() called')

    # check for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        action_results=results,
        conditions=[
            ["REST_GET_Get_WorkFlow_Name:action_result.data.*.response_body.count", ">", 0],
        ])

    # call connected blocks if condition 1 matched
    if matched_artifacts_1 or matched_results_1:
        API_Comment_Has_Workbook_No(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        action_results=results,
        conditions=[
            ["REST_GET_Get_WorkFlow_Name:action_result.data.*.response_body.count", "==", 0],
        ])

    # call connected blocks if condition 2 matched
    if matched_artifacts_2 or matched_results_2:
        API_Comment_Has_Workbook_Yes(action=action, success=success, container=container, results=results, handle=handle)
        return

    return

"""
Comment Container has a workbook
"""
def API_Comment_Has_Workbook_Yes(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('API_Comment_Has_Workbook_Yes() called')

    phantom.comment(container=container, comment="Container has a workbook, proceed to add workbook.")

    return

"""
Comment Container has no workbook
"""
def API_Comment_Has_Workbook_No(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('API_Comment_Has_Workbook_No() called')

    phantom.comment(container=container, comment="Container doesn't have a workbook.")

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