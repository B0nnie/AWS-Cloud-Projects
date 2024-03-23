# Backend State Bucket in AWS
resource "aws_s3_bucket" "state_bucket" {
  bucket = "guestbook-web-app-state-bucket-32324"

  tags = {
    project = var.project_tag
  }
}

resource "aws_s3_bucket_public_access_block" "state_bucket_block_public_access" {
  bucket = aws_s3_bucket.state_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "state_bucket_versioning" {
  bucket = aws_s3_bucket.state_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "state_bucket_encryption" {
  bucket = aws_s3_bucket.state_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# State locking with DynamoDB
resource "aws_dynamodb_table" "terraform_state_lock" {
  name           = "GuestbookWebAppStateLocking"
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "LockID"
  table_class    = "STANDARD"

  attribute {
    name = "LockID"
    type = "S"
  }

  server_side_encryption {
    enabled = false
  }

  deletion_protection_enabled = true

  tags = {
    project = var.project_tag
  }
}

