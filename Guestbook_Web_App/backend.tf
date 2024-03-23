# Remote backend in AWS S3 with DynamoDB state locking
terraform {
  backend "s3" {
    bucket         = "guestbook-web-app-state-bucket-32324"
    key            = "terraform/state"
    region         = "us-east-1"
    dynamodb_table = "GuestbookWebAppStateLocking"
  }
}