*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${Base_URL}    https://69b675b7583f543fbd9dc80a.mockapi.io//
${student_id}  7


*** Test Cases ***
TC002_Fetch_Student_details_by_ID
    Create Session    alias=FetchDetail  url=${Base_URL}
    ${response}=  GET On Session    FetchDetail    testproject/users/${student_id}
    ${actual result}=  Convert To String  ${response.status_code}
    Should Be Equal  first=${actual result}  second=200
    ${json_resp}=  Set Variable  ${response.json()}
    @{name_list}=  Get Value From Json  ${json_resp}  name
    ${name}=  Get From List  ${name_list}  0
    Should Be Equal  ${name}  Terry Update

