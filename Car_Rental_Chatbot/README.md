## Amazon Lex Chatbot with Slack Integration
Play around with the chatbot [here](https://join.slack.com/t/carrentalchatbot/shared_invite/zt-2e5b022o4-6PjMYAmgAN6xwnm7f83Raw)! (Use a temporary email address for privacy.)

A cloud-based solution for a car rental chatbot using Amazon Lex V2, Slack integration, and a GitHub Actions CI/CD pipeline. The infrastructure was set up on AWS and GCP with Terraform and CloudFormation, which included creating the Lex bot (and its aliases and versions) and configuring a remote Terraform backend in GCP Cloud Storage for built-in locking of the state file. A Slack app was created with the Slack API, and a channel integration was configured via the AWS console for communication between the Slack app and the Lex chatbot. With GitHub Actions, a CI/CD workflow was established where pushed changes trigger automated tests followed by deployment to AWS upon tests passing. The project files are [here](https://github.com/B0nnie/AWS-Cloud-Projects/tree/main/Car_Rental_Chatbot).

<br>

![Amazon Lex Diagram](https://github.com/B0nnie/AWS-Cloud-Projects/assets/10394696/877406ab-98c3-4993-b7a3-7af5285accdb)
