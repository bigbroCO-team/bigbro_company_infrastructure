resource "aws_ecr_repository" "bigbro-ecr" {
  name                 = "bigbro-ecr"
  image_tag_mutability = "MUTABLE"

  tags = {
    Name    = "bigbro-ecr"
    Project = var.project_name
  }
}