  data "aws_cloudformation_stack" "lexv2_chatbot_template" {
  name = "lexv2_chatbot_template"
}

#Check that CloudFormation template exists
run "check_cf_template_exists" {



  command = plan

  assert {
    condition     = can(data.aws_cloudformation_stack.lexv2_chatbot_template.template_body)
    error_message = "Template body is missing"
  }

}

#Check that correct CloudFormation template body is referenced
run "check_cf_template_body" {

  command = plan

  assert {
    condition     = var.template_file_path == "lexv2chatbot_cf.yml"
    error_message = "Incorrect template body was used"
  }
}


#Check that CloudFormation template name hasn't changed
run "check_cf_template_name" {

  command = plan

  assert {
    condition     = data.aws_cloudformation_stack.lexv2_chatbot_template.name == "${var.project_name}-cf"
    error_message = "Template name changed"
  }
}