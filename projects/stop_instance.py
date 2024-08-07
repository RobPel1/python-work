from awscode import listInstances,stopInstance

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}
#qa_filter = {'Name': 'tag:env', 'Values': ['qa']}
#prod_filter = [{'Name': 'tag:env', 'Values': ['prod']}]

instances = listInstances(dev_filter)
stopInstance(instances)

