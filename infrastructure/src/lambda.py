from troposphere import Template, Output, Ref, GetAtt, Parameter, Join, Export
from troposphere.constants import NUMBER, STRING
from troposphere.awslambda import Function, Code, MEMORY_VALUES, EventSourceMapping, Alias, Environment
from troposphere.iam import Role, Policy

FUNCTION_NAME="ibrowseMainFunction"

template = Template()

template.set_description("Main lambda called from ibrowse UI")

pythonLayer = template.add_parameter(Parameter(
    "PythonLayer",
    Default="arn:aws:lambda:eu-west-1:399891621064:layer:AWSLambda-Python37-SciPy1x:37",
    Description="ARN of AWS Python Lambda Layer",
    Type="String",
))

ibrowseMainFunction = template.add_resource(Function(
    FUNCTION_NAME,
    FunctionName=FUNCTION_NAME,
    Description="Lambda returns next recommended product to show to end user",
    Handler="index.lambda_handler",
    Layers=[
        Ref(pythonLayer)
    ],
    Runtime="python3.7",
))

print(template.to_json())