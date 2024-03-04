# AWS IAM Role for LexV2 Chatbot
resource "aws_iam_role" "lex_bot_role" {
  name = "LexV2BotRole"
  tags = {
    name = var.project_name
  }

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lexv2.amazonaws.com"
      },
      "Effect": "Allow"
    }
  ]
}
EOF
}

data "aws_iam_policy" "lex_v2_bot_policy" {
  name = "AmazonLexFullAccess"
}

# Attach the AmazonLexFullAccess AWS managed policy to IAM LexV2 Chatbot role
resource "aws_iam_role_policy_attachment" "lex_bot_policy" {
  role       = aws_iam_role.lex_bot_role.name
  policy_arn = data.aws_iam_policy.lex_v2_bot_policy.arn
}

# Link to CloudFormation LexV2 chatbot template
resource "aws_cloudformation_stack" "lexv2_chatbot_template" {
  name = "${var.project_name}-cf"
  #parameters = var.parameters
  #capabilities = var.capabilities 
  template_body = file(var.template_file_path)

  tags = {
    name = var.project_name
  }
}