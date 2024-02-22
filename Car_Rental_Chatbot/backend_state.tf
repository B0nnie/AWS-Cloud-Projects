# Backend State Bucket in Google
resource "google_storage_bucket" "state_bucket" {
  name                        = "${var.project_name}-tfstate"
  force_destroy               = false
  location                    = var.region
  storage_class               = "STANDARD"
  public_access_prevention    = "enforced"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    condition {
      num_newer_versions = 2 # Keep a maximum of 2 versions
      age                = 7 # Expire noncurrent versions after 7 days
    }
    action {
      type = "Delete"
    }
  }
}