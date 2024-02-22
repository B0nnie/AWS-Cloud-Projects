![AWS Cloud Projects README Banner Gif (1)](https://github.com/B0nnie/AWS-Cloud-Projects/assets/10394696/8ab9d2cb-6cdc-44c1-9b9e-027fb6d98bd3)

<h3 align="center">
<em>A collection of cloud projects using the latest and greatest from AWS.</em>
</h3>
<br>
<br>

# Projects

## • Cloud Resume Challenge
Visit the live webpage here: [cloudresumechallenge.csr4w.com](https://www.cloudresumechallenge.csr4w.com/)

A web-based resume page written in HTML and styled with CSS, deployed as a static website on Amazon S3 with HTTPS security implemented via CloudFront. The webpage features a visitor counter, which utilizes both DynamoDB for data storage/retrieval and an API built with AWS API HTTP Gateway and Lambda to communicate with the database. This project's infrastructure was defined using AWS Serverless Application Model (SAM) and is managed with a GitHub Actions CI/CD pipeline for both [back-end and front-end code](https://github.com/B0nnie/AWS-Cloud-Projects/tree/main/Cloud_Resume_Challenge). Here are The Cloud Resume Challenge instructions: [cloudresumechallenge.dev/docs/the-challenge/aws/](https://cloudresumechallenge.dev/docs/the-challenge/aws/) 

<br>

![Cloud Resume Challenge Diagram](https://github.com/B0nnie/AWS-Cloud-Projects/assets/10394696/dbddf085-29cd-42e0-8091-f6ca9cfde2d7)


<br>

# Tech Stack

- Cloud Providers: AWS, GCP
- Deployments: Serverless
- Infrastructure as Code (IaC) tools: Serverless Application Model (SAM), CloudFormation, Terraform
- CI/CD: GitHub Actions
- Databases: DynamoDB
- Languages: Python, JavaScript, YAML, HTML, CSS, HashiCorp Configuration Language (HCL)

