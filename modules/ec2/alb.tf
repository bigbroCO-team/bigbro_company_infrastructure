resource "aws_lb" "bigbro-alb" {
  name               = "bigbro-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.bigbro-alb-sg.id]
  subnets = [
    var.public_subnet_1_id,
    var.public_subnet_2_id
  ]

  enable_deletion_protection = false

  tags = {
    Name    = "bigbro-alb"
    Project = var.project_name
  }
}
