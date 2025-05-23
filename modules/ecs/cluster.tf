resource "aws_ecs_cluster" "bigbro-cluster" {
  name = "bigbro-cluster"

  tags = {
    Name    = "bigbro-cluster"
    Project = var.project_name
  }
}