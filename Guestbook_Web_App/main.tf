# VPC
resource "aws_vpc" "VPC" {
  cidr_block                       = "10.0.0.0/27"
  instance_tenancy                 = "default"
  assign_generated_ipv6_cidr_block = false

  tags = {
    Name    = "forGuestbook"
    project = var.project_tag
  }
}

# Subnet for EC2 Group 1
resource "aws_subnet" "EC2_web1" {
  vpc_id            = aws_vpc.VPC.id
  availability_zone = "us-east-1a"
  cidr_block        = "10.0.0.0/28"

  tags = {
    Name    = "Guestbook-Web-1"
    project = var.project_tag
  }
}

# Subnet for EC2 Group 2
resource "aws_subnet" "EC2_web2" {
  vpc_id            = aws_vpc.VPC.id
  availability_zone = "us-east-1b"
  cidr_block        = "10.0.0.16/28"

  tags = {
    Name    = "Guestbook-Web-2"
    project = var.project_tag
  }
}

# Security Group for EC2s
resource "aws_security_group" "EC2_security_group" {
  name        = "WebServerGroup"
  description = "TBD"
  vpc_id      = aws_vpc.VPC.id

  tags = {
    Name    = "WebServerGroup"
    project = var.project_tag
  }
}

# EC2 instances for web server
data "aws_ami" "amazon_linux_2023" {
  owners             = ["amazon"]
  include_deprecated = false

  filter {
    name   = "name"
    values = ["al2023-ami-2023.4.20240319.1-kernel-6.1-x86_64"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "web_server_1" {
  ami                         = data.aws_ami.amazon_linux_2023.id
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.EC2_web1.id
  vpc_security_group_ids      = [aws_security_group.EC2_security_group.id]
  key_name                    = var.key_name
  associate_public_ip_address = true
  #user_data = file("")

  tags = {
    Name    = "Web-Server-1"
    project = var.project_tag
  }
}

resource "aws_instance" "web_server_2" {
  ami                         = data.aws_ami.amazon_linux_2023.id
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.EC2_web2.id
  vpc_security_group_ids      = [aws_security_group.EC2_security_group.id]
  key_name                    = var.key_name
  associate_public_ip_address = true
  #user_data = file("")

  tags = {
    Name    = "Web-Server-2"
    project = var.project_tag
  }
}