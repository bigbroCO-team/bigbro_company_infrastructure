resource "aws_alb_target_group" "bigbro-stage-tg" {
  name        = "bigbro-stage-tg"
  port        = 80
  protocol    = "HTTP"
  vpc_id      = var.bigbro_vpc_id
  target_type = "ip"

  health_check {
    path                = "/health"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
    matcher             = "200"
  }

  tags = {
    Name    = "bigbro-stage-tg"
    Project = var.project_name
  }
}
