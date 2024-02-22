terraform {
  backend "gcs" {
    bucket = "carrentalchatbot-tfstate"
    prefix = "terraform/state"
  }
}