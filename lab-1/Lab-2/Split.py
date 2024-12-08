new = "hai this is Thara Akshaya and i am from chittor"
data = new.split( )
print("Words:", data)
print(new.split( )[1])

arn = "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0e9801d129EXAMPLE"
new_arn = arn.split("/")
print(new_arn)
print(arn.split("/")[1])

ARN = "arn:aws:sns:us-east-1:123456789012:example-sns-topic-name"
New_arn = ARN.split(":")
print(New_arn)
print(ARN.split(":")[1])
