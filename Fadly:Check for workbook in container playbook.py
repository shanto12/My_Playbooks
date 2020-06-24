"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'Format_data_to_get_workflow_name' block
    Format_data_to_get_workflow_name(container=container)

    return

"""
Format data to get workflow_name
"""
def Format_data_to_get_workflow_name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('Format_data_to_get_workflow_name() called')
    
    template = """/container?_filter_id={0}&_filter_workflow_name=\"\""""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Format_data_to_get_workflow_name")

    Get_workflow_name(container=container)

    return

"""
Get workflow_name
"""
def Get_workflow_name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('Get_workflow_name() called')

    # collect data for 'Get_workflow_name' call
    formatted_data_1 = phantom.get_format_data(name='Format_data_to_get_workflow_name')

    parameters = []
    
    # build parameters list for 'Get_workflow_name' call
    parameters.append({
        'headers': "",
        'location': formatted_data_1,
        'verify_certificate': False,
    })

    phantom.act("get data", parameters=parameters, assets=['http01'], callback=Check_if_container_already_have_workbook, name="Get_workflow_name")

    return

"""
Check if container already have workbook
"""
def Check_if_container_already_have_workbook(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('Check_if_container_already_have_workbook() called')

    # check for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        action_results=results,
        conditions=[
            ["Get_workflow_name:action_result.data.*.response_body.count", ">", 0],
        ])

    # call connected blocks if condition 1 matched
    if matched_artifacts_1 or matched_results_1:
        Comment_Container_has_no_workbook(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        action_results=results,
        conditions=[
            ["Get_workflow_name:action_result.data.*.response_body.count", "==", 0],
        ])

    # call connected blocks if condition 2 matched
    if matched_artifacts_2 or matched_results_2:
        Comment_Container_has_a_workbook(action=action, success=success, container=container, results=results, handle=handle)
        return

    return

"""
Comment Container has a workbook
"""
def Comment_Container_has_a_workbook(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('Comment_Container_has_a_workbook() called')

    phantom.comment(container=container, comment="Container has no workbook, proceed to add workbook.")

    return

"""
Comment Container has no workbook
"""
def Comment_Container_has_no_workbook(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('Comment_Container_has_no_workbook() called')

    phantom.comment(container=container, comment="Container has a workbook.")

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