import boto3

# Get the service resource.
session = boto3.session.Session(profile_name='when2lift_iam')
dynamodb = session.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('when2lift')
#table.meta.client.get_waiter('table_exists').wait(TableName='when2lift')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
print(table.creation_date_time)
table.put_item(
   Item={
   		'id' : '2',
        'time': '0',
        'location': 'pit',
        'occupants': 0,
    }
)
