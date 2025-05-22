resource "aws_s3_bucket" "bigbro-company-bucket" {
  bucket = "bigbro-company-bucket"

  tags = {
    Name    = "bigbro-company-bucket"
    Project = var.project_name
  }
}