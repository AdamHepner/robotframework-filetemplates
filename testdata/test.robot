*** Settings ***
Library  filetemplates.FileTemplates

*** Variables ***
&{args}  who="World"

*** Test Cases ***
Sample  Render Template  testdata/template.tpl  ${OUTPUTDIR}/output.py  &{args}