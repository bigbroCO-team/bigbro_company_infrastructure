resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.bigbro-alb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_alb_target_group.bigbro-stage-tg.arn
  }
}
